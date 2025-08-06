# skyjo/main.py

import json
import random

cards = {
    "-2": 5,
    "-1": 10,
    "0": 15,  
    "1": 10,
    "2": 10,
    "3": 10,
    "4": 10,
    "5": 10,
    "6": 10,
    "7": 10,
    "8": 10,
    "9": 10,
    "10": 10,
    "11": 10,
    "12": 10
}

# Template for player cards
# This will be used to initialize each player's card structure
# Each player has 4 rows of cards, each with 3 cards
# Unturned cards are represented as None
player_template = {
    "cards": {
        "row1": {
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "row2": {
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "row3": {
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "row4": {
            "card1": None,
            "card2": None,
            "card3": None,
        },
    }
}

# Initialize the game state
# This will hold the number of players, their cards, and the last card played
global state
state = {
    "player-count": 4,
    "players": {},
    "playerTurn": None,
    "last-card": None,
    "cards": cards,
}


def init_game_data():
    # Initialize the game state
    
    # Load the number of players from user input
    state["player-count"] = int(input("Enter number of players (2-8): "))
    
    # Create player entries in the state dictionary
    for player in range(0, state["player-count"]):
        state["players"][f"player{player}"] = player_template.copy()

def start_game():
    # Initialize the game data
    init_game_data()
    
    starting_cards()
    
def starting_cards():
    # Players will pick which starting cards to reveal
    for player in state["players"]:
        for x in range(2):
            r, c = map(int, input(f"{player}, pick starting card {x} (row, card): ").split(","))
            state["players"][player]["cards"][f"row{r}"][f"card{c}"] = new_card()
            
def new_card():
    if not state["cards"]:
        raise ValueError("No cards left to draw.")
    names = list(state["cards"].keys())
    weights = list(state["cards"].values())
    chosen_card = random.choices(names, weights=weights, k=1)[0]

    # Modify the original dictionary in-place
    state["cards"][chosen_card] -= 1
    
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=4)
    
start_game()