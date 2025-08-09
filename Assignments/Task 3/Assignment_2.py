print('             No.1 - Number guesser           ')

secret_number = 7

guess = 0
while guess != secret_number:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess == secret_number:
        print('Congratulations! You guessed it!')
    else:
        print('Try again!')

print()
print('             No.2 - Countdown           ')

for i in range(10, 0, -1):
    print(i)
