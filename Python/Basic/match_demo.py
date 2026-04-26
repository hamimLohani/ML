num = int(input("Enter an integer: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("1 > integer  > 3")