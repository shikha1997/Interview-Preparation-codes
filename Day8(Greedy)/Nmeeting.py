#Activity sel same problem
def Nmeet(arr):
    for i,x in enumerate(arr):
        x.append(i)

    arr=sorted(arr,key = lambda x:x[1])
    i=0
    c=1
    pos=[arr[0][2]]
    print(arr[0])
    for j in range(1,len(arr)):
        if(arr[j][0]>arr[i][1]):
            print(arr[j])
            i=j
            c+=1
            pos.append(arr[j][2])


    return c,pos

if __name__ == '__main__':
    arr=[[1,2],[3,4],[0,6],[5,9],[8,9],[5,7]]
    c,pos=Nmeet(arr)
    print("count: ",c,"position:",pos)