"""
Table Printer

Write a function named printTable() that takes a list of lists of
strings and displays it in a well-organized table with each column
right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""

def print_table(main_list):
    """
    Displays a list of lists of strings in a well-organized table with
    each column right-justified
    """
    # Create a list to store the max width for each column
    col_widths = [0] * len(main_list)

    # Loop through the list to find out max width for each column
    for i, _ in enumerate(main_list):
        for word in main_list[i]:
            if len(word) > col_widths[i]:
                col_widths[i] = len(word)

    # Loop through the list again, this time printing the table
    for x, _ in enumerate(main_list[0]):
        for y, _ in enumerate(main_list):
            print((main_list[y][x]).rjust(col_widths[y]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
