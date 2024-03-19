# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u0086\n\3\3\4\3\4\5\4\u008a\n\4\3\4\6\4")
        buf.write("\u008d\n\4\r\4\16\4\u008e\3\5\3\5\5\5\u0093\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6\u009b\n\6\3\6\5\6\u009e\n\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\b\u00a6\n\b\3\t\3\t\5\t\u00aa\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00b3\n\13\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00b9\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00c4\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00cc\n\17\f\17\16\17\u00cf\13\17\3\17\5\17")
        buf.write("\u00d2\n\17\3\20\3\20\5\20\u00d6\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00dd\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00e5\n\22\3\23\3\23\5\23\u00e9\n\23\3\24\3\24\6")
        buf.write("\24\u00ed\n\24\r\24\16\24\u00ee\3\24\3\24\3\24\5\24\u00f4")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00ff\n\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\6\30\u0108")
        buf.write("\n\30\r\30\16\30\u0109\3\30\7\30\u010d\n\30\f\30\16\30")
        buf.write("\u0110\13\30\3\30\6\30\u0113\n\30\r\30\16\30\u0114\3\30")
        buf.write("\5\30\u0118\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0121\n\31\f\31\16\31\u0124\13\31\3\31\3\31\3\32\3")
        buf.write("\32\3\33\3\33\3\34\3\34\5\34\u012e\n\34\3\35\3\35\3\36")
        buf.write("\3\36\6\36\u0134\n\36\r\36\16\36\u0135\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \5 \u0140\n \3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u014c\n\"\f\"\16\"\u014f\13\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\7#\u0158\n#\f#\16#\u015b\13#\3#\3#\3")
        buf.write("$\3$\7$\u0161\n$\f$\16$\u0164\13$\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\5&\u016f\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0176\n\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\7(\u017f\n(\f(\16(\u0182\13(\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\7)\u018b\n)\f)\16)\u018e\13)\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\7*\u0197\n*\f*\16*\u019a\13*\3+\3+\3+")
        buf.write("\3+\5+\u01a0\n+\3,\3,\3,\3,\5,\u01a6\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\5-\u01ae\n-\3.\3.\3.\3.\5.\u01b4\n.\3/\3/\5/\u01b8")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\5\62\u01c5\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01cc")
        buf.write("\n\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3;\3;\3;\5;\u01e1\n;\3<\3<\3<\2\5NPR")
        buf.write("=\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\b\3\2\6\b\3")
        buf.write("\2\4\5\5\2\37\37!%\'\'\3\2\30\31\3\2\32\33\3\2\34\36\2")
        buf.write("\u01e1\2{\3\2\2\2\4\u0085\3\2\2\2\6\u0089\3\2\2\2\b\u0092")
        buf.write("\3\2\2\2\n\u0094\3\2\2\2\f\u009f\3\2\2\2\16\u00a5\3\2")
        buf.write("\2\2\20\u00a9\3\2\2\2\22\u00ab\3\2\2\2\24\u00af\3\2\2")
        buf.write("\2\26\u00b8\3\2\2\2\30\u00ba\3\2\2\2\32\u00c3\3\2\2\2")
        buf.write("\34\u00c5\3\2\2\2\36\u00d5\3\2\2\2 \u00dc\3\2\2\2\"\u00de")
        buf.write("\3\2\2\2$\u00e8\3\2\2\2&\u00f3\3\2\2\2(\u00fe\3\2\2\2")
        buf.write("*\u0100\3\2\2\2,\u0102\3\2\2\2.\u0105\3\2\2\2\60\u0119")
        buf.write("\3\2\2\2\62\u0127\3\2\2\2\64\u0129\3\2\2\2\66\u012b\3")
        buf.write("\2\2\28\u012f\3\2\2\2:\u0131\3\2\2\2<\u013a\3\2\2\2>\u013f")
        buf.write("\3\2\2\2@\u0141\3\2\2\2B\u0146\3\2\2\2D\u0152\3\2\2\2")
        buf.write("F\u015e\3\2\2\2H\u0167\3\2\2\2J\u016e\3\2\2\2L\u0175\3")
        buf.write("\2\2\2N\u0177\3\2\2\2P\u0183\3\2\2\2R\u018f\3\2\2\2T\u019f")
        buf.write("\3\2\2\2V\u01a5\3\2\2\2X\u01ad\3\2\2\2Z\u01b3\3\2\2\2")
        buf.write("\\\u01b7\3\2\2\2^\u01b9\3\2\2\2`\u01be\3\2\2\2b\u01c4")
        buf.write("\3\2\2\2d\u01cb\3\2\2\2f\u01cd\3\2\2\2h\u01cf\3\2\2\2")
        buf.write("j\u01d1\3\2\2\2l\u01d3\3\2\2\2n\u01d5\3\2\2\2p\u01d7\3")
        buf.write("\2\2\2r\u01d9\3\2\2\2t\u01e0\3\2\2\2v\u01e2\3\2\2\2xz")
        buf.write("\7-\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2")
        buf.write("\2\2}{\3\2\2\2~\177\5\4\3\2\177\u0080\7\2\2\3\u0080\3")
        buf.write("\3\2\2\2\u0081\u0082\5\6\4\2\u0082\u0083\5\4\3\2\u0083")
        buf.write("\u0086\3\2\2\2\u0084\u0086\5\6\4\2\u0085\u0081\3\2\2\2")
        buf.write("\u0085\u0084\3\2\2\2\u0086\5\3\2\2\2\u0087\u008a\5\b\5")
        buf.write("\2\u0088\u008a\5\34\17\2\u0089\u0087\3\2\2\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u008d\7-\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\7\3\2\2\2\u0090\u0093\5\n\6")
        buf.write("\2\u0091\u0093\5\20\t\2\u0092\u0090\3\2\2\2\u0092\u0091")
        buf.write("\3\2\2\2\u0093\t\3\2\2\2\u0094\u0095\5\f\7\2\u0095\u009a")
        buf.write("\7.\2\2\u0096\u0097\7*\2\2\u0097\u0098\5\16\b\2\u0098")
        buf.write("\u0099\7+\2\2\u0099\u009b\3\2\2\2\u009a\u0096\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009e\5")
        buf.write("<\37\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\13")
        buf.write("\3\2\2\2\u009f\u00a0\t\2\2\2\u00a0\r\3\2\2\2\u00a1\u00a2")
        buf.write("\7/\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a6\5\16\b\2\u00a4")
        buf.write("\u00a6\7/\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a6\17\3\2\2\2\u00a7\u00aa\5\22\n\2\u00a8\u00aa\5\24")
        buf.write("\13\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\21")
        buf.write("\3\2\2\2\u00ab\u00ac\7\n\2\2\u00ac\u00ad\7.\2\2\u00ad")
        buf.write("\u00ae\5<\37\2\u00ae\23\3\2\2\2\u00af\u00b0\7\13\2\2\u00b0")
        buf.write("\u00b2\7.\2\2\u00b1\u00b3\5<\37\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\25\3\2\2\2\u00b4\u00b9\7/\2")
        buf.write("\2\u00b5\u00b9\t\3\2\2\u00b6\u00b9\7\60\2\2\u00b7\u00b9")
        buf.write("\5\30\r\2\u00b8\u00b4\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\27\3\2\2\2\u00ba")
        buf.write("\u00bb\7*\2\2\u00bb\u00bc\5\32\16\2\u00bc\u00bd\7+\2\2")
        buf.write("\u00bd\31\3\2\2\2\u00be\u00bf\5H%\2\u00bf\u00c0\7,\2\2")
        buf.write("\u00c0\u00c1\5\32\16\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4")
        buf.write("\5H%\2\u00c3\u00be\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\33")
        buf.write("\3\2\2\2\u00c5\u00c6\7\f\2\2\u00c6\u00c7\7.\2\2\u00c7")
        buf.write("\u00c8\7(\2\2\u00c8\u00c9\5\36\20\2\u00c9\u00d1\7)\2\2")
        buf.write("\u00ca\u00cc\7-\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d2\5$\23\2\u00d1")
        buf.write("\u00cd\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\35\3\2\2\2\u00d3")
        buf.write("\u00d6\5 \21\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d4\3\2\2\2\u00d6\37\3\2\2\2\u00d7\u00d8\5\"")
        buf.write("\22\2\u00d8\u00d9\7,\2\2\u00d9\u00da\5 \21\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00dd\5\"\22\2\u00dc\u00d7\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd!\3\2\2\2\u00de\u00df\5\f\7\2\u00df")
        buf.write("\u00e4\7.\2\2\u00e0\u00e1\7*\2\2\u00e1\u00e2\5\16\b\2")
        buf.write("\u00e2\u00e3\7+\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e0\3")
        buf.write("\2\2\2\u00e4\u00e5\3\2\2\2\u00e5#\3\2\2\2\u00e6\u00e9")
        buf.write("\5\66\34\2\u00e7\u00e9\5:\36\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9%\3\2\2\2\u00ea\u00ec\5(\25\2\u00eb")
        buf.write("\u00ed\7-\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0\u00f1\5&\24\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4")
        buf.write("\3\2\2\2\u00f3\u00ea\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\'\3\2\2\2\u00f5\u00ff\5*\26\2\u00f6\u00ff\5,\27\2\u00f7")
        buf.write("\u00ff\5.\30\2\u00f8\u00ff\5\60\31\2\u00f9\u00ff\5\62")
        buf.write("\32\2\u00fa\u00ff\5\64\33\2\u00fb\u00ff\5\66\34\2\u00fc")
        buf.write("\u00ff\58\35\2\u00fd\u00ff\5:\36\2\u00fe\u00f5\3\2\2\2")
        buf.write("\u00fe\u00f6\3\2\2\2\u00fe\u00f7\3\2\2\2\u00fe\u00f8\3")
        buf.write("\2\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fb")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write(")\3\2\2\2\u0100\u0101\5\b\5\2\u0101+\3\2\2\2\u0102\u0103")
        buf.write("\5> \2\u0103\u0104\5<\37\2\u0104-\3\2\2\2\u0105\u010e")
        buf.write("\5B\"\2\u0106\u0108\7-\2\2\u0107\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010d\5D#\2\u010c\u0107\3\2\2\2\u010d")
        buf.write("\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0117\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0113\7")
        buf.write("-\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0118\5F$\2\u0117\u0112\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("/\3\2\2\2\u0119\u011a\7\r\2\2\u011a\u011b\7.\2\2\u011b")
        buf.write("\u011c\7\16\2\2\u011c\u011d\5H%\2\u011d\u011e\7\17\2\2")
        buf.write("\u011e\u0122\5H%\2\u011f\u0121\7-\2\2\u0120\u011f\3\2")
        buf.write("\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2\u0125")
        buf.write("\u0126\5(\25\2\u0126\61\3\2\2\2\u0127\u0128\7\20\2\2\u0128")
        buf.write("\63\3\2\2\2\u0129\u012a\7\21\2\2\u012a\65\3\2\2\2\u012b")
        buf.write("\u012d\7\t\2\2\u012c\u012e\5H%\2\u012d\u012c\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\67\3\2\2\2\u012f\u0130\5^\60\2\u0130")
        buf.write("9\3\2\2\2\u0131\u0133\7\25\2\2\u0132\u0134\7-\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\5")
        buf.write("&\24\2\u0138\u0139\7\26\2\2\u0139;\3\2\2\2\u013a\u013b")
        buf.write("\7 \2\2\u013b\u013c\5H%\2\u013c=\3\2\2\2\u013d\u0140\7")
        buf.write(".\2\2\u013e\u0140\5@!\2\u013f\u013d\3\2\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140?\3\2\2\2\u0141\u0142\7.\2\2\u0142\u0143")
        buf.write("\7*\2\2\u0143\u0144\5t;\2\u0144\u0145\7+\2\2\u0145A\3")
        buf.write("\2\2\2\u0146\u0147\7\22\2\2\u0147\u0148\7(\2\2\u0148\u0149")
        buf.write("\5H%\2\u0149\u014d\7)\2\2\u014a\u014c\7-\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u0150\u0151\5(\25\2\u0151C\3\2\2\2\u0152\u0153\7\24\2")
        buf.write("\2\u0153\u0154\7(\2\2\u0154\u0155\5H%\2\u0155\u0159\7")
        buf.write(")\2\2\u0156\u0158\7-\2\2\u0157\u0156\3\2\2\2\u0158\u015b")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\5(\25\2")
        buf.write("\u015dE\3\2\2\2\u015e\u0162\7\23\2\2\u015f\u0161\7-\2")
        buf.write("\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0166\5(\25\2\u0166G\3\2\2\2\u0167")
        buf.write("\u0168\5J&\2\u0168I\3\2\2\2\u0169\u016a\5L\'\2\u016a\u016b")
        buf.write("\5f\64\2\u016b\u016c\5L\'\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016f\5L\'\2\u016e\u0169\3\2\2\2\u016e\u016d\3\2\2\2")
        buf.write("\u016fK\3\2\2\2\u0170\u0171\5N(\2\u0171\u0172\5h\65\2")
        buf.write("\u0172\u0173\5N(\2\u0173\u0176\3\2\2\2\u0174\u0176\5N")
        buf.write("(\2\u0175\u0170\3\2\2\2\u0175\u0174\3\2\2\2\u0176M\3\2")
        buf.write("\2\2\u0177\u0178\b(\1\2\u0178\u0179\5P)\2\u0179\u0180")
        buf.write("\3\2\2\2\u017a\u017b\f\4\2\2\u017b\u017c\5j\66\2\u017c")
        buf.write("\u017d\5P)\2\u017d\u017f\3\2\2\2\u017e\u017a\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181O\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\b)\1\2")
        buf.write("\u0184\u0185\5R*\2\u0185\u018c\3\2\2\2\u0186\u0187\f\4")
        buf.write("\2\2\u0187\u0188\5l\67\2\u0188\u0189\5R*\2\u0189\u018b")
        buf.write("\3\2\2\2\u018a\u0186\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dQ\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0190\b*\1\2\u0190\u0191\5T+\2\u0191")
        buf.write("\u0198\3\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\5n8\2\u0194")
        buf.write("\u0195\5T+\2\u0195\u0197\3\2\2\2\u0196\u0192\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199S\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\5p9\2")
        buf.write("\u019c\u019d\5T+\2\u019d\u01a0\3\2\2\2\u019e\u01a0\5V")
        buf.write(",\2\u019f\u019b\3\2\2\2\u019f\u019e\3\2\2\2\u01a0U\3\2")
        buf.write("\2\2\u01a1\u01a2\5r:\2\u01a2\u01a3\5V,\2\u01a3\u01a6\3")
        buf.write("\2\2\2\u01a4\u01a6\5X-\2\u01a5\u01a1\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6W\3\2\2\2\u01a7\u01a8\5\\/\2\u01a8\u01a9")
        buf.write("\7*\2\2\u01a9\u01aa\5t;\2\u01aa\u01ab\7+\2\2\u01ab\u01ae")
        buf.write("\3\2\2\2\u01ac\u01ae\5Z.\2\u01ad\u01a7\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01aeY\3\2\2\2\u01af\u01b4\5\26\f\2\u01b0\u01b4")
        buf.write("\7.\2\2\u01b1\u01b4\5^\60\2\u01b2\u01b4\5`\61\2\u01b3")
        buf.write("\u01af\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b2\3\2\2\2\u01b4[\3\2\2\2\u01b5\u01b8\7.\2\2")
        buf.write("\u01b6\u01b8\5^\60\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3")
        buf.write("\2\2\2\u01b8]\3\2\2\2\u01b9\u01ba\7.\2\2\u01ba\u01bb\7")
        buf.write("(\2\2\u01bb\u01bc\5b\62\2\u01bc\u01bd\7)\2\2\u01bd_\3")
        buf.write("\2\2\2\u01be\u01bf\7(\2\2\u01bf\u01c0\5H%\2\u01c0\u01c1")
        buf.write("\7)\2\2\u01c1a\3\2\2\2\u01c2\u01c5\5d\63\2\u01c3\u01c5")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("c\3\2\2\2\u01c6\u01c7\5H%\2\u01c7\u01c8\7,\2\2\u01c8\u01c9")
        buf.write("\5d\63\2\u01c9\u01cc\3\2\2\2\u01ca\u01cc\5H%\2\u01cb\u01c6")
        buf.write("\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cce\3\2\2\2\u01cd\u01ce")
        buf.write("\7&\2\2\u01ceg\3\2\2\2\u01cf\u01d0\t\4\2\2\u01d0i\3\2")
        buf.write("\2\2\u01d1\u01d2\t\5\2\2\u01d2k\3\2\2\2\u01d3\u01d4\t")
        buf.write("\6\2\2\u01d4m\3\2\2\2\u01d5\u01d6\t\7\2\2\u01d6o\3\2\2")
        buf.write("\2\u01d7\u01d8\7\27\2\2\u01d8q\3\2\2\2\u01d9\u01da\7\33")
        buf.write("\2\2\u01das\3\2\2\2\u01db\u01e1\5H%\2\u01dc\u01dd\5H%")
        buf.write("\2\u01dd\u01de\7,\2\2\u01de\u01df\5t;\2\u01df\u01e1\3")
        buf.write("\2\2\2\u01e0\u01db\3\2\2\2\u01e0\u01dc\3\2\2\2\u01e1u")
        buf.write("\3\2\2\2\u01e2\u01e3\7\3\2\2\u01e3w\3\2\2\2/{\u0085\u0089")
        buf.write("\u008e\u0092\u009a\u009d\u00a5\u00a9\u00b2\u00b8\u00c3")
        buf.write("\u00cd\u00d1\u00d5\u00dc\u00e4\u00e8\u00ee\u00f3\u00fe")
        buf.write("\u0109\u010e\u0114\u0117\u0122\u012d\u0135\u013f\u014d")
        buf.write("\u0159\u0162\u016e\u0175\u0180\u018c\u0198\u019f\u01a5")
        buf.write("\u01ad\u01b3\u01b7\u01c4\u01cb\u01e0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "TRUE", "FALSE", "NUMBER", 
                      "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ_NUM", "ASSIGN", "NOT_EQ", 
                      "LESS", "LESS_EQ", "GREATER", "GREATER_EQ", "CONCAT", 
                      "EQ_STR", "L_RB", "R_RB", "L_SB", "R_SB", "COMMA", 
                      "NEWLINE", "IDENTIFIER", "NUM_LIT", "STR_LIT", "WS", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_variable_decl = 3
    RULE_explicit_decl = 4
    RULE_type_decl = 5
    RULE_size_list = 6
    RULE_implicit_decl = 7
    RULE_var_decl = 8
    RULE_dynamic_decl = 9
    RULE_literals = 10
    RULE_arr_lit = 11
    RULE_arr_list = 12
    RULE_function_decl = 13
    RULE_para_list = 14
    RULE_prime_para_list = 15
    RULE_para_decl = 16
    RULE_func_body = 17
    RULE_stmt_list = 18
    RULE_stmt = 19
    RULE_var_decl_stmt = 20
    RULE_assign_stmt = 21
    RULE_if_stmt = 22
    RULE_for_stmt = 23
    RULE_break_stmt = 24
    RULE_continue_stmt = 25
    RULE_return_stmt = 26
    RULE_call_stmt = 27
    RULE_block_stmt = 28
    RULE_assign_expr = 29
    RULE_lhs = 30
    RULE_recur_idx_expr = 31
    RULE_if_part = 32
    RULE_elif_part = 33
    RULE_else_part = 34
    RULE_expr = 35
    RULE_str_expr = 36
    RULE_cmp_expr = 37
    RULE_log2_expr = 38
    RULE_add_expr = 39
    RULE_mul_expr = 40
    RULE_log1_expr = 41
    RULE_sign_expr = 42
    RULE_idx_expr = 43
    RULE_val_expr = 44
    RULE_var_expr = 45
    RULE_call_expr = 46
    RULE_sub_expr = 47
    RULE_arg_list = 48
    RULE_prime_arg_list = 49
    RULE_concat_operator = 50
    RULE_cmp_operator = 51
    RULE_log2_operator = 52
    RULE_add_operator = 53
    RULE_mul_operator = 54
    RULE_log1_operator = 55
    RULE_sign_operator = 56
    RULE_idx_operator = 57
    RULE_comment = 58

    ruleNames =  [ "program", "decl_list", "decl", "variable_decl", "explicit_decl", 
                   "type_decl", "size_list", "implicit_decl", "var_decl", 
                   "dynamic_decl", "literals", "arr_lit", "arr_list", "function_decl", 
                   "para_list", "prime_para_list", "para_decl", "func_body", 
                   "stmt_list", "stmt", "var_decl_stmt", "assign_stmt", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "call_stmt", "block_stmt", "assign_expr", 
                   "lhs", "recur_idx_expr", "if_part", "elif_part", "else_part", 
                   "expr", "str_expr", "cmp_expr", "log2_expr", "add_expr", 
                   "mul_expr", "log1_expr", "sign_expr", "idx_expr", "val_expr", 
                   "var_expr", "call_expr", "sub_expr", "arg_list", "prime_arg_list", 
                   "concat_operator", "cmp_operator", "log2_operator", "add_operator", 
                   "mul_operator", "log1_operator", "sign_operator", "idx_operator", 
                   "comment" ]

    EOF = Token.EOF
    COMMENT=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONTINUE=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    NOT=21
    AND=22
    OR=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    EQ_NUM=29
    ASSIGN=30
    NOT_EQ=31
    LESS=32
    LESS_EQ=33
    GREATER=34
    GREATER_EQ=35
    CONCAT=36
    EQ_STR=37
    L_RB=38
    R_RB=39
    L_SB=40
    R_SB=41
    COMMA=42
    NEWLINE=43
    IDENTIFIER=44
    NUM_LIT=45
    STR_LIT=46
    WS=47
    ILLEGAL_ESCAPE=48
    UNCLOSE_STRING=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 118
                self.match(ZCodeParser.NEWLINE)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.decl_list()
            self.state = 125
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.decl()
                self.state = 128
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 133
                self.variable_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.state = 134
                self.function_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.match(ZCodeParser.NEWLINE)
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Explicit_declContext,0)


        def implicit_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = ZCodeParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.explicit_decl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.implicit_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_declContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def L_SB(self):
            return self.getToken(ZCodeParser.L_SB, 0)

        def size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Size_listContext,0)


        def R_SB(self):
            return self.getToken(ZCodeParser.R_SB, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explicit_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_decl" ):
                return visitor.visitExplicit_decl(self)
            else:
                return visitor.visitChildren(self)




    def explicit_decl(self):

        localctx = ZCodeParser.Explicit_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_explicit_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.type_decl()
            self.state = 147
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.L_SB:
                self.state = 148
                self.match(ZCodeParser.L_SB)
                self.state = 149
                self.size_list()
                self.state = 150
                self.match(ZCodeParser.R_SB)


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 154
                self.assign_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = ZCodeParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Size_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize_list" ):
                return visitor.visitSize_list(self)
            else:
                return visitor.visitChildren(self)




    def size_list(self):

        localctx = ZCodeParser.Size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_size_list)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(ZCodeParser.NUM_LIT)
                self.state = 160
                self.match(ZCodeParser.COMMA)
                self.state = 161
                self.size_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def dynamic_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_decl" ):
                return visitor.visitImplicit_decl(self)
            else:
                return visitor.visitChildren(self)




    def implicit_decl(self):

        localctx = ZCodeParser.Implicit_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicit_decl)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.var_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.dynamic_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.VAR)
            self.state = 170
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 171
            self.assign_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_decl" ):
                return visitor.visitDynamic_decl(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_decl(self):

        localctx = ZCodeParser.Dynamic_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dynamic_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.DYNAMIC)
            self.state = 174
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 175
                self.assign_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [ZCodeParser.L_SB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.arr_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_SB(self):
            return self.getToken(ZCodeParser.L_SB, 0)

        def arr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_listContext,0)


        def R_SB(self):
            return self.getToken(ZCodeParser.R_SB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = ZCodeParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ZCodeParser.L_SB)
            self.state = 185
            self.arr_list()
            self.state = 186
            self.match(ZCodeParser.R_SB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_list" ):
                return visitor.visitArr_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_list(self):

        localctx = ZCodeParser.Arr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arr_list)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expr()
                self.state = 189
                self.match(ZCodeParser.COMMA)
                self.state = 190
                self.arr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def L_RB(self):
            return self.getToken(ZCodeParser.L_RB, 0)

        def para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Para_listContext,0)


        def R_RB(self):
            return self.getToken(ZCodeParser.R_RB, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = ZCodeParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ZCodeParser.FUNC)
            self.state = 196
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 197
            self.match(ZCodeParser.L_RB)
            self.state = 198
            self.para_list()
            self.state = 199
            self.match(ZCodeParser.R_RB)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 200
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 206
                self.func_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prime_para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prime_para_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = ZCodeParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_para_list)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.prime_para_list()
                pass
            elif token in [ZCodeParser.R_RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prime_para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Para_declContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def prime_para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prime_para_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prime_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrime_para_list" ):
                return visitor.visitPrime_para_list(self)
            else:
                return visitor.visitChildren(self)




    def prime_para_list(self):

        localctx = ZCodeParser.Prime_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prime_para_list)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.para_decl()
                self.state = 214
                self.match(ZCodeParser.COMMA)
                self.state = 215
                self.prime_para_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.para_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_declContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def L_SB(self):
            return self.getToken(ZCodeParser.L_SB, 0)

        def size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Size_listContext,0)


        def R_SB(self):
            return self.getToken(ZCodeParser.R_SB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = ZCodeParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.type_decl()
            self.state = 221
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.L_SB:
                self.state = 222
                self.match(ZCodeParser.L_SB)
                self.state = 223
                self.size_list()
                self.state = 224
                self.match(ZCodeParser.R_SB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_body)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.stmt()
                self.state = 234 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 233
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 236 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 238
                self.stmt_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Var_decl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.var_decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 250
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 251
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stmt" ):
                return visitor.visitVar_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stmt(self):

        localctx = ZCodeParser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.variable_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def assign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.lhs()
            self.state = 257
            self.assign_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(ZCodeParser.If_partContext,0)


        def elif_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_partContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(ZCodeParser.Else_partContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.if_part()
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 261 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 260
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 263 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break

                    self.state = 265
                    self.elif_part() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 271
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 274 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEWLINE):
                        break

                self.state = 276
                self.else_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ZCodeParser.FOR)
            self.state = 280
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 281
            self.match(ZCodeParser.UNTIL)
            self.state = 282
            self.expr()
            self.state = 283
            self.match(ZCodeParser.BY)
            self.state = 284
            self.expr()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 285
                self.match(ZCodeParser.NEWLINE)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ZCodeParser.RETURN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.L_RB) | (1 << ZCodeParser.L_SB) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 298
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.call_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.BEGIN)
            self.state = 305 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 304
                self.match(ZCodeParser.NEWLINE)
                self.state = 307 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 309
            self.stmt_list()
            self.state = 310
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_expr" ):
                return visitor.visitAssign_expr(self)
            else:
                return visitor.visitChildren(self)




    def assign_expr(self):

        localctx = ZCodeParser.Assign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assign_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ZCodeParser.ASSIGN)
            self.state = 313
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def recur_idx_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Recur_idx_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.recur_idx_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Recur_idx_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def L_SB(self):
            return self.getToken(ZCodeParser.L_SB, 0)

        def idx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_operatorContext,0)


        def R_SB(self):
            return self.getToken(ZCodeParser.R_SB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_recur_idx_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecur_idx_expr" ):
                return visitor.visitRecur_idx_expr(self)
            else:
                return visitor.visitChildren(self)




    def recur_idx_expr(self):

        localctx = ZCodeParser.Recur_idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_recur_idx_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 320
            self.match(ZCodeParser.L_SB)
            self.state = 321
            self.idx_operator()
            self.state = 322
            self.match(ZCodeParser.R_SB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def L_RB(self):
            return self.getToken(ZCodeParser.L_RB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_RB(self):
            return self.getToken(ZCodeParser.R_RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = ZCodeParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.IF)
            self.state = 325
            self.match(ZCodeParser.L_RB)
            self.state = 326
            self.expr()
            self.state = 327
            self.match(ZCodeParser.R_RB)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 328
                self.match(ZCodeParser.NEWLINE)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def L_RB(self):
            return self.getToken(ZCodeParser.L_RB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_RB(self):
            return self.getToken(ZCodeParser.R_RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_part" ):
                return visitor.visitElif_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_part(self):

        localctx = ZCodeParser.Elif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elif_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZCodeParser.ELIF)
            self.state = 337
            self.match(ZCodeParser.L_RB)
            self.state = 338
            self.expr()
            self.state = 339
            self.match(ZCodeParser.R_RB)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 340
                self.match(ZCodeParser.NEWLINE)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = ZCodeParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ZCodeParser.ELSE)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 349
                self.match(ZCodeParser.NEWLINE)
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Str_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.str_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmp_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Cmp_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Cmp_exprContext,i)


        def concat_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Concat_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_str_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_expr" ):
                return visitor.visitStr_expr(self)
            else:
                return visitor.visitChildren(self)




    def str_expr(self):

        localctx = ZCodeParser.Str_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_str_expr)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.cmp_expr()
                self.state = 360
                self.concat_operator()
                self.state = 361
                self.cmp_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.cmp_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmp_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log2_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Log2_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Log2_exprContext,i)


        def cmp_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Cmp_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_cmp_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmp_expr" ):
                return visitor.visitCmp_expr(self)
            else:
                return visitor.visitChildren(self)




    def cmp_expr(self):

        localctx = ZCodeParser.Cmp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_cmp_expr)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.log2_expr(0)
                self.state = 367
                self.cmp_operator()
                self.state = 368
                self.log2_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.log2_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log2_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def log2_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Log2_exprContext,0)


        def log2_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Log2_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_log2_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog2_expr" ):
                return visitor.visitLog2_expr(self)
            else:
                return visitor.visitChildren(self)



    def log2_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Log2_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_log2_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Log2_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_log2_expr)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.log2_operator()
                    self.state = 378
                    self.add_expr(0) 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def add_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Add_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 388
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 389
                    self.add_operator()
                    self.state = 390
                    self.mul_expr(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log1_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Log1_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def mul_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_mul_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.log1_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    self.mul_operator()
                    self.state = 402
                    self.log1_expr() 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Log1_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log1_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Log1_operatorContext,0)


        def log1_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Log1_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_log1_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog1_expr" ):
                return visitor.visitLog1_expr(self)
            else:
                return visitor.visitChildren(self)




    def log1_expr(self):

        localctx = ZCodeParser.Log1_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_log1_expr)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.log1_operator()
                self.state = 410
                self.log1_expr()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.L_RB, ZCodeParser.L_SB, ZCodeParser.IDENTIFIER, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_operatorContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def idx_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_sign_expr)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.sign_operator()
                self.state = 416
                self.sign_expr()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.L_RB, ZCodeParser.L_SB, ZCodeParser.IDENTIFIER, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.idx_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Var_exprContext,0)


        def L_SB(self):
            return self.getToken(ZCodeParser.L_SB, 0)

        def idx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_operatorContext,0)


        def R_SB(self):
            return self.getToken(ZCodeParser.R_SB, 0)

        def val_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Val_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idx_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_expr" ):
                return visitor.visitIdx_expr(self)
            else:
                return visitor.visitChildren(self)




    def idx_expr(self):

        localctx = ZCodeParser.Idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_idx_expr)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.var_expr()
                self.state = 422
                self.match(ZCodeParser.L_SB)
                self.state = 423
                self.idx_operator()
                self.state = 424
                self.match(ZCodeParser.R_SB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.val_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_val_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_expr" ):
                return visitor.visitVal_expr(self)
            else:
                return visitor.visitChildren(self)




    def val_expr(self):

        localctx = ZCodeParser.Val_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_val_expr)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_expr" ):
                return visitor.visitVar_expr(self)
            else:
                return visitor.visitChildren(self)




    def var_expr(self):

        localctx = ZCodeParser.Var_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_var_expr)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def L_RB(self):
            return self.getToken(ZCodeParser.L_RB, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def R_RB(self):
            return self.getToken(ZCodeParser.R_RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = ZCodeParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 440
            self.match(ZCodeParser.L_RB)
            self.state = 441
            self.arg_list()
            self.state = 442
            self.match(ZCodeParser.R_RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_RB(self):
            return self.getToken(ZCodeParser.L_RB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_RB(self):
            return self.getToken(ZCodeParser.R_RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = ZCodeParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(ZCodeParser.L_RB)
            self.state = 445
            self.expr()
            self.state = 446
            self.match(ZCodeParser.R_RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prime_arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prime_arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = ZCodeParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arg_list)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.L_RB, ZCodeParser.L_SB, ZCodeParser.IDENTIFIER, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.prime_arg_list()
                pass
            elif token in [ZCodeParser.R_RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prime_arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def prime_arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prime_arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prime_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrime_arg_list" ):
                return visitor.visitPrime_arg_list(self)
            else:
                return visitor.visitChildren(self)




    def prime_arg_list(self):

        localctx = ZCodeParser.Prime_arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_prime_arg_list)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.expr()
                self.state = 453
                self.match(ZCodeParser.COMMA)
                self.state = 454
                self.prime_arg_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_concat_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_operator" ):
                return visitor.visitConcat_operator(self)
            else:
                return visitor.visitChildren(self)




    def concat_operator(self):

        localctx = ZCodeParser.Concat_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_concat_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(ZCodeParser.CONCAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmp_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_NUM(self):
            return self.getToken(ZCodeParser.EQ_NUM, 0)

        def NOT_EQ(self):
            return self.getToken(ZCodeParser.NOT_EQ, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LESS_EQ(self):
            return self.getToken(ZCodeParser.LESS_EQ, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def GREATER_EQ(self):
            return self.getToken(ZCodeParser.GREATER_EQ, 0)

        def EQ_STR(self):
            return self.getToken(ZCodeParser.EQ_STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_cmp_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmp_operator" ):
                return visitor.visitCmp_operator(self)
            else:
                return visitor.visitChildren(self)




    def cmp_operator(self):

        localctx = ZCodeParser.Cmp_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_cmp_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ_NUM) | (1 << ZCodeParser.NOT_EQ) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESS_EQ) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GREATER_EQ) | (1 << ZCodeParser.EQ_STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log2_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_log2_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog2_operator" ):
                return visitor.visitLog2_operator(self)
            else:
                return visitor.visitChildren(self)




    def log2_operator(self):

        localctx = ZCodeParser.Log2_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_log2_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_operator" ):
                return visitor.visitAdd_operator(self)
            else:
                return visitor.visitChildren(self)




    def add_operator(self):

        localctx = ZCodeParser.Add_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_add_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_operator" ):
                return visitor.visitMul_operator(self)
            else:
                return visitor.visitChildren(self)




    def mul_operator(self):

        localctx = ZCodeParser.Mul_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_mul_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log1_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_log1_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog1_operator" ):
                return visitor.visitLog1_operator(self)
            else:
                return visitor.visitChildren(self)




    def log1_operator(self):

        localctx = ZCodeParser.Log1_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_log1_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(ZCodeParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operator" ):
                return visitor.visitSign_operator(self)
            else:
                return visitor.visitChildren(self)




    def sign_operator(self):

        localctx = ZCodeParser.Sign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_sign_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ZCodeParser.SUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def idx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idx_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_operator" ):
                return visitor.visitIdx_operator(self)
            else:
                return visitor.visitChildren(self)




    def idx_operator(self):

        localctx = ZCodeParser.Idx_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_idx_operator)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.expr()
                self.state = 475
                self.match(ZCodeParser.COMMA)
                self.state = 476
                self.idx_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = ZCodeParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ZCodeParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.log2_expr_sempred
        self._predicates[39] = self.add_expr_sempred
        self._predicates[40] = self.mul_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def log2_expr_sempred(self, localctx:Log2_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




