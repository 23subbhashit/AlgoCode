# AlgoCode
Algorithm Class Codes
## Assignment 1
1>
```
def merge(A,low,mid,high):
    l = A[low:mid+1]
    r = A[mid+1:high+1]
    i=j=0
    k=low
    swaps=0
    while(i<len(l) and j<len(r)):
        if l[i]<r[j]:
            A[k]=l[i]
            i+=1
        else:
            swaps+=mid-i+1
            A[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        A[k]=l[i]
        k+=1
        i+=1
    while j<len(r):
        A[k]=r[j]
        k+=1
        j+=1
    return swaps
def CIP(A,l,r):
    c=0
    if l<r:
        mid = (l+r)//2
        c+=CIP(A,l,mid)
        c+=CIP(A,mid+1,r)
        c+=merge(A,l,mid,r)
    return c
        
s = input("Enter String : ")
n = len(s)
A = [-1]*n
c = 0
for i in range(n):
    if s[i]=='1': c+=1
    else: c-=1
    A[i]=c
A.insert(0,0)
temp = CIP(A,0,n)
print((n*(n+1)//2)-temp)
```

2>
```
def findLongestSub(bin1):
	n = len(bin1)
	# To store sum.
	s= 0
	# To store first occurrence of each
	# sum value.
	prevSum = {i:0 for i in range(n)}
	# To store maximum length.
	maxlen = 0
	# To store current substring length.
	for i in range(n):
		# Add 1 if current character is 1
		# else subtract 1.
		if (bin1[i] == '1'):
			s += 1
		else:
			s -= 1
		# If sum is positive, then maximum
		# length substring is bin1[0..i]
		if (s > 0):
			maxlen = i + 1
		# If sum is negative, then maximum
		# length substring is bin1[j+1..i], where
		# sum of substring bin1[0..j] is sum-1.
		elif (s <= 0):
			if ((s - 1) in prevSum):
				currlen = i - prevSum[s - 1]
				maxlen = max(maxlen, currlen)
		# Make entry for this sum value in hash
		# table if this value is not present.
		if ((s) not in prevSum):
			prevSum[s] = i
	return maxlen
# Driver code
bin1 = "1010"
print(findLongestSub(bin1))

```
3>
```
s = input("Enter Binary String : ")
c=len(s)
m = 0
t = [-1]*(2*len(s))
for i in range(len(s)):
    if s[i]=='1': c+=1
    else :
        c-=1
    if t[c]<0 and c==len(s): t[c]=-1
    else: t[c]=i
    m = max(m,i-t[c])
print(m)
    
```

4> 
```
def f(s):
    c=0
    for i in s:
        if i=='1':
            c+=1
    return c
s = input("Enter Binary String")
print("Output : ",f(s))
```
5>
```
class ll:
    def __init__(self,data,nxt=None):
        self.data=data
        self.next=nxt

def f(head):
    cur = head

    prev = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def printll(head):
    cur = head
    while cur:
        print(cur.data)
        cur=cur.next
        
n = int(input("Enter No. of node :"))
temp = dummy = None
for i in range(n):
    a = int(input())
    node = ll(a)
    if temp is None:
        temp = node
        dummy = node
    else:
        temp.next = node
        temp = temp.next
print("Linked List : ")
printll(dummy)
rev = f(dummy)
print("Reversed : ")
printll(rev)      

```
6>
```
class ll:
    def __init__(self,data,nxt=None):
        self.data=data
        self.next=nxt

def f(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False

def printll(head):
    cur = head
    while cur:
        print(cur.data)
        cur=cur.next
        
n = int(input("Enter No. of node :"))
temp = dummy = None
cn = None
for i in range(n):
    a = int(input())
    node = ll(a)
    if temp is None:
        temp = node
        dummy = node
    else:
        if i==2:
            cn = node
        temp.next = node
        if i==n-1:
            temp.next = cn
        else:
            temp.next = node
        temp = temp.next
print("Linked List : ")
ans = f(dummy)
print(ans)      
```
7>
```
class ll:
    def __init__(self,data,nxt=None):
        self.data=data
        self.next=nxt

def f(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        print(slow.data,fast.data)
        if slow==fast:
            start = head
            while start.next!=slow.next:
                start=start.next
                slow=slow.next
            slow.next= None
            break
    print("Linked List : ")
    printll(head)
    

def printll(head):
    cur = head
    while cur:
        print(cur.data)
        cur=cur.next
        
n = int(input("Enter No. of node :"))
temp = dummy = None
cn = None
for i in range(n):
    a = int(input())
    node = ll(a)
    if temp is None:
        temp = node
        dummy = node
    else:
        if i==2:
            cn = node 
        
        temp.next = node
        temp = temp.next
#create dummy cycle    
temp.next = cn
f(dummy)     
```

