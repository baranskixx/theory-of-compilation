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
            | instructions"""


def p_instructions(p):
    """ instructions : instr
                    | instructions instr"""


def p_instr(p):
    """ instr : instr_if
                | instr_for
                | instr_while
                | instr_return ';'
                | instr_assign ';'
                | instr_print ';'
                | break ';'
                | continue ';' """


def p_scope(p):
    """ instr : '{' instructions '}' """


def p_instr_if(p):
    """ instr_if : IF '(' expr ')' instr %prec IFX
                    | IF '(' expr ')' instr ELSE instr"""


def p_instr_return(p):
    """ instr_return : RETURN
                        | RETURN expr"""

###### LOOPS ######

def p_instr_for(p):
    """ instr_for : FOR id '=' expr ':' expr instr"""


def p_instr_while(p):
    """ instr_while : WHILE '(' expr ')' instr"""


def p_break(p):
    """break : BREAK"""


def p_continue(p):
    """continue : CONTINUE"""

###### PRINT ######

def p_str(p):
    """str : STRING"""


def p_instr_print(p):
    """ instr_print : PRINT printables"""


def p_printables(p):
    """ printables : printable
                | printables ',' printable"""


def p_printable(p):
    """ printable : expr
                | str"""

###### ASSIGNING ######

def p_instr_assign(p):
    """ instr_assign : assignable '=' expr
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
