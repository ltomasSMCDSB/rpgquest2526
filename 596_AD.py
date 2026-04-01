#flowchart https://app.eraser.io/workspace/C1EyX4oDgn6Gxdu4RwVi
#Game name: 596 AD
playerhealth = 65
playersworddamage = 5
playeraxedamage = 7
playerdamage = 5
playercrit = playerdamage * 2
gold = 0
silver = 0
copper = 0

goblin1health = 15
goblin1damage = 6
goblin1critdamage = 9

mimichealth = 20
mimicdamage = 7

skeleton1health = 12
skeleton1damage = 8

skeleton2health = 15
skeleton2damage = 7

slime1health = 8
slime1damage = 3

slime2health = 5
slime2damage = 5

axedoor1 = "do"
axedoor11 = "you"
sworddoor11 = "like"
sworddoor1 = "pancakes"
door2interact = "or"
door2interact2 = "waffels"
door1interact2 = "I"
door1interact = "perfer"
secondinteraction = "pancakes"
axedoor2 = "with"
axedoor22 = "blueberries"
sworddoor2 = "yum"
sworddoor22 = "wfvpk"
door1kill = "qehk"
door2kill = "wndwfon"
goblincorpseloot = "afefae"
goblincorpseloot1 = "weofu"
goblincorpseloot2 = "rweiuyfgkw"
goblincorpseloot22 = "werkhfbv"
teleporttome = "fasafea"
teleporttomeleave = "urwdf"
teleporttomeleave2 = "qwikehyfr"
room1look = "efvpefv"
room1loot = "jdlnfw"
room1loot2 = "wefoj"
room1door1 = "wefuosdfb"
room1door11 = "gsddfgk"
room1door111 = "sdff"
room1door2 = "odfjn"
room1door22 = "slmnkwdk"
room1door222 = "sdjnl"
chestlootinteract = "sdfjfg"
skeleton2kill = "ugpcou"
room1door2look = "ibhsd"

print("\t    Hello adventurer\nYou gain conciousness in a wet cold stone room\nYou have armor on but no weapon\nWhat do you want to do")
firstinteraction = input("(Figure out where you are) (Find an exit) (Look for a weapon): ")

if firstinteraction.strip().lower() == "figure out where you are":
    print("You look around and you see that your in a stone room\nYou remember seeing something like this before \nAnd you remember it's a dungeon that you had enterd\nWhat do you want to do next")
    secondinteraction = input("(Find an exit) (Look for a weapon): ")

if firstinteraction.strip().lower() == "find an exit" or secondinteraction.strip().lower() == "find an exit":
        print("You see two big wooden doors, you don't know whats behind them\nWhat do you do next")
        thirdinteraction = input("(Go to door 1) (Go to door 2): ")
        if thirdinteraction.strip().lower() == "go to door 1":
            print("When you get to door 1 you decide to peek inside\nYou see 2 slime\nWhat do you do next")
            door1interact = input("(Open door and enter) (Go to the other door) (Look for a weapon): ")
            if door1interact.strip().lower() == "open door and enter":
                 print("You enter the door and the 2 slimes start attacking you and you have no way of protecting yourself and die")
            if door1interact.strip().lower() == "go to other door":
                 print("You go to the other door and when you get to door 2 you decide to peek inside\nYou see 2 slimes\nWhat do you do next")
                 door2interact2 = input("(Open door and enter) (Look for a weapon): ")
                 if door2interact2.strip().lower() == "open door and enter":
                      print("You enter the door and the 2 slimes start attacking you and you have no way of protecting yourself and die")
        if thirdinteraction.strip().lower() == "go to door 2":
            print("When you get to door 2 you decide to peek inside\nYou see 1 goblin\n what do you do next")
            door2interact = input("(Open door and enter) (Go to the other door) (Look for a weapon): ")
            if door2interact.strip().lower() == "open door and enter":
                 print("You enter the door and the goblin starts attacking you and you have no way of protecting yourself and die")
            if door2interact.strip().lower() == "go to the other door":
                 print("You go to the other door and when you get to door 1 you decide to peek inside\nYou see 1 goblin\nWhat do you do next")
                 door1interact2 = input("(Open door and enter) (Look for a weapon): ")
                 if door1interact2.strip().lower() == "open door and enter":
                      print("You enter the door and the 2 slimes start attacking you and you have no way of protecting yourself and die")

