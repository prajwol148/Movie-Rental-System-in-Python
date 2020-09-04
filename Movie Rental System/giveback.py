import sys
def giveback():
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
    
    
    username=input("Can I know your name again: ")
            
    file=open("%s %s.txt" % ("Returned by ", username),"w") 
    file.write("%s %s\n" % ("Name: ", username)) 
    
    p=0
    f=0

                
    quantity= False
    while quantity== False:
        quan= False
        try:
            while quan== False:
                q=int(input("Enter the number of movies you want to return: "))
                if q<=0:
                    print("Please enter a valid number")
                else:
                    quan= True
            quantity= True
        except:
            print("Please enter a valid number")
            
    

    for i in range (1):
        movie=0
        name= False
        while name== False:
            moviename= False
            try:
                while moviename== False:
                    movie=int(input("Which movie you want to return? Please specify SN of the movie:"))
                    if movie<=0 or movie>10:
                        print("Please choose again and choose valid number")
                    else:
                        moviename= True
                name= True
            except:
                print("Please choose again and choose valid number")
                movie=int(input("Which movie you want to return? Please specify SN of the movie:"))
        if movie==1:
            time= int(input("How many days did you enjoy movie:"))
            
            if sn_PF<31 and q<(31-(sn_PF)):
                sn_PF=sn_PF+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Pulp Fiction available are:",sn_PF)
                    file.write("%s\n"%("Movie Returned: Pulp Fiction"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Pulp Fiction available are:",sn_PF)
                    file.write("%s\n"%("Movie Returned: Pulp Fiction"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Pulp Fiction because all",l[0][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()


        if movie==2:
            time= int(input("How many days did you enjoy movie:"))
            
            if sn_LOR<26 and q<(26-(sn_LOR)):
                sn_LOR=sn_LOR+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Lord Of The Rings available are:",sn_LOR)
                    file.write("%s\n"%("Movie Returned: Pulp Lord Of The Rings"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Lord Of The Rings available are:",sn_LOR)
                    file.write("%s\n"%("Movie Returned: Lord Of The Rings"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Lord Of The Rings because all",l[1][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()

        if movie==3:
            time= int(input("How many days did you enjoy movie:"))
            
            if sn_TR<23 and q<(23-(sn_TR)):
                sn_TR=sn_TR+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of 'The Revenant' available are:",sn_TR)
                    file.write("%s\n"%("Movie Returned: The Revenant"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of The Revenant available are:",sn_TR)
                    file.write("%s\n"%("Movie Returned: The Revenant"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with The Revenant because all",l[2][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()



        if movie==4:
            time= int(input("How many days did you enjoy movie:"))
            
            if sn_AE<17 and q<(17-(sn_AE)):
                sn_AE=sn_AE+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Avengers Endgame available are:",sn_AE)
                    file.write("%s\n"%("Movie Returned: Avengers Endgame"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Avengers Endgame available are:",sn_AE)
                    file.write("%s\n"%("Movie Returned: Avengers Endgame"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Avengers Endgame because all",l[3][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()




        if movie==5:
            time= int(input("How many days did you enjoy movie:"))
            
            if sn_DBS<36 and q<(36-(sn_DBS)):
                sn_DBS=sn_DBS+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Dragon Ball Super Broly available are:",sn_DBS)
                    file.write("%s\n"%("Movie Returned: Dragon Ball Super Broly"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Dragon Ball Super Broly available are:",sn_DBS)
                    file.write("%s\n"%("Movie Returned: Dragon Ball Super Broly"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Dragon Ball Super Broly because all",l[4][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()       
                    

        if movie==6:
            time= int(input("How many days did you enjoy movie:"))
           
            if sn_INC<16 and q<(16-(sn_INC)):
                sn_INC=sn_INC+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Inception available are:",sn_INC)
                    file.write("%s\n"%("Movie Returned: Inception"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Inception available are:",sn_INC)
                    file.write("%s\n"%("Movie Returned: Inception"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Inception because all",l[5][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()



        if movie==7:
            time= int(input("How many days did you enjoy movie:"))
            p=time-10
            if sn_LOG<20 and q<(20-(sn_LOG)):
                sn_LOG=sn_LOG+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Logan available are:",sn_LOG)
                    file.write("%s\n"%("Movie Returned: Logan"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Logan available are:",sn_LOG)
                    file.write("%s\n"%("Movie Returned: Logan"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Logan because all",l[6][0],"movies are already present in our store. Thank you!")
                Yes=input("If you want to return any other movie, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                    
                    
                elif Yes=="N":
                    sys.exit()


        if movie==8:
            time= int(input("How many days did you enjoy movie:"))
            p=time-10
            if sn_TWOWS<14 and q<(14-(sn_TWOWS)):
                sn_TWOWS=sn_TWOWS+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of The Wolf Of Wall Street available are:",sn_TWOWS)
                    file.write("%s\n"%("Movie Returned: The Wolf Of Wall Street"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of The Wolf Of Wall Street available are:",sn_TWOWS)
                    file.write("%s\n"%("Movie Returned: The Wolf Of Wall Street"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with The Wolf Of Wall Street because all",l[7][0],"movies are already present in our store. Thank you!")
                Yes=input("If you want to return any other movie, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                    
                    
                elif Yes=="N":
                    sys.exit()



        if movie==9:
            time= int(input("How many days did you enjoy movie:"))
            p=time-10
            if sn_SP<10 and q<(10-(sn_SP)):
                sn_SP=sn_SP+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Spiderman-3 available are:",sn_SP)
                    file.write("%s\n"%("Movie Returned: Spiderman-3"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Pulp Ficion available are:",sn_SP)
                    file.write("%s\n"%("Movie Returned: Spiderman-3"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Spiderman-3 because all",l[8][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()


        if movie==10:
            time= int(input("How many days did you enjoy movie:"))
            p=time-10
            if sn_PH<16 and q<(16-(sn_PH)):
                sn_PH=sn_PH+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of The Persuit Of Happiness available are:",sn_PH)
                    file.write("%s\n"%("Movie Returned: The Persuit Of Happiness"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of The Persuit Of Happiness available are:",sn_PH)
                    file.write("%s\n"%("Movie Returned: The Persuit Of Happiness"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with The Persuit Of Happiness because all",l[9][0],"movies are already present in our store. Thank you!")
                print("Let's start over.")
                Yes=input("If you want to borrow again, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                elif Yes=="N":
                    sys.exit()
                    
        
        if movie==11:
            time= int(input("How many days did you enjoy movie:"))
            p=time-10
            if sn_HANG<15 and q<(15-(sn_HANG)):
                sn_HANG=sn_HANG+q
                if time<=10:
                    print("Thank you for returning movie")
                    print("No of Hangover available are:",sn_HANG)
                    file.write("%s\n"%("Movie Returned: Hangover"))
                    file.write("%s\n"%("Thank you for returning movie. We will be grateful to see you again"))
                    
                if time>10:
                    p=time-10
                    print("Thank you for returning movie but you are late so you will be fined.")
                    print("No of Hangover available are:",sn_HANG)
                    file.write("%s\n"%("Movie Returned: Hangover"))
                    file.write("%s %5.0f %s\n"%("You are late, your fine is:",p,"dollars"))
                f=f+p

    
            else:
                print("I think you have mistaken other movies with Hangover because all",l[10][0],"movies are already present in our store. Thank you!")
                Yes=input("If you want to return any other movie, press Y for YES and N for No: ")
                if Yes=="Y":
                    giveback()
                    
                    
                elif Yes=="N":
                    sys.exit()



            
            

        

        elif movie<1 or movie>11:
            print("Please choose again and choose valid number")
            movie=int(input("Which movie you want to return? Please specify SN of the movie:"))

    

            
        
        file.write("%s %5.1f %s\n"%("Your total fine is :",f,"dollars"))
        from datetime import date
        file.write("%s"%("Returning Date"))
        file.write(str(date.today()))
        file.close()
                             
    print("************************************************************************************************")
                             
    file=open("%s %s.txt" % ("Returned by ", username),"r")
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

giveback()
