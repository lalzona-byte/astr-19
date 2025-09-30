#This program will write 
#Hello World 


#this function tells the computer to print Hello World 
def PrintHelloWorld(): #defines the start of the function
	print("Hello World!") #then it indents to show to belongs to the 
	#function above 
	#it goes back - doesnt indent - when the function ends 
def main():
	PrintHelloWorld() #this defines the MAIN fucntion of our program
	#idiom 
# this is a failsafe to let you write complicated programs 
if __name__=="__main__": #if we are executing the script, the first thing 
	main() #it executes is the main function, first thing that you start w 
	# make a template outta this and always put it at the bottom 