words = input("Enter some words to translate: ")
print("You entered " + words)
#to break apart words into a list with split function
words = words.split(' ') #these are dicks
print(words)
#you will get a list from split functions
for i in words: #these
    if len(i) >= 4: #these = 5 #length of first string >= 4
        i = i[2:] + "%s" % i[1:] #ese + hese
        print("Translated strings: ", i)
    else:
        pass