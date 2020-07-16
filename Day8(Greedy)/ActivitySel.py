def actsel(arr):
    arr=sorted(arr,key = lambda x:x[1])
    i=0
    print(arr[0])
    for j in range(1,len(arr)):
        if(arr[j][0]>arr[i][1]):
            print(arr[j])
            i=j

if __name__ == '__main__':
    arr=[[1,2],[3,4],[0,6],[5,9],[5,7],[8,9]]
    actsel(arr)
