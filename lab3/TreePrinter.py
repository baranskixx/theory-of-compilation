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
        for e in self.expr:
            e.printTree(indent + 1)
    
    @addToClass(AST.IfCondition)
    def printTree(self, indent):
        self.print_indent(indent)
        print("IF")
        self.if_cond.printTree(indent + 1)
        self.if_body.printTree(indent + 1)
        if self.else_body is not None:
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

    @addToClass(AST.Assignable)
    def printTree(self, indent):
        self.id.printTree(indent)
        if self.index is not None:
            self.print_indent(indent)
            print("REF")
            for i in self.index:
                self.print_indent(indent + 1)
                print(i)

    # LOOPS

    @addToClass(AST.ForLoop)
    def printTree(self, indent):
        self.print_indent(indent)
        print("FOR")
        self.var.printTree(indent + 1)
        self.print_indent(indent + 1)
        print("RANGE")
        self.loop_start.printTree(indent + 2)

        self.loop_end.printTree(indent + 2)
        self.loop_body.printTree(indent + 1)

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
        print("VECTOR")
        for row in self.val:
            self.print_indent(indent + 1)
            print("VECTOR")
            for elem in row:
                self.print_indent(indent + 2)
                print(elem)

    @addToClass(AST.MatrixCreate)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.func_name)
        self.matrix_size.printTree(indent + 1)

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

    @addToClass(AST.IntNum)
    def printTree(self, indent):
        self.print_indent(indent)
        print(self.val)
    
    @addToClass(AST.FloatNum)
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