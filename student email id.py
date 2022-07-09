lst = []
n = int(input("No. of Students: "))
for i in range(n):
    email = input("Enter email ID of student "+str(i+1)+": ")
    lst.append(email)
    etuple = tuple(lst)

print("Student email IDs:\n", etuple)
