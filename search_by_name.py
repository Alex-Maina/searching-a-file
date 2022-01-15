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
            print (line)
    
    #If the list has no "True", then no entry was found
    if (check.count("True")==0): 
        print("No entry exists that starts with "+ user_letter)

searchname ()
