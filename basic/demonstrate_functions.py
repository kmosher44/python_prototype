
# Python Function use and behavior
def demonstrate_functions() -> None:
    demonstrate_args("string to print", 3)
    print(demonstrate_return_simple("starting string"))
    print(demonstrate_return_tuple("tuple string"))
    pass_by_ref_a: str = "original text"
    demonstrate_pass_by_ref(pass_by_ref_a)
    print(pass_by_ref_a)
    demonstrate_arbitrary_args("a")
    demonstrate_arbitrary_args("a", 2)
    demonstrate_arbitrary_args("a", 3.14, "wombat")

def demonstrate_args(str_to_print: str, repeat_count: int) -> None:
    # Arguments/Parameters

    for i in range(repeat_count):
        print(f"{i}: ", str_to_print)

def demonstrate_return_simple(base_str: str) -> str:
    # Simple Return

    return_string: str = f"the base string is: {base_str}"
    return return_string

def demonstrate_return_tuple(base_str: str) -> tuple[int, float, str]:
    # Tuple Return

    return_tuple: tuple[int, float, str] = (7, 3.14, base_str)
    return return_tuple

def demonstrate_pass_by_ref(pass_by_ref_input: str) -> None:
    # Pass by reference
    # no change for immutable but pointers to changeable objects can have the object they are pointed to updated

    pass_by_ref_input = "modified text"
    # TODO update placeholder with examples of changeable objects changed in function

def demonstrate_arbitrary_args(*all_the_args) -> None:
    # Arbitrary Arguments/Parameters

    print(f"demonstrate_arbitrary_args has {len(all_the_args)} args:")
    print(all_the_args)
    for tuple_item in all_the_args:
        print(tuple_item)