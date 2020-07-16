def jobsch(arr):
    n=len(arr)
    arr=sorted(arr,key = lambda x:x[2],reverse= True)
    slot =[0]*n
    result = [0]*n
    price=0
    print(arr)
    for i in range(n):
        for j in range(min(n,arr[i][1])-1,-1,-1):
            if(slot[j]==0):
                print(arr[i])
                price+=arr[i][2]
                slot[j]=1
                break

    # for i in range(n):
    #     if(slot[i]):
    #         print(arr[result[i]][0])

    print("Total profit:",price)

arr=[['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]
jobsch(arr)