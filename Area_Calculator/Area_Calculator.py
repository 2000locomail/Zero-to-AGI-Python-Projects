shape = input("Choose Your Shape (Square, Circle, or Triangle): ").strip().capitalize()
if shape == "Square":
    sqsize = float(input("Enter Square Size (in cm): "))
    area_of_sq = sqsize**2
    print(f"The area of Square is {area_of_sq} cm.sq")
elif shape == "Circle":
    cirsize = float(input("Enter Radius of Circle (in cm): "))
    area_of_cir = 3.14159*cirsize**2
    print(f"The area of Circle is {area_of_cir} cm.sq")
elif shape == "Triangle":
    trihsize = float(input("Enter Height of Triangle (in cm): "))
    trilsize = float(input("Enter Length of Triangle (in cm): "))
    area_of_tri = 0.5*trihsize*trilsize
    print(f"The area of Triangle is {area_of_tri} cm.sq")
else:
    print("Error")