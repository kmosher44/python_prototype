from demonstrate_data_types import demonstrate_data_types


# Python Function use and behavior
def demonstrate_string_manipulation() -> None:
    demonstrate_strip_and_index(" string-a-ling-ling ")
    demonstrate_split_and_replace(" lorem ipsum dolor ", "ipsum")

def demonstrate_strip_and_index(str_to_print: str) -> None:
    # Trim strings with .strip
    # Access chars in string using index

    print(f"{len(str_to_print)}: ###{str_to_print}###")
    trimmed_string: str = str_to_print.strip()
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