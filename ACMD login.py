login={}
ct=0

while True:
    print("Hello! Welcome to the ACMD Database ")
    print("Enter 1 if you are a new user")
    print("Enter 2 if you are an existing user")
    ch=int(input())
    print()
    print("Redirecting.....")

    if ch==1:
        username=input("Enter your username")
        while True:
            if username not in login:
                print("Username not found")
                break
            else:
                if ct<5:
                    passwd=input("Enter your password")
                    if login[username]!=passwd:
                        print("Password doesn't match")
                        ct+=1
                       
            login[username]=passwd
            print("You have logged in successfully!")
    elif ch==2:
        user=input("Enter your username")
        while True:
            for i in login:
                if i==user:
                    print("This user id already exists. Please try again")
                    break
        while True:
            passw=input("Enter your password")
            if len(passw)<8:
                print("The password must have atleast 8 characters.")
            else:
                break
            print("Your account has been created successfully.")
