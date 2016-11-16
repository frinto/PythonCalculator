#!/usr/bin/python

'''
	Script	 : calculator.py
	Big thanks to vrori for helping with this code as well as big thanks to all my teamates for helping out with it!!!
	Purpose  : basic python calculator that does simple addition, substraction, division and multiplication
'''

''' Imports '''
import sys

''' Classes '''


class CalculatorException(Exception):
    pass


''' Functions '''


def addition(x, y):
    return (x + y)


def substract(x, y):
    return (x - y)


def divide(x, y):
    if (x == 0 or y == 0):
        raise CalculatorException('Division by 0 is not allowed!')
    return (x / y)


def multiply(x, y):
    return (x * y)


''' Main Program '''
actions = {
    'add': addition,
    'subtract': substract,
    'divide': divide,
    'multiply': multiply
}


def EntryPoint():

    #if length of arguments does not equal 4 then write error requiring correct number of input
    if (len(sys.argv) != 4):
        raise CalculatorException('Usage: calculator.py <switch> <leftHandSideNumber> <rightHandSideNumber>')

    #if the action is not recognized as a valid switch then print error
    #sys.argv[1] represents if its division, multiplication, addition, or subtraction
    if (actions.get(sys.argv[1]) == None):
        raise CalculatorException('%s is not a recognized switch!' % sys.argv[1])

    #convert the value into a float
    #example python calculator.py add 5 20
    #sys.argv[0] will represent FILE NAME "calculator.py"
    #sys.argv[1] will represent the switch which is either dividing, multiplying, adding, or subtracting
    #sys.argv[2] will represent the value 5
    #sys.argv[3] represents 20 will represent the value 20

    leftHandSide = float(sys.argv[2])
    rightHandSide = float(sys.argv[3])

    #sys.argv[0] represents the name of the file for example printing sys.argv[0] will show this file name is calculator.py
    print("python file name = " + sys.argv[0])

    #outputting our result
    #the action that will be performed on leftHandSide and rightHandSide
    print("result of " + " " +sys.argv[2] + " " + sys.argv[1] + " " + sys.argv[3] + " = ")
    print(actions[sys.argv[1]](leftHandSide, rightHandSide))


if (__name__ == '__main__'):
    EntryPoint()
