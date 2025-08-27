number = 5
guess = int(input("Enter a number: "))

while guess != number:
    print("Try again")
    guess = int(input("Enter a number: "))
print("You guessed the number correctly")
