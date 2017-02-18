class Linkedlist:
    def __init__(self,value):
        self.value=value
        self.next=None
#n=input("Enter number of elements:")
a=[5,3,7,2,6,9,4]
prev=None
for i in a:
    name='a'+str(i)
    name=Linkedlist(i)
    #print name.value
    if prev!=None:
        prev.next=name
        prev=prev.next
    else:
        prev=name
        head=prev
k=input("Enter K::: ")
fastrunner=head
slowrunner=head
while k:
    fastrunner=fastrunner.next
    #print k
    k=k-1
while fastrunner.next!=None:
    #print head.value
    fastrunner=fastrunner.next
    slowrunner=slowrunner.next
if slowrunner !=None:
    print "Kth last element=",slowrunner.value








