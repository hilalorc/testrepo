t1 = tuple(range(100))
print(t1)

x = 10
def my_func():
    x = 5
    print('x inside the function:' , x)

my_func()
print('x outside the function:' , x)

a = 10
def my_func1(b):
    global a
    a += b
    print('a inside the function:' , a)

my_func1(7)
print('a outside the function:' , a)


def my_func2():
    print(x)
    x = 8

print(c)
c = 6

my_func2()

print(len('abc'))

def len(x):
    print(x)

len('123456')

del len

print(len('uhjodffdjfdifdjf'))