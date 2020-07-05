def pascal(n):
    if(n==0):
        return [1]
    if(n==1):
        return [1,1]
    rs=pascal(n-1)
    res=[1]
    for i in range(len(rs)-1):
        res.append(rs[i]+rs[i+1])

    return res+[1]

def Ptriangle(n):
    res=[[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        for j in range(i+1):
            if(j==0 or j==i):
                res[i][j]=1
                print(res[i][j],end=" ")
            else:
                res[i][j]=res[i-1][j-1]+res[i-1][j]
                print(res[i][j],end=" ")
        print()

    return "Done!"



print(Ptriangle(5))