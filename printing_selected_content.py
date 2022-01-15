#printing only the lines where the name starts with the letter “A”
print ('Lines where the name starts with the letter “A”: ')
def searchname ():
    open_file = open("names.txt", "r")
    for line in open_file:
        if line.startswith('A'):
            print (line)
