import random


def game_init(player_count):
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
    
    return game_state, card_pool
    

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
                        cards[card] -= 1
        card_pool[game_state["last_card"]] -= 1  # remove the last card from the pool
        card_pool["remaining_cards"] -= 1
        
    names = list(card_pool.keys())
    weights = list(card_pool.values())
    card = random.choices(names, weights=weights, k=1)[0]
    
    return card, card_pool[card] - 1 