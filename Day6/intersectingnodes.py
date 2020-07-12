#Find intersecting point in a linked list-Leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ###Solution1
        # nodes = set()
        # while headA:
        #     nodes.add(headA)
        #     headA = headA.next
        # while headB:
        #     if headB in nodes:
        #         return headB
        #     headB = headB.next
        # return None
        ###Solution 2
        c1 = 0
        c2 = 0
        if (headA == None or headB == None):
            return
        temp1 = headA
        while (temp1):
            temp1 = temp1.next
            c1 += 1
        temp1 = headB
        while (temp1):
            temp1 = temp1.next
            c2 += 1
        n = abs(c1 - c2)

        t = headA
        temp1 = headB
        if (c1 > c2):
            while (n > 0):
                t = t.next
                n -= 1
        else:
            while (n > 0):
                temp1 = temp1.next
                n -= 1

        while (t != temp1):
            if (t or temp1):
                t = t.next
                temp1 = temp1.next
            else:
                return
        return t



