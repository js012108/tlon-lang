grammar TLON;

parse
 : block EOF
 ;

block
 : stat (stat*)
 ;

stat
 : assignment
 | if_stat
 | while_stat
 | for_stat
 | log
 | funcion
 | importar
 | retornar
 | atom SCOL
 | OTHER
 ;

assignment
 : variable ASSIGN expr SCOL
 ;

if_stat
 : IF condition_block (ELSE IF condition_block)* (ELSE stat_block)?
 ;

while_stat
 : WHILE expr stat_block
 ;

for_stat
 : FOR ID IN expr stat_block
 ;

log
 : LOG OPAR expr CPAR SCOL
 ;

funcion
 : FUNCION ID OPAR (parametro (COMMA parametro)*)? CPAR stat* END FUNCION
 ;

importar
 : IMPORT ID (POINT ID)*
 | FROM ID IMPORT ID
 ;

retornar
 : RETORNO OPAR expr CPAR SCOL
 ;

condition_block
 : expr stat_block
 ;

stat_block
 : OBRACE block? CBRACE
 | stat
 ;

array
 : OKEY (expr (COMMA expr)*)? CKEY
 | OKEY expr POINTS (expr POINTS)? expr CKEY
 ;

accessarray
 : variable OKEY expr CKEY
 ;

variable
 : ID (POINT ID)* (OPAR (expr (COMMA expr)*)? CPAR)?
 ;

parametro
 : ID (ASSIGN expr)?
 ;

expr
 : expr POW<assoc=right> expr           #powExpr
 | MINUS expr                           #unaryMinusExpr
 | NOT expr                             #notExpr
 | expr op=(MULT | DIV | MOD) expr      #multiplicationExpr
 | expr op=(PLUS | MINUS) expr          #additiveExpr
 | expr op=(LTEQ | GTEQ | LT | GT) expr #relationalExpr
 | expr op=(EQ | NEQ) expr              #equalityExpr
 | expr AND expr                        #andExpr
 | expr OR expr                         #orExpr
 | OPAR expr CPAR 						#parExpr
 | atom                                 #atomExpr
 ;

atom
 : (INT | FLOAT)  #numberAtom
 | (TRUE | FALSE) #booleanAtom
 | STRING         #stringAtom
 | array		  #arrayAtom
 | objeto		  #objetoAtom
 | accessarray    #accessToarray
 | variable		  #accessVariable
 | NIL            #nilAtom
 ;

objeto
 : OBRACE (keyvalue (COMMA keyvalue)*)? CBRACE
 ;

keyvalue
 : ID POINTS expr
 ;

OR : '||';
AND : '&&';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
POW : '^';
NOT : '!';

SCOL : ';';
ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';
OKEY : '[';
CKEY : ']';
COMMA : ',';
POINTS: ':';

TRUE : 'true';
FALSE : 'false';
NIL : 'nil';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
LOG : 'log';
FOR : 'for';
IN : 'in';
FUNCION: 'funcion';
END: 'end';
RETORNO: 'retorno';
IMPORT: 'importar';
FROM: 'desde';
ASTERISC: 'todo';
POINT: '.';

ID
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

INT
 : [0-9]+
 ;

FLOAT
 : [0-9]+ '.' [0-9]*
 | '.' [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 ;

COMMENT
 : '#' ~[\r\n]* -> skip
 ;

SPACE
 : [ \t\r\n] -> skip
 ;

OTHER
 : .
 ;