
coins = [1 , 10 , 25, 50, 100]

def possible_change(total, num_coins):
    if num_coins == 1:
        return total in coins
    else:
        for coin in coins:
            if possible_change(total - coin, num_coins-1):
                return True
        return False

n = 7
summ = 265
final_list = possible_change(summ,n)
print("final_list ",final_list)