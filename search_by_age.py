#gets the search age from the user
check_age =[] 
search_age = str(input('Which age would you like to use for your search: '))
def searchage ():
    open_file = open("names.txt", "r")
    for line in open_file:

        #Looks for a match
        clean_line = line.strip()
        x = clean_line.endswith(search_age)

        #Adds the boolean value from each line to the list (Check_age)
        check_age.append(str(x))  

        #Print the line where the boolean value is true
        if x==True:
            print (line)
    
    #If the list has no "True", then no entry was found
    if (check_age.count("True")==0): 
        print("No entry exists for age: "+ search_age)

searchage ()
