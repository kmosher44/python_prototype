from typing import Tuple
from dateutil import tz
from datetime import date, time, datetime, timedelta
import random

def function_to_do_the_datetime_thing(
        start_datetime: datetime,
        data_point_count: int
    ) -> Tuple[list[datetime], list[int]]:
    """Generates a 1-minute frequency timeseries of random integers (a list of times
    and a matching list of integers).

    args:
    -start_datetime: The first time point for the 1-minute frequency timeseries.
    -data_point_count: The number of time/integer values to include in the output.

    returns:
    -list of time points.
    -list of random integers."""
    x_return: list[datetime] = []
    y_return: list[int] = []
    recurrence_gap: timedelta = timedelta(seconds=60)

    for i in range(data_point_count):
        x_return.append(start_datetime + i * recurrence_gap)
        y_return.append(random.randint(1,100))

    return (x_return, y_return)


def test_basic_functionality_local():
    local_now = datetime.now(tz = tz.tzlocal()).replace(microsecond=0)
    x_values, y_values = function_to_do_the_datetime_thing(start_datetime = local_now, data_point_count = 10)
    assert x_values[0] == local_now
    assert len(y_values) == 10
    print(f"\n****Passed test_basic_functionality_local, values:")
    for i in range(len(x_values)):
        print(f"{x_values[i].isoformat()} {y_values[i]}")

def test_basic_functionality_utc():
    utc_now = datetime.now(tz = tz.UTC).replace(microsecond=0)
    x_values, y_values = function_to_do_the_datetime_thing(start_datetime = utc_now, data_point_count = 7)
    assert x_values[0] == utc_now
    assert len(y_values) == 7
    print(f"\n**** Passed test_basic_functionality_utc, values:")
    for i in range(len(x_values)):
        print(f"{x_values[i].isoformat()} {y_values[i]}")


if __name__ == '__main__':
    print("Hello World (and Angela)!")

    test_basic_functionality_local()
    test_basic_functionality_utc()

    print("test completed!")
