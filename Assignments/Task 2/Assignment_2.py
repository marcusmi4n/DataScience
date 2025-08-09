print('             No.1 - STATIONARY               ')

tuple = ['pen', 'pencil', 'eraser']

print('Item borrowed : ')

print('pencil')

tuple.remove('pencil')

print('Enter Item you want to add : ')
item = input()

tuple[1] = item

print('Items :', tuple)



print('                No.2 - STUDENT SCORES               ')

scores = [85, 92, 78, 85, 90, 85]

print('The Score are : ', scores)

count = scores.count(85)

index = scores.index(92)

print('Score 85 appears '+ str(count) +' times.')

print('The first Occurence of score 92 is at index '+ str(index) +' .')