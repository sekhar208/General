import os.path
from collections import Counter

# inp_file = input("Input file: ")
inp_file = "D:/dev/python/General/input_golden_crown.txt"

if os.path.isfile(inp_file) is False:
    print("File doesn't exist")

kingdom = {'SPACE': 'Gorilla',
           'LAND': 'Panda',
           'WATER': 'Octopus',
           'ICE': 'Mammoth',
           'AIR': 'Owl',
           'FIRE': 'Dragon'
           }


def decipher(mystr, dkey):
    if (ord(mystr) - dkey) < 65:
        myord = ord(mystr) + 26 - dkey
    else:
        myord = ord(mystr) - dkey
    return chr(myord)


with open(inp_file, 'r') as fh:
    inlines = fh.readlines()
    ally = []
    for each in inlines:
        if each == "\n":
            continue
        ruler, msg = each.split(' ', 1)
        msg = msg.rstrip('\n').rstrip('\r')

        counter_list = Counter(kingdom[ruler].upper())

        decipher_key = len(kingdom[ruler])
        final_list = list(map(lambda x: decipher(x, decipher_key), msg))
        final_counter = Counter(final_list)
        check = all(map(lambda x: x in final_counter and final_counter[x] >= counter_list[x], counter_list))
        if check is True:
            ally.append(ruler)

    if len(ally) >= 3:
        print("SPACE", " ".join(ally))
    else:
        print("None")