def sortNums(nums):
  aux = [0,0,0,0]

  for i in nums:
    aux[i] = aux[i] + 1
  
  i = 0
  j = 1
  while(aux[3] > 0):
    if aux[j] <= 0:
      j = j + 1

    nums[i] = j
    aux[j] = aux[j] - 1
    
    i = i + 1

  return nums
  
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]