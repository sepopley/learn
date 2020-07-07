import copy 

class StairCount: 
	def __init__(self, n):
		#print "hello world", n
		self.count = self.countStairs(n)
		self.minCount, self.minPath = self.minCountStairs(n,list())
		self.minCountWithThree, self.minPathWithThree = self.minCountStairsWithThree(n,list())

		
		#self.countWithCache = self.countStairsWithCache(n)

		self.countCache = {}
		self.countCache[0] = 0
		self.countCache[1] = 1
		self.countCache[2] = 1

		self.pathCache = {}
		self.pathCache[0] = []
		self.pathCache[1] = [1]
		self.pathCache[2] = [2]
		self.minCountWithCache, self.minPathWithCache = self.minCountStairsWithCache(n,list())

	# Count all possible ways to climb stairs 
	def countStairs(self,n): 
		#edge cases 
		if(n<0):
			return 0
		if(n<=2): 
			return n  

		#recursive calls 
		return self.countStairs(n-1) + self.countStairs(n-2)

	# Count stairs, but cache every computation to save resources for future runs 
	def countStairsWithCache(self, n): 
		#edge cases 
		if(n in self.countCache):
			return self.countCache[n]
		
		#recursive calls 
		self.countCache[n-1] = self.countStairs(n-1)
		self.countCache[n-2] = self.countStairs(n-2)
		return self.countCache[n-1] + self.countCache[n-2]


	# Return the most efficient way to climb a set of stairs 
	def minCountStairs(self,n, l): 
		#edge cases 
		if(n<0):
			return (0,l)
		if(n<=2): 
			result = copy.deepcopy(l)
			result.append(n)
			return (1, result)  

		#recursive calls 
		l1 = copy.deepcopy(l)
		l1.append(1)
		l2 = copy.deepcopy(l)
		l2.append(2)
		result1 = self.minCountStairs(n-1, l1) 
		result2 = self.minCountStairs(n-2, l2)

		if(result1>result2): 
			return (result2[0]+1, result2[1])
		else: 
			return (result1[0]+1, result1[1])


	#Return the shortest way to climb a set of stairs using a caching list
	def minCountStairsWithCache(self,n, l): 
		#already computed  
		if(n in self.countCache):
			temp = copy.deepcopy(self.pathCache[n])
			return self.countCache[n], temp

		#recursive calls 		
		self.countCache[n-1], self.pathCache[n-1] = self.minCountStairsWithCache(n-1, l) 
		self.countCache[n-2], self.pathCache[n-2] = self.minCountStairsWithCache(n-2, l)
		
		#return min path + count 
		if(self.countCache[n-1]>self.countCache[n-2]): 
			return 1 + self.countCache[n-2], copy.deepcopy(l) + [2] + self.pathCache[n-2]
		else: 
			return 1 + self.countCache[n-1], copy.deepcopy(l) + [1] +  self.pathCache[n-1]

	#Return the shortest way to clumb a set of stairs where you can take 1, 2, or 3 steps 
	def minCountStairsWithThree(self,n, l): 
		#edge cases 
		if(n<0):
			return (0,l)
		if(n<=3): 
			result = copy.deepcopy(l)
			result.append(n)
			return (1, result)  

		#recursive calls 
		l1 = copy.deepcopy(l)
		l1.append(1)
		l2 = copy.deepcopy(l)
		l2.append(2)
		l3 = copy.deepcopy(l)
		l3.append(3)
		result1 = self.minCountStairsWithThree(n-1, l1) 
		result2 = self.minCountStairsWithThree(n-2, l2)
		result3 = self.minCountStairsWithThree(n-3, l3)

		if(result1<=result2 and result1<=result3): 
			return (result1[0]+1, copy.deepcopy(l) + [2] + result1[1])
		if(result2<=result1 and result2<=result3): 
			return (result2[0]+1, result2[1])
		else: 
			return (result3[0]+1, result3[1])

s = StairCount(9)
print s.minCount, s.minPath
print s.minCountWithCache, s.minPathWithCache