print('             No.1 - SQUARE NUMBERS               ')

for i in range(1, 11):
    print(str(i) + ' squared is ' + str(i * i))

print()
print('             No.2 - SUM OF EVEN NUMBERS               ')

sum_even = 0
for i in range(2, 101, 2):
    sum_even += i

print('Sum of all even numbers between 1 and 100: ' + str(sum_even))
