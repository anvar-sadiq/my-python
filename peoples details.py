def getpeoplesdetails():
    print("People Details")
    Name=str(input('Enter a Name: '))
    Email=str(input('Enter a Email: '))
    Age=int(input('Enter Age: '))
    
    if Age>18:
        print("Allowed")
    else:
        print("Not Allowed")

getpeoplesdetails()




    