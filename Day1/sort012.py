#Sort an array of 0’s 1’s 2’s without using extra space or sorting algo
def sort012(arr):

    j=len(arr)-1
    c=0
    i=0
    l = len(arr) - 1
    while(i<len(arr) and j>=0):
        if(arr[i]==0):
            arr[i],arr[c]=arr[c],arr[i]
            c+=1
        i+=1
        if (arr[j] == 2):
            arr[j], arr[l] = arr[l], arr[j]
            l -= 1

        j-=1

    print(arr)

if __name__=='__main__':
    arr = [int(x) for x in input().split()]
    sort012(arr)
