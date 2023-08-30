
# Degree centigrade to fahrenheit
# (c * 9/5) + 32 = Fahrenheit

#fahreinheit to degree centigrade

#(F-32)* 5/9 = degrees

unit = input("Enter the temperature unit centigrade or fahrenheit C or F: ")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = temp * 9/5 + 32
    print(f"Temperature is {temp}")
elif unit == "F":
    temp = temp - 32 * 5/9
    print(f"Temperature is {temp} ")
else:
    print("Unit is invalid")



