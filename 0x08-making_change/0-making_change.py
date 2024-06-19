#!/usr/bin/python3
"""defining 0-make_change module.
"""


def makeChange(coins, total):
    """returns the minimum number of coins required to give change.
       Args:
          coins(list): list of coins to be provided.
          total: Amount to find change of.
       Returns:
          if total is 0 || < 0 return 0
          if no change can be returned -2
          else count of minimum coins to give change.`
    """
    if total == 0:
        return 0
    if len(coins) == 1 and coins[0] == 1:
        return total
    my_array = [total] * (total + 1)
    my_array[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin < 0:
               break;
            my_array[i] = min(my_array[i], 1 + my_array[i - coin])
    if my_array[total] == total:
        return -1
    return my_array[total]
