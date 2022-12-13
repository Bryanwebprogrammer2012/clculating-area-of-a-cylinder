print(" CALCULATING AREA OF A CYLINDER ")


def equation():
    r = int(input("Enter radius: "))
    h = int(input("Enter height: "))
    pi = 3.142
    s = (2*pi*r*h) + (2*pi*r*r)
    print(s)
equation()
