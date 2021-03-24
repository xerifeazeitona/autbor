"""
Mad Libs

Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace
them.

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
"""

from pathlib import Path

def read_template_file(filename):
    """Return the contents of template file as a string."""
    with open(filename) as file_object:
        return file_object.read()

def get_user_input():
    """Prompts user and return a dictionary with the responses."""
    user_input_dic = {}
    user_input_dic['ADJECTIVE'] = input('Enter an adjective: ')
    user_input_dic['NOUN1'] = input('Enter a noun: ')
    user_input_dic['VERB'] = input('Enter a verb (past tense): ')
    user_input_dic['NOUN2'] = input('Enter a noun: ')
    return user_input_dic

def create_mad_libs(template_text, user_input_dic):
    """Replace template contents with user input."""
    new_text = template_text
    for key, value in user_input_dic.items():
        new_text = new_text.replace(key, value)
    return new_text

def _get_file_name():
    """Returns a valid, non existing filename."""
    number = 1
    while True:
        new_file = Path(f'mad_lib_{number}.txt')
        if not new_file.exists():
            break
        number += 1
    return new_file

def save_mad_lib_file(text):
    """Save the mad lib file to a text file."""
    filename = _get_file_name()
    with open(filename, 'w') as file_object:
        file_object.write(text)
    print(f'\nText saved to: {filename}')


template = read_template_file('template.txt')
user_input = get_user_input()
modded_text = create_mad_libs(template, user_input)
print(f'\n{modded_text}')
save_mad_lib_file(modded_text)
