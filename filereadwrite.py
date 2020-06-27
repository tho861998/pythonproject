file = open("test.txt")
print(file.read())
file = open("test.txt", "a") ##append the file 
file.write("this is some text i want to append")
file.close()
file = open("test.txt")
print(file.read())
file = open("test.txt", "w") ##overwrite the file 
file.write("this is some text i want to overwrite")
file.close()
file = open("test.txt")
print(file.read())
