import random
import os
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    """Simulates rolling a six-sided dice."""
    return random.randint(1, 6)

def play_snake_and_ladder():
    """Main function to play the Snake and Ladder game."""
    board_size = 100
    max_players = 2
    ladder = {5: 25, 20: 40, 35: 55, 50: 70, 65: 85, 80: 95, 90: 99}
    snake = {15: 5, 25: 10, 37: 18, 52: 36, 68: 48, 85: 63, 98: 78}

    current_position = [0] * max_players
    player = 0

    while True:
        clear_screen()
        print("Snake and Ladder Game!!")
        print("Current Player:", player + 1)
        print("========================")
        for i in range(max_players):
            print("Player", i + 1, "is at position", current_position[i])
        print("========================")

        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("Player", player + 1, "rolled a", dice_roll)
        current_position[player] += dice_roll

        if current_position[player] >= board_size:
            print("Player", player + 1, "wins!")
            break

        if current_position[player] in ladder:
            print("Player", player + 1, "climbed a ladder to position", ladder[current_position[player]])
            current_position[player] = ladder[current_position[player]]

        if current_position[player] in snake:
            print("Player", player + 1, "was bitten by a snake to position", snake[current_position[player]])
            current_position[player] = snake[current_position[player]]

        player = (player + 1) % max_players
        time.sleep(1)

if __name__ == "__main__":
    play_snake_and_ladder()
