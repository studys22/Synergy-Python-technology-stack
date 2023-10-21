a, b = map(
    float,
    input("Enter the length and width of the rectangle separated by a space: ").split(),
)
print("The area of the rectangle is equal to", a * b)
print("The perimeter of the rectangle is equal to", 2 * (a + b))
