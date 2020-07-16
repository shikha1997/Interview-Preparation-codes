#Fractional Knapsack
def frknap(arr,W):
    for i,x in enumerate(arr):
        x.append(i)
    arr=sorted(arr,key= lambda x:x[0]/x[1],reverse=True)
    c=0
    price=0
    ans=[0]*len(arr)
    for i in range(len(arr)):
        if(W>=0):
            if(W>=arr[i][1]):
                W -= arr[i][1]
                price += arr[i][0]
                ans[arr[i][2]]=1
                c+=1
            else:
                frac = W/arr[i][1]
                W -= frac*arr[i][1]
                price+=frac*arr[i][0]
                ans[arr[i][2]]=frac
                c+=1
                break


    return c,price,ans

if __name__ == '__main__':
    arr=[[60,10],[120,30],[100,20]]
    W=50
    c,tot_price,ans = frknap(arr,W)
    print("Total no. of items: ",c)
    print("Total price :",tot_price)
    print("Items:",ans)




