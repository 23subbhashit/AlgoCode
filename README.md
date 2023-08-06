# AlgoCode
Algorithm Class Codes
## Assignment 1
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
