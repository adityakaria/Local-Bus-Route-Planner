# ew=open("EdgeWeight.txt", "r")
# while True:
# 	f=ew.readline()
# 	l=f.rstrip('\n').split()
# 	if l == []:
# 		break
# 	# l=l.split()
# 	G.AddEdge(l[0],l[1],int(l[2]))
# 	# print(l)


fh=open("BUS.txt","r")
f=fh.readline()
l=f.rstrip('\n').split()
bt=l.pop(0) 			#bt: bustype
# G.UpdateBusInfo(bt,l)
for f in fh:
	l=f.rstrip('\n').split()
	bt=l.pop(0)
	# G.UpdateBusInfo(bt,l)	
	print(bt, l)