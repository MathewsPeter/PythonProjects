line = input("enter a sentence: ")
line = "hi hi i play game game"
cc = 0
wc = 1
for character in line:
    cc+=1
    if character == " ":
        wc+=1
    
print("character count is ", cc)
print("word count is ", wc)

words = line.split(" ")
wcdict = {}
for word in words:
    if word not in wcdict.keys():
        wcdicttmp= {word:1}
        wcdict.update(wcdicttmp)
    else:
        wcdict[word] += 1
    
print("Frequecy of each word:",wcdict)

