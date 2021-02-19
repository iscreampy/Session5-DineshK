from game_rules import *

def play(card_set1, card_set2, mode):
    """This function executes the poker mode. All poker hierachies are implemented.

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2 or tie (if it is a tie game)
    """
    is_four_card = (mode.lower() == 'four card')
    is_three_card = (mode.lower() == 'three card')
    # check against user input to declare winners

    # royal flush
    if royal_flush(card_set1) ^ royal_flush(card_set2):
        if royal_flush(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif royal_flush(card_set1) and royal_flush(card_set2):
        return 'tie'

    # straight flush
    elif straight_flush(card_set1) ^ straight_flush(card_set2):
        if straight_flush(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif straight_flush(card_set1) and straight_flush(card_set2):
        return high_card(card_set1, card_set2)

    # four of a kind
    elif (four_of_kind(card_set1) ^ four_of_kind(card_set2)) and not is_three_card:
        if four_of_kind(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif four_of_kind(card_set1) and four_of_kind(card_set2):
        return four_of_kind_comp(card_set1, card_set2)

    # full_house

    elif (full_house(card_set1) ^ full_house(card_set2)) and not (is_four_card or is_three_card):
        if full_house(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif (full_house(card_set1) and full_house(card_set2)) and not (is_four_card or is_three_card):
        return full_house_comp(card_set1, card_set2)

    # flush
    elif flush(card_set1) ^ flush(card_set2):
        if flush(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif flush(card_set1) and flush(card_set2):
        return high_card(card_set1, card_set2)

    # straight
    elif straight(card_set1) ^ straight(card_set2):
        if straight(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif straight(card_set1) and straight(card_set2):
        return straight_comp(card_set1, card_set2)

    # three of a kind
    elif three_of_kind(card_set1) ^ three_of_kind(card_set2):
        if three_of_kind(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif three_of_kind(card_set1) and three_of_kind(card_set2):
        return full_house_comp(card_set1, card_set2)

    # two pair
    elif (two_pair(card_set1) ^ two_pair(card_set2)) and not is_three_card:
        if two_pair(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif two_pair(card_set1) and two_pair(card_set2):
        return two_pair_comp(card_set1, card_set2)

    # one pair
    elif one_pair(card_set1) ^ one_pair(card_set2):
        if one_pair(card_set1):
            return 'player1'
        else:
            return 'player2'

    elif one_pair(card_set1) and one_pair(card_set2):
        return two_pair_comp(card_set1, card_set2)

    # high card
    else:
        return high_card(card_set1, card_set2)