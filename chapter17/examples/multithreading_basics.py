import threading

# Passing arguments to the Thread's target function
print('Cats', 'Dogs', 'Frogs', sep=' & ')
# When threading the above example, 
# - regular arguments can be passed as a list to the "args" 
# - keyword arguments can be passed as a dictionary to the "kwargs"
thread_obj = threading.Thread(
    target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
thread_obj.start()
