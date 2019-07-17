def straight(ranks):					#ranks are compared in straight suits may be different
    if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
        return True
    return False


def flush(suits):					#suits should be same for a flush
    if len(set(suits))==1:
        return True
    return False


def kind(n,ranks):					#to check two or three or four of a kind 'n' represents here the kind to be checked
    for r in ranks:
        if ranks.count(r)==n:
            return r
    return None


def two_pair(ranks):					#to check for pairs
    highcard=kind(2,ranks)
    lowcard=kind(2,tuple(reversed(ranks)))		#tuple(reversed(ranks)) to sort in reversed order
    if highcard != lowcard:
        return (highcard,lowcard)
    return None


def card_ranks(hand):					#to seperate the ranks in hand
    ranks=['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks


def card_suits(hand):					#to seperate the suits in hand
    return [s for r,s in hand]


def poker(hands):					#to compare the different ranks
    return max(hands,key=hand_rank)


def hand_rank(hand):					#comparison key for the different ranks
    ranks=[]
    suits=[]
    ranks=card_ranks(hand)
    suits=card_ranks(hand)

    if straight(ranks) and flush(suits):
        return list(8,max(ranks))

    elif kind(4,ranks):
        return list(7,kind(4,ranks),kind(1,ranks))

    elif kind(3,ranks) and kind(2,ranks):
        return list(6,kind(3,ranks),kind(2,ranks))

    elif flush(suits):
        return list(5,sorted(ranks))

    elif straight(ranks):
        return list(4,max(ranks))

    elif kind(3,ranks):
        return list(3,kind(3,ranks),ranks.remove(kind(3,ranks)))

    elif two_pair(ranks):
        return list(2,two_pair(ranks),kind(1,ranks))

    elif kind(2,ranks):
        return list(1,kind(2,ranks),ranks.remove(kind(2,ranks)))

    else:
        return list(ranks)




if __name__=="__main__":
    assert(straight([6,5,4,3,2])==True)			#for unit testing
    assert(straight([6,5,5,3,2])==False)
    assert(flush(['D','D','D','D','D'])==True)
    assert(kind(2,[6,5,5,3,2])==5)
    assert(two_pair([6,5,5,3,3])==(5,3))
    assert(card_ranks(['6D','TD','AC','JD'])==[14,11,10,6])
    assert(card_ranks(['6D','TD','AC','JD'])==[14,11,10,6])
    assert(card_suits(['6D','TD','AC','JD'])==['D','D','C','D'])
    print(poker([['6C','7D','4C','9S','AS'],['4S','JD','KS','AC','2D']]))
