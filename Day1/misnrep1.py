#Given an unsorted array of size n. Array elements are in the range from 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.
def misnrep(arr):
    ans1=0
    ans2=0
    for i in range(len(arr)):
        if(arr[abs(arr[i])-1]>0):
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        else:
            ans1=abs(arr[i])
            break
    for i in range(len(arr)):
        if(arr[i]>0):
            ans2=i+1
            break

    return ans2,ans1








if __name__=='__main__':
    arr = [int(x) for x in input().split()]
    x,y=misnrep(arr)
    print("The missing elm is: "+str(x)+" and repeated elm is: "+str(y))