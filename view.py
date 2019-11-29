import random

def gen_low_letters():

    list_a = map(chr, range(ord('a'), ord('z') + 1))

    for i in list_a:
        print(i, end=',')
