import sys

def function1():
    print("In function1")
    function2()


def function2():
    print("In function2")


def main_fct():
    function1()


def profile_fct(frame, event, arg):
    #fcode = frame.f_code
    #fn = (fcode.co_filename, fcode.co_firstlineno, fcode.co_name)
    print("event:", event, "  function: ", frame.f_code.co_name)

if __name__ == '__main__':
    sys.setprofile(profile_fct)
    main_fct()
