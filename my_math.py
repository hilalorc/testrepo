a = 10
def my_sum(*args):
    s = 0
    for number in args:
        s = s + number
    return s

if __name__ == '__main__':

    print('Message printed inside my_math.py')
    s = my_sum(10, 20 ,30)
    print(f'sum calculated inside my_math.py is {s}')
else:
    print('this is the else block of code')
    print(f'__name__ inside my_math.py')


    #print(f'__name__ in my_math.py is {__name__}')

