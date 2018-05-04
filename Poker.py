########################################
Poker program
########################################

from collections import defaultdict

hand=['2S','3S','4S','5S','6S']

def One_Pair(hand):
    d=defaultdict(lambda:0)
    number = [i[0] for i in hand]
    for n in number:
        d[n] +=1
    if 2 in d.values():
        return True


def Two_Pair(hand):
    d=defaultdict(lambda:0)
    number = [i[0] for i in hand]
    for n in number:
        d[n] +=1
    if (sorted(d.values())) == [1,1,1,2]:
        return True

def Three_Pair(hand):
    numbers= [value[0] for value in hand]
    numbers_dict=defaultdict(lambda :0)
    for number in numbers:
        numbers_dict[number] += 1
    if sorted(numbers_dict.values()):
        return True

def check_flush(hand):
    values = [i[1] for i in hand]
    if(len(set(values))==1):
        print("card flush")

def check_straight(hand):
    values = [i[0] for i in hand]
    rank_set=set(sorted(map(int,values)))

    if((max(rank_set) - min(rank_set) + 1) == len(rank_set) and len(rank_set) == len(values)):
        print("straight")





result = check_straight(hand)
