def powerxy(x,y):
    ans=1
    if(y==0):
        return 1
    temp=powerxy(x,int(y/2))
    if(int(y%2)==0):
        ans=temp*temp
    else:
        if(y>0):
            ans=temp*temp*x
        else:
            ans=(temp*temp)/x
    return ans

print(powerxy(2,-4))