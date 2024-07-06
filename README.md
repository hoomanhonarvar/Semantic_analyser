# Semantic Analyser

* compiler project part_3
* implementing Semantic analyser for PL language

## Description
In this part of compiler project we should implement and design a SDD for our compiler which apply semantic rules to the program to check some principles of PL language.
Before using semantic analyaser you should run your lexicon and syntax parser and the parse tree should be sent to semantic analyser.
After semantic analyser you can create Intermediate code and optimze it and create assembly for better approach and after that the final language is machine code :) .

## Getting Started

### Dependencies

* reading a lexeme analyser in https://github.com/hoomanhonarvar/lexeme_analyser
* reading a syntax analyser in https://github.com/hoomanhonarvar/syntax_analyser

### Executing program

* run lexeme analyser
  
```
lexeme.py file.pl
```
* new output should be smt like token_list.txt and tokens_without_space.txt

* run syntax analyser

  ```
  syntax_analyser.py
  ```
  * new output should be parse_tree.json

* now run 
```
Semantic_analyser.py
```



## Authors

Hooman honarvar 

student number :993613063
