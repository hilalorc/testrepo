def square(x):
    return x**2

print(type(lambda x: x**2))

sq = lambda x=1: x**2

print(sq())

print(sq(5))

s = lambda x, y: x + y

print(s(5,7))

def my_function(x, func):
    return func(x)


y = my_function(5, lambda x: x**2)

print(y)