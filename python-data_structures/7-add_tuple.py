#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        t_a_first = tuple_a[0]
    else:
        t_a_first = 0
    if len(tuple_a) > 1:
        t_a_second = tuple_a[1]
    else:
        t_a_second = 0
    if len(tuple_b) > 0:
        t_b_first = tuple_b[0]
    else:
        t_b_first = 0
    if len(tuple_b) > 1:
        t_b_second = tuple_b[1]
    else:
        t_b_second = 0

    firsts_sum = t_a_first + t_b_first
    seconds_sum = t_a_second + t_b_second

    result = (firsts_sum, seconds_sum)
    return result
