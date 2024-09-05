import typing

# TODO: list comprehensions

# Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple
def demonstrate_data_types():
    demonstrate_list()
    demonstrate_dictionary()

def demonstrate_list():
    # List (ordered, changeable, allows duplicates, access by index demo_list_a[x])

    demo_list_a = [1, 2, 3]
    print(f"demo_list_a has {len(demo_list_a)} items:")
    for list_item in demo_list_a:
        print(list_item)

    demo_list_b = ["a", "b", "c"]
    print(f"demo_list_b has {len(demo_list_b)} items:")
    for list_item in demo_list_b:
        print(list_item)

    demo_list_c = []
    print(f"demo_list_c has {len(demo_list_c)} items:")
    for list_item in demo_list_c:
        print(list_item)
    demo_list_c.append("x")
    demo_list_c.append("y")
    demo_list_c.append("z")
    print(f"demo_list_c has {len(demo_list_c)} items:")
    for list_item in demo_list_c:
        print(list_item)

def demonstrate_dictionary():
    # Dictionary (ordered, changeable, no duplicates, access by key demo_dict_a["key"])

    demo_dict_a = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    print(f"demo_dict_a has {len(demo_dict_a)} items:")
    for dict_key in demo_dict_a:
        print(f"{dict_key} : {demo_dict_a[dict_key]}")

if __name__ == '__main__':
    print("Hello World!")
    demonstrate_data_types()



