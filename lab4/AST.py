from copy import copy

class Node(object):
    def print_indent(self, depth):
        print("|    " * depth, end='')
        
# USED FOR p_start and p_keyword

class Instruction(Node):
    def __init__(self, instructions, last_instruction):
        if instructions is None:
            self.instructions = []
        else:
            self.instructions = instructions.instructions
        
        self.instructions.append(last_instruction)


class BinExpression(Node):
    def __init__(self, left_side, op, right_side, line):
        self.op = op
        self.left_side = left_side
        self.right_side = right_side
        self.line = line

# PRINT

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

class Printables(Node):
    def __init__(self, values, val):
        self.values = values.values if values  else []
        self.values.append(val)

# IF

class Condition(Node):
    def __init__(self, left_side, op, right_side, line):
        self.left_side = left_side
        self.right_side = right_side
        self.op = op
        self.line = line

class If(Node):
    def __init__(self, if_cond, if_body):
        self.if_cond = if_cond
        self.if_body = if_body

class IfElse(Node):
    def __init__(self, if_cond, if_body, else_body):
        self.if_cond = if_cond
        self.if_body = if_body
        self.else_body = else_body

# ASSIGNING

class Assign(Node):
    def __init__(self, left_side, op, right_side, line):
        self.op = op
        self.left_side = left_side
        self.right_side = right_side 
        self.line = line

# LOOPS

class Range(Node):
    def __init__(self, start, end, line):
        self.start = start
        self.end = end
        self.line = line

class ForLoop(Node):
    def __init__(self, var, _range, loop_body):
        self.var = var
        self._range = _range
        self.loop_body = loop_body

class WhileLoop(Node):
    def __init__(self, loop_cond, loop_body) -> None:
        self.loop_cond = loop_cond
        self.loop_body = loop_body

class Continue(Node):
    def __init__(self, line):
        self.line = line
 
class Break(Node):
    def __init__(self, line):
        self.line = line

class Return(Node):
    def __init__(self, result):
        self.result = result

# MATRICES

class Matrix(Node):
    def __init__(self, matrix, vector, line):
        self.matrix = copy(matrix.matrix) if matrix else []
        self.matrix.append(vector)
        self.line = line

class Vector(Node):
    def __init__(self, vector, elem, line):
        self.vector = copy(vector.vector) if vector is not None else []
        self.vector.append(elem)
        self.line = line


class MatrixCreate(Node):
    def __init__(self, func_name, matrix_size, line):
        self.func_name = func_name
        self.matrix_size = matrix_size
        self.line = line

class Transpose(Node):
    def __init__(self, matrix, line):
        self.matrix = matrix
        self.line = line

# Variables

class Variable(Node):
    def __init__(self, name, line):
        self.name = name
        self.line = line

class ID(Node):
    def __init__(self, id, line):
        self.id = id
        self.line = line

class Num(Node):
    def __init__(self, val):
        self.val = val

class String(Node):
    def __init__(self, val):
        self.val = val

class VectorElement(Node):
    def __init__(self, id, index, line):
        self.id = id
        self.index = index
        self.line = line


class MatrixElement(Node):
    def __init__(self, id, x, y, line):
        self.id = id
        self.x = x
        self.y = y
        self.line = line

# OPERATORS

def Uminus(Node):
    def __init__(self, val, line):
        self.val = val
        self.line = line

# ERROR

class Error(Node):
    def __init__(self):
        pass
