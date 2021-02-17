w=input("enter a word")
w = w.strip()
if w == w[::-1]:
    print(w, " is a palindrome")
else:
    print(w, " is not a palindrome")