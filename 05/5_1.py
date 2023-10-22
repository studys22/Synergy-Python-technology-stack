a = int(input("Input a number: "))

if a == 0:
    print("This is a zero!")
elif a > 0:
    if a % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    if a % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")

if a % 2 != 0:
    print("The number is not even")
