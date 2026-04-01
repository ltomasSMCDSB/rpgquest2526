#Game Name: Mystic Gardens

answer = input("Would you like to start? (yes/no): ").lower().strip()

if answer == "yes":
    print("Loading...")
    input()
    print("Just one minute...")

elif answer == "no":
    print("Logging off...")
    input("")
    print("Goodbye.")
    exit()

else:
    print("Invalid input.")
    exit()

input()
#Decorative Loading Screen
character1 = "☆"
character2 = "❀"
word = "Mystic Gardens"
print(character1 * 18)
print(f"☆ {word:^13} ❀")
print(character2 * 18)

input("")
name = input("Please enter your name : ")
age = int(input("Enter your age: "))

if age >= 10:
    print("Verifying name and age...")
else:
    print("Invalid Age.")
    exit()

input("")
print(f"Hello {name[0].upper() + name[1:].lower()}! Welcome to Mystic Gardens.")
input("")

#Starting

gameplay=input("Gameplay starting... would you like to proceed? (yes/no): ").lower().strip()

if gameplay == "yes":
    print("...")
    input("")
    print("You are currently situated in a town called Lavendria.")
    input("")
    print("Your dream is to help people someday with medicine, so you've come here to seek for opportunities to learn.")

elif gameplay == "no":
    print("...")
    print("You've been logged off .✦ ݁˖")
    exit()

else:
    print("Invalid input.")
    exit()

input("")
print("You notice that at the edge of the town there seems to be a huge garden with big trees, many flowers and grasses.")
input("")
input("Out of curiousity you begin to walk towards the garden...")
input("...")
input("You find yourself in the garden.")
input("...")
input("crakle... crakle..")
input("")
print("As you're walking through the garden, you hear strange sounds.")
input("")
print(f"{name[0].upper() + name[1:].lower()}: Is anyone there??")
input("")
print("???: Oh sorry, didn't see you there.")
input("")
print("Greg: My name's Greg, and this is my garden of 55 years.")
input("")
print("Greg: Nice to meet you.")
input("")
print(f"{name[0].upper() + name[1:].lower()}: Oh, hello Greg, my name is {name[0].upper() + name[1:].lower()}. Nice to meet you too.")
input("")
print("...")
input("")
print("You assume that since Greg is quite old and has owned this impressive garden for so long, he must know something about plants and herbs.")
input("")
print(f"{name[0].upper() + name[1:].lower()}: Do you by any chance know anything about herbal medicine? I've travelled to Lavendria to learn about the town's traditional medicine.")
input("")
print("Greg: Oh, yes I do..! I was once an apothecary back in my olden days.")
input("")
print("Your assumption was correct.")
input("")
print("Greg: Consider this... would you like to become an apothecary in training?")
input("")
print("It's a great opportunity to learn about our ancient herbal medicines.")


answer = input("(Type 'yes'): ").lower().strip()

if answer == "yes" :
    input("")
    print("★★★ You are offically an apothecary in training. ★★★")
    input("")
    print("Greg: Your mission is to find the herbs chamomile, peppermint, lavender, and lemon balm before the day ends.")
    input("")
    print("Greg: Search for the herbs in the bountiful Mystic Gardens.")
    input("")
    print("Greg: All items will be added to your inventory and we'll use the herbs to create a tea for medicinal purposes later.")
    input("")
    print("Greg: Finding the useful herbs that I listed will increase the effectiveness of the final medicine by 1 each time.")
    input("")
    print("Greg: Avoid poisonous flowers such as lily of the valley, nightshade, and foxglove.")
    input("")
    print("Greg: You have 3 hearts and your medicine's effectiveness is 0 as you haven't found any herbs yet.")
    input("")
    print("Greg: Less fortunate outcomes will decrease your hearts by 1 each time during the game.")
    input("")
    print("FINAL CONDITIONS: If you lose all 3 hearts, you fail. Your medicine must also have an effectiveness of at least 2 by the end of the game.")
    input("")
    print("Goodluck.")
    input("")
    print("⋆✴︎˚｡⋆ ⊹₊")

else :
    print("Invalid answer.")
    input("")
    print("Game Over.")
    input("")
    print("⋆✴︎˚｡⋆ ⊹₊")


#Part_2
input("")
print("You are now ready to start your training.")
input("")
print("You begin to search the garden...")
input("")
print("...You approach two plants within the garden that may contain useful ingredients.")
input("")
print("Pick a plant to search.")

hearts = 3
effectiveness = 0

choice = int(input("Enter your choice (1, 2): ").strip())

if choice == 1:
    print("...")
    print("You've found chamomile! ❀ Good job.")
    input("")
    print("You gain a effectiveness point for finding a herb that can make the medicine stronger.")
    effectiveness += 1
    print(f"Medicine effectiveness: {effectiveness} ✦")
    print(f"Hearts remaining: {hearts} ♥")

elif choice == 2:
    print("...")
    input("")
    print("Uh-oh, this is foxglove (a poisonous plant).")
    input("")
    print("You lose a heart because you failed to find the right herb.")
    input("")
    print(f"Medicine effectiveness: {effectiveness} ✦")
    hearts -= 1
    print(f"Hearts remaining: {hearts} ♥")

else:
    print("Invalid input.")

