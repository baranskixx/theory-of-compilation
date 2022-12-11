class Node(object):
    def print_indent(self, depth):
        print("|    " * depth, end='')
        

class Error(Node):
    def __init__(self):
        pass

# USED FOR p_start and p_keyword
class Instruction(Node):
    def __init__(self, instructions):
        self.instructions = instructions

class BinExpression(Node):
    def __init__(self, left_side, op, right_side):
        self.op = op
        self.left_side = left_side
        self.right_side = right_side

# PRINT

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

class Printables(Node):
    def __init__(self, values):
        self.values = values

# IF

class IfCondition(Node):
    def __init__(self, if_cond, if_body, else_body):
        self.if_cond = if_cond
        self.if_body = if_body
        self.else_body = else_body

# ASSIGNING

class Assign(Node):
    def __init__(self, left_side, op, right_side):
        self.op = op
        self.left_side = left_side
        self.right_side = right_side 

class Assignable(Node):
    def __init__(self, id, index):
        self.id = id
        self.index = index

# LOOPS

class ForLoop(Node):
    def __init__(self, var, loop_start, loop_end, loop_body):
        self.var = var
        self.loop_start = loop_start
        self.loop_end = loop_end
        self.loop_body = loop_body

class WhileLoop(Node):
    def __init__(self, loop_cond, loop_body) -> None:
        self.loop_cond = loop_cond
        self.loop_body = loop_body

class Continue(Node):
    def __init__(self):
        pass
 
class Break(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(self, result):
        self.result = result

# MATRICES

class Matrix(Node):
    def __init__(self, val):
        self.val = val

class MatrixCreate(Node):
    def __init__(self, func_name, matrix_size):
        self.func_name = func_name
        self.matrix_size = matrix_size

class Transpose(Node):
    def __init__(self, matrix):
        self.matrix = matrix

# Variables

class ID(Node):
    def __init__(self, id):
        self.id = id

class IntNum(Node):
    def __init__(self, val):
        self.val = val

class FloatNum(Node):
    def __init__(self, val):
        self.val = val

class String(Node):
    def __init__(self, val):
        self.val = val

# OPERATORS

def Uminus(Node):
    def __init__(self, val):
        self.val = val

# ERROR

class Error(Node):
    def __init__(self):
        pass
