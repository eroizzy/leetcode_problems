from typing import Optional
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):# -> Optional[ListNode]:
        return self.addTwoListNodes(l1,l2,0)

    def addTwoListNodes(self, l1, l2, r):
        if l1 != None and l2 != None:
            s = l1.val + l2.val + r
            ts = s % 10
            tr = (int(s / 10))
            return ListNode(ts, self.addTwoListNodes(l1.next, l2.next, tr))
        elif l1 !=None and l2 == None:
            s = l1.val + r
            ts = s % 10
            tr = (int(s / 10))
            return ListNode(ts, self.addTwoListNodes(l1.next, l2, tr))
        elif l1 ==None and l2 != None:
            s = l2.val + r
            ts = s % 10
            tr = (int(s / 10))
            return ListNode(ts, self.addTwoListNodes(l1, l2.next, tr))
        else:
            if r != 0:
                return ListNode(r,None);
            return None

    def nodeDive(self, ln:ListNode):
            if ln != None:
                print (ln.val)
            if ln.next != None:
                self.nodeDive(ln.next)
            return None

    def generateListNode(self, nums) -> ListNode:
        temp = None
        for x in reversed(nums):
            temp = ListNode(x,temp)
        return temp


## test cases

sol = Solution()

lnl1 = sol.generateListNode( [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2] )
lnl2 = sol.generateListNode( [6,7,8] )
lnl3 = sol.generateListNode( [4,5,6] )

sol.nodeDive(sol.addTwoNumbers(lnl2, lnl3) )