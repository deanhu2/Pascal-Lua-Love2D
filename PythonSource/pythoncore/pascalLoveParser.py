from pascalLexer import pascalLexer
from pascalListener import pascalListener
from pascalParser import pascalParser
from antlr4 import *

class pascalLoveParser(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
def __init__(self): # this method creates the class object.
    pass
		
		

def parse(argv):
    #input = FileStream(argv[1])
    if len(argv)==1:
        filename=argv[0]
    input = FileStream("add.pas")
    lexer = pascalLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pascalParser(stream)
    tree = parser.program()
    printer = pascalListener(tree,filename)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

		
