"""
Test file implements tests in pytest.
"""
import inspect
import os.path
import re
import pytest
import session6
from session6 import *

README_CONTENT_CHECK_FOR = [
    'poker',
    'four card',
    'three card',
    'combination',
    'comparison',
    'hierarchy',
    'docstring',
    'annotation',
    'game modes'
]


def test_readme_exists():
    '''
    Test 1 : tests if readme file exists.
    '''
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    '''
    Test 2 : tests if readme file is descriptive enough.
    '''
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    '''
    Test 3 : tests if reame file has all the key functions explained. 
    '''
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    '''
    Test 4 : tests if readme file has proper formatting.
    '''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_fourspace():
    ''' 
    Test 5: Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    '''
    list_of_files = [game_modes, game_rules, session6]
    for file_elm in list_of_files:
        lines = inspect.getsource(file_elm)
        spaces = re.findall('\n +.', lines)
        for space in spaces:
            assert re.search(
                '[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
            assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
                "Your code intentation does not follow PEP8 guidelines"


def test_combinations():
    """
    Test 6 : Poker hierarchies implemented for all three game modes. 
    Exceptions : Fullhouse not implemented in Four card game. 
    Full house, Four of a kind, two pair not implemented in Three card game.
    High card comparisons to be implemented as seperate tests.
    """

    ######### Poker tests #########

    # royal flush vs straight flush (1)
    set1 = [('ace', 'diamonds'), ('queen', 'diamonds'),
            ('jack', 'diamonds'), ('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'),
            ('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # straight flush vs four of a kind (2)
    set1 = [('9', 'diamonds'), ('queen', 'diamonds'),
            ('jack', 'diamonds'), ('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('8', 'clubs'), ('8', 'diamonds'), ('8', 'hearts'),
            ('8', 'spades'), ('queen', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # four of a kind vs full house (3)
    set1 = [('8', 'clubs'), ('8', 'diamonds'), ('8', 'hearts'),
            ('8', 'spades'), ('queen', 'clubs')]
    set2 = [('9', 'diamonds'), ('9', 'clubs'), ('9', 'hearts'),
            ('king', 'diamonds'), ('king', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # full house vs flush (4)
    set1 = [('9', 'diamonds'), ('9', 'clubs'), ('9', 'hearts'),
            ('king', 'diamonds'), ('king', 'clubs')]
    set2 = [('10', 'clubs'), ('8', 'clubs'), ('6', 'clubs'),
            ('3', 'clubs'), ('queen', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # flush vs straight (5)
    set1 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'),
            ('king', 'clubs'), ('queen', 'clubs')]
    set2 = [('9', 'diamonds'), ('8', 'clubs'), ('7', 'hearts'),
            ('6', 'diamonds'), ('5', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # straight vs three of a kind (6)
    set1 = [('4', 'diamonds'), ('8', 'clubs'), ('7', 'hearts'),
            ('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('9', 'clubs'), ('9', 'diamonds'), ('9', 'hearts'),
            ('king', 'clubs'), ('queen', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # three of a kind vs two pair (7)
    set1 = [('9', 'clubs'), ('9', 'diamonds'), ('9', 'hearts'),
            ('king', 'clubs'), ('queen', 'clubs')]
    set2 = [('4', 'diamonds'), ('4', 'clubs'), ('7', 'hearts'),
            ('7', 'diamonds'), ('5', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # two pair vs one pair (8)
    set1 = [('4', 'diamonds'), ('4', 'clubs'), ('7', 'hearts'),
            ('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('9', 'clubs'), ('9', 'diamonds'), ('jack', 'hearts'),
            ('king', 'clubs'), ('queen', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    # one pair vs high card (9)
    set1 = [('9', 'clubs'), ('9', 'diamonds'), ('jack', 'hearts'),
            ('king', 'clubs'), ('queen', 'clubs')]
    set2 = [('4', 'diamonds'), ('2', 'clubs'), ('3', 'hearts'),
            ('7', 'diamonds'), ('5', 'clubs')]
    assert card_game(
        set1, set2) == 'player1', "poker hierarchy rules improperly implemented!"

    ######### Four card game tests #########

    # royal flush vs straight flush (10)
    set1 = [('ace', 'diamonds'), ('queen', 'diamonds'),
            ('jack', 'diamonds'), ('king', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('7', 'clubs'), ('8', 'clubs')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # straight flush vs four of a kind (11)
    set1 = [('queen', 'diamonds'), ('jack', 'diamonds'),
            ('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('8', 'clubs'), ('8', 'diamonds'),
            ('8', 'hearts'), ('8', 'spades')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # four of a kind vs flush (12)
    set1 = [('8', 'clubs'), ('8', 'diamonds'),
            ('8', 'hearts'), ('8', 'spades')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'), ('king', 'clubs')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # flush vs straight (13)
    set1 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'), ('king', 'clubs')]
    set2 = [('9', 'diamonds'), ('8', 'clubs'),
            ('7', 'hearts'), ('6', 'diamonds')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # straight vs three of a kind (14)
    set1 = [('8', 'clubs'), ('7', 'hearts'), ('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('9', 'clubs'), ('9', 'diamonds'),
            ('9', 'hearts'), ('king', 'clubs')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # three of a kind vs two pair (15)
    set1 = [('9', 'clubs'), ('9', 'diamonds'),
            ('9', 'hearts'), ('king', 'clubs')]
    set2 = [('4', 'diamonds'), ('4', 'clubs'),
            ('7', 'hearts'), ('7', 'diamonds')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # two pair vs one pair (16)
    set1 = [('4', 'diamonds'), ('4', 'clubs'),
            ('7', 'hearts'), ('7', 'diamonds')]
    set2 = [('9', 'clubs'), ('9', 'diamonds'),
            ('jack', 'hearts'), ('king', 'clubs')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    # one pair vs high card (17)
    set1 = [('9', 'clubs'), ('9', 'diamonds'),
            ('jack', 'hearts'), ('king', 'clubs')]
    set2 = [('4', 'diamonds'), ('2', 'clubs'),
            ('3', 'hearts'), ('7', 'diamonds')]
    assert card_game(
        set1, set2, game_mode='Four card') == 'player1', "hierarchy rules improperly implemented!"

    ######### Three card game tests #########

    # royal flush vs straight flush (18)
    set1 = [('ace', 'diamonds'), ('queen', 'diamonds'), ('king', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs')]
    assert card_game(
        set1, set2, game_mode='three Card') == 'player1', "hierarchy rules improperly implemented!"

    # straight flush vs flush (19)
    set1 = [('queen', 'diamonds'), ('jack', 'diamonds'), ('king', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs')]
    assert card_game(
        set1, set2, game_mode='three Card') == 'player1', "hierarchy rules improperly implemented!"

    # flush vs straight (20)
    set1 = [('10', 'clubs'), ('9', 'clubs'), ('king', 'clubs')]
    set2 = [('9', 'diamonds'), ('8', 'clubs'), ('7', 'hearts')]
    assert card_game(
        set1, set2, game_mode='Three card') == 'player1', "hierarchy rules improperly implemented!"

    # straight vs three of a kind (21)
    set1 = [('8', 'clubs'), ('7', 'hearts'), ('6', 'diamonds')]
    set2 = [('9', 'clubs'), ('9', 'diamonds'), ('9', 'hearts')]
    assert card_game(
        set1, set2, game_mode='Three Card') == 'player1', "hierarchy rules improperly implemented!"

    # three of a kind vs one pair (22)
    set1 = [('9', 'clubs'), ('9', 'diamonds'), ('9', 'hearts')]
    set2 = [('4', 'diamonds'), ('4', 'clubs'), ('7', 'hearts')]
    assert card_game(
        set1, set2, game_mode='three card') == 'player1', "hierarchy rules improperly implemented!"

def test_highvhigh_fc():
    """
    Test 7: Test if high card hierarchy is implemented correctly (Four card)
    """
    # high card vs high card
    set1 = [('jack', 'diamonds'), ('2', 'hearts'), ('3', 'hearts'),('7', 'diamonds')]
    set2 = [('9', 'diamonds'), ('2', 'clubs'), ('5', 'hearts'),('8', 'diamonds')]
    assert card_game(set1, set2, game_mode='four card') == 'player1', "high card hierarchy not implemented correctly!"

def test_highvhigh_tie_fc():
    """
    Test 8: Test if high card hierarchy is implemented correctly in case of tie
    """
    # high card vs high card - tie
    set1 = [('jack', 'diamonds'), ('2', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('7', 'spades'), ('2', 'clubs'), ('5', 'hearts'),('jack', 'clubs')]
    card_game(set1, set2, game_mode='four card') == 'tie', "high card hierarchy not implemented correctly!"

def test_highvhigh_tc():
    """
    Test 9: Test if high card hierarchy is implemented correctly (Three card)
    """
    # high card vs high card
    set1 = [('jack', 'diamonds'), ('2', 'hearts'), ('3', 'hearts')]
    set2 = [('9', 'diamonds'), ('2', 'clubs'), ('5', 'hearts')]
    assert card_game(set1, set2, game_mode='three card') == 'player1', "high card hierarchy not implemented correctly!"

def test_highvhigh_tie_tc():
    """
    Test 10: Test if high card hierarchy is implemented correctly in case of tie (Three card)
    """
    # high card vs high card - tie
    set1 = [('jack', 'diamonds'), ('2', 'hearts'),('7', 'diamonds')]
    set2 = [('7', 'spades'), ('2', 'clubs'),('jack', 'clubs')]
    assert card_game(set1, set2, game_mode='three card') == 'tie', "high card hierarchy not implemented correctly!"

def test_highvhigh_p():
    """
    Test 11: Test if high card hierarchy is implemented correctly (Poker)
    """
    set1 = [('jack', 'diamonds'), ('2', 'hearts'), ('3', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('9', 'diamonds'), ('2', 'clubs'), ('5', 'hearts'),('8', 'diamonds'), ('7', 'clubs')]
    assert card_game(set1, set2) == 'player1', "high card hierarchy not implemented correctly!"

def test_highvhigh_tie_p():
    """
    Test 12: Test if high card hierarchy is implemented correctly in case of tie (Poker)
    """
    # high card vs high card - tie
    set1 = [('jack', 'diamonds'), ('2', 'hearts'), ('3', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('7', 'spades'), ('2', 'clubs'), ('5', 'hearts'),('jack', 'clubs'), ('3', 'clubs')]
    assert card_game(set1, set2) == 'tie', "high card hierarchy not implemented correctly!"

def test_poker_rand1():
    """
    Test 13: Test if poker hierarchy is implemented correctly (Poker)
    """
    # straight flush vs flush
    set1 = [('9', 'diamonds'), ('queen', 'diamonds'), ('jack', 'diamonds'),('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'),('king', 'clubs'), ('queen', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"
    
def test_poker_tie1():
    """
    Test 14: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # straight flush vs straight flush - tie
    set1 = [('9', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'),('6', 'diamonds'), ('10', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'),('7', 'clubs'), ('8', 'clubs')]
    card_game(set1, set2) == 'tie', "poker hierarchy not implemented correctly"

def test_poker_tie2():
    """
    Test 15: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # straight flush vs straight flush
    set1 = [('9', 'diamonds'), ('queen', 'diamonds'), ('jack', 'diamonds'),('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('6', 'clubs'),('7', 'clubs'), ('8', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie3():
    """
    Test 16: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # four of a kind vs four of a kind
    set1 = [('8', 'clubs'), ('8', 'diamonds'), ('8', 'hearts'),('8', 'spades'), ('queen', 'clubs')]
    set2 = [('7', 'diamonds'), ('7', 'clubs'), ('7', 'hearts'),('7', 'spades'), ('king', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie4():
    """
    Test 17: Test if poker hierarchy is implemented correctly in case of same category(Poker, Named cards)
    """
    # four of a kind vs four of a kind
    set1 = [('king', 'diamonds'), ('king', 'clubs'), ('king', 'hearts'),('king', 'spades'), ('7', 'clubs')]
    set2 = [('jack', 'clubs'), ('jack', 'diamonds'), ('jack', 'hearts'),('jack', 'spades'), ('queen', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie5():
    """
    Test 18: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # fullhouse vs fullhouse
    set1 = [('ace', 'clubs'), ('ace', 'diamonds'), ('ace', 'hearts'),('queen', 'spades'), ('queen', 'clubs')]
    set2 = [('king', 'diamonds'), ('king', 'clubs'), ('king', 'hearts'),('7', 'spades'), ('7', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie6():
    """
    Test 19: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # straight vs straight
    set1 = [('9', 'diamonds'), ('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('4', 'clubs'), ('5', 'diamonds'), ('6', 'hearts'),('7', 'clubs'), ('8', 'spades')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie7():
    """
    Test 20: Test if poker hierarchy is implemented correctly in case of same category(Poker, tie case)
    """
    # straight vs straight
    set1 = [('4', 'diamonds'), ('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('4', 'clubs'), ('5', 'diamonds'), ('6', 'hearts'),('7', 'clubs'), ('8', 'spades')]
    assert card_game(set1, set2) == 'tie', "poker hierarchy not implemented correctly"

def test_poker_tie8():
    """
    Test 21: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # poker tests - tie test
    # three of a kind vs three of a kind
    set1 = [('8', 'diamonds'), ('8', 'clubs'), ('8', 'hearts'),('6', 'diamonds'), ('9', 'clubs')]
    set2 = [('5', 'clubs'), ('5', 'diamonds'), ('5', 'hearts'),('7', 'clubs'), ('8', 'spades')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie9():
    """
    Test 22: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # poker tests - tie test
    # two pair vs two pair
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('king', 'diamonds'), ('jack', 'hearts'),('jack', 'clubs'), ('queen', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_poker_tie10():
    """
    Test 23: Test if poker hierarchy is implemented correctly in case of same category(Poker)
    """
    # poker tests - tie test
    # one pair vs one pair
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('king', 'diamonds'), ('9', 'hearts'),('jack', 'clubs'), ('queen', 'clubs')]
    assert card_game(set1, set2) == 'player1', "poker hierarchy not implemented correctly"

def test_single_deck():
    """
    Test 24: Test if cards of both sets together come from a single deck
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('ace', 'diamonds'), ('9', 'hearts'),('jack', 'clubs'), ('queen', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2)

def test_uneven1():
    """
    Test 25: Test if cards of both sets having unequal cards throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('9', 'hearts'),('jack', 'clubs'), ('queen', 'clubs')]
    with pytest.raises(ValueError):
        card_game(set1, set2)

def test_uneven2():
    """
    Test 26: Test if cards of both sets having unequal cards throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('9', 'hearts'),('jack', 'clubs')]
    with pytest.raises(ValueError):
        card_game(set1, set2)

def test_uneven3():
    """
    Test 27: Test if cards of both sets having unequal cards throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds')]
    set2 = [('king', 'clubs'), ('9', 'hearts'),('jack', 'clubs')]
    with pytest.raises(ValueError):
        card_game(set1, set2, game_mode='four card')

def test_uneven4():
    """
    Test 28: Test if cards of both sets having unequal cards throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds')]
    set2 = [('king', 'clubs'), ('9', 'hearts'),('jack', 'clubs')]
    with pytest.raises(ValueError):
        card_game(set1, set2, game_mode='three card')

def test_invalid1():
    """
    Test 29: Test if invalid input throws an error
    """
    set1 = ({'8', 'clubs'}, ('8', 'diamonds'), ('8', 'hearts'),('8', 'spades'))
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'),('king', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2)

def test_invalid2():
    """
    Test 30: Test if invalid input throws an error
    """
    set1 = ('8', 'clubs', ('8', 'diamonds'), ('8', 'hearts'),('8', 'spades'))
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'),('king', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2)

def test_invalid3():
    """
    Test 31: Test if invalid input throws an error
    """
    set1 = "something random", "a", "b", "c","d"
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('8', 'clubs'),('king', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2)

def test_fc_tie1():
    """
    Test 32: Test if poker hierarchy is implemented correctly in case of same category(Four card)
    """
    # straight flush vs straight flush - tie
    set1 = [('9', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'),('6', 'diamonds')]
    set2 = [ ('9', 'clubs'), ('6', 'clubs'),('7', 'clubs'), ('8', 'clubs')]
    card_game(set1, set2, game_mode='Four card') == 'tie', "poker hierarchy not implemented correctly"

def test_fc_tie2():
    """
    Test 33: Test if poker hierarchy is implemented correctly in case of same category(Four card)
    """
    # straight flush vs straight flush
    set1 = [ ('queen', 'diamonds'), ('jack', 'diamonds'),('king', 'diamonds'), ('10', 'diamonds')]
    set2 = [('10', 'clubs'), ('9', 'clubs'), ('7', 'clubs'), ('8', 'clubs')]
    assert card_game(set1, set2, game_mode='Four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie3():
    """
    Test 34: Test if poker hierarchy is implemented correctly in case of same category(Four card)
    """
    # four of a kind vs four of a kind
    set1 = [('8', 'clubs'), ('8', 'diamonds'), ('8', 'hearts'),('8', 'spades')]
    set2 = [('7', 'diamonds'), ('7', 'clubs'), ('7', 'hearts'),('7', 'spades')]
    assert card_game(set1, set2, game_mode='Four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie4():
    """
    Test 35: Test if poker hierarchy is implemented correctly in case of same category(Four card, Named cards)
    """
    # four of a kind vs four of a kind
    set1 = [('king', 'diamonds'), ('king', 'clubs'), ('king', 'hearts'),('king', 'spades'),]
    set2 = [('jack', 'clubs'), ('jack', 'diamonds'), ('jack', 'hearts'),('jack', 'spades')]
    assert card_game(set1, set2, game_mode='Four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie5():
    """
    Test 36: Test if when game mode and number of cards are mismatched, throws an error (Four card)
    """
    # fullhouse vs fullhouse
    set1 = [('ace', 'clubs'), ('ace', 'diamonds'), ('ace', 'hearts'),('queen', 'spades'), ('queen', 'clubs')]
    set2 = [('king', 'diamonds'), ('king', 'clubs'), ('king', 'hearts'),('7', 'spades'), ('7', 'clubs')]
    with pytest.raises(ValueError):
        card_game(set1, set2, game_mode='Four card') 

def test_fc_tie6():
    """
    Test 37: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # straight vs straight
    set1 = [('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('4', 'clubs'), ('5', 'diamonds'), ('6', 'hearts'),('7', 'clubs')]
    assert card_game(set1, set2, game_mode='four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie7():
    """
    Test 38: Test if poker hierarchy is implemented correctly in case of same category(Three card, tie case)
    """
    # straight vs straight
    set1 = [('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('5', 'diamonds'), ('6', 'hearts'),('7', 'clubs'), ('8', 'spades')]
    assert card_game(set1, set2, game_mode='four card') == 'tie', "poker hierarchy not implemented correctly"

def test_fc_tie8():
    """
    Test 39: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # poker tests - tie test
    # three of a kind vs three of a kind
    set1 = [('8', 'diamonds'), ('8', 'clubs'), ('8', 'hearts'),('6', 'diamonds')]
    set2 = [('5', 'clubs'), ('5', 'diamonds'), ('5', 'hearts'),('7', 'clubs')]
    assert card_game(set1, set2, game_mode='four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie9():
    """
    Test 40: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # poker tests - tie test
    # two pair vs two pair
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('6', 'diamonds')]
    set2 = [('king', 'clubs'), ('king', 'diamonds'), ('jack', 'hearts'),('jack', 'clubs')]
    assert card_game(set1, set2, game_mode='four card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie10():
    """
    Test 41: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # poker tests - tie test
    # one pair vs one pair
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds')]
    set2 = [('king', 'clubs'), ('king', 'diamonds'), ('9', 'hearts'),('jack', 'clubs')]
    assert card_game(set1, set2, game_mode='four card') == 'player1', "poker hierarchy not implemented correctly"

def test_tc_tie1():
    """
    Test 42: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # straight flush vs straight flush - tie
    set1 = [('9', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds')]
    set2 = [ ('9', 'clubs'),('7', 'clubs'), ('8', 'clubs')]
    card_game(set1, set2, game_mode='Three card') == 'tie', "poker hierarchy not implemented correctly"

def test_tc_tie2():
    """
    Test 43: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # straight flush vs straight flush
    set1 = [ ('queen', 'diamonds'), ('jack', 'diamonds'), ('10', 'diamonds')]
    set2 = [ ('9', 'clubs'), ('7', 'clubs'), ('8', 'clubs')]
    assert card_game(set1, set2, game_mode='Three card') == 'player1', "poker hierarchy not implemented correctly"

def test_tc_tie3():
    """
    Test 44: Test if wrong mode on incorrect number of cards throws an error
    """
    # four of a kind vs four of a kind
    set1 = [('8', 'clubs'), ('8', 'diamonds'), ('8', 'hearts'),('8', 'spades')]
    set2 = [('7', 'diamonds'), ('7', 'clubs'), ('7', 'hearts'),('7', 'spades')]
    with pytest.raises(ValueError):
        card_game(set1, set2, game_mode='Three card')

def test_tc_tie4():
    """
    Test 45: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # straight vs straight
    set1 = [('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]
    set2 = [('4', 'clubs'), ('5', 'diamonds'), ('6', 'hearts')]
    assert card_game(set1, set2, game_mode='Three card') == 'player1', "poker hierarchy not implemented correctly"

def test_fc_tie5():
    """
    Test 46: Test if poker hierarchy is implemented correctly in case of same category(Three card, tie case)
    """
    # straight vs straight
    set1 = [('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds')]
    set2 = [('6', 'hearts'),('7', 'clubs'), ('8', 'spades')]
    assert card_game(set1, set2, game_mode='Three card') == 'tie', "poker hierarchy not implemented correctly"

def test_tc_tie6():
    """
    Test 47: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # three of a kind vs three of a kind
    set1 = [('8', 'diamonds'), ('8', 'clubs'), ('8', 'hearts')]
    set2 = [('5', 'clubs'), ('5', 'diamonds'), ('5', 'hearts')]
    assert card_game(set1, set2, game_mode='Three card') == 'player1', "poker hierarchy not implemented correctly"

def test_tc_tie7():
    """
    Test 48: Test if poker hierarchy is implemented correctly in case of same category(Three card)
    """
    # poker tests - tie test
    # one pair vs one pair
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts')]
    set2 = [('king', 'clubs'), ('king', 'diamonds'), ('9', 'hearts')]
    assert card_game(set1, set2, game_mode='Three card') == 'player1', "poker hierarchy not implemented correctly"

def test_docstr1():
    """
    Test 49 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in valid_input.__doc__

def test_docstr2():
    """
    Test 50 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in single_deck.__doc__

def test_docstr3():
    """
    Test 51 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in flush.__doc__

def test_docstr4():
    """
    Test 52 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in royal_flush.__doc__

def test_docstr5():
    """
    Test 53 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in straight_flush.__doc__

def test_docstr6():
    """
    Test 54 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in four_of_kind.__doc__

def test_docstr7():
    """
    Test 55 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in four_of_kind_comp.__doc__

def test_docstr8():
    """
    Test 56 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in full_house.__doc__

def test_docstr9():
    """
    Test 57 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in full_house_comp.__doc__

def test_docstr10():
    """
    Test 58 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in straight.__doc__

def test_docstr11():
    """
    Test 59 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in straight_comp.__doc__

def test_docstr12():
    """
    Test 60 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in three_of_kind.__doc__

def test_docstr13():
    """
    Test 61 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in two_pair.__doc__

def test_docstr14():
    """
    Test 62 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in two_pair_comp.__doc__

def test_docstr15():
    """
    Test 63 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in one_pair.__doc__

def test_docstr16():
    """
    Test 64 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in high_card.__doc__

def test_docstr17():
    """
    Test 65 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in poker.__doc__

def test_docstr18():
    """
    Test 66 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in three_card.__doc__

def test_docstr19():
    """
    Test 67 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in four_card.__doc__

def test_docstr20():
    """
    Test 68 : Test if docstring has all important sections
    """
    assert 'Args', 'Returns' in create_deck.__doc__

def test_invalid4():
    """
    Test 69: Test if invalid game mode throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('6', 'hearts'),('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('ace', 'diamonds'), ('9', 'hearts'),('jack', 'clubs'), ('queen', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2, game_mode='piker mode')

def test_invalid5():
    """
    Test 70: Test if invalid game mode throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('7', 'diamonds'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('ace', 'diamonds'), ('jack', 'clubs'), ('queen', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2, game_mode='four mode')

def test_invalid6():
    """
    Test 71: Test if invalid game mode throws an error
    """
    set1 = [('ace', 'diamonds'), ('ace', 'clubs'), ('5', 'clubs')]
    set2 = [('king', 'clubs'), ('ace', 'diamonds'), ('queen', 'clubs')]
    with pytest.raises(AssertionError):
        card_game(set1, set2, game_mode='three mode')

def test_lambda():
    """
    Test 72: Check if lambda function is used
    """
    lines = inspect.getsource(session6)
    assert re.search('lambda', lines), "lambda function not used!"

def test_map():
    """
    Test 73: Check if map function is used
    """
    lines = inspect.getsource(session6)
    assert re.search('map', lines), "map function not used!"

def test_zip():
    """
    Test 74: Check if map function is used
    """
    lines = inspect.getsource(session6)
    assert re.search('zip', lines), "zip function not used!"
    
def test_deck():
    """
    Test 75: Check if the deck object created through normal function definition returns 52 cards
    """
    deck = create_deck() 
    assert len(deck) == 52, "improper implementation of deck!"