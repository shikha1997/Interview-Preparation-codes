def trailingzeros(n):
    i=5
    c=0
    while(int(n/i)>=1):
        c+=int(n/i)
        i=i*5
    print(c)

trailingzeros(10)

