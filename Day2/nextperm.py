#Next possible permutation in lexo order
def nperm(a):
    if(len(a)==1):
        return a
    for i in range(len(a)-1,0,-1):
        if(a[i]>a[i-1]):
            t_idx=i+a[i:].index(min(filter(lambda x:x>a[i-1],a[i:])))
            a[t_idx],a[i-1]=a[i-1],a[t_idx]
            a[i:]=sorted(a[i:])
            return
    a.reverse()


if __name__ == '__main__':
    a=[1,3,2]
    nperm(a)
    print(a)
