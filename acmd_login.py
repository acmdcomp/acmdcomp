#login-acmd

login={}
ct=0

#inputting choice
# while True:

while True:
    print("Hello! Welcome to the ACMD Database ")
    print("Enter 1 if you are a new user")
    print("Enter 2 if you are an existing user")
    ch=int(input())
    print()
    print("Redirecting.....")

    #new user creation-done
    if ch==1:
        user=input("Create your username ")
        
        for i in login:
            if i==user:
                print("This user id already exists. Please try again")
                break

        while True:
            passw=input("Enter your password ")
            if len(passw)<3:
                print("The password must have atleast 3 characters.")       #to be changed to 8 char, and add alphabet and number
            else:
                login[user]=passw
                
                print("Your account has been created successfully.")
                break
        break
            


    elif ch==2:
        username=input("Enter your username")
        while True:
            if username not in login:
                print("Username not found, please try again! ")
                break
            else:
                if ct<5:
                    passwd=input("Enter your password")
                    if login[username]!=passwd:
                        print("Password doesn't match")
                        ct+=1
                        if ct==5:
                            print("You have exhausted 5 trials. Please begin again!")
                    
                    elif login[username]==passwd:
                        print("You have logged in successfully!")
                        break
    break



        