#Set Matrix Zero-GFG
def mtx(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]==0):
                a[i][j]='z'

    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]=='z'):
                for k in range(len(a)):
                    if(a[k][j]!='z'):

                        a[k][j]=0
                for l in range(len(a[0])):
                    if(a[i][l]!='z'):
                        a[i][l]=0
                a[i][j]='z'

    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]=='z'):
                a[i][j]=0

    print(a)

if __name__ == '__main__':
    a=[[1,1,1],[1,0,1],[1,1,1]]
    mtx(a)