8>
```
n = int(input())
arr = [int(x) for x in input().split()]
s= []
j=0
for i in range(1,n+1):
    s.append(i)
    while s and arr[j]==s[-1]:
        s.pop()
        j+=1
if len(s)==0:
    print("Stack Sequence!!")
else:
    print("Nahi h BC")


```
9>
```
from collections import deque

def windowmax(arr,n,res,k):
    window = deque()
    for i in range(n):
        while window and window[0]<=i-k:
            window.popleft()
        while window and arr[i]>arr[window[-1]]:
            window.pop()
        window.append(i)
        if i>=k-1:
            res.append(arr[window[0]])
    return res

n = int(input("Enter the number of elements"))
arr = [int(x) for x in input("Enter array").split()]
k = int(input("Enter the Window Size"))
res = []
ans = windowmax(arr,n,res,k)
print(ans)
```
10>
```
n = int(input("Enter length of Array : "))
arr = [int(x) for x in input("Enter Array : ").split()]
ans = [-1]*n
ans[n-1]=n
s = [n-1]
for i in  range(n-2,-1,-1):
    while s and arr[s[-1]]>=arr[i]:
        s.pop()
    if s:
        ans[i]=s[-1]
    else:
        ans[i]=n
    s.append(i)
print(ans)
```
11>
```
n = int(input("Enter length of Array : "))
arr = [int(x) for x in input("Enter Array : ").split()]
ans = [-1]*n
ans[0]=-1
s = [0]
for i in  range(1,n):
    while s and arr[s[-1]]<=arr[i]:
        s.pop()
    if s:
        ans[i]=s[-1]
    else:
        ans[i]=-1
    s.append(i)
print(ans)
```
12>
```
def bs(arr,s,l,h,key):
    ans = -1
    while (l<=h):
        mid = (l+h)>>1
        if arr[s[mid]]<key:
                ans=mid
                h = mid-1
        else:
            l = mid+1
    return ans

n = int(input("Enter Size Of Array : "))
arr = [int(x) for x in input("Enter Array : ").split()] # 100 50 20 25 40
b = [-1]*n
s=[]
i = 0
top = -1 # intially no ele
while i<n:
    if not s:
        b[i]=-1
    else:
        k=bs(arr,s,0,top,arr[i])
        if k == -1:
            b[i] = -1
        else:
            b[i]=s[k]
    if not s or arr[i]<arr[s[-1]] :
        s.append(i)
        top+=1
    i+=1
    #print("i : ",i," b : ",b ," s : ",s)
print(b)
```
13>
```
def bs(arr,s,l,h,key):
    ans = n
    while (l<=h):
        mid = (l+h)>>1
        if arr[s[mid]]>key:
            ans = mid
            h = mid-1
            
            #print("ans : ",ans," key : ",key," stack : ",s)
        else:
            l = mid+1
    return ans

n = int(input("Enter Size Of Array : "))
arr = [int(x) for x in input("Enter Array : ").split()] # 50 20 100 40 10
b = [-1]*n
s=[]
i = 0
top = -1 # intially no ele
for i in range(n-1,-1,-1):
    if not s:
        b[i]= n
    else:
        k=bs(arr,s,0,top,arr[i])
        if k == n:
            b[i] = n
        else:
            b[i]=s[k]
    if not s or arr[i]>arr[s[-1]] :
        s.append(i)
        top+=1
    #print(" s : ",s)
    
print(b)
```
14>
```
n = int(input("Enter No. of ele : "))
A = [int(x) for x in input("Enter Array : ").split()]
m = float('-inf')
i =0
for j in range(1,n):
    m = max(m,A[j]-A[i])
    if A[j]<A[i]:
        i=j
print("Max : ",m)
```
15>
```
n = int(input("Enter No. of ele : "))
k = int(input("Enter Gap days : "))
A = [int(x) for x in input("Enter Array : ").split()]
m = float('-inf')
i =0
for j in range(k,n):
    m = max(m,A[j]-A[i])
    i+=1
print("Max : ",m)
```

16>
```
n = int(input("Enter No. of ele : "))
k = int(input("Enter Gap days : "))
A = [int(x) for x in input("Enter Array : ").split()]
m = float('-inf')
i =0
for j in range(k,n):
    m = max(m,A[j]-A[i])
    if A[j-k+1]<A[i]:
        i = j-k+1
print("Max : ",m)

```
18>
```
n = int(input("Enter length of array : "))
arr = [int(x) for x in input("Enter array : ").split()] 
ps = [arr[0]]
for i in range(1,n):
    ps.append(ps[-1]+arr[i])

i = 0
m = float('-inf')
for j in range(1,n):
    m = max(m,ps[j]-ps[i])
    if ps[j]<ps[i]:
        i=j
print("Max Subarray Sum : ",m)
    
```

