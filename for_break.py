for number in range(10):
    if number == 5:
        break
    print(number)

print('instruction outside for loop')

for letter in 'Python':
    print(letter)
    if letter == 'o':
        break

for x in range(1, 12):
    if x % 13 == 0:
        break
else:
    print('There is no number divisible by 13 in the range')