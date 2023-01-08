#driver interface

import csv

#login-acmd

login={}
'''login={username:[password, profession, inbox]}
newuser=[password, profession, inbox]'''
inbox=[]
newuser=[]
ct=0


#LOGIN
while True:
    print("Hello! Welcome to the ACMD Database ")
    print("Enter 1 if you are a new user. ")
    print("Enter 2 if you are an existing user. ")
    ch=int(input())
    print()

    #new user creation-done
    if ch==1:
    
        while True:
            username=input("Create your username ")
            if username in login:
                print()
                print("Sorry this username is already taken. Try again")
                continue
            else:
                login[username]=newuser
                break
        print()        
        

        '''
        SQL PROFILE CREATION
        '''
        
        import mysql.connector
        db=mysql.connector.connect(host='localhost', user='root', passwd='sql123', autocommit=True)
        m=db.cursor()

        m.execute('drop database if exists acmd')
        m.execute('create database acmd')   
        m.execute('use acmd')


        #Users table
        m.execute('drop table if exists users')
        m.execute('create table users (Name varchar(25), Age int, Gender varchar(10), Medical_history varchar(100), Family_doctor varchar(25), FD_contactinfo varchar(20), current_disease varchar(25))')



        while True:
            password=input("Enter your password ")
            if len(password)<3:
                print("The password must have atleast 3 characters.")   
                continue
            elif password.isalpha()==True or password.isnumeric()==True:
                print("The password must have alpahbets and numerals")
            else:
                newuser.append(password)
                login[username]=newuser
                print()
                print("Your password has been linked successfully.")
                break
        print()

        ctnew=0
        while ct<5:
            print()
            print("If you are logging in as an ambulance service provider, please enter 1.")
            print("If you are logging in as a client/patient, please enter 2.")
            print()
            loginchoice=int(input("Please enter your choice. "))



            if loginchoice==1:
                newuser.append('driver')        
                login[username]=newuser
##                break - to run program w/o sql


            #'''PROFILE CREATION - DRIVER'''
            nm=input('Enter your name ')
            ag=int(input('Enter your age '))
            g=input('Enter your gender(Enter M for male and F for female) ')
            if g=='m':
                g='M'
            elif g=='f':
                g='F'
            me=input('Enter the medical equipment available in the ambulance ')
            lh=input('Enter the name of the hospital to which you are linked ')
            m.execute("insert into drivers values (%s,%s,%s,NULL,%s,%s)",(nm,ag,g,me,lh))
            
            print('Your profile has been created successfully')
            print()nm=input('Enter your name ')
            ag=int(input('Enter your age '))
            g=input('Enter your gender(Enter M for male and F for female) ')
            if g=='m':
                g='M'
            elif g=='f':
                g='F'
            me=input('Enter the medical equipment available in the ambulance ')
            lh=input('Enter the name of the hospital to which you are linked ')
            m.execute("insert into drivers values (%s,%s,%s,NULL,%s,%s)",(nm,ag,g,me,lh))
            
            print('Your profile has been created successfully')
            print()
              break

                
            elif loginchoice==2:
                newuser.append('client')       
                login[username]=newuser
##                break - to run program w/o sql

                       
                #'''PROFILE CREATION-USER'''  

                nm=input('Enter your name ')
                ag=int(input('Enter your age '))
                g=input('Enter your gender(Enter M for male and F for female) ')
                if g=='m':
                    g='M'
                elif g=='f':
                    g='F'
                md=input('Enter your medical history ')
                fd=input('Enter the name of your family doctor ')
                fdc=input('Enter your family doctor\'s contact number ')
                m.execute("insert into users values (%s,%s,%s,%s,%s,%s,NULL)",(nm, ag,g,md,fd,fdc))
                print('Your profile has been created successfully')
                print()
                db.commit()
                break

                
        else:
            print("Sorry you have exhausted 5 trials, please begin again!")
        print()
        


    #EXISTING USER LOGIN
    elif ch==2:
        username=input("Enter your username")
        while True:
            if username not in login:
                print("Username not found, please try again! ")
                break
            else:
                if ct<5:
                    password=input("Enter your password")
                    if login[username][0]!=password:
                        print("Password doesn't match")
                        ct+=1
                        if ct==5:
                            print("You have exhausted 5 trials. Please begin again!")
                    
                    elif login[username]==password:
                        print("You have logged in successfully!")
                        flag='success'
                        break
    break
    
    

print("Hello welcome to ACMD - Ambulance Contact Management Database! We are here to provide you with immediate solutions in times of medical emergency.")
print("On this platform, you will be able to view the required data for contacting an ambulance for medical purposes.")

#Creating csv file

locfile=open("Location1.csv",'w', newline='')
writer=csv.writer(locfile)
head=['Driver Name', 'Location']
writer.writerow(head)
locfile.close()

