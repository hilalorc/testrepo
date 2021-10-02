def my_function1(a, b=10, c=9):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'c is {c}')

#my_function1(6, b=1, c=9)

def f1(a, *args):
    print(f'a:{a}')
    print(f'args: {args}')
    s = a + sum(args)
    print(f'Sum: {s}')


def f2(**x:
    print(x)
    if 'name' in x:
        print(f'Your name is {x ["name"]}')

f1(5, 4, 5, 3, 7, 7, 1, 6)
f2(name='John', age=40, location='London')