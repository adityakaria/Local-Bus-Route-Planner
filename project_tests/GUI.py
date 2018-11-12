from UpdatedGraph import Vertex, Graph, BUS, DijkstrasCP, DijkstrasSP, DijkstrasST, DijkstrasST
from MinHeap import MinHeap
from tkinter import *
c2=1
c1 = 2
i=6
master = Tk()

def PrintPath(G,s,d):
    global master, i
    if G.GetVertex(d).parent!=None:
        PrintPath(G,s,G.GetVertex(d).parent)
    if d==s:
        x = Label(master, text=(str(G.GetVertex(d).name) + " "))
        x.grid(row=i)
        print(G.GetVertex(d).name,end=' ')
    else:
        x = Label(master, text=(' ---' + str(G.GetVertex(d).busFrom) +'----->' + str(G.GetVertex(d).name) + " "))
        x.grid(row=i)
        print(' ---',G.GetVertex(d).busFrom,'----->',G.GetVertex(d).name,end=' ')

def main():
    global c2, c1, i
    global master
    S=StringVar(master)
    D=StringVar(master)
    master.title("ROUTE PLANNER")
    def taps():
        print(str(S.get()))
    def tapd():
        print(str(D.get()))
    w = Label(master, text='WELCOME TO YOUR PERSONAL ROUTE PLANNER', justify=CENTER)
    w.grid(row=0)
    Label(master, text='SOURCE').grid(row=1, column=0)
    Label(master, text='DESTINATION').grid(row=2, column=0)
    e1 = Entry(master, textvariable = S, command=taps())
    e2 = Entry(master, textvariable = D, command=tapd())
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)


    
    # var1 = IntVar()
    # Checkbutton(master, text='SHORTEST TIME', variable=var1).grid(row=3, sticky=W)
    # var2 = IntVar()
    # Checkbutton(master, text='CHEAPEST FARE', variable=var2).grid(row=4, sticky=W)
     
    selected = IntVar()
    Label(master, text='Least Time path').grid(row=3, column=0)
    Label(master, text='Cheapest Cost Path').grid(row=4, column=0)
    Label(master, text='Best Path').grid(row=5, column=0)
    rad1 = Radiobutton(master, text='ST', fg='black', value=1, variable=selected)
    rad2 = Radiobutton(master, fg='black', text='CP', value=2, variable=selected)
    rad3 = Radiobutton(master, fg='black', text='LT', value=3, variable=selected)
    def clicked():
      print(selected.get())
      c2=int(selected.get())
    btn = Button(master, text="Search", bg="black", activebackground='black', activeforeground="white", fg='white', command=clicked)
    rad1.grid(row=3, column=1, columnspan=2)
    rad2.grid(row=4, column=1)
    rad3.grid(row=5, column=1)
    btn.grid(column=1, row=6)

    # c1.pack()
    # c2.pack()
    
    G=Graph()
    print("Updating contents of map")
    # print("enter values")
	# l=input()
	# while l!='':
	# 	l=l.split()
	# 	G.AddEdge(l[0],l[1],int(l[2]))
	# 	l=input()
    master.update_idletasks()
    master.update()
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
    # s=input()
    #s='NITK'
    # s = str(e1.get())
    master.update_idletasks()
    master.update()
    source=S.get()
    s=source
    print(s)
    print("enter the destination")
    # d=input()
    #d='MANNAGUDDA
    # d = str(e2.get())
    dest=D.get()
    d=dest
    print(d)
    print("Enter your choice")
    print("How do you want to go?")
    print("1.own Transport-Car,Motorcycle")
    print("2.public Transport-Bus")
    # c1=int(input())
    c1=1
    print(c1)
    print(c2)
    while c1!=1 and c1!=2:
        print("Ooops, Its seems you have entered an invalid choice.Please enter a valid choice")
        c1=int(input())
    if c1==1:
        DijkstrasSP(G,G.GetVertex(s),G.GetVertex(d))
        print("your path from souce to destination is")
        PrintPath(G,s,d)
        print(G.GetVertex(d).ds)
    elif c1==2:
        print("Choose your priority")
        print("1.Travel in Shortest time path")
        print("2.Travel in Cheapest Price path")
        print("3.Travel in the Best Path")
        master.update_idletasks()
        master.update()
        choice2=int(selected.get())
        c2=choice2
        print(c2)
        # c2=int(input())
        while c2!=1 and c2!=2 and c2!=3:
            print("Ooops, Its seems you have entered an invalid choice.Please enter a valid choice")
            c2=int(input())
        if c2==1:
            DijkstrasST(G,G.GetVertex(s),G.GetVertex(d))
            print("your path from souce to destination is")
            PrintPath(G,s,d)
            print("\b\b\b\b\b\b\b\b\b\n")
            print("Time taken: Approx.",G.GetVertex(d).ts, "minutes")
        elif c2==2:
            DijkstrasCP(G,G.GetVertex(s),G.GetVertex(d))
            print("your path from souce to destination is")
            PrintPath(G,s,d)
            print(G.GetVertex(d).cs)
   

if __name__ == '__main__':
    main()