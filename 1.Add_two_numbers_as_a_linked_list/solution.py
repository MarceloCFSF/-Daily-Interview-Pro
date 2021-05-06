# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

def addList(l1, l2, c=0):
  val = l1.val + l2.val + c
  return int(val%10), int(val/10)

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    val, c = addList(l1, l2)
    l = ListNode(val)
    val, c = addList(l1.next, l2.next, c)
    l.next = ListNode(val)
    val, c = addList(l1.next.next, l2.next.next, c)
    l.next.next = ListNode(val)

    return l

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val,end=" "),
  result = result.next
# 7 0 8