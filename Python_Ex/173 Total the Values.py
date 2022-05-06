def sum_num(num):
    new_num = input("Give me your number( 'E' - for exit) ")
    if new_num == 'E':
        return True
    summ = int(num)+int(new_num)
    print ("Yor sum ", summ)
    sum_num(summ)


sum_num(0)