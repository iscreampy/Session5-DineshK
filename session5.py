# imports
import game_rules
import game_modes
from game_rules import *
from game_modes import *

# 1. creating a deck with lambda, map and zip

vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = tuple(map(lambda v: list(zip([v]*4, suits)), vals))

# 2. write a function without lambda, map and zip to create a deck

def create_deck():
    """Function returns a deck of cards

    Returns:
        tuple of tuples: a single deck of cards as an immutable object
    """
    vals = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = []
    for val in vals:
        for suit in suits:
            tup = (val, suit)
            deck.append(tup)
    return tuple(deck)

# 3.Write a function that, when given 2 sets of 3 or 4 or 5 cards
# (1 game can only have 3 cards with each player or 4 cards or 5 cards per player)
# (1 deck of cards only), (2 players only), can identify who won the game of poker

def card_game(card_set1: 'a tuple of tuples or list of lists',
            card_set2: 'a tuple of tuples or list of lists', *,
            game_mode='poker') -> 'string containing winning player':
    """This function tells which card set is the winner in a 5 card, 4 card and 3 card game

    Args:
        card_set1 (list or tuple): input sets should be list of tuples or tuple of tuples
        card_set2 (list or tuple): input sets should be list of tuples or tuple of tuples
        game_mode (str, optional): choose between four card, three card & poker. Defaults to 'poker'.

    Raises:
        ValueError: raised if unequal number of cards are compared
        ValueError: raised if inappropriate number of cards are compared in an incorrect game mode

    Returns:
        string : the winning player or tie (if it is a tie game)
    """
    valid_input(card_set1)
    valid_input(card_set2)

    assert single_deck(
        card_set1, card_set2), "cards need to belong to a single deck!"

    accepted_modes = ['poker', 'four card', 'three card']
    assert game_mode.lower() in accepted_modes
    if game_mode.lower() == 'poker':
        length_condition = (len(card_set1) == 5) and (len(card_set2) == 5)
        if length_condition:
            returned = play(card_set1, card_set2, game_mode)
            return returned
        else:
            raise ValueError("Poker requires 5 cards for both players!")

    elif game_mode.lower() == 'four card':
        length_condition = (len(card_set1) == 4) and (len(card_set2) == 4)
        if length_condition:
            returned = play(card_set1, card_set2, game_mode)
            return returned
        else:
            raise ValueError("Four card requires 4 cards for both players!")

    elif game_mode.lower() == 'three card':
        length_condition = (len(card_set1) == 3) and (len(card_set2) == 3)
        if length_condition:
            returned = play(card_set1, card_set2, game_mode)
            return returned
        else:
            raise ValueError("Three card requires 3 cards for both players!")

