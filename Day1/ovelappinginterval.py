#Merge Overlapping Subintervals
def interval(l):
    l=sorted(l,key=lambda x:x[0])
    stk=[]
    stk.append(l[0])
    for i in range(1,len(l)):
        if(l[i][0]>=stk[-1][0] and l[i][0]<=stk[-1][1]):
            if(l[i][1]>stk[-1][1]):
                stk[-1][1]=l[i][1]
        else:
            stk.append(l[i])

    print(stk)

if __name__=='__main__':
    arr = [[6, 8], [1, 5], [2, 4], [6, 7]]
    interval(arr)