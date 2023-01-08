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

#Creating csv file

locfile=open("Location1.csv",'w', newline='')
writer=csv.writer(file)
head=['Driver Name', 'Location']
writer.writerow(head)
locfile.close()

locfile=open("Location2.csv",'w', newline='')
writer=csv.writer(file)
head=['Client Name', 'Location']
writer.writerow(head)
locfile.close()

if login[username]['profession']=='driver':
    while True:
        print("Enter 1 to input your current location to provide services.")
        print("Enter 2 to view/update your profile on ACMD.")
        print("Enter 3 to view the main menu again.")
        print("Enter 4 to exit ACMD")
        print()
        chasdr=int(input("Please enter your choice "))
        print()
        if chasdr==1:
            locfile=open("Location.csv", 'a+', newline='')
            location=input("Enter your current location ")
            writer=csv.writer(locfile)
            rd=next(header)
            #name=to be input from sql
            inp=[name, location]
            writer.writerow(inp)
            
            
        elif chasdr==2:
            #MANYA-MYSQL
            pass
        elif chasdr==3:
            continue
        elif chasdr==4:
            break

elif login[username]['profession']=='client':
    while True:
        print("Enter 1 to input your current location to avail services.")
        print("Enter 2 to view/update your profile on ACMD.")
        print("Enter 3 to view the main menu again.")
        print("Enter 4 to exit ACMD")
        chascl=int(input("Please enter your choice "))

        if chascl==1:
            locfile=open("Location.csv", 'a+', newline='')
            location=input("Enter your current location ")
            writer=csv.writer(locfile)
            rd=next(header)
            #name=to be input from sql
            inp=[name, location]
            writer.writerow(inp)
            while True:
                print("Enter 1 to view information about client location.")
                print("Enter 2 to exit this menu.")
                print()
                cd=int(input("Enter your choice "))
                if cd==1: