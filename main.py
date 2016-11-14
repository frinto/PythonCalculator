#!/usr/bin/python

'''
	Script	 : calculator.py
	Big thanks to vrori for writing this code we will need to remodify it and simplify it a bit so our classmates can understand
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
    '-add': addition,
    '-subtract': substract,
    '-divide': divide,
    '-multiply': multiply
}


def EntryPoint():
    if (len(sys.argv) != 4):
        raise CalculatorException('Usage: calculator.py <switch> <number> <number>')

    if (actions.get(sys.argv[1]) == None):
        raise CalculatorException('%s is not a recognized switch!' % sys.argv[1])

    leftHandSide = float(sys.argv[2])
    rightHandSide = float(sys.argv[3])

    print(actions[sys.argv[1]](leftHandSide, rightHandSide))


if (__name__ == '__main__'):
    EntryPoint()
