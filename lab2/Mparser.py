import scanner
import ply.yacc as yacc

tokens = scanner.tokens
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('right', 'MULASSIGN', 'DIVASSIGN', 'SUBASSIGN', 'ADDASSIGN'),
    ('nonassoc', '<', '>', 'GEQ', 'LEQ', 'EQ', 'NEQ'),
    ('left', '+', '-'),
    ('left', 'DOTADD', 'DOTSUB'),
    ('left', '*', '/'),
    ('left', 'DOTMUL', 'DOTDIV'),
    ('right', 'UMINUS'),
    ('left', "'"),
)

###### ERROR ######

def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(
            p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

###### START ######

def p_start(p):
    """start :
            | keywords"""


def p_keywords(p):
    """ keywords : keyword
                    | keywords keyword"""


def p_keyword(p):
    """ keyword : keyword_if
                | keyword_for
                | keyword_while
                | keyword_return ';'
                | keyword_assign ';'
                | keyword_print ';'
                | break ';'
                | continue ';' """


def p_scope(p):
    """ keyword : '{' keywords '}' """


def p_keyword_if(p):
    """ keyword_if : IF '(' expr ')' keyword %prec IFX
                    | IF '(' expr ')' keyword ELSE keyword"""


def p_keyword_return(p):
    """ keyword_return : RETURN
                        | RETURN expr"""

###### LOOPS ######

def p_keyword_for(p):
    """ keyword_for : FOR id '=' expr ':' expr keyword"""


def p_keyword_while(p):
    """ keyword_while : WHILE '(' expr ')' keyword"""


def p_break(p):
    """break : BREAK"""


def p_continue(p):
    """continue : CONTINUE"""

###### PRINT ######

def p_str(p):
    """str : STRING"""


def p_keyword_print(p):
    """ keyword_print : PRINT printables"""


def p_printables(p):
    """ printables : printable
                | printables ',' printable"""


def p_printable(p):
    """ printable : expr
                | str"""

###### ASSIGNING ######

def p_keyword_assign(p):
    """ keyword_assign : assignable '=' expr
                    | assignable ADDASSIGN expr
                    | assignable SUBASSIGN expr
                    | assignable MULASSIGN expr
                    | assignable DIVASSIGN expr"""


def p_id(p):
    """id : ID"""


def p_assignable(p):
    """ assignable : id
                    | matrix_element
                    | vector_element"""

###### EXPRESSIONS ######

def p_expr_trans(p):
    """expr : expr '\\''"""


def p_expr_nested(p):
    """expr : '(' expr ')' """


def p_expr_matrix_create(p):
    """expr : matrix_create '(' expr ')'"""


def p_expr_minus(p):
    """expr : "-" expr %prec UMINUS"""


def p_expr_literal(p):
    """expr : assignable
            | matrix"""


def p_expr_int(p):
    """expr : INTNUM"""


def p_expr_float(p):
    """expr : FLOAT"""


def p_binary_expr(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr
            | expr '>' expr
            | expr '<' expr
            | expr EQ expr
            | expr NEQ expr
            | expr LEQ expr
            | expr GEQ expr 
            """
    
###### MATRICES ######

def p_matrix(p):
    """ matrix : '[' vectors ']'"""


def p_matrix_create(p):
    """ matrix_create : ZEROS
                            | ONES
                            | EYE"""


def p_matrix_element(p):
    """ matrix_element : id "[" INTNUM "," INTNUM "]" """

###### VECTORS ######

def p_vectors(p):
    """vectors : vectors ',' vector
               | vector """


def p_vector(p):
    """vector : '[' variables ']' """


def p_vector_element(p):
    """ vector_element : id "[" INTNUM "]" """

###### VARIABLES ######

def p_variables(p):
    """variables : variables ',' variable
                 | variable """


def p_variable(p):
    """variable : INTNUM
                | FLOAT
                | assignable """


parser = yacc.yacc()