if firstinteraction.strip().lower() == "look for a weapon" or secondinteraction.strip().lower() == "look for a weapon" or door1interact.strip().lower() == "look for a weapon" or door1interact2.strip().lower() == "look for a weapon" or door2interact.strip().lower() == "look for a weapon" or door2interact2.strip().lower() == "look for a weapon":
    print("You look for a weapon and see two weapons on the wall")
    weapon = input("(Sword) (Great Axe): ")
    if weapon.strip().lower() == "sword":
        playerdamage = 5
        print("You pick up the sword and see your reflection on it's metal surface\nYou also see two different large wooden doors on different sides of the room\nWhat do you want to do next")
        sworddoorinteract = input("(Go to door 1) (Go to door 2): ")
        if sworddoorinteract.strip().lower() == "go to door 1":
             print("You got to the first door with your sword\nYou look inside and see 2 slimes\nWhat do you want to do next")
             sworddoor1 = input("(Go to door 2) (Enter door and attack): ")
             if sworddoor1.strip().lower() == "go to door 2":
                  print("You go to the other door")
                  sworddoor22 = "yes"
        if sworddoorinteract.strip().lower() == "go to door 2":
             print("You got to the second door with your sword\nYou look inside and see 1 goblin\nWhat do you want to do next")
             sworddoor2 = input("(Go to door 1) (Enter door and attack): ")
             if sworddoor2.strip().lower() == "go to door 1":
                  print("You go to the other door")
                  sworddoor11 = "yes"
    if weapon.strip().lower() == "great axe":
        playerhealth = 43
        playerdamage = 7
        print("You pick up the great axe and you see your reflection on it's metal surface\nYou also see two different large wooden doors on different sides of the room\nWhat do you want to do next")
        axedoorinteract = input("(Go to door 1) (Go to door 2): ")
        if axedoorinteract.strip().lower() == "go to door 1":
             print("You got to the first door with your axe\nYou look inside and see 2 slimes\nWhat do you want to do next")
             axedoor1 = input("(Go to door 2) (Enter door and attack): ")
             if axedoorinteract == "go to door 2":
                  print("You go to the other door")
                  axedoor22 = "yes"
        if axedoorinteract.strip().lower() == "go to door 2":
             print("You got to the second door with your axe\nYou look inside and see 1 goblin\nWhat do you want to do next")
             axedoor2 = input("(Go to door 1) (Enter door and attack): ")
             if axedoorinteract == "go to door 1":
                  print("You go to the other door")
                  axedoor11 = "yes"

if axedoor1.strip().lower() == "enter door and attack" or sworddoor1.strip().lower() == "enter door and attack" or sworddoor11 == "yes" or axedoor11 == "yes":
     print(f"You enter the first door with 2 slimes\nYou attack the first slime for {playerdamage} damage the first slime has {slime1health - playerdamage} health left\nThe first slime attacks you for {slime1damage} damage and then the second slime attacks you for {slime2damage} damage \nYou have {playerhealth - slime1damage - slime2damage} health left \nYou attack the first slime again for {playerdamage} damage")
     playerhealth = playerhealth - slime1damage - slime2damage
     print(f"You killed the first slime but the second slime deals {slime2damage} damage \nYou have {playerhealth - slime2damage} health left\nYou attack the second slime for {playerdamage} damage they die in one hit\nWhat do you want to do next")
     playerhealth = playerhealth - slime2damage
     door1kill = input("(Look for anything left behind from the slimes) (Look around): ")
     if door1kill.strip().lower() == "look for anything left behind from the slimes":
          print("You go over to where you killed the first slime and find there is a silver and 2 copper coins\nWhat do you want to do next")
          silver = silver + 1
          copper = copper + 2
          room1loot = input("(Loot the other slime) (Look around): ")
          if room1loot.strip().lower() == "loot the other slime":
               print("You loot the other slime for 12 copper pieces and then")
               copper = copper + 12
               room1loot2 = "look around"

