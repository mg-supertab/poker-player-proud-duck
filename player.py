from ranker import rank_hand
from random import randint

TEAM_NAME = "Proud Duck"

def get_our_cards(game_state):
    for player in game_state["players"]:
        if player["name"] == TEAM_NAME:
            return player["hole_cards"]
    return []

def get_our_stack(game_state):
    for player in game_state["players"]:
        if player["name"] == TEAM_NAME:
            return player["stack"]
    return 0

def get_table_cards(game_state):
    return game_state["community_cards"]

def get_current_buy_in(game_state):
    return game_state["current_buy_in"]

def get_whole_hans(our_cards, table_cards):
    return our_cards + table_cards

def get_total_number_of_cards(game_state):
    return len(game_state["community_cards"]) + 2

BETTING_STRATEGY = {
        0: 0,
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
        6: 60,
        7: 70,
        8: 80
    }

def get_betting_amount(game_state, rank):
    # If we have a bad hand, we fold
    current_buy_in = get_current_buy_in(game_state)
    if current_buy_in > get_our_stack(game_state):
        return 0
    
    if get_total_number_of_cards(game_state) < 4:
        return current_buy_in

    # If we have a good hand, we go all in
    our_stack = get_our_stack(game_state)
    our_potential_bet = BETTING_STRATEGY[rank] / 100 * our_stack

    if our_potential_bet < current_buy_in:
        return 0

    n = randint(0, 100)

    if n > 40:
        rank = (rank + 2) if rank + 2 <= 8 else 8
        our_potential_bet = BETTING_STRATEGY[rank] / 100 * our_stack
    else:
        return our_potential_bet

class Player:
    VERSION = "0.16"

    def betRequest(self, game_state):
        print("Game state: ", game_state)
        rank, _ = rank_hand(get_whole_hans(get_our_cards(game_state), get_table_cards(game_state)))
        return get_betting_amount(game_state, rank)
        # return 0

    def showdown(self, game_state):
        pass
