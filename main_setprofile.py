import sys

def function1():
    print("In function1")
    function2()


def function2():
    print("In function2")


def main_fct():
    function1()


def profile_fct(frame, event, arg):
    """
    https://p403n1x87.github.io/deterministic-and-statistical-python-profiling.html
    :param frame: PyFrame_Object, bears the information about the execution of a code block
    :param event: 'call', 'return', 'c_call', 'c_return', or 'c_exception'
    :param arg: arg depends on event type
    """
    #fn = (frame.f_code.co_filename, frame.f_code.co_firstlineno, frame.f_code.co_name)
    print("event:", event, "  function: ", frame.f_code.co_name)

if __name__ == '__main__':
    sys.setprofile(profile_fct)
    main_fct()
