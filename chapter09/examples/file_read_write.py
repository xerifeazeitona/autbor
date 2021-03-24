from pathlib import Path

# you can use Path to create files
p = Path('spam.txt')
p.write_text('Hello. world!')
p.read_text()

# however you can also use the methods from the internal library
# to achieve the same result
hello_file = open('spam.txt', 'w')
hello_file.write('Hello, world!\n')
hello_file.close()
hello_file = open('spam.txt')
print(hello_file.read())

# the readlines returns a list of string values, one string for each line
sonnet_file = open(Path.home() / 'sonnet29.txt')
sonnet_file.readlines()