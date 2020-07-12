#Reverse a LinkedList in groups.

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LL:
    def __init__(self):
        self.head=None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def printll(self):
        t = self.head
        while (t):
            print(t.data, end=" ")
            t = t.next
        print()

    def reverse(self,head, k):
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)

        self.head=prev
        return prev

if __name__ == '__main__':
    n=LL()
    n.append(1)
    n.append(2)
    n.append(3)
    n.append(4)
    n.append(5)
    n.append(6)
    n.append(7)
    n.append(8)
    n.append(9)
    n.append(10)
    n.printll()
    n.reverse(n.head,3)
    n.printll()





