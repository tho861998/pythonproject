def switch():
    def volume(r,h):
        return r*r*r*h
    option = int(input("what do you want to calculate? \n1.Surface area 2.Literal area 3.Volume: "))
    if option in range(1, 4):
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        if option == 1:
            output = 2 * 3.14 * r * (r+h)
            print("Surface area: ", output)
        if option == 2:
            output = 2 * 3.14 * r * r
            print("Literal area: ", output)
        if option == 3:
            print("Volume: ", volume(r,h))
    else:
        print("Invalid input")
switch()