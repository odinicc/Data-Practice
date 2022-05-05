from collections import defaultdict
import collections

im_lists_temp = {}
dictofdict  = collections.defaultdict(dict)
im_lists = {}


#Function take (3, 3, "pr") and return il3pi3pr 
def get_product_char(current_l,  current_p, current_char):
    st =  "il" + str(current_l) + "pi" + str(current_p) + str(current_char)
    return st

#Function take (1, 2, 3) and return il1pi2cd3
def get_product_cd(current_l,  current_p, current_cd):
    st =  "il" + str(current_l) + "pi" + str(current_p) + "cd" + str(current_cd)
    return st

print("get_product_cd_char(1,  4, 3) ", get_product_cd(1,  4, 3))

# Fill global list im_lists_temp which describe mapping list and products
# "il1nm": "Products on request" , "il3nm": "Products on range"
# Example: im_lists_temp {'1': 'Products on request', '3': 'Products on range'} 

def define_im_lists_temp(msg, im_lists_temp):
    for k in list(msg):
        if (k[0:2] == 'il' and k[3:5] == 'nm'):
            n = k[2]
            im_lists_temp[n]  =  msg[k]
            msg.pop(k)
    return msg, im_lists_temp

print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

# Create dict "dictofdict" where key is list number and value is different product numbers
# List 3 has products 1 3 (cd = 3 4 5) 4(cd = 3 4) , List 1 has products 1, 2.
# dictofdict ={'3': {'1':[], '3':[], '4':[]}, '1': {'1':[], '2':[]}}
# dictofdict ={'3': {'1': [], '3': ['3', '4', '5'], '4': ['3', '4']}, '1': {'1': [], '2': []}}
def create_dictofdict(msg, dictofdict):
# dictofdict ={'3': {'1':[], '3':[], '4':[]}, '1': {'1':[], '2':[]}}
    for key in msg:
        string = str(key)
        if string[0:2] == "il" and string[6:8] == "id":
            il = string[2]
            pi = string[5]
            xi = []
            dictofdict[il][pi] = xi


# dictofdict ={'3': {'1': [], '3': ['3', '4', '5'], '4': ['3', '4']}, '1': {'1': [], '2': []}}
    for key in msg:
        string = str(key)
        if string[0:2] == "il" and string[6:8] == "cd":
            il=string[2]
            pi = string[5]
            cd = string[8]
            try:
                dictofdict[il][pi].append(cd)
            except KeyError:
                print("Warring. Can't transform key", key, "in hit with hit_id = ",msg["hit_id"])
                print("Product with id",pi,"in empression list",il,"doesn't exist")
                pass

    return msg, dictofdict

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#Create lists of products in "r" dictionary
def create_lists_of_products(msg, r):

    im_lists_temp = {}
    dictofdict = collections.defaultdict(dict)
    msg, im_lists_temp = define_im_lists_temp(msg, im_lists_temp)
    msg, dictofdict = create_dictofdict(msg, dictofdict)

    prd = []
    for key_l in dictofdict:
        for key_p in dictofdict[key_l]:
            temp = {}
            temp_list_cd = []

            products = {}
            temp['isImpression'] = True
            temp['impressionList'] = im_lists_temp[key_l]
            temp['productSku'] = msg.pop(get_product_char(key_l, key_p, "id"), None)
            temp['productName'] = msg.pop(get_product_char(key_l, key_p, "nm"), None)
            temp['productPrice'] = msg.pop(get_product_char(key_l, key_p, "pr"), None)
            temp['productBrand'] = msg.pop(get_product_char(key_l, key_p, "br"), None)
            temp['productCategory'] = msg.pop(get_product_char(key_l, key_p, "ca"), None)
            temp['productVariant'] = msg.pop(get_product_char(key_l, key_p, "va"), None)
            temp['position'] = msg.pop(get_product_char(key_l, key_p, "ps"), None)


            for key_cd in dictofdict[key_l][key_p]:
                temp_cd_dic = {}
                temp_cd_dic[key_cd] = msg.pop(get_product_cd(key_l, key_p, key_cd), None)
                temp_list_cd.append(temp_cd_dic)
            temp['customDimensions'] = temp_list_cd
            prd.append(temp)

    r["product"] = prd
    # print("r = " , r)
    return msg, r


def run():
    msg = {'cd1':'cd1_value','cd2':'cd2_value','key':'value', "il1nm": "Products on request",
        "il3nm": "Products on range",
        "il3pi1id": "16214334",
        "il3pi1pr": "476",
        "il1pi1id": "26214334",
        "il3pi3id": "64334",
        "il3pi3pr": "276",
        "il3pi4id": "964334",
        "il1pi2id": "534",
        "il3pi3cd3": "available",
        "il3pi3cd4": "prescription goods",
        "il3pi3cd5": "",
        "il3pi4cd3": "not available",
        "il3pi4cd4": "FMCG",
        "hit_id": "603d4944-dfc7-4862-80a5-0344827b7e7d",
        "il3pi6cd4": "not_FMCG",
        "il3pi7pr": "26214334",

       }
    print("msg = ", msg) 

    r = {'region':'rus'}
    msg, r = create_lists_of_products(msg,r)

    print("msg = ", msg) 

    print("r = ", r)
    
run()
