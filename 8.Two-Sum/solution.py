def two_sum(list, k):
  aux = {}
  for i in list:
    aux.update({k-i: 1})
    if aux.get(i): return True

  return False

print(two_sum([4,7, 1, -3,2], 5))
# True