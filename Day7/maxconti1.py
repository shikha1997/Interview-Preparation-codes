def continuous1max(a):
    res=0
    c=0
    for i in range(len(a)):
        if(a[i]!=1):
            c=0
        else:
            c+=1
            res=max(res,c)
    return res

print(continuous1max([1,1,3,4,0,1,0,1,1,1,0,1,1,2,1,1,2,5,6,1,1,1,1]))