import random

def roll_dice():
    return random.randint(1, 6)

def create_board():
    # Define snakes and ladders as dictionaries
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    return snakes, ladders

def play_game():
    player_position = 0
    snakes, ladders = create_board()
    
    while(player_position < 100):
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"You rolled a {roll}")
        
        player_position += roll
        
        if (player_position>= 100): 
             print(f"You are now on square {player_position}")
        
        if (player_position in snakes):
            print(f"Oh no! You hit a snake and slid down to {snakes[player_position]}")
            player_position = snakes[player_position]
            
        elif player_position in ladders:
            print(f"Yay! You climbed a ladder to {ladders[player_position]}")
            player_position = ladders[player_position]
        
        print(f"You are now on square {player_position}")
print("Congratulations! You've won the game!")     
      

if __name__ == "__main__":
    print("Welcome to Snakes and Ladders!")
    play_game()