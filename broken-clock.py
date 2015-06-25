# We have a broken clock. We know how quickly it runs or lags over a
# specific period of time. At first, the clock is set to the correct
# time, but after a while it begins to display an incorrect time... But
# instead of correcting the clock each time, we will use an algorithm to
# calculate the correct time by accounting for the difference compared
# to the actual current time. Of course we will have access to the
# correct time for each day. In addition, you can be certain that the
# correct starting time and current actual time fall on the same
# day. For this mission, time is measured in a 24 hour format.
# You are given three values. The first is the correct starting
# time. The second is the current time displayed on the broken clock
# (which is incorrect). Time is given as strings in the format
# "hh:mm:ss" (Examples: "01:16:59" and "23:00:13"). The third value is a
# description of the clock error in the format "+(-)N [second, minute,
# hour](s) at M [second, minute, hour](s)". For Example "+1 second at 10
# seconds" -- the clock is 1 second fast for every 10 seconds of actual
# time and "-5 minutes at 5 hours" -- the clock lags 5 minutes for every
# 5 hours of actual time.
# You should calculate the real time with the given values. The result
# should be rounded down to the nearest second (use floor or int).
# Input: Three arguments. Correct starting time, current wrong time and
# broken clock descriptions as strings.
# Output: The real time as a string.
# Precondition:
# "wrong_time" is later than "starting_time".

from datetime import time, timedelta, date, datetime

def broken_clock(starting_time, wrong_time, error_description):
    start = time(*[int(t) for t in starting_time.split(':')])
    wrong = time(*[int(t) for t in wrong_time.split(':')])

    start_dt = datetime.combine(date(2000,1,1), start)
    wrong_dt = datetime.combine(date(2000,1,1), wrong)

    gap = wrong_dt - start_dt
    
    err_vals = error_description.split(' ')
    error_size = int(err_vals[0])
    size_unit = err_vals[1]
    error_freq = int(err_vals[3])
    freq_unit = err_vals[4]

    if size_unit[0] == 'm':
        error_size *= 60
    if size_unit[0] == 'h':
        error_size *= 3600

    if freq_unit[0] == 'm':
        error_freq *= 60
    if freq_unit[0] == 'h':
        error_freq *= 3600

    num_cycles = gap.total_seconds()/(error_size + error_freq)

    correct = start_dt + timedelta(seconds = num_cycles * error_freq)
    return correct.strftime('%H:%M:%S')


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
    print broken_clock("03:14:10", "10:20:30", "+4 minutes at 2 hours")
