N = input("Enter your Name: ")
M = int(input ("Enter your Marks (out of 100): "))

#Case 1
if 100>=M>=80:
    print ("Excellent")

#Case 2
if 50<=M<80:
    print("You can do better")

#Case 3
if 0<=M<50:
    print("You need to work hard");

if M>100 or M<0:
    print ("Invalid Input")