if room1loot2.strip().lower() == "look around" or room1loot.strip().lower() == "look around" or door1kill.strip().lower() == "look around":
     print("You look around the room and notice it's simaler to the last room but a little bigger\nYou see 2 more doors but from the corner of your eye you notice a wooden chest\nWhat do you want to do next")
     room1look = input("(Go to door 1) (Go to door 2) (Inspect the chest): ")
     if room1look.strip().lower() == "inspect the chest":
          print("You to the chest and when you look at the chest you see a lock\nWhen you touch the chest it opens on it's own\nAs you look inside you see some cobwebs and a few peices of stale bread that hasn't gone moldy some how\nAs you dig a little further you find 3 silver coins and 8 copper coins\nWhat do you want to do next")
          silver = silver + 3
          chestlootinteract = input("(Go to door 1) (Go to door 2): ")
     if room1look.strip().lower() == "go to door 1" or chestlootinteract.strip().lower() == "go to door 1":
          print("You go to the first door and when you look inside you can't see much but an empty dark room\nWhat do you want to do next")
          room1door1 = input("(Enter) (Go to door 2): ")
          if room1door1.strip().lower() == "go to door 2":
               print("You go to the second door and when you look inside you find it is a small space with a chest\nWhat do you want to do next")
               room1door22 = input("(Enter) (Go to door 1): ")
               if room1door22.strip().lower() == "go to door 1":
                    print("You go to the first door and when you look inside you can't see much but an empty dark room\nWhat do you want to do next")
                    room1door111 = input("(Enter): ")
     if room1look.strip().lower() == "go to door 2" or chestlootinteract.strip().lower() == "go to door 2":
          print("You go to the second door and when you look inside you find it is a small space with a chest\nWhat do you want to do next")
          room1door2 = input("(Enter) (Go to door 1): ")
          if room1door2.strip().lower() == "go to door 1":
               print("You go to the first door and when you look inside you can't see much but an empty dark room\nWhat do you want to do next")
               room1door11 = input("(Enter) (Go to door 2): ")
               if room1door11.strip().lower() == "go to door 2":
                    print("You go to the second door and when you look inside you find it is a small space with a chest\nWhat do you want to do next")
                    room1door222 = input("(Enter): ")

