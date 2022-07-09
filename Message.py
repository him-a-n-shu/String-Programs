def fullname(mes,fn,ln):
    full_name = fn + " " + ln
    print(mes, full_name)

mes = input("Enter message: ")
fulln = input("Enter first name: ")
lastn = input("Enter last name: ")
fullname(fulln,lastn)
