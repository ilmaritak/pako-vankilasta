# Author: Ilmari Takkunen
# Github: ilmaritak
#
#
from utils import handle_commands, add_score
from items import inventory

# Vankiselli
def room1():
    room_name = "room1"
    room_description = "Olet omassa sellissäsi. Ovesi itään on auki. "

    direction = handle_commands(room_name, room_description, valid_dirs=['i'])

    if direction == 'i':
        room2()

# Tyrmän käytävä
def room2():
    room_name = "room2"
    room_description = (
        "Olet hämärässä käytävässä. "
        "Lännessä on ovi selliin, etelässä vartijan koppi, "
        "pohjoisessa portaikko ja idässä siivouskomero. "
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
        "Olet vartijan kopissa. Sinun onneksesi vartija ei ole paikalla. "
        "Pohjoisessa on ovi takaisin käytävään. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room2()

# Siivouskomero
def room4():
    room_name = "room4"
    room_description = (
        "Olet siivouskomerossa. "
        "Komerossa haisee ummehtunut ja jokapuolella on likaisia siivousvälineitä. "
        "Lännessä on ovi takaisin käytävään. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l'])

    if direction == 'l':
        room2()


# Portaikko
def room5():
    room_name = "room5"
    room_description = (
        "Olet yläkertaan johtavassa portaikossa. "
        "Poistumalla itään pääset yläkertaan. "
        "Poistumalla etelään pääset takaisin alakerran käytävään. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['e', 'i'])

    if direction == 'e':
        room2()
    if direction == 'i':
        room6()

# 2. kerroksen käytävä
def room6():
    room_name = "room6"
    room_description = (
        "Olet hyvin valaistussa käytävässä. "
        "Pohjoisessa on ovi vankilanjohtajan toimistoon, "
        "Etelässä on ruokavarasto ja idässä on ovi parvekkeelle. "
        "Lännestä pääset takaisin potaikkoon. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room5()
    if direction == 'e':
        room7()
    if direction == 'i':
        room10()
    if direction == 'p':
        if "avain" not in inventory:
            print("Ovi on lukossa. Tarvitset avaimen päästäksesi vankilanjohtajan toimistoon.")
            return room6()
        else:
            print("Avaat oven avaimella.")
            inventory.remove("avain")
            add_score(10)
            room8()

# Ruokavarasto
def room7():
    room_name = "room7"
    room_description = (
        "Olet vankien ruokavarastossa. "
        "Tuoksuu ummehtuneelle ja pilantuneelle ruoalle. "
        "Hyllyt ovat pullollaan erilaisia vangeille tarkoitettuja ruokia. "
        "Pohjoisessa on ovi takaisin käytävään. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room6()

# Toimisto
def room8():
    room_name = "room8"
    room_description = (
        "Olet vankilanjohtajan toimistossa. "
        "Huoneessa on työpöytä ja hyllyjä täynnä erilaisia asiakirjoja. "
        "Etelässä on ovi takaisin käytäävään ja idässä on ovi asevarastoon. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['e', 'i'])

    if direction == 'e':
        room6()
    if direction == 'i':
        room9()

# Asevarasto
def room9():
    room_name = "room9"
    room_description = (
        "Olet asevarastossa. "
        "Ympärilläsi on lukittuja kaappeja täynnä vartijoiden käyttämiä aseita. "
        "Lännessä on ovi takaisin toimistoon. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l'])

    if direction == 'l':
        room8()

# Parveke
def room10():
    room_name = "room10"
    room_description = (
        "Olet parvekkeella. "
        "Näet vankilan pihamaan ja kaukaisuudessa olevat vankilan muurit. "
        "Etelässä on ovi paloportaikkoon ja lännestä pääset takaisin käytävään. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e'])

    if direction == 'l':
        room6()
    if direction == 'e':
        room11()

# Paloportaikko
def room11():
    room_name = "room11"
    room_description = (
        "Olet paloportaikossa. "
        "Portaikko on ruostunut ja rämisevä. "
        "Poistumalla itään pääset pääaulaan, pohjoisesta pääset takaisin parvekkeelle. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p', 'i'])

    if direction == 'i':
        room12()
    if direction == 'p':
        room10()

# Pääaula
def room12():
    room_name = "room12"
    room_description = (
        "Olet avarassa pääaulassa."
        "Aula on hyvin valaistu ja seinät on koristeltu kauniilla maalauksilla. "
        "Etelässä on ovi parkkihalliin, pohjoisessa on vartijoiden taukohuone. "
        "Idässä on on pääovien eteistila ja lännestä pääset takaisin paloportaisiin. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room11()
    if direction == 'e':
        room13()
    if direction == 'i':
        room14()
    if direction == 'p':
        room15()

# Parkkihalli
def room13():
    room_name = "room13"
    room_description = (
        "Olet viileässä parkkihallissa. "
        "On autiota ja autoja ei näy missään. "
        "Idässä on uloskäynti tankkausasemalle, pohjoisesta pääset takaisin pääaulaan. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p', 'i'])

    if direction == 'i':
        room17()
    if direction == 'p':
        room12()

# Uloskäynnin eteinen
def room14():
    room_name = "room14"
    room_description = (
        "Olet uloskäynnin eteisessä. "
        "Seinällä on ilmoitustaulu täynnä erilaisia ilmoituksia ja mainoksia. "
        "Idässä on uloskäynti sisäpihalle, lännestä pääset pääaulaan. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'i'])

    if direction == 'l':
        room12()
    if direction == 'i':
        room17()

# Vartijoiden taukohuone
def room15():
    room_name = "room15"
    room_description = (
        "Olet vartijoiden taukohuoneessa. "
        "Huoneessa on likainen pöytä täynnä ruoan jämiä ja kahviläikkiä. "
        "Joka paikka on hujanhajan erilaisia varusteita ja roskia. "
        "Pohjoisessa on ovi vartijoiden pukuhuoneeseen, etelästä pääset takaisin pääaulaan. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['e', 'p'])

    if direction == 'e':
        room12()
    if direction == 'p':
        room16()

# Vartijoiden pukuhuone
def room16():
    room_name = "room16"
    room_description = (
        "Olet vartijoiden pukuhuoneessa. "
        "Huoneessa haisee hiki ja ilma on raskas. Seinillä on avonaisia pukukaappeja. "
        "Etelästä pääset takaisin taukohuoneeseen. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['e'])

    if direction == 'e':
        room15()

# Sisäpiha
def room17():
    room_name = "room17"
    room_description = (
        "Olet vankilan sisäpihalla. "
        "Ilma on raikas ja aurinko lämmittää mukavasti. "
        "Pohjoisessa on tankkausasema vanginkuljetusautoja varten. "
        "Etelässä on portinvartijan koppi ja Idässä on portit ulos vankilasta. "
        "Lännestä pääset pääovien eteistilaan. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e', 'p', 'i'])

    if direction == 'l':
        room14()
    if direction == 'e':
        room18()
    if direction == 'i':
        room20()
    if direction == 'p':
        room19()

# Portinvartijan koppi
def room18():
    room_name = "room18"
    room_description = (
        "Olet portinvartijan kopissa. "
        "Kopissa on pieni pöytä, jossa on tietokone ja donitsin muruja. "
        "Pohjoisesta pääset takaisin sisäpihalle. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['p'])

    if direction == 'p':
        room17()

# Tankkausasema
def room19():
    room_name = "room19"
    room_description = (
        "Olet tankkausasemalla. "
        "Täällä tankataan vankienkuljetusautot. "
        "On autiota ja lattialla on öljyläikkiä. "
        "Etelästä pääset sisäpihalle, lännestä pääset parkkihalliin. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'e'])

    if direction == 'l':
        room13()
    if direction == 'e':
        room17()

# Ulkoamaailma
def room20():
    room_name = "room20"
    room_description = (
        "Olet vankilan ulkopuolla. "
        "Näet loputtomiin jatkuvan vankilan ympärille levittyvän metsän. "
        "On kaunista. "
        "Liikkumalla itään olet vapaa. "
        "Lännestä pääset takaisin sisäpihalle. "
    )

    direction = handle_commands(room_name, room_description, valid_dirs=['l', 'i'])

    if direction == 'l':
        room17()
    if direction == 'i':
        room17()
