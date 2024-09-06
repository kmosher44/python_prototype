from demonstrate_data_types import demonstrate_data_types


# Python Function use and behavior
def demonstrate_string_manipulation() -> None:
    demonstrate_strip_and_index(" string-a-ling-ling ")

def demonstrate_strip_and_index(str_to_print: str) -> None:
    # Trim strings with .strip
    # Access chars in string using index

    print(f"{len(str_to_print)}: ###{str_to_print}###")
    trimmed_string = str_to_print.strip()
    print(f"{len(trimmed_string)}: ###{trimmed_string}###")

    # Forwards
    for i in range(len(str_to_print)):
        print(str_to_print[i])
    # Backwards
    for i in range((len(str_to_print) - 1), 0, -1):
        print(str_to_print[i])
