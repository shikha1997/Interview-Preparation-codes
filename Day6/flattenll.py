class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.down=None


def merge(a,b):
    if(a is None):
        return b
    if(b is None):
        return a
    if(a.data<b.data):
        temp=a
        temp.down=merge(a.down,b)
    else:
        temp=b
        temp.down=merge(b,a.down)

    temp.right=None
    return temp

def flatten(head):
    if(head is None or head.right is None):
        return head
    return merge(head,flatten(head.right))