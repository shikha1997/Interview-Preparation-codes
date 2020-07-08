class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LL:
    def __init__(self):

        self.head = None

    

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
        t=self.head
        while(t):
            print(t.data,end=" ")
            t=t.next
        print()

def mergell(a,b):
    if(a is None):
        return b
    if(b is None):
        return  a
    if(a.data<=b.data):
        temp=a
        temp.next= mergell(a.next,b)
    if(a.data>=b.data):
        temp=b
        temp.next = mergell(a,b.next)

    return temp

if __name__ == '__main__':

    # Create linked list :
    # 10->20->30->40->50
    list1 = LL()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = LL()
    list2.append(5)
    list2.append(15)
    list2.append(18)
    list2.append(35)
    list2.append(60)

    # Create linked list 3
    list3 =LL()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = mergell(list1.head, list2.head)
    print(" Merged Linked List is : ", end="")
    list3.printll()

