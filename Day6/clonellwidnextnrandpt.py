class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.rand=None

def clone(originalhead):
    curr=originalhead
    while(curr is not None):
        new=Node(curr.data)
        new.next=curr.next
        curr.next=new
        curr=curr.next.next

    curr=originalhead
    while(curr is not None):
        curr.next.random = curr.random.next
        curr=curr.next.next

    curr=originalhead
    dup_root=originalhead.next
    while(curr.next is not None):
        t=curr.next
        curr.next=curr.next.next
        curr=t

    return dup_root

def printll(head):
    curr=head
    while curr != None:
        print('Data =', curr.data, ', Random =', curr.random.data)
        curr = curr.next

if __name__ == '__main__':
    original_list = Node(1)
    original_list.next = Node(2)
    original_list.next.next = Node(3)
    original_list.next.next.next = Node(4)
    original_list.next.next.next.next = Node(5)

    '''Set the random pointers'''

    # 1's random points to 3
    original_list.random = original_list.next.next

    # 2's random points to 1
    original_list.next.random = original_list

    # 3's random points to 5
    original_list.next.next.random = original_list.next.next.next.next

    # 4's random points to 5
    original_list.next.next.next.random = original_list.next.next.next.next

    # 5's random points to 2
    original_list.next.next.next.next.random = original_list.next
    '''Print the original linked list'''
    print('Original list:')
    printll(original_list)

    '''Create a duplicate linked list'''
    cloned_list = clone(original_list)

    '''Print the duplicate linked list'''
    print('\nCloned list:')
    printll(cloned_list)
