# List of lists where each value in the list is a one character list
# use examples from book to print list values in inverted image
# *note 'end' keyword for print will need to be used to prevent auto next line

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def printGrid(aGrid):
        for j in range(len(aGrid[0])):
                print()
                for i in range(len(aGrid)):
                        print(aGrid[i][j], end='')


printGrid(grid)
