from typing import Optional
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(None)

    def generateListNode(self, nums) -> ListNode:
        temp = None
        for x in reversed(nums):
            temp = ListNode(x,temp)
        return temp

    def nodeToArray(self, ln:ListNode) -> list:
        return list(reversed(self.nodeToString(ln)))

    def nodeToString(self, ln:ListNode) -> str:
        if ln.next == None:
            return str(ln.val)
        else:
            return self.nodeToString(ln.next) + str(ln.val)
    

## test cases

sol = Solution()

lnl1 = sol.generateListNode( [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2] )

print ( sol.nodeToArray(lnl1) )