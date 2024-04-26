from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Symbol():
    def __init__(self, decl, kind=Variable()):
        self.decl = decl
        self.kind = kind

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        if(self.visit(self.ast, [[]])):
            return []
    
    def visitProgram(self, ast, param):
        return reduce(lambda prev, curr: self.visit(curr,prev), ast.decl, param)

    def visitVarDecl(self, ast, param, kind=Variable()):
        # redeclared
        for decl in param[0]:
            if ast.name == decl.name:
                raise Redeclared(kind, ast.name)
        #
        
        param[0] += [ast]
        return param
                
            
    def visitFuncDecl(self, ast, param):
        # redeclared func
        for decl in param[0]:
            if ast.name == decl.name:
                raise Redeclared(Function(), ast.name)
            
        param[0] += [ast]

        #redeclared para
        func_scope = [[]] + param
        func_scope = reduce(lambda prev, curr: Symbol(self.visit(curr,prev), Parameter()), ast.param, func_scope)
        
        #
        
        return param

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitBlock(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        pass

