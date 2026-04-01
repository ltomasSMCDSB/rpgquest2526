
#Game Name - dungeon stuff and what not

import time
import random
import sys
#variables

socrates_rat = 0
left_room1 = 0
right_room1 = 0
hermes_boots = 0
max_life = 100
current_life = 100
old_man = 0
young_boy = 0
item_money = 0
stage_2 = 0
patrick_star = 0
shop_prices = 0
item_guitar = 0
item_cosmic_worm = 0
item_fungus = 0
item_dagger = 0
item_garlic_bread = 0
item_life_crystal = 0
price_guitar = 0
price_garlic_bread = 0
price_cosmic_worm = 0
price_dagger = 0
price_life_crystal = 0
price_fungus = 0
old_man_answer = 0
boss_hp = 150
dagger_dmg = 12
fist_dmg = 6
item_fist = 1
boss_charm = 0

#start/entering the dungeon
user = input("input your name: ")
print (f"welcome {user}, to the dungeon.")

while True:
    enter_dungeon = input("would you like to enter? (Y/N) ")
    if enter_dungeon.upper() == "Y" or enter_dungeon.upper() == "YES":
        print (f"Good luck, {user}")
        enter_dungeon == True
        break
    elif enter_dungeon.upper() == "N" or enter_dungeon.upper() == "NO":
        are_you_sure = input("are you sure? theres lots of gold...: (Enter/N)")
        if are_you_sure.upper() == "ENTER" or are_you_sure.upper()=="Y":
            print("thats what i thought.")
            enter_dungeon == True
            break
        elif are_you_sure.upper() == "NO" or are_you_sure.upper() == "N":
            print ("oh nooo a bunch of big bad wolves force you into the dungeon!")
            enter_dungeon == True
            break
    else:
         try_again = input("your input was invalid. Use the inputs provided (Y/N) to make your choice. Press [ENTER] to try again.")

time.sleep(1)



while True:
    decide_path = input ("which way would you like to go? (left, right or straight): ")

    if decide_path.upper().strip() == "STRAIGHT":
        print ("two paths are in front of you.")
        time.sleep(0.5)
        print ("one path is accompanied by a little boy\nthe other with an old man.")
        time.sleep(1)
        print ("you must choose which path to follow.")
        time.sleep(0.5)
        print ("*LITTLE BOY* - Come with me! That old fart is creepy and he'll only slow you down!")
        time.sleep(0.5)
        print ("*OLD MAN* - Dont listen to that little crap! He only causes trouble and mischief, come with me instead!")
        time.sleep(0.7)
        follow_person = input ("*NOTE* YOU CANNOT GO BACK AFTER CHOOSING!!!\nWho would you like to follow? (man/boy/back)")
        if follow_person.lower().strip() == "man":
            print("*OLD MAN ALFRED HAS JOINED YOUR PARTY!*")
            old_man = 1
            stage_2 = 1
            break
        if follow_person.lower().strip() == "boy":
            print ("*LITTLE JIMBO HAS JOINED YOUR PARTY!*")
            young_boy = 1
            stage_2 = 1
            break
        if follow_person.lower().strip() == "back":
            print ("*You went back to the main hall...*")
            continue
        else:
            print("your input was invalid, press [ENTER] to try again.")
            continue

    if decide_path.upper().strip() == "RIGHT" and right_room1 == 1:
        print ("You already went this way!")
        continue

    if decide_path.upper().strip() == "RIGHT" and right_room1 == 0:

        print ("you are presented with a key and two chests.")
        time.sleep(1)
        print("there is a pedestal in front of you holding one key.")
        time.sleep(1)
        print("A sign reads \"This key can open both chests, but dissapears after use. Choose wisely...\"")
        time.sleep(1)

        chest_choice = input ("There is a big gold chest and a small wooden chest. Which do you choose?\n(gold/wood)\n:")

        if chest_choice.lower().strip() == "gold":

            print ("You insert the key into the golden chest.")
            time.sleep(1)
            print ("It shatters in your hand as you turn it, unlocking the chest.")
            time.sleep(1.3)
            print ("The chest pops open. You look inside and see...")
            time.sleep(2)
            print ("*HERMES BOOTS!*")
            time.sleep(0.7)
            hermes_boots = 1
            right_room1 = 1
            if socrates_rat == 1:
                print("SOCRATES: Those are Hermes Boots!")
                time.sleep(0.5)
                print("SOCRATES: Im sure you feel a whole lot faster with them on.")

        elif chest_choice.lower().strip() == "wood":

            print ("You insert the key into the wooden chest.")
            time.sleep(1)
            print ("It shatters in your hand as you turn it, unlocking the chest.")
            time.sleep(1.3)
            print ("The chest pops open. You look inside and see...")
            time.sleep(2)
            print ("*LIFE CRYSTAL*")
            time.sleep(0.7)
            print ("The second you touch the crystal, it shatters and absorbs into your body.")
            time.sleep(1.5)
            max_life = 120
            current_life = 120
            right_room = 1
            if socrates_rat == 1:
                print ("SOCRATES: Hey im pretty sure that was a life crystal!")
                time.sleep(0.8)
                print ("SOCRATES: It increases your maximum HP by 20, so right now you should have 120 HP!")
                continue
        else:
            try_again = input("your input was invalid. Press [ENTER] to try again.")
            continue

    if decide_path.upper().strip() == "LEFT" and left_room1 == 1:
        print ("You already went this way!")
        continue

    if decide_path.upper().strip() == "LEFT" and left_room1 == 0:

        print ("you encounter a rat!")
        time.sleep(0.5)
        print (f"\"I am the all knowing Soc-rat-es! And I have a task for you {user}.")
        time.sleep(1)
        reply_rat1 = input ("reply with the number associated with the prompt: \n1:\"What is the task?\" \nor \n2:\"How did you know my name!?\"\n:")
        if reply_rat1.strip() == "1":
            time.sleep(0.7)
            print ("You must solve one of my legendary riddles!! \njust know that my intelligence is far superior to yours, so don't beat yourself up when you get it wrong")
            time.sleep(2)
            riddle_answer1 = input ("here it is *smirks*\n\nWhat gets smaller every time it takes a bath?\n:")
            if riddle_answer1.lower().strip() == "soap":
                print ("WHAT!? HOW DID YOU GET IT RIGHT!??!?!?!!??")
                time.sleep(1.2)
                print("\nThis... This can't be!")
                time.sleep(1.3)
                print("\nNO! You got lucky! I'll be back DONT YOU WORRY BUDDY!")
                time.sleep(1)
                item_money += 10
                print("\n*You got 5 dollars!*")
                left_room1 = 1
            else:
                print("WRONG!! HAHAHA! You make me wonder how you even GOT INTO THE DUNGEON!!! ")
                time.sleep(1.5)
                print("\nMan you are GREAT! I might just tag along with you for the laughs!")
                time.sleep(1.5)
                print("\n*Socrates the rat has joined your party!*")
                socrates_rat = 1
                left_room1 = 1


        if reply_rat1 == "2":
            print ("heh, dont worry about that right now, all you need to worry about is solving one of my legendary riddles! \nBeware dungeon person, for my riddles are among the HARDEST!")
            time.sleep(1)
            riddle_answer1 = input ("here it is *smirks*\n\nWhat gets smaller every time it takes a bath?\n:")
            if riddle_answer1.lower().strip() == "soap":
                print ("WHAT!? HOW DID YOU GET IT RIGHT!??!?!?!!??")
                time.sleep(1.2)
                print("\nThis... This can't be!")
                time.sleep(1.3)
                print("\nNO! You got lucky! I'll be back DONT YOU WORRY BUDDY!")
                time.sleep(1)
                item_money += 10
                print("\n*You got 5 dollars!*")
                left_room1 = 1
            else:
                print("WRONG!! HAHAHA! You make me wonder how you even GOT INTO THE DUNGEON!!! ")
                time.sleep(1.5)
                print("\nMan you are GREAT! I might just tag along with you for the laughs!")
                time.sleep(1.5)
                print("\n*Socrates the rat has joined your party!*")
                socrates_rat = 1
                left_room1 = 1
            continue