if room1door1.strip().lower() == "enter" or room1door11.strip().lower() == "enter" or room1door111.strip().lower() == "enter" or room1door2look.strip().lower() == "go to door 1":
     print("You open the door first door to a dark room and as you step into the room \nLanterns along the walls light to the path down a long corridor\nWhile you follow the path the lights made you notice 2 piles of bones beside 2 weapons\nWhen you get closer they begin to animate themselves as 2 skeletons form")
     print(f"You attack the first skeleton for {playerdamage} damage the first skeleton is at {skeleton1health - playerdamage} health they both retaliate \nThe first skeleton attacks you for {skeleton1damage} damage and the second one hits you for {skeleton2damage} damage\nYour at {playerhealth - skeleton1damage - skeleton2damage} health left")
     playerhealth = playerhealth - skeleton1damage - skeleton2damage
     skeleton1health = skeleton1health - playerdamage
     print(f"You go to attack the first skeleton dealing {playerdamage} damage")
     skeleton1health = skeleton1health - playerdamage
     if skeleton1health <= 0:
          print("Killing it")
          print(f"You go to attack the second skeleton but it parries your attack as it makes a counter attack hitting you for {skeleton2damage} damage\nYou have {playerhealth - skeleton2damage} health left\nYou hit the skeleton for {playerdamage} damage it has {skeleton2health - playerdamage} health left")
          skeleton2health = skeleton2health - playerdamage
          playerhealth = playerhealth - skeleton2damage
          print(f"The skeleton hits you for {skeleton2damage} you have {playerhealth - skeleton2damage} health left\nYou attack the skeleton for {playercrit} damage\nA critical hit\nKilling it")
          print("As you see the bones fall down hitting the ground almost in slow motion due to your sorry state\nYou follow down the corridor and as you turn a corner you see a set of stairs\nYou follow the stairs up and find yourself outside of the dungeon finally free and able to relax\n\nThis is the forth good ending thank you for playing")
     else:
          print(f"The skeleton has {skeleton1health} health left")
          print(f"They both attack you the first skeleton hits you for {skeleton1damage} damage and the second hits you for {skeleton2damage} damage\nYou have {playerhealth - skeleton1damage - skeleton2damage} health left\nYou attack the first skeleton one more time killing it")
          skeleton1health = skeleton1health - playerdamage
          playerhealth = playerhealth - skeleton1damage - skeleton2damage
          print(f"The second skeleton hits you for {skeleton2damage} damage\nYou have {playerhealth - skeleton2damage} health left\nYou hit them back for {playerdamage} damage\nThey have {skeleton2health - playerdamage} health left")
          playerhealth = playerhealth - skeleton2damage
          skeleton2health = skeleton2health - playerdamage
          print(f"They hit back for {skeleton2damage} damage\nYou have {playerhealth - skeleton2damage} health left\nYou hit them back for {playerdamage} damage\nThey have {skeleton2health - playerdamage} health left")
          playerhealth = playerhealth - skeleton2damage
          skeleton2health = skeleton2health - playerdamage
          print(f"They hit back for {skeleton2damage} damage\nYou have {playerhealth - skeleton2damage} health left\nYou hit them back for {playerdamage} damage\nAs you see the bones fall down hitting the ground almost in slow motion due to your sorry state\nYou follow the stairs up and find yourself outside of the dungeon finally free and able to relax\n\nThis is the fifth good ending thank you for playing")

if room1door2.strip().lower() == "enter" or room1door22.strip().lower() == "enter" or room1door222.strip().lower() == "enter":
     print(f"You open the second door to find a closet of some sort with some random scraps of leather and a few turn up clothes\nYou also find a chest\nWhat do you want to do next")
     room1door2look = input("(Loot the chest) (Go to door 1): ")
     if room1door2look.strip().lower() == "loot the chest":
          print(f"You go to loot the chest and right as you touch it the lid it springs open to reveal sharp teeth and a grotest mouth\nIt's a mimic and before you have time to react it swallows you slowly digesting you inside it's stomach protected by it's chest exterior\n\nThis is the second bad ending thank you for playing")

if axedoor2.strip().lower() == "enter door and attack" or axedoor22.strip().lower() == "enter door and attack" or sworddoor2.strip().lower() == "enter door and attack" or sworddoor22.strip().lower() == "enter door and attack":
     print(f"You enter the second door with 1 goblin\nYou attack the goblin for {playerdamage} damage the goblin has {goblin1health - playerdamage} health left\nThe goblin retaliates and hits you for {goblin1damage} damage\nYou have {playerhealth - goblin1damage} health left")
     playerhealth = playerhealth - goblin1damage
     goblin1health = goblin1health - playerdamage
     print(f"The goblin reacts quickly to your attack and attacks you dealing {goblin1damage} damage \nLeaving you at {playerhealth - goblin1damage} health\nYou attack the goblin once more for {playerdamage} damage\nThe goblin has {goblin1health - playerdamage} health left")
     playerhealth = playerhealth - goblin1damage
     goblin1health = goblin1health - playerdamage
     print(f"With the last of the goblins strength he makes a final effort to attack you hitting you for {goblin1critdamage} damage\nAfter using the last of it's strength it falls to the ground\nWhat do you want to do next")
     door2kill = input("(Loot the corpse) (Look around): ")
     if door2kill.strip().lower() == "loot the corpse":
          print("You go to loot the corpse of the goblin you killed\nAs you walk over to the corpse a shimmer of light hits your eyes\nYou find a dagger that was hidden on there back\nWhat do you want to do next")
          goblincorpseloot = input("(Loot the dagger) (Keep looting) (Look around): ")
          if goblincorpseloot.strip().lower() == "loot the dagger":
               print("As you pick up the dagger you check it for any damage and as you do this you the reflection of the room that you entered\nWhen you turn around")
               goblincorpseloot1 = "look around"
          if goblincorpseloot.strip().lower() == "keep looting":
               print("You keep looting trying to find anything of value\nYou find a small crude leather pouch with a few cons and buttons\nYou look at the bag and see that there are inessials A.P\nYou don't know who that is but you are very curios about who that might be\nWhat do you want to do next")
               goblincorpseloot2 = input("(Look around) (Look for a book about the pouch): ")
               if goblincorpseloot2.strip().lower() == "look for a book about the pouch":
                    print("You look up from the pouch and")
                    goblincorpseloot22 = "look around"

