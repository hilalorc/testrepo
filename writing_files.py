with open('myfile.txt', 'a') as f:
    f.write('\nabc\n')
    f.write('just a 2nd line\n')


with open('configuration.txt', 'r+') as f:
    f.seek(5)
    f.write('100')


