class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def spl(root):
    if root is None:
        return
    q=[root]
    ltor=1
    ans=[]
    while(len(q)):
        temp=[]
        for i in range(len(q)):
            x=q.pop(0)
            temp.append(x.data)
            if(x.left):
                q.append(x.left)
            if(x.right):
                q.append(x.right)

        ans.append(temp[::ltor])
        ltor*=-1

    return ans


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(spl(root))

