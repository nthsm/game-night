import random

# ------------------------------
# GAME DATA (points and rotations will be adjusted dynamically)
# ------------------------------

def generate_points(num_players, top_points, min_points=1):
    decrement = max((top_points - min_points) // (num_players - 1), 1) if num_players > 1 else 0
    points_text = ""
    current_points = top_points
    for place in range(1, num_players + 1):
        suffix = "st" if place == 1 else "nd" if place == 2 else "rd" if place == 3 else "th"
        points_text += f"{place}{suffix} Place: {current_points} pts\n"
        current_points = max(min_points, current_points - decrement)
    return points_text


def generate_rotation(num_players, group_size):
    rounds = []
    for r in range(num_players):
        rotation = []
        for i in range(group_size):
            rotation.append((r + i) % num_players + 1)
        rounds.append(f"Round {r + 1}: Players " + ", ".join([f"Player {p}" for p in rotation]) + f", Player {rotation[0]} is the solo player.")
    return "\n".join(rounds)

# ------------------------------
# EXCLUSION GROUPS
# ------------------------------

def get_exclusions(num_players):
    exclusions = [
        {"Super Smash Bros. Melee", "JoJo's Bizarre Adventure: All-Star Battle R"},
        {"Mario Kart: Double Dash!!", "Mario Kart Wii"},
        {"Mario Party 6", "Pummel Party"}
    ]
    if num_players > 16:
        exclusions.append({"Mario Party 6"})
        exclusions.append({"Pummel Party"})
    return exclusions

# ------------------------------
# GAME SELECTION FUNCTION
# ------------------------------

def is_valid_selection(selected_games, exclusions):
    selected_names = {game['name'] for game in selected_games}
    for pair in exclusions:
        if len(selected_names.intersection(pair)) > 1:
            return False
    return True

def select_games(pool, num_games, exclusions):
    while True:
        selected = random.sample(pool, num_games)
        if is_valid_selection(selected, exclusions):
            return selected

# ------------------------------
# PLAYER NUMBER ASSIGNMENT
# ------------------------------

def assign_player_numbers(players):
    shuffled = players.copy()
    random.shuffle(shuffled)
    return {i+1: shuffled[i] for i in range(len(shuffled))}

# ------------------------------
# GAME NIGHT SCRIPT
# ------------------------------

def main():
    print(f"There are 10 total games that can be played tonight!")

    # --- Players ---
    num_players = int(input("How many players are participating? "))
    players = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]

    print("\nPlayers:", ", ".join(players))

    # --- Exclusions ---
    exclusions = get_exclusions(num_players)

    # --- Number of games ---
    num_games = int(input(f"How many games will you play tonight? (Max 7) "))
    selected_games = select_games([
        {
            "name": "Super Smash Bros. Melee",
            "points": generate_points(num_players, 12),
            "how_to_play": "Standard 1v1 Tournament Bracket (Single Elimination, BO3).\nLosers' Bracket: Once knocked out of the main bracket, players enter the Random Character Roulette Bracket (BO1).",
            "drinking_rules": "Each time you lose a stock, take a sip."
        },
        {
            "name": "JoJo's Bizarre Adventure: All-Star Battle R",
            "points": generate_points(num_players, 12),
            "how_to_play": "Standard 1v1 Tournament Bracket (Single Elimination, BO3).\nLosers' Bracket: Once knocked out of the main bracket, players enter the Random Character Roulette Bracket (BO1).",
            "drinking_rules": "Each time you lose a game, take a sip."
        },
        {
            "name": "Super Monkey Ball 2",
            "points": generate_points(min(4, num_players), 7),
            "how_to_play": "Play 4-player battle mode, rotate controllers as needed.\n" + generate_rotation(num_players, 5),
            "drinking_rules": "Bottom two scorers take a sip."
        },
        {
            "name": "Mario Kart: Double Dash!!",
            "points": generate_points(num_players, 14),
            "how_to_play": "Three rounds each of Balloon Battle and Bob-Omb Blast, one round of Shine Thief.\nWinner of each round gets 1 in-game point. Player with the most points gets 1st, and so on.",
            "drinking_rules": "Balloon Battle: Lose a balloon? Take a sip.\nBob-Omb Blast: Get hit by a bomb? Take a sip."
        },
        {
            "name": "Mario Kart Wii",
            "points": generate_points(num_players, 10),
            "how_to_play": "Everyone will use Daisy / Mach Bike.\nTime Trial Daisy Circuit, fastest time wins.",
            "drinking_rules": "Chug a beer before your run.\nIf you can't finish it, a 15 second time penalty will be added."
        },
        {
            "name": "New Super Mario Bros. Wii",
            "points": generate_points(num_players, 10),
            "how_to_play": "Each player completes World 1-1 solo, fastest time wins.\nTimer doesn't stop till you complete the level, not if you die or game over. You keep going.",
            "drinking_rules": "The bottom half of finishers drink."
        },
        {
            "name": "Nintendo Land",
            "points": "Mario Chase:\nMario wins → 5 pts\nToad who catches Mario (or gets the closest) → 3 pts\nOther Toads → 1 pt each\nMario loses → 0 pts\n\nLuigi’s Ghost Mansion:\nGhost wins → 5 pts\nLast Luigi standing → 3 pts\nOther Luigis → 1 pt\nGhost loses → 0 pts\n\nAnimal Crossing: Sweet Day:\nGuard wins → 5 pts\nAnimal with the most candy → 3 pts\nOther animals → 1 pt\nGuard loses → 0 pts",
            "how_to_play": "Choose one of the following mini-games:\n1. Mario Chase — 1 Mario vs 4 Toads.\n2. Luigi's Ghost Mansion — 1 Ghost vs Luigi players.\n3. Animal Crossing: Sweet Day — 1 Guard vs 4 Animals.\nEach round, one player is selected as the solo player.\nWe will rotate until everyone has been 'It' once.\n\n" + generate_rotation(num_players, 5),
            "drinking_rules": "Mario Chase:\nIf Mario escapes → all Toads take a sip.\nIf Mario gets caught → Mario takes a big sip.\nIf a Toad doesn’t touch Mario at all, take another sip.\n\nLuigi’s Ghost Mansion:\nIf the ghost wins → all Luigi players take a sip.\nIf the ghost loses → ghost takes a big sip.\nIf you die first → take an extra sip.\n\nAnimal Crossing: Sweet Day:\nIf the guards catch you → take a big sip.\nIf the animals win → guards take a sip.\nIf the guards win → animals take a sip."
        },
        {
            "name": "WarioWare, Inc.: Mega Party Games!",
            "points": "Win a microgame: 2 pts\nFail a microgame: 0 pts",
            "how_to_play": "Play Single Player, rotating players in each microgame.\nThe game will be played until a boss is defeated.",
            "drinking_rules": "Fail a microgame? Take a sip.\nBeat a boss? Everyone else takes a sip."
        },
        {
            "name": "Mario Party 6",
            "points": generate_points(min(4, num_players), 18),
            "how_to_play": (
                "Format: "
                + ("Solo play" if num_players <= 4 else
                f"Teams of {2 if num_players <= 8 else 3 if num_players <= 12 else 4}") 
                + " - 20 Turn Game.\nTeams will be grouped based on player order."
            ),
            "drinking_rules": "Lose a minigame? Take a sip.\nLose a Star? Take a big sip.\nLand on a Red Space? Take a sip.\nLand on an opponent's Character Space? Take a sip."
        },
        {
            "name": "Pummel Party",
            "points": generate_points(min(4, num_players), 18),
            "how_to_play": (
                "Format: "
                + ("Solo play" if num_players <= 4 else
                f"Teams of {2 if num_players <= 8 else 3 if num_players <= 12 else 4}") 
                + "\nTeams will be randomly selected."
            ),
            "drinking_rules": "Lose a minigame? Take a sip.\nLose a Star? Take a big sip.\nLand on a Red Space? Take a sip.\nLand on an opponent's Character Space? Take a sip."
        }
    ], num_games, exclusions)

    # --- Drinking? ---
    drinking = input("Are you drinking tonight? (Y/N): ").strip().upper()
    if drinking == "Y":
        print("Sounds good!")
    else:
        print("Too bad!")

    # --- Game Loop ---
    print("\nStarting Game Night...\n")
    for i, game in enumerate(selected_games, 1):
        player_numbers = assign_player_numbers(players)
        print(f"Game {i}: {game['name']}")
        print("\nPlayer Numbers:")
        for num, name in player_numbers.items():
            print(f"Player {num}: {name}")
        print("\nPoints System:")
        print(game['points'])
        print("\nHow to Play:")
        print(game['how_to_play'])
        if drinking == "Y":
            print("\nDrinking Rules:")
            print(game['drinking_rules'])


        while True:
            done = input("\nAre you done with this game? (Y/N): ").strip().upper()
            if done == "Y":
                print("\nNext game coming up...\n")
                break

    print("Game Night Complete! Tally up your points!")

if __name__ == "__main__":
    main()
