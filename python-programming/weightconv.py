weight = float(input("Enter Your weight: "))

unit = input("Enter desired unit in K or L : ")

if unit == "K":
    weight = weight / 2.205
    measurement = "kgs."
    print(f"Enter weight is {weight} {measurement}")
elif unit == "L":
    weight = weight * 2.205
    measurement = "lbs."
    print(f"Enter weight is {weight} {measurement}")
else:
    print("Invalid Unit")
