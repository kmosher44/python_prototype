
# Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple)
def demonstrate_data_types():
    demonstrate_list()
    demonstrate_dictionary()
    demonstrate_tuple()
    demonstrate_set()

def demonstrate_list() -> None:
    # List (ordered, changeable, allows duplicates, access by index demo_list_a[x])

    demo_list_a: list[int] = [1, 2, 3]
    print(f"demo_list_a has {len(demo_list_a)} items:")
    print(demo_list_a)
    for list_item in demo_list_a:
        print(list_item)

    demo_list_b: list[str] = ["a", "b", "c"]
    print(f"demo_list_b has {len(demo_list_b)} items:")
    for list_item in demo_list_b:
        print(list_item)

    demo_list_c: list[str] = []
    print(f"demo_list_c has {len(demo_list_c)} items:")
    for list_item in demo_list_c:
        print(list_item)
    demo_list_c.append("x")
    demo_list_c.append("y")
    demo_list_c.append("z")
    print(f"demo_list_c has {len(demo_list_c)} items:")
    for list_item in demo_list_c:
        print(list_item)

def demonstrate_dictionary() -> None:
    # Dictionary (ordered, changeable, no duplicates, access by key demo_dict_a["key"])

    demo_dict_a: dict[str, int] = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    print(f"demo_dict_a has {len(demo_dict_a)} items:")
    print(demo_dict_a)
    for dict_key in demo_dict_a:
        print(f"{dict_key} : {demo_dict_a[dict_key]}")

def demonstrate_tuple() -> None:
    # Tuple (ordered, unchangeable, allow duplicates, accessed by index demo_tuple_a[x])

    demo_tuple_a: tuple[int, str, float] = (1, "a", 3.14)
    print(f"demo_tuple_a has {len(demo_tuple_a)} items:")
    print(demo_tuple_a)
    for tuple_item in demo_tuple_a:
        print(tuple_item)

def demonstrate_set() -> None:
    # Set (unordered!, unchangeable, no duplicates)

    demo_set_a: set[int] = {1, 2, 3}
    print(f"demo_set_a has {len(demo_set_a)} items:")
    print(demo_set_a)
    for set_item in demo_set_a:
        print(set_item)
