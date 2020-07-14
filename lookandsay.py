import copy



"""
Implement a function that outputs the Look and Say sequence:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""
class LookAndSay:
	def __init__(self, input, l): 
		self.say(input, l)

	def say(self, input, l):
		if(not input): 
			return input


		for i in range(l): 
			numberCount = 1
			result = ""
			
			if(len(input)==1):
				result = "1" + copy.deepcopy(input)

			else: 
				for l in range(0,len(input)): 
					if(l+1<len(input) and input[l]==input[l+1]): 
						numberCount =  numberCount + 1
					else: 
						result = result + str(numberCount) + input[l]
						numberCount = 1
			
			print result 
			input = result 

t = LookAndSay("1", 10)



