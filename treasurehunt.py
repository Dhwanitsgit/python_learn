MAX_PATH_LENGTH = 70
MIN_PATH_LENGTH = 10
MAX_LIVES = 10
MIN_LIVES = 1

class Player:
    def __init__(self):
        self.lives = 0
        self.treasures_collected = 0
        self.symbol = ''
        self.positions = [0] * MAX_PATH_LENGTH

class Game:
    def __init__(self):
        self.total_moves = 0
        self.path_length = 0
        self.bomb_locations = [0] * MAX_PATH_LENGTH
        self.treasure_locations = [0] * MAX_PATH_LENGTH

def main():
    player = Player()
    game = Game()

    print("================================")
    print("         Treasure Hunt!")
    print("================================\n")

    print("PLAYER Configuration")
    print("--------------------")
    player.symbol = input("Enter a single character to represent the player: ")

    while True:
        player.lives = int(input("Set the number of lives: "))
        if MIN_LIVES <= player.lives <= MAX_LIVES:
            break
        print("     Must be between 1 and 10!\n")

    print("Player configuration set-up is complete\n")
    print("GAME Configuration")
    print("------------------")

    while True:
        game.path_length = int(input("Set the path length (a multiple of 5 between 10-70): "))
        if MIN_PATH_LENGTH <= game.path_length <= MAX_PATH_LENGTH and game.path_length % 5 == 0:
            break
        print("     Must be a multiple of 5 and between 10-70!!!\n")

    while True:
        game.total_moves = int(input("Set the limit for number of moves allowed: "))
        if player.lives <= game.total_moves <= int(0.75 * game.path_length):
            break
        print(f"    Value must be between {player.lives} and {int(0.75 * game.path_length)}\n")

    print("\nBOMB Placement")
    print("--------------")
    print("Enter the bomb positions in sets of 5 where a value")
    print("of 1=BOMB, and 0=NO BOMB. Space-delimit your input.")
    print(f"(Example: 1 0 0 1 1) NOTE: there are {game.path_length} to set!")

    for i in range(0, game.path_length, 5):
        bomb_input = input(f"   Positions [{i + 1}-{i + 5}]: ").split()
        game.bomb_locations[i:i + 5] = map(int, bomb_input)

    print("BOMB placement set\n")
    print("TREASURE Placement")
    print("------------------")
    print("Enter the treasure placements in sets of 5 where a value")
    print("of 1=TREASURE, and 0=NO TREASURE. Space-delimit your input.")
    print(f"(Example: 1 0 0 1 1) NOTE: there are {game.path_length} to set!")

    for i in range(0, game.path_length, 5):
        treasure_input = input(f"   Positions [{i + 1}-{i + 5}]: ").split()
        game.treasure_locations[i:i + 5] = map(int, treasure_input)

    print("TREASURE placement set\n")
    print("GAME configuration set-up is complete...\n")
    print("------------------------------------")
    print("TREASURE HUNT Configuration Settings")
    print("------------------------------------")
    print(f"Player:\n   Symbol     : {player.symbol}\n   Lives      : {player.lives}")
    print("   Treasures  : [ready for gameplay]\n   History    : [ready for gameplay]\n")
    print(f"Game:\n   Path Length: {game.path_length}\n   Bombs      : {''.join(map(str, game.bomb_locations))}")
    print(f"   Treasures  : {''.join(map(str, game.treasure_locations))}\n\n")
    print("====================================")
    print("~ Get ready to play TREASURE HUNT! ~")
    print("====================================")

    remaining_moves = game.total_moves
    remaining_lives = player.lives
    player.treasures_collected = 0
    visited_count = 0
    current_position_symbols = [' '] * MAX_PATH_LENGTH
    path_symbols = ['-'] * MAX_PATH_LENGTH

    while remaining_moves > 0 and remaining_lives > 0:
        visited_count = 0

        for k in range(game.path_length):
            if current_position_symbols[k] == 'V':
                visited_count += 1
        
        if visited_count == 0:
            print("\n")
        else:
            print("  ", end="")
            for k in range(game.path_length):
                if current_position_symbols[k] == 'V':
                    print(f"{current_position_symbols[k]}\n", end="")
                    break
                else:
                    print(f"{current_position_symbols[k]}", end="")
            print()

        current_position_symbols = [' '] * MAX_PATH_LENGTH

        print("  ", end="")
        for k in range(game.path_length):
            print(f"{path_symbols[k]}", end="")
        print("\n  ", end="")

        for i in range(1, game.path_length + 1):
            if i % 10 == 0:
                print(f"{i // 10}", end="")
            else:
                print("|", end="")
        print("\n  ", end="")

        for i in range(0, game.path_length, 10):
            print("1234567890", end="")
        print("\n+---------------------------------------------------+")
        print(f"  Lives: {remaining_lives:2d}  | Treasures: {player.treasures_collected:2d}  |  Moves Remaining: {remaining_moves:2d}")
        print("+---------------------------------------------------+")

        if remaining_lives == 0:
            break

        if remaining_moves == 0:
            break

        while True:
            move_position = int(input("Next Move [1-70]: "))
            if 1 <= move_position <= game.path_length:
                break
            print("  Out of Range!!!")

        print("\n")

        if player.positions[move_position - 1] == 1:
            print("===============> Dope! You've been here before!\n")
            current_position_symbols[move_position - 1] = 'V'
            remaining_moves += 1

        elif game.bomb_locations[move_position - 1] == 1 and game.treasure_locations[move_position - 1] == 1:
            print("===============> [&] !!! BOOOOOM !!! [&]")
            print("===============> [&] $$$ Life Insurance Payout!!! [&]\n")
            path_symbols[move_position - 1] = '&'
            current_position_symbols[move_position - 1] = 'V'
            remaining_lives -= 1
            player.treasures_collected += 1

        elif game.bomb_locations[move_position - 1] == 1:
            print("===============> [!] !!! BOOOOOM !!! [!]\n")
            path_symbols[move_position - 1] = '!'
            current_position_symbols[move_position - 1] = 'V'
            remaining_lives -= 1

        elif game.treasure_locations[move_position - 1] == 1:
            print("===============> [$] $$$ Found Treasure! $$$ [$]\n")
            path_symbols[move_position - 1] = '$'
            current_position_symbols[move_position - 1] = 'V'
            player.treasures_collected += 1

        else:
            print("===============> [.] ...Nothing found here... [.]\n")
            path_symbols[move_position - 1] = '.'
            current_position_symbols[move_position - 1] = 'V'

        player.positions[move_position - 1] = 1
        remaining_moves -= 1

        if remaining_lives == 0:
            print("No more LIVES remaining!\n")

        if remaining_moves == 0:
            print("No more MOVES remaining!\n")

    print("\n##################")
    print("#   Game over!   #")
    print("##################\n")
    print("You should play again and try to beat your score!\n")

if __name__ == "__main__":
    main()

