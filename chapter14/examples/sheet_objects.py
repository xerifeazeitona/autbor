"""
The Sheet objects represent the rows and columns of data in each sheet
"""
import ezsheets

ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.sheets      # The sheet objects in this spreadsheet
ss.sheets[0]   # Get the first sheet object in this spreadsheet
ss[0]          # Also get the first sheet object in this spreadsheet
ss.sheetTitles # The titles of all sheet objects in this spreadsheet

# Reading and writing data
sheet = ss[0]
sheet['A1'] = 'Name' # Set the value in cell A1
sheet['A1'] # Get the value in cell A1
sheet['A2'] # Empty cells return a blank string
sheet[1, 1] # Colum 1, Row 1 is the same address as A1

# Column row addressing
ezsheets.convertAddress('A2') # Returns 1, 2
ezsheets.convertAddress(1, 2) # Return A2
ezsheets.getColumnLetterOf(2) # Returns B
ezsheets.getColumnNumberOf('B') # Returns 2

# Reading and Writing entire columns and rows
ss = ezsheets.upload('produceSales.xlsx')
sheet.getRow(1) # The first row is 1, not 0
sheet.getColumn(1)
sheet.getColumn('A') # Same as getColumn(1)
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
column_one = sheet.getColumn(1)
for i, value in enumerate(column_one):
    # Make python list contain uppercase strings
    column_one[i] = value.upper()
sheet.updateColumn(1, column_one) # Update the entire column in one request