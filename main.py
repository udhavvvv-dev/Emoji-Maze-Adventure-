import random
import os
import time

# Maze size
GRID_SIZE = 7

# Emoji symbols
PLAYER = "🐱"
TREASURE = "🎁"
TRAP = "💀"
BONUS = "⭐"
EMPTY = "⬜"

# Initialize the maze
def create_maze():
    maze = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # Place traps, bonuses, and treasure
    for _ in range(random.randint(5, 10)):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        maze[x][y] = TRAP
    for _ in range(random.randint(3, 6)):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        maze[x][y] = BONUS
    tx, ty = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
    maze[tx][ty] = TREASURE
    return maze, (tx, ty)

# Display the maze
def display_maze(maze, player_pos):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == player_pos:
                print(PLAYER, end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

# Move the player
def move_player(position, direction):
    x, y = position
    if direction == "W" and x > 0:
        x -= 1
    elif direction == "S" and x < GRID_SIZE-1:
        x += 1
    elif direction == "A" and y > 0:
        y -= 1
    elif direction == "D" and y < GRID_SIZE-1:
        y += 1
    return x, y

# Main game loop
def play_game():
    maze, treasure_pos = create_maze()
    player_pos = (0, 0)
    bonus_collected = 0
    start_time = time.time()  # Track start time
    
    while True:
        display_maze(maze, player_pos)
        print(f"Bonuses Collected: {bonus_collected}")
        print("Use W (up), A (left), S (down), D (right) to move. Q to quit.")
        
        # Get user input
        move = input("Your move: ").upper()
        if move == "Q":
            print("You exited the game. Thanks for playing!")
            break

        # Move player
        new_pos = move_player(player_pos, move)
        
        if new_pos == treasure_pos:
            end_time = time.time()  # Calculate end time
            time_taken = end_time - start_time
            final_score = max(1000 - int(time_taken * 10) + (bonus_collected * 50), 0)
            display_maze(maze, new_pos)
            print("🎉 You found the treasure! You win! 🎉")
            print(f"Time Taken: {int(time_taken)} seconds")
            print(f"Final Score: {final_score}")
            break
        
        if maze[new_pos[0]][new_pos[1]] == TRAP:
            end_time = time.time()  # Calculate end time
            time_taken = end_time - start_time
            final_score = max(1000 - int(time_taken * 10) + (bonus_collected * 50), 0)
            display_maze(maze, new_pos)
            print("💀 You stepped on a trap! Game over!")
            print(f"Time Taken: {int(time_taken)} seconds")
            print(f"Final Score: {final_score}")
            break
        
        if maze[new_pos[0]][new_pos[1]] == BONUS:
            bonus_collected += 1
            maze[new_pos[0]][new_pos[1]] = EMPTY
        
        player_pos = new_pos

# Run the game
if __name__ == "__main__":
    play_game()
