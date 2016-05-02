from pascalLexer import pascalLexer
from pascalListener import pascalListener
from pascalParser import pascalParser
from antlr4 import *
import sys

class pascalLoveParser(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
def __init__(self): # this method creates the class object.
    pass
		
		
#function used to parse an input file for translation
def parse(argv):
    if len(sys.argv) > 1:
        input = FileStream(argv[1])
        lexer = pascalLexer(input)
        stream = CommonTokenStream(lexer)
        parser = pascalParser(stream)
        tree = parser.program()
        printer = pascalListener(tree,input)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
    else:
        print('Error : Expected a valid .pas or .pua input file parameter but got none.')
        print('Format : Python3 main.py <inputfile>')

		
