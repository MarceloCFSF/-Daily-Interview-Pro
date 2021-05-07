class Solution:
  def lengthOfLongestSubstring(self, s):
    characters = {}
    maxLength = 0
    length = 0
    
    for i in range(len(s)):
      for j in s[i:]:
        if characters.get(j): break
        characters.update({j: 1})
        length = length + 1

      if length > maxLength:
        maxLength = length

      characters = {}
      length = 0

    return maxLength

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10