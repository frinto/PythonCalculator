#!/usr/bin/python

'''
	Script	 : calculator.py
	Author	 : < add member names here ... >
	Requires : < add python version number here ... >
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

	# Sanity check. Let us make sure the input are numerical values ( 0 - 9 )
	if ( sys.argv [ 2 ] . isdigit ( ) and sys.argv [ 3 ] . isdigit ( ) ) :
		lhs = int ( sys.argv [ 2 ] )
		rhs = int ( sys.argv [ 3 ] )

		print (
			actions [ sys.argv [ 1 ] ] ( lhs , rhs )
		)
	else :
		raise CalculatorException (
			'Either lhs or rhs contains invalid input... ( %s | %s )' % ( sys.argv [ 2 ] , sys.argv [ 3 ] )
		)

if ( __name__ == '__main__' ) :
	EntryPoint ( )
