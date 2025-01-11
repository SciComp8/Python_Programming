## References:
# https://github.com/ScienceComputing/Python_Programming/blob/68201ab5a7ec56c128425f736fd34298c1258548/Utilities/List/*List_Comprehension.py#L87
# Boolean variables can either be True or False
# ! https://en.wikipedia.org/wiki/De_Morgan%27s_laws 
# https://en.wikipedia.org/wiki/Blackjack

bool(0) # False
bool(0.1) # True
int(False) # 0
int(True) # 1

## Question 1
def sign(num=-1):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1

## Question 2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies <= 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

# Use a *succinct* conditional expression
def concise_to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies <= 1 else "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

## Question 3
# Proof by contradiction
# I said that I'm safe from today's weather if...
# assumption 1: I have an umbrella...
# assumption 2: or if the rain isn't too heavy and I have a hood...
# assumption 3: otherwise, I'm still fine unless it's raining and it's a workday == I'll be fine if it's not raining or it's not a workday.
# To prove that prepared_for_weather is buggy, come up with a set of inputs where either:
# the function returns False (but should have returned True), or the function returned True (but should have returned False).

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday # not (rain_level > 0 and is_workday)
# Apply De Morgan's laws: not (rain_level > 0 and is_workday)  => (rain_level <= 0 or not is_workday)

# The function returns False (but should have returned True)
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

## Question 4
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0 # Replace the verbose expression if number < 0: return True

## Question 5a
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup & mustard & onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup, mustard, onion
# Expected return value of True given ketchup=True, mustard=True, onion=True, but got (True, True, True) instead.

## Question 5b
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)

# This logical equivalence stems from De Morgan's laws in boolean algebra, which state that the negation of "A or B" is the same as "not A and not B.

## Question 5c
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (not ketchup and mustard)

## Question 6
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1 # return (ketchup + mustard + onion) == 1

## Question 7
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """
    Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    """
    if player_high_aces > 0:
        if player_total <= 17:
            return True
        if player_total == 18 and dealer_total >= 9:
            return True
        return False
    else:
        if player_total < 10:
            return True
        if player_total >= 17:
            return False
        if dealer_total >= 7:
            if player_total <= 16:
                return True
            return False
        if dealer_total <= 6:
            if player_total <= 10:
                if player_total == 11 and player_high_aces == 0:
                    return False
                return True
            return False
    return False