if hearts <= 0:
    print("You do not have enough hearts to proceed.")
    input("")
    print("Game Over.")
    input("")
    print("⋆✴︎˚｡⋆ ⊹₊")
    exit()

#Part_3
input("")
print("Greg: Next, for the lavender, I would like to request for a special type called 'rainbow lavender'.")
input("")
print("Greg: It's exculsively grown in my greenhouse, but unfornately I've lost the keys for the greenhouse in one of the nearby coffee shops.")
input("")
print("Greg: You need to find the keys to my greenhouse to obtain the rainbow lavender.")
input("")
print("You search Lavendria and examine two cafes.")
input("")
print("There are only two cafes in Lavendria, so it must be here somewhere...")
input("")

try:
    cafe = int(input("Pick a cafe to search (1, 2): ").strip())

    if cafe == 1:
        print("...")
        input("")
        print("There are no keys.")
        input("")
        print("You cannot open the greenhouse and obtain the rainbow lavender.")
        input("")
        print("You lose heart because of your inability to find rainbow lavender.")
        input("")
        hearts -= 1
        print(f"Medicine effectiveness: {effectiveness} ✦")
        print(f"Hearts remaining: {hearts} ♥")

    elif cafe == 2:
        print("...")
        print("You've found the greenhouse keys! Good job.")
        input("")
        print("You use the keys to open the greenhouse and obtain the rainbow lavender. 🌈🪻")
        input("")
        print("You gain an effectiveness point for finding a herb that can make the medicine stronger.")

        hearts = hearts
        effectiveness += 1
        print(f"Medicine effectiveness: {effectiveness} ✦")
        print(f"Hearts remaining: {hearts} ♥")

except:
    print("Invalid input.")

if hearts <= 0:
    print("You do not have enough hearts to proceed.")
    input("")
    print("Game Over.")
    input("")
    print("⋆✴︎˚｡⋆ ⊹₊")
    exit()

#Part_4
input("")
print("You continue to search the Mystic Gardens...")
input("")
print("You find two plants that may contain useful herbs.")
input("")

try:
    choosing = int(input("Choose a plant (1, 2): ").strip())

    if choosing == 2:
        print("...")
        input("")
        print("You've found peppermint! Good job.")
        input("")
        print("You gain an effectiveness point for finding a herb that can make the medicine stronger.")

        effectiveness += 1
        print(f"Medicine effectiveness: {effectiveness} ✦")
        print(f"Hearts: {hearts} ♥")


    elif choosing == 1:
        print("...")
        input("")
        print("Uh-oh, this is nightshade.")
        input("")
        print("You lose a heart because you've failed to find the right herb.")

        hearts -= 1
        print(f"Medicine effectiveness: {effectiveness} ✦")
        print(f"Hearts: {hearts} ♥")

except:
    print("Invalid input.")

if hearts <= 0:
    print("You do not have enough hearts to proceed")
    input("")
    print("Game over.")
    input("")
    print("⋆✴︎˚｡⋆ ⊹₊")
    exit()

#Part_5
input("")
print("You find another two plants that may contain useful herbs.")
input("")

try:
    plant = int(input("Choose a plant (1, 2): ").strip())

    if plant == 1:
        print("...")
        print("You've found lemon balm! Good job.")
        input("")

        effectiveness += 1
        print(f"Medicine effectiveness: {effectiveness} ✦")
        print(f"Hearts : {hearts} ♥")

        input("")
        print("This was your last opportunity to find herbs today.")
        input("")
        print("Submit all herbs to Greg.")
        input("")

    elif plant == 2:
        print("...")
        input("")
        print("Uh-oh, this is lily of the valley.")
        input("")
        print("You lose a heart because you've failed to find the right herb.")
        input("")

        print(f"Medicine effectiveness: {effectiveness} ✦")
        hearts -= 1
        print(f"Hearts: {hearts} ♥")

        input("")
        print("This was your last opportunity to find herbs today.")
        input("")
        print("Submit all herbs to Greg.")
        input("")


except:
    print("Invalid input.")


#Part_6
if effectiveness > 0:
    print(f"{name[0].upper() + name[1:].lower()}: Greg! I've found everything that I was able to find. Take a look.")
    input("")
    print("Greg examines what you've found...")
    input("")
    print("...")

if effectiveness < 2 or hearts <= 0:
    if effectiveness < 2:
        print("-You fail your training because your medicine will not be strong enough.")
        input("")
        print("You cannot make the medicine.")
    if hearts <= 0:
        input("")
        print("-You fail your training because you have no hearts.")
        input("")
        print("You cannot proceed.")

    input("")
    print("Game Over.")
    input("")
    print("Thanks for playing.")
    input("⋆✴︎˚｡⋆ ⊹₊")
    exit()

elif effectiveness > 2 :
    print("You can create a medicine.")

elif effectiveness == 2 :
    print("Greg: I'll just add an additional ingredient to make it stronger.")
    input("")
    print("Greg adds an additional ingredient...")

    input("")
    print("...")
    input("")
    print("You and Greg set up the herbs to brew them.")
    input("")
    print("Brewing tea...")
    input("")
    print("...")
    input("")
    print("You've successfully brewed a tea that has strong medicinal purposes.")
    input("")
    print("Greg: Congratulations!! You are now an official apothecary.")
    input("")
    print("This is the end of the game. Thanks for playing.")
    input("")
    input("⋆✴︎˚｡⋆ ⊹₊")
