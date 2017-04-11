import sys
from core import *


def main():
  memory = TLONGlobalMemory__()
  file_param = False
  input_stream = None

  if len(sys.argv) > 1:
    file_param = True
    input_stream = FileStream(sys.argv[1])
  else:
    input_stream = InputStream(sys.stdin.readline())

  lexer = TLONLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = TLONParser(token_stream)
  tree = parser.parse()

  visitor = Visitor(memory)
  visitor.visit(tree)


if __name__ == '__main__':
  main()