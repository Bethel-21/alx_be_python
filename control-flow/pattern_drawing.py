

number = int(input("Enter the size of the pattern:"))

while number % 2 == 0:
    for i in range(0, number):
        print("*" * number, end="")
        print()
    break
