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

    def klast(self,k):
        temp=self.head
        count=0
        while(count<k and None!=temp):
            count+=1
            temp=temp.next
        if(count<k and None==temp):
            return
        t1=self.head
        while(temp!=None):
            temp=temp.next
            t1=t1.next

        return t1.data

if __name__ == '__main__':

    # Create linked list :
    # 10->20->30->40->50
    list1 = LL()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)
    print(list1.klast(5))