#defines a func f(x) x^3+8 with a return function 
#main func, use a call function for f(x) with x=9 and print 
#use if, then statement that executes if the result is larger than 27 and prints YAY!

def f(x): 
	return x**3 + 8 #return function

result = f(9) #x = 9 
print(result) #answer should be 737 

if result > 27:
	print("YAY!!") #IT WORKS! 
