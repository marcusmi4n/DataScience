print('             No.1 - Hobbies              ')

hobbies = ['anime', 'eating', 'swimming', 'games']

friend = ['eating', 'cooking', 'washing']

print('My hobbies:', hobbies)
print('Friend hobbies:', friend)

common = []
for hobby in hobbies:
    if hobby in friend:
        common.append(hobby)

print('Common hobbies:', common)

unique_mine = []
for hobby in hobbies:
    if hobby not in friend:
        unique_mine.append(hobby)

unique_friend = []
for hobby in friend:
    if hobby not in hobbies:
        unique_friend.append(hobby)

print('My unique hobbies:', unique_mine)
print('Friend unique hobbies:', unique_friend)


print('             No.2 - SETS                ')

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print('Set A:', A)
print('Set B:', B)

union = A | B
print('Union (A | B):', union)

difference = A - B
print('Difference (A - B):', difference)
