#!/usr/bin/python3
def weight_average(my_list=[]):
    ''' Returns the weighted average'''
    if not my_list:
        return 0

    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return weighted_sum / total_weight if total_weight != 0 else 0
