import json
import pandas as pd
from nutree import Tree, Node, IterMethod

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
def get_perv_siblings(node):
    list=[]
    if node!=node.first_sibling():
        prev_node=node.prev_sibling()
        list.append(prev_node)
        while node.parent.first_child()!=prev_node:
            prev_node=prev_node.prev_sibling()
            list.append(prev_node)
    return list
class SemanticAnalyzer:
    def __init__(self,parse_tree):
        self.parse_tree=parse_tree
        self.global_scope=SymbolTable()
        self.current_scope=self.global_scope
    def analyze(self):
        return self._analyze_node(self.parse_tree)

    def _analyze_node(self, node):
        # # print("node is ",node.name)
        # if (len(node.children))!=0:
        #     for i in node.children:
        #         # print(f"{i} child is :", i.name)
        #         if node[0] == 'number':
        #             return node  # No semantic check needed for number literals
        #         elif node[0] == 'identifier':
        #             self.current_scope.lookup(node[1])
        #             return node
        #         elif node[0] == 'binop':
        #             left = self._analyze_node(node[1])
        #             right = self._analyze_node(node[3])
        #             op = node[2][1]
        #             if op in ('+', '-', '*', '/'):
        #                 if left[0] != 'number' or right[0] != 'number':
        #                     raise TypeError('Operands must be numbers')
        #             return ('binop', left, node[2], right)
        #         elif node[0] == 'assignment':
        #             identifier = node[1]
        #             value = self._analyze_node(node[2])
        #             self.current_scope.define(identifier[1], value)
        #             return ('assignment', identifier, value)
        #         elif node[0] == 'block':
        #             self._enter_scope()
        #             for stmt in node[1]:
        #                 self._analyze_node(stmt)
        #             self._exit_scope()
        #             return ('block', node[1])
        #         else:
        #             raise ValueError(f'Unknown node type: {node[0]}')
        #         # self._analyze_node(i)
        # else:
        #     print(node.name)
        for node in loaded_tree.iterator(method=IterMethod.PRE_ORDER):
            if node==node.last_sibling():
                #do the last semantic action
                print("hello")
            if not node.is_leaf():
                match node.name:
                    case "program":
                        print("hello")
                    case "FunctionDeclarations":
                        print("hello")
                    case "FunctionDeclaration":
                        print("hello")
                    case "ParameterList":
                        print("hello")
                    case "ParameterListPrime":
                        print("hello")
                    case "Parameter":
                        print("hello")
                    case "Declarations":
                        print("hello")
                    case "Declaration":
                        print("hello")
                    case "AssignmentPrime":
                        print("hello")
                    case "Type":
                        print("hello")
                    case "ArraySpecifier":
                        print("hello")
                    case "Num":
                        print("hello")
                    case "Statements":
                        print("hello")
                    case "Statement":
                        print("hello")
                    case "StatementPrime":
                        print("hello")
                    case "Assignment":
                        print("hello")
                    case "PrintStatement":
                        print("hello")
                    case "FormattingString":
                        print("hello")
                    case "ExpressionList":
                        print("hello")
                    case "ExpressionsList":
                        print("hello")
                    case "Loop":
                        print("hello")
                    case "IfStatement":
                        print("hello")
                    case "ElsePart":
                        print("hello")
                    case "Block":
                        print("hello")
                    case "Condition":
                        print("hello")
                    case "RO_Expression":
                        print("hello")
                    case "T_ROp":
                        print("hello")
                    case "ConditionPrime":
                        print("hello")
                    case "T_LOp":
                        print("hello")
                    case "Expression":
                        print("hello")
                    case "Term":
                        print("hello")
                    case "TermPrime":
                        print("hello")
                    case "Aop":
                        print("hello")
                    case "Factor":
                        print("hello")
                    case "FunctionCall":
                        print("hello")
                    case "ArgumentList":
                        print("hello")
                    case "ArgumentListPrime":
                        print("hello")
                    case "Condition_tmp":
                        print("hello")
                    case "FunctionCallPrime":
                        print("hello")
                    case "Assignment_Declaration":
                        print("hello")
                    case "Operation":
                        print("hello")
                    case "ExpressionPrime":
                        print("hello")
                    case "Exp_Or_None":
                        print("hello")
            else:
                match node.name:
                    case "T_Id":
                        print("hello")
                    case "T_String":
                        print("hello")
                    case "T_Character":
                        print("hello")
                    case "T_Decimal":
                        print("hello")
                    case "T_Hexadecimal":
                        print("hello")
                    case "_":
                        print("hello")


    def _enter_scope(self):
        new_scope = SymbolTable(parent=self.current_scope)
        self.current_scope = new_scope

    def _exit_scope(self):
        self.current_scope = self.current_scope.parent

loaded_tree = load_tree_from_file("parse_tree.json")

semantic_analyzer=SemanticAnalyzer(loaded_tree)
semantic_analyzer.analyze()

