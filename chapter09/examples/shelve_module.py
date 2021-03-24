"""
You can save variables in your Python programs to binary shelf ﬁles
using the shelve module. This way, your program can restore data to
variables from the hard drive.
"""
import shelve

shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

# Your programs can use the shelve module to later reopen and retrieve
# the data from these shelf files.
shelf_file = shelve.open('mydata')
type(shelf_file)
shelf_file['cats']
shelf_file.close()

# Just like dictionaries, shelf values have keys() and values() methods
shelf_file = shelve.open('mydata')
list(shelf_file.keys())
list(shelf_file.values())
shelf_file.close()