while True:
    time.sleep(1.3)
    print ("There are two bridges ahead...")
    time.sleep(0.5)
    bridge_choice = input ("there is an old raggedy wooden bridge on one side,\nand some stone platforms to hop on the other.\nwhat will you choose?\n(wood/stone/help)")

    if bridge_choice.lower().strip() == "wood":
        print ("!YOU FELL! sustained some injuries but managed to climb back up. *-30HP*")
        current_life -=30
        break

    if bridge_choice.lower().strip() == "stone":
        print ("You hop across safely!")
        break

    if bridge_choice.lower().strip() == "help" and socrates_rat == 1:
        print ("*SOCRATES* Hmmm, I gotta say the stone platforms look safer man, as long as you can take it slow.")
        continue

    if bridge_choice.lower().strip() == "help" and old_man == 1:
        print ("*ALFRED* The stone platforms look more stable to me.")
        continue

    if bridge_choice.lower().strip() == "help" and young_boy == 1:
        print ("*JIMBO* You should TOTALLLYYY go on the wooden bridge, trust me bro.")

    else:
        try_again = input ("your input was invalid. press [ENTER] to continue.")
        continue

while True:
    time.sleep(1)
    print ("As you walk down the path, you see a hallway on your right")
    time.sleep(0.7)
    print ("its a hallway of lava with some stepping stones to get across")
    time.sleep(1)
    lava_path = input ("there is a golden door at the end, would you like to take the risk? (Y/N)")
    if lava_path.lower().strip() == "y" or lava_path.lower().strip() == "yes":
        if random.random()<0.3:
            print ("YOU FELL IN! -50HP")
            current_life -=50
            if current_life <= 0:
                print ("YOU DIED")
                sys.exit()
            elif current_life >= 1:
                try_again2 = input ("would you like to try again or move on? (try/no)")
                if try_again2.lower().strip() == "try":
                    print("you decide to give it another go")
                continue
            if try_again2.lower().strip() == "n" or try_again2.lower().strip() == "no":
                print ("you give up and leave the golden door as a mystery.")
                break
            break
        else:
            print ("you made it across safely.")
            time.sleep(0.5)
            print ("you open the door and see...")
            time.sleep(2)
            print ("""
⣿⣿⣟⣯⣿⣟⣯⣿⣿⣻⣿⣟⣿⣿⣻⣿⣽⣿⣻⣿⣟⣿⣿⣻⣿⡿⣿⣟⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⣿⡷⣿⣻
⣿⣿⢿⣿⣻⣿⢿⣻⣽⣿⣟⣿⣿⣻⣿⢿⣻⣿⡿⣟⣿⣿⣻⣿⡿⣿⣿⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⡿⣯⢷⣿⣻⣽
⣿⣿⡿⣟⣿⡿⣿⣿⢿⣯⣿⣿⣽⣿⢿⣿⣿⣻⣿⡿⣟⣿⣿⣻⣿⢿⣻⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣼⡻⣽⣻⣞⣷⣻
⣿⣷⣿⡿⣟⣿⣿⣽⣿⡿⠽⠾⠿⠿⠿⣯⣿⣟⣷⣿⣿⢿⣽⣿⣻⣿⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⣳⣿⢿⣟⣿⣻⣿
⣿⡿⣾⣿⢿⣿⡾⠋⣡⡶⠟⣛⠛⡛⠶⣦⣌⠻⣿⣽⣾⣿⢿⣽⡿⣷⣿⡟⣣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣳⣿⣻⣿⣻⣟⣿⣽
⣿⣟⣿⣽⡿⣷⠁⣿⠏⢰⣿⣿⣿⣿⣿⣄⢻⣧⢹⣿⣽⣾⠟⢛⣉⣭⣕⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣳⣿⢿⣽⣿⣻⣯⢿
⣿⣟⣯⣿⢿⣿⡄⠻⣦⣘⠻⠿⣾⣿⣽⣿⢀⡿⢸⣿⠟⣡⣾⠟⣋⣋⣉⣭⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣟⡧⣟⢿⣛⢾⡳⣏⢿
⣿⣿⣟⣿⣿⣉⣛⡳⣮⣭⣯⣗⣶⣬⣻⣧⠸⣥⣭⡥⠞⣫⣴⣿⣿⣿⣿⣿⡻⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣹⣮⣷⣹⣎⣷⣹⣾
⣿⣿⣿⣭⣭⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣖⣲⡾⣻⣟⣻⣿⣷⣿⣷⠿⣿⣎⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣻⣽⣾⣿⣻⣟⣿⣽
⣿⡄⠛⠿⠿⢿⣿⣟⣛⣛⣋⠿⣿⣯⠹⣿⡿⠿⢣⣾⣿⣿⣿⣿⣻⣟⣒⠿⢿⣿⣷⣭⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⣿⢿⣾⡿⣿⣽⣷⣿⢿⣻⣿
⣎⣛⣛⣛⣛⣋⣭⣿⡿⠿⣛⣷⢹⣿⣷⠖⣲⣾⣟⠻⣿⣿⡿⣿⣿⣿⣍⠛⣦⡉⣿⣿⣿⣿⣷⣦⣍⠻⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⢿⣯⣿⣿⣻⣿⣻⣿⣟⣯⣿⣾⣿⢿⣻
⣿⣿⣿⡿⣿⡟⣡⡶⢟⣋⣭⣶⣿⡿⡇⢾⠹⣿⡌⣷⣌⠻⢿⣟⣷⣿⠟⣠⣿⠁⣽⣿⣾⢿⣽⣿⠟⢃⣿⣿⣿⡟⢀⣾⣿⡿⣟⣯⣷⣿⣿⣻⣽⣟⣿⣽⣿⣳⣿⣟⣯⣷⣿⡿⣿
⣿⣟⣾⡿⣿⠰⣿⠀⢿⣿⣟⣿⣽⣿⣇⢸⡆⣿⣿⣌⡛⠷⣶⣤⣤⡶⠾⢛⣡⣶⣿⣿⣾⡿⠯⠘⠁⣭⠉⣉⠙⠳⠦⢹⣿⢿⣿⣻⣿⢾⣟⣿⣽⡿⣯⣿⣾⣟⣿⣾⢿⣻⣾⢿⣿
⣿⣿⣽⢿⡿⣧⡙⢷⣬⣙⣛⢋⡛⣚⣋⡼⠃⣾⣿⣻⣿⣿⣶⣶⣶⣶⡾⣿⢿⣻⣽⡾⠗⠊⣠⡾⠵⢿⣤⣿⣉⣆⠀⠈⠻⣿⣯⣿⣻⣟⣯⢿⣯⢿⣯⢷⣯⢿⣽⡾⣟⡿⣿⣻⢿
⣿⢻⣞⣯⠿⣽⢿⣦⣍⣉⡙⡛⢛⣋⣩⣴⡿⣯⢷⣻⣞⣳⡟⣾⡽⣞⣿⡽⠋⢁⣤⣶⡶⢀⣥⣶⣷⣦⡈⢹⣿⣿⣄⠀⠀⢜⡳⢯⣷⣻⣞⣧⣟⡿⣞⡿⣞⡿⣾⡽⣯⣟⣷⣻⢿
⣯⣟⡾⣽⠯⢟⣟⡾⣽⣏⣿⣻⢯⣟⣳⢯⡷⣯⣟⡷⣞⡷⣿⣳⢿⣟⡮⠁⣠⣿⡉⠈⢠⣿⣿⠛⠙⠿⠃⡰⣽⣿⣿⣦⠁⠈⢧⠙⢾⣵⣻⡼⣯⢿⣽⣻⣽⣻⢷⣻⢷⣻⢾⡽⣿
⣷⢯⠟⠉⢀⠜⢯⣽⣳⢾⣳⢯⣟⡾⣽⢯⣻⢷⡯⣿⣽⣻⢷⣯⣟⡾⣽⡀⠹⣿⣿⠇⢿⣿⣿⣷⣾⠋⣰⣽⣿⣿⣿⣿⣷⣄⠈⠑⢢⡱⣷⣻⢽⡯⠞⢓⣋⠟⣭⢋⡟⣭⣻⢿⣽
⠁⠀⠀⠐⠀⢠⠰⠟⠾⠋⠉⡿⠾⣽⢯⣟⡽⣯⢷⣻⢾⡍⠉⠀⠀⠈⠋⠃⢠⢶⣶⣶⣌⣙⣛⣫⣴⣿⣿⣿⠻⠿⣿⣿⣿⣿⣦⡁⢀⠙⢲⢭⡻⣄⠈⠃⢎⠞⣤⠋⠄⢀⡿⣯⣿
⠀⠀⠀⠀⠀⠂⠀⢀⠀⠀⠈⠀⠀⢸⣻⢾⣹⢯⣷⣻⢯⣇⠀⠉⠇⠀⣶⣶⣶⣦⣤⣤⣬⣉⣉⣉⣙⣉⣩⣉⣤⣦⣼⣿⣿⣿⣿⣿⣌⠀⠆⢣⡝⡲⣌⡑⣈⣈⢀⣠⡴⣾⣽⡳⣿
⠀⠀⠀⠀⠀⠀⠌⠀⡐⠠⠀⠀⣨⡿⣽⡳⣯⣟⡾⣽⢯⡟⢶⠀⠀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⡄⠘⢵⢪⡕⣣⠞⣭⢳⡹⢣⣗⢻⡽
⠀⠀⠄⠀⢀⠤⠀⠀⢠⠁⠀⣾⡻⣽⣳⣟⡷⣯⢿⡝⣫⠔⠃⢀⣼⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢂⠈⠳⡜⣥⡛⢦⠳⣍⡳⣬⣳⣽
⣆⠀⠀⠐⡌⢎⠀⠀⢂⠀⢆⡚⢽⢳⡛⢾⠹⡳⢫⠞⠁⢀⣴⣿⣿⣿⣿⣷⣮⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠻⣿⣿⣿⣿⣄⢈⠀⠛⡴⣩⢋⠷⣡⢛⠶⡹⢎
⣟⠆⠀⡐⠀⢂⠀⠀⠂⢀⡳⢌⢧⠲⣉⢎⡳⡉⠒⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡘⢿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣦⠀⠀⠑⠥⠋⠮⠑⠎⠎⠵⠩
⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠈⣁⠉⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠒⠐⠒⢂⠒⡐⠐⠂⠒
⣤⢤⠤⠶⠴⠒⢒⡒⢒⡒⣉⠉⠠⠤⠐⠂⠀⣾⣿⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠈⠉⠉⠉⠉
⠠⣤⠦⠒⠖⠊⠁⠉⠀⠀⠀⠠⠠⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣷⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠄⠠⠄⠀⠀⠀⠀
⠀⠀⠀⣠⣤⣤⠤⠶⠒⠚⠛⠉⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⣴⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠇⠀⠀⢂⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠘⢿⣿⣿⣿⣿⣿⣿⡇⠀⡄⢰⣶⣶⣿⣿⣿
⣉⣉⣉⣉⣉⣀⡀⠀⠀⠀⠀⠀⠂⢀⡄⠸⡏⠀⠠⠉⡁⠒⠀⠉⠭⠉⣉⣛⠙⠛⠛⠛⠿⠟⠿⠟⠛⠛⠛⠛⠛⡛⣙⣉⡉⠉⠁⠀⣀⡈⠹⣿⣿⣿⠟⠛⡇⠀⠑⠻⠿⣿⣿⣷⣤
⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠱⣄⣁⣃⣤⠁⢚⡐⢆⡒⠤⠠⠄⡌⢡⠉⡄⢠⢠⣤⣭⣤⣵⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣄⠙⠻⣿⣷⠶⠃⠀⢸⡑⡲⠤⢀⠉⠉
""")
            time.sleep(1)
            print ("you hop back to the hallway and continue.")
            patrick_star += 1
            break
    if lava_path.lower().strip() == "n" or lava_path.lower().strip() == "no":
            print ("you decide that it isnt worth the risk and move on...")
    break


