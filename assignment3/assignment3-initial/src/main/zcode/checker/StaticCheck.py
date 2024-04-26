from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Util():
    def infer(name, typ, params):
        for param in params:
            for sym in param:
                if sym.name.name == name:
                    sym.datatype = typ
                    return typ

class NoType(Type):
    def __str__(self):
        return "NoType"

class Symbol():
    def __init__(self, decltype, name, datatype, params=[], body = False):
        self.decltype = decltype
        self.name = name
        self.datatype = datatype
        self.params = params
        self.body = body

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.inLoop = []
        
    def check(self):
        if(self.visit(self.ast, [[]])):
            return ''
    
    # decl: List[Decl]
    def visitProgram(self, ast, param):
        # built-in function
        param[0] += [Symbol(Function(), Id('readNumber'), NumberType(), [], True),
                     Symbol(Function(), Id('writeNumber'), VoidType(), [NumberType()], True),
                     Symbol(Function(), Id('readBool'), BoolType(), [], True),
                     Symbol(Function(), Id('writeBool'), VoidType(), [BoolType()], True),
                     Symbol(Function(), Id('readString'), StringType(), [], True),
                     Symbol(Function(), Id('writeString'), VoidType(), [StringType()], True)
                    ]       
        
        # decl
        param = reduce(lambda prev, curr: self.visit(curr,prev), ast.decl, param)


        # no definition for a function
        entryPoint = False
        for sym in param[0]:
            if type(sym.decltype) is Function and not sym.body:
                raise NoDefinition(sym.name.name)
            elif(sym.name.name=='main' and type(sym.datatype) is VoidType and sym.params == []):
                entryPoint = True
            
        # no entry point
        if not entryPoint:
            raise NoEntryPoint()

        return param

    # name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None 
    def visitVarDecl(self, ast, param):
        # redeclared
        for sym in param[0]:
            if type(sym.decltype) is Variable and ast.name == sym.name:
                raise Redeclared(Variable(), ast.name.name)

        # update o      
        param[0] += [Symbol(Variable(), ast.name, ast.varType if ast.varType else NoType())]

        # infer type
        varInitName = None
        if type(ast.varInit) is Id:
            varInitName = ast.varInit.name
        elif type(ast.varInit) is CallExpr:
            varInitName = ast.varInit.name.name

        
        if ast.varType:
            self.curType = ast.varType
            varInit = self.visit(ast.varInit, param) if ast.varInit else None

            if varInit and type(varInit) is NoType:
                varInit = Util.infer(varInitName, ast.varType, param)

            if varInit and type(ast.varType) is ArrayType and (ast.varType.size != varInit.size or type(ast.varType.eleType) != type(varInit.eleType)):
                raise TypeMismatchInStatement(ast)
            elif varInit and type(ast.varType) != type(varInit):
                raise TypeMismatchInStatement(ast)
            
        else:
            varInit = self.visit(ast.varInit, param) if ast.varInit else None
            if varInit and type(varInit) is NoType:
                raise TypeCannotBeInferred(ast)
            
            curType = param[0][-1].datatype
            
            if varInit and type(curType) is NoType:
                curType = Util.infer(ast.name.name, varInit, param)
            if varInit and type(curType) != type(varInit):
                raise TypeMismatchInStatement(ast)
            
        
        
        return param
    
    # lhs: Expr, rhs: Expr
    def visitAssign(self, ast, param):
        rhs = self.visit(ast.rhs, param)
        lhs = self.visit(ast.lhs, param)
        
        if type(lhs) is NoType and type(rhs) is NoType:
            raise TypeCannotBeInferred(ast)
        if type(lhs) is NoType:
            lhs = Util.infer(ast.lhs.name, rhs, param)
        if type(rhs) is NoType:
            rhsName = ast.rhs.name if type(ast.rhs) is Id else ast.rhs.name.name
            rhs = Util.infer(rhsName, lhs, param)

        if type(lhs) is ArrayType and (lhs.size != rhs.size or type(lhs.eleType) != type(rhs.eleType)):
            raise TypeMismatchInStatement(ast)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)

        return param
    
    # name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None 
    def visitParaDecl(self, ast, param):
        # redeclared
        for sym in param[0]:
            if ast.name == sym.name:
                raise Redeclared(Parameter(), ast.name.name)
        
        #update o
        param[0] += [Symbol(Parameter(), ast.name, ast.varType)]
        return param
                


    # name: Id, param: List[VarDecl], body: Stmt = None
    def visitFuncDecl(self, ast, param):
        # redeclared param
        if ast.body:
            func_scope = [[]] + param
            func_scope = reduce(lambda prev, curr:  self.visitParaDecl(curr, prev) , ast.param, func_scope)

        # redeclared func
        curFunc = None

        for sym in param[0]:
            if type(sym.decltype) is Function and ast.name == sym.name:
                if len(sym.params) != len(ast.param):
                    raise Redeclared(Function(), ast.name.name)
                else:
                    for i in range(len(sym.params)):
                        left = sym.params[i]
                        right = ast.param[i].varType
                        if type(left) is ArrayType and (left.size != right.size or type(left.eleType) != type(right.eleType)):
                            raise Redeclared(Function(), ast.name.name)
                        elif type(left) != type(right):
                            raise Redeclared(Function(), ast.name.name)
                if sym.body or not ast.body:
                    raise Redeclared(Function(), ast.name.name)
                else:
                    param[0].remove(sym)
                    param[0] += [sym]
                    sym.body = True
                    curFunc = sym 
                    break
            
        # update o
        if ast.body:
            if not curFunc:
                curFunc = Symbol(Function(), ast.name, NoType(), list(map(lambda vardecl : vardecl.varType , ast.param)), True)
                param[0] += [curFunc]

            # return type
            self.visit(ast.body,func_scope)

            rettype = param[-1][-1].datatype

            if type(rettype) is NoType:
                param[-1][-1].datatype = VoidType()

        else:
            curFunc = Symbol(Function(), ast.name, NoType(), list(map(lambda vardecl : vardecl.varType , ast.param)))
            param[0] += [curFunc]

        return param


    # stmt: List[Stmt]
    def visitBlock(self, ast, param):
        block_scope = [[]] + param
        block_scope = reduce(lambda prev, curr:  self.visit(curr, prev) , ast.stmt, block_scope)
        return param
    

    # expr: Expr = None
    def visitReturn(self, ast, param):
        rettype = param[-1][-1].datatype

        if ast.expr:
            expr = self.visit(ast.expr, param)

            exprName = None
            if type(ast.expr) is Id:
                exprName = ast.expr.name
            elif type(ast.expr) is CallExpr:
                exprName = ast.expr.name.name

            if type(rettype) is NoType and type(expr) is NoType:
                raise TypeCannotBeInferred(ast)
            elif type(rettype) is NoType:
                param[-1][-1].datatype = expr
                rettype = expr
            elif type(expr) is NoType and not (type(rettype) is VoidType):
                expr = Util.infer(exprName, rettype, param)
            
            if type(rettype) != type(expr) or rettype != expr:
                raise TypeMismatchInStatement(ast)
                
        else:
            if type(rettype) is NoType:
                param[-1][-1].datatype = VoidType()
            elif not (type(rettype) is VoidType):
                raise TypeMismatchInStatement(ast)
        
        return param

        


        

    
    # name: Id, args: List[Expr]
    def visitCallExpr(self, ast, param):
        for sym in param[-1]:
            # type mismatch function
            if type(sym.decltype) is Function and ast.name == sym.name:
                if type(sym.datatype) is VoidType or len(sym.params) != len(ast.args):
                    raise TypeMismatchInExpression(ast)

                #infer type
                for i in range(0, len(ast.args)):
                    arg = self.visit(ast.args[i], param)
                    if type(arg) is NoType:
                        name = ast.args[i].name if type(ast.args[i]) is Id else ast.args[i].name.name
                        Util.infer(name, sym.params[i], param)   

                    elif type(arg) is ArrayType and (arg.size != sym.params[i].size or type(arg.eleType) != type(sym.params[i].eleType)):
                        raise TypeMismatchInExpression(ast)
                    elif type(arg) != ArrayType and type(arg) != type(sym.params[i]):
                        raise TypeMismatchInExpression(ast)

                return sym.datatype
            
        # undeclared func
        raise Undeclared(Function(), ast.name.name)
    
    # name: Id, args: List[Expr]    
    def visitCallStmt(self, ast, param):
        for sym in param[-1]:
            # type mismatch function
            if type(sym.decltype) is Function and ast.name == sym.name:
                if type(sym.datatype) is NoType:
                    sym.datatype = VoidType()
                if len(ast.args) != len(sym.params) or not(type(sym.datatype) is VoidType):
                    raise TypeMismatchInStatement(ast)
                
                #infer type
                for i in range(0, len(ast.args)):
                    arg = self.visit(ast.args[i], param)
                    if type(arg) is NoType:
                        name = ast.args[i].name if type(ast.args[i]) is Id else ast.args[i].name.name
                        Util.infer(name, sym.params[i], param)   

                    elif type(arg) is ArrayType and (arg.size != sym.params[i].size or type(arg.eleType) != type(sym.params[i].eleType)):
                        raise TypeMismatchInStatement(ast)
                    elif type(arg) != ArrayType and type(arg) != type(sym.params[i]):
                        raise TypeMismatchInStatement(ast)
                    
                return param

        # undeclared func
        raise Undeclared(Function(), ast.name.name)


    # name: str
    def visitId(self, ast, param):
        for env in param:
            for sym in env:
                if ast == sym.name:
                    return sym.datatype
        raise Undeclared(Identifier(), ast.name)
    

    # op: str, left: Expr, right: Expr
    def visitBinaryOp(self, ast, param):
        op = ast.op
        left = None
        right = None
        
        leftName = rightName = None

        if type(ast.left) is Id:
            leftName = ast.left.name
        elif type(ast.left) is CallExpr:
            leftName = ast.left.name.name

        if type(ast.right) is Id:
            rightName = ast.right.name
        elif type(ast.right) is CallExpr:
            rightName = ast.right.name.name

        if op in ['+','-','*','/','%']:
            left = self.visit(ast.left, param)
            if type(left) is NoType:
                left = Util.infer(leftName, NumberType(), param)

            right = self.visit(ast.right, param)
            if type(right) is NoType:
                right = Util.infer(rightName, NumberType(), param)

            if type(left) is NumberType and type(right) is NumberType:
                return NumberType()
            
        elif op in ['and', 'or']:
            left = self.visit(ast.left, param)
            if type(left) is NoType:
                left = Util.infer(leftName, BoolType(), param)

            right = self.visit(ast.right, param)
            if type(right) is NoType:
                right = Util.infer(rightName, BoolType(), param)

            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            
        
        elif op in ['...']:
            left = self.visit(ast.left, param)
            if type(left) is NoType:
                left = Util.infer(leftName, StringType(), param)

            right = self.visit(ast.right, param)
            if type(right) is NoType:
                right = Util.infer(rightName, StringType(), param)

            if type(left) is StringType and type(right) is StringType:
                return StringType()
            
        
        elif op in ['=','!=','>','<','<=','>=']:
            left = self.visit(ast.left, param)
            if type(left) is NoType:
                left = Util.infer(leftName, NumberType(), param)

            right = self.visit(ast.right, param)
            if type(right) is NoType:
                right = Util.infer(rightName, NumberType(), param)

            if type(left) is NumberType and type(right) is NumberType:
                return BoolType()
        
        else:
            left = self.visit(ast.left, param)
            if type(left) is NoType:
                left = Util.infer(ast.left.name, StringType(), param)

            right = self.visit(ast.right, param)
            if type(right) is NoType:
                right = Util.infer(ast.right.name, StringType(), param)

            if type(left) is StringType and type(right) is StringType:
                return BoolType()
            

        raise TypeMismatchInExpression(ast)

    # op: str, operand: Expr
    def visitUnaryOp(self, ast, param):
        op = ast.op
        operand = self.visit(ast.operand, param)

        operandName = None

        if type(ast.operand) is Id:
            operandName = ast.operand.name
        elif type(ast.operand) is CallExpr:
            operandName = ast.operand.name.name

        if op == '-':
            if type(operand) is NoType:
                operand = Util.infer(operandName, NumberType(), param)

            if type(operand) is NumberType:
                return NumberType()
            
        else:
            if type(operand) is NoType:
                operand = Util.infer(operandName, BoolType(), param)

            if type(operand) is BoolType:
                return BoolType()
            

        raise TypeMismatchInExpression(ast)
    
    # arr: Expr, idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)

        if type(arr) != ArrayType:
            raise TypeMismatchInExpression(ast)

        for idx in ast.idx:
            curIdx = self.visit(idx, param)
            if type(curIdx) is NoType:
                idxName = idx.name if type(idx) is Id else idx.name.name
                curIdx = Util.infer(idxName, NumberType(), param)
            if type(curIdx) != NumberType:
                raise TypeMismatchInExpression(ast)

        return arr.eleType
        
        
        

            

    # expr: Expr, thenStmt: Stmt, elifStmt: List[Tuple[Expr, Stmt]], elseStmt: Stmt = None 
    def visitIf(self, ast, param):
        # if
        ifExpr = self.visit(ast.expr, param)

        if type(ifExpr) is NoType:
            ifExpr = Util.infer(ast.expr.name if type(ast.expr) is Id else ast.expr.name.name, BoolType(), param)
        if type(ifExpr) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, param)

        # elif
        for tup in ast.elifStmt:
            elifExpr = self.visit(tup[0], param)

            if type(elifExpr) is NoType:
                elifExpr = Util.infer(tup[0].name if type(tup[0]) is Id else tup[0].name.name, BoolType(), param)
            if not (type(elifExpr) is BoolType):
                raise TypeMismatchInStatement(ast)
        
            self.visit(tup[1], param)
            
        # else
        if ast.elseStmt:
            self.visit(ast.elseStmt, param) 

        return param
        

    # name: Id, condExpr: Expr, updExpr: Expr, body: Stmt
    def visitFor(self, ast, param):
        # counter
        counter = self.visit(ast.name, param)

        if type(counter) is NoType:
            counter = Util.infer(ast.name.name, NumberType(), param)
        if type(counter) != NumberType:
            raise TypeMismatchInStatement(ast)
        
        # condition
        condition = self.visit(ast.condExpr, param)

        if type(condition) is NoType:
            condition = Util.infer(ast.condExpr.name if type(ast.condExpr) is Id else ast.condExpr.name.name, BoolType(), param)
        if type(condition) != BoolType:
            raise TypeMismatchInStatement(ast)

        # update expr
        updateExpr = self.visit(ast.updExpr, param)

        if type(updateExpr) is NoType:
            updateExpr = Util.infer(ast.updExpr.name if type(ast.updExpr) is Id else ast.updExpr.name.name, NumberType(), param)
        if not (type(updateExpr) is NumberType):
            raise TypeMismatchInStatement(ast)

        # body
        self.inLoop += [True]
        self.visit(ast.body, param)
        self.inLoop.pop()
        return param

    # value: List[Expr]
    def visitArrayLiteral(self, ast, param):
        datatype = self.visit(ast.value[0], param)
        
        if type(datatype) is ArrayType:
            for expr in ast.value:
                typ = self.visit(expr, param)
                if typ.size != datatype.size or type(typ.eleType) != type(datatype.eleType):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([float(len(ast.value))]+datatype.size, datatype.eleType)
        else:
            for expr in ast.value:
                typ = self.visit(expr, param)
                if type(typ) != type(datatype):
                    raise TypeMismatchInExpression(ast)
            return ArrayType([float(len(ast.value))], datatype)
        

    # size: List[float], eleType: Type
    def visitArrayType(self, ast, param):
        return ast

    def visitContinue(self, ast, param):
        if self.inLoop == []:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.inLoop == []:
            raise MustInLoop(ast)

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    



