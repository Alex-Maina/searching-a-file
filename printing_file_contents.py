#A function that opens the file “names.txt” and print its contents using a loop
print ('File contents: ')
def searchname ():
    open_file = open("names.txt", "r")
    for x in open_file:
        print (x)

searchname ()
