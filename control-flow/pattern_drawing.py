# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # print star without new line
    print()  # move to next line after row is done
    row += 1
