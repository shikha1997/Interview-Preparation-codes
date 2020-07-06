def colno(s):
    c=1
    ans=0
    for i in range(len(s)-1,-1,-1):
        ans+=(ord(s[i])-64)*c
        c*=26

    print(ans)


colno('AbC'.upper())