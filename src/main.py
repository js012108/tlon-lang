from antlr4 import *
from core import *


def main():
  print ('----- LangTLON v1.0 -----')
  print ()

  memory = TLONGlobalMemory__()

  if len(sys.argv) > 1:
    try:
      input_stream = FileStream(sys.argv[1])
    except Exception as e:
      raise Exception('File not Found.')

    lexer = TLONLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TLONParser(token_stream)
    tree = parser.from_file()

    visitor = Visitor(memory)
    visitor.visit(tree)

  else:
    while True:
      print('>>> ', end='', flush=True)
      input_data = sys.stdin.readline().strip()
      tabs = input_data.count('{') + input_data.count('funcion') - \
             input_data.count('}') - input_data.count('end')

      if 'exit()' in input_data:
        print ('Message: Console terminated')
        break

      while tabs > 0:
        print ('... ', end='', flush=True)
        input_data = input_data + sys.stdin.readline()
        tabs = input_data.count('{') + input_data.count('funcion') - input_data.count('}') - input_data.count('end')

      input_stream = InputStream(input_data)

      lexer = TLONLexer(input_stream)
      token_stream = CommonTokenStream(lexer)
      parser = TLONParser(token_stream)
      tree = parser.parse()

      visitor = Visitor(memory)
      result = visitor.visit(tree)

      if result is not None:
        print (result)


if __name__ == '__main__':
  main()