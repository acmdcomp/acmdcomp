import pickle
f=open("try.dat",'wb+')
login={}
#login['key1']=['val1','val2']
login={1:"ome",2:"two"}
print(login)
pickle.dump(login,f)

'''
try:
    f.seek(0)
    e=pickle.load(f)
    
    print(e)
 
except EOFError:
    pass
'''
f1=open('try.dat','wb')
login['key1']=['val1','val2']
pickle.dump(login,f1)
f1.close()

try:
    o=open('try.dat','rb')
    
    e=pickle.load(o)
    print(e)
except EOFError():
    pass
