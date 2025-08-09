print('         ASSIGNMENT TWO          ')
print('Enter your First Name : ')

fn = input()

print('Enter your Last Name : ')

ln = input()

full_name = ( str(fn) + ' ' + str(ln) ).upper()

name_length = len(fn + ln)

print('Hello, ' + full_name + '! Your name has ' + str(name_length) + ' characters.')