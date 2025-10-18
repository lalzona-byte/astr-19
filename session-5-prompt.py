#write a table of sin(x) v x, x being between 0 and 2pi with a thousand entries 
#follow basic python structure 

import numpy as np 

def main():
	x_entries = np.linspace(0,2*np.pi,1000)
	y_entries = np.sin(x_entries)


	for x, y in zip(x_entries, y_entries):
		print(f"{x:f} {y:f}")

if __name__=="__main__":
	main()
