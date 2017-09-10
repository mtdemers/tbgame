#
## Combat stuff
#
import random

def main():
    ## main method

    if __name__ == "__main__":
        main()

hp = 100


def damage(weapon, multiplier, health):
    ## getting hurt
    health += - random.randrange(0, weapon) * multiplier
    return health

