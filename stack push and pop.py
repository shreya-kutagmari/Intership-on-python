class stack:
   def __init__(self):
      self.stack=[]
      self.size=3
      self.top=-1
   def push(self,item):
       if self.top<self.size-1:
         self.stack.append(item)
         self.top +=1
       else:
         print("overflow")
   def display(self):
       for i in range (len(self.stack)-1,-1,-1):
          print(self.stack[i])
   def pop(self):
      if self.isEmpty():
         print("underflow")
      else:
         self.stack.pop()
         self.top -=1
   def isEmpty(self):
      if self.top==-1:
         return True
      else:return False
obj=stack()
obj.push("apple")
obj.push("mango")
obj.push("grapes")
obj.pop()
obj.display()