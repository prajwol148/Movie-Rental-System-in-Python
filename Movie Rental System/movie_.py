def movie_():
    sn=1
    l=[]
    print("Hello!\nWe have following movies available for you to rent:\n ")
    print("************************************************************************************")
    print("S/N       Movies             Rental Charge(in dollar)           Available quantity")
    print("____________________________________________________________________________________")

    file=open("movielist.txt","r") # here "r" reperesnts the read function

    
    for line in file:
        line=line.replace("\sn","")
        line=line.replace(",","\t\t")
        print("",sn,"\t"+line)
        line=line.replace("\t\t",",")
        b=line.split(",")
        l.append(b)
        sn=sn+1
    print("____________________________________________________________________________________\n")
        
    
