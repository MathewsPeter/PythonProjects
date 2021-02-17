fullform = input("Enter a full form: ")
words = fullform.split(" ")
acro = ""
for word in words:
    acro+=word[0]
print("Acronym is ", acro)    