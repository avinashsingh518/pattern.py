# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:36:42 2022

@author: Avinash
"""

noOfRows = int(input("Enter the no of rows: "))
"""
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
        print(row,end="")
        #print("{0}".format(row),end="")
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
        print(column,end="")
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
ch = 65          #ASCII Value of A is 65

for row in range(1,noOfRows+1):
    for column in range(1,row+1):
        print("{0} ".format(chr(ch)),end="")
        ch = ch + 1
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
            print(" ", end =" ")
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

n = int(input("enter the no. of rows: "))
for row in range(1,n+1):
  for col in range(1,2*n):
      if row ==n or row+col ==n+1 or col -row ==n-1:
          print("*", end="")
      else:
          print(" ", end="")
  print()

n = int(input("enter the no. of rows: "))
k=2
for row in range(1,n+1):
  for col in range(1,2*n):
      if row+col ==n+1 or col -row ==n-1:
          print("*", end="")
      elif row==n and col!=k:
          print("*", end = "")
          k=k+2
      else:
          print(" ", end="")
  print()



num = int(input("enter the no of rows"))
for row in range(num,0,-1):
  for col in range(0,num-row):
          print(end =" ")                     #1 space in end
  for stars in range(0,row):
      print("* ", end="")                     #1 space after star      
  print()


n = int(input("enter the no of rows: "))
   
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end = "")
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()

for i in range(1,n):
    for j in range(i+1):
        print("*", end = "")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
 


for row in range(noOfRows):
    for col in range(noOfRows):
        if row ==0 or row ==noOfRows-1 or col==0 or col==noOfRows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



for i in range(noOfRows):
    for j in range(noOfRows-i-1):
         print(" ",end ="")
    for j in range(2*i+1):
         if j==0 or j==2*i:
             print("*",end="")
         else:
             print(" ",end="")
    print()
for i in range(noOfRows-1):
    for j in range(i+1):
         print(" ",end="")
    for j in range(2*(noOfRows-i-1)-1):
         print("*",end="")
    print()
         
    """      

for i in range(noOfRows):
    for j in range(noOfRows-i-1):
         print(" ",end ="")
    for j in range(2*i+1):
         if j==0 or j==2*i:
             print("*",end="")
         else:
             print(" ",end="")
    print()
for i in range(noOfRows-1):
    for j in range(i+1):
         print(" ",end="")
    for j in range(2*(noOfRows-i-1)-1):
        if j==0 or j==2*(noOfRows-i-1)-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
























   
    
    
    



























    