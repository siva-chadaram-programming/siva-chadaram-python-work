#python way of  file handling
#method1
file = open("simple.txt", 'r')
content = file.read()
print(content)

#method2
with open("simple.txt", 'r') as file:
    sf = file.read()
print(sf)

#method3
#Read mode character wise
file = open("simple.txt", 'r')
print(file.read(2))

#method4
#python code to illustrate split function
with open("simple.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

#method5
#python code to create a file
file = open("write.txt", 'w')
file.write("Hello this is how the writing works")
file.write("In Python")
file.close()

#method6
#python writen statement along with()

with open("write.txt", 'w') as file:
    file.write("Cupertino")

#method7
#python code to append a file
file = open("write.txt", 'a')
file.write("Am adding this line to my file")
file.close()

#method8
import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)






