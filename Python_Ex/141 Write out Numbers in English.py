

def write_in_eng(st):
    dic = {
        1:"one" ,
        2:"two" ,
        3:"three" ,
        4:"four" ,
        5:"five" ,
        6:"six" ,
        7:"seven" ,
        8:"eight" ,
        9:"nine" ,
        10:"ten" ,
        11:"eleven" ,
        12:"twelve" ,
        13:"thirteen" ,
        14:"fourteen" ,
        15:"fifteen" ,
        16:"sixteen" ,
        17:"seven" ,
        18:"eighteen" ,
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety",
        100:"hundred",
        }
    sta = int(st)
    hundr = sta // 100
    part = sta % 100
    dozens = part // 10
    units = part % 10

    # create 2 number part
    if part < 21:
        z = dic[sta]
    elif part % 10 == 0:
        z = dic[sta]
    else:
        z1 = dic[dozens*10]
        z2 = dic[units]
        z = z1 + "-" + z2

    # add hundreds
    if hundr == 0:
        return z
    elif 0 < hundr < 10:
        z = "(" + dic[hundr] + " hundreds " + z + ")" 
        return z
    
st = input("Give me number ")
y =write_in_eng(st)

print("yor number is", y)
