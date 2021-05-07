def singleNumber(nums):
  single = 0
  for i in nums:
    single += i * 2
    for j in nums:
      if i == j: 
        single -= j

    if single != 0:
      return single

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1