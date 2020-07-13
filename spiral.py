 
class Spiral: 
	def __init__(self, num):
		self.result = [[None for y in range(num)] for x in range(num)] 
		self.count = 1
		self.spiral(0, 0, num, "H") 

	def spiral(self, row, col, num, dir): 
		if(row <0 or col <0 
			or row>=num or col>=num 
			or self.result[row][col]!=None 
			or self.count>num*num): 
			return None

		if(self.result[row][col]==None):
			self.result[row][col] = self.count
			self.count = self.count + 1

		if(dir=="V"): 
			if(not self.spiral(row-1, col, num, "V")):
				if(not self.spiral(row, col+1, num, "H")): 
					if(not self.spiral(row+1, col, num, "V")): 
						self.spiral(row, col-1, num, "H")
		else: 
				if(not self.spiral(row, col+1, num, "H")): 
					if(not self.spiral(row+1, col, num, "V")): 
						if(not self.spiral(row, col-1, num, "H")): 
							self.spiral(row-1, col, num, "V")		
						

		return self.result





print Spiral(8).result
