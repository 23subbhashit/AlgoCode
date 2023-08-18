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
