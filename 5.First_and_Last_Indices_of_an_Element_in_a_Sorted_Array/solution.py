class Solution: 
  def getRange(self, arr, target):
    answer = [-1, -1]
    for i in range(len(arr)):
      if arr[i] == target:
        if answer[0] == -1:
          answer[0] = i
          answer[1] = i
        else:
          answer[1] = i

    return answer
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]