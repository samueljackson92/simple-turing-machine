Simple Turing Machine
=====================

Simple implementation of a Turing machine in less than 100 lines of python
Reads "Tape" file (using parameter -i) with symbols on it and a "Program" file (using parameter -p) consisting 
of a set of instructions. Each instruction is a comma seperated list of the state number, direction of 
reading/writing (or halt), symbol to match, symbol to replace and the next state to go to.

An example instruction might be the following:
```
1,R,#,1,2
```
Which is  read as: state 1, looking RIGHT along the tape, find the next occurence of '#', replace
that symbole with '1' and then execute instruction 2.

Programs can be commented using double slash notation such as the following:
```
//Simple program to add one to a number
//in unary

1,R,#,1,2
2,L,#,#,3
3,H
```
Note that instruction 3 tells the program to HALT execution and finish.

The tape file must contain a sequence of input characters, and it must begin and end with the '#' symbol. An example
input tape might be:
```
#111#11#
```
