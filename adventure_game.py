import time
import random
from datetime import datetime

weapon = "hand stunner"
planet = random.choice(["WOO", "ATLAS"])
aliens = random.choice(["WOOtarians", "ATLASIANS"])


def greeting():
    if datetime.today().hour > 18:
        return "Evening"
    else:
        return "Day"


print(greeting())


def confirmation(message):
    for n in range(len(message)):
        print(message[n])
        time.sleep(1)


def print_pause(statement):
    print(statement)
    time.sleep(2)


def intro():
    print_pause("!!!WELCOME---TO---SPACE---QUEST!!!")
    print_pause(f"Good {greeting()} Captain")
    print_pause("We have taken damage warping through a meteor field..")
    print_pause("Our systems and navigation are down...")
    print_pause(f"The {aliens} have detected our presence \n and are moving in \
    on our position to take over the ship ")
    print_pause(f"You look at your trusty {weapon}, which you haven't used in \
    years..")
    print_pause("With the odds against you, will you fight? or try to crash \
    land?")
    time.sleep(1)


def command_center(arsenal):
    response = input(f"Enter command: \n(1) Fight the {aliens} "
                     "\n(2) Crash land the ship\n")
    if response == "1":
        print_pause(f"You stun the {aliens} \n"
                    "They flea in fear..")
        print_pause("This trusty old hand stunner still proves effective")
        confirmation("YOU ARE A HERO")
    elif response == "2":
        print_pause(f"You crash land onto planet {planet}")
        print_pause("Everyone is safe")
        print_pause(f"After several days on planet {planet},\n You're able to \
        get the ship repaired")
    else:
        print_pause("We don't have time for error!")
        command_center(arsenal)


def game_restart():
    print_pause("\n Do you want to go on another Space Quest?")
    restart = input("Select an input:\n(1) yes\n(2) no\n")
    if restart == "1":
        print_pause("Initiating sequence")
        print_pause("starting in")
        confirmation("321")
        space_quest()
    elif restart != "2":
        print_pause("NO time for ERRORS! Please enter a valid input\n")
        game_restart()
    else:
        print_pause("Thanks for playing!")


def space_quest():
    arsenal = []
    intro()
    command_center(arsenal)
    game_restart()


space_quest()

