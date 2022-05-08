import random
coins = [1 , 10 , 25, 50, 100]
work_list = []
print(coins)

def finder(work_list,n,summ):
    if len(work_list)<n:
        work_list.append(coins[0])
        finder(work_list, n, summ)
    else:

        Suma = sum(work_list)

        ran = random.randint(0,n-1)
        ran_coin = work_list[ran]
        ran_coin_pos = coins.index(ran_coin)
        #take bigger coin for random coin
        print("Suma - summ" ,Suma - summ)
        if Suma < summ and ran_coin_pos < len(coins)-1:
            coin_pos_bigger = ran_coin_pos + 1
            coin_new = coins[coin_pos_bigger]
            print("ran_coin ", ran_coin, "coin_new bigger ", coin_new)
            work_list[ran] = coin_new
            print("work_list",work_list)
            finder(work_list, n, summ)
        # take smaller coin for random coin
        elif Suma > summ and ran_coin_pos > 1:
            coin_pos_smaller = ran_coin_pos - 1
            coin_new = coins[coin_pos_smaller]
            print("ran_coin " ,ran_coin,"coin_new smaller", coin_new)
            work_list[ran] = coin_new
            print("work_list", work_list)
            finder(work_list, n, summ)
        elif Suma != summ:
            finder(work_list, n, summ)
    return work_list


n = 10
summ = 260
final_list = finder(work_list, n, summ)
print("final_list ",final_list)