import logging

# if you want to avoid clutter on the screen, you can log to a file
logging.basicConfig(
    filename='my_program.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
