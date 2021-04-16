def isPalindromic(s):
	for i in range(len(s)):
		if s[i] != s[len(s) - i - 1]:
			return False
	
	return True

class Solution: 
	def longestPalindrome(self, s):
		val = ""
		size = 0
		for i in range(len(s)):
			for j in range(len(s[i:])):
				subs = s[i:(i+j+1)]
				if isPalindromic(subs):
					if len(subs) > size:
						size = len(subs)
						val = subs

		return val
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar