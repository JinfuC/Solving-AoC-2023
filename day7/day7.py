from functools import cmp_to_key

def camel(part_two=False):
    with open('input.txt') as f:
        lines = f.readlines()

    all_hands = {6:[],5:[], 4:[], 3: [], 2: [], 1:[], 0:[]}
    amount_hands = 0

    for line in lines:
        amount_hands += 1
        hand, pot = line.strip().split(' ')
        pot = int(pot.strip())
        hand_count = {}

        if part_two:
            original_hand = hand
            hand = convert_J(hand)
        
        for card in hand:
            if card in hand_count:
                hand_count[card] = hand_count[card] + 1
            else:
                hand_count[card] = 1
            
        hand_kind = determine_hand(hand_count)
        
        if part_two:
            all_hands[hand_kind].append((original_hand,pot))
        else:
            all_hands[hand_kind].append((hand,pot))

    winnings = 0

    for hands in all_hands.values():
        ranked = sorted(hands, key=cmp_to_key(card_sorting))
        if part_two:
            ranked = sorted(hands, key=cmp_to_key(card_sorting_p2))
        
        for _, pot in ranked:
            winnings += amount_hands * pot
            amount_hands -=1
    if part_two:
        print('The total winnings of part two:', winnings)
    else:
        print('The total winnings of part one:', winnings)
    return 


def determine_hand(hand_count: dict):
    keys = list(hand_count.keys())
    values = list(hand_count.values())
    # high card
    if len(set(keys)) == 5:
        return 0
    # five of a kind
    elif len(set(keys)) == 1:
        return 6
    # four of a kind
    elif 4 in values:
        return 5
    elif 3 in values:
        # full house
        if len(values) == 2:
            return 4
        # three of a kind
        else:
            return 3
    # pairs
    else:
        pairs = 0
        for v in values:
            if v == 2:
                pairs +=1
        if pairs == 2:
            return 2
        elif pairs == 1:
            return 1
        else:
            print('sanity check')
            return 999

def card_sorting(card1, card2):

    mapping = {'A': 1 ,'K': 2 ,'Q':3 ,'J':4 ,'T':5}

    for i in range(0,len(card1[0])):
        if card1[0][i] == card2[0][i]:
            continue
        # both number cards
        elif (card1[0][i] in '23456789' and card2[0][i] in '23456789'):
            if card1[0][i] < card2[0][i]:
                return 1
            else:
                return -1
        # both character cards
        elif (card1[0][i] in 'AKQJT' and card2[0][i] in 'AKQJT'):
            if mapping[card1[0][i]] < mapping[card2[0][i]]:
                return -1
            else:
                return 1
        # one is character other one is number
        else:
            if card1[0][i] in 'AKQJT':
                return -1
            else:
                return 1

def card_sorting_p2(card1, card2):
    mapping = {'A': 1 ,'K': 2 ,'Q':3 ,'T':5}

    for i in range(0,len(card1[0])):
        if card1[0][i] == card2[0][i]:
            continue
        elif (card1[0][i] in '23456789J' and card2[0][i] in '23456789J'):
            
            if card1[0][i] == 'J' or card2[0][i] == 'J':
                l = card1[0][i]
                r = card2[0][i]
                if card1[0][i] == 'J':
                    l = '1'
                if card2[0][i] == 'J':
                    r = '1'
                if l < r:
                    return 1
                else:
                    return -1
            if card1[0][i] < card2[0][i]:
                return 1
            else:
                return -1
        elif (card1[0][i] in 'AKQT' and card2[0][i] in 'AKQT'):
            
            if mapping[card1[0][i]] < mapping[card2[0][i]]:
                return -1
            else:
                return 1
        else:
            
            if card1[0][i] in 'AKQT':
                return -1
            else:
                return 1


def convert_J(hand: str):

    letter_map = {'T':10, 'Q':12, 'K':13, 'A':14}
    reverse_letter_map = {10: 'T', 12: 'Q', 13: 'K', 14: 'A'}

    amount_j = sum([1 if card == 'J' else 0 for card in hand])
    
    if amount_j == 0:
        return hand
    
    else:
        highest_cards = []
        card_count = {}
        for card in hand:
            if card == 'J':
                pass
            elif card in 'TQKA':
                if card in card_count :
                    card_count[card] = card_count[card] + 1
                else:
                    card_count[card] = 1
                    highest_cards.append(letter_map[card])
            else:
                if card in card_count :
                    card_count[card] = card_count[card] + 1
                else:
                    card_count[card] = 1
                    highest_cards.append(int(card))
        highest_cards.sort(reverse=True)
        ordered_cards = []
        for card in highest_cards:
            if card in reverse_letter_map:
                card = reverse_letter_map[card]
            else:
                card = str(card)
            ordered_cards.append(card)
        
        if amount_j == 5:
            return 'AAAAA'
        elif amount_j in [4,3]:
            return hand.replace('J',ordered_cards[0])
        elif amount_j == 2:
            if len(ordered_cards) == 1 or len(ordered_cards) == 3:
                return hand.replace('J',ordered_cards[0])
            else:
                for card,count in card_count.items():
                    if count == 2:
                        return hand.replace('J', card)
        elif amount_j == 1:
            if len(ordered_cards) == 1 or len(ordered_cards) == 4:
                return hand.replace('J',ordered_cards[0])
            elif len(ordered_cards) == 2:
                if card_count[ordered_cards[0]] < card_count[ordered_cards[1]]:
                    return hand.replace('J', ordered_cards[1])
                else:
                    return hand.replace('J', ordered_cards[0])
            else:
                for card,count in card_count.items():
                    if count == 2:
                        return hand.replace('J', card)

camel()
camel(True)