import sys
import math
from inspect import signature, _empty, isbuiltin
from types import *
from importlib import import_module

from .TLONParser import TLONParser
from .TLONVisitor import TLONVisitor

from .structures import *

sys.setrecursionlimit(10000000)


class Visitor(TLONVisitor):
    memory_manager = None
    value_returned = False

    def __init__(self, memory_manager=TLONGlobalMemory__()):
        self.memory_manager = memory_manager

    def visitAssignment(self, ctx):
        name = ctx.variable().getText()
        value = self.visit(ctx.expr())

        self.memory_manager.assign(name, value)

        return None

    def visitImportar(self, ctx):
        packageName = '.'.join([str(x.getText()) for x in ctx.ID()])
        mod = import_module(packageName)

        global_mem = self.memory_manager.get_memory(0)

        for name, attribute in mod.__dict__.items():
            if not name.startswith('__'):
                var = TLONVariable__(name, 'default', attribute)
                global_mem.assign(name, var)

        return None

    def visitTLONVariable__(self, ctx):
        name = ctx.ID()
        item = self.memory_manager.find(name)

        if item.kind == 'default':
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
                try:
                    return func(*params)
                except Exception as e:
                    raise Exception('FunctionError: Builtin function throws error:', e)
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
            if (type(item.value) is int or type(item.value) is float or
                        type(item.value) is str or type(item.value) is list or
                        type(item.value) is dict):
                item = item.value

        return item

    def visitStringAtom(self, ctx):
        string = str(ctx.STRING().getText())
        string = string[1:len(string) - 1]
        return string

    def visitNumberAtom(self, ctx):
        if ctx.INT() is not None:
            return int(ctx.INT().getText())

        return float(ctx.FLOAT().getText())

    def visitLog(self, ctx):
        variable = self.visit(ctx.expr())
        if type(variable) is Variable:
            print(variable.value)
        else:
            print(variable)
        return None

    def visitBooleanAtom(self, ctx):
        if ctx.TRUE() is not None:
            return True

        return False

    def visitNilAtom(self, ctx):
        return None

    def visitPowExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        return math.pow(left, right)

    def visitUnaryMinusExpr(self, ctx):
        data = self.visit(ctx.expr())
        if data.__class__ is Variable:
            data = data.value
        return -data

    def visitMultiplicationExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
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

    def visitAdditiveExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        if ctx.op.type == TLONParser.PLUS:
            return left + right
        if ctx.op.type == TLONParser.MINUS:
            return left - right

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        if ctx.op.type == TLONParser.LT:
            return left < right
        if ctx.op.type == TLONParser.LTEQ:
            return left <= right
        if ctx.op.type == TLONParser.GT:
            return left > right
        if ctx.op.type == TLONParser.GTEQ:
            return left >= right

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        if ctx.op.type == TLONParser.EQ:
            return left == right
        elif ctx.op.type == TLONParser.NEQ:
            return left != right

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        return left and right

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.__class__ is Variable:
            left = left.value
        if right.__class__ is Variable:
            right = right.value

        return left or right

    def visitNotExpr(self, ctx):
        value = self.visit(ctx.expr())

        if value.__class__ is Variable:
            value = value.value

        return not value

    def visitIf_stat(self, ctx):
        conditions = ctx.condition_block()

        is_accepted = False
        for condition in conditions:
            is_accepted = self.visit(condition.expr())

            if is_accepted is True:
                self.memory_manager.add_memory('IF_STAT')
                value = self.visit(condition.stat_block())
                self.memory_manager.pop_memory()
                if (type(value) is tuple and value[1] == 1):
                    return value

        if is_accepted is False and ctx.stat_block() is not None:
            self.memory_manager.add_memory('IF_STAT')
            value = self.visit(ctx.stat_block())
            if (type(value) is tuple and value[1] == 1):
                return value
            self.memory_manager.pop_memory()

        return None

    def visitWhile_stat(self, ctx):
        condition = self.visit(ctx.expr())

        while condition:
            self.memory_manager.add_memory('WHILE_LOOP')
            self.visit(ctx.stat_block())
            self.memory_manager.pop_memory()

            condition = self.visit(ctx.expr())

        return None

    # Revisar que esta haciendo esta funcion
    def visitFor_stat(self, ctx):
        items = self.visit(ctx.expr())
        var = str(ctx.ID())

        if (self.memory_manager.exists(var)):
            raise Exception("Error: Can\'t use variable " + var + " already assigned.")

        if type(items) is list:

            for item in items:
                self.memory_manager.add_memory('FOR_LOOP')
                self.memory_manager.assign(var, item)

                self.visit(ctx.stat_block())

                self.memory_manager.pop_memory()
        else:
            raise Exception("Error: Variable is not iterable.")

        return None

    def visitArray(self, ctx):
        items = ctx.expr()
        array = []

        if (ctx.POINTS() is not None):
            try:
                init = self.visit(items[0])
                step = 1
                end = self.visit(items[-1])

                if len(ctx.POINTS()) == 2:
                    step = self.visit(items[1])

                if type(init) is float or type(end) is float or type(step) is float:
                    init = float(init)
                    step = float(step)
                    end = float(end)
                else:
                    init = int(init)
                    step = int(step)
                    end = int(end)

            except Exception:
                raise Exception('Error: Variable types are not numeric.')

            i = init
            while i <= end:
                array.append(i)
                i += step

            if i > end and i < end + step:
                array.append(end)
        else:
            for item in items:
                value = self.visit(item)
                array.append(value)

        return array

    def visitAccessarray(self, ctx):
        variable = self.visit(ctx.variable())
        position = self.visit(ctx.expr())

        if type(variable) is list and type(position) is int:
            return variable[position]
        else:
            raise Exception("Error: Variable is not list.")

    def visitFuncion(self, ctx):
        opcionales = False

        name = str(ctx.ID())
        kind = 'user'
        value = ctx.stat()

        parameters = {}
        for param in ctx.parametro():
            param_name = str(param.ID())

            if self.memory_manager.exists(param_name):
                raise Exception('Can\'t assign variable as parameter of function')

            if (opcionales and param.ASSIGN() is None):
                raise Exception('Can\'t set mandatory parameter after optional parameter')

            parameter = TLONParameter__(param_name)

            if (param.ASSIGN() is not None):
                parameter.kind = 'optional'
                parameter.default = self.visit(param.expr())
                opcionales = True
            else:
                parameter.kind = 'mandatory'

            parameters[param_name] = parameter

        local_memory = self.memory_manager.peek_memory()

        funcion = TLONVariable__(name, kind, value, parameters)
        local_memory.assign(name, funcion)

        return None

    def visitRetornar(self, ctx):
        return (self.visit(ctx.expr()), 1)

    def visitObjeto(self, ctx):
        items = {}

        for it in ctx.keyvalue():
            item = self.visit(it)
            items[item.name] = item

        return items

    def visitKeyvalue(self, ctx):
        name = str(ctx.ID())
        value = self.visit(ctx.expr())

        obj = TLONVariable__(name, 'any', value)

        return obj

    def visitStat(self, ctx: TLONParser.StatContext):
        if (ctx.if_stat() is not None):
            value = self.visit(ctx.if_stat())
            if (type(value) is tuple and value[1] == 1):
                return value
        if (ctx.retornar() is not None):
            value = self.visit(ctx.retornar())
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: TLONParser.BlockContext):
        for stat in ctx.stat():
            value = self.visit(stat)
            if (type(value) is tuple and value[1] == 1):
                return value
        return None

    def visitStat_block(self, ctx: TLONParser.Stat_blockContext):

        if ctx.block() is not None:
            for stat in ctx.block().stat():
                value = self.visit(stat)
                if (type(value) is tuple and value[1] == 1):
                    return value

        else:
            value = self.visit(ctx.stat())
            if (type(value) is tuple and value[1] == 1):
                return value

        return None

    def visitParExpr(self, ctx: TLONParser.ParExprContext):
        return self.visit(ctx.expr())

    def visitCondition_block(self, ctx: TLONParser.Condition_blockContext):
        value = self.visit(ctx.stat_block())

        if (type(value) is tuple and value[1] == 1):
            return value

        return None
