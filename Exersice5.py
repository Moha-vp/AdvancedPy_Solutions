
name1 = input("Enter the name of the first runner: ")
time1 = float(input(f"Enter {name1}'s time: "))

name2 = input("Enter the name of the second runner: ")
time2 = float(input(f"Enter {name2}'s time : "))


if time1 < time2:
    print(f"{name1} is the faster runner")
elif time1 > time2:
    print(f"{name2} is the faster runner")
else:
    print("Both runners have the same time!")
