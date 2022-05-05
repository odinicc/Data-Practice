from tqdm import tqdm
from itertools import islice
import pprint
from pathlib import Path
import collections

file_path = "C:\\Users\\ivan\\Documents\\GitHub\\Analyzing-Data-with-Python\\Python_Ex\\baby_names\\"
file_name = "yob1880.txt"
F_names ={}
M_names ={}
Hender = {}
ff_name = file_path + file_name
print(ff_name)


for c_year in tqdm(range(1880,2020)):
    ff_name = file_path + "yob" + str(c_year) + ".txt"
    #print(ff_name)
    inf = open(ff_name, 'r')
    Lines = inf.readlines()
    k = len(Lines)
    for row in range(k):
        words = Lines[row].split(",")
        words[2] = words[2].replace('\n', '')
        #print(words[0], words[1], words[2])
        sex = str(words[1])
        if sex == "M":
            if words[0] in M_names:
                M_names[words[0]] += int(words[2])
            else:
                M_names[words[0]] = int(words[2])

            if words[0] in Hender:
                if Hender[words[0]] == 'F':
                    Hender[words[0]] = 'T'
            else:
                Hender[words[0]] = 'M'
        if sex == "F":
            if words[0] in F_names:
                F_names[words[0]] += int(words[2])
            else:
                F_names[words[0]] = int(words[2])

            if words[0] in Hender:
                if Hender[words[0]] == 'M':
                    Hender[words[0]] = 'T'
            else:
                Hender[words[0]] = 'F'

def sort_by_popularity(names):
    names_sorted = {}
    sorted_keys = sorted(names,key = names.get,reverse = True)
    for w in sorted_keys:
        names_sorted[w] = names[w]
    return names_sorted

M_names_sorted = sort_by_popularity(M_names)
F_names_sorted = sort_by_popularity(F_names)

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

m_items = take(30, M_names_sorted.items())
f_items = take(30, F_names_sorted.items())

pp = pprint.PrettyPrinter(sort_dicts=False)
#pp.pprint(m_items)
#pp.pprint(f_items)
#pp.pprint(Hender)

for i in range(10) :
    year = input("Give me the year ( 0 - for exit) ")
    if int(year) == 0:
        break
    ff_path = file_path + "yob" + str(year) + ".txt"
    path = Path(ff_path)
    if path.is_file() == False:
        print("File for year", year, "don't exist")
    else:
        inf = open(path, 'r')
        Lines = inf.readlines()
        k = len(Lines)
        year_trans_names = collections.defaultdict(dict)
        year_trans_names_2 = collections.defaultdict(dict)
        for row in range(k):
            words = Lines[row].split(",")
            words[2] = words[2].replace('\n', '')
            if Hender[words[0]] == 'T':
                year_trans_names[words[0]][words[1]] = words[2]

        for row in year_trans_names:
            if ("M" in year_trans_names[row]) and ("F" in year_trans_names[row]):
                year_trans_names_2[row] = year_trans_names[row]
        pp.pprint(year_trans_names_2)


