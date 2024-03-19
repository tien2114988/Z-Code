from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

# class ASTGeneration(ZCodeVisitor):

#     def visitProgram(self, ctx: ZCodeParser.ProgramContext):
#         return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])

class ASTGeneration(ZCodeVisitor):
    # program: NEWLINE* decl_list EOF;
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))

    # decl_list: decl decl_list | decl;
    def visitDecl_list(self,ctx:ZCodeParser.Decl_listContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
        
    # decl: (variable_decl | function_decl)  NEWLINE+;
    def visitDecl(self,ctx:ZCodeParser.DeclContext):
        if ctx.variable_decl(): 
            return self.visit(ctx.variable_decl())  
        else:
            return self.visit(ctx.function_decl())

    # variable_decl: explicit_decl | implicit_decl;
    def visitVariable_decl(self,ctx:ZCodeParser.Variable_declContext):
        if ctx.explicit_decl():
            return self.visit(ctx.explicit_decl()) 
        else:
            return self.visit(ctx.implicit_decl())
    
    # explicit_decl: type_decl IDENTIFIER (L_SB size_list R_SB | ) (assign_expr | );
    def visitExplicit_decl(self,ctx:ZCodeParser.Explicit_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        if ctx.size_list():
            varType =  ArrayType(self.visit(ctx.size_list()), self.visit(ctx.type_decl()))  
        else:
            varType = self.visit(ctx.type_decl())
        modifier = None
        if ctx.assign_expr():
            varInit = self.visit(ctx.assign_expr())  
        else:
            varInit = None
        return VarDecl(name, varType, modifier, varInit)

    # type_decl: NUMBER | BOOL | STRING;
    def visitType_decl(self,ctx:ZCodeParser.Type_declContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()
    
    # size_list: NUM_LIT COMMA size_list | NUM_LIT;
    def visitSize_list(self,ctx:ZCodeParser.Size_listContext):
        if ctx.COMMA():
            return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.size_list())
        else:
            return [float(ctx.NUM_LIT().getText())]

    # implicit_decl: var_decl | dynamic_decl;
    def visitImplicit_decl(self,ctx:ZCodeParser.Implicit_declContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        else:
            return self.visit(ctx.dynamic_decl())

    # var_decl: VAR IDENTIFIER assign_expr;
    def visitVar_decl(self,ctx:ZCodeParser.Var_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None 
        modifier = ctx.VAR().getText()
        varInit = self.visit(ctx.assign_expr())
        return VarDecl(name, varType, modifier, varInit)
    
    # dynamic_decl: DYNAMIC IDENTIFIER (assign_expr | );
    def visitDynamic_decl(self,ctx:ZCodeParser.Dynamic_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None 
        modifier = ctx.DYNAMIC().getText()
        if ctx.assign_expr():
            varInit = self.visit(ctx.assign_expr()) 
        else:
            varInit = None
        return VarDecl(name, varType, modifier, varInit)

    # literals: NUM_LIT | (TRUE | FALSE) | STR_LIT | arr_lit;
    def visitLiterals(self,ctx:ZCodeParser.LiteralsContext):
        if ctx.NUM_LIT():
            value = float(ctx.NUM_LIT().getText())
            return NumberLiteral(value)
        elif ctx.STR_LIT():
            value = ctx.STR_LIT().getText()
            return StringLiteral(value)
        elif ctx.arr_lit():
            value = self.visit(ctx.arr_lit())
            return ArrayLiteral(value)
        else:
            value = True if ctx.TRUE() else False
            return BooleanLiteral(value)
    
    # arr_lit: L_SB arr_list R_SB;
    def visitArr_lit(self,ctx:ZCodeParser.Arr_litContext):
        return self.visit(ctx.arr_list())
    
    # arr_list: expr COMMA arr_list | expr;
    def visitArr_list(self,ctx:ZCodeParser.Arr_listContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.arr_list())
        else:
            return [self.visit(ctx.expr())]
    
    
    
    
    
    # function_decl: FUNC IDENTIFIER L_RB para_list R_RB (NEWLINE* func_body | );
    def visitFunction_decl(self,ctx:ZCodeParser.Function_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.para_list())
        if ctx.func_body():
            body = self.visit(ctx.func_body()) 
        else:
            body = None
        return FuncDecl(name, param, body)
    
    # para_list: prime_para_list | ;
    def visitPara_list(self,ctx:ZCodeParser.Para_listContext):
        if ctx.prime_para_list():
            return self.visit(ctx.prime_para_list())
        else:
            return []
    
    # prime_para_list: para_decl COMMA prime_para_list | para_decl;
    def visitPrime_para_list(self,ctx:ZCodeParser.Prime_para_listContext):
        if ctx.COMMA():
            return [self.visit(ctx.para_decl())] + self.visit(ctx.prime_para_list())
        else:
            return [self.visit(ctx.para_decl())]
    
    # para_decl: type_decl IDENTIFIER (L_SB size_list R_SB | );
    def visitPara_decl(self,ctx:ZCodeParser.Para_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        if ctx.size_list():
            varType = ArrayType(self.visit(ctx.size_list()), self.visit(ctx.type_decl()))
        else:
            varType = self.visit(ctx.type_decl())
        return VarDecl(name, varType)

    # func_body: return_stmt | block_stmt;
    def visitFunc_body(self,ctx:ZCodeParser.Func_bodyContext):
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        else:
            return self.visit(ctx.block_stmt())

    # stmt_list: stmt NEWLINE+ stmt_list | ;
    def visitStmt_list(self,ctx:ZCodeParser.Stmt_listContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list())
        else:
            return []
    
    # stmt: var_decl_stmt | assign_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;
    def visitStmt(self,ctx:ZCodeParser.StmtContext):
        if ctx.var_decl_stmt():
            return self.visit(ctx.var_decl_stmt())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        else:
            return self.visit(ctx.block_stmt())

    # var_decl_stmt: variable_decl;
    def visitVar_decl_stmt(self,ctx:ZCodeParser.Var_decl_stmtContext):
        return self.visit(ctx.variable_decl())
    
    # assign_stmt: lhs assign_expr;
    def visitAssign_stmt(self,ctx:ZCodeParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.assign_expr())
        return Assign(lhs, exp)
    
    # if_stmt: if_part elif_list else_part;
    def visitIf_stmt(self,ctx:ZCodeParser.If_stmtContext):
        expr = self.visit(ctx.if_part())[0]
        thenStmt = self.visit(ctx.if_part())[1]
        elifStmt = self.visit(ctx.elif_list())
        elseStmt = self.visit(ctx.else_part())
        return If(expr, thenStmt, elifStmt, elseStmt)
    
    # for_stmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE* stmt;
    def visitFor_stmt(self,ctx:ZCodeParser.For_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.expr(0))
        updpExpr = self.visit(ctx.expr(1))
        body = self.visit(ctx.stmt())
        return For(name, condExpr, updpExpr, body)
    
    # break_stmt: BREAK;
    def visitBreak_stmt(self,ctx:ZCodeParser.Break_stmtContext):
        return Break()
    
    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self,ctx:ZCodeParser.Continue_stmtContext):
        return Continue()
    
    # return_stmt: RETURN expr | RETURN;
    def visitReturn_stmt(self,ctx:ZCodeParser.Return_stmtContext):
        if ctx.getChildCount()==1:
            return Return()
        else: 
            expr = self.visit(ctx.expr())
            return Return(expr)

    # call_stmt: IDENTIFIER L_RB arg_list R_RB;
    def visitCall_stmt(self,ctx:ZCodeParser.Call_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.arg_list())
        return CallStmt(name, args)
    
    # block_stmt: BEGIN NEWLINE+ stmt_list END;
    def visitBlock_stmt(self,ctx:ZCodeParser.Block_stmtContext):
        stmt = self.visit(ctx.stmt_list())
        return Block(stmt)

    # assign_expr: ASSIGN expr;
    def visitAssign_expr(self,ctx:ZCodeParser.Assign_exprContext):
        return self.visit(ctx.expr())
    
    # lhs: IDENTIFIER | recur_idx_expr;
    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return Id(name)
        else:
            return self.visit(ctx.recur_idx_expr())
    
    # recur_idx_expr: IDENTIFIER L_SB idx_operator R_SB;
    def visitRecur_idx_expr(self,ctx:ZCodeParser.Recur_idx_exprContext):
        arr = Id(ctx.IDENTIFIER().getText())
        idx = self.visit(ctx.idx_operator())
        return ArrayCell(arr, idx)

    # if_part: IF L_RB expr R_RB NEWLINE* stmt;
    def visitIf_part(self,ctx:ZCodeParser.If_partContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return (expr, stmt)
    
    # elif_list: NEWLINE+ elif_part elif_list | ;
    def visitElif_list(self,ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount()>0:
            return [self.visit(ctx.elif_part())] + self.visit(ctx.elif_list())
        else:
            return []
    
    # elif_part: ELIF L_RB expr R_RB NEWLINE* stmt;
    def visitElif_part(self,ctx:ZCodeParser.Elif_partContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return (expr, stmt)
    
    # else_part: NEWLINE+ ELSE NEWLINE* stmt | ;
    def visitElse_part(self,ctx:ZCodeParser.Else_partContext):
        if ctx.ELSE():
            return self.visit(ctx.stmt())
        else:
            return None
    
    
    
    
    
    
    
    
    
    # expr: str_expr;
    def visitExpr(self,ctx:ZCodeParser.ExprContext):
        return self.visit(ctx.str_expr())
    
    # str_expr: cmp_expr concat_operator cmp_expr | cmp_expr;
    def visitStr_expr(self,ctx:ZCodeParser.Str_exprContext):
        if ctx.concat_operator():
            op = self.visit(ctx.concat_operator())
            left = self.visit(ctx.cmp_expr(0))
            right = self.visit(ctx.cmp_expr(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.cmp_expr(0))
    
    # cmp_expr: log2_expr cmp_operator log2_expr | log2_expr;
    def visitCmp_expr(self,ctx:ZCodeParser.Cmp_exprContext):
        if ctx.cmp_operator():
            op = self.visit(ctx.cmp_operator())
            left = self.visit(ctx.log2_expr(0))
            right = self.visit(ctx.log2_expr(1))
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.log2_expr(0))
    
    # log2_expr: log2_expr log2_operator add_expr | add_expr;
    def visitLog2_expr(self,ctx:ZCodeParser.Log2_exprContext):
        if ctx.log2_operator():
            op = self.visit(ctx.log2_operator())
            left = self.visit(ctx.log2_expr())
            right = self.visit(ctx.add_expr())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.add_expr())
    
    # add_expr: add_expr add_operator mul_expr | mul_expr;
    def visitAdd_expr(self,ctx:ZCodeParser.Add_exprContext):
        if ctx.add_operator():
            op = self.visit(ctx.add_operator())
            left = self.visit(ctx.add_expr())
            right = self.visit(ctx.mul_expr())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.mul_expr())
    
    # mul_expr: mul_expr mul_operator log1_expr | log1_expr;
    def visitMul_expr(self,ctx:ZCodeParser.Mul_exprContext):
        if ctx.mul_operator():
            op = self.visit(ctx.mul_operator())
            left = self.visit(ctx.mul_expr())
            right = self.visit(ctx.log1_expr())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.log1_expr())
    
    # log1_expr: log1_operator log1_expr | sign_expr;
    def visitLog1_expr(self,ctx:ZCodeParser.Log1_exprContext):
        if ctx.log1_operator():
            op = self.visit(ctx.log1_operator())
            operand = self.visit(ctx.log1_expr())
            return UnaryOp(op, operand)
        else:
            return self.visit(ctx.sign_expr())
    
    # sign_expr: sign_operator sign_expr | idx_expr;
    def visitSign_expr(self,ctx:ZCodeParser.Sign_exprContext):
        if ctx.sign_operator():
            op = self.visit(ctx.sign_operator())
            operand = self.visit(ctx.sign_expr())
            return UnaryOp(op, operand)
        else:
            return self.visit(ctx.idx_expr())
        
    # idx_expr: var_expr L_SB idx_operator R_SB | val_expr;
    def visitIdx_expr(self,ctx:ZCodeParser.Idx_exprContext):
        if ctx.idx_operator():
            arr = self.visit(ctx.var_expr())
            idx = self.visit(ctx.idx_operator())
            return ArrayCell(arr, idx)
        else:
            return self.visit(ctx.val_expr())
    
    # val_expr: literals | IDENTIFIER | call_expr | sub_expr;
    def visitVal_expr(self,ctx:ZCodeParser.Val_exprContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return Id(name)
        elif ctx.call_expr():
            return self.visit(ctx.call_expr())
        else: 
            return self.visit(ctx.sub_expr())
    
    # var_expr: IDENTIFIER | call_expr;
    def visitVar_expr(self,ctx:ZCodeParser.Var_exprContext):
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return Id(name)
        else:
            return self.visit(ctx.call_expr())
    
    # call_expr: IDENTIFIER L_RB arg_list R_RB;
    def visitCall_expr(self,ctx:ZCodeParser.Call_exprContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.arg_list())
        return CallExpr(name, args)
    
    # sub_expr: L_RB expr R_RB;
    def visitSub_expr(self,ctx:ZCodeParser.Sub_exprContext):
        return self.visit(ctx.expr())

    # arg_list: prime_arg_list | ;
    def visitArg_list(self,ctx:ZCodeParser.Arg_listContext):
        if ctx.prime_arg_list():
            return self.visit(ctx.prime_arg_list())
        else:
            return []
    
    # prime_arg_list: expr COMMA prime_arg_list | expr;
    def visitPrime_arg_list(self,ctx:ZCodeParser.Prime_arg_listContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.prime_arg_list())
        else: 
            return [self.visit(ctx.expr())]

    # concat_operator: CONCAT;
    def visitConcat_operator(self,ctx:ZCodeParser.Concat_operatorContext):
        return ctx.CONCAT().getText()
    
    # cmp_operator: EQ_NUM | NOT_EQ | LESS | LESS_EQ | GREATER | GREATER_EQ | EQ_STR;
    def visitCmp_operator(self,ctx:ZCodeParser.Cmp_operatorContext):
        if ctx.EQ_NUM():
            return ctx.EQ_NUM().getText()
        elif ctx.NOT_EQ():
            return ctx.NOT_EQ().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.LESS_EQ():
            return ctx.LESS_EQ().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.GREATER_EQ():
            return ctx.GREATER_EQ().getText()
        else: 
            return ctx.EQ_STR().getText()
        
    # log2_operator: AND | OR;
    def visitLog2_operator(self,ctx:ZCodeParser.Log2_operatorContext):
        if ctx.AND():
            return ctx.AND().getText()
        else:
            return ctx.OR().getText()
    
    # add_operator: ADD | SUB;
    def visitAdd_operator(self,ctx:ZCodeParser.Add_operatorContext):
        if ctx.ADD():
            return ctx.ADD().getText()
        else:
            return ctx.SUB().getText()
    
    # mul_operator: MUL | DIV | MOD;
    def visitMul_operator(self,ctx:ZCodeParser.Mul_operatorContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        else: 
            return ctx.MOD().getText()
        
    # log1_operator: NOT;
    def visitLog1_operator(self,ctx:ZCodeParser.Log1_operatorContext):
        return ctx.NOT().getText()
    
    # sign_operator: SUB;
    def visitSign_operator(self,ctx:ZCodeParser.Sign_operatorContext):
        return ctx.SUB().getText()
    
    # idx_operator: expr | expr COMMA idx_operator;
    def visitIdx_operator(self,ctx:ZCodeParser.Idx_operatorContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.idx_operator())
        else:
            return [self.visit(ctx.expr())]