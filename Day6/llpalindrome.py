
#Check if palindrome is reverse or not
def isPalindrome(head: ListNode) -> bool:
    if (head is None or head.next is None):
        return True

    slow = head
    fast = head
    c = 0

    while (fast.next is not None and fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
        c += 1
    
    curr = slow.next
    while (curr is not None):
        temp = curr.next
        curr.next = slow
        slow = curr
        curr = temp
    for i in range(c):
        if (slow.val != fast.val):
            return False
        slow = slow.next
        fast = fast.next

    return True

