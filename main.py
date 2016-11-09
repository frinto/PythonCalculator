'''
	Script	 : calculator.py
	Author	 : < add member names here ... >
	Requires : < add python version number here ... >
	Purpose  : basic python calculator that does simple addition, substraction, division and multiplication.
'''

class CalculatorException ( Exception ) :
	pass

def add ( x , y ) :
	return ( x + y )

def substract ( x , y ) :
	return ( x - y )

def divide ( x , y ) :
	if ( x == 0 or y == 0 ) :
		raise CalculatorException ( 'Division by 0 is not allowed!' )
	return ( x / y)

def multiply ( x , y ) :
	return ( x * y )


''' Parse user input here and call appropriate function. '''
