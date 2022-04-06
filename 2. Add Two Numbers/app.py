from typing import Optional
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.intToNode( self.nodeToInt(l1) + self.nodeToInt(l2) )
    
    def generateListNode(self, nums) -> ListNode:
        temp = None
        for x in reversed(nums):
            temp = ListNode(x,temp)
        return temp
    
    def nodeDive(self, ln:ListNode):
        if ln != None:
            print (ln.val)
        if ln.next != None:
            self.nodeDive(ln.next)
        return 0
    
    def nodeToString(self, ln:ListNode):
        if ln.next == None:
            return str(ln.val)
        else:
            return self.nodeToString(ln.next) + str(ln.val)

    def nodeToInt(self, ln:ListNode):
        return int(self.nodeToString(ln))
    
    def intToNode(self, num:int):
        print ( "--------------------------------------------------------------" )
        print ( int( num ) )
        if num > 9:
            print ( num % 10 )
            print ( int ( num / 10 ) )
            return ListNode( int(num) % 10, self.intToNode(  int( num / 10 ) ) )
        else:
            return ListNode( int(num) % 10, None )

## test cases

sol = Solution()

lnl1 = sol.generateListNode( [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] )
lnl2 = sol.generateListNode( [5,6,4] )

print( sol.nodeToInt ( lnl1 ) )

print( sol.nodeToInt ( lnl2 ) )

print ( sol.nodeToInt ( lnl1 ) + sol.nodeToInt ( lnl2 ) )  

print ( sol.nodeToString( sol.intToNode( sol.nodeToInt ( lnl1 ) + sol.nodeToInt ( lnl2 ) ) ) )

#print ( sol.nodeToString( sol.addTwoNumbers(lnl1, lnl2) ) )