#ending 1 good ending
if door2kill.strip().lower() == "look around" or goblincorpseloot.strip().lower() == "look around" or goblincorpseloot1.strip().lower() == "look around" or goblincorpseloot2.strip().lower() == "look around" or goblincorpseloot22.strip().lower() == "look around":
     print("You find yourself in a large old run down library with cobwebs strung along the walls covering most of the books\nAs you walk along the tall bookshelves you run your hand along the spine of the books\nAnd as you are doing this you feel a book that has a spine like none of the other books you have felt\nYou stop and take it of the bookshelf\nYou read the cover of the book and it Viam et Viam\nWhat do you want to do next")
     teleporttome = input("(Open and read) (Leave it): ")
     if teleporttome.strip().lower() == "leave it":
          print("As you turn to leave you hear someone or something saying set me free from my prison\nYou turn back and see that the tome moved from where you put it down\nAs you go to pick it up it keeps saying the words on the cover Viam et Viam, Viam et Viam, Viam et Viam\nWhat do you want to do next")
          teleporttomeleave = input("(Give in) (Leave and walk away): ")
          if teleporttomeleave.strip().lower() == "give in":
               print("You give in and repeat the words out loud triggering the spell transforming the tome to dust\nThe dust swirls around you blocking your view\nOnce the dust settles you find yourself somewhere unfamiliar but free from the restrictions of the dungeon\n\nThis is the first good ending thank you for playing")
          if teleporttomeleave.strip().lower() == "leave and walk away":
               print("You put down the tome and start to walk away but the tome speeks out to you and warns you\nIf you leave me you will regret it\nWhat do you want to do next")
               teleporttomeleave2 = input("(Listen) (Don't listen): ")
               if teleporttomeleave2.strip().lower() == "listen":
                    print("You give in and repeat the words out loud triggering the spell transforming the tome to dust\nThe dust swirls around you blocking your view\nOnce the dust settles you find yourself somewhere unfamiliar but free from the restrictions of the dungeon\n\nThis is the second good ending thank you for playing")
               if teleporttomeleave2.strip().lower() == "don't listen":
                    print("You don't listen to it's warning and walk away the book curses you and says \nYou will get lost like the rest of them\nAs you start walking you start to notice that you keep passing the same spot \nWhen you turn around you notice there is no wall behind you\nAnd as continue walking it seems theres no end in sight and as you lose hope and lose your way you start to go insane\nAs you finally give up you regret not taking the tomes advice and blame it for this whole mess\nAs it begins it ends the same as you see your vision starting to blur and darken you lose consciousness and wake to find yourself in the same senario you first woke up to and you here a voice that says\nThe circle continues\n\nThis is the first bad ending thank you for playing")
     if teleporttome.strip().lower() == "open and read":
          print("As you open the tome you notice that all of the pages are blank except for one\nThe page that isn't blank is a one time use spell to teleport to the surface\nYou use the tome by placing your hand over the cover and say the words written on the tome\nViam et Viam\nAs you speek the sacared words written in the tome it turns to dust\nThe dust swirls around you blocking your view\nOnce the dust settles you find yourself somewhere unfamiliar but free from the restrictions of the dungeon\n\nThis is the third good ending thank you for playing")

else:
    print("You sit there and do nothing")
