tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [] 
    for i in range (len(tableData)):
        shmax = (len(max(tableData[i])) + 1) #adds a 'plus one' to make it work the right way.
        colWidths.append(shmax) #adds max length of strings in each list to colWidths list

    spacing = max(colWidths) #finds length of longest string in original table
    
    for a, b, c in zip(tableData[0], tableData[1], tableData[2]):#a fancy zip function
        print(a.rjust(spacing), b.rjust(spacing), c.rjust(spacing))

printTable(tableData)
