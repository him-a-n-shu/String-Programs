air_temp = int(input("Enter the Temperature : "))

if 25 > air_temp >=15:
    print("It is cold outside.")
elif air_temp >= 25:
    print("It is Moderate outside.")
elif air_temp < 15:
    print("It is too Cold outside.")
elif air_temp > 25:
    print("It is warm outside.")
else:
    print("Invalid Input")
print("Thank You!\nHave a nice day.")
