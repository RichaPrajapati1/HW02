#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def printpattern(char1, char2):
	return char1 * 4 + char2

def two_by_two(rownum):
	if rownum == 1:
		print '+' + printpattern('-','+') + printpattern('-','+')
		return
	elif rownum%5 == 1:
		print '+' + printpattern('-','+') + printpattern('-','+')
	else:
		print '|' + printpattern(' ','|') + printpattern(' ','|')
	two_by_two(rownum-1)


def four_by_four(rownum):
	if rownum == 1:
		print '+' + printpattern('-','+') + printpattern('-','+') + printpattern('-','+') + printpattern('-','+') 
		return
	elif rownum%5 == 1:
		print '+' + printpattern('-','+') + printpattern('-','+') + printpattern('-','+') + printpattern('-','+') 
	else:
		print '|' + printpattern(' ','|') + printpattern(' ','|') + printpattern(' ','|') + printpattern(' ','|') 
	four_by_four(rownum-1)


# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    a = 5*2+1 #Setting length for two by two square
    b = 5*4+1 #Setting length for two by two square
    two_by_two(a)
    four_by_four(b)
    print("Hello World!")
    



if __name__ == "__main__":
    main()