print(f'Hello World!')
#--------------------------------------------------------------------------------------------------------------#
# Advent of Code - Day 1, Secret Entrance
# Dinel Brkic
# 12/1/2025
#--------------------------------------------------------------------------------------------------------------#
# PSEUDOCODE
#--------------------------------------------------------------------------------------------------------------#

# Define the main function
    # Declare a variable 'dial' and set value to 50
    # Declare a variable 'num_of_rotations' and set value to 0

    # Declare a 'with' statement for better file handling, opening file named as 'day1_input.txt.'
    # Read through the entire file
    # Display contents of the file
    # Split the values in the file

    # Declare a for statement with 'move' in 'moves'
        # Set 'move' at position 0 in the list and assign the value to 'direction'
        # Set 'move' as an integer and have it move from position 1 in to the end and set value to 'rotations'

        # If 'direction' is equal to 'R'
            # Add the values of 'dial' and 'rotations' together and use %100 to get the remainder
        # Else
            # Subtract the values of 'dial' from 'rotations' and use %100 to get the remainder

        # If the value of 'dial' is equal to 0
            # Increment the 'num_of_rotations' variable by 1

        # Display "Final dial position: " followed by the value of 'dial'
        # Display "Times landed on 0: " followed by the value of 'num_of_rotations'

    # If '__name__ is equal to "__main__"
        # Call main()
    

#--------------------------------------------------------------------------------------------------------------#
# SUMMARY
#--------------------------------------------------------------------------------------------------------------#

# Problem asks for a program which takes inputs from a user
# (ex. L23, R85) and performs calculation on a cycle of
# numbers from between 0 and 99 until the user ends the
# amount of inputs before counting the amount of times 0
# shows up as the total of every input.

#--------------------------------------------------------------------------------------------------------------#

def main():
    dial = 50
    num_of_rotations = 0

    with open("day1_input.txt", "r") as file:
        content = file.read()
        print(content)
        moves = content.strip().split('\n')

    for move in moves:
        direction = move[0]
        rotations = int(move[1:])

        if direction == 'R':
            dial = (dial + rotations) % 100
        else:
            dial = (dial - rotations) % 100
        
        if dial == 0:
            num_of_rotations += 1
    
    print(f'Final dial position: {dial}')
    print(f'Times landed on 0: {num_of_rotations}')

if __name__ == "__main__":
    main()