import re
import sys


# Python Function use and behavior
def demonstrate_string_manipulation() -> None:
    demonstrate_strip_and_index(" string-a-ling-ling ")
    demonstrate_split_and_replace(" lorem ipsum dolor ", "ipsum")
    print(capital_indexes("My Name Is Inigo MonToya!"))
    csv_swap_2_and_3(["1,2,3,4,5", "a,b,c,d,e"])
    csv_swap_2_and_3(["1,\"2,3\",4", "a,b,c,d,e"])

def demonstrate_strip_and_index(str_to_print: str) -> None:
    # Trim strings with .strip
    # Access chars in string using index

    print(f"{len(str_to_print)}: ###{str_to_print}###")
    trimmed_string: str = str_to_print.strip()
    print(f"{len(trimmed_string)}: ###{trimmed_string}###")
    trimmed_string = str_to_print.lstrip()
    print(f"{len(trimmed_string)}: ###{trimmed_string}###")
    trimmed_string = str_to_print.rstrip()
    print(f"{len(trimmed_string)}: ###{trimmed_string}###")

    # Forwards
    for i in range(len(str_to_print)):
        print(str_to_print[i])
    # Backwards
    for i in range((len(str_to_print) - 1), 0, -1):
        print(str_to_print[i])

def demonstrate_split_and_replace(str_to_print: str, str_to_replace: str) -> None:
    # Split the string
    # Replace parts of the string

    print(f"{len(str_to_print)}: ###{str_to_print}###")
    word_list: list[str] = str_to_print.strip().split(" ")
    print(f"word list: length = {len(word_list)}, {word_list}")
    for word in word_list:
        print(word)

    replaced_str: str = str_to_print.replace(str_to_replace, "heartlessly replaced")
    print(f"{len(replaced_str)}: ###{replaced_str}###")

def capital_indexes(in_str: str) -> list[int]:
    print(f"{len(in_str)}: ###{in_str}###")
    capital_list: list[int] = []
    for i in range(len(in_str)):
        i_str: str = str(in_str[i])
        print(i, i_str)
        if i_str.isalpha() and i_str == i_str.upper():
            capital_list.append(i)
    return capital_list

def csv_swap_2_and_3(input_csv: list[str]) -> None:
    print("calling csv_swap_2_and_3 with:", input_csv)
    for line in input_csv:
        csv_line_list: list = parse_csv_line_to_list(line)
        swapped_line_list: list = csv_line_list

        #print(f"{len(csv_line_list)} : {csv_line_list=}")
        list_remainder: list = csv_line_list[3:]
        #print(f"{swapped_line_list=} {list_remainder=}")
        if len(csv_line_list) < 2:
            swapped_line_list: list = csv_line_list
        else:
            swapped_line_list = [csv_line_list[0], csv_line_list[2], csv_line_list[1]] + list_remainder
        #print(f"{swapped_line_list=} {list_remainder=}")
        delim: str = ","
        result_line: str = delim.join([str(ele) for ele in swapped_line_list]) + "\n"
        #print(f"{result_line}")
        sys.stdout.write(result_line)

    # output_line: str = ""
    # for input_line in input_csv:
    #     print(f"{input_line=}")
    #     output_line = ""
    #     output_line_list: list = []
    #     first_comma_position: int = input_line.find(",")
    #     first_quote_position: int = input_line.find("\"")
    #
    #     if first_comma_position == -1:
    #         # Case 1, no commas, the entire line is one column/value
    #         output_line = input_line
    #     elif first_quote_position == -1:
    #         # Case 2/3, no quotes,
    #         naive_csv_line_items: list = input_line.split(',')
    #         naive_line_item_count: int = len(naive_csv_line_items)
    #         print(f"{naive_line_item_count=}")
    #         if naive_line_item_count < 2:
    #             output_line = input_line
    #         else:
    #             output_line_list = [naive_csv_line_items[0], naive_csv_line_items[3], naive_csv_line_items[2]]
    #             for i in range(3, naive_line_item_count, 1):
    #                 output_line_list.append(naive_csv_line_items[i])
    #     else:
    #         if first_quote_position < first_comma_position:
    #             # first column is quoted, pop off value to second quote as first column
    #
    #
    #     print(f"{output_line=}")
    #     print(f"{output_line_list=}")
    #
    #
    #     regex_pattern: str = r'(?:^|,)(?=[^"]|(")?)"?((?(1)[^"]*|[^,"]*))"?(?=,|$)'
    #     regex_pattern: str = r'(?:,|\n|^)("(?:(?:"")*[^"]*)*"|[^",\n]*|(?:\n|$))'
    #     regex_pattern: str = r'(?:,"|^")(""|[\w\W]*?)(?=",|"$)|(?:,(?!")|^(?!"))([^,]*?)(?=$|,)|(\r\n|\n)'
    #     csv_line_items: list = re.split(regex_pattern, input_line)
    #     #csv_line_items: list = re.split(r'\W+', input_line)
    #     line_item_count: int = len(csv_line_items)
    #     #print(f"{line_item_count=}")
    #     #for item in csv_line_items:
    #         #print(item)

def parse_csv_line_to_list(input_line: str) -> list:
    #print("parse_csv_line_to_list with ", input_line)
    return_list: list = []
    # base case is an empty string
    if len(input_line) < 1:
        return return_list

    #print(f"checking {input_line=} for initial quote with {input_line[0]}")
    if input_line[0] == "\"":
        # start of quoted string, find the next quote
        close_quote_index: int = input_line[1:].find("\"")
        #print(f"{close_quote_index=}")
        if close_quote_index < 0:
            # This is a failure case, there is no enclosing quote.  You could throw an error, but to continue,
            # just pass the remainder of the string back as the final column.
            return_list.append(input_line)
            return return_list
        else:
            head_value = input_line[:close_quote_index+2]
            remaining_string = input_line[close_quote_index+3:]
            #print(f"pop string and recurse, pop:{head_value} recurse:{remaining_string}")
            return_list = [head_value] + parse_csv_line_to_list(remaining_string)
            return return_list
    else:
        next_comma_index: int = input_line.find(",")
        if next_comma_index < 0:
            # no more commas, the rest of the string is the last value
            return_list.append(input_line)
            return return_list
        else:
            # pop off the next value plus the comma, recurse to end of next column
            head_value = input_line[0:next_comma_index]
            remaining_string = input_line[next_comma_index+1:]
            #print(f"pop and recurse, pop:{head_value} recurse:{remaining_string}")
            return_list = [head_value] + parse_csv_line_to_list(remaining_string)
            return return_list
