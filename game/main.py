# Author: Ilmari Takkunen
# Github: ilmaritak
#
# Main file
#
from rooms import room1
import utils

def welcome():

    print()
    print("Tervetuloa vankilaan. Tehtävänäsi on paeta vankilasta onnistuneesti.")
    utils.player = input("Mikä sinun nimesi on: ")
    print()
    print(f"Hei {utils.player}!")
    print("Vankilasta on katkennut sähköt ja huomaat ovesi sähkölukon olevan auki.")
    print("Muutenkin ympäristö vaikuttaa autiolta.")
    print()
    print("Kirjoita 'apua' tai 'vihje' nähdäksesi käytettävissä olevat komennot.")
    room1()

if __name__ == "__main__":
    welcome()
