# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:36:42 2022

@author: Avinash
"""
"""
noOfRows = int(input("Enter the no of rows: "))

#1
for row in range(1,noOfRows+1):
    print("* "*row)
   
#1.1    nested for loop
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("*",end="")
    print()
 
#1.2
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print(row,end="")
    print()

#1.3
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print(column,end="")
    print()
    
#1.4
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0}".format(row),end="")
    print()

#1.5
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0}".format(column),end="")
    print()

#1.6
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0}{1} ".format(row,column),end="")
    print()
 
 #2  
for row in range(noOfRows):
    print("* "*(noOfRows-row))
   
#2.1
for row in range(noOfRows,0,-1):
    for column in range(row):
        print("*",end="")
    print()
 
#1.2.1
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("*",end="")
    print()
for row in range(noOfRows-1,0,-1):
    for column in range(row):
        print("*",end="")
    print()
  
#1.2.2
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print(row,end="")
    print()
for row in range(noOfRows-1,0,-1):
    for column in range(row):
        print(row,end="")
    print()

#1.2.3
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print(column,end="")
    print()
for row in range(noOfRows-1,0,-1):
    for column in range(row):
        print(column,end="")
    print()
    
#1.2.4
for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0}{1} ".format(row,column),end="")
    print()
for row in range(noOfRows-1,0,-1):
    for column in range(row):
        print("{0}{1} ".format(row,column),end="")
    print()
 
    
#1.2.4
noOfRows = int(input("Enter the no of rows: "))
ch = 65          #ASCII Value of A

for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0} ".format(chr(ch)),end="")
    print()
 
#1.2.5
noOfRows = int(input("Enter the no of rows: "))
ch = 64          #ASCII Value of A is 65

for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        ch = ch+1
        print("{0} ".format(chr(ch)),end="")
    print()

#1.2.6
noOfRows = int(input("Enter the no of rows: "))
sum = 0         

for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        sum = sum+1
        print("{:02d} ".format(sum),end="")
    print()


#3.1
for row in range(1,noOfRows+1):
    for spaces in range(1,(noOfRows-row)+1):
        print(" ",end="")
    for stars in range(1,row+1):
        print("*",end="")
    print()

#4.3.1  
for row in range(1,noOfRows+1):
    for spaces in range(1,(noOfRows-row)+1):
        print(" ",end="")
    for stars in range(1,row+1):
        print("* ",end="")
    print()    


#5

for row in range(noOfRows):
    for column in range(noOfRows):
        print("* ",end="")
    print()

#6.1.1
for row in range(noOfRows):
    for column in range(noOfRows):
        print("{0}".format(row),end="")
    print()
    
#6.1.2
for row in range(noOfRows):
    for column in range(noOfRows):
        if (row == column) or ((row + column) == noOfRows-1):
            print("{0}".format(row),end="")
        else:
            print(" ", end="")
    print()
    

#6.1.3
for row in range(noOfRows):
    for column in range(noOfRows):
        if (row == column) or ((row + column) == noOfRows-1):
            print("{0}".format(column),end="")
        else:
            print(" ", end="")
    print()

"""
"""
#6.2.1 
value = input("Enter the string values with odd no. of characters: ")        #i/p eg 12345, anils
noOfRows= len(value)
for row in range(noOfRows):
    for column in range(noOfRows):
        if (row == column) or ((row + column) == noOfRows-1):
            print("{0}".format(value[row]),end="")
        else:
            print(" ", end="")
    print() 

#6.2.2
value = input("Enter the string values with odd no. of characters: ")      #i/p eg 12345, anils
noOfRows= len(value)
for row in range(noOfRows):
    for column in range(noOfRows):
        if (row == column) or ((row + column) == noOfRows-1):
            print("{0}".format(value[column]),end="")
        else:
            print(" ", end="")
    print()  
    

#7
totalrows = int(input("Enter the total no of rows: "))

for rowno in range(totalrows):
    for colno in range(totalrows):
        if (colno==0) or (rowno==totalrows-1) or (rowno==colno):
            print("*", end=" ")
        else:
            print(" ", end = " ")
    print()
  
#7.1
totalrows = int(input("Enter the total no of rows: "))

for rowno in range(totalrows):
    for colno in range(totalrows):
        if (colno==totalrows-1) or (rowno==0) or (rowno==colno):
            print("*", end=" ")
        else:
            print(" ", end = " ")
    print()
    
    """  
    
    
    
    
    
    
    
    
    



























    