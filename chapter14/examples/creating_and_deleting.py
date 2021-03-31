import ezsheets

# Create sheet
ss = ezsheets.createSpreadsheet('Multiple Sheets')
ss.sheetTitles
ss.createSheet('Spam') # Create a new sheet at the end of the list
ss.createSheet('Bacon', 0) # Create a sheet at index 0
ss.sheetTitles

# Delete sheet
ss[0].delete()      # Delete the sheet at index 0
ss['Spam'].delete() # Delete the Spam sheet
ss[0].clear()       # Clear all the cells on Sheet1 sheet

# Copying sheets
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1.copyTo(ss2) # Copy the ss1's Sheet1 to ss2 spreadsheet
ss2.sheetTitles # ss2 now contains a copy of ss1's Sheet1