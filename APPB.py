import sys

''' Import Antlr from build output folder'''
sys.path.insert(1, 'Antlr/output')
from antlr4 import *
from popLexer import popLexer
from popParser import popParser
from popVisitor import popVisitor

def main(argv):
    
    # Launch arg input
    if len(argv) < 2:
      print("Please input your popfile file path as a launch argument!")
      print("\tpython .\\APPB.py .\\Examples\\mvm_bigrock_sigdemo.pop")
      print("\tpython .\\APPB.py .\\Examples\\simple_example.pop")
      print()
      return
    
    # Input file as FileStream
    input_stream = FileStream(argv[1])

    ### pop Lexer ###
    lexer = popLexer(input_stream)
    stream = CommonTokenStream(lexer)

    ### pop Parser ###
    parser = popParser(stream)

    # Count and display number of syntax errors.
    syntax_error_count = parser.getNumberOfSyntaxErrors()
    if syntax_error_count > 0:
        print(f"Found {syntax_error_count} syntax errors!")

    ### Build Parse Tree ###
    tree = parser.pop()

    ### Visitor ###
    visitor = popVisitor()
    visitor.visit(tree)

    return

if __name__ == '__main__':
  main(sys.argv)