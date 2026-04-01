#Game name: JOURNEY
print ("\nWelcome to JOURNEY.")
print ("\nWhen playing this game:")
print ("\nAnswer each question with the numbers, letters, or words that are asked for.")

print ("\nYour boat has washed up on an isolated island in the middle of the ocean. You and your cat named Potato jump out of the boat and look around. You're here because this was the last location your friend was when he went missing. Your goal is to find him and bring him back to your boat. The jungle in front of you is dense, completely dark, and creepy sounds come from within. The beach is brighter, but the sand ripples under your feet as if there are creatures hiding underground.")
print ("Health = 100")
print ("Inventory is empty")
Health = (int(100))
inventory = ("Empty")
name = input ("\nEnter your characters name:")

direction = input ("\nWhich way do you go? Through the jungle (A) or down the beach (B)?")

if direction.upper().strip() == "A":
    path = input ("\nYou enter the jungle and find two paths. One path has a tiger (1) and one has a monkey (2). Which path do you choose to go down?")
    if path.upper().strip() == "1":
        print ("\nYou and Potato walk down the path with the tiger. The tiger jumps at you and scratches your arm! You grab Potato and manage to get past it, running away deeper into the jungle. You lose 10 health points.")
        health1 = (int(10))
        print(f"Health =  {int(Health) - int(health1)}")
        print ("Inventory is empty")
        health1 = (int(Health) - int(health1))
    if path.upper().strip() == "2":
        print ("\nYou and Potato choose to take the path with the monkey. The monkey walks towards you and takes your hand. It puts Potato on its back and guides you through the jungle. You feel safe with the monkey. As it is about to leave you on your journey, it gives you a shiny green key. You gain 20 health points. You put the key in your pocket and continue walking through the jungle.")
        health1 = (int(20))
        print(f"Health =  {int(Health) + int(health1)}")
        print ("Inventory = shiny green key")
        health1 = (int(Health) + int(health1))
        inventory1 = ("shiny green key")

    journey = input ("\nYou and Potato are tired of walking at this point, and you feel as if you will never find your friend. As you are lost in your thoughts, Potato gives a loud meow and you look down at him, noticing you are about to walk into a deep pond of green algae and swirling water. You take in your surroundings and see a small mud structure that looks like a jail on the other side of the pond. From where you're standing you can just make out an arm waving from inside the house. That must be your friend! You have found him, but how will you get to him? Do you choose to swim across the pond (0) or grab a vine and swing over? (00)")
    if journey.upper().strip() == "0":
        shinygreenkey = input (f"\nYou put Potato on your head and slowly step into the water. As you swim across, the algae starts to form large shapes around you. You manage to get to the other side where your friend is. '{name}! You found me! Help get me out!' You notice a keyhole on the door. Do you have the shiny green key? yes/no:")
        if shinygreenkey.lower().strip() == "yes":
            print ("\nYou insert the key and turn the lock, freeing your friend. You decide to keep the key and put it in your pocket. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat. You gain 25 health points for saving your friend!")
            health2 = (int(25))
            print(f"Health =  {int(health1) + int(health2)}")
            print ("Inventory = shiny green key")
            health2 = (int(health1) + int(health2))
            inventory1 = ("shiny green key")
        if shinygreenkey.lower().strip() == "no":
            integer = input ("\nYou don't have the key for the keyhole so you decide to kick the door down. Choose an integer above 1:")
            try:
                print (f"\nYou kick the door {integer} times. The door breaks and your friend is free. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")
            except:
                print (f"\nYou kick the door {integer} times. Then you kick it another {integer} times, and the door breaks open. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")

    if journey.upper().strip() == "00":
        print ("\nYou and Potato grab onto a vine and swing across the water. As you soar through the air, the vine snaps and you both fall towards the dark water below. You land in the water hard and hurt your arm. Potato is okay but you lose 10 health points. You grab Potato and swim the rest of the way to the other side. When you crawl out of the water you walk over to the bars where your friend is.")
        health2 = (int(10))
        print (f"Health =  {int(health1) - int(health2)}")
        print ("Inventory = shiny green key")
        health2 = (int(health1) - int(health2))
        inventory1 = ("shiny green key")
        shinygreenkey = input (f"\nYou notice a keyhole on the door. Do you have the shiny green key? yes/no:")
        if shinygreenkey.lower().strip() == "yes":
            print ("\nYou insert the key and turn the lock, freeing your friend. You decide to keep the key and put it in your pocket. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat. You gain 25 health points for saving your friend!")
            health3 = (int(25))
            print(f"Health =  {int(health2) + int(health3)}")
            print ("Inventory = shiny green key")
            health3 = (int(health2) + int(health3))
            inventory1 = ("shiny green key")
        if shinygreenkey.lower().strip() == "no":
            integer = input ("\nYou don't have the key for the keyhole so you decide to kick the door down. Choose an integer above 1:")
            try:
                print (f"\nYou kick the door {integer} times. The door breaks and your friend is free. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")
            except:
                print (f"\nYou kick the door {integer} times. Then you kick it another {integer} times, and the door breaks open. You, Potato, and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")

