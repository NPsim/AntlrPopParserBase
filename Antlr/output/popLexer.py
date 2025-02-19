# Generated from ./pop.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,27,8,3,10,
        3,12,3,30,9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,38,8,4,10,4,12,4,41,9,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,4,6,53,8,6,11,6,12,6,54,
        1,7,1,7,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,5,2,
        0,10,10,13,13,4,0,10,10,13,13,34,34,92,92,2,0,34,34,92,92,9,0,36,
        36,40,41,45,57,60,60,62,62,64,91,93,93,95,95,97,122,3,0,9,10,13,
        13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,
        1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,33,1,0,0,0,11,44,1,0,0,0,13,
        52,1,0,0,0,15,56,1,0,0,0,17,18,5,123,0,0,18,2,1,0,0,0,19,20,5,125,
        0,0,20,4,1,0,0,0,21,22,5,35,0,0,22,6,1,0,0,0,23,24,5,47,0,0,24,28,
        5,47,0,0,25,27,8,0,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,
        28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,32,6,3,0,0,32,8,1,0,
        0,0,33,39,5,34,0,0,34,38,8,1,0,0,35,36,5,92,0,0,36,38,7,2,0,0,37,
        34,1,0,0,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,34,0,0,43,10,1,0,0,0,44,45,
        5,91,0,0,45,46,5,36,0,0,46,47,3,13,6,0,47,48,5,93,0,0,48,49,1,0,
        0,0,49,50,6,5,0,0,50,12,1,0,0,0,51,53,7,3,0,0,52,51,1,0,0,0,53,54,
        1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,14,1,0,0,0,56,57,7,4,0,0,
        57,58,1,0,0,0,58,59,6,7,0,0,59,16,1,0,0,0,5,0,28,37,39,54,1,6,0,
        0
    ]

class popLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    COMMENT = 4
    QUOTEDSTRING = 5
    FLAG = 6
    STRING = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'#'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "QUOTEDSTRING", "FLAG", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "COMMENT", "QUOTEDSTRING", "FLAG", 
                  "STRING", "WS" ]

    grammarFileName = "pop.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


