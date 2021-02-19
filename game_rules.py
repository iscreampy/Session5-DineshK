# check if input is valid

def valid_input(card_set):
    """This function checks if a given card set is in an acceptable format

    Args:
        card_set (list or tuple): input sets should be list of tuples or tuple of tuples
    """
    if isinstance(card_set, list) or isinstance(card_set, tuple):
        for elm in card_set:
            assert isinstance(
                elm, tuple), "valid inputs are list of tuples or tuple of tuples!"


# check if the cards comes from a single deck

def single_deck(card_set1, card_set2):
    """This function checks if given card sets come from the same deck

    Args:
        card_set1 (list or tuple): input sets should be list or tuple
        card_set2 (list or tuple): input sets should be list or tuple

    Returns:
        boolean: returns if card sets are from a single deck
    """
    deck_dict = {}
    for elm in card_set1:
        if elm in deck_dict:
            deck_dict[elm] += 1
        else:
            deck_dict[elm] = 1

    for elm in card_set2:
        if elm in deck_dict:
            deck_dict[elm] += 1
        else:
            deck_dict[elm] = 1

    return max(deck_dict.values()) == 1

# function definitions for poker hierarchies

def flush(card_set):
    """This function checks if given card set results in flush

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains flush
    """
    suits = [suit for value, suit in card_set]
    return len(set(suits)) == 1

def royal_flush(card_set):
    """This function checks if given card sets results in royal flush

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains royal flush
    """
    required_royalflush = ['ace', 'king', 'queen', 'jack', '10']
    if len(card_set) == 4:
        required_royalflush = set(required_royalflush[:4])
    if len(card_set) == 3:
        required_royalflush = set(required_royalflush[:3])
    values = set([value for value, suit in card_set])
    condition = len(values.intersection(required_royalflush)) == len(values)
    return flush(card_set) and condition

def straight_flush(card_set):
    """This function checks if given card set results in straight flush

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains straight flush
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    sorted_values = sorted([rank[value] for value, suit in card_set])
    required_values = list(range(min(sorted_values), max(sorted_values)+1))
    condition = (sorted_values == required_values)
    return flush(card_set) and condition

def four_of_kind(card_set):
    """This function checks if given card set results in four of a kind

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains four of a kind
    """
    values = [value for value, suit in card_set]
    value_counts = [values.count(value) for value in set(values)]
    return 4 in value_counts

def four_of_kind_comp(card_set1, card_set2):
    """This function checks two four of kind card sets and returns the winner

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    values1 = [value for value, suit in card_set1]
    value_counts1 = {value: values1.count(value) for value in set(values1)}
    values2 = [value for value, suit in card_set2]
    value_counts2 = {value: values2.count(value) for value in set(values2)}
    key_list1 = list(value_counts1.keys())
    val_list1 = list(value_counts1.values())
    val1 = key_list1[val_list1.index(4)]
    key_list2 = list(value_counts2.keys())
    val_list2 = list(value_counts2.values())
    val2 = key_list2[val_list2.index(4)]
    if rank[val1] > rank[val2]:
        return 'player1'
    else:
        return 'player2'

def full_house(card_set):
    """This function checks if given card set results in a full house

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains full house
    """
    values = [value for value, suit in card_set]
    value_counts = [values.count(value) for value in set(values)]
    return 3 in value_counts and 2 in value_counts

def full_house_comp(card_set1, card_set2):
    """[summary]

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2
    """

    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

    values1 = [value for value, suit in card_set1]
    value_counts1 = {value: values1.count(value) for value in set(values1)}

    values2 = [value for value, suit in card_set2]
    value_counts2 = {value: values2.count(value) for value in set(values2)}

    key_list1 = list(value_counts1.keys())
    val_list1 = list(value_counts1.values())
    val1 = key_list1[val_list1.index(3)]

    key_list2 = list(value_counts2.keys())
    val_list2 = list(value_counts2.values())
    val2 = key_list2[val_list2.index(3)]

    if rank[val1] > rank[val2]:
        return 'player1'
    else:
        return 'player2'

def straight(card_set):
    """This function checks if given card set results in a straight

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains straight
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    sorted_values = sorted([rank[value] for value, suit in card_set])
    required_values = list(range(min(sorted_values), max(sorted_values)+1))
    return sorted_values == required_values

def straight_comp(card_set1, card_set2):
    """[summary]

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2 or tie (in case of a tie game)
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

    sorted_values1 = sorted([rank[value] for value, suit in card_set1])
    sorted_values2 = sorted([rank[value] for value, suit in card_set2])

    if max(sorted_values1) == max(sorted_values2):
        return 'tie'
    elif max(sorted_values1) > max(sorted_values2):
        return 'player1'
    else:
        return 'player2'

def three_of_kind(card_set):
    """This function checks if given card set results in a three of a kind

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains three of a kind
    """
    values = [value for value, suit in card_set]
    value_counts = [values.count(value) for value in set(values)]
    return 3 in value_counts

def two_pair(card_set):
    """This function checks if given card set results in two pair

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains two pair
    """
    values = [value for value, suit in card_set]
    value_counts = [values.count(value) for value in set(values)]
    return value_counts.count(2) == 2

def two_pair_comp(card_set1, card_set2):
    """[summary]

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

    values1 = [value for value, suit in card_set1]
    value_counts1 = {value: values1.count(value) for value in set(values1)}
    values2 = [value for value, suit in card_set2]
    value_counts2 = {value: values2.count(value) for value in set(values2)}

    needed1 = {k: v for (k, v) in value_counts1.items() if v == 2}
    needed2 = {k: v for (k, v) in value_counts2.items() if v == 2}

    this1 = {k: rank[k] for k, v in needed1.items()}
    this2 = {k: rank[k] for k, v in needed2.items()}

    key_list1 = list(this1.keys())
    val_list1 = list(this1.values())
    val1 = key_list1[val_list1.index(max(val_list1))]

    key_list2 = list(this2.keys())
    val_list2 = list(this2.values())
    val2 = key_list2[val_list2.index(max(val_list2))]

    if rank[val1] > rank[val2]:
        return 'player1'
    else:
        return 'player2'

def one_pair(card_set):
    """This function checks if given card set results in a pair

    Args:
        card_set (list or tuple): card set that a user is holding

    Returns:
        boolean: returns if card set contains a pair
    """
    values = [value for value, suit in card_set]
    value_counts = [values.count(value) for value in set(values)]
    return value_counts.count(2) == 1

def high_card(card_set1, card_set2):
    """This function checks which of the given card sets is the winner

    Args:
        card_set1 (list or tuple): card set that a user is holding
        card_set2 (list or tuple): card set that a user is holding

    Returns:
        string : returns the winner as player1 or player2 or tie (in case of a tie game)
    """
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    sorted_values1 = sorted([rank[value]
                            for value, suit in card_set1], reverse=True)
    sorted_values2 = sorted([rank[value]
                            for value, suit in card_set2], reverse=True)
    for val1, val2 in zip(sorted_values1, sorted_values2):
        if val1 > val2:
            return 'player1'
        elif val2 > val1:
            return 'player2'
        else:
            continue
    return 'tie'