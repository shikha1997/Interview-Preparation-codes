def minplatform(s,f):
    s.sort()
    f.sort()
    i=1
    j=0
    ans=1
    pltneed=1
    n=len(s)
    while(i<n and j<n):
        if(s[i]>f[j]):
            pltneed-=1
            j+=1
        else:
            pltneed+=1
            i+=1
        if(pltneed>ans):
            ans=pltneed

    return ans

if __name__ == '__main__':
    arrival=[900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print(minplatform(arrival,departure))
