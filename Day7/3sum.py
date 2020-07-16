def sum3(a,k):
    result=[]
    a.sort()

    for i in range(len(a)):
        if(i>0 and a[i]==a[i-1]):
            continue
        start=i+1
        end=len(a)-1

        while(start<end):
            if(a[start]+a[end]+a[i]<k):
                start+=1
            elif(a[start]+a[end]+a[i]>k):
                end-=1
            else:
                result.append([a[i],a[start],a[end]])
                start+=1
                end-=1
    return result

print(sum3([-1,0,1,2,-1,-4],3))

