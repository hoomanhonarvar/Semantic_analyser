import json
import pandas as pd
from nutree import Tree, Node
data=[]
main_symbol_table = pd.DataFrame(data, columns=[ 'word', 'name', 'type','line'])
#adding key words to symbol table

def dict_to_tree(data, parent=Tree("Parse Tree")):
    node=parent.add(data["name"])

    for child_data in data.get("children", []):
        dict_to_tree(child_data, parent=node)
    return node

def load_tree_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    print(data)
    print(type(data))
    return dict_to_tree(data)

def print_tree(node, level=0):
    print("  " * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)
class SymbolTable:
    def __init__(self,parent=None):
        self.parent=parent
        self.symbols={}

    def define(self, name,value):
        self.symbols[name]=value
    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return f'Undefined variable: {name}'

class SemanticAnalyzer():
    def __int__(self,parse_tree):
        self.parse_tree=parse_tree
        self.global_scope=SymbolTable()
        self.current_scope=self.global_scope
    def analyze(self):
        return self._analyze_node(self.parse_tree)

    def _analyze_node(self, node):
        if node[0] == 'number':
            return node  # No semantic check needed for number literals
        elif node[0] == 'identifier':
            self.current_scope.lookup(node[1])
            return node
        elif node[0] == 'binop':
            left = self._analyze_node(node[1])
            right = self._analyze_node(node[3])
            op = node[2][1]
            if op in ('+', '-', '*', '/'):
                if left[0] != 'number' or right[0] != 'number':
                    raise TypeError('Operands must be numbers')
            return ('binop', left, node[2], right)
        elif node[0] == 'assignment':
            identifier = node[1]
            value = self._analyze_node(node[2])
            self.current_scope.define(identifier[1], value)
            return ('assignment', identifier, value)
        elif node[0] == 'block':
            self._enter_scope()
            for stmt in node[1]:
                self._analyze_node(stmt)
            self._exit_scope()
            return ('block', node[1])
        else:
            raise ValueError(f'Unknown node type: {node[0]}')

    def _enter_scope(self):
        new_scope = SymbolTable(parent=self.current_scope)
        self.current_scope = new_scope

    def _exit_scope(self):
        self.current_scope = self.current_scope.parent


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.block()

    def block(self):
        statements = []
        while self.current_token_index < len(self.tokens):
            statements.append(self.statement())
        return ('block', statements)

    def statement(self):
        token = self.tokens[self.current_token_index]
        if token[0] == 'ID' and self._peek()[0] == 'ASSIGN':
            return self.assignment()
        else:
            return self.expression()

    def assignment(self):
        identifier = self.tokens[self.current_token_index]
        self.current_token_index += 1  # Skip the identifier
        self.current_token_index += 1  # Skip the '='
        value = self.expression()
        if self._peek()[0] == 'END':
            self.current_token_index += 1  # Skip the ';'
        return ('assignment', identifier, value)

    def expression(self):
        left = self.term()
        while self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index][0] in ('OP',):
            op = self.tokens[self.current_token_index]
            self.current_token_index += 1
            right = self.term()
            left = ('binop', left, op, right)
        return left

    def term(self):
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        if token[0] == 'NUMBER':
            return ('number', token[1])
        elif token[0] == 'ID':
            return ('identifier', token[1])
        raise SyntaxError(f'Unexpected token: {token}')

    def _peek(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None


loaded_tree = load_tree_from_file("parse_tree.json")
