from typing import Tuple


def generate_sawtooth(points: int, turn_point: int) -> Tuple[list[int], list[int]]:
    """Generates two list of integers that can be used to plot a sawtooth shape on a
    scatter plot. The first represents the x values and the second list represents the
    y values for plotting. The first value in each list is 0, representing a point at
    the origin. All subsequent x values increment by 1. All subsequent y values
    increment by 1 until the turn_point, after which they decrement by 1 until 0, then
    repeat until "points" values exist in each list.

    args:
    -points: total count of points in sawtooth, also represents the result list lengths.
    -turn_point: The point at which the sawtooth "turns around". For example, if 10,
        the resulting y value list would have [...8, 9, 10, 9, 8...] and
        [..., 2, 1, 0, 1, 2...] as the two turn around points.

    returns:
    -list of length points to represent x values in sawtooth.
    -list of length points to represent y values in sawtooth."""
    x_return: list[int] = []
    y_return: list[int] = []

    current_y: int = 0
    direction_up: bool = True
    for i in range(points):
        x_return.append(i)
        y_return.append(current_y)
        if direction_up:
            current_y += 1
            if current_y > turn_point:
                current_y = turn_point - 1
                direction_up = False
        else:
            current_y -= 1
            if current_y < 0:
                current_y = 1
                direction_up = True



    return (x_return, y_return)


def test_sawtooth_basic_functionality():
    x_values, y_values = generate_sawtooth(points=10, turn_point=5)
    assert x_values == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert y_values == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]


def test_sawtooth_smallest_case():
    x_values, y_values = generate_sawtooth(points=2, turn_point=1)
    assert x_values == [0, 1]
    assert y_values == [0, 1]


def test_sawtooth_larger_points():
    x_values, y_values = generate_sawtooth(points=15, turn_point=7)
    assert x_values == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert y_values == [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0]


def test_sawtooth_even_larger():
    x_values, y_values = generate_sawtooth(points=27, turn_point=6)
    assert x_values == [i for i in range(27)]
    assert y_values == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        1,
        2,
    ]



if __name__ == '__main__':
    print("Hello World (and Ross)!")
    test_sawtooth_even_larger()
    test_sawtooth_basic_functionality()
    test_sawtooth_smallest_case()
    test_sawtooth_larger_points()
    print("test completed!")