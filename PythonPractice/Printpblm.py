# what is the output of the below code?
# print(*objects, sep=' ', end='\n', file=None, flush=False)

#copy the class function here and then keep the breakpoint and debug.
#check the debugger in python (pycon).

#import pdb; pdb.set_trace() to add breakpoint directly to your code.
#import ipdb; pdb.set_trace() to add breakpoint directly to your code.
#invoke python debugger interactively 'python -m pdb hello.py'; break <line number>

import sys

def printtest(*args, **kwargs):
    """The new-style print function from py3k."""
    breakpoint()
    fp = kwargs.pop("file", sys.stdout)
    if fp is None:
        return
    def write(data):
        if not isinstance(data, str):
            data = str(data)
        fp.write(data)
    want_unicode = False
    sep = kwargs.pop("sep", None)
    if sep is not None:
        if isinstance(sep, str):
            want_unicode = True
        elif not isinstance(sep, str):
            raise TypeError("sep must be None or a string")
    end = kwargs.pop("end", None)
    if end is not None:
        if isinstance(end, str):
            want_unicode = True
        elif not isinstance(end, str):
            raise TypeError("end must be None or a string")
    if kwargs:
        raise TypeError("invalid keyword arguments to print()")
    if not want_unicode:
        for arg in args:
            if isinstance(arg, str):
                want_unicode = True
                break
    if want_unicode:
        newline = u"\n"
        space = u" "
    else:
        newline = "\n"
        space = " "
    if sep is None:
        sep = space
    if end is None:
        end = newline
    for i, arg in enumerate(args):
        if i:
            write(sep)
        write(arg)
    write(end)

fp = open("C:\\Users\\vasu\\OneDrive\\Documents\\PythonoopsDustinPhilips\\PythonPractice\\test.txt",'a')

nums = ['a', 'b', 'c', 4, 5]
for n in reversed(nums):
    printtest(n, end = " ", sep = "\n", file=fp)
