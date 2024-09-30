from demonstrate_data_types import demonstrate_data_types
from demonstrate_functions import demonstrate_functions
from demonstrate_string_manipulation import demonstrate_string_manipulation
from demonstrate_decorator_pattern import demonstrate_decorator_pattern
from quiz_functions import quiz_functions

# TODO: list comprehensions
# TODO: functions - variable passing and value return (incl. pass by ref and return tuple), inc. *args and **kwargs
# TODO: classes
# TODO: file handling
# TODO: database handling
# TODO: logic and control (conditionals, if/else, for and while loops
# TODO: lambda functions
# TODO: regular expressions
# TODO: math (modulo, rounding, random, range etc)

if __name__ == '__main__':
    print("Hello World!")

    isquiz = True

    if isquiz:
        quiz_functions()
    else:
        # Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple)
        demonstrate_data_types()

        # Function Demonstration
        demonstrate_functions()

        # String Manipulation
        demonstrate_string_manipulation()

        demonstrate_decorator_pattern()



