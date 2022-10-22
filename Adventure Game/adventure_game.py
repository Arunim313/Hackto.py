# IMPORT STATEMENTS
import time
import random

# FUNCTIONS
# print scene lines and timer


def print_pause(scene):
    for text in scene:
        print(text)
        time.sleep(2)
# knock function


def knock():
    print_pause(knock_scenario)

# peer function


def peer():
    print_pause(peer_scenario)

# multiple peer function


def double_peer():
    print_pause(double_peer_scenario)

# fight and win function


def fight_win():
    print_pause(fight_win_scenario)

# fight and lose function


def fight_lose():
    print_pause(fight_lose_scenario)

# run function


def run():
    print_pause(run_scenario)

def rematch():
    while True:
        print("would you like to play again? (y/n)")
        rematch = input()
        if rematch == 'y':
            print("Excellent! restarting the game")
            game()
        elif rematch == 'n':
            quit()
        else:
            print("would you like to play again? (y/n)")
            rematch = input()

# START GAME FUNCTION


def game():
    print_pause(game_scenario1)
    print_pause(choices)
    knock_selection()

# GENERAL CHOICE PROCESS / AFTER MAKING KNOCKING FIRST CHOICE


def knock_selection():
    while True:
        print("(Please enter 1 or 2.)")
        choice = input()
        # IF USER KNOCKS
        if choice == '1':
            knock()
            print("Would you like to (1) fight or (2) run away?")
            second_choice = input()
            # IF USER FIGHTS AND LOSES
            while True:
                if second_choice == '1':
                    fight_lose()
                    # REMATCH
                    rematch()
                # IF USER RUNS AFTER KNOCKING AND SEEING CREATURE
                elif second_choice == '2':
                    run()
                    # ASK USER TO KNOCK OR PEER AGAIN
                    print_pause(choices)
                    knock_selection()
                else:
                    print("Would you like to (1) fight or (2) run away?")
                    second_choice = input()

        # IF USER PEERS
        elif choice == '2':
            peer()
            # AFTER GETTING WEAPON, ASK USER TO KNOCK OR PEER AGAIN
            peer_selection()

        else:
            print("(Please enter 1 or 2.)")
            choice = input()

# peer function after making peering first choice


def peer_selection():

    print_pause(choices)
    while True:
        print("(Please enter 1 or 2.)")
        choice2 = input()
        # IF USER KNOCKS
        if choice2 == '1':
            knock()
            while True:
                print("Would you like to (1) fight or (2) run away?")
                peer_choice = input()
                # IF USER FIGHTS AND WINS
                if peer_choice == '1':
                    fight_win()
                    # REMATCH
                    rematch()
                # IF USER RUNS
                elif peer_choice == '2':
                    run()
                    peer_selection()
        # IF USER PEERS MULTIPLE TIMES
        elif choice2 == '2':
            double_peer()
            peer_selection()


# RANDOM CHOICES FOR WEAPONS AND MONSTERS
creature = random.choice(
    ['dragon', 'gorgon', 'beast', 'goblin', 'large snake', 'witch'])
weapon = random.choice(['sword', 'knife', 'blade', 'trowel', 'magic scissor'])
treasure = random.choice(['Sword of Tripata', 'Knife of Brazar',
                         'Blade of Odysseus', 'Lightning',
                          'Rod of Zeus', 'Dagger of Athena'])
damage = random.randint(1, 10)

# SCENE LIST FOR DIFFERENT SCENARIOS
game_scenario1 = ["You find yourself standing in an open field, filled",
                  "with grass and yellow wildflowers.",
                  "Rumor has it that a " + creature +
                  " is somewhere around here, and",
                  "has been terrifying the nearby village.",
                  "In front of you is a house.",
                  "To your right is a dark cave.",
                  "In your hand you hold your",
                  "trusty (but not very effective) " +
                  weapon + " that",
                  "deals just " + str(damage)+" points damage.", " "]

knock_scenario = ["You approach the door of the house.",
                  "You are about to knock when the",
                  "door opens and out steps a " + creature+".",
                  "Eep! This is the "+creature+"'s house!",
                  "The "+creature+" attacks you!"]

peer_scenario = ["You peer cautiously into the cave.",
                 "It turns out to be only a very small cave.",
                 "Your eye catches a glint behind a rock.",
                 "You have found the "+treasure+"!",
                 "You discard your silly old "+weapon +
                 " and take the "+treasure+" with you.",
                 "You walk back out to the field."]

fight_win_scenario = ["As the "+creature+" moves to attack, you",
                      "unsheath your new sword.",
                      "The "+treasure + " shines brightly in your",
                      "hand as you brace yourself for the attack.",
                      "But the "+creature +
                      " takes one look at your shiny new toy and runs away!",
                      "You have rid the town of the "+creature+".",
                      "You are victorious!"]

fight_lose_scenario = ["You do your best...",
                       "but your " + weapon + " is no",
                       "match for the "+creature+".",
                       "You have been defeated!"]

run_scenario = [
    "You run back into the field. Luckily,",
    "you don't seem to have been followed."]

double_peer_scenario = ["You peer cautiously into the cave.",
                        "You've been here before, and gotten",
                        "all the good stuff. It's just an empty cave now.",
                        "You walk back out to the field."]


choices = ["\nEnter 1 to knock on door",
           "Enter 2 to peer into the cave", "What would you like to do?"]


# START GAME FUNCTION CALL
game()
