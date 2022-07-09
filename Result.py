print("Whether you are passed or failed?")

N = input ("Enter your Name : ")
M = int(input ("Enter your Marks (out of 100): "))

if 100>=M>=33:
    print("You are Passed", N)

elif 0<=M<33:
    print ("You are Failed", N)

else:
    print ("Invalid Input")
