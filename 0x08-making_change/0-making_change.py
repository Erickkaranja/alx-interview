#usr/bin/usr/python3
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
    coins = sorted(coins, reverse=True)
    count = 0
    while total and total > 0:
        check_count = 0
        for coin in coins:
            check_count = total // coin
            count += check_count
            total -= coin * check_count
            continue
        if total != 0:
            return -1
        return count
    return 0
