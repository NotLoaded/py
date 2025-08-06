import random
from collections import Counter

# Define the card distribution
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

# State object to simulate the environment
state = {
    "cards": cards.copy()
}

def new_card():
    if not state["cards"]:
        raise ValueError("No cards left to draw.")
    names = list(state["cards"].keys())
    weights = list(state["cards"].values())
    card = random.choices(names, weights=weights, k=1)[0]
    return card


num_trials = 1000000
draw_counts = Counter()

for _ in range(num_trials):
    draw = new_card()
    draw_counts[draw] += 1

total_cards = sum(cards.values())

print(f"{'Card':>4} | {'Expected %':>10} | {'Observed %':>10}")
print("-" * 32)

for card in sorted(cards, key=int):
    expected_pct = cards[card] / total_cards * 100
    observed_pct = draw_counts[card] / num_trials * 100
    print(f"{card:>4} | {expected_pct:10.2f} | {observed_pct:10.2f}")