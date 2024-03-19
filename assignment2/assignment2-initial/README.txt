Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite

intro 3, lexer 8, parser 8, oop 8, fp 8, ast 10

ctx.index().accept(self) = self.visit(ctx.index())