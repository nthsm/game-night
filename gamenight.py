import random

# ------------------------------
# GAME DATA
# ------------------------------

game_pool = [
    {
        "name": "Super Smash Bros. Melee",
        "points": "\n1st Place: 12 pts\n2nd Place: 9 pts\n3rd Place: 7 pts\n4th Place: 5 pts\n5th Place: 4 pts\n6th Place: 3 pts\n7th Place: 2 pts",
        "how_to_play": "\nFormat: Standard 1v1 Tournament Bracket (Single Elimination, BO3).\nLosers' Bracket: Once knocked out of the main bracket, players enter the Random Character Roulette Bracket (BO1).",
        "drinking_rules": "\nEach time you lose a stock, take a sip."
    },
    {
        "name": "Super Monkey Ball 2",
        "points": "\n1st Place: 7 pts\n2nd Place: 6 pts\n3rd Place: 5 pts\n4th Place: 4 pts",
        "how_to_play": "\nFormat: Play 4-player battle mode, rotate controllers as needed.\nRound 1: Players 1-5 play.\nRound 2: Players 2-6 play.\nRound 3: Players 3-7 play.\nRound 4: Players 4,5,6,7,1 play.\nRound 5: Players 5,6,7,1,2 play.\nRound 6: Players 6,7,1,2,3 play.\nRound 7: Players 7,1,2,3,4 play.\nYour player number will be randomly assigned.",
        "drinking_rules": "\nBottom two scorers take a sip."
    },
    {
        "name": "Mario Kart: Double Dash!!",
        "points": "\n1st Place: 14 pts\n2nd Place: 10 pts\n3rd Place: 8 pts\n4th Place: 6 pts\n5th Place: 4 pts\n6th Place: 2 pts\n7th Place: 1 pt",
        "how_to_play": "\nFormat: Three rounds each of Balloon Battle and Bob-Omb Blast, one round of Shine Thief.\nWinner of each round gets 1 in-game point. Player with the most points gets 1st, and so on.",
        "drinking_rules": "\nBalloon Battle: Lose a balloon? Take a sip.\nBob-Omb Blast: Get hit by a bomb? Take a sip."
    },
    {
        "name": "Mario Kart Wii",
        "points": "\n1st Place: 10 pts\n2nd Place: 8 pts\n3rd Place: 7 pts\n4th Place: 6 pts\n5th Place: 5 pts\n6th Place: 4 pts\n7th Place: 3 pts",
        "how_to_play": "\nFormat: Everyone will use Daisy / Mach Bike.\nPlaying order will be randomly selected.",
        "drinking_rules": "\nChug a beer before your run.\nIf you can’t finish it, a 15 second time penalty will be added."
    },
    {
        "name": "New Super Mario Bros. Wii",
        "points": "\n1st Place: 10 pts\n2nd Place: 8 pts\n3rd Place: 7 pts\n4th Place: 6 pts\n5th Place: 5 pts\n6th Place: 4 pts\n7th Place: 3 pts",
        "how_to_play": "\nFormat: Each player completes World 1-1 solo, fastest time wins.\nTimer doesn’t stop till you complete the level, not if you die or game over. You keep going.\nPlaying order will be randomly selected.",
        "drinking_rules": "\nThe bottom 4 finishers drink."
    },
    {
        "name": "Nintendo Land",
        "points": "\nVaries depending on mini-game:\n\nMario Chase:\nMario wins → 5 pts\nToad who catches Mario (or gets the closest) → 3 pts\nOther Toads → 1 pt each\nMario loses → 0 pts\n\nLuigi’s Ghost Mansion:\nGhost wins → 5 pts\nLast Luigi standing → 3 pts\nOther Luigis → 1 pt\nGhost loses → 0 pts\n\nAnimal Crossing: Sweet Day:\nGuard wins → 5 pts\nAnimal with the most candy → 3 pts\nOther animals → 1 pt\nGuard loses → 0 pts",
        "how_to_play": "\nFormat: We will play 7 rounds, everyone gets to be ‘It’ once.\nThe person whose turn it is to be ‘It’ will pick which of the 3 minigames they want to compete in.\nThe player who is ‘It’ does not pick who they are playing against.\nRound 1: Players 1-5 play, Player 1 is the solo player.\nRound 2: Players 2-6 play, Player 2 is the solo player.\nRound 3: Players 3-7 play, Player 3 is the solo player.\nRound 4: Players 4,5,6,7,1 play, Player 4 is the solo player.\nRound 5: Players 5,6,7,1,2 play, Player 5 is the solo player.\nRound 6: Players 6,7,1,2,3 play, Player 6 is the solo player.\nRound 7: Players 7,1,2,3,4 play, Player 7 is the solo player.\nYour player number will be randomly assigned.",
        "drinking_rules": "\nSee mini-game specific rules."
    },
    {
        "name": "WarioWare, Inc.: Mega Party Games!",
        "points": "\nWin a microgame: 2 pts\nFail a microgame: 0 pts",
        "how_to_play": "\nFormat: Play Single Player, rotating players in each microgame.\nThe game will be played until a boss is defeated.\nStarting player will be randomly selected.",
        "drinking_rules": "\nFail a microgame? Take a sip.\nBeat a boss? Everyone else takes a sip."
    },
    {
        "name": "Mario Party 6",
        "points": "\n1st Place: 18 pts\n2nd Place: 14 pts\n3rd Place: 10 pts\n4th Place: 6 pts",
        "how_to_play": "\nFormat: 2v2v2v1 - 20 Turn Game.\nTeams will be randomly selected.",
        "drinking_rules": "\nLose a minigame? Take a sip.\nLose a Star? Take a big sip.\nLand on a Red Space? Take a sip.\nLand on an opponent’s Character Space? Take a sip."
    },
    {
        "name": "JoJo's Bizarre Adventure: All-Star Battle R",
        "points": "\n1st Place: 12 pts\n2nd Place: 9 pts\n3rd Place: 7 pts\n4th Place: 5 pts\n5th Place: 4 pts\n6th Place: 3 pts\n7th Place: 2 pts",
        "how_to_play": "\nFormat: Standard 1v1 Tournament Bracket (Single Elimination, BO3).\nLosers' Bracket: Once knocked out of the main bracket, players enter the Random Character Roulette Bracket (BO1).",
        "drinking_rules": "\nEach time you lose a stock, take a sip."
    },
    {
        "name": "Pummel Party",
        "points": "\n1st Place: 18 pts\n2nd Place: 14 pts\n3rd Place: 10 pts\n4th Place: 6 pts",
        "how_to_play": "\nFormat: Standard Pummel Party game.",
        "drinking_rules": "\nLose a minigame? Take a sip.\nLose a Star? Take a big sip.\nLand on a Red Space? Take a sip.\nLand on an opponent’s Character Space? Take a sip."
    }
]

