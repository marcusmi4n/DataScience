print('                No.1 - LIST OF MOVIES               ')

movies = ['one_piece', 'kaiju', 'naruto', 'bleach', 'deathnote']

print('List of the movies : ', movies)

print(' Enter the movie you would like to replace the third one : ')


sec = input()

movies[2] = sec

print('Unsorted movies list : ', movies)

movies.sort()


print('Sorted movies list : ', movies)

print('              No.2 - LIST OF NUMBERS          ')

numbers = [5, 15, 25, 35, 45]

print('Numbers : ', numbers)

numbers.insert(2, 20)


print(' New changed : ', numbers)


numbers.pop()

print('Modified Numbers : ', numbers)