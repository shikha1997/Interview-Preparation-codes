class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LL:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node

    def printll(self):
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next
        print()

    def midelm(self):
        fast=self.head
        slow= self.head
        while(fast.next!=None):
            # fast=fast.next.next
            # slow=slow.next
            if(fast.next is not None and fast.next.next is None):
                break
            fast = fast.next.next
            slow = slow.next

        print(slow.data)

if __name__ == '__main__':
    n=LL()
    n.push(1)
    n.push(2)
    n.push(3)
    n.push(4)

    n.printll()
    n.midelm()
