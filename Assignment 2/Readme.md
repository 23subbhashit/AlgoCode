4>
```
def exists(arr,l,r,n,X):
    while r<n and l<n:
        if arr[r] - arr[l] == X:
            print(arr[r],arr[l])
            return True
        if arr[r] - arr[l]<X:
            r+=1
        else:
            l+=1
        
    return False
arr = [int(x) for x in input("Enter Array : ").split()]
arr.sort()
l = 0
r = 0
X = int(input("Enter X : "))
n = len(arr)
print(exists(arr,l,r,n,X))
```
5>
```
def exists(a,n):
    a.sort()
    for k in range(0,n):
        l = 0
        r = n-1
        while(l<r):
            if a[l]+a[r] == a[k]:
                print(a[l],a[r],a[k])
                return True
            if a[l]+a[r] < a[k]:
                l+=1
            else:
                r-=1
    return False
arr = [int(x) for x in input("Enter Array : ").split()]
arr.sort()
n = len(arr)
print(exists(arr,n))

```

6>
```
def exists(a,n):
    a.sort()
    for i in range(n):
        for l in range(n):
            j = 0
            k = n-1
            while(j<k):
                s = {i,j,k,l}
                
                if 2*a[j]+a[k] == a[i]+3*a[l] and len(s)==4:
                    print(a[i],a[j],a[k],a[l])
                    return True
                if 2*a[j]+a[k] < a[i]+3*a[l]:
                    j+=1
                else:
                    k-=1
    for i in range(n):
        for l in range(n):
            k = 0
            j = n-1
            while(k<j):
                s = {i,j,k,l}
                
                if a[k]+2*a[j] == a[i]+3*a[l] and len(s)==4:
                    print(a[i],a[j],a[k],a[l])
                    return True
                if a[k]+2*a[j] < a[i]+3*a[l]:
                    k+=1
                else:
                    j-=1
    return False
arr = [int(x) for x in input("Enter Array : ").split()]
arr.sort()
n = len(arr)
print(exists(arr,n))
```
7>
```
import random

def find_rank(arr, l, r, rank):
    k = partition(arr, l, r)
    if rank == r - k + 1:
        return k
    if rank < r - k + 1:
        return find_rank(arr, k + 1, r, rank)
    else:
        return find_rank(arr, l, k - 1, rank - (r - k + 1))

def partition(arr, p, q):
    rand_index = random.randint(p, q)%(q-p+1)+p
    arr[p], arr[rand_index] = arr[rand_index], arr[p]
    pivot = arr[p]
    i, j = p + 1, q

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    i -= 1
    arr[p], arr[i] = arr[i], arr[p]
    return i

n = int(input())
rank = int(input())
arr = list(map(int, input().split()))
result = find_rank(arr, 0, n - 1, rank)
print(arr[result])
```
