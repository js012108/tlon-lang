import sys
import math
from numpy import arange
from inspect import signature, _empty, isbuiltin
from importlib import import_module

from .TLONParser import TLONParser
from .TLONVisitor import TLONVisitor

from .structures import *

sys.setrecursionlimit(100000)
sys.path.append('/src/lib')
from mas.__init__ import *

class Visitor(TLONVisitor):
  memory_manager = None
  value_returned = False
  line_error = -1

  def __init__(self):
    self.memory_manager = TLONGlobalMemory__()
    TLONVariable__._visitor = self
    TLONVariable__._memory_manager = self.memory_manager

    # Visit a parse tree produced by TLONParser#parse.
  def visitParse(self, ctx: TLONParser.ParseContext):
    if ctx.from_file is not None:
      return self.visit(ctx.from_file())
    else:
      return self.visit(ctx.from_input())

  # Visit a parse tree produced by TLONParser#from_input.
  def visitFrom_input(self, ctx: TLONParser.From_inputContext):
    return self.visit(ctx.stat())

  # Visit a parse tree produced by TLONParser#from_file.
  def visitFrom_file(self, ctx: TLONParser.From_fileContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#stat.
  def visitStat(self, ctx: TLONParser.StatContext):
    if ctx.compound_stat() is not None:
      return self.visit(ctx.compound_stat())

    return self.visit(ctx.simple_stat())

  # Visit a parse tree produced by TLONParser#compound_stat.
  def visitCompound_stat(self, ctx: TLONParser.Compound_statContext):
    if ctx.if_stat() is not None:
      return self.visit(ctx.if_stat())
    elif ctx.while_stat() is not None:
      return self.visit(ctx.while_stat())
    elif ctx.for_stat() is not None:
      return self.visit(ctx.for_stat())

    return self.visit(ctx.funcion())

  # Visit a parse tree produced by TLONParser#simple_stat.
  def visitSimple_stat(self, ctx: TLONParser.Simple_statContext):
    if ctx.assignment() is not None:
      return self.visit(ctx.assignment())
    elif ctx.log() is not None:
      return self.visit(ctx.log())
    elif ctx.importar() is not None:
      return self.visit(ctx.importar())
    elif ctx.retornar() is not None:
      return self.visit(ctx.retornar())
    elif ctx.atom() is not None:
      return self.visit(ctx.atom())

    raise Exception('Semantic Error: Found ' + str(self.OTHER()))

  # Visit a parse tree produced by TLONParser#assignment.
  def visitAssignment(self, ctx: TLONParser.AssignmentContext):
    name = str(ctx.variable().getText())
    value = None

    if ctx.expr() is not None:
      value = self.visit(ctx.expr())
    elif ctx.assignment() is not None:
      value = self.visit(ctx.assigment())

    self.memory_manager.assign(name, value)
    return value

  # Visit a parse tree produced by TLONParser#if_stat.
  def visitIf_stat(self, ctx: TLONParser.If_statContext):
    conditions = ctx.condition_block()

    for condition in conditions:
      result = self.visit(condition)

      if result['accepted'] is True:
        return result['value_returned']

    if ctx.stat_block() is not None:
      self.memory_manager.add_memory('ELSE_STMT')
      value_returned = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()
      return value_returned

    return None

  # Visit a parse tree produced by TLONParser#while_stat.
  def visitWhile_stat(self, ctx: TLONParser.While_statContext):
    condition = self.visit(ctx.expr())
    returned_value = None

    while condition:
      self.memory_manager.add_memory('WHILE_STMT')
      returned_value = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()

      if type(returned_value) is tuple and returned_value[1] == 1:
        return returned_value[0]

      condition = self.visit(ctx.expr())

    return None

  # Visit a parse tree produced by TLONParser#for_stat.
  def visitFor_stat(self, ctx: TLONParser.For_statContext):
    items = self.visit(ctx.expr())
    var = str(ctx.ID())

    if self.memory_manager.find(var) is not None:
      raise Exception("Error: Cannot use variable " + var + ". Already assigned.")

    try:
      #validate if object is iterable
      items_iterator = iter(items)
      for item in items:
        self.memory_manager.add_memory('FOR_STMT')
        self.memory_manager.assign(var, item)
        returned_value = self.visit(ctx.stat_block())
        self.memory_manager.pop_memory()

        if type(returned_value) is tuple and returned_value[1] == 1:
          return returned_value[0]
    except:
      raise Exception("Error: Variable is not iterable.")

    return None

  # Visit a parse tree produced by TLONParser#log.
  def visitLog(self, ctx: TLONParser.LogContext):
    variable = self.visit(ctx.expr())

    if isinstance(variable, TLONVariable__):
      print(variable.value)
    else:
      print(variable)

    return None

  # Visit a parse tree produced by TLONParser#agente.
  def visitAgente(self, ctx:TLONParser.AgenteContext):
    array = []
    for param in ctx.atom():
      value = self.visit(param)
      array.append(value)
    agent = eval(array[0])(*array[1:])
    return agent

  # Visit a parse tree produced by TLONParser#funcion.
  def visitFuncion(self, ctx: TLONParser.FuncionContext):
    opcionales = False

    name = str(ctx.ID())
    kind = 'user'
    value = ctx.stat()

    parameters = {}
    for param in ctx.parametro():
      param_name = str(param.ID())

      if self.memory_manager.find(param_name) is not None:
        raise Exception('Cannot assign variable as parameter of function. Already assigned.')

      if (opcionales and param.ASSIGN() is None):
        raise Exception('Cannot set mandatory parameter after optional parameter')

      parameter = TLONParameter__(param_name)

      if (param.ASSIGN() is not None):
        parameter.kind = 'optional'
        parameter.default = self.visit(param.expr())
        opcionales = True
      else:
        parameter.kind = 'mandatory'

      parameters[param_name] = parameter

    local_memory = self.memory_manager.peek_memory()

    funcion = TLONVariable__(name, value, kind, parameters)
    local_memory.assign(name, funcion,None)

    return funcion

  # Visit a parse tree produced by TLONParser#importar.
  def visitImportar(self, ctx: TLONParser.ImportarContext):
    try:
        mod=None
        package_name = '.'.join([str(x.getText()) for x in ctx.ID()])
        try:
            mod = import_module(package_name)
            global_mem = self.memory_manager.get_memory(0)
            for name, attribute in mod.__dict__.items():
                if not name.startswith('__'):
                    var = TLONVariable__(name, attribute, 'default')
                    global_mem.assign(name, var,None)
        except:
            if len((ctx.ID()))==2:
                package_name = import_module(str(ctx.ID()[0]))
                if str(ctx.ID()[1]) in package_name.__dict__:
                    mod = getattr(package_name,str(ctx.ID()[1]))
                    global_mem = self.memory_manager.get_memory(0)
                    var = TLONVariable__(str(ctx.ID()[1]), mod, 'default')
                    global_mem.assign(str(ctx.ID()[1]), var,None)
                else:
                    error = "No module named '" + str(ctx.ID()[1]) +"'; '"+ str(ctx.ID()[0]) + "' is not a package"
                    raise Exception(error)

        return mod
    except Exception as e:
      print (e)

  # Visit a parse tree produced by TLONParser#retornar.
  def visitRetornar(self, ctx: TLONParser.RetornarContext):
    return (self.visit(ctx.expr()), 1)

  # Visit a parse tree produced by TLONParser#condition_block.
  def visitCondition_block(self, ctx: TLONParser.Condition_blockContext):

    result = { 'accepted': self.visit(ctx.expr()) }

    if result['accepted'] is True:
      self.memory_manager.add_memory('IF_STMT')
      result['value_returned'] = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()

    return result

  # Visit a parse tree produced by TLONParser#stat_block.
  def visitStat_block(self, ctx: TLONParser.Stat_blockContext):
    value_returned = None

    for stat in ctx.stat():
      value_returned = self.visit(stat)

    return value_returned

  # Visit a parse tree produced by TLONParser#array.
  def visitArray(self, ctx: TLONParser.ArrayContext):
    array = []

    if (len(ctx.POINTS()) > 0):
      try:
        init = self.visit(ctx.expr(0))
        end = self.visit(ctx.expr(1)) + 1
        step = 1

        if ctx.step is not None:
          step = self.visit(ctx.expr(1))
          end = self.visit(ctx.expr(2)) + 1

        if type(init) is float or type(end) is float or type(step) is float:
          init = float(init)
          step = float(step)
          end = float(end)
        else:
          init = int(init)
          step = int(step)
          end = int(end)

        array = list(arange(init, end, step))
      except Exception as e:
        print (e)
        raise Exception('Error: Variable types are not numeric.')

    else:
      items = ctx.expr()

      for item in items:
        value = self.visit(item)
        array.append(value)

    return array

  # Visit a parse tree produced by TLONParser#accessarray.
  def visitAccessarray(self, ctx: TLONParser.AccessarrayContext):
    variable = self.visit(ctx.variable())
    position = self.visit(ctx.expr())

    if (isinstance(variable, list) or isinstance(variable, tuple)) and type(position) is int:
      return variable[position]
    else:
      raise Exception("Error: Variable is not list.")

      # Visit a parse tree produced by TLONParser#dimamicarray.
    def visitDimamicarray(self, ctx:TLONParser.DimamicarrayContext):
        name = str(ctx.variable().getText())
    value = None

    if ctx.expr() is not None:
      value = self.visit(ctx.expr())
    elif ctx.assignment() is not None:
      value = self.visit(ctx.assigment())

    self.memory_manager.assign(name, value)

    return value
  # Visit a parse tree produced by TLONParser#variable.
  def visitVariable(self, ctx: TLONParser.VariableContext):
    name = ctx.ID()

    name = '.'.join(list(map(lambda x: x.getText(), name)))

    item = self.memory_manager.find(name)

    if item.kind == 'default' or (item.kind == 'any' and not (type(item.value) is int or type(item.value) is float or
                                                                  type(item.value) is str or type(item.value) is list or
                                                                  type(item.value) is dict)):
      if ctx.OPAR() is not None:
        params = list(map(lambda x: self.visit(x), ctx.expr()))
        if not isbuiltin(item.value):
          def_func_params = signature(item.value).parameters

          count_mandatory = sum(type(v.default) is type(_empty) for k, v in def_func_params.items())
          count = len(def_func_params)

          if len(params) > count:
            raise Exception('FunctionError: Too many parameter to call function.')
          if len(params) < count_mandatory:
            raise Exception('FunctionError: Too few parameter to call function.')

        func = item.value

        #try:
        return func(*params)
        #except Exception as e:
        #  raise Exception('FunctionError: Builtin function throws error:', e)
      else:
        item = item.value
    elif item.kind == 'user':
      if ctx.OPAR() is not None:
        params = list(map(lambda x: self.visit(x), ctx.expr()))
        count_mandatory = sum(param.kind == 'mandatory' for name, param in item.params.items())

        count = len(item.params)

        if len(params) > count:
          raise Exception('FunctionError: Too many parameter to call function.')
        if len(params) < count_mandatory:
          raise Exception('FunctionError: Too few parameter to call function.')

        index = 0
        func_params = {}
        ########################################################
        # ERROR
        # Resolver problema con programacion funcional
        # A veces se cambia el orden de los items en 'iem.params.items()' en python 3.4.2
        ########################################################
        for name, param in item.params.items():
          if len(params) <= index:
            break

          func_params[name] = params[index]
          index += 1

        local_memory = self.memory_manager.add_memory('FUNCTION', func_params)
        func = item.value

        returned = None
        for stat in func:
          value = self.visit(stat)

          if type(value) is tuple and value[1] == 1:
            self.memory_manager.pop_memory()
            return value[0]

        item = returned
      else:
        return item
    elif item.kind == 'any':
      if (type(item.value) is int or type(item.value) is float or type(item.value) is str or
              type(item.value) is list or type(item.value) is dict):
        item = item.value

    return item

  # Visit a parse tree produced by TLONParser#parametro.
  def visitParametro(self, ctx: TLONParser.ParametroContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#parExpr.
  def visitParExpr(self, ctx: TLONParser.ParExprContext):
    return self.visit(ctx.expr())

  # Visit a parse tree produced by TLONParser#notExpr.
  def visitNotExpr(self, ctx: TLONParser.NotExprContext):
    value = self.visit(ctx.expr())

    if isinstance(value, TLONVariable__):
      value = value.value

    return not value

  # Visit a parse tree produced by TLONParser#unaryMinusExpr.
  def visitUnaryMinusExpr(self, ctx: TLONParser.UnaryMinusExprContext):
    data = self.visit(ctx.expr())
    if isinstance(data, TLONVariable__):
      data = data.value
    return -data

  # Visit a parse tree produced by TLONParser#multiplicationExpr.
  def visitMultiplicationExpr(self, ctx: TLONParser.MultiplicationExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.MULT:
      return left * right
    if ctx.op.type == TLONParser.DIV:
      value = 0

      if right == 0:
        raise Exception("Error: Can\'t divide by zero.")
      else:
        value = left / right

      return value
    if ctx.op.type == TLONParser.MOD:
      return left % right

  # Visit a parse tree produced by TLONParser#atomExpr.
  def visitAtomExpr(self, ctx: TLONParser.AtomExprContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#orExpr.
  def visitOrExpr(self, ctx: TLONParser.OrExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return left or right

  # Visit a parse tree produced by TLONParser#additiveExpr.
  def visitAdditiveExpr(self, ctx: TLONParser.AdditiveExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.PLUS:
      if isinstance(left, str) or isinstance(right, str):
        return str(left) + str(right)
      return left + right
    if ctx.op.type == TLONParser.MINUS:
      return left - right

  # Visit a parse tree produced by TLONParser#powExpr.
  def visitPowExpr(self, ctx: TLONParser.PowExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return math.pow(left, right)

  # Visit a parse tree produced by TLONParser#relationalExpr.
  def visitRelationalExpr(self, ctx: TLONParser.RelationalExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.LT:
      return left < right
    if ctx.op.type == TLONParser.LTEQ:
      return left <= right
    if ctx.op.type == TLONParser.GT:
      return left > right
    if ctx.op.type == TLONParser.GTEQ:
      return left >= right

  # Visit a parse tree produced by TLONParser#equalityExpr.
  def visitEqualityExpr(self, ctx: TLONParser.EqualityExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.EQ:
      return left == right
    elif ctx.op.type == TLONParser.NEQ:
      return left != right

  # Visit a parse tree produced by TLONParser#andExpr.
  def visitAndExpr(self, ctx: TLONParser.AndExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return left and right

  # Visit a parse tree produced by TLONParser#numberAtom.
  def visitNumberAtom(self, ctx: TLONParser.NumberAtomContext):
    if ctx.INT() is not None:
      return int(ctx.INT().getText())

    return float(ctx.FLOAT().getText())

  # Visit a parse tree produced by TLONParser#booleanAtom.
  def visitBooleanAtom(self, ctx: TLONParser.BooleanAtomContext):
    if ctx.TRUE() is not None:
      return True

    return False

  # Visit a parse tree produced by TLONParser#stringAtom.
  def visitStringAtom(self, ctx: TLONParser.StringAtomContext):
    string = str(ctx.STRING().getText())
    string = string[1:len(string) - 1]

    return string

  # Visit a parse tree produced by TLONParser#arrayAtom.
  def visitArrayAtom(self, ctx: TLONParser.ArrayAtomContext):
    return self.visit(ctx.array());

  # Visit a parse tree produced by TLONParser#objetoAtom.
  def visitObjetoAtom(self, ctx: TLONParser.ObjetoAtomContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#accessToarray.
  def visitAccessToarray(self, ctx: TLONParser.AccessToarrayContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#accessVariable.
  def visitAccessVariable(self, ctx: TLONParser.AccessVariableContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#nilAtom.
  def visitNilAtom(self, ctx: TLONParser.NilAtomContext):
    return None

  # Visit a parse tree produced by TLONParser#objeto.
  def visitObjeto(self, ctx: TLONParser.ObjetoContext):
    items = {}

    for it in ctx.keyvalue():
      item = self.visit(it)
      items[item.name] = item

    return items

  # Visit a parse tree produced by TLONParser#keyvalue.
  def visitKeyvalue(self, ctx: TLONParser.KeyvalueContext):
    name = str(ctx.ID())
    value = self.visit(ctx.expr())

    obj = TLONVariable__(name, value, 'any')

    return obj
