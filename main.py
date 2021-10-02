# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
'''
#my_str1 = "I learn Python"
#print(my_str1)

#a = 6
#b = 7
#print('a+b=', a+b)
'''
'''
#print('something here')
'''

a = 1.33
b = 2

print('a is {a} and b is {b}, a times b is {a * b:.3f}')

price = 50
balance = 40

if balance >= price:
    print('You can buy this product and your new balance will be balance - price = ', balance - price)
else:
    print('Insufficient funds. Please deposit price - balance =', price - balance)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

answer = raw_input('Do you want to continue? Enter yes or no:')
if answer == "yes":
    print('We\'ll move on')
elif answer == "no":
    print('We\'ll stop')
else:
    print('Invalid answer')

