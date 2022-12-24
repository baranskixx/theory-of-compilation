from collections import defaultdict
from functools import reduce

ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

ttype['+']["int"]["int"] = "int"
ttype['-']["int"]["int"] = "int"
ttype['*']["int"]["int"] = "int"
ttype['/']["int"]["int"] = "int"
ttype['<']["int"]["int"] = "logic"
ttype['>']["int"]["int"] = "logic"
ttype["<="]["int"]["int"] = "logic"
ttype[">="]["int"]["int"] = "logic"
ttype["=="]["int"]["int"] = "logic"
ttype["!="]["int"]["int"] = "logic"

ttype['+']["int"]["float"] = "float"
ttype['-']["int"]["float"] = "float"
ttype['*']["int"]["float"] = "float"
ttype['/']["int"]["float"] = "float"
ttype['<']["int"]["float"] = "logic"
ttype['>']["int"]["float"] = "logic"
ttype["<="]["int"]["float"] = "logic"
ttype[">="]["int"]["float"] = "logic"
ttype["=="]["int"]["float"] = "logic"
ttype["!="]["int"]["float"] = "logic"

ttype['+']["float"]["int"] = "float"
ttype['-']["float"]["int"] = "float"
ttype['*']["float"]["int"] = "float"
ttype['/']["float"]["int"] = "float"
ttype['<']["float"]["int"] = "logic"
ttype['>']["float"]["int"] = "logic"
ttype["<="]["float"]["int"] = "logic"
ttype[">="]["float"]["int"] = "logic"
ttype["=="]["float"]["int"] = "logic"
ttype["!="]["float"]["int"] = "logic"

ttype['+']["float"]["float"] = "float"
ttype['-']["float"]["float"] = "float"
ttype['*']["float"]["float"] = "float"
ttype['/']["float"]["float"] = "float"
ttype['<']["float"]["float"] = "logic"
ttype['>']["float"]["float"] = "logic"
ttype["<="]["float"]["float"] = "logic"
ttype[">="]["float"]["float"] = "logic"
ttype["=="]["float"]["float"] = "logic"
ttype["!="]["float"]["float"] = "logic"

ttype['+']['vector']['vector'] = 'vector'
ttype['-']['vector']['vector'] = 'vector'
ttype['*']['vector']['vector'] = 'vector'
ttype['/']['vector']['vector'] = 'vector'
ttype['+=']['vector']['vector'] = 'vector'
ttype['-=']['vector']['vector'] = 'vector'
ttype['*=']['vector']['vector'] = 'vector'
ttype['/=']['vector']['vector'] = 'vector'

ttype['.+']['vector']['vector'] = 'vector'
ttype['.+']['vector']['int'] = 'vector'
ttype['.+']['vector']['float'] = 'vector'
ttype['.+']['int']['vector'] = 'vector'
ttype['.+']['float']['vector'] = 'vector'

ttype['.-']['vector']['vector'] = 'vector'
ttype['.-']['vector']['int'] = 'vector'
ttype['.-']['vector']['float'] = 'vector'
ttype['.-']['int']['vector'] = 'vector'
ttype['.-']['float']['vector'] = 'vector'

ttype['.*']['vector']['vector'] = 'vector'
ttype['.*']['vector']['int'] = 'vector'
ttype['.*']['vector']['float'] = 'vector'
ttype['.*']['int']['vector'] = 'vector'
ttype['.*']['float']['vector'] = 'vector'

ttype['./']['vector']['vector'] = 'vector'
ttype['./']['vector']['int'] = 'vector'
ttype['./']['vector']['float'] = 'vector'
ttype['./']['int']['vector'] = 'vector'
ttype['./']['float']['vector'] = 'vector'

ttype['\'']['vector'][None] = 'vector'
ttype['-']['vector'][None] = 'vector'
ttype['-']['int'][None] = 'int'
ttype['-']['float'][None] = 'float'
ttype['+']['string']['string'] = 'string'



class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

class TypeChecker(NodeVisitor):
    def init_visit(self):
        
        
