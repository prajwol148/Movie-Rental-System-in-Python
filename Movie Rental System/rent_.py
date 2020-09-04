import sys
def rent_():
    file=open("movielist.txt","r")
    l=[]
    for line in file:
        line=line.replace("\n","")
        a=line.split(",")
        l.append(a)
    sn_PF=int(l[0][2])
    sn_LOR=int(l[1][2])
    sn_TR=int(l[2][2])
    sn_AE=int(l[3][2])
    sn_DBS=int(l[4][2])
    sn_INC=int(l[5][2])
    sn_LOG=int(l[6][2])
    sn_TWOWS=int(l[7][2])
    sn_SP=int(l[8][2])
    sn_PH=int(l[9][2])
    sn_HANG=int(l[10][2])
    
    
    username=input("What would you like us to call you: ")
            
    file=open("%s %s.txt" % ("Rented by ", username),"w") # this creates receipt which is named as Borrowed by user(user= person who borrow)
    file.write("%s %s" % ("Name: ", username)) # Print the name of borrower
    
    p=0 #p represents the price


                
    quantity= False
    while quantity== False:
        quan= False
        try:
            while quan== False:
                q=int(input("Enter the number of movies you want to rent: "))
                if q<=0:
                    print("Please enter a valid command")
                else:
                    quan= True
            quantity= True
        except:
            print("Please enter a valid command")
            
    

    for i in range (1):
        movie=0
        name= False
        while name== False:
            moviename= False
            try:
                while moviename== False:
                    movie=int(input("Which movie you want to rent? Please specify SN of the movie:"))
                    if movie<=0 or movie>10:
                        print("Please choose again and choose valid number")
                    else:
                        moviename= True
                name= True
            except:
                print("Please choose again and choose valid number")
                movie=int(input("Which movie you want to rent? Please specify SN of the movie:"))


        if movie==1:
            p=p+5
            if q<sn_PF:
                sn_PF= sn_PF-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Pulp Fiction' remaining to rent is: ", sn_PF)
                file.write("%s %s\n" %("\nMovie rented is: ",l[0][0]))
                file.write("%s %d\n" %("Price per movie: ",int(l[0][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))


                
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==2:
            p=p+2
            if q<sn_LOR:
                sn_LOR= sn_LOR-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Lord Of The Rings' remaining to rent is: ", sn_LOR)
                file.write("%s %s\n" %("\nMovie rented is: ",l[1][0]))
                file.write("%s %d\n" %("Price per movie: ",int(l[1][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))


                
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()


        elif movie==3:
            p=p+4
            if q<sn_TR:
                sn_TR= sn_TR-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'The Revenant' remaining to rent is: ", sn_TR)
                file.write("%s %s\n" %("\nMovie rented is:",l[2][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[2][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==4:
            p=p+5
            if q<sn_AE:
                sn_AE= sn_AE-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Avengers Endgame' remaining to rent is: ", sn_AE)
                file.write("%s %s\n" %("\nMovie rented is:",l[3][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[3][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==5:
            p=p+4
            if q<sn_DBS:
                sn_DBS= sn_DBS-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Dragonn Ball Super Broly' remaining to rent is: ", sn_DBS)
                file.write("%s %s\n" %("\nMovie rented is:",l[4][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[4][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()
                             


        elif movie==6:
            p=p+3
            if q<sn_INC:
                sn_INC= sn_INC-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Inception' remaining to rent is: ", sn_INC)
                file.write("%s %s\n" %("\nMovie rented is:",l[5][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[5][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==7:
            p=p+4
            if q<sn_LOG:
                sn_TR= sn_TR-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'The Revenant' remaining to rent is: ", sn_LOG)
                file.write("%s %s\n" %("\nMovie rented is:",l[6][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[6][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==8:
            p=p+3.5
            if q<sn_TWOWS:
                sn_LOR= sn_TWOWS-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'The Wolf Of Wall Street' remaining to rent is: ", sn_TWOWS)
                file.write("%s %s\n" %("\nMovie rented is:",(l[7][0])))
                file.write("%s %d\n" %("Price per movie:",int(l[7][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==9:
            p=p+2
            if q<sn_SP:
                sn_SP= sn_SP-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Spiderman-3' remaining to rent is: ", sn_SP)
                file.write("%s %s\n" %("\nMovie rented is:",l[8][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[8][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()



        elif movie==10:
            p=p+4
            if q<sn_PH:
                sn_PH= sn_PH-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'The Persuit Of Happiness' remaining to rent is: ", sn_PH)
                file.write("%s %s\n" %("\nMovie rented is:",l[9][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[9][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))                  
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()


        elif movie==11:
            p=p+4
            if q<sn_HANG:
                sn_HANG= sn_HANG-q
                print("Thank you for renting. I hope you will  enjoy!")
                print("Total number of 'Hangover' remaining to rent is: ", sn_HANG)
                file.write("%s %s\n" %("\nMovie rented is:",l[10][0]))
                file.write("%s %d\n" %("Price per movie:",int(l[10][1])))
                file.write("%s %d\n" %("Total number of movie you rented: ",q))
            else:
                print("We are sorry to say that the total amount of movies available is: ",l[0][2])
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and any other keys for NO: ")
                if Yes=="Y":
                    rent_()
                else:
                    sys.exit()


        elif movie<1 or movie>11:
            print("Please choose again and choose valid number")
            movie=int(input("Which movie you want to rent? Please specify SN of the movie:"))

    

            
        
        file.write("%s %5.1f %s\n"%("Your total amount is :",q*p,"dollars"))
        from datetime import date
        file.write("%s"%("Renting Date"))
        file.write(str(date.today()))
        file.close()
                             
    print("************************************************************************************************")
                             
    file=open("%s %s.txt" % ("Rented by ", username),"r")
    for line in file:
            print (line)
    print("************************************************************************************************")                         

    again=open("movielist.txt","w")
    again.write("%s %s %s %d\n"%("Pulp Fiction,                ", "5",", ", sn_PF))
    again.write("%s %s %s %d\n"%("Lord Of The Rings,        ", "2",", ", sn_LOR))
    again.write("%s %s %s %d\n"%("The Revenant,                ", "4",", ", sn_LOR))
    again.write("%s %s %s %d\n"%("Avengers Endgame,        ", "5",", ", sn_AE))
    again.write("%s %s %s %d\n"%("Dragon Ball Super,        ", "4",", ", sn_DBS))
    again.write("%s %s %s %d\n"%("Inception,                ", "3", ", ",sn_INC))
    again.write("%s %s %s %d\n"%("Logan,                        ", "4", ", ",sn_LOG))
    again.write("%s %s %s %d\n"%("The Wolf Of Wall Street,        ", "3", ", ",sn_TWOWS))
    again.write("%s %s %s %d\n"%("Spiderman-3,                ",   "2", ", ",sn_SP))
    again.write("%s %s %s %d\n"%("The Persuit Of Happiness,", "4",", ",sn_PH))
    again.write("%s %s %s %d\n"%("Hangover,                ",    "4",", ",sn_HANG))

    file.close()

rent_()
