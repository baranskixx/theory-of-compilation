import scanner
import ply.yacc as yacc
import AST

tokens = scanner.tokens
precedence = (
    ('nonassoc', 'IF'),
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
    """start : instructions"""
    p[0] = p[1]

def p_instructions(p):
    """ instructions : instr
                    | instructions instr"""
    if len(p) == 2:
        p[0] = AST.Instruction(None, p[1])
    else:
        p[0] = AST.Instruction(p[1], p[2])

def p_instr(p):
    """ instr : instr_assign ';'
                | statement ';'
                | '{' instructions '}'
                """
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_instr_if(p):
    """ instr : IF '(' condition ')' instr %prec IF """
    p[0] = AST.If(p[3], p[5])

def p_instr_if_else(p):
    """instr : IF '(' condition ')' instr ELSE instr"""
    p[0] = AST.IfElse(p[3], p[5], p[7])

def p_instr_return(p):
    """ statement : RETURN expr"""
    p[0] = AST.Return(p[2])

def p_condition(p):
    """condition : expr '>' expr
            | expr '<' expr
            | expr EQ expr
            | expr NEQ expr
            | expr LEQ expr
            | expr GEQ expr """
    p[0] = AST.Condition(p[1], p[2], p[3])

###### LOOPS ######

def p_instr_for(p):
    """ instr : FOR id '=' range instr"""
    p[0] = AST.ForLoop(p[2], p[4], p[5])

def p_range(p):
    """range : expr ':' expr """
    p[0] = AST.Range(p[1], p[3], p.lineno(1))

def p_instr_while(p):
    """ instr : WHILE '(' expr ')' instr"""
    p[0] = AST.WhileLoop(p[3], p[5])

def p_break(p):
    """statement : BREAK"""
    p[0] = AST.Break(p.lineno[1])

def p_continue(p):
    """statement : CONTINUE"""
    p[0] = AST.Continue(p.lineno(1))

###### PRINT ######

def p_str(p):
    """str : STRING"""
    p[0] = AST.String(p[1])

def p_instr_print(p):
    """ statement : PRINT printables"""
    p[0] = AST.Print(p[2])

def p_printables(p):
    """ printables : printable
                | printables ',' printable"""
    p[0] = AST.Printables(p[1], p[3]) if len(p) == 4 else AST.Printables(None, p[1])

def p_printable(p):
    """ printable : expr"""
    p[0] = p[1]

###### ASSIGNING ######

def p_assign_operator(p):
    """assign_operator : ADDASSIGN
                    | SUBASSIGN
                    | MULASSIGN
                    | DIVASSIGN
                    | '=' 
                    """
    p[0] = p[1]

def p_instr_assign(p):
    """ instr_assign : id assign_operator expr
                | matrix_element assign_operator expr
                | vector_element assign_operator expr
    """
    p[0] = AST.Assign(p[1], p[2], p[3], p.lineno(1))

def p_id(p):
    """id : ID"""
    p[0] = AST.ID(p[1], p.lineno(1))

###### EXPRESSIONS ######

def p_trans(p):
    """trans : expr '\\''"""
    p[0] = AST.Transpose(p[1], p.lineno(1))

def p_uminus(p):
    """uminus : "-" expr %prec UMINUS"""
    p[0] = AST.Uminus(p[2], p.lineno(1))

def p_binary_expr(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr
            """
    p[0] = AST.BinExpression(p[1], p[2], p[3], p.lineno(2))
    
def p_expr(p):
    """expr : num_expr
            | matrix 
            | matrix_create
            | vector
            | uminus
            | trans
            | matrix_element
            | vector_element"""
    p[0] = p[1]

###### MATRICES ######

def p_num_expr(p):
    """ num_expr : number
                | str
                | id"""
    p[0] = p[1]

def p_matrix(p):
    """ matrix : '[' vectors ']'"""
    p[0] = p[2] 

def p_matrix_create(p):
    """ matrix_create : ZEROS '(' INTNUM ')'
                            | ONES '(' INTNUM ')'
                            | EYE '(' INTNUM ')'"""
    p[0] = AST.MatrixCreate(p[1], p[3], p.lineno(1))

###### VECTORS ######

def p_vectors(p):
    """vectors : vectors ',' vector
               | vector """
    p[0] = AST.Matrix(p[1], p[3], p.lineno(2)) if len(p) == 4 else AST.Matrix(None, p[1], p.lineno(1))

def p_vector(p):
    """vector : '[' variables ']' """
    p[0] = p[2]

###### VARIABLES ######

def p_variables(p):
    """variables : variables ',' variable
                 | variable """
    p[0] = AST.Vector(p[1], p[3], p.lineno(1)) if len(p) == 4 else AST.Vector(None, p[1], p.lineno(1))

def p_variable(p):
    """variable : number
                | id
                | element """
    p[0] = p[1]

def p_number(p):
    """ number : INTNUM
            | FLOAT"""
    p[0] = AST.Num(p[1])

def p_element(p):
    """ element : vector_element 
                | matrix_element"""
    p[0] = p[1]

def p_vector_element(p):
    """ vector_element : id "[" INTNUM "]" """
    p[0] = AST.VectorElement(p[1], p[3], p.lineno(1))

def p_matrix_element(p):
    """ matrix_element : id "[" INTNUM "," INTNUM "]" """
    p[0] = AST.MatrixElement(p[1], p[3], p[5], p.lineno(2))

parser = yacc.yacc()
