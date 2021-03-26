
def create_sample_data():
    """Creates a couple files to test the program"""
    sample_files = [
        'prefix04-20-1964.spam',
        '11-3-2003suffix.spam',
        'bacon.spam',
        '7-7-2007.spam',
        'invalid10071997dateformat.spam',
        ]

    for sample_file in sample_files:
        with open(sample_file, 'w') as file_obj:
            file_obj.write('sample file for rename_dates.py')

create_sample_data()