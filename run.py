run = input("Do you run in the morning: ")

if run == 'yes':
    print("You are doing great work")
else:
    response = input("Do you have any health issue? ")
    if response == 'yes':
        print("Just walk, do not run")
        print("Do Yoga also")
    else:
        print("You should run in the morning")