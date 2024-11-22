from random import random


# Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple)
def codewars_functions() -> None:
    print("\n\n*** codewars_functions")

def is_pangram(st):
    # https://www.codewars.com/kata/545cedaa9943f7fe7b000048/solutions/python?filter=me&sort=best_practice&invalids=false
    # simple brute force approach
    test_chars: str = "abcdefghijklmnopqrstuvwxyz"
    test_st = st.lower()
    for i in test_chars:
        if test_st.find(i) == -1:
            return False
    return True


def is_pangram_other(s):
    import string
    return set(string.ascii_lowercase).issubset(s.lower())


def likes(names):
    # https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python?filter=me&sort=best_practice&invalids=false
    like_text: str = ""
    liker_count: int = len(names)
    if liker_count < 1:
        like_text = "no one likes this"
    elif liker_count == 1:
        like_text = f"{names[0]} likes this"
    elif liker_count == 2:
        like_text = f"{names[0]} and {names[1]} like this"
    elif liker_count == 3:
        like_text = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        like_text = f"{names[0]}, {names[1]} and {liker_count - 2} others like this"

    return like_text

def square_digits(num):
    # https://www.codewars.com/kata/546e2562b03326a88e000020/solutions/python?filter=me&sort=best_practice&invalids=false
    num_str: str = str(num)
    output_values_list: list = []
    for i in num_str:
        output_values_list.append(int(i)**2)
    output_str: str = ""
    for j in output_values_list:
        output_str += str(j)
    return int(output_str)

def find_it(seq):
    check_dict: dict = {}
    for i in seq:
        check_dict[i] = check_dict.get(i,0) + 1
    for key in check_dict:
        if (check_dict[key] % 2) == 1:
            return key
    return None
    '''
    Given an array of integers, find the one that appears an odd number of times.
    
    There will always be only one integer that appears an odd number of times.
    Examples
    
    [7] should return 7, because it occurs 1 time (which is odd).
    [0] should return 0, because it occurs 1 time (which is odd).
    [1,1,2] should return 2, because it occurs 1 time (which is odd).
    [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
    [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
    
    '''

def find_it_other(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

def find_it_other_2(seq):
    return [x for x in seq if seq.count(x) % 2][0]

def get_count(sentence):
    '''
    Return the number (count) of vowels in the given string.

    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    
    The input string will only consist of lower case letters and/or spaces.

    '''
    vowels: str = 'aeiou'
    return_count = 0
    for i in vowels:
        return_count += sentence.count(i)
    return return_count

def get_count_other(s):
    return sum(c in 'aeiou' for c in s)