import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', passwd='sql123')
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

print('Enter d if you are a driver and enter u if you are a user')
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

        if ch==2:
            print('''1. Update a category
2. Delete a value
3. Delete your profile''')
            chh=int(input('Enter your choice '))
            if chh==1:
                while True:
                    nm=input('Enter your name ')
                    change=input('Enter the name of the category for which you want to change the information- name, age, gender, medical history, family doctor, family doctor contact number ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical history'and change.lower()!='family doctor'and change.lower()!='family doctor contact number':
                        print('Invalid category name ')
                        print()
                    else:
                        break
                if change=='medical history':
                        change='Medical_history'
                elif change=='family doctor':
                        change= 'Family_doctor'
                elif change=='family doctor contact number':
                    change='FD_contactinfo'
                up=input('Enter the updated information ')
### check from here. Field name has to be given separately.
                m.execute('update users set %s=%s where name=%s',(change,up,nm))
                print('Your information has been updated successfully ')
                print()
            if chh==2:
                nm=input('Enter your name ')
                change=input('Enter the name of the category for which you want to delete the information- name, age, gender, medical history, family doctor, family doctor contact number ')
                if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical history'and change.lower()!='family doctor'and change.lower()!='family doctor contact number':
                    print('Invalid category name ')
                    print()
                else:
                    break
                if change=='medical history':
                        change='Medical_history'
                elif change=='family doctor':
                        change= 'Family_doctor'
                elif change=='family doctor contact number':
                    change='FD_contactinfo'
                m.execute('update users set %s=NULL where name=%s',(change,nm))
                print('The data has been deleted successfully.')
            if chh==3:
                nm=input('Enter your name ')
                m.execute('delete from users where name=%s',nm)
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
            m.execute("insert into users values (%s,%s,%s,NULL,%s,%s)",(nm,ag,g,me,lh))
            print('Your profile has been created successfully')
            print()

        if ch==2:
            print('''1. Update a category
2. Delete a value
3. Delete your profile''')
            chh=int(input('Enter your choice '))
            if chh==1:
                while True:
                    nm=input('Enter your name')
                    change=input('Enter the name of the category for which you want to change the information- name, age, gender,medical equipment available,linked hospital ')
                    if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical equipment available' and change.lower()!='linked hospital':
                        print('Invalid category name ')
                    else:
                        break
                    if change=='medical equipment':
                        change='ME_available'
                    elif change=='linked hospital':
                        change= 'LHospital'
                up=input('Enter the updated information')
                m.execute('update users set change=%s where name=%s',(up,nm))
                print('Your information has been updated successfully ')
                print()
            if chh==2:
                nm=input('Enter your name')
                change=input('Enter the name of the category for which you want to delete the information- name, age, gender,medical equipment available,linked hospital ')
                if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical equipment available' and change.lower()!='linked hospital':
                    print('Invalid category name ')
                    print()
                else:
                    break
                if change=='medical equipment':
                    change='ME_available'
                elif change=='linked hospital':
                    change= 'LHospital'
                m.execute('update drivers set %s=NULL where name=%s',(change,nm))
                print('The data has been deleted successfully.')
                print()
            if chh==3:
                nm=input('Enter your name ')
                m.execute('delete from drivers where name=%s',nm)
                print('Your profile has been deleted successfully')
                print()

        if ch==3:
            break
