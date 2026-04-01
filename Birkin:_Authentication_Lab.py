#Birkin: Authentication Lab

#controlled variables
game_on = True
expert_reputation = 100
evidence_list = []

#Background story
print("Hello player!\nYou are a Hermes Birkin handbag authenticator.\nYour task is to determine if your client's Birkin 30 in Togo leather is real or fake.\nWill you be able to identify flaws or lose your reputation?")

print("\nYou will have two state managements.\nExpert reputation decides if you made the right call when identifing the bag.\nEvidence list is the inventory of data and observations made.")

#room 1

price = input("\nEnter the cost price of the bag: $")

try :
    if int(price) <= 5000:
        print("Suspiciously Low. -40 expert reputation")
        expert_reputation = expert_reputation - 40
        if expert_reputation <= 0:
            print("You lose!")
            game_on = False

        else:
            print(f"Expert reputation is {expert_reputation}")
            game_on = True


    elif 10000 > int(price) > 5000:
        print("Low. -10 expert reputation")
        expert_reputation = expert_reputation - 10
        if expert_reputation <= 0:
            print("You lose!")
            game_on = False

        else:
            print(f"Expert reputation is {expert_reputation}")
            game_on = True

    elif 20000 >= int(price) >= 10000:
        print("Perfect price and matches current market value.\nProceed with no penalty.")
        game_on = True
    elif int(price) > 20000:
        print("Suspiciously High. -40 expert reputation")
        expert_reputation = expert_reputation - 40
        if expert_reputation <= 0:
            print("You lose!")
            game_on = False

        else:
            print(f"Expert reputation is {expert_reputation}")
            game_on = True
except:
    print("Invalid input. Please enter a whole number.")
    game_on = False

#room 2
if game_on == True:
    print("\nDoes the interior of the bag smell like chemicals or leather?")
    q2valid = False
    while q2valid == False:
        smell = input("Enter 'chemicals' or 'leather': ").lower().strip()
        if "chemicals" == smell:
            print("Ewww CHEMICALS! -20 expert reputation")
            expert_reputation = expert_reputation -20

            if expert_reputation <= 0:
                print("You lose!")
                game_on = False

            else:
                print(f"Expert reputation is {expert_reputation}")
                game_on = True
            q2valid = True
        elif "leather" == smell:
            print("Rich scent is added to evidence list.")
            evidence_list = evidence_list + ["Rich Leather Scent"]
            game_on = True
            q2valid = True
        else:
            print("Invalid input. Please enter 'chemicals' or leather'.")
            game_on = False

#room 3

if game_on == True:
    q3valid = False
    while q3valid == False:
        print("\nCheck the stitching of the bag")
        stich = input("Is the stitching straight? (Yes/No)").lower().strip()

        if stich == 'yes':
            print("Hermes bag's are stitched at 18 degrees. -30 expert reputation")
            expert_reputation = expert_reputation - 30

            if expert_reputation <= 0:
                print("You lose!")
                game_on = False

            else:
                print(f"Expert reputation is {expert_reputation}")
                game_on = True
                q3valid = True

        elif stich == 'no':
            print("Saddle stitch is added to evidence list.")
            evidence_list = evidence_list + ['Saddle Stich']
            game_on = True
            q3valid = True
        else:
            print("Invalid input. Please enter (Yes/No)")
            game_on = False


#room 4
if game_on == True:
    print("\nCheck the hardware of the bag.")
    hardware = input("Is it more than 2lb? (Yes/No)").lower().strip()

    if hardware == 'yes':
        zipper = input("Is the zipper parallel to the opening? (Yes/No)").lower().strip()
        if zipper == 'yes':
            print("Quality hardware is added to evidence list.")
            evidence_list = evidence_list + ["Quality Hardware"]
            game_on = True

        elif zipper =='no' :
            print("-30 expert reputation.")
            expert_reputation = expert_reputation - 30

            if expert_reputation <= 0:
                print("You lose!")
                game_on = False

            else:
                print(f"Expert reputation is {expert_reputation}")
                game_on = True


    elif hardware == 'no':
        print("-30 expert reputation.")
        expert_reputation = expert_reputation - 30

        if expert_reputation <= 0:
            print("You lose!")
            game_on = False

        else:
            print(f"Expert reputation is {expert_reputation}")
            game_on = True

    else:
        print("Invalid input. Please enter (Yes/No)")
        game_on = False

#room 5
if game_on == True:
    q5valid = False
    while q5valid == False:
        card = input("\nDoes it have a orange card? (Yes/No)").lower().strip()
        if card == 'yes':
            print("You lose!")
            expert_reputation = 0
            game_on = False
            q5valid = True

        elif card == 'no':
            print("Proceed with no penalty.")
            game_on = True
            q5valid = True

        else:
            print("Invalid input. Please enter (Yes/No)")
            game_on = False

#room 6
if game_on == True:

    if expert_reputation <= 50:
        print(f"Expert reputation is {expert_reputation}")
        print(f"Evidence list has {evidence_list}")
        print("\nYou lose! You will never recieve clients ever again.")
    elif expert_reputation > 50 and len(evidence_list) >= 3:
        print(f"\nExpert repututation is {expert_reputation}")
        print(f"Evidence list has {evidence_list}")
        print("You win! The Birkin is real.")
