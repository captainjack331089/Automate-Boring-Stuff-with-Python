"""
Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
tableData = [
             ['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
            ]

Your printTable() function would print the following:
    apples Alice  dogs
   oranges   Bob  cats
  cherries Carol moose
    banana David goose
"""""

def printTable(data):
    rows = len(data)
    cols = len(data[0])
    newData = [[0] * rows for _ in range(cols)]
    #print(newData)
    for i in range(rows):
        for j in range(cols):
            newData[j][i] = data[i][j]

    _max_l = 0
    for i in range(len(newData)):
        l = 0
        for j in range(len(newData[0])):
            l += len(newData[i][j])
        _max_l = max(_max_l, l)
    _max_l += len(newData[0])
    #print(_max_l)

    temp = ''
    for i in newData:
        temp += (str(' '.join(i))).rjust(_max_l) + '\n'
    return(temp)

if __name__ == '__main__':
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    print(printTable(tableData))