time.sleep(1)
print("as you continue, you come across a telephone line.")
time.sleep(1)
print("it seems to be some kind of puzzle.")
time.sleep(1)
print("a page is presented to you with a telephone, it reads...")
time.sleep(0.8)
print("\"you took the risk, and found the treasure. Now call the one you found.\"")
time.sleep(1.5)
while True:
    fountain_answer = input ("do you know the answer?\n\n1: Type the answer\n\n2: Type \"H\" for help\n\n3: Type \"give up\" to give up.\n\n:")
    if fountain_answer.lower().strip() == "7287425" or fountain_answer.lower().strip() == "72874257827":
        print("the phone rings...")
        time.sleep(1)
        print("*Someone picks up*")
        time.sleep(1)
        print("\"enrique\"")
        time.sleep(1)
        print("*the phone hangs up and gold coins start coming out of it!")
        time.sleep(1)
        print("you got $20!")
        item_money += 20
        time.sleep(1)
        break
    if fountain_answer.lower().strip() == "h" and patrick_star == 0 or fountain_answer.lower().strip() == "help" and patrick_star == 0:
        print("nobody could help as there were no hints...")
        continue
    if fountain_answer.lower().strip() == "h" and old_man == 1 and patrick_star == 1 or fountain_answer.lower().strip() == "help" and old_man == 1 and patrick_star == 1:
        print("*ALFRED* Took the risk? Hmm, well the only risks you took were the bridges and lava pit right?")
        time.sleep(2)
        print("*ALFRED* it must be something to do with what you saw on the other side of that door.")
        time.sleep(1)
        continue
    if fountain_answer.lower().strip() == "h" and socrates_rat == 1 and patrick_star == 1 or fountain_answer.lower().strip() == "help" and socrates_rat == 1 and patrick_star == 1:
        print("*SOCRATES* Hmmmmm well think of all the risks you took, maybe theres a hint within one of them?")
        time.sleep(1)
        continue
    if fountain_answer.lower().strip() == "h" and young_boy == 1 and patrick_star == 1 or fountain_answer.lower().strip() == "help" and young_boy == 1 and patrick_star == 1:
        print("*JIMBO* Dont ask me my broman empire idk lol")
        time.sleep(1)
        continue
    if fountain_answer.lower().strip() == "giveup":
        print("you gave up and left...")
        time.sleep(2)
        break