if direction.upper().strip() == "B":
    chestopen = input ("\nYou and Potato choose to walk along the beach. The sand under your feet is moving unnaturally. You have walked a far distance before you come across a small golden chest sitting in the middle of the beach. Do you want to open it? yes/no:")
    if chestopen.lower().strip() == "yes":
        print ("\nYou open the chest and look inside. There is a shiny yellow coin sitting on a velvet pillow. You take the coin and put it in a pouch around Potato's neck. You gain 5 health points. You start to think that your friend is not on the beach so you decide to enter the jungle.")
        print(f"Health =  {int(Health) + 5}")
        print ("Inventory = shiny yellow coin")
        health1 = (int(Health) + 5)
        inventory2 = ("shiny yellow coin")
    if chestopen.lower().strip() == "no":
        print ("\nYou and Potato don't want to open the box because you feel it is unsafe. As you walk past the chest, the tide comes in and a giant crab emerges and grabs you and Potato. It throws you over the treetop and into the jungle. You land in a deep pond and cutt yourself on a sharp rock. You lose 15 health points.")
        print(f"Health =  {int(Health) - 15}")
        print ("Inventory is empty")
        health1 = (int(Health) - 15)
        inventory2 = ("Empty")

    jungle = input ("\nYou hear a scream from the distance. That must be your friend calling for help! You run towards the noise and see your friend sitting in a tree while a panther circles below. The panther sees you and walks towards you. 'If you want your friend you have to offer me something in return. I accept shiny yellow coins.' Do you have a shiny yellow coin to give to the panther? yes/no:")
    if jungle.lower().strip() == "yes":
        print (f"\nYou pull the shiny yellow coin from your pocket and give it to the panther. The panther accepts the coin and walks away. Your friend sees you and climbs down the tree. '{name}! You found me! Let's get off this island!' You, Potato and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")
    if jungle.lower().strip() == "no":
        print ("\nYou do not have the shiny yellow coin. The panther lunges at you and you dodge out of the way. You strike at it and send it flying through the bushes. You get 30 health points for fighting the panther. You run towards the tree and yell to your friend to climb down. You, Potato and your friend run away through the jungle. You can see the beach from a distance and know that you are close to making it back to the boat.")
        health0 = (int(30))
        print(f"Health =  {int(health1) + int(health0)}")
        print ("Inventory is empty")
        health0 = (int(health1) + int(health0))

end = input (f"\nYou, Potato, and your friend have made it back to the beach! The problem is you are very far from where your boat washed up. You hear a squawk and turn your head to see a giant nest with beautiful white birds. '{name}, we should catch a ride on those birds. They can take us back to your boat.' The birds can either give you a ride on their backs (D) or carry you in their talons (M). What do you choose?")
if end.upper().strip() == "D":
        print ("\nYou, Potato, and your friend walk over to the birds and hide behind a bush. When the birds have their backs turned towards the three of you, you run and jump onto them. The birds soar into the air and you grab onto their necks to keep from falling. You can see the entire island from this high up! As you get closer to your boat, you can see it is still where you left it. You wave to your friend and Potato who jumped onto their own birds. The birds land on the ground in front of your boat and you jump off, running towards it. You and your friend push the boat into the water and sail away from the island. This journey of yours was an experience none of you will forget.")
        print ("\nYour journey has ended")
if end.upper().strip() == "M":
        print ("\nYou, Potato, and your friend run over to the birds. They flap their wings, lift into the air, and grab you in their huge talons. You can see the entire island from this high up! As you get closer to your boat, you can see it is still where you left it. You call to your friend and Potato to drop into the water as the birds start to descend. You plunge into the water and swim towards the sand. When the three of you have made it to shore, you and your friend push the boat into the water and sail away from the island. This journey of yours was an experience none of you will forget.")
        print ("\nYour journey has ended.")
