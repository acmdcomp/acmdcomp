import pickle
f=open("try.dat",'ab')
login={}
pickle.dump(login,f)
f.close()
f=open("try.dat",'rb')
try:
    e=pickle.load(f)
    e['rty']=['qwe','frggt',{}]
    print(e)

except EOFError:
    pass
f1=open('try.dat','ab')
pickle.dump(e,f1)
f1.close()
o=open('try.dat','rb')
try:
    e=pickle.load(f)
    print(e)
except EOFError():
    pass