# ------------------------------
# EXCLUSION GROUPS
# ------------------------------

exclusions = [
    {"Super Smash Bros. Melee", "JoJo's Bizarre Adventure: All-Star Battle R"},
    {"Mario Kart: Double Dash!!", "Mario Kart Wii"},
    {"Mario Party 6", "Pummel Party"}
]

# ------------------------------
# GAME SELECTION FUNCTION
# ------------------------------

def is_valid_selection(selected_games):
    selected_names = {game['name'] for game in selected_games}
    for pair in exclusions:
        if len(selected_names.intersection(pair)) > 1:
            return False
    return True

def select_games(pool, num_games):
    while True:
        selected = random.sample(pool, num_games)
        if is_valid_selection(selected):
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
    print(f"There are {len(game_pool)} total games that can be played tonight!")

    # --- Players ---
    num_players = int(input("How many players are participating? "))
    players = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]

    print("\nPlayers:", ", ".join(players))

    # --- Number of games ---
    num_games = int(input(f"How many games will you play tonight? (Max {len(game_pool)}) "))
    selected_games = select_games(game_pool, num_games)

    # --- Drinking? ---
    drinking = input("Are you drinking tonight? (Y/N): ").strip().upper()
    if drinking == "Y":
        print("Sounds good!")
    else:
        print("Too bad!")

    # --- Game Loop ---
    print("\nStarting Game Night...\n")
    for i, game in enumerate(selected_games, 1):
        print(f"Game {i}: {game['name']}")
        print("\nPoints System:", game['points'])
        print("\nHow to Play:", game['how_to_play'])
        if drinking == "Y":
            print("\nDrinking Rules:", game['drinking_rules'])
        player_numbers = assign_player_numbers(players)
        print()
        for num, name in player_numbers.items():
            print(f"Player {num}: {name}")

        while True:
            done = input("\nAre you done with this game? (Y/N): ").strip().upper()
            if done == "Y":
                print("\nNext game coming up...\n")
                break

    print("Game Night Complete! Tally up your points!")

if __name__ == "__main__":
    main()