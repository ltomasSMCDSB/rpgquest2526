#Name of game: The Forest of Monsters
print("Welcome to the game: \n The Forest of Monsters")

print(" \n WHILE PLAYING: You must ONLY enter yes or no on questions, unless asked for a different answer.")
print(" \n You are in a dark forest. The twisting trees block out the light from the moon and make the night seem darker, and you are not able to see a clear path out. You are not sure how you got here, but you know you must escape the forest before something else inside it traps you there forever. There are strange noises echoing far off in the distance, but sometimes they sound closer. You are carrying a bag, but you lost the items that were inside it a while ago when you were running." )
print("Health Points = 100")
print("Inventory = Empty")
health = (int(100))
Inventory = ("Empty")
nameofplayer = input("Enter a name: ")


#first question (yes answer)
answer = input(" \n You hear something hit the tree behind you. Do you turn around and investigate? (yes/no)")
#first yes or no
if answer.lower().strip() == "yes":
    bonenecklace = input(" \n You walk over to the tree and see a bone necklace. Do you put it on? (yes/no)")
    if bonenecklace.lower().strip() == "yes":
         print(" \n You put the bone necklace on and gain the power of invisibility. You decide not to use it right away, and that you will save it for when you need it the most. You also gain 10 health points. Magical Bone Necklace has now been added to your inventory.")
         print(f"Health Points = {int(health) + 10}")
         newhealth1 = (int(health) + 10)
         newinventory1 = ("Magical Bone Necklace")
         print(f"Inventory: {newinventory1}")
    if bonenecklace.lower().strip() == "no":
         print(" \n You do not put on the necklace. Instead you take the string from it and put it in your pocket. String has been added to your inventory.")
         newhealth1 = (int(health))
         print(f"Health Points = {newhealth1}")
         newinventory1 = ("String")
         print(f"Inventory: {newinventory1}")


    #second question in first group
    flashlight = input(" \n You continue walking until you see something big run in front of you. It's too dark to see what it was. You have a flashlight in your pocket. Do you take it out to look? (yes/no)")
    if flashlight.lower().strip() == "yes":
        print(" \n You click the flashlight on and its circle of light catches on a pair of feet in front of you. You move the flashlight upwards and see that a monster is moving around a few feet from you. You freeze at the sight of it, but the the monster sees you and breaks the flashlight. You run away in the opposite direction until you find an even bigger monster blocking your path. You lose 10 health points. Broken flashlight has been added to your inventory.")
        newhealth2 = (int(10))
        finalnewhealth3 = (int(newhealth1) - int(newhealth2))
        print(f"Health Points = {int(newhealth1) - int(newhealth2)}")
        newinventory2 = ("Broken Flashlight")
        print(f"Inventory: {newinventory1}, {newinventory2}")
    if flashlight.lower().strip() == "no":
         print(" \n You keep the flashlight off and walk to the right. You follow a dirt path until you find a tree in the middle of it. The tree has a hole in it and you find a map inside. It shows you that you are almost out of the forest, but that something big lies ahead on the trail. The map has been added to your inventory and you gain 15 health points.")
         newhealth2 = (int(15))
         finalnewhealth3 = (int(newhealth1) + int(newhealth2))
         print(f"Health Points = {int(newhealth1) + int(newhealth2)}")
         newinventory2 = ("Map")
         print(f"Inventory: {newinventory1}, {newinventory2}")

#first question (no answer)
if answer.lower().strip() == "no":
    box = input(" \n You walk straight ahead until you come across a large wooden box. Do you open it? (yes/no)")
#first yes or no
    if box.lower().strip() == "yes":
            print(" \n You open the box and a monster jumps out. Underneath it is a sword. You pick it up but accidentally cut yourself. You lose 10 health points. The sword is added to your inventory.")
            print(f"Health Points = {int(health) - 10}")
            newhealth1 = (int(health) - 10)
            newinventory1 = ("Sword")
            print(f"Inventory: {newinventory1}")
    if box.lower().strip() == "no":
            print(" \n You look behind the box and find a pair of night vision goggles and put them on. You gain 5 health points for finding the goggles. Night vision goggles is added to your inventory.")
            print(f"Health Points = {int(health) + 5}")
            newhealth1 = (int(health) + 5)
            newinventory1 = ("Night Vision Goggles")
            print(f"Inventory: {newinventory1}")
            number = input("Choose an integer: ")
            try:
                 print(f"Your Night Vision Goggles double your vision, allowing you to see {int(number) * int(2)} feet in front of you in the dark.")
            except:
                 print(f"Your Night Vision Goggles allow you to see {number} feet in front of you in the dark.")



    #second question in second group
    follow = input(f" \n You continue walking and use your tools to help you along the way. You avoid any monsters you see by hiding behind trees. You see light coming through the trees a distance away, and decide that must be the end of the forest. You hear a voice behind you and turn around to find another person standing there. They tell you: '{nameofplayer}, I have seen the way out of this forest. If you follow me then I can show you the way.' You have not come across anyone else during your time in the forest, so you find it odd that they know your name. Do you follow them? (yes/no)")
    if follow.lower().strip() == "yes":
         print(" \n You decide that you could use the extra help to get out of the forest, so you follow the stranger. You pick up rocks and put them into your bag to use when needed. You look behind you at the sound of a branch snapping, then forward again to find a huge monster standing where the stranger just was. They tricked you. You lose 15 health points.")
         newhealth2 = (int(15))
         finalnewhealth3 = (int(newhealth1) - int(newhealth2))
         print(f"Health Points = {int(newhealth1) - int(newhealth2)}")
         newinventory2 = ("Large Rocks")
         print(f"Inventory: {newinventory1}, {newinventory2}")
    if follow.lower().strip() == "no":
        print(" \n You decide that you do not need the extra help and you don't fully trust the stranger. You walk away quickly and continue to follow the light. You collect a handful of rocks you find in the mud. You climb up a steep muddy hill but stop at the top. There is a huge monster guarding the exit.")
        newinventory2 = ("Small Rocks")
        print(f"Inventory: {newinventory1}, {newinventory2}")
        print(f"Health Points = {int(newhealth1)}")
        finalnewhealth3 = (int(newhealth1))

#final question (ending of game)
print(" \n You have almost made it to the end of the forest, but you have not yet escaped the monsters inside it. The massive monster turns its head to look at you. You can see that it has large claws and sharp teeth. It's small black eyes seem to sink into it's head as it focuses on you. It towers over you, and you fear that you will not be able to escape. Then you remember that you have gained tools along your journey that can help you. You look inside your bag to see what you have.")
print(f"Inventory: {newinventory1}, {newinventory2}")
final = input("Do you have the Sword or the Magical Bone Necklace? (yes/no)")
finalhealth = int(finalnewhealth3)
print(f"Health Points= {finalnewhealth3}")
finalhealth2 = input("Are your Health Points above 90? (yes/no)")
if final.lower().strip() == "yes" and finalhealth2 == "yes":
    print(f" \n You use the {newinventory1} to fight the monster. It stands no chance against you, and you are able to defeat it using your tool. You run the last few steps out of the forest and are finally free.")
    print("End of Game")
    print(f"Thanks for playing, {nameofplayer}")
else:
    # final.lower().strip() or finalhealth2 == "no":
    print(f" \n You use your {newinventory1} and {newinventory2} that you have collected to avoid the monster. You can't risk fighting the monster without the right tools or enough health. You are able to get out by running around it, but you know that next time you enter the forest you might not be so lucky.")
    print("End of Game")
    print(f"Thanks for playing, {nameofplayer}")
