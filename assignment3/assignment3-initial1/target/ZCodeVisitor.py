# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_decl.
    def visitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicit_decl.
    def visitExplicit_decl(self, ctx:ZCodeParser.Explicit_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_decl.
    def visitType_decl(self, ctx:ZCodeParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#size_list.
    def visitSize_list(self, ctx:ZCodeParser.Size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_decl.
    def visitImplicit_decl(self, ctx:ZCodeParser.Implicit_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_decl.
    def visitDynamic_decl(self, ctx:ZCodeParser.Dynamic_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_lit.
    def visitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_list.
    def visitArr_list(self, ctx:ZCodeParser.Arr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_decl.
    def visitFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_list.
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prime_para_list.
    def visitPrime_para_list(self, ctx:ZCodeParser.Prime_para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_decl.
    def visitPara_decl(self, ctx:ZCodeParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_body.
    def visitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx:ZCodeParser.Var_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_expr.
    def visitAssign_expr(self, ctx:ZCodeParser.Assign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#recur_idx_expr.
    def visitRecur_idx_expr(self, ctx:ZCodeParser.Recur_idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_part.
    def visitIf_part(self, ctx:ZCodeParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_part.
    def visitElif_part(self, ctx:ZCodeParser.Elif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_part.
    def visitElse_part(self, ctx:ZCodeParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#str_expr.
    def visitStr_expr(self, ctx:ZCodeParser.Str_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cmp_expr.
    def visitCmp_expr(self, ctx:ZCodeParser.Cmp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#log2_expr.
    def visitLog2_expr(self, ctx:ZCodeParser.Log2_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_expr.
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mul_expr.
    def visitMul_expr(self, ctx:ZCodeParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#log1_expr.
    def visitLog1_expr(self, ctx:ZCodeParser.Log1_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#idx_expr.
    def visitIdx_expr(self, ctx:ZCodeParser.Idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#val_expr.
    def visitVal_expr(self, ctx:ZCodeParser.Val_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_expr.
    def visitVar_expr(self, ctx:ZCodeParser.Var_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_expr.
    def visitCall_expr(self, ctx:ZCodeParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_expr.
    def visitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prime_arg_list.
    def visitPrime_arg_list(self, ctx:ZCodeParser.Prime_arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#concat_operator.
    def visitConcat_operator(self, ctx:ZCodeParser.Concat_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cmp_operator.
    def visitCmp_operator(self, ctx:ZCodeParser.Cmp_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#log2_operator.
    def visitLog2_operator(self, ctx:ZCodeParser.Log2_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_operator.
    def visitAdd_operator(self, ctx:ZCodeParser.Add_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mul_operator.
    def visitMul_operator(self, ctx:ZCodeParser.Mul_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#log1_operator.
    def visitLog1_operator(self, ctx:ZCodeParser.Log1_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_operator.
    def visitSign_operator(self, ctx:ZCodeParser.Sign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#idx_operator.
    def visitIdx_operator(self, ctx:ZCodeParser.Idx_operatorContext):
        return self.visitChildren(ctx)



del ZCodeParser