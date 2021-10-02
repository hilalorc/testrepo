while True:
    guess = input('Guess a lucky number between 1 and 10:')
    if int(guess) == 8:
        print ('You won!')
        break
    print(f'{guess} was not a lucky number.')
