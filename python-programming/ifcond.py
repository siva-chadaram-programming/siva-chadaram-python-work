age = int(input("Enter Your age: "))
if age >= 18:
    print("You are qualified")
elif age < 0:
    print("Fuck away from here")
else:
    print("You are not qualified")

response = input("Are you hungry (Y/N): ")
if response == "Y":
    print("Go and Have KFC")
else:
    print("Thanks for saving food")

name = input("Enter your name: ")
if name == "":
    print("You didn't enter anything")
else:
    print(f"Hello your name is {name}")


for_sale = True

if for_sale:
    print("This iteam is for sale")
else:
    print("This item is not for sale")

