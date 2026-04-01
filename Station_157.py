# Game Name: Station 157



#imports
import random
import time
#name of astronaut and inventory
user_name = input("\nWhat is your name astronaut? ")
print("\t Inventory \n1 item: Knife")

#health and items found
hp = 200
knife = 25
acid_knife = 50
meds = 40
rusted_knife = 75
endgame_knife = 100
weapon = knife
friend = False
friend_dmg = 40
cw_weapon = "knife"

#asks if basic instructions are understood

while True:
    understand = input(f"Hello, {user_name.strip().lower()} your task is to retrive classifed files in the control room from the old space station. Do you under stand?(hint say yes) y/n ")

    if str(understand.strip().lower()) == "y" or str(understand.strip().lower()) == "yes":
        print("\nOnce retrived return to your capsule to leave. Good luck astronaut mysterys await \nOld supplys should be left behind on station 10011101")
        break
    elif str(understand.strip().lower()) == "n" or str(understand.strip().lower()) == "no":
        print("\nToo bad. Go in blind.")
        break
    else:
        print("Invalid input try again. ")
    continue
#narator telling you that youve offically docked
print("Docking with docking bay 4... \nDocking sequence completed. \nCapsule door opening. \n ")

print(f"You see the old rusted interior of the long hallway esitmated 50m in length. You see a hallway leading left, another right and straight. \nFrom the left you hear these strange sounds through the door.\nFrom the right you hear the geiger counter going off the charts far past 100000 Millisieverts. \nLastly you see that you can continue forward to what looks like a small observatory.\n")

