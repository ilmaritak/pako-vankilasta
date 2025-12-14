# Author: Ilmari Takkunen
# Github: ilmaritak
#
# This file is respnsibele of the commands and logic of the game
#
from items import inventory, items

score = 0
max_score = 90
player = "" # This is used in end_game function and set in the welcome function in main

# Functions for basic actions
def show_inventory():
    print()
    if inventory:
        print("Sinulla on mukana:")
        for item in inventory:
            print(" -", item)
    else:
        print("Sinulla ei ole mitään mukana.")

def add_score(points):
    global score
    score = min(max_score, score + points)
    print(f"(Sait {points} pistettä. Pisteesi nyt: {score}/{max_score})")

def take_item(item_name, room_name):
    if item_name not in items:
        print("Sellaista esinettä ei ole.")
        return

    if items[item_name]["location"] != room_name:
        print("Et näe sellaista täällä.")
        return

    inventory.append(item_name)
    items[item_name]["location"] = "inventory"
    print(f"Otit esineen: {item_name}")

    if "points" in items[item_name]:
        add_score(items[item_name]["points"])

def drop_item(item_name, room_name):
    if item_name not in inventory:
        print("Ei ole sinulla sellaista.")
        return

    inventory.remove(item_name)
    items[item_name]["location"] = room_name
    print(f"Pudotit esineen: {item_name}")

def look(room_name, room_description):
    print()
    print(room_description)
    print()

    here_items = [item for item in items if items[item]["location"] == room_name]

    if here_items:
        print("Näet täällä:")
        for i in here_items:
            print(f" - {i}: {items[i]['description']}")
    else:
        print("Täällä ei näytä olevan mitään erikoista.")


# Input handling and item related actions
def handle_commands(room_name, room_description, valid_dirs):
    look(room_name, room_description)

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ["katsele", "tutki"]:
            look(room_name, room_description)

        elif cmd == "mukana":
            show_inventory()

        elif cmd == "lopeta":
            print("Peli päättyy.")
            exit()

        elif cmd in ["apua", "vihje"]:
            help()

        elif cmd.startswith("ota "):
            take_item(cmd[4:], room_name)

        elif cmd.startswith("pudota "):
            drop_item(cmd[7:], room_name)

        elif cmd.startswith("mene "):
            direction = cmd[5]

            if direction in valid_dirs:
                return direction
            else:
                print("Et voi mennä siihen suuntaan.")

        elif cmd.startswith("tarkista "):
            item = cmd[9:]
            if item in inventory:

                print(items[item]["description"])
            else:
                print("Ei ole sinulla sellaista.")

        elif cmd.startswith("syö "):
            item = cmd[4:]
            if item not in inventory:
                print("Ei ole sinulla sellaista.")
            elif item not in ["kuivamuonaa"]:
                print("Et voi syödä sitä.")
            else:
                print("Söit kuivamuonaa. Olosi on nyt parempi.")

        elif cmd.startswith("lataa "):
            parts = cmd.split()
            if len(parts) != 3:
                print("Käytä muotoa: lataa <esine1> <esine2>")
                continue

            a, b = parts[1], parts[2]

            if a not in inventory or b not in inventory:
                print("Sinulla ei ole molempia esineitä.")

            elif (a == "kivääri" and b == "ammuksia") or (a == "ammuksia" and b == "kivääri"):
                print("Latasit kiväärisi.")
                add_score(10)

            elif (a == "taskulamppu" and b == "paristo") or (a == "paristo" and b == "taskulamppu"):
                print("Latasit taskulampun paristolla.")
                add_score(10)

            else:
                print("Tätä esinettä ei voi ladata.")

        elif cmd.startswith("pue "):
            item = cmd[4:]
            if item not in inventory:
                print("Ei ole sinulla sellaista.")
            elif item not in ["takki"]:
                print("Et voi pukea tätä sinettä.")
            else:
                print("Puit takin päällesi. Olosi on mukavan lämmin.")
                inventory.remove(item)
                add_score(10)

        elif cmd.startswith("lue "):
            item = cmd[4:]
            if item not in inventory:
                print("Ei ole sinulla sellaista.")
            elif item not in ["kirje"]:
                print("Et voi lukea tätä sinettä.")
            else:
                print("Hei, Herra vankilanjohtaja. ")
                print("Lumimyrkskyn vuoksi sähköt ovat poikki koko pohjoisesta osasta valtiota. ")
                print("Pyydän teitä evakuoimaan kaikki työntekijät ja vangit. ")
                print("Lähin turvallinen kaupunki on noin 500km etelään, teidät sijoitetaan sinne.")
                print("Varmistakaa että ketään ei unohdu.")
                print("Yt. Pormestari")
                inventory.remove(item)
                add_score(10)

        else:
            print("En ymmärrä komentoa.")

# ending function usen after moving east from room 20
def game_end():
    global score, max_score


    print("  PELI PÄÄTTYI  ")
    print()

    print(f"Onneksi olkoon {player}, pakenit vankilasta!")
    print(f"Pisteesi: {score}/{max_score}\n")

    if score >= 90:
        print("Uskomaton suoritus! Et jättänyt mitään tutkimatta.")
        print("Olet todellinen mestaripakolainen.")
    elif score >= 50:
        print("Hieno pako! Löysit suurimman osan salaisuuksista.")
    elif score >= 30:
        print("Selvisit nipin napin. Olisit voinut tutkia enemmän.")
    else:
        print("Pääsit pakoon, mutta hyvin hutiloiden.")
        print("Vankila piti vielä monta salaisuutta sisällään.")

    print("\nKiitos pelaamisesta!")
    exit()

# help function
def help():
    print()
    print("Käytettävissä olevat komennot:")
    print("--------------------------------")
    print("mene <suunta>      - Liiku")
    print("katsele / tutki    - Katso ympärillesi uudelleen")
    print("ota <esine>        - Ota esine mukaasi")
    print("pudota <esine>     - Pudota esine")
    print("mukana             - Näytä inventaario")
    print("tarkista <esine>   - Tarkista esineen kuvaus")
    print("lataa <e1> <e2>    - Lataa esine (esim. kivääri, taskulamppu)")
    print("syö <esine>        - Syö esine (jos mahdollista)")
    print("pue <esine>        - Pue esine päällesi")
    print("lue <esine>        - Lue esine")
    print("lopeta             - Lopeta peli")
    print("--------------------------------")
    print()
