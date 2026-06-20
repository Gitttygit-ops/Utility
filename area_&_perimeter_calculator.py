def calc_area(length, width):
    area = length * width
    print("The area is", area)

def calc_perimeter(length, width):
    perimeter = (length * 2) + (width * 2)
    print("The perimeter is", perimeter)

while True:
    calculate_type = (input("Do you want to do calculate area or perimeter? "))
    if not (calculate_type == "area" or calculate_type == "perimeter"):
        print("Please enter either area or perimeter")

    if calculate_type == "area" or calculate_type == "perimeter":
        break

while True:
    length = int(input("Enter the length of the sides: "))
    if not length.is_integer():
        print("Please enter a number")

    if length.is_integer():
         break



while True:
    width = int(input("Enter the length of the top and bottom: "))
    if not width.is_integer():
        print("Please enter a number")

    if width.is_integer():
        break



if calculate_type == "area":
    calc_area(length, width)


elif calculate_type == "perimeter":
    calc_perimeter(length, width)








