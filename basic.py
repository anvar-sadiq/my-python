def getFullName(firstName,lastName):
    return firstName+" "+lastName

def main():
    
    firstName=str(input('Enter First Name: '))
    lastName=str(input('Enter Last Name: '))

    fullname=getFullName(firstName,lastName)

    print(fullname)

main()



