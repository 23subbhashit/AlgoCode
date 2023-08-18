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
    return False
arr = [int(x) for x in input("Enter Array : ").split()]
arr.sort()
n = len(arr)
print(exists(arr,n))
```
