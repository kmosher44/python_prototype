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
