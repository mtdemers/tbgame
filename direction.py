#
## Threadbare - The Text Adventure
#
def main():
    ## main method

    if __name__ == "__main__":
        main()

def get_direction():
    ## Function for getting direction
    direction = raw_input('Which way do you go? ')
    direction = direction.upper()
    if direction == 'NORTH' or direction == 'N':
        return 'N'
    elif direction == 'SOUTH' or direction == 'S':
        return 'S'
    elif direction == 'WEST' or direction == 'W':
        return 'W'
    elif direction == 'EAST' or direction == 'E':
        return 'E'
    else:
        print "I don't understand."
        get_direction()
