import json
import pandas as pd
from nutree import Tree, Node, IterMethod

data=[]
main_symbol_table = pd.DataFrame(data, columns=[ 'word', 'name', 'type','line'])
#adding key words to symbol table
class customNode:
    def __init__(self,name):
        self.value=0
        self.type=""
        self.expected_type=""
        self.name=name


f=open("tokens_without_space.txt")
def reverse_sibling_order(node: Tree):
    # If the node has children, reverse the order of the children
    if node.children:
        node.children.reverse()
        # Recursively call the function on each child
        for child in node.children:
            reverse_sibling_order(child)
def dict_to_tree(data, parent=Tree("Parse Tree")):
    new_node=parent.add(customNode(data["name"]))

    for child_data in data.get("children", []):
        dict_to_tree(child_data, parent=new_node)
    return new_node

def load_tree_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    print(data)
    print(type(data))
    return dict_to_tree(data)

def print_tree(node, level=0):
    print("  " * level + node.data.name + "   = "+str(node.data.value))
    for child in node.children:
        print_tree(child, level + 1)
class SymbolTable:
    def __init__(self,parent=None):
        self.parent=parent
        self.symbols={}

    def define(self, name,type):
        self.symbols[name]=type
    def lookup_current(self, name):
        if name in self.symbols:
            return self.symbols[name]
        # else:
        #     return f'Undefined variable: {name}'
        else:
            return None
    def lookup_parent(self,name):
        if self.parent:
            if name in self.parent.symbols:
                return self.parent.symbols[name]
        else:
            return None
def get_perv_siblings(node):
    list=[]
    if node!=node.first_sibling():
        prev_node=node.prev_sibling()
        list.append(prev_node)
        while node.parent.first_child()!=prev_node:
            prev_node=prev_node.prev_sibling()
            list.append(prev_node)
    return list

