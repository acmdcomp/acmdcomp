import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', passwd='sql123')
m=db.cursor()

print('Enter d if you are a driver and enter u if you are a user')
ud=input('Enter your choice ')
if ud.lower()=='u':
    print('Enter 1 if you want to create your profile')
    print('Enter 2 if you want to edit your profile')
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
        
    if ch==2:
        print('''1. Update a category
2. Delete a value
3. Delete your profile''')
        if ch==1:
            while True:
                nm=input('Enter your name')
                change=input('Enter the name of the category for which you want to change the information- name, age, gender, medical history, family doctor, family doctor contact number ')
                if change.lower()!='name' and change.lower()!='age'and change.lower()!='gender'and change.lower()!='medical history'and change.lower()!='family doctor'and change.lower()!='family doctor contact number':
                    print('Invalid category name ')
                else:
                    break
            if change=='medical history':
                    change='Medical_history'
            elif change=='family doctor':
                    change= 'Family_doctor'
            elif change=='family doctor contact number':
                change='FD_contactinfo'
            up=input('Enter the updated information')
            m.execute('update users set change=%s where name=%s',(up,nm))
            print('Your information has been updated successfully ')
        if ch==2:
            passs
## Deletion- 2 and 3

if ud.lower()=='d':
    print('Enter 1 if you want to create your profile')
    print('Enter 2 if you want to edit your profile')
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
        
    if ch==2:
        print('''1. Update a category
2. Delete a value
3. Delete your profile''')
        if ch==1:
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
        if ch==2:
            pass




        
