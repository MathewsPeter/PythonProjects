line1 = "Hi, NAME is my friend"
line2 = "I like ACTION"
line3 = "Weather is ADJ"

name = input("enter name of a person: ")
action = input("enter an action: ")
adj = input("enter an adjective: ")

print(line1.replace("NAME", name))
print(line2.replace("ACTION", action))
print(line3.replace("ADJ", adj))