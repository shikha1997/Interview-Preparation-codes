#Merge two sorted Arrays without extra space
def marr(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    for i in range(n-1,-1,-1):
        last=arr1[m-1]
        j=m-2
        while(j>=0 and arr1[j]>arr2[i]):
            arr1[j+1]=arr1[j]
            j-=1
        if(j!=m-2 or last>arr2[i]):
            arr1[j+1]=arr2[i]
            arr2[i]=last

    return arr1,arr2

#Merge two sorted Arrays without extra space
if __name__=='__main__':
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    print(marr(arr1,arr2))