19>
```
arr = [int(x) for x in input("Enter Array elements : ").split()]
k = int(input("Enter Subarray Length : "))
max_sum =0
curr = 0

for i in range(k):
    max_sum += arr[i]
    curr += arr[i]

for i in range(k,len(arr)):
    curr += arr[i]-arr[i-k]
    if curr > max_sum:
        max_sum = curr
print(max_sum)

```
20>
```
n = int(input("Enter length of array : "))
arr = [int(x) for x in input("Enter array : ").split()]
l= int(input("Enter number of days : "))
ps = [arr[0]]
for i in range(1,n):
    ps.append(ps[-1]+arr[i])

i = 0
m = float('-inf')
for j in range(l,n):
    m = max(m,ps[j]-ps[i])
    if ps[j-l+1]<ps[i]:
        i=j-l+1
print("Max Subarray Sum : ",m)   

```
22>
```
n = int(input("Enter n value : ")) #1000
m = int(input("Enter Modulo Value : "))#10
arr=[-1]*n
arr[0]=0
arr[1]=1
for p in range(2,6*m+2):
    arr[p]=(arr[p-1]+arr[p-2])%m
    if arr[p-1]==0 and arr[p]==1:
        break
p-=1
print(arr[n%p])
```
23>
```
def matrix_multiply_mod(A, B, m):
    result = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % m
    return result

def matrix_power_mod(M, exponent, m):
    if exponent == 1:
        return M
    if exponent % 2 == 0:
        half_power = matrix_power_mod(M, exponent // 2, m)
        return matrix_multiply_mod(half_power, half_power, m)
    else:
        half_power = matrix_power_mod(M, (exponent - 1) // 2, m)
        return matrix_multiply_mod(matrix_multiply_mod(half_power, half_power, m), M, m)

def compute_fn(n, m):
    if n == 0:
        return 0
    if n == 1:
        return 1

    transformation_matrix = [
        [1, 1],
        [1, 0]
    ]

    powered_matrix = matrix_power_mod(transformation_matrix, n - 1, m)
    initial_vector = [1, 0]  # Adjusted initial vector
    result_vector = [0, 0]
    for i in range(2):
        for j in range(2):
            result_vector[i] = (result_vector[i] + powered_matrix[i][j] * initial_vector[j]) % m

    return (result_vector[0]) % m  # No need to add 1 here as it was already considered in the transformation

def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    result = compute_fn(n, m)
    print("F({}) % {} = {}".format(n, m, result))

if __name__ == "__main__":
    main()


```
25>
```
# Python3 program to find value of f(n)
# where f(n) is defined as
# F(n) = F(n-1) + F(n-2) + F(n-3), n >= 3
# Base Cases :
# F(0) = 0, F(1) = 1, F(2) = 1

# A utility function to multiply two
# matrices a[][] and b[][]. Multiplication
# result is stored back in b[][]
def multiply(a, b,m):
	
	# Creating an auxiliary matrix
	# to store elements of the
	# multiplication matrix
	mul = [[0 for x in range(3)]
			for y in range(3)];
	for i in range(3):
		for j in range(3):
			mul[i][j] = 0;
			for k in range(3):
				mul[i][j] += a[i][k] * b[k][j];
			mul[i][j]=mul[i][j]%m

	# storing the multiplication
	# result in a[][]
	for i in range(3):
		for j in range(3):
			a[i][j] = mul[i][j] # Updating our matrix
	return a;

# Function to compute F raise
# to power n-2.
def power(F, n,m):

	M = [[2,0,-3], [1, 0, 0], [0, 1, 0]]

	# Multiply it with initial values i.e
	# with F(0) = 0, F(1) = 1, F(2) = 1
	if (n == 1):
		return F[0][0] + F[0][1];

	power(F, int(n / 2),m);

	F = multiply(F, F,m);

	if (n % 2 != 0):
		F = multiply(F, M,m);

	# Multiply it with initial values i.e
	# with F(0) = 0, F(1) = 1, F(2) = 1
	return F[0][0] + F[0][1] ;

# Return n'th term of a series defined
# using below recurrence relation.
# f(n) is defined as
# f(n) = f(n-1) + f(n-2) + f(n-3), n>=3
# Base Cases :
# f(0) = 0, f(1) = 1, f(2) = 1
def findNthTerm(n,m):
	F = [[2,0,-3], [1, 0, 0], [0, 1, 0]]

	return power(F, n - 2,m);

# Driver code
n = 5
m = 10
print("F(5) is",
	findNthTerm(n,m));
```
