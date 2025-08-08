# skyjo/main.py

import json
import random
import copy

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
        "collumn1": {
            "removed": False,  # Indicates if the column is removed
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "collumn2": {
            "removed": False,  # Indicates if the column is removed
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "collumn3": {
            "removed": False,  # Indicates if the column is removed
            "card1": None,
            "card2": None,
            "card3": None,
        },
        "collumn4": {
            "removed": False,  # Indicates if the column is removed
            "card1": None,
            "card2": None,
            "card3": None,
        },
    },
    "startingCards": [None, None],
    "startingSum": 0,  # Sum of the two starting cards
    "totalSum": 0,     # Total sum of all cards
    "openCards": 0,  # Number of open cards (revealed)
}

# Initialize the game state
# This will hold the number of players, their cards, and the last card played
global state
state = {
    "player-count": 4,
    "players": {},
    "playerTurn": None,
    "last-card": None,
    "last-round-player": None,  # Indicates if it's the last round
    "cards": cards,
}


def init_game_data():
    # Initialize the game state
    
    # Load the number of players from user input
    state["player-count"] = int(input("Enter number of players (2-8): "))
    
    # Create player entries in the state dictionary
    for player in range(0, state["player-count"]):
        state["players"][f"player{player}"] = copy.deepcopy(player_template)

def start_game():
    # Initialize the game data
    init_game_data()
    
    starting_cards()
    
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=4)
        
    game_loop()
    
def starting_cards():
    highset_sum = None
    highest_player = None
    # Players will pick which starting cards to reveal
    for player in state["players"]:
    
        for x in range(2):
            c, r = map(int, input(f"{player}, pick starting card {x} (collumn, card): ").split(","))
            print(f"Picking card at row {c}, card {r} for {player}")
            state["players"][player]["cards"][f"collumn{c}"][f"card{r}"]  = new_card()
            state["players"][player]["startingCards"][x] = state["players"][player]["cards"][f"collumn{c}"][f"card{r}"]
            state["players"][player]["openCards"] += 1
            if x == 1:
                state["players"][player]["startingSum"] = sum(state["players"][player]["startingCards"])
                state["players"][player]["totalSum"] = state["players"][player]["startingSum"]
        if highset_sum is None or state["players"][player]["startingSum"] > highset_sum:
            highset_sum = state["players"][player]["startingSum"]
            highest_player = player
    state["playerTurn"] = highest_player       
            
def new_card():
    if not state["cards"]:
        raise ValueError("No cards left to draw.")
    names = list(state["cards"].keys())
    weights = list(state["cards"].values())
    chosen_card = random.choices(names, weights=weights, k=1)[0]
    print(f"Drawn card: {chosen_card}")
    # Modify the original dictionary in-place
    state["cards"][chosen_card] -= 1
    return int(chosen_card)

def game_ending():
    # Check all collumns of every player for unopened cards
    # Generate new cards for all unopened cards
    for player in state["players"]:
        for collumn in state["players"][player]["cards"].values():
            if not collumn["removed"]:
                for card_key in ["card1", "card2", "card3"]:
                    if collumn[card_key] is None:
                        collumn[card_key] = new_card()
                        state["players"][player]["openCards"] += 1
                        state["players"][player]["totalSum"] += collumn[card_key]
    # Calculate the final scores and determine winner by lowest score
    scores = {player: state["players"][player]["totalSum"] for player in state["players"]}
    winner = min(scores, key=scores.get)
    # Print out the winner and all scores
    print("Final scores:")
    print(f"Game over! The winner is {winner} with a score of {scores[winner]}.")
    for player, score in scores.items():
        print(f"{player}: {score}")
    # Save the final state to the file
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=4)

def game_loop():
    # Main game loop
    
    if state["last-round-player"] == current_player:
        game_ending()
        return
        
    while True:
        current_player = state["playerTurn"]
        print(f"It's {current_player}'s turn.")
        
        # Get the player's action (draw card / take last card)
        action = input(f"{current_player}, choose action (draw/take): ").strip()
        if action == "draw":
            # Draw a new card
            drawn_card = new_card()
            print(f"{current_player} drew a card: {drawn_card}")
            draw_action = input(f"{current_player}, do you want to place the drawn card in a column? (yes/no): ").strip()
            if draw_action.lower() == "yes" or "y":
                c, r = map(int, input(f"{current_player}, choose column and card position to place the drawn card (collumn, card): ").split(","))
                if state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] is None:
                    state["last-card"] = new_card()
                    state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] = drawn_card
                    state["players"][current_player]["openCards"] += 1
                    state["players"][current_player]["totalSum"] += drawn_card
                    print(f"{current_player} placed the drawn card in column {c}, card {r}: {drawn_card}")
                elif state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] is not None:
                    state["last-card"] = state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"]
                    state["players"][current_player]["totalSum"] -= state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"]
                    state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] = drawn_card
                    state["players"][current_player]["totalSum"] += drawn_card
                    print(f"{current_player} replaced the card in column {c}, card {r} with the drawn card: {drawn_card}")
                    
            elif draw_action.lower() == "no" or "n":
                # If the player does not want to place the card, it is discarded
                state["last-card"] = drawn_card
                print(f"{current_player} discarded the drawn card: {drawn_card}")
                c, r = map(int, input(f"{current_player}, choose column and card position to reveal (collumn, card): ").split(","))
                if state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] is None:
                    state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] = new_card()
                    state["players"][current_player]["openCards"] += 1
                    state["players"][current_player]["totalSum"] += state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"]
                    print(f"{current_player} revealed the card in column {c}, card {r}: {state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"]}")
                else:
                    print(f"Column {c}, card {r} is already revealed. Please choose another position.")
                    continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
            
        elif action == "take":
            # Take the last played card
            if state["last-card"] is None:
                print("No last card to take.")
                continue
            elif state["last-card"] is not None:
                c, r = map(int, input(f"{current_player}, choose column and card position to replace with the last card (collumn, card): ").split(","))
                if state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] is None:
                    state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] = state["last-card"]
                    state["players"][current_player]["openCards"] += 1
                    state["players"][current_player]["totalSum"] += state["last-card"]
                    state["last-card"] = new_card()
                    print(f"It replaced the unturned card {state['last-card']} in column {c}, card {r}, which is now discarded.")
                elif state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] is not None:
                    replaced_card = state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"]
                    state["players"][current_player]["totalSum"] -= replaced_card
                    state["players"][current_player]["cards"][f"collumn{c}"][f"card{r}"] = state["last-card"]
                    state["players"][current_player]["totalSum"] += state["last-card"]
                    print(f"{current_player} replaced the card in column {c}, card {r}: {replaced_card} with the last card: {state['last-card']}.")
                    
        for collumn in state["players"][current_player]["cards"].values():
            if collumn["card1"] == collumn["card2"] == collumn["card3"] != None and not collumn["removed"]:
                print(f"{current_player} has a complete column with cards {collumn['card1']}, {collumn['card2']}, {collumn['card3']}.")
                # remove the column from the player's cards
                collumn["removed"] = True
                collumn["card1"] = None
                collumn["card2"] = None
                collumn["card3"] = None
                
        if state["players"][current_player]["openCards"] == 12:
            print(f"{current_player} has revealed all cards. One last round for all players, except himself.")
            state["last-round-player"] = current_player
            
        
        
        
        # Update player turn logic (for simplicity, just rotate through players)
        next_player_index = (int(current_player[-1]) + 1) % state["player-count"]
        state["playerTurn"] = f"player{next_player_index}"
        
        with open('state.json', 'w') as f:
            json.dump(state, f, indent=4)

start_game()