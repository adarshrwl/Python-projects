import random


def easy():
    looping = True
    randomnumber = random.randint(0, 100)
    count = 0
    while looping:
        try:
            inputed_number = int(input("Enter your guessing number(1-100): "))
            count = count+1
            if inputed_number == randomnumber:
                print(f"Congralutions You guessed number in {count} times")
                exit()
            elif(inputed_number < randomnumber):
                print("Please guess higher number")
            elif(inputed_number > randomnumber):
                print("Please guess lower number")
        except:
            print("Please Input numbers")
        finally:
            if count > 10:
                print(
                    f"You lost the game as you have made more than {count-1} mistakes")
                break


def medium():
    looping = True
    randomnumber = random.randint(0, 100)
    count = 0
    while looping:
        try:
            inputed_number = int(input("Enter your guessing number(1-100): "))
            count = count+1
            if inputed_number == randomnumber:
                print(f"Congralutions You guessed number in {count} times")
                exit
            elif(inputed_number < randomnumber):
                print("Please guess higher number")
            elif(inputed_number > randomnumber):
                print("Please guess lower number")
        except:
            print("Please Input numbers")
        finally:
            if count > 7:
                print(
                    f"You lost the game as you have made more than {count-1} mistakes")
                break


def hard():
    looping = True
    randomnumber = random.randint(0, 100)
    count = 0
    while looping:
        try:
            inputed_number = int(input("Enter your guessing number(1-100): "))
            count = count+1
            if inputed_number == randomnumber:
                print(f"Congralutions You guessed number in {count} times")
                exit()
            elif(inputed_number < randomnumber):
                print("Please guess higher number")
            elif(inputed_number > randomnumber):
                print("Please guess lower number")
        except:
            print("Please Input numbers")
        finally:
            if count > 5:
                print(
                    f"You lost the game as you have made more than {count-1} mistakes")
                break


print("Welcome to the guessing game")
difficulty_level = input(
    "Enter the difficulty level(e for easy/m for medium/h for hard): ")
if difficulty_level == 'e':
    easy()
elif difficulty_level == 'm':
    medium()
else:
    hard()
