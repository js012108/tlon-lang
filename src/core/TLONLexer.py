# Generated from /home/eccarrilloe/projects/python/tlon-lang/src/core/grammar/TLON.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0127\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!")
        buf.write("\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3*\3*\7*\u00ee")
        buf.write("\n*\f*\16*\u00f1\13*\3+\6+\u00f4\n+\r+\16+\u00f5\3,\6")
        buf.write(",\u00f9\n,\r,\16,\u00fa\3,\3,\7,\u00ff\n,\f,\16,\u0102")
        buf.write("\13,\3,\3,\6,\u0106\n,\r,\16,\u0107\5,\u010a\n,\3-\3-")
        buf.write("\3-\3-\7-\u0110\n-\f-\16-\u0113\13-\3-\3-\3.\3.\7.\u0119")
        buf.write("\n.\f.\16.\u011c\13.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\2\2\62\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62\3\2\t\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\5\2\f\f\17\17$$\4\2\f\f\17\17")
        buf.write("\5\2\13\13\17\17\"\"\3\2\f\f\2\u012f\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\3c\3\2\2\2\5f\3\2\2\2\7i\3\2\2\2\tl\3\2\2\2")
        buf.write("\13o\3\2\2\2\rq\3\2\2\2\17s\3\2\2\2\21v\3\2\2\2\23y\3")
        buf.write("\2\2\2\25{\3\2\2\2\27}\3\2\2\2\31\177\3\2\2\2\33\u0081")
        buf.write("\3\2\2\2\35\u0083\3\2\2\2\37\u0085\3\2\2\2!\u0087\3\2")
        buf.write("\2\2#\u0089\3\2\2\2%\u008b\3\2\2\2\'\u008d\3\2\2\2)\u008f")
        buf.write("\3\2\2\2+\u0091\3\2\2\2-\u0093\3\2\2\2/\u0095\3\2\2\2")
        buf.write("\61\u0097\3\2\2\2\63\u0099\3\2\2\2\65\u009e\3\2\2\2\67")
        buf.write("\u00a4\3\2\2\29\u00a8\3\2\2\2;\u00ab\3\2\2\2=\u00b0\3")
        buf.write("\2\2\2?\u00b6\3\2\2\2A\u00ba\3\2\2\2C\u00be\3\2\2\2E\u00c1")
        buf.write("\3\2\2\2G\u00c9\3\2\2\2I\u00cd\3\2\2\2K\u00d5\3\2\2\2")
        buf.write("M\u00de\3\2\2\2O\u00e4\3\2\2\2Q\u00e9\3\2\2\2S\u00eb\3")
        buf.write("\2\2\2U\u00f3\3\2\2\2W\u0109\3\2\2\2Y\u010b\3\2\2\2[\u0116")
        buf.write("\3\2\2\2]\u011f\3\2\2\2_\u0123\3\2\2\2a\u0125\3\2\2\2")
        buf.write("cd\7~\2\2de\7~\2\2e\4\3\2\2\2fg\7(\2\2gh\7(\2\2h\6\3\2")
        buf.write("\2\2ij\7?\2\2jk\7?\2\2k\b\3\2\2\2lm\7#\2\2mn\7?\2\2n\n")
        buf.write("\3\2\2\2op\7@\2\2p\f\3\2\2\2qr\7>\2\2r\16\3\2\2\2st\7")
        buf.write("@\2\2tu\7?\2\2u\20\3\2\2\2vw\7>\2\2wx\7?\2\2x\22\3\2\2")
        buf.write("\2yz\7-\2\2z\24\3\2\2\2{|\7/\2\2|\26\3\2\2\2}~\7,\2\2")
        buf.write("~\30\3\2\2\2\177\u0080\7\61\2\2\u0080\32\3\2\2\2\u0081")
        buf.write("\u0082\7\'\2\2\u0082\34\3\2\2\2\u0083\u0084\7`\2\2\u0084")
        buf.write("\36\3\2\2\2\u0085\u0086\7#\2\2\u0086 \3\2\2\2\u0087\u0088")
        buf.write("\7?\2\2\u0088\"\3\2\2\2\u0089\u008a\7*\2\2\u008a$\3\2")
        buf.write("\2\2\u008b\u008c\7+\2\2\u008c&\3\2\2\2\u008d\u008e\7}")
        buf.write("\2\2\u008e(\3\2\2\2\u008f\u0090\7\177\2\2\u0090*\3\2\2")
        buf.write("\2\u0091\u0092\7]\2\2\u0092,\3\2\2\2\u0093\u0094\7_\2")
        buf.write("\2\u0094.\3\2\2\2\u0095\u0096\7.\2\2\u0096\60\3\2\2\2")
        buf.write("\u0097\u0098\7<\2\2\u0098\62\3\2\2\2\u0099\u009a\7v\2")
        buf.write("\2\u009a\u009b\7t\2\2\u009b\u009c\7w\2\2\u009c\u009d\7")
        buf.write("g\2\2\u009d\64\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\66\3\2\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7k\2\2\u00a6\u00a7\7n\2\2\u00a78\3\2\2\2\u00a8\u00a9")
        buf.write("\7k\2\2\u00a9\u00aa\7h\2\2\u00aa:\3\2\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af<\3\2\2\2\u00b0\u00b1\7y\2\2\u00b1\u00b2")
        buf.write("\7j\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5>\3\2\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7i\2\2\u00b9@\3\2\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7t\2\2\u00bdB\3")
        buf.write("\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0D\3")
        buf.write("\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7p\2\2\u00c8F\3\2\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7f\2\2\u00ccH\3")
        buf.write("\2\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7q\2\2\u00d4J\3\2\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7o\2\2\u00d7\u00d8\7r\2\2\u00d8\u00d9")
        buf.write("\7q\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7t\2\2\u00ddL\3\2\2\2\u00de\u00df")
        buf.write("\7f\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2")
        buf.write("\7f\2\2\u00e2\u00e3\7g\2\2\u00e3N\3\2\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7f\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8P\3\2\2\2\u00e9\u00ea\7\60\2\2\u00eaR\3\2")
        buf.write("\2\2\u00eb\u00ef\t\2\2\2\u00ec\u00ee\t\3\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0T\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2")
        buf.write("\u00f4\t\4\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6V\3\2\2")
        buf.write("\2\u00f7\u00f9\t\4\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u0100\7\60\2\2\u00fd\u00ff\t\4\2")
        buf.write("\2\u00fe\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u010a\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0105\7\60\2\2\u0104\u0106\t\4\2")
        buf.write("\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109")
        buf.write("\u00f8\3\2\2\2\u0109\u0103\3\2\2\2\u010aX\3\2\2\2\u010b")
        buf.write("\u0111\7$\2\2\u010c\u0110\n\5\2\2\u010d\u010e\7$\2\2\u010e")
        buf.write("\u0110\7$\2\2\u010f\u010c\3\2\2\2\u010f\u010d\3\2\2\2")
        buf.write("\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115")
        buf.write("\7$\2\2\u0115Z\3\2\2\2\u0116\u011a\7%\2\2\u0117\u0119")
        buf.write("\n\6\2\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011d\u011e\b.\2\2\u011e\\\3\2\2")
        buf.write("\2\u011f\u0120\t\7\2\2\u0120\u0121\3\2\2\2\u0121\u0122")
        buf.write("\b/\2\2\u0122^\3\2\2\2\u0123\u0124\t\b\2\2\u0124`\3\2")
        buf.write("\2\2\u0125\u0126\13\2\2\2\u0126b\3\2\2\2\f\2\u00ef\u00f5")
        buf.write("\u00fa\u0100\u0107\u0109\u010f\u0111\u011a\3\b\2\2")
        return buf.getvalue()


class TLONLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OR = 1
    AND = 2
    EQ = 3
    NEQ = 4
    GT = 5
    LT = 6
    GTEQ = 7
    LTEQ = 8
    PLUS = 9
    MINUS = 10
    MULT = 11
    DIV = 12
    MOD = 13
    POW = 14
    NOT = 15
    ASSIGN = 16
    OPAR = 17
    CPAR = 18
    OBRACE = 19
    CBRACE = 20
    OKEY = 21
    CKEY = 22
    COMMA = 23
    POINTS = 24
    TRUE = 25
    FALSE = 26
    NIL = 27
    IF = 28
    ELSE = 29
    WHILE = 30
    LOG = 31
    FOR = 32
    IN = 33
    FUNCION = 34
    END = 35
    RETORNO = 36
    IMPORT = 37
    FROM = 38
    ASTERISC = 39
    POINT = 40
    ID = 41
    INT = 42
    FLOAT = 43
    STRING = 44
    COMMENT = 45
    SPACE = 46
    NEWLINE = 47
    OTHER = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'!'", "'='", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "','", "':'", "'true'", "'false'", 
            "'nil'", "'if'", "'else'", "'while'", "'log'", "'for'", "'in'", 
            "'funcion'", "'end'", "'retorno'", "'importar'", "'desde'", 
            "'todo'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "OR", "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", 
            "MINUS", "MULT", "DIV", "MOD", "POW", "NOT", "ASSIGN", "OPAR", 
            "CPAR", "OBRACE", "CBRACE", "OKEY", "CKEY", "COMMA", "POINTS", 
            "TRUE", "FALSE", "NIL", "IF", "ELSE", "WHILE", "LOG", "FOR", 
            "IN", "FUNCION", "END", "RETORNO", "IMPORT", "FROM", "ASTERISC", 
            "POINT", "ID", "INT", "FLOAT", "STRING", "COMMENT", "SPACE", 
            "NEWLINE", "OTHER" ]

    ruleNames = [ "OR", "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", 
                  "PLUS", "MINUS", "MULT", "DIV", "MOD", "POW", "NOT", "ASSIGN", 
                  "OPAR", "CPAR", "OBRACE", "CBRACE", "OKEY", "CKEY", "COMMA", 
                  "POINTS", "TRUE", "FALSE", "NIL", "IF", "ELSE", "WHILE", 
                  "LOG", "FOR", "IN", "FUNCION", "END", "RETORNO", "IMPORT", 
                  "FROM", "ASTERISC", "POINT", "ID", "INT", "FLOAT", "STRING", 
                  "COMMENT", "SPACE", "NEWLINE", "OTHER" ]

    grammarFileName = "TLON.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


