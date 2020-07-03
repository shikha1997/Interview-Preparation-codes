#Find the max sum of continuous sub array: KadaneAlgo
def kadane(arr):
    s=-100000000
    c=0
    for i in range(len(arr)):
        c=c+arr[i]
        if(s<c):
            s=c
        if(c<=0):
            c=0
    return s

if __name__=='__main__':
    arr = [int(x) for x in input().split()]
    print(kadane(arr))

