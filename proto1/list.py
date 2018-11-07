class node:
	def __init__(self,element,next):
		self.element=element
		self.next=next

class list:
	def __init__(self):
		self.head=None
		self.size=0

	def insertHead(self,element):
		n=node(element,next)
		n.next=self.head
		self.head=n
		self.size+=1

	def remove(self):
		if self.size==0:
			print(" List Empty ")
		else:
			a=self.head.element
			self.head=self.head.next
			self.size-=1
			return a

l=list()
l.insertHead(1)
l.insertHead(2)

print(l.remove())

		
