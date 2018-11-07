from graph import graph

print(" Enter the Number of Vertices: ")
a=int(input())
g = graph(a)
for i in range(a):
	g.addVertex(i)

print(" Enter the Number of Edges: ")
n=int(input())
for i in range(n):
	print(" Enter Edge ",i)
	c=int(input())
	d=int(input())
	print(" Enter the Edge Weight: ")
	e=int(input())
	g.addEdge(c,d,e)

print(" Adjacency List is: ")
for v in g:
	for w in v.getConnections():
		print("(%s , %s )"%(v.getId(), w.getId()))


