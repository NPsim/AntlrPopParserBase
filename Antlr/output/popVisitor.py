# Generated from ./pop.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .popParser import popParser
else:
    from popParser import popParser

# This class defines a complete generic visitor for a parse tree produced by popParser.

class popVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by popParser#pop.
    def visitPop(self, ctx:popParser.PopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#keyvalue.
    def visitKeyvalue(self, ctx:popParser.KeyvalueContext):
        
        # This section was manually written. Rebuilding Antlr will wipe this!
        # Print keyvalue pairs
        if ctx.getChild(1).getRuleContext().getRuleIndex() == ctx.parser.RULE_atomicvalue:
          print("\tKey:", ctx.key().getText())
          print("\t\tValue:", ctx.getChild(1).getText())

        # This section was manually written. Rebuilding Antlr will wipe this!
        # Print start of lists
        elif ctx.getChild(1).getRuleContext().getRuleIndex() == ctx.parser.RULE_listvalue:
          print("List:", ctx.key().getText())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#key.
    def visitKey(self, ctx:popParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#atomicvalue.
    def visitAtomicvalue(self, ctx:popParser.AtomicvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#val.
    def visitVal(self, ctx:popParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#listvalue.
    def visitListvalue(self, ctx:popParser.ListvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by popParser#directive.
    def visitDirective(self, ctx:popParser.DirectiveContext):
        return self.visitChildren(ctx)



del popParser