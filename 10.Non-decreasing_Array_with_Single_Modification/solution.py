def check(lst):
  count = 0
  for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
      if count == 1:
        return False
      count += 1

  return True

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False