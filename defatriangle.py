#difine the triangle type
def main():
    base = input("Triangle base lenght:")
    side1 = input("First side lenght:")
    side2 = input("Second side lenght:")
    triangle = 0
    if  side1 == side2:
        if base != side1:
            triangle = "isosceles"
        else:
            triangle = "equilateral"
    elif side1 == base:
        triangle = "isosceles"
    elif side2 == base:
        triangle = "isosceles"
    else:
        triangle = "scalene"
    
    print("the triangle is " + triangle)





if __name__ == "__main__":
    main()