while True:
    hallway_choice1 = input("Which direction do you wish to search? left, right or straight/forward ")


    #directions - left
    if str(hallway_choice1.strip().lower()) == "left" or str(hallway_choice1.strip().lower()) == "l":
        print ("\n You've entered the research lab, you finally know what was making those sounds... \n\n  A Large Radioactive Crow: You must fight.")
        crow_hp = 50
        player_dodging = False

        while hp > 0 and crow_hp > 0:
            print(f"\nYour HP: {hp} | Enemy HP: {crow_hp}")
            choice = input("Choose: attack or dodge? ")

        #if attack
            if choice.lower().strip() == "a" or choice.lower().strip() == "attack":
                crow_hp -= knife
                print(f"You hit the crow for {knife} damage!")

        #dodge option
            elif choice.lower().strip() == "d" or choice.lower().strip() == "dodge":
              player_dodging = True
            else:
                print("Invalid choice, you float and do nothing!!!")
        #enemy phase
            if crow_hp > 0:
                print("Crow attacks..")
                if random.random() < 0.2:
                    print("The Crow spit, but missed you completely.")

                elif player_dodging and random.random() < 0.5:
                    print("You successfully dodged the Crows acid")

                else:
                    hp-= 20
                    print("You took 20 damage!")
            player_dodging = False
        #END BATTLE
        if hp > 0:
            print("\nYou beat the Crow... It dropped an acid knife and medicine")
            print("You pick up the medicine.")

        else:
            print("\nYou died. Game Over.")
            break
        #options now for vent or back out to the observitory
        while True:
            inv = input("Do you wish to pick up acid knife? y/n")
            if inv.strip().lower() == "y" or inv.strip().lower() == "yes":
                weapon = acid_knife
                cw_weapon = "Acid Knife"
                print("You picked up the acid knife it does 50 damage...")
                print("\nInventory \n2 Items: Knife and Acid Knife")
                #heal chance
                healingstat = input("\nYour read the lable on the old medicine it says they are long expired by 10 years.\n Do you use them?(NOTE: this is the one chance to heal.) y/n")
                if healingstat.strip().lower() == "y" or healingstat.strip().lower() == "yes":
                    hp +=40
                    print("You take the meds.....\n\n\nYour lucky some medication last 15 years after best before date, you still have extra")
                else:
                    print("You leave the expire medication on the floor...")
            else:
                print("You dont use it.")
                print("\nInventory \n1 Items: Knife ")
             #choice vent
            vent_choice = input(f"You see a vent do you wish to enter it or leave and go back to the observitory? ")
            if vent_choice.strip().lower() == "v" or vent_choice.strip().lower() == "vent":
                print("Entered vent")

                #control room
                print("\nYou crawl through the vent listening to all the mechanical sounds")
                print("\nYou've entered the Control room, looking like a 90's show nasa contorl room.")
                lastc1 = input("Do you wish to grab the USB stick? y/n")
                if lastc1.strip().lower() == "y" or lastc1.strip().lower() == "yes":
                    print("You grab the USB stick...")

                else:
                    print("Too Bad, you grab the USB stick regardless")

                print("As you walk around the control room you notice this werid thin tall fuzzy leg in a different doorway that leads to the large Observitory")
                print("\nYou walk towards it. The stations lights go out for a bief second and the hatch is empty now, nothing blocking it. It looks as if it has still been sealed for decades")
                print("")

                #secret code
                door_locked = True
                secret_code = 157
                print("You find a terminal along with a log book it contains binary codes.")
                print("11111111 | 01110110 | 00000001 | 11110000")
                while door_locked:
                    user_input = input("\nEnter the 3-digit override code: ")
                    try:
                        guess = int(user_input)
                        if guess == secret_code:
                            print("CORRECT. The hydraulic seals hiss and the door slides open.")
                            door_locked = False
                        else:
                            print("ERROR: Invalid Code. The internal alarm chirps.")
                    except ValueError:
                        print(f"CRITICAL ERROR: '{user_input}' is not a numeric value. Use the keypad.")


                #boss fight
                print("\nYou enter this large glass dome and this huge spider slams into you...")
                spider_hp = 1000
                player_dodging = False

                while hp > 0 and spider_hp > 0:
                    print(f"\nYour HP: {hp} | Enemy HP: {spider_hp}")
                    choice_boss = input("Choose: attack or dodge? ")

                    #if attack
                    if choice_boss.lower().strip() == "a" or choice_boss.lower().strip() == "attack":
                        # 20% Chance for a Critical Hit
                        if random.random() < 0.2:
                            crit_dmg = weapon * 2
                            spider_hp -= crit_dmg
                            print(f"CRITICAL HIT! You dealt {crit_dmg} damage!")
                        else:
                            spider_hp -=weapon
                            print(f"You hit the spider for {weapon} damage!")

                    elif choice_boss.lower().strip() == "d" or choice_boss.lower().strip() == "dodge":
                        print("You get ready to dodge as you watch the spider")
                        player_dodging = True
                    else:
                        print("Invalid choice, you float and do nothing!!!")

                    #Enemy Phase
                    if spider_hp > 0:
                        print("\nThe spider lunges at you!")

                        if player_dodging:
                            if random.random() < 0.6:
                                print("You rolled under the spider's massive leg.")
                            else:
                                hp -=15
                                print(">> You tried to dodge but got nicked! You took 15 damage.")
                        else:
                            if random.random() < 0.7:
                                print(">> The spider misses and stabs the floor instead.")
                            else:
                                hp -= 35
                                print("The spider slashes you for 35 damage!")

                        player_dodging = False
                if hp > 0:
                    print("\nVICTORY! The giant spider falls.")
                    print("The Observatory is quiet once again... for now.")
                    print("You walk around the Large Obervitory to look out and see the destroyed remains of earth and of the first moon.")

                    #final choice of game
                    final_choice = input("Your final choice astro. Do you finish the mission and leave with the USB or will you break the mission. Break or finish?")
                    if final_choice.strip().lower() == "finish" or final_choice.strip().lower() == "f":
                        print("You walk back to your ship....\n\nYou undock but \n\n ")
                        time.sleep(2)
                        print("What home to return too?")
                    elif final_choice.strip().lower() == "break" or final_choice.strip().lower() == "b":
                        print("\n\nYou walk away with th ideas of freedom. \nYou chose to break the mission and you smashed the drive and all information stored on it. \nYou get in you ship and undock. You fly away to distant stars....")
                    else:
                        print("You either made an error or typed characters. \n\nYou choose to stay on the ship, decades pass and you go crazy.....")
                    print(f"You lived with {hp} health and your trusty {cw_weapon}.")

                else:
                    print("\n......GAME OVER.... The fuzzy legs wrap around you as the screen fades to black.")

                break

                #choice observitory
            elif vent_choice.strip().lower() == "observitory" or vent_choice.strip().lower() == "o":
                print("Entering small observitory")
                print("You get swarmed by a single crow? how. You actually suck at fighting....")
                crow_hp = 50
                player_dodging = False

                while hp > 0 and crow_hp > 0:
                    print(f"\nYour HP: {hp} | Enemy HP: {crow_hp}")
                    choice = input("Choose: attack or dodge? ")

                #if attack
                    if choice.lower().strip() == "a" or choice.lower().strip() == "attack":
                        crow_hp -= weapon
                        print(f"You hit the crow for {weapon} damage!")

                #dodge option
                    elif choice.lower().strip() == "d" or choice.lower().strip() == "dodge":
                        player_dodging = True
                    else:
                        print("Invalid choice, you float and do nothing!!!")

                    if crow_hp > 0:
                        print("Crow attacks..")
                        if random.random() < 0.2:
                            print("The Crow spit, but missed you completely.")

                        elif player_dodging and random.random() < 0.5:
                            print("You successfully dodged the Crows acid")

                        else:
                            hp-= 20
                            print("You took 20 damage!")
                    player_dodging = False
                #END BATTLE
                if hp > 0:
                    print("\nYou beat the Crow...")
                else:
                    print("\nYou died. Game Over.")
                    break



                print("\nYou've entered the Control room, looking like a 90's show nasa control room.\n")
                lastc1 = input("Do you wish to grab the USB stick? y/n")
                if lastc1.strip().lower() == "y" or lastc1.strip().lower() == "yes":
                    print("You grab the USB stick...")

                else:
                    print("\nToo Bad, you grab the USB stick regardless")

                print("As you walk around the control room you notice this werid thin tall fuzzy leg in a different doorway that leads to the large Observitory")
                print("\nYou walk towards it. The stations lights go out for a bief second and the hatch is empty now, nothing blocking it. It looks as if it has still been sealed for decades")
                print("")

                door_locked = True
                secret_code = 157
                print("You find a terminal along with a log book it contains binary codes.")
                print("11111111 | 01110110 | 00000001 | 11110000")
                while door_locked:
                    user_input = input("\nEnter the 3-digit override code: ")
                    try:
                        guess = int(user_input)
                        if guess == secret_code:
                            print("CORRECT. The hydraulic seals hiss and the door slides open.")
                            door_locked = False
                        else:
                            print("ERROR: Invalid Code. The internal alarm chirps.")
                    except ValueError:
                        print(f"CRITICAL ERROR: '{user_input}' is not a numeric value. Use the keypad.")
                #entering boss room
                print("You enter this large glass dome and this huge spider slams into you...")

                #combat
                spider_hp = 1000
                player_dodging = False

                while hp > 0 and spider_hp > 0:
                    print(f"\nYour HP: {hp} | Enemy HP: {spider_hp}")
                    choice_boss = input("Choose: attack or dodge? ")

                    #if attack
                    if choice_boss.lower().strip() == "a" or choice_boss.lower().strip() == "attack":
                        #ritical Hit
                        if random.random() < 0.2:
                            crit_dmg = weapon * 2
                            spider_hp -= crit_dmg
                            print(f"CRITICAL HIT! You dealt {crit_dmg} damage!")
                        else:
                            spider_hp -=weapon
                            print(f"You hit the spider for {weapon} damage!")
                    #if dodge
                    elif choice_boss.lower().strip() == "d" or choice_boss.lower().strip() == "dodge":
                        print("You get ready to dodge as you watch the spider")
                        player_dodging = True
                    else:
                        print("Invalid choice, you float and do nothing!!!")

                    #Enemy Phase
                    if spider_hp > 0:
                        print("\nThe spider lunges at you!")

                        if player_dodging:
                            if random.random() < 0.6:
                                print("You rolled under the spider's massive leg.")
                            else:
                                hp -=15
                                print(">> You tried to dodge but got nicked! You took 15 damage.")
                        #boss attack miss
                        else:
                            if random.random() < 0.7:
                                print(">> The spider misses and stabs the floor instead.")
                            else:
                                hp -= 35
                                print("The spider slashes you for 35 damage!")

                        player_dodging = False
                if hp > 0:
                    print("\nVICTORY! The giant spider falls.")
                    print("The Observatory is quiet once again... for now.")
                    print("You walk around the Large Obervitory to look out and see the destroyed remains of earth and of the first moon.")

                    #final choice of game
                    final_choice = input("Your final choice astro. Do you finish the mission and leave with the USB or will you break the mission. Break or finish?")
                    if final_choice.strip().lower() == "finish" or final_choice.strip().lower() == "f":
                        print("You walk back to your ship....\n\nYou undock but \n\n ")
                        time.sleep(2)
                        print("What home to return too?")
                    elif final_choice.strip().lower() == "break" or final_choice.strip().lower() == "b":
                        print("\n\nYou walk away with the ideas of freedom. \nYou chose to break the mission and you smashed the drive and all information stored on it. \nYou get in you ship and undock. You fly away to distant stars....")
                    else:
                        print("You either made an error or typed characters. \n\nYou choose to stay on the ship, decades pass and you go crazy.....")
                    print(f"{user_name} lived with {hp} health and your trusty {cw_weapon}.")

                else:
                    print("\n......GAME OVER.... The fuzzy legs wrap around you as the screen fades to black.")
                #end of choice 1
                break

            else:
                print("invalid try again")

            continue

        break


    #directions - right
    elif str(hallway_choice1.strip().lower()) == "right" or str(hallway_choice1.strip().lower()) == "r":
        print("\nAs you open the heavy door you geiger counter's glass dial shatters. You look in to see this green hue. \nYou fianlly read the rusted doors name. \nEngine Bay. \n\n The reactors core is exposed")
        if random.random() > 0.4:
            hp -=50
            print("You lost heal as the suit failed to withstand the radiation...")
        else:
            print("You suit managed to withsatnd the extreme radiation of the reactor")
        reactor_puzzle = input ("You have to try and answer this question. You wont be punished if you get this incorrect, type its full name or its first letter.\nWhich element on the periodic table with a 1-inch pellet can equal the power output of 1 ton of coal.")
        if reactor_puzzle.strip().lower() == "u" or reactor_puzzle.strip().lower() == "uranium":
            print("Corret")
            weapon = rusted_knife
            print("You aquired a rusted knife")
        else:
            print("Incorrect: You do not get another chance for the item")

        print("You look around and find a hidden hatch that you decide to open and crawl through...\nYou've entered the medical bay..")

        #heal gamble
        heal_gamble = input("You get the chance to heal or lose health or to gain a new weapon. Do you wish to take the chance? (80/20 y/n")
        if heal_gamble.strip().lower() == "y" or heal_gamble.strip().lower() == "yes":
            print("You take the chance")
            if random.random() < 0.8:
                hp += 20

                print("You gained 20 health and recived a better knife")
                weapon = endgame_knife
                cw_weapon = "Endgame Knife"
            else:
                print("You lost the gamble and failed to get the weapon. \nYou lose 20 health")
                hp-=20

        else:
            print("You refused to take a chance.")

        print("As you walk around the control room you notice this werid thin tall fuzzy leg in a different doorway that leads to the large Observitory")
        print("\nYou walk towards it. The stations lights go out for a bief second and the hatch is empty now, nothing blocking it. It looks as if it has still been sealed for decades")
        print("")

        door_locked = True
        secret_code = 157
        print("You find a terminal along with a log book it contains binary codes.")
        print("11111111 | 01110110 | 00000001 | 11110000")
        while door_locked:
            user_input = input("\nEnter the 3-digit override code: ")
            try:
                guess = int(user_input)
                if guess == secret_code:
                    print("CORRECT. The hydraulic seals hiss and the door slides open.")
                    door_locked = False
                else:
                    print("ERROR: Invalid Code. The internal alarm chirps.")
            except ValueError:
                print(f"CRITICAL ERROR: '{user_input}' is not a numeric value. Use the keypad.")
        #entering boss room
            print("You enter this large glass dome and this huge spider slams into you...")

        #combat
        spider_hp = 1000
        player_dodging = False

        while hp > 0 and spider_hp > 0:
            print(f"\nYour HP: {hp} | Enemy HP: {spider_hp}")
            choice_boss = input("Choose: attack or dodge? ")

            #if attack
            if choice_boss.lower().strip() == "a" or choice_boss.lower().strip() == "attack":
                #ritical Hit
                if random.random() < 0.2:
                    crit_dmg = weapon * 2
                    spider_hp -= crit_dmg
                    print(f"CRITICAL HIT! You dealt {crit_dmg} damage!")
                else:
                    spider_hp -=weapon
                    print(f"You hit the spider for {weapon} damage!")
            #if dodge
            elif choice_boss.lower().strip() == "d" or choice_boss.lower().strip() == "dodge":
                print("You get ready to dodge as you watch the spider")
                player_dodging = True
            else:
                print("Invalid choice, you float and do nothing!!!")

            #Enemy Phase
            if spider_hp > 0:
                print("\nThe spider lunges at you!")

                if player_dodging:
                    if random.random() < 0.6:
                        print("You rolled under the spider's massive leg.")
                    else:
                        hp -=15
                        print(">> You tried to dodge but got nicked! You took 15 damage.")
                #boss attack miss
                else:
                    if random.random() < 0.5:
                        print(">> The spider misses and stabs the floor instead.")
                    else:
                        hp -= 35
                        print("The spider slashes you for 35 damage!")

                player_dodging = False
        if hp > 0:
            print("\nVICTORY! The giant spider falls.")
            print("The Observatory is quiet once again... for now.")
            print("You walk around the Large Obervitory to look out and see the destroyed remains of earth and of the first moon.")
            #final choice of game
            final_choice = input("Your final choice astro. Do you finish the mission and leave with the USB or will you break the mission. Break or finish?")
            if final_choice.strip().lower() == "finish" or final_choice.strip().lower() == "f":
                print("You walk back to your ship....\n\nYou undock but \n\n ")
                time.sleep(2)
                print("What home to return too?")
            elif final_choice.strip().lower() == "break" or final_choice.strip().lower() == "b":
                print("\n\nYou walk away with th ideas of freedom. \nYou chose to break the mission and you smashed the drive and all information stored on it. \nYou get in you ship and undock. You fly away to distant stars....")
            else:
                print("You either made an error or typed characters. \n\nYou choose to stay on the ship, decades pass and you go crazy.....")
                print(f"You lived with {hp} health and your trusty {cw_weapon}.")

        else:
            print("\n......GAME OVER.... The fuzzy legs wrap around you as the screen fades to black.")


        break


    #directions - straight
    elif str(hallway_choice1.strip().lower()) == "straight" or str(hallway_choice1.strip().lower()) == "s" or str(hallway_choice1.strip().lower()) == "forward" or str(hallway_choice1.strip().lower()) == "f":
        print("\nYou went forward you walk into the small run down observatory, you look out the glass to see earths new second moon, its dark red like a blood moon.")
        print("You hear this strange sound?.... You get swarmed by a single crow?")
        crow_hp = 50
        player_dodging = False

        while hp > 0 and crow_hp > 0:
            print(f"\nYour HP: {hp} | Enemy HP: {crow_hp}")
            choice = input("Choose: attack or dodge? ")
            #if attack
            if choice.lower().strip() == "a" or choice.lower().strip() == "attack":
                crow_hp -= weapon
                print(f"You hit the crow for {weapon} damage!")
            #if dodge
            elif choice.lower().strip() == "d" or choice.lower().strip() == "dodge":
                player_dodging = True
            #you suck
            else:
                print("Invalid choice, you float and do nothing!!!")
            #enemy phase
            if crow_hp > 0:
                print("Crow attacks..")
                if random.random() < 0.2:
                    print("The Crow spit, but missed you completely.")

                elif player_dodging and random.random() < 0.65:
                    print("You successfully dodged the Crows acid")

                else:
                    hp-= 20
                    print("You took 20 damage!")
            player_dodging = False
        if hp > 0:
            print("\nYou beat the Crow...")

        else:
            print("\nYou died. Game Over.")
            break

        print("The crow lives?, it seems to be asking something?")
        friend = input("Maybe it wants to befriend you? Your could share 20 hp to heal it or let it die....    y/n")
        if friend.strip().lower() == "y" or friend.strip().lower() == "yes":
            hp-=10
            friend = True
            print("You got a friend")

        elif friend.strip().lower() == "n" or friend.strip().lower() == "no":
            friend = False
            print("You left him to die, you coward...")

        else:
            hp -=20
            print("You either type something wrong or put gibberish. \n\n You lost 25 hp as you failed to save the crow...")
        print("\n\nYou continue to stare at the moon after the crow was delt with")
        print("You walk into the room that says ###CONTROL ROOM### \nYou see this long lanky fuzzy leg in the distant doorway that reads Large Obervitory...")
        print("You take a second to take in how the Control Room looks, a 90s Nasa style of hardware")

        lastc1 = input("Do you wish to grab the USB stick? y/n")
        if lastc1.strip().lower() == "y" or lastc1.strip().lower() == "yes":
            print("You grab the USB stick...")

        else:
            print("\nToo Bad, you grab the USB stick regardless")
        print("\nYou look back towards the door and the fuzzy looking stick is gone\n\nSuddenly the lights flicker and the large door slams shut at what seems like light speed to you...")
        print("You look around in hope of finding how to open it but you find a terminal that requires a 3 didget code...")
        print("")
        door_locked = True
        secret_code = 157
        print("Along with a log book it contains binary codes.")
        print("11111111 | 01110110 | 00000001 | 11110000")
        while door_locked:
            user_input = input("\nEnter the 3-digit override code: ")
            try:
                guess = int(user_input)
                if guess == secret_code:
                    print("CORRECT. The hydraulic seals hiss and the door slides open.")
                    door_locked = False
                else:
                    print("ERROR: Invalid Code. The internal alarm chirps.")
            except ValueError:
                print(f"CRITICAL ERROR: '{user_input}' is not a numeric value. Use the keypad.")
                #entering boss room
        print("You enter this large glass dome and this huge spider grabs you with a single limb and throws you...")
        spider_hp = 1000
        player_dodging = False

        while hp > 0 and spider_hp > 0:
            print(f"\nYour HP: {hp} | Enemy HP: {spider_hp}")
            choice_boss = input("Choose: attack or dodge? ")
            #attack choice
            if choice_boss.strip().lower() == "a" or choice_boss.strip().lower() == "attack":
                #chance of crit 20%
                if random.random() <0.2:
                    crit_dmg = weapon * 2
                    spider_hp -= crit_dmg
                    print("CRITICAL HIT! You dely {crit_dmg} damage!2")
                else:
                    spider_hp -=weapon
                    print(f"You hit the spider for {weapon} damage!")

            elif choice_boss.strip().lower()== "d" or choice_boss.strip().lower() == "dodge":
                print("You get ready to dodge as you watch the spider")
                player_dodging = True
            else:
                print("invalid choice, you float and do nothing!!!")

            #friend phase
            if friend == True and spider_hp > 0:
                if random.random() < 0.8:
                    spider_hp -= friend_dmg
                    print(f"The crow pecks the spider's eyes for {friend_dmg} damage!")
                else:
                    print("The crow circles overhead, looking for an opening.")

            #Enemy phase
            if spider_hp > 0:
                print("\nThe spider lunges at you!")

                if player_dodging:
                    if random.random() < 0.6:
                        print("You rolled under the spiders massive leg.")

                    else:
                        hp -=15
                        print(">> You tried to dodge but you got nicked!")
                else:
                    if random.random() <0.67:
                        print(">> The spider misses and stabs the floor instead.")
                    else:
                        hp -= 30
                        print("The spider slashes you for 30 damage!")

                player_dodging = False
        if hp > 0:
            print("\nVICTORY! The giant spider falls.")
            print("The Observatory is quiet once again... for now.")
            print("You walk around the Large Obervitory to look out and see the destroyed remains of earth and of the first moon.")

            friend_end = input("You walk back to your shuttle. \nYour stuck with a choice... Do you take your friend with you? y/n")
            if friend_end.strip().lower() == "y" or friend_end.strip().lower() == "yes":
                print("You escape with your new crow friend?\nI dont really know the idea.")
            elif friend_end.strip().lower() == "n" or friend_end.strip().lower() == "no":
                print("You left behind the strange radiactive crow as you return to your shuttle?....")
            print(f"{user_name} lived with {hp} health and your trusty {cw_weapon}.")

            break

        else:
            print("\n......GAME OVER.... The fuzzy legs wrap around you as the screen fades to black.")
            #end of choice 1
            break


    else:
        print("\nInvalid input try again")
