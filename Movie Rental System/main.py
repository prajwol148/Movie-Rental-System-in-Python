import sys
def main():
    sorted_=True#assigning the value of sorted as false
    while sorted_==True:
        
        option =int(input(''' How would we help you?
        1: Show the list of available movies for renting
        2: Press 2 to rent a movie
        3: Press 3 if you want to return rented movie
        4: Press 4 if you feel like exiting: \n'''))
        if option ==1:
            import movie_
            movie_.movie_()#import the movie_ module
        elif option ==2:
            import rent_
            rent_.rent_()#importing the return module


        elif option ==3:
            import giveback
            giveback.giveback()#importing the return module
        elif option ==4:
            sys.exit()
        else:
            print("Please enter valid option")
            main()
        optionn=input("Press Y to continue or any other key to exit:")
        if optionn=="Y":
            sorted_=True
        else:
            sorted_=False
            print("Thank you. We hope we could serve you again. Have a nice day.")               
main()
