from itertools import  product
from random import shuffle
import itertools as it

suits = ["C","D","H","S"]
ranks = ["2","3","4","5","4","6","7","8","9","J","Q","K","A"]

cards = list(r + s for r,s in product(ranks,suits))
shuffle(cards)

def grouper(n, iterable, fillvalue=None):
    #from itertools import izip_longest
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return it.zip_longest(fillvalue=fillvalue, *args)
    #return izip_longest(fillvalue=fillvalue, *args)


hand = grouper(5, cards)
for i in range(5):
    print next(hand)
