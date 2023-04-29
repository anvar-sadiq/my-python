def Persondetails():
    print("Person Details")
    Name=str(input('Enter a Name: '))
    Age=int(input('Enter Age: '))

    if Age<18:
        print("Bad Luck")
    if Age==18:
        print("You Are In")
    if Age>19 and Age<36:
        print("More OK")
    else:
        print("Processing")

Persondetails()


