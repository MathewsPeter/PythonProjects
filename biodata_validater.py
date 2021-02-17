'''Example: What is your name? If the user enters * you prompt them that the input is wrong, and ask them to enter a valid name.

At the end you print a summary that looks like this:

- Name: John Doe
- Date of birth: Jan 1, 1954
- Address: 24 fifth Ave, NY
- Personal goals: To be the best programmer there ever was.
'''
while(1):
    name = input("Enter name: ")
    if name.replace(" ", "").isalpha():
        break
    print("Name shall have only alphabets and space. Please try again.\n")
    
while(1):
    dob = input("Enter DOB as DDMMYYY: ")
    dd = (int)(dob[0:2])
    mm =  (int)(dob[2:4])
    yyyy =  (int)(dob[4:8])
    if(dd>0 and dd<=31):
        if(mm>0 and mm<=12):
            if(yyyy>1900 and yyyy<=2021):
                break;
            else:
                print("Year should be between 1900 and 2021. Please try again.\n")
        else:
            print("Month should be between 1 and 12. Please try again.\n")
    else:
        print("Date should be between 1 and 31. Please try again.\n")                
                
        
print("Name is ", name)
print("DOB is ", dd,"-",mm,"-",yyyy)
    