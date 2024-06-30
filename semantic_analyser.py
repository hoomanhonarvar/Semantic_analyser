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
    print("  " * level + node.data.name + "   = "+str(node.data.value)+ "   = "+str(node.data.type))
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
                tmp_node.parent.data.value +=tmp_node.data.value
            else:
                tmp_node.parent.data.value -= tmp_node.data.value
        tmp_node=tmp_node.parent
    node.data.value=tmp_node.data.value
    node.data.type=tmp_node.data.type
def after_Term(node,y):
    tmp_node = node.last_child()
    while tmp_node.data.value != "ε":
        tmp_node = tmp_node.last_child()
    tmp_node.data.value = tmp_node.prev_sibling().data.value
    tmp_node.data.type = tmp_node.prev_sibling().data.type
    while tmp_node != node.last_child():
        print(tmp_node.data.value, " ",tmp_node.data.type)
        print(tmp_node.parent.data.value, " ", tmp_node.parent.data.type," ",tmp_node.parent.data.name)
        if tmp_node.parent.data.type != tmp_node.data.type:
            print("error unmatched type :", y)
        else:
            print("salam")
            print(tmp_node.parent.first_child().data.value)
            match tmp_node.parent.first_child().data.value:
                case "T_LOp_AND":
                    if tmp_node.parent.data.type != "bool":
                        print("error logical operator for not bool", y.split(" ")[0])
                    else:
                        tmp_node.parent.data.value = tmp_node.parent.data.value and tmp_node.data.value
                case "T_LOp_OR":
                    if tmp_node.parent.data.type != "bool":
                        print("error logical operator for not bool", y.split(" ")[0])
                    else:
                        tmp_node.parent.data.value = tmp_node.parent.data.value or tmp_node.data.value
                case "T_AOp_DV":
                    if tmp_node.parent.data.type != "int":
                        print("error Arithmatic operator for not int", y.split(" ")[0])
                    else:
                        tmp_node.parent.data.value = tmp_node.parent.data.value / tmp_node.data.value
                case "T_AOp_ML":
                    if tmp_node.parent.data.type != "int":
                        print("error Arithmatic operator for not int", y.split(" ")[0])
                    else:
                        tmp_node.parent.data.value = tmp_node.parent.data.value * tmp_node.data.value
                case "T_AOp_RM":
                    if tmp_node.parent.data.type != "int":
                        print("error Arithmatic operator for not int", y.split(" ")[0])
                    else:
                        tmp_node.parent.data.value = tmp_node.parent.data.value % tmp_node.data.value
                case "T_ROp_NE":
                    tmp_node.parent.data.type = "bool"
                    if tmp_node.parent.data.value != tmp_node.data.value:
                        tmp_node.parent.data.value = False
                    else:
                        tmp_node.parent.data.value = True
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
                    print("fuck")
                    print(tmp_node.parent.data.value)
                    tmp_node.parent.data.type = "bool"
                    if tmp_node.parent.data.value > tmp_node.data.value:
                        tmp_node.parent.data.value = True
                    else:
                        tmp_node.parent.data.value = False
        tmp_node = tmp_node.parent
    node.data.value = tmp_node.data.value
    node.data.type = tmp_node.data.type
def get_type_of_current_function(node):

    while node.data.name!="FunctionDeclaration":
        node=node.parent
    return node.first_child().data.type
def after_ParameterList(node,y):
    if node.data.value!="ε":
        tmp_node=node.last_child()
        while tmp_node.data.value!="ε":
            tmp_node=tmp_node.last_child()
        tmp_node.data.value=[]
        tmp_node.data.value.append([tmp_node.prev_sibling().data.type,tmp_node.prev_sibling().data.value])
        while tmp_node!=node.last_child():
            for i in tmp_node.data.value:
                tmp_node.parent.data.value.append(i)
            tmp_node=tmp_node.parent
        node.data.value=tmp_node.data.value

class SemanticAnalyzer:
    def __init__(self,parse_tree):
        self.parse_tree=parse_tree
        self.global_scope=SymbolTable()
        self.current_scope=self.global_scope
        self.main_function=False

    def analyze(self,tokens_witouht_space=f):
        return self._analyze_node(self.parse_tree,tokens_witouht_space)

    def _analyze_node(self, node,f):
        count=0
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
                        node.data.value=[]
                        node.data.value.append([node.prev_sibling().data.type,node.prev_sibling().data.value])
                    case "Parameter":
                        x=2
                    case "Declarations":
                        if node.prev_sibling().data.name=="AssignmentPrime":
                            if node.prev_sibling().data.value!="ε":
                                after_Expression(node.prev_sibling().last_child(),y)
                        if node.parent.data.name=="Declaration":
                            if node.parent.children[1].data.type!=node.parent.children[3].last_child().data.type:
                                print("error unmatched type in declaration ",y.split(" ")[0])


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
                        if node.parent.data.name=="FunctionDeclaration":
                            if self.global_scope.lookup_current(node.parent.children[1].data.value)==None:

                                self.global_scope.define(node.parent.children[1].data.value,[node.first_sibling().data.type,node.parent.children[3].data.value,True])


                            else:
                                print("error this function has already defined  ",y.split(" ")[0])
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
                                print("error you use ! token with not bool factor",y.split(" ")[0])
                            else:
                                node.prev_sibling().data.value=not node.prev_sibling().children[1].data.value
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
                        node.data.value=[]
                        if node.parent.data.name=="ArgumentList" or node.parent.data.name=="ArgumentListPrime":
                            after_Expression(node.prev_sibling(),y)
                        node.data.value.append([node.prev_sibling().data.type,node.prev_sibling().data.value])

                    case "Condition_tmp":
                        x=2
                    case "FunctionCallPrime":
                        node.parent.data.type=node.prev_sibling().data.type
                    case "Assignment_Declaration":
                        x=2
                    case "Operation":
                        x=2
                    case "ExpressionPrime":
                        after_Term(node.prev_sibling(),y)
                        # tmp_node=node.prev_sibling().last_child()
                        # if node.prev_sibling().last_child().data.value=="ε":
                        #     node.prev_sibling().data.value=node.prev_sibling().first_child().data.value
                        #     node.prev_sibling().data.type=node.prev_sibling().first_child().data.type
                        # else:
                        #     while tmp_node.data.value!="ε":
                        #         tmp_node=tmp_node.last_child()
                        #     tmp_node.data.value=tmp_node.prev_sibling().data.value
                        #     tmp_node.data.type=tmp_node.prev_sibling().data.type
                        #     while tmp_node!=node.prev_sibling().last_child():
                        #
                        #         if tmp_node.parent.data.type!=tmp_node.data.type  :
                        #             print(tmp_node.parent.data.type," alkj ",tmp_node.data.type)
                        #             print(tmp_node.parent.data.name," aljk ",tmp_node.data.name)
                        #             print(tmp_node.parent.data.value," aljk ",tmp_node.data.value)
                        #
                        #             print(tmp_node.parent.parent.data.name)
                        #             print("error unmatched type :",y.split(" ")[0])
                        #         else:
                        #             match tmp_node.parent.first_child().data.value:
                        #                 case "T_LOp_AND":
                        #                     if tmp_node.parent.data.type!="bool":
                        #                         print("error logical operator for not bool" ,y.split(" ")[0])
                        #                     else:
                        #                         tmp_node.parent.data.value= tmp_node.parent.data.value and tmp_node.data.value
                        #                 case "T_LOp_OR":
                        #                     if tmp_node.parent.data.type!="bool":
                        #                         print("error logical operator for not bool",y.split(" ")[0])
                        #                     else:
                        #                         tmp_node.parent.data.value = tmp_node.parent.data.value or tmp_node.data.value
                        #                 case "T_AOp_DV":
                        #                     if tmp_node.parent.data.type!="int":
                        #                         print("error Arithmatic operator for not int",y.split(" ")[0])
                        #                     else:
                        #                         tmp_node.parent.data.value = tmp_node.parent.data.value / tmp_node.data.value
                        #                 case "T_AOp_ML":
                        #                     if tmp_node.parent.data.type != "int":
                        #                         print("error Arithmatic operator for not int",y.split(" ")[0])
                        #                     else:
                        #                         tmp_node.parent.data.value = tmp_node.parent.data.value * tmp_node.data.value
                        #                 case "T_AOp_RM":
                        #                     if tmp_node.parent.data.type != "int":
                        #                         print("error Arithmatic operator for not int",y.split(" ")[0])
                        #                     else:
                        #                         tmp_node.parent.data.value = tmp_node.parent.data.value % tmp_node.data.value
                        #                 case "T_ROp_NE":
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value!=tmp_node.data.value:
                        #                         tmp_node.parent.data.value=False
                        #                     else:
                        #                         tmp_node.parent.data.value=True
                        #                 case "T_ROp_E":
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value == tmp_node.data.value:
                        #                         tmp_node.parent.data.value = True
                        #                     else:
                        #                         tmp_node.parent.data.value = False
                        #                 case "T_ROp_L":
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value < tmp_node.data.value:
                        #                         tmp_node.parent.data.value = True
                        #                     else:
                        #                         tmp_node.parent.data.value = False
                        #                 case "T_ROp_LE":
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value <= tmp_node.data.value:
                        #                         tmp_node.parent.data.value = True
                        #                     else:
                        #                         tmp_node.parent.data.value = False
                        #                 case "T_ROp_GE":
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value >= tmp_node.data.value:
                        #                         tmp_node.parent.data.value = True
                        #                     else:
                        #                         tmp_node.parent.data.value = False
                        #                 case "T_ROp_G":
                        #                     print("fuck")
                        #                     print(tmp_node.parent.data.value)
                        #                     tmp_node.parent.data.type = "bool"
                        #                     if tmp_node.parent.data.value > tmp_node.data.value:
                        #                         tmp_node.parent.data.value = True
                        #                     else:
                        #                         tmp_node.parent.data.value = False
                        #         tmp_node=tmp_node.parent
                        #     node.prev_sibling().data.type=tmp_node.data.type
                        #     node.prev_sibling().data.value=tmp_node.data.value
                        #
                        #
                        # node.data.value=node.prev_sibling().data.value
                        # node.data.type=node.prev_sibling().data.type


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
                        name=y.split(" ")[2][:-1]
                        node.data.value=name
                        if node.parent.data.name=="Parameter":
                            node.parent.data.value=name
                            node.parent.data.type=node.prev_sibling().data.type

                        if node.parent.data.name=="FunctionDeclaration":
                            if self.global_scope.lookup_current(name)==None:
                                node.data.value=name
                                node.data.type=node.prev_sibling().data.value
                            else:
                                print("error this Id has been declared!  ",f'line is :{y.split(" ")[0]}')
                        if node.parent.data.name=="Declaration":
                            if self.current_scope.lookup_current(name) == None:
                                node.data.type=node.prev_sibling().data.type
                                self.current_scope.define(name, [node.prev_sibling().data.type,False])
                            else:
                                print("error this Id has been declared!  ", f'line is :{y.split(" ")[0]}')
                        if node.parent.data.name=="Statement":
                            if node.next_sibling().first_child().data.name=="FunctionCallPrime":
                                if self.current_scope.lookup_current(name) == None:
                                    if self.current_scope.lookup_current(name)[1]==False:
                                        print("error this function Id never has been declared!  ", f'line is :{y.split(" ")[0]}')
                                    else:
                                        node.data.type=self.current_scope.lookup_current(name)[0]


                            else:
                                if self.current_scope.lookup_current(name)==None:
                                    print("error this Id never has been declared!  ", f'line is :{y.split(" ")[0]}')
                                else:
                                    node.data.type = self.current_scope.lookup_current(name)
                        if node.parent.data.name=="Assignment":
                            if self.current_scope.lookup_current(name) == None:
                                print("error this Id never has been declared!  ", f'line is :{y.split(" ")[0]}')
                            else:
                                node.data.type=self.current_scope.lookup_current(name)[0]
                        if node.parent.data.name=="Factor":
                            if self.current_scope.lookup_current(name) == None:
                                print("error this Id never has been declared!  ", f'line is :{y.split(" ")[0]}')
                            else:
                                print(self.current_scope.lookup_current(name)[0])
                                node.data.type=self.current_scope.lookup_current(name)




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
                        if node.parent.parent.data.name=="FunctionDeclaration":
                            if node.parent.parent.children[3].data.value!="ε":
                                for i in node.parent.parent.children[3].data.value:
                                    self.current_scope.define(i[1],i[0])
                    case "T_RC":
                        self._exit_scope()
                        x=3
                    case "T_Int":
                        node.parent.data.type="int"
                    case "T_Char":
                        node.parent.data.type="char"
                    case "T_Bool":
                        node.parent.data.type="bool"
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
                            after_Expression(node.prev_sibling(),y)
                            node.parent.data.type = node.prev_sibling().data.type
                            node.parent.data.value = node.prev_sibling().data.value
                        if node.parent.data.name=="IfStatement":
                            after_Expression(node.prev_sibling(),y)
                            if node.prev_sibling().data.type!="bool":
                                print("error not bool expression in if statement ",y.split(" ")[0])
                        if node.parent.data.name=="Loop":
                            after_Expression(node.prev_sibling().last_child(),y.split(" ")[0])

                            if node.prev_sibling().data.name=="Assignment":
                                if node.prev_sibling().first_child().data.type!=node.prev_sibling().last_child().data.type:
                                    print("error unmatched type in assignment ",y.split(" ")[0])
                        if node.parent.data.name=="FunctionDeclaration" and node.parent.children[1].data.value=="main":
                            if node.prev_sibling().data.value!="ε":
                                print("error parameter list in main function is not empty" , y.split(" ")[0])
                            if node.first_sibling().data.type!="int":
                                print("error function type of main function is not int ",y.split(" ")[0])
                        if node.parent.data.name=="FunctionDeclaration":
                            after_ParameterList(node.prev_sibling(),y)
                        if node.parent.data.name=="FunctionCallPrime":
                            after_ParameterList(node.prev_sibling(),y)
                            # func=self.global_scope.lookup_current(node.parent.prev_sibling().data.value)
                            if node.parent.parent.data.name=="Factor":
                                print("hello",node.parent.prev_sibling().data.value ,node.parent.prev_sibling().name)
                            if node.parent.parent.data.name=="StatementPrime":
                                func = self.global_scope.lookup_current(node.parent.parent.prev_sibling().data.value)
                                if func[2]==True:
                                    node.parent.data.type=func[0]
                                    if len(node.prev_sibling().data.value)!=len(func[1]):
                                        print("error unmatched argument list of function " ,y.split(" ")[0])
                                    else:
                                        for i,j in func[1],node.prev_sibling().data.value:
                                            if i[0]!=j[0]:
                                                print("error unmatched type of argument of function",y.split(" ")[0])


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
                            if node.prev_sibling().data.type!="int":
                                print("error not int expression for array specifier",y.split(" ")[0])
                            else:
                                if node.prev_sibling().data.value<1:
                                    print("error expression int array specifier is less than 1",y.split(" ")[0])
                    case "T_Semicolon":
                        if node.prev_sibling().first_child()=="Assignment":
                            after_Expression(node.prev_sibling().first_child(),y.split(" ")[0])
                        if node.prev_sibling().first_child()=="AssignmentPrime":
                            if node.prev_sibling().first_child().last_child().data.type!=node.parent.first_child().data.type:
                                print("error unmatched type in assignment ", y.split(" ")[0])
                        if node.prev_sibling().data.name=="Expression" and node.first_sibling().data.name=="T_Return":
                            after_Expression(node.prev_sibling(), y)
                            if node.prev_sibling().data.type!=get_type_of_current_function(node):
                                print("error return type is not equal to its function" , y.split(" ")[0])
                        if node.prev_sibling().data.name=="Assignment_Declaration":
                            node_tmp = node.prev_sibling().first_child()
                            if node.prev_sibling().first_child().data.name=="Assignment":

                                if node_tmp.first_child().data.type!=node_tmp.last_child().data.type:
                                    print("error unmatched type in assignment ",y.split(" ")[0])
                            else:
                                if node_tmp.children[3].data.value!="ε":
                                    if node_tmp.children[1].data.type!=node_tmp.children[3].last_child().data.type:
                                        print("error unmatched type in assignment ",y.split(" ")[0])
                        if node.prev_sibling().data.name=="StatementPrime":
                            if node.prev_sibling().first_child().data.name=="AssignmentPrime":
                                if node.prev_sibling().first_child().data.value!="ε":
                                    after_Expression(node.prev_sibling().first_child().last_child(),y)
                    case "_":
                        print(y, node.name)
        available_main=False
        for function in self.global_scope.symbols:
            if function=="main":
                available_main=True

        if not available_main:
            print("error whole program doesn't have main function")






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
