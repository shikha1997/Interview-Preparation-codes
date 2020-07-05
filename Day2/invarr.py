#Count Inversions in an array using merge sort
def merge(a,left,right):

    inv=0
    if(left<right):
        mid=left+(right-left)//2
        inv+=merge(a,left,mid)
        inv+=merge(a,mid+1,right)
        inv+=tmerge(a,left,mid,right)

    return inv

def tmerge(a,left,mid,right):
    i=left
    j=mid+1
    inv=0
    while(i<=mid and j<=right):
        if(a[i]<=a[j]):
            #te.append(a[i])
            i+=1
        else:
            #te.append(a[i])
            inv+=(mid-i)+1
            j += 1


    while(i<=mid):
        #te.append(a[i])
        i+=1


    while(j<=right):
        #te.append(a[j])
        j+=1

    return inv


print(merge([1, 20, 6, 4, 5] ,0,4))




