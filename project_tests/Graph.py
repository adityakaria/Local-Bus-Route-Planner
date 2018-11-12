import math
from MinHeap import MinHeap
c2=0
class Vertex:
	def __init__(self,name):
		self.name=name
		self.neighbours={}
		self.ds=math.inf   				#initially set distance from source to infinity
		self.parent=None
		self.MHListIndex=None
		self.bus={'EXPRESS':False,'SERVICE':False,'CITY1':False, 'CITY2':False, 'CITY3': False, 'CITY4': False, 'CITY5': False, 'CITY6': False}
		self.busFrom = None
		self.ts=math.inf
		self.cs=math.inf

	def Addneighbour(self, name, weight=0):
		self.neighbours[name]=weight

	def __str__(self):
		return str(self.name) + ' neighbours are ' + str([x for x in self.neighbours.keys()])


	def NeighbourWeight(self, nbr):
		if nbr in self.neighbours:
			return self.neighbours[nbr]

	def DistFromSource(self):
		return self.ds

	def SetBus(self,bustype):
		self.bus[bustype]=True

	def TimeFromSource(self):
		return self.ts


	def __lt__(self,other):
		global c2
		if c2==0:
			if self.ds<other.ds:
				return True
			elif self.ds>other.ds:
				return False
		elif c2==1:
			if self.ts<other.ts:
				return True
			elif self.ts>other.ts:
				return False
		elif c2==2:
			if self.cs<other.cs:
				return True
			elif self.cs>other.cs:
				return False


class BUS:
	def __init__(self,name):
		self.name=name
		if name=='EXPRESS':
			self.speed=75
			self.rate=1.5
		elif name=='CITY1' or name=='CITY2' or name=='CITY3' or name=='CITY4' or name=='CITY5' or name=='CITY6' :
			self.speed=30
			self.rate=0.56
		elif name=='SERVICE':
			self.speed=40
			self.rate=1


class Graph:
	def __init__(self):
		self.nv=0     #no. of vertices
		self.Vertices={}     #vertices dictionary

	# def __iter__(self):
	# 	return iter(self.Vertices.values())
	
	def AddVertex(self,name):
		self.nv=self.nv+1
		NewVertex=Vertex(name)
		self.Vertices[name]=NewVertex
		return NewVertex

	def AddEdge(self,Head,Tail,weight):    #assuming undirected for now
		if Head not in self.Vertices:
			self.AddVertex(Head)
		if Tail not in self.Vertices:
			self.AddVertex(Tail)
		self.Vertices[Head].Addneighbour(Tail,weight)
		self.Vertices[Tail].Addneighbour(Head,weight)  #remove 

	def GetVertex(self,name):
		if name in self.Vertices:
			return self.Vertices[name]


	def UpdateBusInfo(self,bustype,l):
		for i in range(0,len(l)):
			self.GetVertex(l[i]).SetBus(bustype)

	def GetVertices(self):
		return self.Vertices.keys()


def DijkstrasSP(G,s,d):
	R=[]
	s.ds=0
	MH=MinHeap()
	for u in G.Vertices:
		MH.Insert(G.Vertices[u])    #because u is a string
	MH.BuildHeap()
	while not MH.isEmpty():
		U=MH.ExtractMin()
		R.append(U.name)
		for v in U.neighbours:
			V=G.GetVertex(v)
			if V==s:
				continue
			if  V.DistFromSource()>=U.DistFromSource()+U.NeighbourWeight(v):
				V.ds=U.ds+U.NeighbourWeight(v)
				MH.UpdatePriority(V)
				V.parent=U.name
	print(R)


def DijkstrasST(G,s,d):
	s.ts=0
	s.ds=0
	MH=MinHeap()
	for u in G.Vertices:
		MH.Insert(G.Vertices[u])	#because u is a string
		# print(G.Vertices[u].name)
		# print(G.Vertices[u].bus.items())
	MH.BuildHeap()
	print(MH)
	while not MH.isEmpty():
		U=MH.ExtractMin()
		print("=================================================")
		print(U.name)
		for v in U.neighbours:
			V=G.GetVertex(v)
			print(V.name, "------------------------")
			# print(U.bus, V.bus)
			if V==s:
				continue
			if U.bus['EXPRESS'] and V.bus['EXPRESS']:
				print("	--e--")
				bus=BUS('EXPRESS')
			elif U.bus['SERVICE'] and V.bus['SERVICE']:
				print("	--s--")
				bus=BUS('SERVICE')
			elif U.bus['CITY1'] and V.bus['CITY1']:
				print("	--c1--")
				bus=BUS('CITY1')
			elif U.bus['CITY2'] and V.bus['CITY2']:
				print("	--c2--")
				bus=BUS('CITY2')
			elif U.bus['CITY3'] and V.bus['CITY3']:
				print("	--c3--")
				bus=BUS('CITY3')
			elif U.bus['CITY4'] and V.bus['CITY4']:
				print("	--c4--")
				bus=BUS('CITY4')
			elif U.bus['CITY5'] and V.bus['CITY5']:
				print("	--c5--")
				bus=BUS('CITY5')
			elif U.bus['CITY6'] and V.bus['CITY6']:
				print("	--c6--")
				bus=BUS('CITY6')
			else:
				continue
			if (V.DistFromSource()/bus.speed)>=(U.DistFromSource()/bus.speed)+(U.NeighbourWeight(v)/bus.speed):
				V.ts=U.ts+(U.NeighbourWeight(v)/bus.speed)
				V.ds=U.ds+U.NeighbourWeight(v)
				MH.UpdatePriority(V)
				V.parent=U.name
				V.busFrom = bus.name
				print("updated: ", U.name, "->" ,V.name)
			bus=None      #because might have to change the bus
		# print(U.name, ">--" + bus.name + "-->", V.name)


