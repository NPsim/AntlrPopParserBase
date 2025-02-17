# Generated from ./pop.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,
        1,0,1,0,1,1,1,1,1,1,4,1,32,8,1,11,1,12,1,33,3,1,36,8,1,1,2,1,2,1,
        3,1,3,1,4,1,4,1,5,1,5,5,5,46,8,5,10,5,12,5,49,9,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,2,0,5,5,7,7,54,0,17,1,0,
        0,0,2,28,1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,0,8,41,1,0,0,0,10,43,1,
        0,0,0,12,52,1,0,0,0,14,16,3,12,6,0,15,14,1,0,0,0,16,19,1,0,0,0,17,
        15,1,0,0,0,17,18,1,0,0,0,18,23,1,0,0,0,19,17,1,0,0,0,20,22,3,2,1,
        0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,
        1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,35,3,4,2,0,29,
        36,3,6,3,0,30,32,3,10,5,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,
        0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,29,1,0,0,0,35,31,1,0,0,0,36,3,
        1,0,0,0,37,38,3,8,4,0,38,5,1,0,0,0,39,40,3,8,4,0,40,7,1,0,0,0,41,
        42,7,0,0,0,42,9,1,0,0,0,43,47,5,1,0,0,44,46,3,2,1,0,45,44,1,0,0,
        0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,
        1,0,0,0,50,51,5,2,0,0,51,11,1,0,0,0,52,53,5,3,0,0,53,54,5,7,0,0,
        54,55,3,8,4,0,55,13,1,0,0,0,5,17,23,33,35,47
    ]

class popParser ( Parser ):

    grammarFileName = "pop.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "QUOTEDSTRING", "FLAG", "STRING", "WS" ]

    RULE_pop = 0
    RULE_keyvalue = 1
    RULE_key = 2
    RULE_atomicvalue = 3
    RULE_val = 4
    RULE_listvalue = 5
    RULE_directive = 6

    ruleNames =  [ "pop", "keyvalue", "key", "atomicvalue", "val", "listvalue", 
                   "directive" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    COMMENT=4
    QUOTEDSTRING=5
    FLAG=6
    STRING=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(popParser.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(popParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(popParser.DirectiveContext,i)


        def keyvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(popParser.KeyvalueContext)
            else:
                return self.getTypedRuleContext(popParser.KeyvalueContext,i)


        def getRuleIndex(self):
            return popParser.RULE_pop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPop" ):
                return visitor.visitPop(self)
            else:
                return visitor.visitChildren(self)




    def pop(self):

        localctx = popParser.PopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 14
                self.directive()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==7:
                self.state = 20
                self.keyvalue()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(popParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(popParser.KeyContext,0)


        def atomicvalue(self):
            return self.getTypedRuleContext(popParser.AtomicvalueContext,0)


        def listvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(popParser.ListvalueContext)
            else:
                return self.getTypedRuleContext(popParser.ListvalueContext,i)


        def getRuleIndex(self):
            return popParser.RULE_keyvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyvalue" ):
                return visitor.visitKeyvalue(self)
            else:
                return visitor.visitChildren(self)




    def keyvalue(self):

        localctx = popParser.KeyvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_keyvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.key()
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7]:
                self.state = 29
                self.atomicvalue()
                pass
            elif token in [1]:
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 30
                    self.listvalue()
                    self.state = 33 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

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


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self):
            return self.getTypedRuleContext(popParser.ValContext,0)


        def getRuleIndex(self):
            return popParser.RULE_key

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = popParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self):
            return self.getTypedRuleContext(popParser.ValContext,0)


        def getRuleIndex(self):
            return popParser.RULE_atomicvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicvalue" ):
                return visitor.visitAtomicvalue(self)
            else:
                return visitor.visitChildren(self)




    def atomicvalue(self):

        localctx = popParser.AtomicvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atomicvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self):
            return self.getToken(popParser.QUOTEDSTRING, 0)

        def STRING(self):
            return self.getToken(popParser.STRING, 0)

        def getRuleIndex(self):
            return popParser.RULE_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)




    def val(self):

        localctx = popParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==5 or _la==7):
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


    class ListvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(popParser.KeyvalueContext)
            else:
                return self.getTypedRuleContext(popParser.KeyvalueContext,i)


        def getRuleIndex(self):
            return popParser.RULE_listvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListvalue" ):
                return visitor.visitListvalue(self)
            else:
                return visitor.visitChildren(self)




    def listvalue(self):

        localctx = popParser.ListvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(popParser.T__0)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==7:
                self.state = 44
                self.keyvalue()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(popParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(popParser.STRING, 0)

        def val(self):
            return self.getTypedRuleContext(popParser.ValContext,0)


        def getRuleIndex(self):
            return popParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = popParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(popParser.T__2)
            self.state = 53
            self.match(popParser.STRING)
            self.state = 54
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





