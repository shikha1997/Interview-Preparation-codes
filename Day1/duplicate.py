#Find the duplicate in an array of N integers.
def dup(arr):
    if(len(arr)==1):
        return arr[0]
    arr.sort()
    for i in range(1,len(arr)):
        if(arr[i]==arr[i-1]):
            return arr[i]

    return -1

if __name__=='__main__':
    arr=[int(x) for x in input().split()]
    print(dup(arr))
