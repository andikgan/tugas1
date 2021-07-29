#1. buatlah function yang memiliki variable scope

def a():
    x=3
    print(x)
andik()

x=3
def b():
    y=4
    z=x+y
    print(z)
b()

#2. buatlah function yang memiliki 2 parameter name & age

def c(name,age):
    y=str(age)
    print("nama anda " + name + " dan umur anda " + y);
c("andik",100)

#3. buatlah function yang yang memiliki 2 parameter yang hasilnya perkalian 2 parameter integer tersebut 
def d(a,b):
    c=a*b
    print("a dikali b = ",c)
d(2,5)

def e(a,b,c,d):
    e=a+b+c+d
    f=a*b*c
    print(e)
    print(f)
e(2,3,4,5)

#4. buatlah function yang berfungsi melakukan print sebuah list
def list():
    a=[1,2,3,4]
    print(a)
list()

#5. buatlah function yang berfungsi melakukan print item dalam sebuah list
def item():
    list=[1,2,3,4,5,6,7,8]
    print(list[0:8])
item()

#6. buatlah function yang didalamnya memanggil function lain
def nama():
    print("andik")
    
def kurang():
    nama()
    print("purwanto")
kurang()

#7. butalah function yang didalamnya ada if else
def z():
    a=2
    b=3
    if a>b:
        print('angka yang ketik 1')
    else:
        print('angka lainnya')
z()

#8. buatlah function yang didalamnya ada if else filter umur (misal: age > 15)
def umur():
    x=int(input('masukan angka : '))
    print(x)
    if x>15:
        print('umur anda lebih dr 15')
    elif x<15:
        print('umur ada kurang 15')
    elif x==15:
        print('umur anda 15')
    else:
        print('gada umur')
umur()

#9. butalah function yang didalamnya melakukan print looping item list umur dan pengecekan if else
def listumur():
    umur=[10,20,30]
    for x in umur:
        print(x)
    if x>15:
        print('umur anda lebih dr 15')
    elif x<15:
        print('umur ada kurang 15')
    elif x==15:
        print('umur anda 15')
    else:
        print('gada umur')
listumur()
    