from random import random


# Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple)
def quiz_functions() -> None:
    print("\n\n*** capital_indexes")
    print(capital_indexes("HeLlO"))
    print(capital_indexes("#HeLlO_W0rld!"))
    print("\n\n*** mid")
    print(mid("abc"))
    print(mid("aaaa"))
    print(mid("A"))

    print("\n\n*** online_count")
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    print(online_count(statuses))
    statuses = {
    }
    print(online_count(statuses))
    statuses = {
        "Jim": "offline",
        "Pete": "online",
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    print(online_count(statuses))

    print("\n\n*** random_number")
    print(random_number())
    print(random_number())
    print(random_number())

    print("\n\n*** max_val min_val")
    print(max_val([1,2,3,2,1]))
    new_list = [random_number() for i in range(0,3000)]
    print(max_val(new_list))
    print(max(new_list))
    print(min_val([1,2,3,2,1]))
    print(min_val(new_list))
    print(min(new_list))

    print("\n\n*** only_ints")
    print(only_ints(1,2))
    print(only_ints("a",2.2))
    print(only_ints(1,2.2))
    print(only_ints("a",2))

    print("\n\n*** double_letters")
    print(double_letters("asdf"))
    print(double_letters("assdf"))
    print(double_letters("asdff"))
    print(double_letters("aasdf"))
    print(double_letters("asdfasdfasdfasdfasdfasdfasdf"))

    print("\n\n*** add_dots")
    print(add_dots("test"))
    print(remove_dots(add_dots("test")))

    print("\n\n*** count")
    print(count("ho-tel"))
    print(count("cat"))
    print(count("met-a-phor"))
    print(count("ter-min-a-tor"))


    print("\n\n*** is_anagram")
    print(is_anagram("typhoon", "opython"))
    print(is_anagram("Alice", "Bob"))
    print(is_anagram("Alice", "Bobce"))

    print("\n\n*** flatten")
    print(flatten([[1, 2], [3, 4]]))


    print("\n\n*** largest_difference")
    print(largest_difference([1, 2, 3, 4]))
    print(largest_difference([1, 2, 3]))
    print(largest_difference([1, 2, 3, 4, -10, 35]))


    print("\n\n*** format_number")
    print(format_number(10000))
    print(format_number(1))
    print(format_number(10))
    print(format_number(100))
    print(format_number(1000000000))
    print(format_number(100000000000000))
    print(format_number(1000000))

    stack_numbers_math(3)
    stack_numbers_math(12)
    stack_numbers_math(133)
    print("\n\n*** stack_numbers_print")
    stack_numbers_print(3)
    stack_numbers_print(12)
    stack_numbers_print(133)

    print("\n\n*** list_reshaping")
    list_reshaping("1 2 3 4 5 6 7 8 9")
    list_reshaping("99 98 97 96 95 94 93 92 91")

def capital_indexes(input_str: str) -> list[int]:
    # https://pythonprinciples.com/challenges/Capital-indexes/
    # Capital indexes
    #
    # Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
    #
    # For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
    return_list: list[int] = []

    for i in range(len(input_str)):
        current_character: str = str(input_str[i])
        if current_character.isalpha() and (current_character.upper() == current_character):
            return_list.append(i)

    return return_list

def mid(input_str: str) -> str:
    # https://pythonprinciples.com/challenges/Middle-letter/
    # Middle letter
    #
    # Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
    #
    # For example, mid("abc") should return "b" and mid("aaaa") should return "".
    return_string: str = ""

    string_length: int = len(input_str)
    if string_length % 2 == 1:
        center_index: int = int((string_length - 1) / 2)
        return_string = str(input_str[center_index])

    return return_string

def online_count(input_dict: dict[str,str]) -> int:
    # https://pythonprinciples.com/challenges/Online-status/
    # Online status
    #
    # The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
    #
    # For example, consider the following dictionary:
    #
    # statuses = {
    #     "Alice": "online",
    #     "Bob": "offline",
    #     "Eve": "online",
    # }
    #
    # In this case, the number of people online is 2.
    #
    # Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
    #
    # Your function should return the number of people who are online.

    return_count: int = 0

    for key in input_dict:
        if input_dict[key] == "online":
            return_count = return_count + 1

    return return_count

from random import random
def random_number() -> int:
    # https://pythonprinciples.com/challenges/Randomness/
    # Randomness
    #
    # Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
    #
    # Calling the function multiple times should (usually) return different numbers.
    #
    # For example, calling random_number() some times might first return 42, then 63, then 1.
    random_number_return: int = int(100 * random()) + 1

    return random_number_return

def max_val(input_list: list[int]) -> int:
    return_val: int = -1
    if len(input_list) < 1:
        return return_val

    return_val = input_list[0]
    for item in input_list:
        if item > return_val:
            return_val = item
    return return_val


def min_val(input_list: list[int]) -> int:
    return_val: int = -1
    if len(input_list) < 1:
        return return_val

    return_val = input_list[0]
    for item in input_list:
        if item < return_val:
            return_val = item
    return return_val

def only_ints(param1, param2) -> bool:
    # https://pythonprinciples.com/challenges/Type-check/
    # Type check
    #
    # Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
    #
    # For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
    param1_is_int: bool = type(param1) == int
    param2_is_int: bool = type(param2) == int
    all_params_int: bool = param1_is_int and param2_is_int
    return all_params_int

def double_letters(input_str: str) -> bool:
    # https://pythonprinciples.com/challenges/Double-letters/
    # Double letters
    #
    # The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
    #
    # Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
    has_double_letters: bool = False
    if len(input_str) < 2:
        return has_double_letters
    current_char: str = str(input_str[0])
    next_char: str = str(input_str[1])
    for i in range(1,len(input_str)):
        next_char: str = str(input_str[i])
        if current_char == next_char:
            has_double_letters = True
            return has_double_letters
        else:
            current_char = next_char

    return has_double_letters

def add_dots(input_str: str) -> str:
    # https://pythonprinciples.com/challenges/Adding-and-removing-dots/
    # Adding and removing dots
    #
    # Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
    #
    # Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
    #
    # If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
    #
    # (You may assume that the input to add_dots does not itself contain any dots.)
    input_len: int = len(input_str)
    if input_len < 2:
        return input_str

    return_str_list = []
    for i in range(0, input_len-1):
        return_str_list.append(input_str[i])
        return_str_list.append(".")
    return_str_list.append(input_str[input_len-1])

    return_str: str = ""
    return_str = return_str.join(return_str_list)

    # Alternate single line version
    #return_str = ".".join(str(j) for j in list(input_str))

    return return_str


def remove_dots(input_str: str) -> str:
    return_str_list: list[str] = []
    for i in input_str:
        if str(i) != ".":
            return_str_list.append(i)

    return_str: str = ""
    return_str = return_str.join(return_str_list)

    # Alternate single line version
    #return_str = input_str.replace(".","")

    return return_str

def count(input_str: str) -> int:
    # https://pythonprinciples.com/challenges/Counting-syllables/
    # Counting syllables
    #
    # Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
    #
    # "ho-tel"
    # "cat"
    # "met-a-phor"
    # "ter-min-a-tor"
    #
    # Your function should count the number of syllables and return it.
    #
    # For example, the call count("ho-tel") should return 2.
    syllable_count: int = 0
    if len(input_str) < 1:
        return syllable_count
    syllable_list: list[str] = input_str.split('-')
    return len(syllable_list)

def is_anagram(input_str_1: str, input_str_2: str) -> bool:
    # https://pythonprinciples.com/challenges/Anagrams/
    # Anagrams
    #
    # Two strings are anagrams if you can make one from the other by rearranging the letters.
    #
    # Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
    #
    # For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

    list_input_string_1: list[str] = list(input_str_1.lower())
    list_input_string_2: list[str] = list(input_str_2.lower())

    len1: int = len(list_input_string_1)
    len2: int = len(list_input_string_2)
    if len1 != len2:
        return False  # strings of different lengths can not be anagrams
    if len1 < 1:
        return True  # two empty strings are anagrams
    for i in range(len1):  # pop each char off of string 1, look for it in string 2 and pop it out when found
        char_from_1: str = str(list_input_string_1.pop(0))
        character_matched: bool = False
        for j in range(len1 - i):
            char_from_2: str = str(list_input_string_2[j])
            if char_from_2 == char_from_1:
                list_input_string_2.pop(j)
                character_matched = True
                break
        if character_matched:
            continue
        else:
            return False  # no character in 2 matched the current character in 1, so they are not anagrams
    return True  # all characters have been popped from 1 and all had a matching char in 2

def flatten(list_o_lists: list[list]) -> list:
    # https://pythonprinciples.com/challenges/Flatten-a-list/
    # Write a function that takes a list of lists and flattens it into a one-dimensional list.
    #
    # Name your function flatten. It should take a single parameter and return a list.
    #
    # For example, calling:
    #
    # flatten([[1, 2], [3, 4]])
    #
    # Should return the list:
    #
    # [1, 2, 3, 4]
    return_list: list = []

    for current_list in list_o_lists:
        current_list_length: int = len(current_list)
        for i in range(current_list_length):
            return_list.append(current_list.pop(0))

    return return_list

def largest_difference(num_list: list) -> float:
    # https://pythonprinciples.com/challenges/Minmaxing/
    # Min-maxing
    #
    # Define a function named largest_difference that takes a list of numbers as its only parameter.
    #
    # Your function should compute and return the difference between the largest and smallest number in the list.
    #
    # For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
    #
    # You may assume that no numbers are smaller or larger than -100 and 100.
    return max(num_list) - min(num_list)


def format_number(input_num: int) -> str:
    # https://pythonprinciples.com/challenges/Thousands-separator/
    # Thousands separator
    #
    # Write a function named format_number that takes a non-negative number as its only parameter.
    #
    # Your function should convert the number to a string and add commas as a thousands separator.
    #
    # For example, calling format_number(1000000) should return "1,000,000".
    input_num_str: str = str(input_num)
    num_len: int = len(input_num_str)
    if num_len < 4:
        return input_num_str
    return_num_str: str = ""
    input_num_str_list: list[str] = list(input_num_str)
    num_group_count: int = 0
    for i in range(num_len - 1, -1, -1):
        if num_group_count == 3:
            return_num_str = "," + return_num_str
            num_group_count = 0
        return_num_str = str(input_num_str_list[i]) + return_num_str
        num_group_count += 1
    return return_num_str

def stack_numbers_math(n: int) -> None:
    '''
    https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
    The included code stub will read an integer, n, from STDIN.

    Without using any string methods, try to print the following:
    123...n

    Note that "..." represents the consecutive values in between.

    Example
    n=5
    Print the string
    12345
    .
    Input Format
    The first line contains an integer n

    Constraints
    1 <= n <= 150

    Output Format
    Print the list of integers from 1 through n as a string, without spaces.

    Sample Input 0
    3
    Sample Output 0
    123
    '''
    digits = 1
    if n > 9 and n < 100:
        digits = 2
    if n > 99 and n < 1000:
        digits = 3

    final_sum = 0
    columns = 0
    for i in range(n, 0, -1):
        current_number = i * 10 ** columns
        # print(current_number)
        final_sum += current_number
        digits = 1
        if i > 9 and i < 100:
            digits = 2
        if i > 99 and i < 1000:
            digits = 3
        columns += digits

    print(final_sum)

def stack_numbers_print(n: int) -> None:
    '''
    https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
    The included code stub will read an integer, n, from STDIN.

    Without using any string methods, try to print the following:
    123...n

    Note that "..." represents the consecutive values in between.

    Example
    n=5
    Print the string
    12345
    .
    Input Format
    The first line contains an integer n

    Constraints
    1 <= n <= 150

    Output Format
    Print the list of integers from 1 through n as a string, without spaces.

    Sample Input 0
    3
    Sample Output 0
    123
    '''
    for i in range(1,n+1):
        print(i, end="")
    print("")

def list_reshaping(n: str) -> None:
    '''
    https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
    	shape

	The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

	(a). Using shape to get array dimensions

	import numpy

	my__1D_array = numpy.array([1, 2, 3, 4, 5])
	print my_1D_array.shape     #(5,) -> 1 row and 5 columns

	my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
	print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns

	(b). Using shape to change array dimensions

	import numpy

	change_array = numpy.array([1,2,3,4,5,6])
	change_array.shape = (3, 2)
	print change_array

	#Output
	[[1 2]
	[3 4]
	[5 6]]

	reshape

	The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

	import numpy

	my_array = numpy.array([1,2,3,4,5,6])
	print numpy.reshape(my_array,(3,2))

	#Output
	[[1 2]
	[3 4]
	[5 6]]

	Task

	You are given a space separated list of nine integers. Your task is to convert this list into a
	X

	NumPy array.

	Input Format

	A single line of input containing

	space separated integers.

	Output Format

	Print the
	X

	NumPy array.

	Sample Input

	1 2 3 4 5 6 7 8 9

	Sample Output

	[[1 2 3]
	 [4 5 6]
	 [7 8 9]]

    '''
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import numpy
    #n = str(input())
    input_list = n.split(" ")
    input_list_int = []
    for i in input_list:
        input_list_int.append(int(i))
    #print(input_list_int)
    change_array = numpy.array(input_list_int)
    #print(change_array)
    change_array.shape = (3,3)
    print(change_array)

def list_transpose(input_list: list[str]) -> None:
    '''

    	We can generate the transposition of an array using the tool numpy.transpose.
	It will not affect the original array, but it will create a new array.

	import numpy

	my_array = numpy.array([[1,2,3],
	                        [4,5,6]])
	print numpy.transpose(my_array)

	#Output
	[[1 4]
	 [2 5]
	 [3 6]]

	Flatten

	The tool flatten creates a copy of the input array flattened to one dimension.

	import numpy

	my_array = numpy.array([[1,2,3],
	                        [4,5,6]])
	print my_array.flatten()

	#Output
	[1 2 3 4 5 6]

	Task

	You are given a
	X integer array matrix with space separated elements ( = rows and

	= columns).
	Your task is to print the transpose and flatten results.

	Input Format

	The first line contains the space separated values of
	and .
	The next lines contains the space separated elements of

	columns.

	Output Format

	First, print the transpose array and then print the flatten.

	Sample Input

	2 2
	1 2
	3 4

	Sample Output

	[[1 3]
	 [2 4]]
	[1 2 3 4]

    '''
    import numpy

    '''
    n_by_m = input()
    n_by_m_list = n_by_m.split(" ")
    # TODO: should check inputs rather than assume
    n = int(n_by_m_list[0])
    m = int(n_by_m_list[1])
    list_o_lists = []
    for i in range(n):
        next_list = []
        line = input()
        row_list = line.split(" ")
        for item in row_list:
            next_list.append(int(item))
        list_o_lists.append(next_list)
    '''
    n_by_m: str = input_list.pop()
    n_by_m_list: list = n_by_m.split(" ")
    # TODO: should check inputs rather than assume
    n: int = int(n_by_m_list[0])
    m: int = int(n_by_m_list[1])
    list_o_lists: list = []
    for i in range(n):
        next_list: list = []
        line = input_list.pop()
        row_list = line.split(" ")
        for item in row_list:
            next_list.append(int(item))
        list_o_lists.append(next_list)

    my_array = numpy.array(list_o_lists)
    # print(my_array)
    print(numpy.transpose(my_array))
    print(my_array.flatten())