"""
Comma Code

Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with and
inserted before the last item. 
For example, passing the previous spam list to the function would return
'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to
it.
Be sure to test the case where an empty list [] is passed to your
function.
"""

def list_stringinator(list_argument):
    """
    Returns a string with all the items separated by a comma and a
    space with 'and' inserted before the last item
    """
    return_string = ''
    for item in list_argument:
        # First item doesn't get anything
        if list_argument.index(item) == 0:
            return_string = item
        # Last item gets a ' and '
        elif list_argument.index(item) == (len(list_argument) - 1):
            return_string = return_string + ' and ' + item
        # All other items get a ', '
        else:
            return_string = return_string + ', ' + item

    return return_string

spam = ['apples', 'bananas', 'tofu', 'cats']
i_like_to_eat = ['apples', 'bananas']
eggs = ['yolk']
sons = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
empty_list = []

print(list_stringinator(spam))
print(list_stringinator(i_like_to_eat))
print(list_stringinator(eggs))
print(list_stringinator(sons))
print(list_stringinator(empty_list))
