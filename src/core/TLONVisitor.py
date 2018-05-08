# Generated from TLON.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TLONParser import TLONParser
else:
    from TLONParser import TLONParser

# This class defines a complete generic visitor for a parse tree produced by TLONParser.

class TLONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TLONParser#parse.
    def visitParse(self, ctx:TLONParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#from_input.
    def visitFrom_input(self, ctx:TLONParser.From_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#from_file.
    def visitFrom_file(self, ctx:TLONParser.From_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#stat.
    def visitStat(self, ctx:TLONParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#compound_stat.
    def visitCompound_stat(self, ctx:TLONParser.Compound_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#simple_stat.
    def visitSimple_stat(self, ctx:TLONParser.Simple_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#assignment.
    def visitAssignment(self, ctx:TLONParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#if_stat.
    def visitIf_stat(self, ctx:TLONParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#while_stat.
    def visitWhile_stat(self, ctx:TLONParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#for_stat.
    def visitFor_stat(self, ctx:TLONParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#log.
    def visitLog(self, ctx:TLONParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#agente.
    def visitAgente(self, ctx:TLONParser.AgenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#funcion.
    def visitFuncion(self, ctx:TLONParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#importar.
    def visitImportar(self, ctx:TLONParser.ImportarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#retornar.
    def visitRetornar(self, ctx:TLONParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#condition_block.
    def visitCondition_block(self, ctx:TLONParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#stat_block.
    def visitStat_block(self, ctx:TLONParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#array.
    def visitArray(self, ctx:TLONParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#accessarray.
    def visitAccessarray(self, ctx:TLONParser.AccessarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#variable.
    def visitVariable(self, ctx:TLONParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#parametro.
    def visitParametro(self, ctx:TLONParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#parExpr.
    def visitParExpr(self, ctx:TLONParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#notExpr.
    def visitNotExpr(self, ctx:TLONParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:TLONParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:TLONParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#atomExpr.
    def visitAtomExpr(self, ctx:TLONParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#orExpr.
    def visitOrExpr(self, ctx:TLONParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:TLONParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#powExpr.
    def visitPowExpr(self, ctx:TLONParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#relationalExpr.
    def visitRelationalExpr(self, ctx:TLONParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#equalityExpr.
    def visitEqualityExpr(self, ctx:TLONParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#andExpr.
    def visitAndExpr(self, ctx:TLONParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#numberAtom.
    def visitNumberAtom(self, ctx:TLONParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#booleanAtom.
    def visitBooleanAtom(self, ctx:TLONParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#stringAtom.
    def visitStringAtom(self, ctx:TLONParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#arrayAtom.
    def visitArrayAtom(self, ctx:TLONParser.ArrayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#objetoAtom.
    def visitObjetoAtom(self, ctx:TLONParser.ObjetoAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#accessToarray.
    def visitAccessToarray(self, ctx:TLONParser.AccessToarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#accessVariable.
    def visitAccessVariable(self, ctx:TLONParser.AccessVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#nilAtom.
    def visitNilAtom(self, ctx:TLONParser.NilAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#objeto.
    def visitObjeto(self, ctx:TLONParser.ObjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TLONParser#keyvalue.
    def visitKeyvalue(self, ctx:TLONParser.KeyvalueContext):
        return self.visitChildren(ctx)



del TLONParser