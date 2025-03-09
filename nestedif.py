#grades of students
per=int(input("Enter the percentage: "))
if (per>=85):
    if (per>=95):
        print("a grade")
    else:
        print("a+ grade")
elif (per>=65):
    if (per>=75):
        print("b grade")
    else:
        print("b+ grade")
elif (per>=45):
    if (per>=55):
        print("c grade")
    else:
        print("c+ grade")
else:
    print("fail")


