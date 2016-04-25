# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pascalLoveParser
import sys

#main method and entry point of application
def main(argv):
    """Main method calling a single debugger for an input script"""
    parser = pascalLoveParser
    parser.parse(argv)

if __name__ == '__main__':
    main(sys.argv)
