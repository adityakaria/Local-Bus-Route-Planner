class vertex:


	def __init__(self,key):
		self.id=key
		self.connectedTo={}

	def addNeighbour(self,nbr,weight=0):
		self.connectedTo[nbr]=weight

	def __str__(self):
		return str(self.id) + ' Connected to : ' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self):
		return self.connectedTo[nbr]

class graph:
	
	def __init__(self,size):
		self.vertList={}
		self.numVertices=0
		self.size=size
	
	def addVertex(self,key):
		self.numVertices+=1
		nv=vertex(key)
		self.vertList[key]=nv
		return nv

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t,cost):
		if f not in self.vertList:
			nv=self.addVertex(f)
		if t not in self.vertList:
			nv=self.addVertex(t)
		self.vertList[f].addNeighbour(self.vertList[t],cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())


			
		

