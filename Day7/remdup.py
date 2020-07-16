def removeduplicate(a):
    if(len(a)==0 or len(a)==1):
        return a
    j=0
    a.sort()
    for i in range(len(a)-1):
        if(a[i]!=a[i+1]):
            a[j]=a[i]
            j+=1
            #print(j)
    a[j]=a[len(a)-1]

    return a[:j+1]

print(removeduplicate([1,11,2,4,5,7,8,9,9,7,4,7,7]))