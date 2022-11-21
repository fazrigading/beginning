import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
firstnim = 2009106001
lastnim = 2009106050
nim = firstnim <= lastnim
while True:
    clear()
    print("Please input your id:")
    try:
        inputID = int(input("NIM: "))
        A = int(input("Year: "))
    except:
        print("Incorrect value.")
        time.sleep(2)
    else:
        if A == 2020:
            if inputID >= nim:
                print("Welcome to Class A of Informatics 2020.")
                input("Press any key to give thanks...")
                break
        elif A != 2020 or inputID != nim:
            print("You are not one of us. Goodbye.")
            break
        exit(1)