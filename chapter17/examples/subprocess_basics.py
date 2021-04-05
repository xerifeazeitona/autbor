import subprocess

# Launching other programs from python
calc_proc = subprocess.Popen('/usr/bin/gnome-calculator')

# The poll() method will return None if the process is still running at
# the time poll() is called. If the program has terminated, it will
# return the process’s integer exit code.
print(calc_proc.poll())
# The wait() method will block until the launched process has terminated.
calc_proc.wait() # Doesn't return until the calculator has been closed
print(calc_proc.poll())

# Passing command line arguments to Popen
# the first item in the list is the path to the program
# all subsequent items are the sys.args for the program
subprocess.Popen(['/usr/bin/gedit', 'hello.txt']).wait()

# You can launch a python script from Python
subprocess.Popen(['/usr/bin/python', 'calc_prod.py'])

# Opening files with default applications
# Linux: xdg-open | Windows: start | macOS: open
with open('hello.txt', 'w') as file_obj:
    file_obj.write('Hello, world!')
subprocess.Popen(['/usr/bin/xdg-open', 'hello.txt'])
