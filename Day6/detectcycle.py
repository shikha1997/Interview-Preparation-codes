###LINKED LIST CYCLE LEETCODE
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head is None or head.next is None):
            return False
        slow = head
        fast = head

        while (slow and fast):
            fast = fast.next
            if (fast == slow):
                return True
            if (fast is None):
                return False
            fast = fast.next
            if (fast == slow):
                return True
            slow = slow.next

###LINKED LIST CYCLE II LEETCODE
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head
        slow, fast = head, head
        hascycle = False
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                hascycle = True
                break

        if not hascycle: return None
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow