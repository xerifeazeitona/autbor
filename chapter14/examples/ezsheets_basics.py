import ezsheets

# Creating spreadsheet object from spreadsheet ID
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss
ss.title

# Creating spreadsheet object from spreadsheet title
ss = ezsheets.Spreadsheet('title of my new spreadsheet')
ss
ss.title

# Upload an existing spreadsheet to Google Sheets
ss = ezsheets.upload('my_spreadsheet.xlsx')

# List spreadsheets in your Google account
ezsheets.listSpreadsheets()

# Spreadsheet attibutes
ss.title                # title of the spreadsheet
ss.title = 'Class Data' # Change the title
ss.spreadsheetId        # Unique ID (read only)
ss.url                  # Spreadsheet URL (read only)
ss.sheetTitles          # Titles of all the sheet objects
ss.sheets               # The sheet objects in the spreadsheet
ss[0]                   # The first sheet object in the spreadsheet
ss['students']          # Sheets can also be accessd by title
del ss[0]               # delete the first sheet object in the spreadsheet
ss.refresh()            # send local changes to upstream

# Downloading and Uploading spreadsheets
ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.
# All the above downloadAsX methods support a filename as parameter
ss.downloadAsExcel('a_new_spreadsheet.xlsx')

ss.delete()               # Move spreadsheet to (google) trash
ss.delete(permanent=True) # Permanently delete the spreadsheet