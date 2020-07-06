def factorial(n):
     if(n==0 or n==1):
         return 1
     return n*factorial(n-1)
def totpath(m,n):
    c=m+n-2
    p=m-1
    q=n-1
    return factorial(c)//(factorial(p)*factorial(q))

def tpath(m,n):
    if(m==1 or n==1):
        return 1
    return tpath(m-1,n)+tpath(m,n-1)
print(totpath(3,4))
print(tpath(3,4))