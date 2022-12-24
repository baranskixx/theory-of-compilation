from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    # @addToClass(AST.Node)
    # def printTree(self, indent):
    #     raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Instruction)
    def printTree(self, indent):
        for instr in self.instructions:
            instr.printTree(indent)

    @addToClass(AST.BinExpression)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.op)
        self.left_side.printTree(indent + 1)
        self.right_side.printTree(indent + 1)

    # PRINT
    @addToClass(AST.Print)
    def printTree(self, indent):
        self.print_indent(indent)
        print("PRINT")
        self.expr.printTree(indent + 1)

    @addToClass(AST.Printables)
    def printTree(self, indent):
        for el in self.values:
            el.printTree(indent)
    
    @addToClass(AST.If)
    def printTree(self, indent):
        self.print_indent(indent)
        print("IF")
        self.if_cond.printTree(indent + 1)
        self.if_body.printTree(indent + 1)
    
    @addToClass(AST.IfElse)
    def printTree(self, indent):
        self.print_indent(indent)
        print("IF")
        self.if_cond.printTree(indent + 1)
        self.if_body.printTree(indent + 1)
        self.print_indent(indent)
        print("ELSE")
        self.else_body.printTree(indent + 1)

    # ASSIGNING

    @addToClass(AST.Assign)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.op)
        self.left_side.printTree(indent + 1)
        self.right_side.printTree(indent + 1)
    # LOOPS

    @addToClass(AST.ForLoop)
    def printTree(self, indent):
        self.print_indent(indent)
        print("FOR")
        self.var.printTree(indent + 1)
        self._range.printTree(indent + 1)
        self.loop_body.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent):
        self.print_indent(indent)
        print("RANGE")
        self.start.printTree(indent + 1)
        self.end.printTree(indent + 1)

    @addToClass(AST.WhileLoop)
    def printTree(self, indent):
        self.print_indent(indent)
        print("WHILE")
        self.loop_cond.printTree(indent + 1)
        self.loop_body.printTree(indent + 1)
    
    @addToClass(AST.Break)
    def printTree(self, indent):
        self.print_indent(indent)
        print("BREAK")
    
    @addToClass(AST.Continue)
    def printTree(self, indent):
        self.print_indent(indent)
        print("CONTINUE")
    
    @addToClass(AST.Return)
    def printTree(self, indent):
        self.print_indent(indent)
        print("RETURN")
        if self.result is not None:
            self.result.printTree(indent + 1)

    # MATRICES
    @addToClass(AST.Matrix)
    def printTree(self, indent):
        self.print_indent(indent)
        print("MATRIX")
        for row in self.matrix:
            row.printTree(indent + 1)
    
    @addToClass(AST.Vector)
    def printTree(self, indent):
        self.print_indent(indent)
        print("VECTOR")
        for el in self.vector:
            el.printTree(indent + 1)

    @addToClass(AST.VectorElement)
    def printTree(self, indent):
        self.print_indent(indent)
        print("VECTOR ELEMENT")
        self.id.printTree(indent + 1)
        self.print_indent(indent)
        print(self.index)
    
    @addToClass(AST.MatrixElement)
    def printTree(self, indent):
        self.print_indent(indent)
        print("MATRIX ELEMENT")
        self.id.printTree(indent + 1)

        self.print_indent(indent + 1)
        print(self.x)
        self.print_indent(indent + 1)
        print(self.y)


    @addToClass(AST.MatrixCreate)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.func_name)
        print(self.matrix_size)

    @addToClass(AST.Transpose)
    def printTree(self, indent):
        self.print_indent(indent)
        print("TRANSPOSE")
        self.matrix.printTree(indent + 1)

    # VARIABLES

    @addToClass(AST.ID)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.id)

    @addToClass(AST.Num)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.val)

    @addToClass(AST.String)
    def printTree(self, indent):
        self.print_indent(indent)
        print("STRING")
        self.print_indent(indent + 1)
        print(self.val)

    # OPERATORS

    @addToClass(AST.Uminus)
    def printTree(self, indent):
        self.print_indent(indent)
        print("-")
        self.val.printTree(indent + 1)

    # ERROR

    @addToClass(AST.Error)
    def printTree(self, indent):
        pass