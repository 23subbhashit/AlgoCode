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
