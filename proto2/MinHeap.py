class MinHeap:

	def __init__(self):
		self.HeapList=[]
		self.num=0

	def __str__(self):
		return "\n----\n" + str(self.HeapList) + "\n----\n"

	def Insert(self,vertex):
		vertex.MHListIndex=self.num
		self.HeapList.append(vertex)
		self.num=self.num+1

	def Heapify(self,source,n):
		min=source
		while source<n:
			l=2*source+1
			r=2*source+2
			if l<n and self.HeapList[l]<self.HeapList[min]:
				min=l
			if r<n and self.HeapList[r]<self.HeapList[min]:
				min=r
			if min!=source:
				temp=self.HeapList[source]
				self.HeapList[source]=self.HeapList[min]
				self.HeapList[min]=temp
				self.HeapList[min].MHListIndex=min
				self.HeapList[source].MHListIndex=source
			else:
				break
			source=min

	def BuildHeap(self):
		for i in range(len(self.HeapList)//2-1,-1,-1):
			self.Heapify(i,len(self.HeapList))

	def ExtractMin(self):
		if len(self.HeapList)>1:
			min=self.HeapList[0]
			self.HeapList[0]=self.HeapList.pop()   #throws list index of out range
			self.HeapList[0].MHListIndex=0
			self.Heapify(0,len(self.HeapList))
		else:
			min=self.HeapList.pop()
		return min

	def Minimum(self):
		return self.HeapList[0]

	def UpdatePriority(self,V):
		i=V.MHListIndex
		p=(i+1)//2-1
		while p>=0:
			if self.HeapList[i]<self.HeapList[p]:
				temp=self.HeapList[p]
				self.HeapList[p]=self.HeapList[i]
				self.HeapList[i]=temp
				self.HeapList[p].MHListIndex=p
				self.HeapList[i].MHListIndex=i
				i=p
				p=(p+1)//2-1
			else:
				break

	def isEmpty(self):
		if len(self.HeapList)>0:
			return False
		return True

	def HeapSort(self): #have to change
		n=len(self.HeapList)
		for i in range(n-1, 0, -1):
			temp=self.HeapList[i]
			self.HeapList[i]=self.HeapList[0]
			self.HeapList[0]=temp
			self.Heapify(0,i)



def main():
	H=MH()
	print("enter values")
	l=input()
	l=list(map(int,l.split()))
	print(l)
	for i in range(0,len(l)):
		H.Insert(l[i])
	print(H.a)
	H.BuildHeap()
	print(H.a)