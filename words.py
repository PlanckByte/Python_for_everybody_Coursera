fname = input("Enter file: ") #promts to enter file
fhandle = open(fname) #opens the file in read mode
word_count = dict() #makes an empty dictionary
count = 0 #counter to 0
for line in fhandle: #reads line by line the file
    words = line.split() #splits file into words and stores in a list
    for word in words: #go through each word in the list increment the count by one and put in a dictionary
        count = count+1
        word_count[word]=count #dictionary with key=word and value=counter
print(word_count)
