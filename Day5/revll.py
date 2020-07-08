class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printll(self):
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next
        print()

    def reversell(self):
        prev=None
        curr = self.head
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self. head = prev

if __name__ == '__main__':
    n=LL()
    n.push(1)
    n.push(2)
    n.push(3)
    n.push(4)
    n.push(5)
    n.printll()
    n.reversell()
    n.printll()

