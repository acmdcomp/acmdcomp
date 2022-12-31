import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', passwd='admin123', autocommit=True)
m=db.cursor()

m.execute('drop database if exists acmd')
m.execute('create database acmd')
m.execute('use acmd')

#Users table
m.execute('drop table if exists users')

m.execute('create table users (Name varchar(25), Age int, Gender varchar(10), Medical_history varchar(100), Family_doctor varchar(25), FD_contactinfo varchar(20), current_disease varchar(25))')
m.execute("insert into users values('Ram', 42,'M','diabetes', 'Anuj','9884558763', 'severe leg pain')")
m.execute("insert into users values('Sundar', 22,'M','NA', 'Anuj','9884545632',NULL)")
m.execute("insert into users values('Manish', 92,'M', 'cataract', 'Kajal','9924356178', NULL)")
m.execute("insert into users values('Kavitha', 67,'F','diabetes', 'Anjana','8876453290',NULL)")
m.execute("insert into users values('Geetha', 35,'F','diabetes', 'Anuj','9887543522',NULL)")

#Drivers table
m.execute('drop table if exists drivers')

m.execute("create table drivers (Name varchar(25), Age int, Gender varchar(10), Rating varchar(10), ME_available varchar(100), LHospital varchar(25))")
m.execute("insert into drivers values ('Raju', 32,'M', '4.8', 'bed, nebuliser', 'Manipal')")
m.execute("insert into drivers values ('Jeeva', 33, 'M', '4.2', 'bed, IV solution set, nebuliser', 'Rainbow')")
m.execute("insert into drivers values ('Sam', 30, 'M', '4.5', 'bed, vaccine, scissors', 'Cloudnine')")
m.execute("insert into drivers values ('Vijaya', 35, 'F', '4.4', 'bed, scissors', 'Manipal')")

db.commit()
print("Enter 'd' if you are a driver and enter 'u' if you are a user")
ud=input('Enter your choice ')
if ud.lower()=='u':
    while True:
        print('Enter 1 if you want to create your profile')
        print('Enter 2 if you want to edit your profile')
        print('Enter 3 if you do not have anything to edit')
        ch=int(input('Enter your choice '))
        if ch==1:
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

        if ch==2:
            print('''1. Update a category
2. Delete a value
3. Delete your profile''')
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
                    #print('Hiiiiiiiiii')
                    #print(m.rowcount)
                    
                elif change=='family doctor':
                    m.execute('update users set Family_doctor=%s where name=%s',(up,nm))
                    
                elif change=='family doctor contact number':
                    m.execute('update users set FD_contactinfo=%s where name=%s',(up,nm))
                    
                
### If they want to change name, what to do?- for both choices- 1 and 2
### For updating, if name doesn't exist, should we check?
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
        if ch==3:
               break

if ud.lower()=='d':
    while True:
        print('Enter 1 if you want to create your profile')
        print('Enter 2 if you want to edit your profile')
        print('Enter 3 if you do not have anything to edit')
        ch=int(input('Enter your choice '))
        if ch==1:
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
            print()

        if ch==2:
            print('''1. Update a category
2. Delete a value
3. Delete your profile''')
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

        if ch==3:
            break
