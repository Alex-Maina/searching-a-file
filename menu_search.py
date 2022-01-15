def main ():
    menu ()

def menu ():
    print ("Welcome to the Search Wizard")
    print ()
    choice = int(input("""
                      1: Search with name
                      2: search with age
                      0: Exit

                      Please enter your choice: """))
    
    if choice == 1:
        searchname ()
    elif choice == 2:
        searchage ()
    elif choice == 0:
        print ("Exiting")
    else:
        print("Invalid choice. Exiting the program")
    
    print ("Thanks for using this program")
        
    
        


#first reads a letter from the user, and then prints only the lines where the name starts with that letter.
def searchname ():
    check =[] 
    user_letter = input('Which letter(s) would you like to use for your search: ')
    open_file = open("names.txt", "r")
    for line in open_file:

        #Looks for a match, either a single letter or longer string nomatter the case of the input
        x = line.startswith(user_letter.title(),0,7) 

        #Adds the boolean value from each line to the list (Check)
        check.append(str(x))  

        #Print the line where the boolean value is true
        if x==True:
            print (line.strip())
    
    #If the list has no "True", then no entry was found
    if (check.count("True")==0): 
        print("No entries exist that starts with "+ user_letter)

    return


#gets the search age from the user
def searchage ():
    check_age =[] 
    search_age = str(input('Which age would you like to use for your search: '))
    open_file = open("names.txt", "r")
    for line in open_file:

        #Looks for a match
        clean_line = line.strip()
        x = clean_line.endswith(search_age)

        #Adds the boolean value from each line to the list (Check_age)
        check_age.append(str(x))  

        #Print the line where the boolean value is true
        if x==True:
            print (clean_line)
    
    #If the list has no "True", then no entry was found
    if (check_age.count("True")==0): 
        print("No entries exist for age: "+ search_age)
    
    return 



#the program is initiated here.
main ()








