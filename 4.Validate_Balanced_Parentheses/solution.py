def addBracket(char, opened, closed, x):
	if char == opened:
		x = x + 1
	elif char == closed:
		x = x - 1
	
	return x

class Solution:
	def isValid(self, s):
		braces = brackets = parentheses = 0
		for i in s:
			parentheses = addBracket(i, '(', ')', parentheses)
			brackets = addBracket(i, '[', ']', brackets)
			braces = addBracket(i, '{', '}', braces)

		if braces == 0 and brackets == 0 and parentheses == 0:
			return True
		else: return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))