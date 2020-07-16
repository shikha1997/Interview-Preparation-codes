def greedymincoin(deno,V):
    deno=sorted(deno)
    n=len(deno)
    i=n-1
    c=0
    while(i>=0):
        while(V>=deno[i]):
            V-=deno[i]
            print(deno[i])
            c+=1
        i-=1
    print("count:",c)

if __name__ == '__main__':
    deno=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
    V=190
    greedymincoin(deno,V)
