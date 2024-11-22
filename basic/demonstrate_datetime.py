from dateutil import tz
from datetime import date, time, datetime, timedelta

# Fundamental Python Data Storage Types (List, Dictionary, Set, Tuple)
def demonstrate_datetime() -> None:
    demonstrate_now()

    # take a datetime, report the previous day and the next day
    date_list: list[date] = recurring_date_set(date.today(), 14, 10)
    for i in date_list:
        print(i.isoformat())

    # start time now, end time is a lookback window in seconds
    now: datetime = get_local_now().replace(microsecond=0)
    lookback: int = 100000
    print(f"{now.isoformat()=}, {lookback=} seconds, {(lookback_seconds(now, lookback)).isoformat()}")

    # create times list for minutely timeseries
    now: datetime = get_local_now().replace(microsecond=0, second=0)
    datetime_list: list[datetime] = recurring_minute_values(now, 1, 10)
    for i in datetime_list:
        print(i.isoformat())

    # add two sets of timeseries data, discard if unmatched

    # combine two sets of timeseries data, add if duplicated

    # fill sparse series with 0s for missing one minute spots

    # combine 2 timeseries with different timezones

    # combine 2 timeseries over DST from DST and non-DST timezones

    # manipulate dates and times, specify midnight tonight, specific dates

    # convert back and forth from 8601

    # convert back and forth from utc

    # convert back and forth from epoch utc

    # timezone to utc and back over DST

    # create set of dates following different patterns

    # take start date, give date list for recurring dates every 2 weeks for 40 events




def demonstrate_now() -> None:

    print(f"demonstrate_now")
    print(f"datetime.now(): {datetime.now()}")
    print(f"datetime.now().isoformat: {datetime.now().isoformat()}")
    print(f"datetime.now().replace(microsecond=0).isoformat: {datetime.now().replace(microsecond=0).isoformat()}")
    print(f"date.today(): {date.today()}")
    print(f"time(): {time()}")
    now = datetime.now(tz = tz.tzlocal())
    utc_now = datetime.now(tz = tz.UTC)
    print(f"now.tzname(): {now.tzname()}")
    print(f"now: {now}")
    print(f"now.replace(microsecond=0).isoformat: {now.replace(microsecond=0).isoformat()}")
    print(f"now.isoformat: {now.isoformat()}")
    print(f"utc_now: {utc_now}")
    print(f"utc_now.replace(microsecond=0).isoformat: {utc_now.replace(microsecond=0).isoformat()}")
    print(f"utc_now.isoformat: {utc_now.isoformat()}")

def get_utc_now() -> datetime:
    return datetime.now(tz = tz.UTC)

def get_local_now() -> datetime:
    return datetime.now(tz = tz.tzlocal())

def recurring_date_set(starting_date: date, recurrence_gap_days: int, repetitions: int) -> list[date]:
    return_dates: list[date] = [starting_date]
    recurrence_gap: timedelta = timedelta(days=recurrence_gap_days)
    for i in range(repetitions):
        return_dates.append(starting_date + i * recurrence_gap)
    return return_dates

def recurring_minute_values(starting_datetime: date, recurrence_gap_minutes: int, repetitions: int) -> list[datetime]:
    return_dates: list[datetime] = [starting_datetime]
    recurrence_gap: timedelta = timedelta(minutes=recurrence_gap_minutes)
    for i in range(repetitions):
        return_dates.append(starting_datetime + i * recurrence_gap)
    return return_dates

def lookback_seconds(input_datetime: datetime, lookback_seconds: int) -> datetime:
    lookback_timedelta: timedelta = timedelta(seconds=lookback_seconds)
    return (input_datetime - lookback_timedelta)
