Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite

1) list of (statement SEMI), null:
BNF: stmtlist -> (stmt SEMI) stmtlist | epsilon
EBNF: stmtlist -> (stmt SEMI)*

2) list of (statement SEMI), not null:
BNF: stmtlist -> (stmt SEMI) stmtlist | (stmt SEMI)
EBNF: stmtlist -> (stmt SEMI)+

3) list of ID seperate other by COMMA, not null:
BNF: idlist -> ID COMMA idlist | ID
EBNF: idlist -> ID (ID COMMA)*

4) list of expression seperate other by COMMA, null:
BNF: explist -> expprime | epsilon
    expprime -> exp COMMA expprime | exp
EBNF: explist -> (exp (COMMA exp)*)?

1) Declaration
2) Statement
3) Expression
- How many operators?
- Priority of operators? (first -> low priority)
- Combination of operators? ()

## Lexer
# Comment: ##abc \n abc => ?
# Number literal: 000 => ?
# String: "abc"abc" => ?
# String: "abc'"abc" => ?

## Parser
# Array: number a[true,1] <- [2,3] => ?
# main 