if socrates_rat == 0 and left_room1 == 1:
    print("*SOCRATES* We meet again human!!")
    time.sleep(1)
    print("\n*SOCRATES* I have spent a considerable amount of time thinking, and I finally HAVE IT!")
    question_to_socrates = input("\n(input 1 or 2)\n\n1: have what?\n\n2: let me guess, another riddle?")
    if question_to_socrates.lower().strip() == "1":
        print("\n*SOCRATES* heh, ITS A NEW RIDDLE!!!")
        time.sleep(1)
        print("\n*SOCRATES* are you ready human? this wont be as easy...")
        time.sleep(1)
        while True:
            print("\nI have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
            riddle_answer2 = input("\nask for help by typing \"H\"\nOr answer the question:")

            if riddle_answer2.lower().strip() == "map" or riddle_answer2.lower().strip() == "amap":
                print("\n*SOCRATES* HUUUUHHHHHHH?!??!?!?!?!?!?!!!!?")
                time.sleep(0.8)
                print("\n*SOCRATES* you really got it right again huh?")
                time.sleep(1.3)
                print("\n*SOCRATES* im not gonna get mad this time, but you'll have another thing comin buddy")
                time.sleep(1.7)
                print("\n*Socrates scurries off further into the dungeon...*")
                shop_prices += 1
                time.sleep(3)
                break

            if riddle_answer2.lower().strip() == "h" and old_man == 1 or riddle_answer2.lower().strip() == "help" and old_man == 1:
                print ("\n*ALFRED* Ah I think I have heard this one before, it should be a map! right?")
                time.sleep(2)
                print("\n*SOCRATES* Wha... bu...")
                time.sleep(2)
                print ("\n*SOCRATES* HEY THAT ISNT FAIR!!")
                time.sleep(0.5)
                print("\n*SOCRATES* YOU KNOW HOW HARD I WORKED TO COME UP WITH THAT!?!?")
                time.sleep(0.8)
                print("\n*SOCRATES* NOW ITS ALL RUINED CAUSE THIS OLD GEEZER KNEW THE ANSWER!!")
                time.sleep(0.8)
                print("\n*SOCRATES* THATS IT!! IM GOING BACK HOME!")
                time.sleep(3)
                print("\n*ALFRED* Wow, what a sore loser.")
                time.sleep(2)
                old_man_answer = 1
                #gives different dialouge if the old man answered and not the person.
                break

            if riddle_answer2.lower().strip() == "h" and young_boy == 1 or riddle_answer2.lower().strip() == "help" and young_boy == 1:
                print("\n*JIMBO* Uhhh yeah im not too good at these things, you're on your own man")
                time.sleep(2)
                continue
            else:
                print("\n*SOCRATES* HAHA! YES! I FOOLED YOU!!")
                time.sleep(1)
                print("\n*SOCRATES* I KNEW YOU WERE TOO INCOMPITENT TO UNDERSTAND MY RIDDLES!")
                time.sleep(1.5)
                print("\n*Socrates dances further into the dungeon, singing his victory song...")
                time.sleep(3)
                break


#if the user has not met socrates make it a new encounter

if socrates_rat == 0 and left_room1 == 0:
    print("*RAT* You there!")
    time.sleep(1)
    print("\n*RAT* I have spent a considerable amount of time thinking, and I finally HAVE IT!")
    question_to_socrates = input("\n(input 1 or 2)\n\n1: have what? \n\n2: who are you?")
    if question_to_socrates.lower().strip() == "1" or question_to_socrates.lower().strip() == "2":
        print("\n*SOCRATES* Well, my name is Socrates the rat, and I have a riddle for you!")
        time.sleep(1)
        print("\n*SOCRATES* are you ready human? this wont be as easy...")
        time.sleep(1)
        while True:
            print("\nI have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
            riddle_answer2 = input("\nask for help by typing \"H\"\nOr answer the question:")

            if riddle_answer2.lower().strip() == "map" or riddle_answer2.lower().strip() == "amap":
                print("\n*SOCRATES* HUUUUHHHHHHH?!??!?!?!?!?!?!!!!?")
                time.sleep(0.8)
                print("\n*SOCRATES* you really got it right huh?")
                time.sleep(1.3)
                print("\n*SOCRATES* im not gonna get mad, but you'll have another thing comin buddy")
                time.sleep(1.7)
                print("\n*Socrates scurries off further into the dungeon...*")
                shop_prices += 1
                time.sleep(3)
                break

            if riddle_answer2.lower().strip() == "h" and old_man == 1 or riddle_answer2.lower().strip() == "help" and old_man == 1:
                print ("\n*ALFRED* Ah I think I have heard this one before, it should be a map! right?")
                time.sleep(2)
                print("\n*SOCRATES* Wha... bu...")
                time.sleep(2)
                print ("\n*SOCRATES* HEY THAT ISNT FAIR!!")
                time.sleep(0.5)
                print("\n*SOCRATES* YOU KNOW HOW HARD I WORKED TO COME UP WITH THAT!?!?")
                time.sleep(0.8)
                print("\n*SOCRATES* NOW ITS ALL RUINED CAUSE THIS OLD GEEZER KNEW THE ANSWER!!")
                time.sleep(0.8)
                print("\n*SOCRATES* THATS IT!! IM GOING BACK HOME!")
                time.sleep(3)
                print("\n*ALFRED* Wow, what a sore loser.")
                time.sleep(2)
                old_man_answer = 1
                #gives different dialouge if the old man answered and not the person.
                break

            if riddle_answer2.lower().strip() == "h" and young_boy == 1 or riddle_answer2.lower().strip() == "help" and young_boy == 1:
                print("\n*JIMBO* Uhhh yeah im not too good at these things, you're on your own man")
                time.sleep(2)
                continue
            else:
                print("\n*SOCRATES* HAHA! YES! I FOOLED YOU!!")
                time.sleep(1)
                print("\n*SOCRATES* I KNEW YOU WERE TOO INCOMPITENT TO UNDERSTAND MY RIDDLES!")
                time.sleep(1.5)
                print("\n*Socrates dances further into the dungeon, singing his victory song...")
                time.sleep(3)
                break


print("*As you venture further, you come across a shop...*")
time.sleep(2)
#if you won both times against socrates, increased prices. (below this text)
if shop_prices == 1:
    item_guitar += 15
    item_garlic_bread += 10
    item_cosmic_worm += 5
    item_dagger += 7
    item_life_crystal += 15
    item_fungus += 0
    print(f"*SOCRATES* heh, WELCOME {user.upper()}, TO MY HUMBLE ABODE!")
    time.sleep(1.5)
    print("*SOCRATES* Feel free to browse around and buy what you want, I hold no grudges to customers :)")
    time.sleep(2)
    print("*You check the prices, they are obviously jacked up...")
    time.sleep(1.5)
    print(f"""[*THE CHEDDAR MINE*]

Intstructions: Items will show with their name and description beside them.
Example: Price - Item - description - stock.
Happy shopping {user}!

You have ${item_money} to spend :)

$15 - Guitar - Maybe those lessons could come in handy! - 1

$10- Garlic Bread - Heals 50HP, i mean who DOESN'T love garlic bread. - 3

$5 - Cosmic Worm - Just looking at it gives you chills, probably best to leave it alone... - 1

$7 - Dagger - Deals 12 DMG instead of 6 DMG(fists), a simple dagger. - 1

$0 - Fungus - *is that even supposed to be on sale??* - 1

$15 - Life crystal -increases your maximum HP by 20! - 2
""")
#^these are the raised prices^
    while True:
        buy_item = input (f"\nWhat would you like to buy with ${item_money} to spend? Type \"exit\" to leave the shop.\n:")

        if buy_item.lower().strip() == "guitar" and item_money >= 15 and item_guitar == 0:
            print ("you obtained *GUITAR*")
            item_money -= price_guitar
            item_guitar += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "guitar" and item_money >= 15 and item_guitar == 1:
            print("you already bought this item!")
            continue
        if buy_item.lower().strip() == "guitar" and item_money <= 14:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 10 and item_garlic_bread <= 2:
            print("you obtained *GARLIC BREAD*")
            item_money -= price_garlic_bread
            item_garlic_bread += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 10 and item_garlic_bread >= 3:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money <= 9:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 5 and item_cosmic_worm == 0:
            print ("you obtained *COSMIC WORM*")
            item_money -= price_cosmic_worm
            item_cosmic_worm += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 5 and item_cosmic_worm == 1:
            print("You already own this item!")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money <= 4:
            print("you cannot afford this item")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 7 and item_dagger == 0:
            print("you obtained *DAGGER*")
            item_money -= price_dagger
            item_dagger += 1
            item_fist -= 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 7 and item_dagger == 1:
            print("you already own this item!")
            continue
        if buy_item.lower().strip() == "dagger" and item_money <= 6:
            print("you cannot afford this item.")
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 0:
            print("*SOCRATES* that wasnt even... you know what just take it bro")
            time.sleep(0.7)
            print("you obtained *FUNGUS*")
            item_fungus += 1
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 1:
            print("There is no more fungus to collect ;(")
            time.sleep(1)
            print("*SOCRATES' THOUGHTS* why would they even want more wtf??????")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 15 and item_life_crystal <= 1:
            print("you absorbed *LIFE CRYSTAL*")
            item_money -= price_life_crystal
            time.sleep(0.5)
            max_life += 20
            print(f"your max life has been increased to {max_life}! (+ full regen)")
            item_life_crystal += 1
            current_life = max_life
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 15 and item_life_crystal >= 2:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money <= 14:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "exit":
            print("you left the shop and continued to the final room...")
            break




#next part is for if you won first against socrates but old man answered for you. meaning default prices. (below this text)

if shop_prices == 0 and old_man_answer == 1:
    price_guitar += 10
    price_garlic_bread += 5
    price_cosmic_worm += 1
    price_dagger += 5
    price_life_crystal += 10
    price_fungus += 0
    print(f"*SOCRATES* heh, WELCOME {user} TO MY HUMBLE ABODE!")
    time.sleep(1.5)
    print("*SOCRATES* Feel free to browse around and buy what you want, I wont punish you for the old man helping you, so the prices will stay normal")
    time.sleep(3)
    print(f"""[THE CHEDDAR MINE]

Intstructions: Items will show with their name and description beside them.
Example: Price - Item - description - stock.
Happy shopping {user}!

You have ${item_money} to spend :)

$10 - Guitar - Maybe those lessons could come in handy! - 1

$5- Garlic Bread - Heals 50HP, i mean who DOESN'T love garlic bread. - 3

$1 - Cosmic Worm - Just looking at it gives you chills, probably best to leave it alone... - 1

$5 - Dagger - Deals 12 DMG instead of 6 DMG(fists), a simple dagger. - 1

$0 - Fungus - *is that even supposed to be on sale??* - 1

$10 - Life crystal -increases your maximum HP by 20! - 2
""")

    while True:
        buy_item = input (f"\nWhat would you like to buy with ${item_money} to spend? Type \"exit\" to leave the shop.\n:")
        if buy_item.lower().strip() == "guitar" and item_money >= 10 and item_guitar == 0:
            print ("you obtained *GUITAR*")
            item_money -= price_guitar
            item_guitar += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "guitar" and item_money >= 10 and item_guitar == 1:
            print("you already bought this item!")
            continue
        if buy_item.lower().strip() == "guitar" and item_money <= 9:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 5 and item_garlic_bread <= 2:
            print("you obtained *GARLIC BREAD*")
            item_money -= price_garlic_bread
            item_garlic_bread += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 5 and item_garlic_bread >= 3:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money <= 4:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 0:
            print ("you obtained *COSMIC WORM*")
            item_money -= price_cosmic_worm
            item_cosmic_worm += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 1:
            print("You already own this item!")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money <= 0:
            print("you cannot afford this item")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 5 and item_dagger == 0:
            print("you obtained *DAGGER*")
            item_money -= price_dagger
            item_dagger += 1
            item_fist -= 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 5 and item_dagger == 1:
            print("you already own this item!")
            continue
        if buy_item.lower().strip() == "dagger" and item_money <= 4:
            print("you cannot afford this item.")
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 0:
            print("*SOCRATES* that wasnt even... you know what just take it bro")
            time.sleep(0.7)
            print("you obtained *FUNGUS*")
            item_fungus += 1
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 1:
            print("There is no more fungus to collect ;(")
            time.sleep(1)
            print("*SOCRATES' THOUGHTS* why would they even want more wtf??????")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 10 and item_life_crystal <= 1:
            print("you absorbed *LIFE CRYSTAL*")
            item_money -= price_life_crystal
            time.sleep(0.5)
            max_life += 20
            print(f"your max life has been increased to {max_life}! (+ full regen)")
            item_life_crystal += 1
            current_life = max_life
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 10 and item_life_crystal >= 2:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money <= 9:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "exit":
            print("you left the shop and continued to the final room...")
            break



#copied again but if the old man didnt help and user just got it wrong (below this text)

if shop_prices == 0 and old_man_answer == 0:
    price_guitar += 10
    price_garlic_bread += 5
    price_cosmic_worm += 1
    price_dagger += 5
    price_life_crystal += 10
    price_fungus += 0
    print(f"*SOCRATES* heh, WELCOME {user} TO MY HUMBLE ABODE!")
    time.sleep(1.5)
    print("*SOCRATES* Feel free to browse around and buy what you want. And remember, NO REFUNDS! :)")
    time.sleep(3)
    print(f"""[THE CHEDDAR MINE]

Intstructions: Items will show with their name and description beside them.
Example: Price - Item - description - stock.
Happy shopping {user}!

You have ${item_money} to spend :)

$10 - Guitar - Maybe those lessons could come in handy! - 1

$5- Garlic Bread - Heals 50HP, i mean who DOESN'T love garlic bread. - 3

$1 - Cosmic Worm - Just looking at it gives you chills, probably best to leave it alone... - 1

$5 - Dagger - Deals 12 DMG instead of 6 DMG(fists), a simple dagger. - 1

$0 - Fungus - *is that even supposed to be on sale??* - 1

$10 - Life crystal -increases your maximum HP by 20! - 2
""")

    while True:
        buy_item = input (f"\nWhat would you like to buy with ${item_money} to spend? Type \"exit\" to leave the shop.\n:")
        if buy_item.lower().strip() == "guitar" and item_money >= 10 and item_guitar == 0:
            print ("you obtained *GUITAR*")
            item_money -= price_guitar
            item_guitar += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "guitar" and item_money >= 10 and item_guitar == 1:
            print("you already bought this item!")
            continue
        if buy_item.lower().strip() == "guitar" and item_money <= 9:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 5 and item_garlic_bread <= 2:
            print("you obtained *GARLIC BREAD*")
            item_money -= price_garlic_bread
            item_garlic_bread += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 5 and item_garlic_bread >= 3:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money <= 4:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 0:
            print ("you obtained *COSMIC WORM*")
            item_money -= price_cosmic_worm
            item_cosmic_worm += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 1:
            print("You already own this item!")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money <= 0:
            print("you cannot afford this item")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 5 and item_dagger == 0:
            print("you obtained *DAGGER*")
            item_money -= price_dagger
            item_dagger += 1
            item_fist -= 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 5 and item_dagger == 1:
            print("you already own this item!")
            continue
        if buy_item.lower().strip() == "dagger" and item_money <= 4:
            print("you cannot afford this item.")
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 0:
            print("*SOCRATES* that wasnt even... you know what just take it bro")
            time.sleep(0.7)
            print("you obtained *FUNGUS*")
            item_fungus += 1
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 1:
            print("There is no more fungus to collect ;(")
            time.sleep(1)
            print("*SOCRATES' THOUGHTS* why would they even want more wtf??????")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 10 and item_life_crystal <= 1:
            print("you absorbed *LIFE CRYSTAL*")
            item_money -= price_life_crystal
            time.sleep(0.5)
            max_life += 20
            print(f"your max life has been increased to {max_life}! (+ full regen)")
            item_life_crystal += 1
            current_life = max_life
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 10 and item_life_crystal >= 2:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money <= 9:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "exit":
            print("you left the shop and continued to the final room...")
            break


#copied again but if user has the rat with them (below this text)



if socrates_rat == 1:
    print("*SOCRATES* Hey, we should be coming up on my shop!")
    time.sleep(1.5)
    if old_man == 1:
        print("*ALFRED* Oh, the Cheddar Mine is it?")
        time.sleep(1)
        print(f"*SOCRATES* Exactly! ill give you some pretty decent discounts when we get there {user}")
    price_guitar += 7
    price_garlic_bread += 3
    price_cosmic_worm += 1
    price_dagger += 3
    price_life_crystal += 7
    price_fungus += 0
    print(f"*SOCRATES* heh, WELCOME {user} TO MY HUMBLE ABODE!")
    time.sleep(1.5)
    print("*SOCRATES* Feel free to browse around and buy what you want. I am your friend but I dont sell stuff for free yaknow")
    time.sleep(3)
    print(f"""[THE CHEDDAR MINE]

Intstructions: Items will show with their name and description beside them.
Example: Price - Item - description - stock.
Input the item name and as long as you got the money, its all yours!
Happy shopping {user}!

You have ${item_money} to spend :)

$7 - Guitar - Maybe those lessons could come in handy! - 1

$3- Garlic Bread - Heals 50HP, i mean who DOESN'T love garlic bread. - 3

$1 - Cosmic Worm - Just looking at it gives you chills, probably best to leave it alone... - 1

$3 - Dagger - Deals 12 DMG instead of 6 DMG(fists), a simple dagger. - 1

$0 - Fungus - *is that even supposed to be on sale??* - 1

$7 - Life crystal -increases your maximum HP by 20! - 2
""")

    while True:
        buy_item = input (f"\nWhat would you like to buy with ${item_money} to spend? Type \"exit\" to leave the shop.\n:")
        if buy_item.lower().strip() == "guitar" and item_money >= 7 and item_guitar == 0:
            print ("you obtained *GUITAR*")
            item_money -= price_guitar
            item_guitar += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "guitar" and item_money >= 7 and item_guitar == 1:
            print("you already bought this item!")
            continue
        if buy_item.lower().strip() == "guitar" and item_money <= 6:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 3 and item_garlic_bread <= 2:
            print("you obtained *GARLIC BREAD*")
            item_money -= price_garlic_bread
            item_garlic_bread += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 3 and item_garlic_bread >= 3:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "garlicbread" and item_money >= 2:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 0:
            print ("you obtained *COSMIC WORM*")
            item_money -= price_cosmic_worm
            item_cosmic_worm += 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money >= 1 and item_cosmic_worm == 1:
            print("You already own this item!")
            continue
        if buy_item.lower().strip() == "cosmicworm" and item_money <= 0:
            print("you cannot afford this item")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 3 and item_dagger == 0:
            print("you obtained *DAGGER*")
            item_money -= price_dagger
            item_dagger += 1
            item_fist -= 1
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "dagger" and item_money >= 3 and item_dagger == 1:
            print("you already own this item!")
            continue
        if buy_item.lower().strip() == "dagger" and item_money <= 2:
            print("you cannot afford this item.")
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 0:
            print("*SOCRATES* that wasnt even... you know what just take it bro")
            time.sleep(0.7)
            print("you obtained *FUNGUS*")
            item_fungus += 1
            continue
        if buy_item.lower().strip() == "fungus" and item_money >= 0 and item_fungus == 1:
            print("There is no more fungus to collect ;(")
            time.sleep(1)
            print("*SOCRATES' THOUGHTS* why would they even want more wtf??????")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 7 and item_life_crystal <= 1:
            print("you absorbed *LIFE CRYSTAL*")
            item_money -= price_life_crystal
            time.sleep(0.5)
            max_life += 20
            print(f"your max life has been increased to {max_life}! (+ full regen)")
            item_life_crystal += 1
            current_life = max_life
            print(f"you now have {item_money} to spend.")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money >= 7 and item_life_crystal >= 2:
            print("This item is out of stock!")
            continue
        if buy_item.lower().strip() == "lifecrystal" and item_money <= 6:
            print("You cannot afford this item.")
            continue
        if buy_item.lower().strip() == "exit":
            print("you left the shop and continued to the final room...")
            time.sleep(1)
            break

if socrates_rat == 1:
    print("*SOCRATES* Hey, were coming up on the final room, Ive always wondered what the outdoors look like...")
    time.sleep(1.5)

print("As you step into the room, you feel a meanacing aura...")
time.sleep(1)
print("you walk further into the room and see a shadowy figure")
time.sleep(2)
if socrates_rat == 1:
    print("*SOCRATES* Hey... you see that thing too right?")
    time.sleep(1)
print("the figure notices you, and speaks...")
time.sleep(2)
print("*???* A visitor? When was the last time that happened...")
time.sleep(2)
print("*YOU* Who are you?")
time.sleep(1)
print("*???* That's irrelavent, Im hungry, and you will be my next dish.")
time.sleep(2)
print("The figure emerges from the darkness...")
time.sleep(2)
print("Its a...")
time.sleep(2)
print("CAT!? A huge one at that. maybe twice the size of a tiger!")
time.sleep(2)
if socrates_rat == 1:
    print("*SOCRATES* AAAAH!!!! A CAT!?? OF ALL THINGS IT HAAADD TO BE A CAT!?")
    time.sleep(2)
    print("*SOCRATES* FINE! TIME TO PUT OUR FEARS ASIDE AND FIGHT THIS MONSTER!")
    time.sleep(2)
print("*YOU* Its kill or be killed!")
time.sleep(1)
ready_to_fight = input(f"""[FIGHT START]

Hey! This is a little tutorial for your first and final fight so you dont die instantly :)

this will be turn based combat, meaning you and your party takes their turn, then the boss takes a turn.

you will have 3 options throughout the fight. [FIGHT] [COUNTER] [ITEM]

FIGHT - you pull out your best weapon and deal damage to the boss!

COUNTER - if you choose to counter, the boss will attack first, and you have a chance of either countering or getting hit.

ITEM - if you bought anything from the shop, nows the time to use it!

different items have different effects and may alter the story.

so try some stuff out and try not to die!

once you are ready, press [ENTER] to initiate the fight!""")

print(f"GOOD LUCK, {user.upper()}!")
time.sleep(2)
if young_boy == 1:
    print("*JIMBO* hey so uh, i know i havent really been useful to you...")
    time.sleep(2)
    print("*JIMBO* But NOWS THE TIME I CHANGE THAT!!")
    time.sleep(1)
    print(f"*JIMBO* LEAD THE WAY {user.upper()}! ILL FOLLOW UP ON YOUR ATTACKS!")
    time.sleep(1.5)
    print("JIMBO becomes useful! he will follow your previous attack, resulting in an extra dagger strike for 12 DMG!")
    time.sleep(2)
if old_man == 1:
    print(f"*ALFRED* yeah im too old for this. Sorry {user}, but I cant help you in this fight.")
    time.sleep(2)
    print("ALFRED will give words of encouragement from the sidelines!")
    time.sleep(2)




print("*BOSS* only the strong deserve to know my name.")
time.sleep(1)
print("*BOSS* now is your chance to prove yourself, puny human.")
time.sleep(2)
while True:
    boss_choice = input("WHAT IS YOUR MOVE?\n\n[FIGHT]\n\n[COUNTER]\n\n[ITEM]\n\n:")
    if boss_choice.lower().strip() == "fight":
        if item_dagger == 1 and young_boy == 0:
            print("YOU DEALT 12 DMG")
            time.sleep(0.7)
            boss_hp -= dagger_dmg
            print(f"BOSS NOW HAS {boss_hp} HP")
            time.sleep(1)
            if random.random()<0.5:
                print("THE CAT LUNGES TOWARDS YOU AND SCRATCHES!")
                time.sleep(1)
                print("caught off guard, you were HIT!")
                time.sleep(0.7)
                current_life -= 20
                print(f"YOU TOOK 20 DMG! current HP:{current_life}")
                time.sleep(1)
                if current_life <= 0:
                    print("*BOSS* that was almost too easy.")
                    print("\nYOU DIED")
                    sys.exit()
                if current_life >= 1 and boss_hp >= 1:
                    print ("*YOU* Ouch!")
                    time.sleep(0.5)
                    continue
                if current_life >= 1 and boss_hp <= 0:
                        break
            else:
                print("THE CAT MOCKS YOU!")
                time.sleep(1)
                print("*BOSS* HAH! You barely scratched me! Dont waste my time human.")
                time.sleep(1)
                continue


        if item_dagger == 1 and young_boy == 1:
            print("YOU DEALT 12 DMG(2x)!")
            time.sleep(0.7)
            boss_hp -= dagger_dmg
            boss_hp -= dagger_dmg
            print(f"BOSS NOW HAS {boss_hp} HP")
            time.sleep(1)
            if random.random()<0.5:
                print("THE CAT LUNGES TOWARDS YOU AND SCRATCHES!")
                time.sleep(1)
                print("caught off guard, you were HIT!")
                time.sleep(0.7)
                current_life -= 20
                print(f"YOU TOOK 20 DMG! current HP:{current_life}")
                time.sleep(1)
                if current_life <= 0:
                    print("*BOSS* that was almost too easy.")
                    print("\nYOU DIED")
                    sys.exit()
                if current_life >= 1 and boss_hp >= 1:
                    print ("*YOU* Ouch!")
                    time.sleep(0.5)
                    continue
                if current_life >= 1 and boss_hp <= 0:
                    break

                else:
                    print("THE CAT MOCKS YOU!")
                    time.sleep(1)
                    print("*BOSS* HAH! You barely scratched me! Dont waste my time human.")
                    time.sleep(1)
                    continue
        if item_fist == 1 and young_boy == 0:
                print("YOU DEALT 6 DMG")
                time.sleep(0.7)
                boss_hp -= fist_dmg
                print(f"BOSS NOW HAS {boss_hp} HP")
                time.sleep(1)
                if random.random()<0.5:
                    print("THE CAT LUNGES TOWARDS YOU AND SCRATCHES!")
                    time.sleep(1)
                    print("caught off guard, you were HIT!")
                    time.sleep(0.7)
                    current_life -= 20
                    print(f"YOU TOOK 20 DMG! current HP:{current_life}")
                    time.sleep(1)
                    if current_life <= 0:
                        print("*BOSS* that was almost too easy.")
                        print("\nYOU DIED")
                        sys.exit()
                    if current_life >= 1 and boss_hp >= 1:
                        print ("*YOU* Ouch!")
                        time.sleep(0.5)
                        continue
                    if current_life >= 1 and boss_hp <= 0:
                        break
                else:
                    print("THE CAT MOCKS YOU!")
                    time.sleep(1)
                    print("*BOSS* HAH! You barely scratched me! Dont waste my time human.")
                    time.sleep(1)
                    continue


        if item_fist == 1 and young_boy == 1:
                print("YOU DEALT 6 DMG(+12)!")
                time.sleep(0.7)
                boss_hp -= fist_dmg
                boss_hp -= dagger_dmg
                print(f"BOSS NOW HAS {boss_hp} HP")
                time.sleep(1)
                if random.random()<0.5:
                    print("THE CAT LUNGES TOWARDS YOU AND SCRATCHES!")
                    time.sleep(1)
                    print("caught off guard, you were HIT!")
                    time.sleep(0.7)
                    current_life -= 20
                    print(f"YOU TOOK 20 DMG! current HP:{current_life}")
                    time.sleep(1)
                    if current_life <= 0:
                        print("*BOSS* that was almost too easy.")
                        print("\nYOU DIED")
                        sys.exit()
                    if current_life >= 1 and boss_hp >= 1:
                        print ("*YOU* Ouch!")
                        time.sleep(0.5)
                        continue
                    if current_life >= 1 and boss_hp <= 0:
                        break

    if boss_choice.lower().strip() == "counter":
        print("you got ready to counter!")
        time.sleep(1)
        print("THE CAT DARTS TOWARDS TOU INTENDING TO EAT YOU!")
        if hermes_boots == 1:
            time.sleep(2)
            print("BUT YOU WERE TOO FAST!")
            time.sleep(1)
            print(f"countered and dealt {dagger_dmg} DMG!")
            boss_hp -= dagger_dmg
            if current_life >= 1 and boss_hp <= 0:
                break
            time.sleep(1)
            print(f"boss now has {boss_hp}!")
            time.sleep(1)
            print("Must be thanks to those hermes boots you got earlier.")
            time.sleep(2)
            print("*BOSS* OW! HEY! NOBODY CAN ESCAPE MY JAW! HOW THE HELL!?")
            time.sleep(2)
            continue
        if hermes_boots == 0:
            if random.random()<0.5:
                print("YOU GOT HIT! -20 HP")
                current_life -= 20
                if current_life <= 0:
                        print("*BOSS* that was almost too easy.")
                        print("\nYOU DIED")
                        sys.exit()
                if current_life >= 1:
                    time.sleep(2)
                    print(f"you now have {current_life} HP")
                    time.sleep(1)
                    continue
            else:
                print("YOU DODGED AND COUNTERED, JUST BARELY!")
                time.sleep(1)
                print(f"countered and dealt {dagger_dmg} DMG")
                boss_hp -= dagger_dmg
                time.sleep(1)
                if boss_hp >= 1:
                    print("*BOSS* You got lucky, human...")
                    time.sleep(2)
                    continue
                if current_life >= 1 and boss_hp <= 0:
                    break



    if boss_choice.lower().strip() == "item":

        choice = input(f"Which item do you want to use?\n\nYou have:\n\n{item_guitar} guitar(s)\n\n{item_garlic_bread} garlic bread(s)\n\n{item_cosmic_worm} cosmic worm(s)\n\n{item_fungus} fungus\n\n:").lower().strip()
        if choice == "guitar" and item_guitar == 1 and boss_charm == 0:
            print("You start playing a melody for the boss.")
            time.sleep(1)
            print("*BOSS* hey, I recognize that song... uhhh nevermind that")
            boss_charm += 1
            continue
        if choice == "guitar" and item_guitar == 1 and boss_charm == 1:
            print("You start playing the same melody for the boss.")
            time.sleep(1)
            print("*BOSS* dude where was that from...hmmm")
            boss_charm += 1
            continue
        if choice == "guitar" and item_guitar == 1 and boss_charm == 2:
            print("You start playing the same melody again for the boss.")
            time.sleep(1)
            print("*BOSS* okay okay STOP THE FIGHT!! You're playing tricks on me arent you human?\n\nThat was the song my mother used to sing to me back when I was still just a kitten.")
            time.sleep(5)
            print("*BOSS* come to think of it, my mother always told me to treat others how I would like to be treated...")
            time.sleep(3)
            print("*BOSS* You know what man, I think ive been losing myself for the past couple years...")
            time.sleep(4)
            print("*BOSS* How about lets just forget about all this and ill let you through, kay?")
            time.sleep(3)
            print("Mittens by the way, thats my name. I've always been kinda embarrassed about it so I made up that rule to find out my name.")
            time.sleep(5)
            print("*MITTENS* Well, heres the exit.")
            time.sleep(2)
            come_back = input("*MITTENS* And before you go, you mind coming back every once in a while? it gets pretty lonley around here...\n\n(Y/N):")
            if come_back.lower().strip() == "Y":
                print("*MITTENS* Thanks, it means a ton")
                time.sleep(1)
                if socrates_rat == 1:
                    print("*SOCRATES* No problem! once you get to know them, cats are actually pretty chill.")
                if old_man == 1:
                    print("*ALFRED* Sure thing Mittens!")
                if young_boy == 1:
                    print("*JIMBO* Deffinetly!! I wanna ride you when we come back though!")
            print("As you leave the dungeon, you feel a sense of relief, knowing that you overcame this challenge and made some friends along the way...")
            time.sleep(6)
            print("THE END")
            sys.exit()


        if choice.lower().strip() == "garlicbread" and item_garlic_bread >= 1:
            print("You healed 50HP!")
            current_life += 50
            continue
        if choice.lower().strip() == "garlicbread" and item_garlic_bread >= 0:
            print("You dont have any garlic bread!")
            continue


        if choice.lower().strip() == "cosmicworm" and item_cosmic_worm == 1:
            are_you_sure1 = input ("holding it in your hands, it is pulsating with an incomprihensable amount of power.\n\n Are you SURE you want to use it? (Y/N):")
            if are_you_sure1.lower().strip() == "y":
                #make story of DoGgie destroying the world
                print("You hold it up and throw it at the boss.")
                time.sleep(2)
                print("A blinding flash of light fills the cave")
                time.sleep(1.5)
                if socrates_rat == 1:
                    print("*SOCRATES* AH! WHAT THE HELL DID YOU JUST DO!?")
                    time.sleep(1)
                print("A NEW BEAST HAS AWOKEN!")
                time.sleep(2)
                print("*???* ONLY WHO IS WORTHY WILL HAVE SUMMONED ME.")
                time.sleep(1)
                print("ITS A GIANT WORM!!")
                time.sleep(1)
                if socrates_rat == 1:
                    print(f"*SOCRATES* THATS THE DEVOURER!! YOUVE DOOMED US ALL {user.upper()}!")
                    time.sleep(2)
                    print(f"*DEVOURER* Thats right. Now that you have freed me, {user}, I shall tear this world apart.")
                    time.sleep(3)
                    print("*DEVOURER* Starting with YOU!")
                    time.sleep(1.5)
                    print("you see the worm fly towards you for a split second before the world goes dark...")
                    time.sleep(4)
                    print(f"CONGRATULATIONS {user.upper()}! You have successfully doomed the entire world!")
                    time.sleep(3)
                    print("kind of overkill for a large cat dont you think?")
                    time.sleep(3)
                    print("THE END")
                    sys.exit()
                print(f"*???* Now that you have freed me, {user}, I shall tear this world apart.")
                time.sleep(3)
                print("*???* Starting with YOU!")
                time.sleep(1.5)
                print("you see the worm fly towards you for a split second before the world goes dark...")
                time.sleep(4)
                print(f"CONGRATULATIONS {user.upper()}! You have successfully doomed the entire world!")
                time.sleep(3)
                print("kind of overkill for a large cat dont you think?")
                time.sleep(3)
                print("THE END")
                sys.exit()


                #eating fungus leaves a weird feeling in your stomach, healing 1HP
                #socrates will question why you ate it and be in shock


        if choice == "fungus" and item_fungus == 1:
            print("You take the fungus and eat it whole.")
            time.sleep(2)
            print("A strange feeling is left in your stomach...")
            time.sleep(1.5)
            if socrates_rat == 1:
                print("*SOCRATES' THOUGHTS* WHY DID HE EAT IT!?")
                time.sleep(1.5)
            print("You healed 1HP!")
            current_life += 1
            time.sleep(1)
            continue


print("*BOSS* GAH! you... YOU!?? HOW DID A MERE CHILD MANAGE TO BEST ME!?!?")
time.sleep(3)
if socrates_rat == 1:
    print("*SOCRATES* THATS WHAT IM SAYING!!")
    time.sleep(1.5)
print("*BOSS* well then *huff* I guess I have to keep my side of the deal huh?")
time.sleep(2)
print("My name...")
time.sleep(2)
print("is.....")
time.sleep(5)
print("MITTENS!")
time.sleep(1.5)
print("*MITTENS* THATS RIGHT! MY NAME IS MITTENS!!!")
time.sleep(2)
print("*MITTENS* ARENT YOU HAPPY TO FIND THAT OUT HUH?")
time.sleep(1.5)
print("*MITTENS* such a stupid name...")
time.sleep(1)
while True:
    mittens_name = input ("\n1: I like that name!\nor\n2: lmfaooo\n:")
    if mittens_name.lower().strip() == "1":
        print("*MITTENS* Dont lie to me human, I know you're holding back laughter.")
        time.sleep(2)
        print(f"*MITTENS* anyways, {user}, go on ahead and exit this dungeon.")
        time.sleep(1)
        print("*MITTENS* I wont be able to stop you if i wanted to.")
        time.sleep(3)
        break
    elif mittens_name.lower().strip() == "2":
        print("*MITTENS* yeah yeah laugh all you want...")
        time.sleep(1.5)
        print("*MITTENS* the exit is just over there when you're ready to leave.")
        time.sleep(3)
        break
    else:
        try_again = input("INVALID INPUT! type either 1 or 2 to make your choice. Press [ENTER] to continue.")
        continue


print("you exit the dungeon and its now night time.")
time.sleep(2)
print("you spent all day traveling and fighting. now you can rest.")
time.sleep(3)
if socrates_rat == 1:
    print("*SOCRATES* HEY!! DONT FORGET ABOUT ME!")
    time.sleep(2)
    print("*SOCRATES* I dont really got a place to go, so im just gonna follow you, kay?")
    time.sleep(3)
    print("*SOCRATES* I mean were practically best buds now right?")
    time.sleep(2)
    print("as you begin your walk back home, you hear a voice behind you.")
    time.sleep(2)
    if old_man == 1:
        print("*ALFRED* HEY! YOUNGSTER! BE SAFE ON THE JOURNEY AHEAD!")
    elif young_boy == 1:
        print(f"*JIMBO* HEY! {user.upper()}! LETS MEET UP AGAIN SOMETIME OKAY?")

    time.sleep(3)
    print("you say your goodbyes and walk home...")
    time.sleep(2)
    print("THE END")
    sys.exit()


print ("as you begin your walk back home, you hear a voice behind you.")
time.sleep(2)
if old_man == 1:
    print("*ALFRED* HEY! YOUNGSTER! BE SAFE ON THE JOURNEY AHEAD!")
elif young_boy == 1:
    print(f"*JIMBO* HEY! {user.upper()}! LETS MEET UP AGAIN SOMETIME OKAY?")

time.sleep(3)
print("you say your goodbyes and walk home...")
time.sleep(2)
print("THE END")
sys.exit()







#plan kinda might be innacurate just rough idea->

#allow the user to go backwards if they have not followed down a path yet.
#if the user has gone down a path, they are not allowed to backtrack.

#room to the left: an extremely intelligent (and cocky) rat blocks your way and asks you a riddle
#get the riddle correct: full heal plus overheal
#get wrong: rat bites you and takes 20hp and calls you

#room to the right: there is a special one time use key on a pedestal and two chests in front of you.
#one chest is huge and made of gold, the other is small and made of wood
#if the user chooses the gold chest, destory the key and give the user *hermes boots* which allow for better dodge chance
#if the user chooses the small chest, destroy the key and give the user a health potion that heals 50HP (you have 100 max HP)
#if the user chooses to save the key for later, make a line that checks if the key is stored, if true then allow the user to open one future chest.
#if false do not allow chest opening.

#path straight: you are presented with two ways, an old man and a young boy are at either path, each trying to convince you to come with them.
#the old man says the boy is a devil and will only cause trouble
#the young boy says the old man is a creep and will distract you during fights
#choose which one to trust and follow them down that path.
#if the user picks to follow the boy, they will recieve a dagger (12dmg instead of fists that do 6)
#if the user picks to follow the old man, they will recieve assistance on future puzzles.
