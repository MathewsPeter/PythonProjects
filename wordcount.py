line = input("enter a sentence: ")
cc = 0
wc = 1
for character in line:
    cc+=1
    if character == " ":
        wc+=1
    
print("character count is ", cc)
print("word count is ", wc)