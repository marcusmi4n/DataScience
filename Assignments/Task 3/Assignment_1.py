print('             AGE VERIFICATION            ')

age = int(input('Enter your age: '))

if age < 18:
    print('You are a minor.')
elif age <= 64:
    print('You are an adult.')
else:
    print('You are a senior.')

print()
print('             NUMBER CHECKER            ')

number = float(input('Enter a number: '))

if number > 0:
    print('The number is positive.')
elif number < 0:
    print('The number is negative.')
else:
    print('The number is zero.')
