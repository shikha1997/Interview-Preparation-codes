class Node:
    def __init__(self, data):
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
        t = self.head
        while (t):
            print(t.data, end=" ")
            t = t.next
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
        return prev
def addtwoll(l1,l2,ans):
    carry=0
    while(l1!=None and l2!=None):
        no=(l1.data+l2.data+carry)%10
        carry=(l1.data+l2.data+carry)//10
        ans.append(no)
        l1=l1.next
        l2=l2.next

    while(l1):
        no = (l1.data+ carry) % 10
        carry = (l1.data+ carry) // 10
        ans.append(no)
        l1=l1.next
    while(l2):
        no = (l2.data + carry) % 10
        carry = (l2.data + carry) // 10
        ans.append(no)
        l2 = l2.next
    if(carry>0):
        ans.append(no)







if __name__ == '__main__':

    # Create linked list :
    list1 = LL()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.printll()
    list1.reversell()
    #list1.printll()

    # Create linked list 2 :
    list2 = LL()
    list2.append(5)
    list2.append(9)
    list2.append(8)
    list2.append(5)
    list2.append(0)
    list2.printll()
    list2.reversell()
    #list2.printll()

    # Create linked list 3
    list3 =LL()
    addtwoll(list1.head,list2.head,list3)
    list3.reversell()
    print("The required ll is:")
    list3.printll()







