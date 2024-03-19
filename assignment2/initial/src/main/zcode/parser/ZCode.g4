// 2114988

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// PROGRAM
program: NEWLINE* decl_list EOF;

// DECLARE
decl_list: decl decl_list | decl;
decl: (variable_decl | function_decl)  NEWLINE+;

// VARIABLE DECLARE
variable_decl: explicit_decl | implicit_decl;

explicit_decl: type_decl IDENTIFIER (L_SB size_list R_SB | ) (assign_expr | );

type_decl: NUMBER | BOOL | STRING;
size_list: NUM_LIT COMMA size_list | NUM_LIT;

implicit_decl: var_decl | dynamic_decl;

var_decl: VAR IDENTIFIER assign_expr;
dynamic_decl: DYNAMIC IDENTIFIER (assign_expr | );

literals: NUM_LIT | (TRUE | FALSE) | STR_LIT | arr_lit;
arr_lit: L_SB arr_list R_SB;
arr_list: expr COMMA arr_list | expr;





// FUNCTION DECLARE
function_decl: FUNC IDENTIFIER L_RB para_list R_RB (NEWLINE* func_body | );

para_list: prime_para_list | ;
prime_para_list: para_decl COMMA prime_para_list | para_decl;
para_decl: type_decl IDENTIFIER (L_SB size_list R_SB | );

func_body: return_stmt | block_stmt;

stmt_list: stmt NEWLINE+ stmt_list | ;
stmt: var_decl_stmt | assign_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;

var_decl_stmt: variable_decl;
assign_stmt: lhs assign_expr;
if_stmt: if_part elif_list else_part;
for_stmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE* stmt;
break_stmt: BREAK;
continue_stmt: CONTINUE;
return_stmt: RETURN expr | RETURN;
call_stmt: IDENTIFIER L_RB arg_list R_RB;
block_stmt: BEGIN NEWLINE+ stmt_list END;

assign_expr: ASSIGN expr;
lhs: IDENTIFIER | recur_idx_expr;
recur_idx_expr: IDENTIFIER L_SB idx_operator R_SB;

if_part: IF L_RB expr R_RB NEWLINE* stmt;
elif_list: NEWLINE+ elif_part elif_list | ;
elif_part: ELIF L_RB expr R_RB NEWLINE* stmt;
else_part: NEWLINE+ ELSE NEWLINE* stmt | ;

 





// EXPRESSION
expr: str_expr;
str_expr: cmp_expr concat_operator cmp_expr | cmp_expr;
cmp_expr: log2_expr cmp_operator log2_expr | log2_expr;
log2_expr: log2_expr log2_operator add_expr | add_expr;
add_expr: add_expr add_operator mul_expr | mul_expr;
mul_expr: mul_expr mul_operator log1_expr | log1_expr;
log1_expr: log1_operator log1_expr | sign_expr;
sign_expr: sign_operator sign_expr | idx_expr;
idx_expr: var_expr L_SB idx_operator R_SB | val_expr;
val_expr: literals | IDENTIFIER | call_expr | sub_expr;
var_expr: IDENTIFIER | call_expr;
call_expr: IDENTIFIER L_RB arg_list R_RB;
sub_expr: L_RB expr R_RB;

arg_list: prime_arg_list | ;
prime_arg_list: expr COMMA prime_arg_list | expr;

concat_operator: CONCAT;
cmp_operator: EQ_NUM | NOT_EQ | LESS | LESS_EQ | GREATER | GREATER_EQ | EQ_STR;
log2_operator: AND | OR;
add_operator: ADD | SUB;
mul_operator: MUL | DIV | MOD;
log1_operator: NOT;
sign_operator: SUB;
idx_operator: expr | expr COMMA idx_operator;



// COMMENTS
COMMENT: '##' ~[\n\r]* -> skip;


// KEYWORDS
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// OPERATORS
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ_NUM: '=';
ASSIGN: '<-';
NOT_EQ: '!=';
LESS: '<';
LESS_EQ: '<=';
GREATER: '>';
GREATER_EQ: '>=';
CONCAT: '...';
EQ_STR: '==';

// SEPARATORS
L_RB: '(';
R_RB: ')';
L_SB : '[';
R_SB : ']';
COMMA: ',';
NEWLINE: '\n';


// IDENTIFIERS
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

// LITERALS
NUM_LIT: INT DEC? EXP?;
fragment INT: [0-9]+;
fragment DEC: '.' INT?;
fragment EXP: ('e'|'E') ('+'|'-')? INT;


STR_LIT: '"' (ESC_SEQ | DOUBLE_QUOTE | OTHER_CHARS)* '"' {self.text = self.text[1:-1]};
fragment ESC_SEQ: [\b\t\n\r\f'\\];
fragment DOUBLE_QUOTE: '\'"';
fragment OTHER_CHARS: ~('"' | '\\');

WS : [ \t\b\f\r]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE: '"' (~'"')*? ('\\' ~[btnfr'\\]) .* {
    output_str = ""
    escape = False

    for char in self.text[1:]:
        if escape:
            output_str += char
            if char not in ['b', 't', 'n', 'r', 'f', '\\', '\'']:
                break
            
            escape = False
        else:
            if char == '\\':
                escape = True
            output_str += char

    raise IllegalEscape(output_str)
};
UNCLOSE_STRING: '"' (~ ["\n\r] | '\'"')* {raise UncloseString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};
