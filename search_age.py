#printing only the lines where the age is equal to 5.
print ('Entries where age is 5 include: ')
def searchage():
    open_file = open("names.txt", "r")
    for line in open_file:
        clean_line = line.strip() #gets rid off the trailing white spaces
        if clean_line.endswith('5'):
            print (line)

searchage()
