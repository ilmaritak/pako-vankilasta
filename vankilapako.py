# Author: Ilmari Takkunen
# Github: ilmaritak
#
#

def welcome():
    print()
    print("Tervetuloa vankilaan. Tehtävänäsi on paeta vankilasta onnistuneesti.")
    player = input("Mikä sinun nimesi on: ")
    print()
    print(f"Hei {player}! ")
    print("Vankilasta on katkennut sähköt ja huomaat ovesi sähkölukon olevan auki.")
    print("Muutenkin ympäristö vaikuttaa autiolta.")

def which_direction(options):
    while True:
        go = input(f"Mihin suuntaan haluat liikkua: ")

        if go == "": continue
        go = go[0].lower()

        if go in options:
            return go
        else:
            print("Et voi liikkua sellaiseen suuntaan.")

inventory = []

items = {
    "avain": {
        "location": "room1",
        "description": "Ruosteinen avain, ehkä se avaa jonkun oven."
    },
    "taskulamppu": {
        "location": "room2",
        "description": "Vanha taskulamppu. Voisi olla hyödyllinen pimeissä paikoissa."
    }
}

def show_inventory():
    print()
    if inventory:
        print("Sinulla on mukana:")
        for item in inventory:
            print(f" - {item}")
    else:
        print("Sinulla ei ole mitään mukana.")


def look(room_name, room_description):
    print()
    print(room_description)
    print()

    # Näytä esineet jotka ovat tässä huoneessa
    here_items = [item for item in items if items[item]["location"] == room_name]

    if here_items:
        print("Näet täällä:")
        for i in here_items:
            print(f" - {i}: {items[i]['description']}")
    else:
        print("Täällä ei näytä olevan mitään erikoista.")

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


def drop_item(item_name, room_name):
    if item_name not in inventory:
        print("Ei ole sinulla sellaista.")
        return

    inventory.remove(item_name)
    items[item_name]["location"] = room_name
    print(f"Pudotit esineen: {item_name}")

def handle_commands(room_name, room_description, valid_dirs):
    look(room_name, room_description)  # Näytä alkuun

    while True:
        cmd = input("> ").strip().lower()

        # yksisanaiset komennot
        if cmd in ["katsele", "tutki"]:
            look(room_name, room_description)

        elif cmd == "mukana":
            show_inventory()

        elif cmd == "lopeta":
            print("Peli päättyy.")
            exit()

        # kaksisanaiset komennot
        elif cmd.startswith("ota "):
            item = cmd[4:]
            take_item(item, room_name)

        elif cmd.startswith("pudota "):
            item = cmd[7:]
            drop_item(item, room_name)

        # liikkuminen
        elif cmd.startswith("mene "):
            direction = cmd[5]

            if direction in valid_dirs:
                return direction
            else:
                print("Et voi mennä siihen suuntaan.")

        else:
            print("En ymmärrä komentoa.")


# Vankiselli
def room1():
    room_name = "room1"
    room_description = "Olet omassa sellissäsi. Ovesi itään on auki."

    direction = handle_commands(room_name, room_description, valid_dirs=['i'])

    if direction == 'i':
        room2()

# Tyrmän käytävä
def room2():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero."
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room1()
    if direction == 'e':
        room3()
    if direction == 'i':
        room4()
    if direction == 'p':
        room5()

# Vartijan koppi
def room3():
    room_name = "room3"
    room_description = (
        "Olet vartijan kopissa. Sinun onneksesi vartija ei ole paikalla "
        "Pohjoisessa on ovi takaisin käytävään "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room2()

welcome()
room1()
