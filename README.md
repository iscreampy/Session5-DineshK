# EPAi - Session 5
## Problem Description

* Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
* Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
* Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 150 pts

#### Basics (applicable to 2/3 above):

* Proper readme file - 50 (if not there then 0)
Docstrings must, and it must mention what the function is doing (2, 3) - 50
* Write annotations for 3 - 50 pts
* Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
* Submit Github link with all test files and github actions in place. 

## Solution
More than 20 functions and 70 tests were written to make sure that poker hierarchy was implemented correctly. 

### Design choices
Since 4 card and 3 card games do not have preset rules, some liberties were taken while designing these functions. 

* four card games do not implement full house for the sake of consistency
* three card games do not implement full house, four of a kind and two pair
* poker, four card & three card games were implemeted using optional keyword argument ```game_mode``` in the ```card_game``` function. When option is not used, it defaults to ```poker```

### Functions
This problem was implemented in 3 modules. ```game_rules``` module implements all the relevant hierarchies for poker, four card and three card games. ```game_modes``` module implements the conditions in which these rules apply. ```session6``` module implements the main function which calls on the functions defined in the previously mentioned modules. 

```game_rules``` module implements functions such as ```royal_flush```, ```straight_flush```, ```four_of_kind```, ```full_house```, ```flush```, ```straight```, ```three_of_kind```, ```two_pair```, ```one_pair```, ```high_card``` and other comparison functions that come into effect when there are two card sets of the same hierarchy level. For example,

```
# straight vs straight
set1 = [('4', 'diamonds'), ('8', 'clubs'), ('7', 'hearts'),('6', 'diamonds'), ('5', 'clubs')]

set2 = [('9', 'clubs'), ('5', 'diamonds'), ('6', 'hearts'),('7', 'clubs'), ('8', 'spades')]

```
This should return player2 (holding set2) as the winner. These sort of comparison functions were implemented and tested for all three game modes.

Finally, all functions are well documented with a docstring that gives a short description of the function as well as mentions the type of input and type of return value. Annotations were implemented for function 3 (```card_game```) as was required by the task. 

### Tests
Tests that where implemented include tests to check if all the hierarchies were implemented correctly for all three game modes all hierarchy combinations accounted for(contained in ```test_combinations```). 

Further more tests where implemented to check if when two card sets have the same hierarchy level they'd be compared according to the rules of poker. As in, when two players have full house, the higher triple wins. These rules were carefully implemented and tested for all possibilities. 

Additionally, tests were conducted to check if correct errors were raised when users tried to input invalid values as card sets or tried to input incorrect number of cards in inappropriate game modes (input of 5 cards in a four card game, comparing 4 cards vs 3 cards etc). Tests were written to check if the documentation contained all the argument and return value details. 



