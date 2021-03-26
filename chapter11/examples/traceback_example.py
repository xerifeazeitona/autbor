import traceback
import os

os.chdir(os.path.join(os.getcwd(), 'chapter11/examples'))

try:
    raise Exception('This is the error message.')
except:
    with open('error_info.txt', 'w') as file_obj:
        file_obj.write(traceback.format_exc())
    print('The traceback info was written to error_info.txt')