def DijkstrasCP(G,s,d):
	s.ts=0
	s.ds=0
	s.cs=0
	MH=MinHeap()
	for u in G.Vertices:
		MH.Insert(G.Vertices[u])		#because u is a string
	MH.BuildHeap()
	while not MH.isEmpty():
		U=MH.ExtractMin()
		for v in U.neighbours:
			V=G.GetVertex(v)
			if V==s:
				continue
			if U.bus['CITY1'] and V.bus['CITY1']:
				bus=BUS('CITY1')
			elif U.bus['CITY2'] and V.bus['CITY2']:
				bus=BUS('CITY2')
			elif U.bus['CITY3'] and V.bus['CITY3']:
				bus=BUS('CITY3')
			elif U.bus['CITY4'] and V.bus['CITY4']:
				bus=BUS('CITY4')
			elif U.bus['CITY5'] and V.bus['CITY5']:
				bus=BUS('CITY5')
			elif U.bus['CITY6'] and V.bus['CITY6']:
				bus=BUS('CITY6')
			elif U.bus['SERVICE'] and V.bus['SERVICE']:
				bus=BUS('SERVICE')
			elif U.bus['EXPRESS'] and V.bus['EXPRESS']:
				bus=BUS('EXPRESS')
			if bus==None:
				continue
			if (V.DistFromSource()*bus.rate)>=(U.DistFromSource()*bus.rate)+(U.NeighbourWeight(v)*bus.rate):
				V.cs=U.cs+(U.NeighbourWeight(v)*bus.rate)
				V.ds=U.ds+U.NeighbourWeight(v)
				MH.UpdatePriority(V)
				# print(U.name, ">--" +  bus.name + "-->", V.name)
				V.parent=U.name
				U.busFrom = bus.name
			bus=None      #because we might have to change the bus


def PrintPath(G,d):             #to print the path from sorce to destination-using recursion
	if G.GetVertex(d).parent!=None:
		PrintPath(G,G.GetVertex(d).parent)
	print(G.GetVertex(d).name,' ---' + G.GetVertex(d).busFrom + '----->',end=' ')





def main():
	G=Graph()
	print("Updating contents of map")
	# print("enter values")
	# l=input()
	# while l!='':
	# 	l=l.split()
	# 	G.AddEdge(l[0],l[1],int(l[2]))
	# 	l=input()

	ew=open("EdgeWeight.txt", "r")
	while True:
		f=ew.readline()
		l=f.rstrip('\n').split()
		if l == []:
			break
		# l=l.split()
		G.AddEdge(l[0],l[1],float(l[2]))
		# print(l)


	fh=open("BUS.txt","r")
	f=fh.readline()
	l=f.rstrip('\n').split()
	bt=l.pop(0)		#bt: bustype
	G.UpdateBusInfo(bt,l)
	for f in fh:
		l=f.rstrip('\n').split()
		bt=l.pop(0)
		G.UpdateBusInfo(bt,l)	
	print("Map formed succesfully")
	print("enter the source")
	s=input()
	print("enter the destination")
	d=input()
	print("Enter your choice")
	print("How do you want to go?")
	print("1.own Transport-Car,Motorcycle")
	print("2.public Transport-Bus")
	c1=int(input())
	while c1!=1 and c1!=2:
		print("Ooops, Its seems you have entered an invalid choice.Please enter a valid choice")
		c1=int(input())
	if c1==1:
		DijkstrasSP(G,G.GetVertex(s),G.GetVertex(d))
		print("your path from souce to destination is")
		PrintPath(G,d)
		print(G.GetVertex(d).ds)
	elif c1==2:
		print("Choose your priority")
		print("1.Travel in Shortest time path")
		print("2.Travel in Cheapest Price path")
		print("3.Travel in the Best Path")
		global c2
		c2=int(input())
		while c2!=1 and c2!=2 and c2!=3:
			print("Ooops, Its seems you have entered an invalid choice.Please enter a valid choice")
			c2=int(input())
		if c2==1:
			DijkstrasST(G,G.GetVertex(s),G.GetVertex(d))
			print("your path from souce to destination is")
			PrintPath(G,d)
			print("\b\b\b\b\b\b\b\b\b\n")
			print("Time taken: Approx.", math.floor((G.GetVertex(d).ts) * 60), "minutes")
		elif c2==2:
			DijkstrasCP(G,G.GetVertex(s),G.GetVertex(d))
			print("your path from souce to destination is")
			PrintPath(G,d)
			print(G.GetVertex(d).cs)




if __name__=='__main__':
	main()