#Rotate matrix in anticlockwise direction

def rotmtx(a):
    r=len(a)
    c=len(a[0])
    top=0
    bottom=r-1
    left=0
    right=c-1
    prev=a[top+1][right]
    while(left<=right and top<=bottom):
        #rotating top row towards left
        for i in range(right,left-1,-1):
            curr=a[top][i]
            a[top][i]=prev
            prev=curr
        top+=1

        for i in range(top,bottom+1):

            curr = a[i][left]
            a[i][left] = prev
            prev = curr
        left+=1

        for i in range(left,right+1):
            curr = a[bottom][i]
            a[bottom][i] = prev
            prev = curr
        bottom-=1

        for i in range(bottom,top-1,-1):
            curr = a[i][right]
            a[i][right] = prev
            prev = curr
        right-=1

    print(a)

if __name__ == '__main__':
    a=[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]
        ]
# Test cas
    rotmtx(a)


