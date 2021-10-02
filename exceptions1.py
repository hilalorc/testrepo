a = 9
b = int(input('Enter b:'))

try:
    c = a / b
except ZeroDivisionError as e:
    print('An exception occured!!')
else:
    print('No error')
    print(f'c = {c}')


print('Other code starts here. Continue Execution...')
for x in range(10):
    print(x, end= ' ')

