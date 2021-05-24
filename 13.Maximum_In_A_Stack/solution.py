class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class MaxStack:
  def __init__(self):
    self.top = None

  def push(self, val):
    new = Node(val)

    if self.top:
      aux = self.top
      self.top = new
      self.top.next = aux
    else: self.top = new

  def pop(self):
    self.top = self.top.next

  def max(self):
    if self.top == None:
      return None

    maxVal = self.top.val
    current = self.top
    while current:
      if current.val > maxVal:
        maxVal = current.val
      current = current.next
    
    return maxVal

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2