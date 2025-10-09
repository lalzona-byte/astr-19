#declare a class describing your fav animal 
# physical parameters: length of arms and legs(float)
# number of eyes (int)
#does it have a tail (bool)
#is it furry (bool)
#write an initialization func that sets the values of this data when the 
#class is created 
#write a member func of the class to print and describe the data 

import sys 

class Snake: 
	def __init__(self, length_arms, length_legs, num_eyes, has_fur, has_tail):
		self.length_arms = length_arms
		self.length_legs = length_legs
		self.num_eyes = num_eyes
		self.has_fur = has_fur
		self.has_tail = has_tail

	def describe(self): 
		print("My favorite animals are snakes. Its characteristics are:")
		print(f"arm length: {self.length_arms}, no arms!")
		print(f"leg length: {self.length_legs}, no legs either!")
		print(f"number of eyes: {self.num_eyes}")
		print(f"tail? {'yes!'if self.has_tail else 'nope'}")
		print(f"fur? {'yes!' if self.has_fur else 'nope'}")

snakes = Snake(length_arms=0, length_legs=0, num_eyes=2, has_tail=True, has_fur=False)

snakes.describe()