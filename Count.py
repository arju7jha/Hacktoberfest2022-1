# Python3 program for the above approach

import math

# Function to find the roots of quadratic equation
def findRoots(K):
	a = 1
	b = -3
	c = -2 * K
	
	# Finding discriminant
	d = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(d))
	
	# Root are distinct
	if d > 0:
		
		# roots of equation
		x1 = (-b + sqrt_val)/(2 * a)
		x2 = (-b - sqrt_val)/(2 * a)
		
		if int(x1) == x1 and x1 > 0:
			return (int(x1))
		elif int(x2) == x2 and x2 > 0:
			return (int(x2))
		else:
			return -1
	
	# Roots are equal
	elif d == 0:
	# roots of equation
		x1 = (-b / (2 * a))
		if int(x1) == x1 and x1 > 0:
			return (int(x1))
		else:
			return -1
			
	# Root are imaginary	
	else:
		return -1

# Driver code
if __name__ == '__main__':
	
	# K is number of diagonals
	K = 9
	
	# Function call
	print(findRoots(K))
