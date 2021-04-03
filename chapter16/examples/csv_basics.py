import csv

# A reader object lets you iterate over lines in the CSV file
example_file = open('example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)

# This is how you access the value at a particular row and column
print(example_data[0][0])
print(example_data[0][1])
print(example_data[0][2])
print(example_data[1][1])
print(example_data[6][1])

# For large CSV files, you'll want to use the reader object in a for loop
# NOTE: The reader object can be read only once. To reread the CSV file 
# you must call csv.reader again to create a new reader object
example_file = open('example.csv')
example_reader = csv.reader(example_file)
for row in example_reader:
    print(f'Row #{example_reader.line_num} {row}')

# A writer object lets you write data to a CSV file
output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])
output_file.close()

# The delimiter and linetwrminator arguments
csv_file = open('example.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['apples', 'oranges', 'grapes'])
csv_writer.writerow(['eggs', 'bacon', 'ham'])
csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csv_file.close()

# For CSV files that contain header rows, it's more convinient to work
# with the DictReader and DictWriter CSV objects
# The DictReader object sets row to a dictionary object with keys
# derived fomr the headers in the first row
example_file = open('exampleWithHeader.csv')
example_dict_reader = csv.DictReader(example_file)
for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

# If you use DictReader on a CSV file that has no headers, you can
# supply your own
example_file = open('example.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])

# DictWriter objecs use dictionaries to create CSV files
# Notice that the order is irrelevant
# Also any missing keys will be empty in the CSV file
output_file = open('output.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['name', 'pet', 'phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()
