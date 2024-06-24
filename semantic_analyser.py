import json
import pandas as pd
from nutree import Tree, Node, IterMethod

data=[]
main_symbol_table = pd.DataFrame(data, columns=[ 'word', 'name', 'type','line'])
#adding key words to symbol table
f=open("tokens_without_space.txt")
def reverse_sibling_order(node: Tree):
    # If the node has children, reverse the order of the children
    if node.children:
        node.children.reverse()
        # Recursively call the function on each child
        for child in node.children:
            reverse_sibling_order(child)
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
    def analyze(self,tokens_witouht_space=f):
        return self._analyze_node(self.parse_tree,tokens_witouht_space)

    def _analyze_node(self, node,f):
        count=0
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
                # print("hello")
                x = 2
            if not node.is_leaf():
                match node.name:
                    case "program":
                        x=2
                    case "FunctionDeclarations":
                        x=2
                    case "FunctionDeclaration":
                        x=2
                    case "ParameterList":
                        x=2
                    case "ParameterListPrime":
                        x=2
                    case "Parameter":
                        x=2
                    case "Declarations":
                        x=2
                    case "Declaration":
                        x=2
                    case "AssignmentPrime":
                        x=2
                    case "Type":
                        x=2
                    case "ArraySpecifier":
                        x=2
                    case "Num":
                        x=2
                    case "Statements":
                        x=2
                    case "Statement":
                        x=2
                    case "StatementPrime":
                        x=2
                    case "Assignment":
                        x=2
                    case "PrintStatement":
                        x=2
                    case "FormattingString":
                        x=2
                    case "ExpressionList":
                        x=2
                    case "ExpressionsList":
                        x=2
                    case "Loop":
                        x=2
                    case "IfStatement":
                        x=2
                    case "ElsePart":
                        x=2
                    case "Block":
                        x=2
                    case "Condition":
                        x=2
                    case "RO_Expression":
                        x=2
                    case "T_ROp":
                        x=2
                    case "ConditionPrime":
                        x=2
                    case "T_LOp":
                        x=2
                    case "Expression":
                        x=2
                    case "Term":
                        x=2
                    case "TermPrime":
                        x=2
                    case "Aop":
                        x=2
                    case "Factor":
                        x=2
                    case "FunctionCall":
                        x=2
                    case "ArgumentList":
                        x=2
                    case "ArgumentListPrime":
                        x=2
                    case "Condition_tmp":
                        x=2
                    case "FunctionCallPrime":
                        x=2
                    case "Assignment_Declaration":
                        x=2
                    case "Operation":
                        x=2
                    case "ExpressionPrime":
                        x=2
                    case "Exp_Or_None":
                        x=2
                    case "_":
                        raise ValueError(f'Unknown node type: {node[0]}')
            else:
                if node.name!="ε":
                    y=(f.readline())
                    print(y,node.name)
                match node.name:
                    #self.current_scope.define(identifier[1], value)
                    case "T_Id":
                        x=2
                    case "T_String":
                        x=2
                    case "T_Character":
                        x=2
                    case "T_Decimal":
                        print(y,node.name)
                    case "T_Hexadecimal":
                        x=2
                    case "T_LC":
                        self._enter_scope()
                    case "T_RC":
                        self._exit_scope()
                    case "_":
                        x=2


    def _enter_scope(self):
        new_scope = SymbolTable(parent=self.current_scope)
        self.current_scope = new_scope

    def _exit_scope(self):
        self.current_scope = self.current_scope.parent

loaded_tree = load_tree_from_file("parse_tree.json")
# print_tree(loaded_tree)
reverse_sibling_order(loaded_tree)
print_tree(loaded_tree)
semantic_analyzer=SemanticAnalyzer(loaded_tree)
semantic_analyzer.analyze()

