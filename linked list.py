class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
obj=linkedlist()
obj.insert_at_end(5)
obj.insert_at_end(6)
obj.insert_at_end(2)
obj.display()