class node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None
class Linkedlist:
    def __init__(self, val):
        self.head = node(val)
        self.temp = self.head
    def insert(self,val):
        self.temp.next = node(val)
        self.temp = self.temp.next
    def display(self):
        self.temp2 = self.head
        while(self.temp2):
            print(self.temp2.val,end="")
            self.temp2 = self.temp2.next
        print()
    def reverse(self):
        prev = None
        curr = self.head
        while(curr):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        self.head = prev
    def insert_at_pos(self, pos, val):
        mid = node(val)
        if pos==1:
            mid.next = self.head
            self.head = mid
        else:
            i = 1
            left = self.head
            while(i!=pos-1):
                left = left.next
                i+=1
            if left.next == None:
                left.next = mid
            else:
                mid.next = left.next
                left.next = mid 
          
        
listt = Linkedlist(1)
listt.insert(2)
listt.insert(4)
listt.insert(5)
listt.display()
listt.reverse()
listt.display()
listt.reverse()
listt.display()
listt.insert_at_pos(5,3)
listt.display()
listt.reverse()
listt.display()