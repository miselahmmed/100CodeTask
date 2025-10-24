#Use random.samnple to pick items from a list

import random

items = list(range(10))

if __name__ == '__main__':
    print("Sample 2 : ", random.sample(items, 3))
    print ("Suffile copy: ", random.sample(items, len(items)))