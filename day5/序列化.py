import  pickle

a = {"name":"ds","age":18}
c = {"name":"ds","age":18}
b = [1,2,3,4,5,"6",7,"8"]
with open('xuliehua.txt','wb') as f:
    pickle.dump(a,f)
    pickle.dump(c,f)

with open('xuliehua.txt','rb') as f:
    z = pickle.load(f)
    y = pickle.load(f)
print(z)
for i in z:
    print(i)

print(y)
for i in y:
    print(i)