locfile=open("Location2.csv",'w', newline='')
writer=csv.writer(locfile)
head=['Client Name', 'Location']
writer.writerow(head)
locfile.close()


#'''LOGIN AS DRIVER'''


if login[username][1]=='driver':
    
    while True:
        print("Enter 1 to input your current location to provide services.")
        print("Enter 2 to view/update your profile on ACMD.")
        print("Enter 3 to view the main menu again.")
        print("Enter 4 to view your inbox.")
        print("Enter 5 to exit ACMD")
        print()
        chasdr=int(input("Please enter your choice "))
        print()

        if chasdr==1:
            locfile=open("Location.csv", 'a+', newline='')
            location=input("Enter your current location ")
            writer=csv.writer(locfile)
            name= username
            inp=[name, location]
            writer.writerow(inp)
            locfile.close()
            continue

        elif chasdr==2:
            print("Enter 1 to update any category in your profile.")
            print("Enter 2 to delete a value.")
            print("Enter 3 to delete your profile.")
            chh=int(input('Enter your choice '))

            if chh==1:
                nm=input('Enter your name ')
                while True:
                    change=input('Enter the name of the category for which you want to change the information- age, gender,medical equipment available,linked hospital ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical equipment available' and change.lower()!='linked hospital':
                        print('Invalid category name ')
                    else:
                        break
                up=input("Enter the new information (If you are updating gender, enter 'M' for male and 'F' for female)")
                if change=='age':
                    m.execute('update drivers set age=%s where name=%s',(up,nm))
                    db.commit()
                elif change=='gender':
                    if up=='m':
                        up='M'
                    elif up=='f':
                        up='F'
                    m.execute('update drivers set gender=%s where name=%s',(up,nm))
                    db.commit()
                elif change=='medical history':
                    m.execute('update drivers set Medical_history=%s where name=%s',(up,nm))
                    db.commit()
                elif change=='medical equipment':
                    m.execute('update drivers set ME_available=%s where name=%s',(up,nm))
                    db.commit()
                elif change=='linked hospital':
                    m.execute('update drivers set LHospital=%s where name=%s',(up,nm))
                    db.commit()
                print('Your information has been updated successfully ')
                print()

            if chh==2:
                nm=input('Enter your name ')
                while True:
                    change=input('Enter the name of the category for which you want to delete the information- age, gender,medical equipment available,linked hospital ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical equipment available' and change.lower()!='linked hospital':
                        print('Invalid category name ')
                        print()
                    else:
                        break
                if change=='age':
                    m.execute('update drivers set age=NULL where name=%s',(nm,))
                    db.commit()
                elif change=='gender':
                    m.execute('update drivers set gender=NULL where name=%s',(nm,))
                    db.commit()
                elif change=='medical equipment':
                    m.execute('update drivers set ME_available=NULL where name=%s',(nm,))
                    db.commit()
                elif change=='linked hospital':
                    m.execute('update drivers set Lhospital=NULL where name=%s',(nm,))
                    db.commit()
                print('The data has been deleted successfully.')
                print()

            if chh==3:
                nm=input('Enter your name ')
                m.execute('delete from drivers where name=%s',(nm,))
                db.commit()
                print('Your profile has been deleted successfully')
                print()


        elif chasdr==3:
            continue


        elif chasdr==4:
            print("Your inbox has", len(inbox), "messages from clients in your location.")
            readch=input("Do you wish to view these messages? Press Y or N ")
            if readch.lower()=='y':
                ctmsg=0
                for i in login:
                    ctmsg+=1
                    print(ctmsg, i)
            profilech=input("Do you wish to contact any of the above clients? Press Y or N ")
            if profilech.lower=='y':
                contact=int(input("Enter the message number you want to pick up "))
                #the linked variable from user will be used here to show sql profile information of THAT user
                messagech=input("Do you wish to enter a costumised message for the client? Press Y or N ")
                if messagech=='y':
                    message=input("Please enter your message to be sent to the driver: ")
                elif messagech=='n':
                    message="The requested driver has been assigned for emergency pick up at the earliest."
                inbox.append(message)
            print("You have successfully been assigned the client in your location. Ensure immediate pickup with required medical equiment.")
                    

        elif chasdr==5:
            break

        else:
            print("Invalid input. Please try again.")
            continue


#'''LOGIN AS USER'''


if login[username][1]=='client':
    while True:
        print()
        print("Enter 1 to input your current location to avail services.")
        print("Enter 2 to view/update your profile on ACMD.")
        print("Enter 3 to view the main menu again.")
        print("Enter 4 to view your inbox.")
        print("Enter 4 to exit ACMD")
        chascl=int(input("Please enter your choice "))
        print()

        if chascl==1:
            locfile=open("Location.csv", 'a+', newline='')
            location=input("Enter your current location ")
            writer=csv.writer(locfile)
            #name=to be input from sql
            inp=['name', location]
            writer.writerow(inp)
            while True:
                print("Enter 1 to contact a driver.")
                print("Enter 2 to exit this menu.")
                print()
                ccl=int(input("Enter your choice "))

                if ccl==1:
                    locfile2=open("Location1.csv", 'r')
                    reader=csv.reader(locfile2)
                    rd=next(reader)
                    for i in head:
                        print(i, end='\t')
                    print()
                    for i in reader:
                        if i[1]==location:
                            print(i[0], i[1], sep='\t')
                    print("These are the drivers in your current location.")
                    dname=input("Enter the name of the driver you wish to contact: ")
                    for i in reader:
                        if i[0].lower()==dname.lower():
                            print("Here are the details of the driver's profile:")
                            #from sql display driver details and to print medical equiment of ambulance from sql also
                    contact=input("Do you wish to proceed to contact the driver? Press Y or N ")
                    if contact.lower=='y':
                        #RIYA SOUND INPUT
                        messagech=input("Do you wish to enter a costumised message for the driver? Press Y or N ")
                        if messagech=='y':
                            message=input("Please enter your message to be sent to the driver: ")
                        elif messagech=='n':
                            message="You have received a client request. They are in location -", location, "and here are their contact details:"   
                        inbox.append(message)
                        #make a linking variable so that the driver can see who sent the message
                    print("You have successfully contacted the driver.")


        elif chascl==2:
            print("Enter 1 to update any category in your profile.")
            print("Enter 2 to delete a value.")
            print("Enter 3 to delete your profile.")
            chh=int(input('Enter your choice '))

            if chh==1:
                nm=input('Enter your name ')    
                while True:
                    change=input('Enter the name of the category for which you want to change the information- age, gender, medical history, family doctor, family doctor contact number ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical history'and change.lower()!='family doctor'and change.lower()!='family doctor contact number':
                        print('Invalid category name ')
                        print()
                    else:
                        break
                up=input("Enter the new information (If you are updating gender, enter 'M' for male and 'F' for female)")
                if change=='age':
                    m.execute('update users set age=%s where name=%s',(up,nm))
                if change=='gender':
                    if up=='m':
                        up='M'
                    elif up=='f':
                        up='F'
                    m.execute('update users set gender=%s where name=%s',(up,nm))
                if change=='medical history':
                    m.execute('update users set Medical_history=%s where name=%s',(up,nm))   
                elif change=='family doctor':
                    m.execute('update users set Family_doctor=%s where name=%s',(up,nm))   
                elif change=='family doctor contact number':
                    m.execute('update users set FD_contactinfo=%s where name=%s',(up,nm))
                print('Your information has been updated successfully ')
                print()

            if chh==2:
                nm=input('Enter your name ')
                while True:
                    change=input('Enter the name of the category for which you want to delete the information- age, gender, medical history, family doctor, family doctor contact number ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical history'and change.lower()!='family doctor'and change.lower()!='family doctor contact number':
                        print('Invalid category name ')
                        print()
                    else:
                        break
                if change=='age':
                    m.execute('update users set age=NULL where name=%s',(nm,))
                if change=='gender':
                    m.execute('update users set gender=NULL where name=%s',(nm,))
                if change=='medical history':
                    m.execute('update users set Medical_history=NULL where name=%s',(nm,))
                elif change=='family doctor':
                    m.execute('update users set Family_doctor=NULL where name=%s',(nm,))
                elif change=='family doctor contact number':
                    m.execute('update users set FD_contactinfo=NULL where name=%s',(nm,))
                print('The data has been deleted successfully.')
                print()
                
            if chh==3:
                nm=input('Enter your name ')
                m.execute('delete from users where name=%s',(nm,))
                print('Your profile has been deleted successfully')
                print()

        
        elif chascl==3:
            continue


        elif chascl==4:
            print("Your inbox has", len(inbox), "messages from drivers you have contacted.")
            readch=input("Do you wish to view these messages? Press Y or N ")
            if readch.lower()=='y':
                ctmsg=0
                for i in login:
                    ctmsg+=1
                    print(ctmsg, i)
                    

        elif chasdr==5:
            break


        else:
            print("Invalid input. Please try again.")
            continue




print("Exiting ACMD.....")
print()
print()
print()
print()
print()
print()
print()
print("You have exited the progam")
print("Thank you for using ACMD. We hope we were able to solve your medical emergency needs. Do consider giving us a google review when you are free and healthy.")
print("We wish to see you again!")
print("Regards, Team ACMD")

            
            
            
        
