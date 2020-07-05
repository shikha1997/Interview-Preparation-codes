#spiral printing of matrix
def spiralprint(a):
    r = len(a)
    c = len(a[0])
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    l=[]
    while (left <= right and top <= bottom):
        for i in range(left,right+1):
            l.append(a[top][i])
        top+=1

        for i in range(top,bottom+1):
            l.append(a[i][right])
        right-=1

        for i in range(right,left-1,-1):
            l.append(a[bottom][i])
        bottom-=1

        for i in range(bottom,top-1,-1):
            l.append(a[i][left])
        left+=1

    print(l)

if __name__ == '__main__':
    a=[[1,4,2],[3,0,5],[7,8,9]]
    spiralprint(a)

