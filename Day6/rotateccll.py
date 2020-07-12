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

    def rotate(self,k):
        if(k==0):
            return
        count=1
        current=self.head
        while(count< k and current is not None):
            current =current.next
            count+=1

        if(current is None):
            return
        knode=current
        while(current.next is not None):
            current=current.next
        current.next=self.head
        self.head=knode.next
        knode.next=None


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
    n.rotate(3)
    n.printll()
