#Buy and Sell to get max profit
def buynsell(a):
    n=len(a)
    i=0
    l=[]
    while(i<n-1):
        while(i<n-1and a[i+1]<=a[i]):
            i+=1
        if(i==n-1):
            break

        buy=i
        while(i<n-1 and a[i+1]>a[i]):
            i+=1

        sell=i

        #l.append([a[buy],a[sell]])
        print("Buy at Day"+str(buy)+" and sell at Day"+str(sell))

    #for getting max profit
    # ans=sorted(l,key=lambda x:x[1]-x[0],reverse=True)
    # print(ans[0])


if __name__ == '__main__':
    a=[100,180,260,310,40,535,695]
    buynsell(a)