#!/usr/bin/python

'''
	Script	 : calculator.py
	Authors  : Huy, Dan and Dirge
	Purpose  : basic python calculator that does simple addition, substraction, division and multiplication.
'''

''' Imports '''
import sys

''' Classes '''
class CalculatorException ( Exception ) :
	pass

''' Functions '''
def addition ( x , y ) :
	return ( x + y )

def substract ( x , y ) :
	return ( x - y )

def divide ( x, y ) :
	if ( x == 0 or y == 0 ) :
		raise CalculatorException ( 'Division by 0 is not allowed!' )
	return ( x / y)

def multiply ( x, y ) :
	return ( x * y )


''' Main Program '''
actions = {
	'-a' : addition,
	'-s' : substract,
	'-d' : divide,
	'-m' : multiply
}

def EntryPoint ( ) :
	if ( len ( sys.argv ) != 4 ) :
		raise CalculatorException ( 'Usage: calculator.py <switch> <number> <number>' )

	if ( actions.get ( sys.argv [ 1 ] ) == None ) :
		raise CalculatorException ( '%s is not a recognized switch!' % sys.argv [ 1 ] )

	lhs = float ( sys.argv [ 2 ] )
	rhs = float ( sys.argv [ 3 ] )

	print (
		actions [ sys.argv [ 1 ] ] ( lhs , rhs )
	)

if ( __name__ == '__main__' ) :
	EntryPoint ( )