def after_Expression(node,y):
    tmp_node=node.last_child()
    while tmp_node.data.value!="ε":
        tmp_node=tmp_node.last_child()
    tmp_node.data.value=tmp_node.prev_sibling().data.value
    tmp_node.data.type=tmp_node.prev_sibling().data.type
    while tmp_node!=node.last_child():
        if tmp_node.parent.data.type!=tmp_node.data.type:
            print("error unmatched type :",y)
        else:
            if tmp_node.parent.first_child().data.name=="T_AOp_PL":
                tmp_node.parent.data.value+=tmp_node.data.value
            else:
                tmp_node.parent.data.value -= tmp_node.data.value
        tmp_node=tmp_node.parent
    node.data.value=tmp_node.data.value
    node.data.type=tmp_node.data.type


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

                match node.data.name:
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
                        if node.prev_sibling().data.name=="AssignmentPrime":
                            if node.prev_sibling().data.value!="ε":
                                after_Expression(node.prev_sibling().last_child(),y)



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
                        node.last_child()
                        if node.prev_sibling().first_child()=="T_LOp_NOT" and node.parent.data.name=="Term":
                            node.prev_sibling().data.type="bool"
                            if node.prev_sibling().children[1].data.type!=node.prev_sibling().data.type:
                                print("error you use ! token with not bool factor")
                            else:
                                node.prev_sibling().data.value=not node.prev_sibling().children[1].data.value
                        print(node.prev_sibling().data.value)
                        node.data.value=node.prev_sibling().data.value
                        node.data.type=node.prev_sibling().data.type
                    case "Aop":
                        x=2
                    case "Factor":
                        if node.parent.data.name =="TermPrime":
                            if node.prev_sibling().data.name=="Operation":
                                node.prev_sibling().data.value=node.prev_sibling().first_child().data.value
                    case "FunctionCall":
                        x=2
                    case "ArgumentList":
                        x=2
                    case "ArgumentListPrime":
                        if node.parent.data.name=="ArgumentList" or node.parent.data.name=="ArgumentListPrime":
                            after_Expression(node.prev_sibling(),y)

                    case "Condition_tmp":
                        x=2
                    case "FunctionCallPrime":
                        x=2
                    case "Assignment_Declaration":
                        x=2
                    case "Operation":
                        x=2
                    case "ExpressionPrime":
                        tmp_node=node.prev_sibling().last_child()
                        if node.prev_sibling().last_child().data.value=="ε":
                            node.prev_sibling().data.value=node.prev_sibling().first_child().data.value
                            node.prev_sibling().data.type=node.prev_sibling().first_child().data.type
                        else:
                            while tmp_node.data.value!="ε":
                                tmp_node=tmp_node.last_child()
                            tmp_node.data.value=tmp_node.prev_sibling().data.value
                            tmp_node.data.type=tmp_node.prev_sibling().data.type
                            while tmp_node!=node.prev_sibling().last_child():
                                if tmp_node.parent.data.type!=tmp_node.data.type:
                                    print("error unmatched type :",y)
                                else:
                                    match tmp_node.parent.first_child().data.value:
                                        case "T_LOp_AND":
                                            tmp_node.parent.data.value= tmp_node.parent.data.value and tmp_node.data.value
                                        case "T_LOp_OR":
                                            tmp_node.parent.data.value = tmp_node.parent.data.value or tmp_node.data.value
                                        case "T_AOp_DV":
                                            tmp_node.parent.data.value = tmp_node.parent.data.value / tmp_node.data.value
                                        case "T_AOp_ML":
                                            tmp_node.parent.data.value = tmp_node.parent.data.value * tmp_node.data.value
                                        case "T_AOp_RM":
                                            tmp_node.parent.data.value = tmp_node.parent.data.value % tmp_node.data.value
                                        case "T_ROp_NE":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value!=tmp_node.data.value:
                                                tmp_node.parent.data.value=False
                                            else:
                                                tmp_node.parent.data.value=True
                                        case "T_ROp_E":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value == tmp_node.data.value:
                                                tmp_node.parent.data.value = True
                                            else:
                                                tmp_node.parent.data.value = False
                                        case "T_ROp_L":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value < tmp_node.data.value:
                                                tmp_node.parent.data.value = True
                                            else:
                                                tmp_node.parent.data.value = False
                                        case "T_ROp_LE":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value <= tmp_node.data.value:
                                                tmp_node.parent.data.value = True
                                            else:
                                                tmp_node.parent.data.value = False
                                        case "T_ROp_GE":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value >= tmp_node.data.value:
                                                tmp_node.parent.data.value = True
                                            else:
                                                tmp_node.parent.data.value = False
                                        case "T_ROp_G":
                                            tmp_node.parent.data.type = "bool"
                                            if tmp_node.parent.data.value > tmp_node.data.value:
                                                tmp_node.parent.data.value = True
                                            else:
                                                tmp_node.parent.data.value = False
                                tmp_node=tmp_node.parent
                            node.prev_sibling().data.type=tmp_node.data.type
                            node.prev_sibling().data.value=tmp_node.data.value


                            node.data.value=node.prev_sibling().data.value
                            node.data.type=node.prev_sibling().data.type


                    case "Exp_Or_None":
                        x=2
                    case "_":
                        raise ValueError(f'Unknown node type: {node[0]}')
            else:
                if node.data.name!="ε":
                    y=(f.readline())
                    # print(y,node.name)
                match node.data.name:
                    #self.current_scope.define(identifier[1], value)
                    case "T_Id":
                        if node.is_last_sibling():
                            founded_node = self.current_scope.lookup_current(y.split(" ")[2][:-1])
                        elif not node.next_sibling().is_leaf():
                            if not node.next_sibling().first_child().is_leaf():
                                if node.next_sibling().first_child().first_child().data.name=="T_LP" :
                                    founded_node = self.current_scope.lookup_parent(y.split(" ")[2][:-1])

                            elif node.next_sibling().first_child().data.name=="T_LP" :
                                founded_node = self.current_scope.lookup_parent(y.split(" ")[2][:-1])
                            else :
                                founded_node = self.current_scope.lookup_current(y.split(" ")[2][:-1])
                            #function
                        else:
                            founded_node = self.current_scope.lookup_current(y.split(" ")[2][:-1])
                        if founded_node==None:
                            if not node.is_first_sibling():
                                if node.prev_sibling().data.name=="Type":
                                    node.data.expected_type = node.prev_sibling().data.expected_type
                                    self.current_scope.define(y.split(" ")[2][:-1],node.data.expected_type)
                                else:
                                    print("error this Id never has been declared!  ",f'line is :{y.split(" ")[0]}')
                            else:
                                print("error this Id never has been declared!  ", f'line is :{y.split(" ")[0]}')
                        # elif node.parent.data.name!="FunctionDeclaration" and node.parent.data.name!="Parameter" and node.parent.data.name!="Parameter":
                        #     if founded_node!=node.data.expected_type:
                        #         print("it should be an error")





                    case "T_String":
                        string = y.split("T_String")[1]
                        node.data.value = string[3:-2]
                        node.data.type="char"
                        node.parent.data.value=node.data.value
                        node.parent.data.type=node.data.type
                    case "T_Character":
                        char = y.split("'")[1]
                        node.data.value = char
                        node.data.type="char"
                        node.parent.data.value = node.data.value
                        node.parent.data.type = node.data.type
                    case "T_Decimal":
                        num=y.split(" ")[2]
                        node.data.value = int(num)
                        node.data.type="int"
                        node.parent.data.value = node.data.value
                        node.parent.data.type = node.data.type
                    case "T_Hexadecimal":
                        num = y.split(" ")[2]
                        node.data.value=int(num,16)
                        node.data.type="int"
                        node.parent.data.value = node.data.value
                        node.parent.data.type = node.data.type
                    case "T_LC":
                        self._enter_scope()
                    case "T_RC":
                        self._exit_scope()
                        x=3
                    case "T_Int":
                        node.parent.data.expected_type="int"
                    case "T_Char":
                        node.parent.data.expected_type="char"
                    case "T_Bool":
                        node.parent.data.expected_type="bool"
                    case "T_True":
                        node.data.type="bool"
                        node.data.value=True
                        node.parent.data.value = node.data.value
                        node.parent.data.type = node.data.type
                    case "T_False":
                        node.data.type="bool"
                        node.data.value=False
                        node.parent.data.value = node.data.value
                        node.parent.data.type = node.data.type
                    case "T_LOp_NOT":
                        x=2
                    case "T_RP":
                        if node.parent.data.name == "Factor":
                            node.parent.data.type = node.prev_sibling().data.type
                            node.parent.data.value = node.prev_sibling().data.value
                        if node.parent.data.name=="IfStatement":
                            after_Expression(node.prev_sibling(),y)
                        if node.parent.data.name=="Loop":
                            after_Expression(node.prev_sibling().prev_sibling(),y)
                    case "T_LOp_AND":
                        node.parent.data.value="T_LOp_AND"
                    case "T_LOp_OR":
                        node.parent.data.value="T_LOp_OR"
                    case "T_ROp_NE":
                        node.parent.data.value="T_ROp_NE"
                    case "T_ROp_E":
                        node.parent.data.value = "T_ROp_E"
                    case "T_ROp_L":
                        node.parent.data.value = "T_ROp_L"
                    case "T_ROp_G":
                        node.parent.data.value = "T_ROp_G"
                    case "T_ROp_LE":
                        node.parent.data.value = "T_ROp_LE"
                    case "T_ROp_GE":
                        node.parent.data.value = "T_ROp_GE"
                    case "T_AOp_DV":
                        node.parent.data.value = "T_AOp_DV"
                    case "T_AOp_ML":
                        node.parent.data.value = "T_AOp_ML"
                    case "T_AOp_RM":
                        node.parent.data.value = "T_AOp_RM"
                    case "ε":
                        node.parent.data.value="ε"

                    case "T_RB":
                        if node.parent.data.name=="ArraySpecifier":
                            after_Expression(node.prev_sibling(),y)
                    case "T_Semicolon":
                        if node.prev_sibling().first_child()=="Assignment":
                            after_Expression(node.prev_sibling().first_child(),y)

                    case "_":
                        print(y, node.name)





    def _enter_scope(self):
        new_scope = SymbolTable(parent=self.current_scope)
        self.current_scope = new_scope

    def _exit_scope(self):
        self.current_scope = self.current_scope.parent

loaded_tree = load_tree_from_file("parse_tree.json")
# print_tree(loaded_tree)
reverse_sibling_order(loaded_tree)
semantic_analyzer=SemanticAnalyzer(loaded_tree)
semantic_analyzer.analyze()
print(semantic_analyzer.current_scope.symbols)
print_tree(loaded_tree)
