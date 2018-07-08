//PYTHON
class stack(object):
	
	def __init__(self,stacksize,top):
		self.stacksize=stacksize
		self.top=top
		self.stackarray=[]
	def isFull(self):
		if self.top == self.stacksize-1:
			return True
		else:
			return False
	def isEmpty(self):
		if not self.stackarray:
			return True
		else:
			return False
	def push(self,num):
		if not stack.isFull(self):
			self.top=self.top+1
			self.stackarray.append(num)
		else:
			return;
			
	def pop_num(self):
		if not stack.isEmpty(self):
			value=self.top
			num=self.stackarray[value]
			self.stackarray.pop(value)
			self.top=self.top-1
			return num

Stack=stack(100,-1)
Stack.push(2)
Stack.push(3)
Stack.push(5)
print Stack.pop_num()
print Stack.pop_num()
