#Game Name: Dungeon Shenanigans

#Imports.
import time
import random

#Definitions.
#Randomly chosen of 1-3 doors when room is cleared.
def doors():
    amount = random.randint(1, 3)

    if amount == 1:
        options = ["straight"]
        print("There is only 1 way... Straight.\n")

    elif amount == 2:
        options = random.choice([["straight", "right"], ["straight", "left"], ["left", "right"]])
        print(f"Seems the path grows. {options[0]} or {options[1]}.\n")

    else:
        options = ["straight", "right", "left"]
        print("3 doors stand before you. Left, Straight, and Right.\n")

    while True:
        choice = input("Which way do you go? ").lower().strip()

        if choice in options:
            print(f"\nYou carefully open the {choice} door...\n")
            time.sleep(2)
            return choice

        else:
            print(f"You gotta pick bro.\n")
            time.sleep(1)
            print("You do know you \033[31mcan't leave\033[0m 'till you clear the \033[30mdungeon\033[0m, right?")

def weak_attack():
    global HP, name, inventory, maxHP
    global weak_enemy_name, weak_enemy_HP, weak_enemy_atk

    weak_enemy_name, weak_enemy_HP, weak_enemy_atk = spawn_weakenemy()

    print(f"You've encountered a \033[33m{weak_enemy_name}\033[0m with \033[32m{weak_enemy_HP}HP\033[0m!!")
    time.sleep(1)

    while True:
        user_input = input("What do you do? Flee/Fight: ").upper().strip()

        if user_input == "FLEE":
            if random.randint(1, 100) <= 35:
                print(f"\n\033[31mEscape failed!\033[0m The \033[33m{weak_enemy_name}\033[0m blocked your path. You have no choice but to fight!\n")
                time.sleep(1.5)
                break

            else:
                print("You managed to escape the \033[33menemy\033[0m. For now.")
                return

        elif user_input == "FIGHT":
            print(f"\nYou chose to fight the \033[33m{weak_enemy_name}\033[0m!!\n")
            time.sleep(0.7)
            break

        else:
            print("Invalid answer. Try again.")

    stunned = False

    while weak_enemy_HP > 0:
        user_input = input("Do you want to \033[31mattack\033[0m, \033[34mDefend\033[0m, or use a \033[32mPotion\033[0m?: ").upper().strip()

        if stone_sword == True and user_input == "ATTACK":
            dmg_dealt = sword1()
            weak_enemy_HP -= dmg_dealt

            if weak_enemy_HP < 0:
                weak_enemy_HP = 0

            print(f"\nYou slashed the {weak_enemy_name} for \033[31m{dmg_dealt} damage\033[0m. They're now at \033[32m{weak_enemy_HP}HP\033[0m.")
            time.sleep(1)

            if weak_enemy_HP <= 0:
                print(f"\nAlright, way to go \033[35m{name}\033[0m! You took the \033[33m{weak_enemy_name}\033[0m down. Now, let's look around and see if we can find anything \033[32museful\033[0m.")
                break

            else:
                if stunned:
                    print(f"The \033[33m{weak_enemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)
                else:
                    HP -= weak_enemy_atk
                    print(f"The \033[33m{weak_enemy_name}\033[0m strikes back for \033[31m{weak_enemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)

                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()

        elif stone_sword == True and user_input == "DEFEND":
            if stunned:
                print(f"The \033[33m{weak_enemy_name}\033[0m is \033[36mstunned\033[0m! You brace yourself, but no attack comes.\n")
                stunned = False
                time.sleep(1)

            else:
                current_def, current_dmg_taken = defend(weak_enemy_atk)
                HP -= current_dmg_taken

                print(f"\nYou defended against the \033[33m{weak_enemy_name}\033[0m and blocked {current_def}% of the damage. You took \033[31m{current_dmg_taken} damage\033[0m and are now at \033[32m{HP}HP\033[0m\n")
                time.sleep(1)

                if HP <= 0:
                    print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                    exit()

                if random.randint(1, 100) <= 20:
                    print(f"\033[36mPerfect Block!\033[0m You staggered the \033[33m{weak_enemy_name}\033[0m! It is stunned for the next turn.\n")
                    stunned = True
                    time.sleep(1.5)

        elif user_input == "POTION":
            if inventory["Health Potions"] > 0:
                inventory["Health Potions"] -= 1
                HP += random.randint(20, 50)

                if HP > maxHP:
                    HP = maxHP

                print(f"\nYou drank a Health Potion! You recovered HP and are now at \033[32m{HP}HP\033[0m. (Potions left: {inventory['Health Potions']})\n")
                time.sleep(1.5)

                if stunned:
                    print(f"The \033[33m{weak_enemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)
                else:
                    HP -= weak_enemy_atk
                    print(f"The \033[33m{weak_enemy_name}\033[0m strikes back for \033[31m{weak_enemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)
                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()
            else:
                print("\nYou reach into your bag, but you don't have any Health Potions left!\n")
                time.sleep(1)
                continue

        else:
            print("That's not an option. Try again.")

def average_attack():
    global HP, name, inventory, maxHP
    global avenemy_name, avenemy_HP, avenemy_atk

    avenemy_name, avenemy_HP, avenemy_atk = spawn_averageenemy()

    print(f"You've encountered a \033[33m{avenemy_name}\033[0m with \033[32m{avenemy_HP}HP\033[0m!!")
    time.sleep(1)

    while True:
        user_input = input("What do you do? Flee/Fight: ").upper().strip()

        if user_input == "FLEE":
            if random.randint(1, 100) <= 35:
                print(f"\n\033[31mEscape failed!\033[0m The \033[33m{avenemy_name}\033[0m blocked your path. You have no choice but to fight!\n")
                time.sleep(1.5)
                break
            else:
                print("You managed to escape the \033[33menemy\033[0m. For now.")
                return

        elif user_input == "FIGHT":
            print(f"\nYou chose to fight the \033[33m{avenemy_name}\033[0m!!\n")
            time.sleep(0.7)
            break
        else:
            print("Invalid answer. Try again.")

    stunned = False

    while avenemy_HP > 0:
        user_input = input("Do you want to \033[31mattack\033[0m, \033[34mDefend\033[0m, or use a \033[32mPotion\033[0m?: ").upper().strip()

        if iron_sword == True and user_input == "ATTACK" or stone_sword == True and user_input == "ATTACK":
            if stone_sword == True:
                dmg_dealt = sword1()

            elif iron_sword == True:
                dmg_dealt = sword2()

            avenemy_HP -= dmg_dealt

            if avenemy_HP < 0:
                avenemy_HP = 0

            print(f"\nYou slashed the {avenemy_name} for \033[31m{dmg_dealt} damage\033[0m. They're now at \033[32m{avenemy_HP}HP\033[0m.")
            time.sleep(1)

            if avenemy_HP <= 0:
                print(f"\nAlright, way to go \033[35m{name}\033[0m! You took the \033[33m{avenemy_name}\033[0m down. Now, let's look around and see if we can find anything \033[32museful\033[0m.")
                break

            else:
                if stunned:
                    print(f"The \033[33m{avenemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)

                else:
                    HP -= avenemy_atk
                    print(f"The \033[33m{avenemy_name}\033[0m strikes back for \033[31m{avenemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)

                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()

        elif stone_sword == True and user_input == "DEFEND" or iron_sword == True and user_input == "DEFEND":

            if stunned:
                print(f"The \033[33m{avenemy_name}\033[0m is \033[36mstunned\033[0m! You brace yourself, but no attack comes.\n")
                stunned = False
                time.sleep(1)

            else:
                current_def, current_dmg_taken = defend(avenemy_atk)
                HP -= current_dmg_taken

                print(f"\nYou defended against the \033[33m{avenemy_name}\033[0m and blocked {current_def}% of the damage. You took \033[31m{current_dmg_taken} damage\033[0m and are now at \033[32m{HP}HP\033[0m\n")
                time.sleep(1)

                if HP <= 0:
                    print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                    exit()

                if random.randint(1, 100) <= 20:
                    print(f"\033[36mPerfect Block!\033[0m You staggered the \033[33m{avenemy_name}\033[0m! It is stunned for the next turn.\n")
                    stunned = True
                    time.sleep(1.5)

        elif user_input == "POTION":

            if inventory["Health Potions"] > 0:
                inventory["Health Potions"] -= 1
                HP += random.randint(20, 50)

                if HP > maxHP:
                    HP = maxHP

                print(f"\nYou drank a Health Potion! You recovered HP and are now at \033[32m{HP}HP\033[0m. (Potions left: {inventory['Health Potions']})\n")
                time.sleep(1.5)

                if stunned:
                    print(f"The \033[33m{avenemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)

                else:
                    HP -= avenemy_atk
                    print(f"The \033[33m{avenemy_name}\033[0m strikes back for \033[31m{avenemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)

                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()
            else:
                print("\nYou reach into your bag, but you don't have any Health Potions left!\n")
                time.sleep(1)
                continue

        else:
            print("That's not an option. Try again.")

def strong_attack():
    global HP, name, inventory, maxHP
    global strenemy_name, strenemy_HP, strenemy_atk

    strenemy_name, strenemy_HP, strenemy_atk = spawn_strenemy()

    print(f"You've encountered a \033[33m{strenemy_name}\033[0m with \033[32m{strenemy_HP}HP\033[0m!!")
    time.sleep(1)

    while True:
        user_input = input("What do you do? Flee/Fight: ").upper().strip()

        if user_input == "FLEE":
            if random.randint(1, 100) <= 35:
                print(f"\n\033[31mEscape failed!\033[0m The \033[33m{strenemy_name}\033[0m blocked your path. You have no choice but to fight!\n")
                time.sleep(1.5)
                break
            else:
                print("You managed to escape the \033[33menemy\033[0m. For now.")
                return

        elif user_input == "FIGHT":
            print(f"\nYou chose to fight the \033[33m{strenemy_name}\033[0m!!\n")
            time.sleep(0.7)
            break
        else:
            print("Invalid answer. Try again.")

    stunned = False

    while strenemy_HP > 0:
        user_input = input("Do you want to \033[31mattack\033[0m, \033[34mDefend\033[0m, or use a \033[32mPotion\033[0m?: ").upper().strip()

        if obsidian_sword == True and user_input == "ATTACK" or stone_sword == True and user_input == "ATTACK" or iron_sword == True and user_input == "ATTACK":
            if stone_sword == True:
                dmg_dealt = sword1()

            elif iron_sword == True:
                dmg_dealt = sword2()

            elif obsidian_sword == True:
                dmg_dealt = sword3()

            strenemy_HP -= dmg_dealt

            if strenemy_HP < 0:
                strenemy_HP = 0

            print(f"\nYou slashed the {strenemy_name} for \033[31m{dmg_dealt} damage\033[0m. They're now at \033[32m{strenemy_HP}HP\033[0m.")
            time.sleep(1)

            if strenemy_HP <= 0:
                print(f"\nAlright, way to go \033[35m{name}\033[0m! You took the \033[33m{strenemy_name}\033[0m down. Now, let's look around and see if we can find anything \033[32museful\033[0m.")
                break
            else:
                if stunned:
                    print(f"The \033[33m{strenemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)
                else:
                    HP -= strenemy_atk
                    print(f"The \033[33m{strenemy_name}\033[0m strikes back for \033[31m{strenemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)
                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()

        elif stone_sword == True and user_input == "DEFEND" or iron_sword == True and user_input == "DEFEND" or obsidian_sword == True and user_input == "DEFEND":
            if stunned:
                print(f"The \033[33m{strenemy_name}\033[0m is \033[36mstunned\033[0m! You brace yourself, but no attack comes.\n")
                stunned = False
                time.sleep(1)
            else:
                current_def, current_dmg_taken = defend(strenemy_atk)
                HP -= current_dmg_taken

                print(f"\nYou defended against the \033[33m{strenemy_name}\033[0m and blocked {current_def}% of the damage. You took \033[31m{current_dmg_taken} damage\033[0m and are now at \033[32m{HP}HP\033[0m\n")
                time.sleep(1)

                if HP <= 0:
                    print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                    exit()

                if random.randint(1, 100) <= 20:
                    print(f"\033[36mPerfect Block!\033[0m You staggered the \033[33m{strenemy_name}\033[0m! It is stunned for the next turn.\n")
                    stunned = True
                    time.sleep(1.5)

        elif user_input == "POTION":
            if inventory["Health Potions"] > 0:
                inventory["Health Potions"] -= 1
                HP += random.randint(20, 50)

                if HP > maxHP:
                    HP = maxHP

                print(f"\nYou drank a Health Potion! You recovered HP and are now at \033[32m{HP}HP\033[0m. (Potions left: {inventory['Health Potions']})\n")
                time.sleep(1.5)

                if stunned:
                    print(f"The \033[33m{strenemy_name}\033[0m is \033[36mstunned\033[0m and won't be able to attack this turn!\n")
                    stunned = False
                    time.sleep(1)
                else:
                    HP -= strenemy_atk
                    print(f"The \033[33m{strenemy_name}\033[0m strikes back for \033[31m{strenemy_atk} damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")
                    time.sleep(1)
                    if HP <= 0:
                        print("\n\033[31mYou have been defeated... Game Over.\033[0m")
                        exit()
            else:
                print("\nYou reach into your bag, but you don't have any Health Potions left!\n")
                time.sleep(1)
                continue
        else:
            print("That's not an option. Try again.")

def defend(enemy_atk):
    defense = random.randint(30, 100)
    final_dmginput = int(round(enemy_atk * (1 - defense / 100)))

    return defense, final_dmginput


#First sword (Stone).
def sword1():
    damage = random.randint(7, 13)
    return damage


#Second Sword (Iron).
def sword2():
    damage = random.randint(17, 25)
    return damage


#Thrid Sword (Obsidian).
def sword3():
    damage = random.randint(35, 50)
    return damage

def potion_event():
    global inventory, name

    if random.randint(1, 100) <= 35:
        print(f"\033[35m{name}\033[0m, look! A potion!")
        time.sleep(1)
        print("It's \033[32mgreen\033[0m, so it must be a \033[32mhealing\033[0m potion. I don't know what else would be \033[32mgreen\033[0m in a bottle.")

        while True:
            user_input = input("Do you want to take it?: ").upper().strip()

            if user_input in ["Y", "YES", "SURE", "YEA"]:
                inventory["Health Potions"] += 1
                time.sleep(1.2)
                print(f"\n\033[32m[Health Potion added to dimensional pocket.]\n[Current Health Potions: {inventory['Health Potions']}.]\033[0m\n")
                break

            elif user_input in ["N", "NO", "NAH", "NOPE"]:
                confirm = input("Are you really sure? This could be a very valuable item in your journey. (\033[32mY\033[0m to leave it / \033[31mN\033[0m to take it): ").upper().strip()

                if confirm in ["Y", "YES", "SURE", "YEA"]:
                    print("\nAlright, your choice. I would've taken it if I were you. Who knows how \033[32museful\033[0m it could've been.")
                    break

                elif confirm in ["N", "NO", "NAH", "NOPE"]:
                    print("\nSmart choice! [You take the potion.]")
                    inventory["Health Potions"] += 1
                    time.sleep(1.2)
                    print(f"\n\033[32m[Health Potion added to dimensional pocket.]\n[Current Health Potions: {inventory['Health Potions']}.]\033[0m\n")
                    break

                else:
                    print("\nI didn't understand that. Let's try that again...\n")
                    continue

            else:
                print("\nThat's not an option. Try again.\n")

#Which starter enemy spawns, if one does.
def spawn_weakenemy():
    weak_enemy_stats = {
        "Slime": 8,
        "Skeleton": 13,
        "Zombie": 17,
        "Mutated Rat": 20
    }

    weak_enemy_name = random.choice(list(weak_enemy_stats.keys()))
    weak_enemy_HP = random.randint(10, 28)
    weak_enemy_atk = weak_enemy_stats[weak_enemy_name]
    return weak_enemy_name, weak_enemy_HP, weak_enemy_atk


#Which average enemy spawns, if one does.
def spawn_averageenemy():
    avenemy_stats = {
        "Lava Hound": 25,
        "Poisonous Slime": 28,
        "Merciless Archer": 30,
        "Ghoul": 33
    }

    avenemy_name = random.choice(list(avenemy_stats.keys()))
    avenemy_HP = random.randint(30, 50)
    avenemy_atk = avenemy_stats[avenemy_name]
    return avenemy_name, avenemy_HP, avenemy_atk


#Which strong enemy spawns, if one does.
def spawn_strenemy():
    strenemy_stats = {
        "Gladiator": 36,
        "Irradiated Mole": 39,
        "Rat/Bird Hybrid": 43,
        "Lycaon": 47
    }
    strenemy_name = random.choice(list(strenemy_stats.keys()))
    strenemy_HP = random.randint(50, 75)
    strenemy_atk = strenemy_stats[strenemy_name]
    return strenemy_name, strenemy_HP, strenemy_atk


#Variables.
HP = int(100)
maxHP = int(120)
inventory = {"Health Potions": 0}
stone_sword = sword1() and True
iron_sword = sword2() and False
obsidian_sword = sword3() and False

#Game start.
#Enter your username.
while True:
    name = input("\n\nWhat is your \033[35musername\033[0m?: ").strip()

    if name == "":
        time.sleep(1)
        print("\n......")
        time.sleep(1.2)
        print("\nOh come on. Everyone's got a \033[35mname\033[0m.\n")
        time.sleep(1)

    else:
        break

#Welcome message.
print(f"Welcome, \033[35m{name}\033[0m!\n")
time.sleep(1)
print("This is the \033[30mdungeon\033[0m \033[32mentrance\033[0m. Big choice coming here, you've got guts.\nWhat do we say we \033[32menter\033[0m the \033[30mdungeon\033[0m eh?\n")
time.sleep(3)

#Whether or not you want to play.
while True:
    user_input = input("Would you like to \033[32menter\033[0m the \033[30mdungeon\033[0m? (\033[32mY\033[0m/\033[31mN\033[0m): ")

    if user_input.upper().strip() == "Y" or user_input.upper().strip() == "YES":
        print("\nYou entered the \033[30mdungeon\033[0m.\n")
        break

    elif user_input.upper().strip() == "N" or user_input.upper().strip() == "NO":
        print("You \033[31mleft\033[0m the dungeon \033[32mentrance\033[0m.")
        time.sleep(1.5)
        print("\033[31mWuss...\033[0m")
        exit()

    else:
        print("Invalid choice. Please type \033[32mY\033[0m or \033[31mN\033[0m.")

time.sleep(1.5)

#Quick HP tutorial.
print(f"Before you start making any \033[33mdecisions\033[0m, let me get you situated with the \033[32mHit Point\033[0m system. \033[32m(HP)\033[0m")
time.sleep(2)
print(f"Currently you have \033[32m{HP}HP\033[0m. Eventually you'll see that this number goes just a bit higher than 100.\nWhen you encounter \033[31menemies\033[0m this will be a crucial part in fighting them, as when your \033[32mHP\033[0m hits zero..")
time.sleep(2)
print("\n\033[31mGame Over\033[0m.\n")
time.sleep(3)
print("So, try your best and think about your \033[33mchoices.\033[0m\n")
time.sleep(1.5)

#Door sequences.
#Door 1
doors()

if random.randint(1, 100) <= 35:
    weak_attack()
else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 2
doors()

if random.randint(1, 100) <= 35:
    weak_attack()
else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 3
doors()

if random.randint(1, 100) <= 35:
    weak_attack()
else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 4
doors()

if random.randint(1, 100) <= 35:
    weak_attack()
else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 5
doors()

print(f"\033[35m{name}\033[0m, LOOK!! It looks like a new \033[37msword\033[0m over there in the corner.\nLet's check it out!")

while True:
    user_input = input("The sword looks like it's made of iron. A strong metal for sure.\nDo you want to take it?: ").upper().strip()

    if user_input == "YES" or user_input == "Y" or user_input == "SURE":
        stone_sword = False
        iron_sword = True
        print("You grab the iron sword by its grip and feel more \033[32mpowerful\033[0m then before. You don't need your old one anymore.")
        break

    elif user_input in ["N", "NO", "NAH"]:
        confirm = input("You're kidding right? This is certainly something \033[32mextremely valuable\033[0m. Are you certain?: ").upper().strip()

        if confirm in ["Y", "YES", "SURE", "YUP"]:
                    print("\nYou astound me... You should've taken that. Who knows how \033[36mpowerful\033[0m it could've been.")
                    break

        elif confirm in ["N", "NO", "NAH"]:
                    print("\nSmart choice! [You take the sword and leave the old one behind.]")
                    stone_sword = False
                    iron_sword = True
                    time.sleep(1.2)
                    break

        else:
            print("I didn't quite catch that. Please try again.")
            continue

    else:
        print("Please try again.")

if random.randint(1, 100) <= 50:
    average_attack()

else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 6
doors()

if random.randint(1, 100) <= 50:
    average_attack()

else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 7
doors()

if random.randint(1, 100) <= 50:
    average_attack()

else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 8
doors()


while True:
    if user_input == "YES" or user_input == "Y" or user_input == "SURE":
        stone_sword = False
        iron_sword = False
        obsidian_sword = True
        print("You grab the obsidian sword by its grip and feel the \033[32mpowerful\033[0m energy course through you. You don't need your Iron Sword anymore one anymore.\n[\033[32mEquipped Obsidian Sword\033[0m")
        break

    elif user_input in ["N", "NO", "NAH"]:
        confirm = input("You're kidding right? This is certainly something \033[32mextremely valuable\033[0m. Are you certain?: ").upper().strip()

        if confirm in ["Y", "YES", "SURE", "YUP"]:
                    print("\nYou astound me... You should've taken that. Who knows how \033[36mpowerful\033[0m it could've been.")
                    break

        elif confirm in ["N", "NO", "NAH"]:
                    print("\nSmart choice! [You take the sword and leave the Iron one behind.]")
                    stone_sword = False
                    iron_sword = False
                    obsidian_sword = True
                    time.sleep(1.2)
                    break

        else:
            print("I didn't quite catch that. Please try again.")
            continue

    else:
        print("Please try again.")

if random.randint(1, 100) <= 60:
    strong_attack()

else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 9
doors()

if random.randint(1, 100) <= 60:
    strong_attack()

else:
    print("The room seems to be \033[32msafe.\033[0m")

potion_event()

#Door 10
doors()

print("\nYou step into a dimly lit room. In the center sits a massive stone \033[33mSphinx\033[0m.")
time.sleep(1.5)
print("Its stone eyes suddenly glow red, and a booming voice echoes in your mind.")
time.sleep(1.5)
print(f"'Halt, \033[35m{name}\033[0m. To earn my blessing, you must answer my riddle with a single number.'")
time.sleep(1.5)
print("'If you multiply me by 5 and subtract 10, you get 40. What number am I?'\n")

while True:
    user_input = input("Enter your answer (Type a number): ").strip()

    # We shrink the try-block so it ONLY tests the conversion
    try:
        answer = int(user_input)
    except:
        # If they type words, it triggers this and restarts the loop immediately
        print("\n\033[31mThe Sphinx roars: 'I SAID A NUMBER! Do not test my patience with words!'\033[0m\n")
        time.sleep(1)
        continue


    if answer == 10:
        print("\nThe Sphinx nods slowly. 'You possess wisdom. Take this, and proceed.'")
        time.sleep(1)
        inventory["Health Potions"] += 1
        print(f"\033[32m[Health Potion added to dimensional pocket.]\n[Current Health Potions: {inventory['Health Potions']}.]\033[0m\n")
        break

    else:
        print("\nThe Sphinx narrows its eyes. 'Incorrect. Try again, mortal.'")
        time.sleep(1)
        HP -= 5
        print(f"A magical zap strikes you for \033[31m5 damage\033[0m! You are now at \033[32m{HP}HP\033[0m.\n")

        if HP <= 0:
            print("\n\033[31mYou have been defeated by your own lack of math skills... Game Over.\033[0m")
            exit()

print("Thank you for playing \"Dungeon Shenanigans\"")
exit()
