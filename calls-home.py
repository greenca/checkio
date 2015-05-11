# Each call is represented as a string with date, time and duration of
# the call in seconds in the follow format:
# "YYYY-MM-DD hh:mm:ss duration"
# The date and time in this information are the start of the call.
# Space-Time Communications Co. has several rules on how to calculate
# the cost of calls:
# First 100 (one hundred) minutes in one day are priced at 1 coin per
# minute;
# After 100 minutes in one day, each minute costs 2 coins per minute;
# All calls are rounded up to the nearest minute. For example 59 sec -> 1
# min, 61 sec -> 2 min;
# Calls count on the day when they began. For example if a call was
# started 2014-01-01 23:59:59, then it counted to 2014-01-01;
# Input: Information about calls as a tuple of strings.
# Output: The total cost as an integer.
# Precondition: 0 < len(calls) <= 30
# 0 < call_duration <= 7200
# The bill is sorted by datetime.

import math

def total_cost(calls):
    call_aggregate = {}
    for call in calls:
        call_info = call.split()
        date = call_info[0]
        length = int(math.ceil(float(call_info[2])/60))
        daily_total = call_aggregate.get(date, 0)
        if daily_total + length <= 100:
            call_aggregate[date] = daily_total + length
        elif daily_total <= 100:
            call_aggregate[date] = 100 + (length - (100 - daily_total))*2
        else:
            call_aggregate[date] = daily_total + 2*length
    return sum(call_aggregate.values())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
