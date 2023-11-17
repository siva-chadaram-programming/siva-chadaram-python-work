
#print(help(str))

name = input("Enter your name: ")

#phone_number = input("Enter your phone number: ")

#result = name.__sizeof__()
#result = name.upper() #makes string to UPPER CASE
#result = name.lower() #makes string to UPPER CASE

#result = name.splitlines()
#result  = name.lstrip()
#result = len(name) #gives lenght of the string
#result = name.find("o") #prints the index of letter o if the letter o present in the string
#result = name.rfind("o") #prints the index of letter o if the letter o present in the string
#result = name.isdigit() #prints true /flse if the string contins digits content
#result = name.isalpha() #prints true /flse if the string contains alphabets content
#result = phone_number.count("-")
#result = phone_number.replace("-", "*")

if len(name) > 12:
    print("username should not be more than 12")
elif not name.find(" ") == -1:
    print("username should not contains spaces")
elif not name.isalpha():
    print("username should not contain digits")
else:
    print(f"Welcome {name}")



#print(result)


