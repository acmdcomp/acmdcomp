#driver interface

import csv


#login-acmd

flag=''
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
    
        while True:
            username=input("Create your username ")
            if username in login:
                print("Sorry this username is already taken. Try again")
                continue
            else: 
                break
        print()        
        newuser={}
        

        while True:
            password=input("Enter your password ")
            if len(password)<3:
                print("The password must have atleast 3 characters.")       #to be changed to 8 char, and add alphabet and number
            else:
                newuser['password']=password
                
                print("Your account has been created successfully.")
                break
        print()

        ctnew=0
        while ct<5:
            print('-'*len("If you are logging in as an ambulance service provider, please enter 1.")+10)
            print('|', end=' ')
            print("If you are logging in as an ambulance service provider, please enter 1.", end=' ')
            print('|')
            print('|', end=' ')
            print("If you are logging in as a client/victim, please enter 2.")
            print('|')
            print('-'*len("If you are logging in as an ambulance service provider, please enter 1.")+10)
            print()
            prof = input("Please enter your choice. ")
            if prof==1:
                login['profession']='driver'        #driver interface
                flag='driver'
                break
            elif prof==2:
                login['profession']='client'        #client interface
                flag='client'
                break
            else:
                print("Invalid input, please try again!")
                ct+=1
        else:
            print("Sorry you have exhausted 5 trials, please begin again!")
        print()

        login[username]=newuser    

        #logging in of existing users-done
    elif ch==2:
        username=input("Enter your username")
        while True:
            if username not in login:
                print("Username not found, please try again! ")
                break
            else:
                if ct<5:
                    password=input("Enter your password")
                    if login[username]!=password:
                        print("Password doesn't match")
                        ct+=1
                        if ct==5:
                            print("You have exhausted 5 trials. Please begin again!")
                    
                    elif login[username]==password:
                        print("You have logged in successfully!")
                        break
    break





print("Hello welcome to ACMD - Ambulance Contact Management Database! We are here to provide you with\
    immediate solutions in times of medical emergency.")
print("On this platform, you will be able to view the required data for contacting an ambulance for medical\
    purposes.")

if login[username]['profession']=='driver':




