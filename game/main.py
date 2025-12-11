# Author: Ilmari Takkunen
# Github: ilmaritak
#
#
from rooms import room1

def welcome():
    print()
    print("Tervetuloa vankilaan. Tehtävänäsi on paeta vankilasta onnistuneesti.")
    player = input("Mikä sinun nimesi on: ")
    print()
    print(f"Hei {player}!")
    print("Vankilasta on katkennut sähköt ja huomaat ovesi sähkölukon olevan auki.")
    print("Muutenkin ympäristö vaikuttaa autiolta.")
    room1()

if __name__ == "__main__":
    welcome()

