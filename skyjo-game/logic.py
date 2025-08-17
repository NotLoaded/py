import random

def new_card(card_pool, game_state):
    if card_pool["remaining_cards"] == 0:
        # all cards that arent currently in the game get reshuffled into the card pool
        card_pool = {
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
            "12": 10,
            "remaining_cards": 150
        }
        for player in game_state["players"].values():
            for column in player["cards"].values():
                for card in column.values():
                    if card is not None and card != "removed":
                        card_pool[card] -= 1
        card_pool[game_state["last_card"]] -= 1  # remove the last card from the pool
        card_pool["remaining_cards"] -= 1
        
    names = list(card_pool.keys())
    weights = list(card_pool.values())
    card = random.choices(names, weights=weights, k=1)[0]
    
    return card, card_pool[card] - 1 

def game():
    player_count = 2 # Default player count
    
    game_state = {
            "players": {
                "player0": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player1": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player2": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player3": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player4": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player5": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player6": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },
                "player7": {
                    "cards": {
                        "column1": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column2": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column3": {"removed": False, "card1": None, "card2": None, "card3": None},
                        "column4": {"removed": False, "card1": None, "card2": None, "card3": None},
                    },
                    "exists": False,  # Indicates if the player exists in the game
                    "total_sum": 0,
                    "open_cards": 0,
                },

        },
        "player_turn": "player0",
        "last_card": None,  # Card in the discard pile,
        "player_count": 0, # Number of players in the game
        "last_round_player": None, # Indicates if it's the last round
        "starting_player": None, # Indicates the player who starts the game
    }
    card_pool = {
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
        "12": 10,
        "remaining_cards": 150
    }
    starting_sum = 0
    for i in range(player_count):
        game_state["players"][f"player{i}"]["exists"] = True
        starting_card_1, card_pool= new_card(card_pool, game_state)
        starting_card_2, card_pool = new_card(card_pool, game_state)
        starting_card_1_c = random.choice({"column1", "column2", "column3", "column4"})
        starting_card_2_c = random.choice({"column1", "column2", "column3", "column4"})
        starting_card_1_r = random.choice({"card1", "card2", "card3"})
        starting_card_2_r = random.choice({"card1", "card2", "card3"})
        game_state["players"][f"player{i}"]["cards"][starting_card_1_c][starting_card_1_r] = starting_card_1
        game_state["players"][f"player{i}"]["cards"][starting_card_2_c][starting_card_2_r] = starting_card_2
        game_state["players"][f"player{i}"]["total_sum"] = starting_card_1 + starting_card_2
        game_state["players"][f"player{i}"]["open_cards"] = 2   
        if game_state["players"][f"player{i}"]["total_sum"] > starting_sum:
            starting_sum = game_state["players"][f"player{i}"]["total_sum"]
            game_state["starting_player"] = f"player{i}"
            
    
    game_state["player_count"] = player_count
    
    while True:
        current_player = game_state["players"][game_state["player_turn"]]
        if game_state["last_round_player"] is not None and game_state["last_round_player"] == current_player:
            # check for every player that exists in this round if all cards are open
            # if not new_card is drawn and placed for all unrevealed cards
            # then check which player has the lowest sum
            ranking = []
            for player in game_state["players"].values():
                if player["exists"]:
                    if player["open_cards"] < 12:
                        for column in player["cards"].values():
                            for card_key in column.keys():
                                if column[card_key] is None:
                                    new_card_drawn, card_pool = new_card(card_pool, game_state)
                                    column[card_key] = new_card_drawn
                                    player["open_cards"] += 1
                                    player["total_sum"] += new_card_drawn
                    # After all cards for this player are open, check if the sum is lower than the current lowest sum
                    if ranking == []:
                        ranking.append({
                            "player": player,
                            "total_sum": player["total_sum"]
                        })
                    else:
                        for rank in ranking:
                            if player["total_sum"] < rank["total_sum"]:
                                ranking.insert(ranking.index(rank), {
                                    "player": player,
                                    "total_sum": player["total_sum"]
                                })
                                break
                    
                    # logic that determines the ranking "right here"            
            game_state["ranking"] = ranking
            reward_players(game_state)        
            break
            
        if current_player["exists"]:
            action = get_player_action_d_t(game_state) # Get the action from the current player wether to draw a card or to take a discarded card
            if action == "draw":
                card, card_pool = new_card(card_pool, game_state)
                action = get_player_action_p_d() # Get the action from the current player wether it should place the card or discard it
                if action == "place":
                    placement = get_player_action_position() # Get the placement from the current player
                    column = placement["column"]
                    row = placement["row"]
                    if current_player["cards"][column][row] is None:
                        current_player["open_cards"] += 1
                    elif current_player["cards"][column][row] is not None:
                        current_player["total_sum"] -= current_player["cards"][column][row]
                        game_state["last_card"] = current_player["cards"][column][row]
                    current_player["cards"][column][row] = card
                    current_player["total_sum"] += card
                elif action == "discard":
                    game_state["last_card"] = card
                    position = get_player_action_position()
                    column = position["column"]
                    row = position["row"]
                    current_player["cards"][column][row], card_pool = new_card(card_pool, game_state)
            elif action == "take_discard":
                if game_state["last_card"] is not None:
                    placement = get_player_action_position()
                    column = placement["column"]
                    row = placement["row"]
                    if current_player["cards"][column][row] is None:
                        current_player["open_cards"] += 1
                        current_player["total_sum"] += game_state["last_card"]
                        current_player["cards"][column][row] = game_state["last_card"]
                        game_state["last_card"], card_pool = new_card(card_pool, game_state)
                    elif current_player["cards"][column][row] is not None:
                        current_player["total_sum"] -= current_player["cards"][column][row]
                        current_player["total_sum"] += game_state["last_card"]
                        current_player["cards"][column][row] = game_state["last_card"]
                        game_state["last_card"], card_pool = new_card(card_pool, game_state)
            # Check if the player has reached the end condition
            if current_player["open_cards"] == 12:
                game_state["last_round_player"] = game_state["player_turn"]
                        
            # Update player turn to the next player
            next_player_index = (int(game_state["player_turn"].replace("player", "")) + 1) % game_state["player_count"]
            game_state["player_turn"] = f"player{next_player_index}"
        else:
            break