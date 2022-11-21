def menu():
    print("Menu")

while True:
    # Enter integer value from the console.
    x = int(input())

    # Divide 1 by x to test error cases
    try:
        result = 1 / x
    except:
        print("Error case")
        menu()
    else:
        print("Pass case")
        exit()