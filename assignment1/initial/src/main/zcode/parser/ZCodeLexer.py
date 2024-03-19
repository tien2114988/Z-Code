# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0178\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\7\2x\n\2\f\2\16\2{\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\7-\u0124\n-\f")
        buf.write("-\16-\u0127\13-\3.\3.\5.\u012b\n.\3.\5.\u012e\n.\3/\6")
        buf.write("/\u0131\n/\r/\16/\u0132\3\60\3\60\5\60\u0137\n\60\3\61")
        buf.write("\3\61\5\61\u013b\n\61\3\61\3\61\3\62\3\62\3\62\3\62\7")
        buf.write("\62\u0143\n\62\f\62\16\62\u0146\13\62\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\6\66\u0153\n\66")
        buf.write("\r\66\16\66\u0154\3\66\3\66\3\67\3\67\7\67\u015b\n\67")
        buf.write("\f\67\16\67\u015e\13\67\3\67\3\67\3\67\3\67\7\67\u0164")
        buf.write("\n\67\f\67\16\67\u0167\13\67\3\67\3\67\38\38\38\38\78")
        buf.write("\u016f\n8\f8\168\u0172\138\38\38\39\39\39\3\u015c\2:\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\2a\2c\60e\2g\2i\2k\61m\62o\63q\64\3\2\16")
        buf.write("\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2G")
        buf.write("Ggg\4\2--//\6\2\n\f\16\17))^^\4\2$$^^\5\2\n\13\16\17\"")
        buf.write("\"\3\2$$\t\2))^^ddhhppttvv\5\2\f\f\17\17$$\2\u0180\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2c\3\2")
        buf.write("\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3")
        buf.write("\2\2\2\5~\3\2\2\2\7\u0083\3\2\2\2\t\u0089\3\2\2\2\13\u0090")
        buf.write("\3\2\2\2\r\u0095\3\2\2\2\17\u009c\3\2\2\2\21\u00a3\3\2")
        buf.write("\2\2\23\u00a7\3\2\2\2\25\u00af\3\2\2\2\27\u00b4\3\2\2")
        buf.write("\2\31\u00b8\3\2\2\2\33\u00be\3\2\2\2\35\u00c1\3\2\2\2")
        buf.write("\37\u00c7\3\2\2\2!\u00d0\3\2\2\2#\u00d3\3\2\2\2%\u00d8")
        buf.write("\3\2\2\2\'\u00dd\3\2\2\2)\u00e3\3\2\2\2+\u00e7\3\2\2\2")
        buf.write("-\u00eb\3\2\2\2/\u00ef\3\2\2\2\61\u00f2\3\2\2\2\63\u00f4")
        buf.write("\3\2\2\2\65\u00f6\3\2\2\2\67\u00f8\3\2\2\29\u00fa\3\2")
        buf.write("\2\2;\u00fc\3\2\2\2=\u00fe\3\2\2\2?\u0101\3\2\2\2A\u0104")
        buf.write("\3\2\2\2C\u0106\3\2\2\2E\u0109\3\2\2\2G\u010b\3\2\2\2")
        buf.write("I\u010e\3\2\2\2K\u0112\3\2\2\2M\u0115\3\2\2\2O\u0117\3")
        buf.write("\2\2\2Q\u0119\3\2\2\2S\u011b\3\2\2\2U\u011d\3\2\2\2W\u011f")
        buf.write("\3\2\2\2Y\u0121\3\2\2\2[\u0128\3\2\2\2]\u0130\3\2\2\2")
        buf.write("_\u0134\3\2\2\2a\u0138\3\2\2\2c\u013e\3\2\2\2e\u014a\3")
        buf.write("\2\2\2g\u014c\3\2\2\2i\u014f\3\2\2\2k\u0152\3\2\2\2m\u0158")
        buf.write("\3\2\2\2o\u016a\3\2\2\2q\u0175\3\2\2\2st\7%\2\2tu\7%\2")
        buf.write("\2uy\3\2\2\2vx\n\2\2\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2y")
        buf.write("z\3\2\2\2z|\3\2\2\2{y\3\2\2\2|}\b\2\2\2}\4\3\2\2\2~\177")
        buf.write("\7v\2\2\177\u0080\7t\2\2\u0080\u0081\7w\2\2\u0081\u0082")
        buf.write("\7g\2\2\u0082\6\3\2\2\2\u0083\u0084\7h\2\2\u0084\u0085")
        buf.write("\7c\2\2\u0085\u0086\7n\2\2\u0086\u0087\7u\2\2\u0087\u0088")
        buf.write("\7g\2\2\u0088\b\3\2\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7w\2\2\u008b\u008c\7o\2\2\u008c\u008d\7d\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7t\2\2\u008f\n\3\2\2\2\u0090\u0091")
        buf.write("\7d\2\2\u0091\u0092\7q\2\2\u0092\u0093\7q\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\f\3\2\2\2\u0095\u0096\7u\2\2\u0096\u0097")
        buf.write("\7v\2\2\u0097\u0098\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7i\2\2\u009b\16\3\2\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7w\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7p\2\2\u00a2\20")
        buf.write("\3\2\2\2\u00a3\u00a4\7x\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\22\3\2\2\2\u00a7\u00a8\7f\2\2\u00a8\u00a9")
        buf.write("\7{\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac")
        buf.write("\7o\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7e\2\2\u00ae\24")
        buf.write("\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7e\2\2\u00b3\26\3\2\2\2\u00b4\u00b5")
        buf.write("\7h\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7t\2\2\u00b7\30")
        buf.write("\3\2\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7n\2\2\u00bd\32")
        buf.write("\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7{\2\2\u00c0\34")
        buf.write("\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7m\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf \3")
        buf.write("\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7h\2\2\u00d2\"\3")
        buf.write("\2\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7u\2\2\u00d6\u00d7\7g\2\2\u00d7$\3\2\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7k\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc&\3\2\2\2\u00dd\u00de\7d\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7i\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2(\3\2\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\u00e6\7f\2\2\u00e6*\3\2\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7v\2\2\u00ea,\3")
        buf.write("\2\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee.\3\2\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\60\3\2\2\2\u00f2\u00f3\7-\2\2\u00f3\62\3")
        buf.write("\2\2\2\u00f4\u00f5\7/\2\2\u00f5\64\3\2\2\2\u00f6\u00f7")
        buf.write("\7,\2\2\u00f7\66\3\2\2\2\u00f8\u00f9\7\61\2\2\u00f98\3")
        buf.write("\2\2\2\u00fa\u00fb\7\'\2\2\u00fb:\3\2\2\2\u00fc\u00fd")
        buf.write("\7?\2\2\u00fd<\3\2\2\2\u00fe\u00ff\7>\2\2\u00ff\u0100")
        buf.write("\7/\2\2\u0100>\3\2\2\2\u0101\u0102\7#\2\2\u0102\u0103")
        buf.write("\7?\2\2\u0103@\3\2\2\2\u0104\u0105\7>\2\2\u0105B\3\2\2")
        buf.write("\2\u0106\u0107\7>\2\2\u0107\u0108\7?\2\2\u0108D\3\2\2")
        buf.write("\2\u0109\u010a\7@\2\2\u010aF\3\2\2\2\u010b\u010c\7@\2")
        buf.write("\2\u010c\u010d\7?\2\2\u010dH\3\2\2\2\u010e\u010f\7\60")
        buf.write("\2\2\u010f\u0110\7\60\2\2\u0110\u0111\7\60\2\2\u0111J")
        buf.write("\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114\7?\2\2\u0114L")
        buf.write("\3\2\2\2\u0115\u0116\7*\2\2\u0116N\3\2\2\2\u0117\u0118")
        buf.write("\7+\2\2\u0118P\3\2\2\2\u0119\u011a\7]\2\2\u011aR\3\2\2")
        buf.write("\2\u011b\u011c\7_\2\2\u011cT\3\2\2\2\u011d\u011e\7.\2")
        buf.write("\2\u011eV\3\2\2\2\u011f\u0120\7\f\2\2\u0120X\3\2\2\2\u0121")
        buf.write("\u0125\t\3\2\2\u0122\u0124\t\4\2\2\u0123\u0122\3\2\2\2")
        buf.write("\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126Z\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a")
        buf.write("\5]/\2\u0129\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u012e\5a\61\2\u012d")
        buf.write("\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\\\3\2\2\2\u012f")
        buf.write("\u0131\t\5\2\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133^\3\2\2")
        buf.write("\2\u0134\u0136\7\60\2\2\u0135\u0137\5]/\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137`\3\2\2\2\u0138\u013a")
        buf.write("\t\6\2\2\u0139\u013b\t\7\2\2\u013a\u0139\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\5]/\2\u013d")
        buf.write("b\3\2\2\2\u013e\u0144\7$\2\2\u013f\u0143\5e\63\2\u0140")
        buf.write("\u0143\5g\64\2\u0141\u0143\5i\65\2\u0142\u013f\3\2\2\2")
        buf.write("\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143\u0146\3")
        buf.write("\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7$\2\2\u0148")
        buf.write("\u0149\b\62\3\2\u0149d\3\2\2\2\u014a\u014b\t\b\2\2\u014b")
        buf.write("f\3\2\2\2\u014c\u014d\7)\2\2\u014d\u014e\7$\2\2\u014e")
        buf.write("h\3\2\2\2\u014f\u0150\n\t\2\2\u0150j\3\2\2\2\u0151\u0153")
        buf.write("\t\n\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\b\66\2\2\u0157l\3\2\2\2\u0158\u015c\7$\2")
        buf.write("\2\u0159\u015b\n\13\2\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\7^\2\2")
        buf.write("\u0160\u0161\n\f\2\2\u0161\u0165\3\2\2\2\u0162\u0164\13")
        buf.write("\2\2\2\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0168\u0169\b\67\4\2\u0169n\3\2\2\2\u016a")
        buf.write("\u0170\7$\2\2\u016b\u016f\n\r\2\2\u016c\u016d\7)\2\2\u016d")
        buf.write("\u016f\7$\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3")
        buf.write("\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174")
        buf.write("\b8\5\2\u0174p\3\2\2\2\u0175\u0176\13\2\2\2\u0176\u0177")
        buf.write("\b9\6\2\u0177r\3\2\2\2\21\2y\u0125\u012a\u012d\u0132\u0136")
        buf.write("\u013a\u0142\u0144\u0154\u015c\u0165\u016e\u0170\7\b\2")
        buf.write("\2\3\62\2\3\67\3\38\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    NOT = 21
    AND = 22
    OR = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQ_NUM = 29
    ASSIGN = 30
    NOT_EQ = 31
    LESS = 32
    LESS_EQ = 33
    GREATER = 34
    GREATER_EQ = 35
    CONCAT = 36
    EQ_STR = 37
    L_RB = 38
    R_RB = 39
    L_SB = 40
    R_SB = 41
    COMMA = 42
    NEWLINE = 43
    IDENTIFIER = 44
    NUM_LIT = 45
    STR_LIT = 46
    WS = 47
    ILLEGAL_ESCAPE = 48
    UNCLOSE_STRING = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ_NUM", "ASSIGN", "NOT_EQ", "LESS", 
            "LESS_EQ", "GREATER", "GREATER_EQ", "CONCAT", "EQ_STR", "L_RB", 
            "R_RB", "L_SB", "R_SB", "COMMA", "NEWLINE", "IDENTIFIER", "NUM_LIT", 
            "STR_LIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQ_NUM", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", "GREATER", 
                  "GREATER_EQ", "CONCAT", "EQ_STR", "L_RB", "R_RB", "L_SB", 
                  "R_SB", "COMMA", "NEWLINE", "IDENTIFIER", "NUM_LIT", "INT", 
                  "DEC", "EXP", "STR_LIT", "ESC_SEQ", "DOUBLE_QUOTE", "OTHER_CHARS", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STR_LIT_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                output_str = ""
                escape = False

                for char in self.text[1:]:
                    if escape:
                        output_str += char
                        if char not in ['b', 't', 'n', 'r', 'f', '\\', '\'']:
                            break
                        
                        escape = False
                    else:
                        if char == '\\':
                            escape = True
                        output_str += char

                raise IllegalEscape(output_str)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


