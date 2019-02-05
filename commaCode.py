# Make a function that takes a list argument and print the contents in the following way
# aList = ['apples', 'bananas', 'beef', 'cats']
# prints as 'apples, bananas, beef, and cats' (inserted commas and 'and' before last entry
# should work with any size list

aList = ['apples', 'bananas', 'beef', 'cats', 'dogs']


def printcomma(abc):

    for i in range(len(abc)):
        if i == (len(abc) - 1):
            print('and ' + abc[i], end='')

        else:
            print(abc[i] + ', ', end='')


printcomma(aList)
