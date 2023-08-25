1>
![WhatsApp Image 2023-08-20 at 12 28 05](https://github.com/23subbhashit/AlgoCode/assets/43717493/f98b8776-9ed1-46d0-9892-72be43e20199)
![WhatsApp Image 2023-08-20 at 12 42 18](https://github.com/23subbhashit/AlgoCode/assets/43717493/aba64f90-2157-4c08-a1aa-ee496e3671cc)
<br/>
2>
![WhatsApp Image 2023-08-20 at 13 27 56](https://github.com/23subbhashit/AlgoCode/assets/43717493/92fb0aa0-4512-4c69-8608-2b1c54faab03)

![WhatsApp Image 2023-08-20 at 13 34 27](https://github.com/23subbhashit/AlgoCode/assets/43717493/396ab2ea-5da5-4948-b81d-5ed0f8bf5917)

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
9>
```
def Rank(a,n,b,m,k):
    if m+n <k or k<1: return -1
    elif n == 0 : return b[m-k]
    elif m == 0 : return a[n-k]
    elif k == 1:
        if a[n-1]>b[m-1]:
            return a[n-1]
        else:
            return b[m-1]
    else:
        i = n-k//2
        if i<0: i = 0
        j = m-k//2
        if j<0: j = 0
        print("i : ",i,"j : ",j)
        if a[i]>b[j]:
            print("A : ",a[:i+1],"B : ",b[:m+1],"k : ",k-n+i)
            return Rank(a,i,b,m,k-n+i)
        else:
            print("A : ",a[:n+1],"B : ",b[:j+1],"k : ",k-m+j)
            return Rank(a,n,b,j,k-m+j)
n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
k = int(input())
print(Rank(a,n,b,m,k))

```
10>
```
# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)
```
