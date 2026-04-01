print("You just stole a super car and the cops are after you escape at all costs")
print("\nYou see flashing lights behind you...")
print("The cops are chasing you!\n")

print("Where do you go?")
print("1. Highway")
print("2. Downtown")
choice1 = input("\nEnter 1 or 2: ")

# ================= HIGHWAY =================
if choice1 == "1":
    print("\n--- HIGHWAY ESCAPE ---")
    print("Do you:")
    print("1. Go WITH traffic")
    print("2. Go AGAINST traffic")
    choice2 = input("Choose 1 or 2: ")

    # ---- AGAINST TRAFFIC ----
    if choice2 == "2":
        print("\nYou drive against traffic!")
        print("A truck is coming straight at you!")
        print("1. Swerve LEFT")
        print("2. Swerve RIGHT")
        choice3 = input("Choose: ")
        if choice3 == "1":
            print("\nYou barely avoid the truck and survive!")
            print("1. Turn into a field")
            print("2. Stay on the road")
            choice4 = input("Choose: ")
            if choice4 == "1":
                print("\nYou disappear into the field")
                print("The cop wasnt excpecting that catching him off gaurd alowing you to escape with the super car>")
            elif choice4 == "2":
                print("\nRoadblock ahead!")
                print("BUSTED!")
            else:
                print("You hesitated and got caught better luck next time...")
        elif choice3 == "2":
            print("\nYou swerve right...")
            print("You crash into the truck. CAUGHT!")
        else:
            print("You hesitated and got caught better luck next time...")

    # ---- WITH TRAFFIC ----
    elif choice2 == "1":
        print("\nYou stay with traffic.")
        print("1. Swerve through cars")
        print("2. Stay in left lane and go fast")
        choice3 = input("Choose: ")
        print("\nYou make it ahead of the cops...")
        print("1. Pull into a gas station")
        print("2. Keep driving")
        choice4 = input("Choose: ")
        if choice4 == "1":
            print("\nAt the gas station:")
            print("1. Steal another car")
            print("2. Refuel")
            choice5 = input("Choose: ")
            if choice5 == "1":
                print("\nYou switch cars...")
                print("Nobody excpected you to do that especially not the cops you escaped good job you escaped.")
            elif choice5 == "2":
                print("\nYou take too long...")
                print("It took to long, the cops sorounded you and busted youy better luck next time.")
            else:
                print("You hesitated and got caught better luck next time...")
        elif choice4 == "2":
            print("\nYou stay on the road...")
            print("You started to run out of fule so to save gas you slow down problem is the cops caught up to you fule up next time")
        else:
            print("You hesitated and got caught better luck next time...")
    else:
        print("You hesitated and got caught better luck next time...")

# ================= DOWNTOWN =================
elif choice1 == "2":
    print("\n--- DOWNTOWN ESCAPE ---")
    print("Do you:")
    print("1. Take MAIN ROADS")
    print("2. Take BACK ALLEYS")
    choice2 = input("Choose 1 or 2: ")

    # ---- MAIN ROADS ----
    if choice2 == "1":
        print("\nYou speed through main roads.")
        print("1. Drive fast and outrun")
        print("2. Turn into a parking lot")
        choice3 = input("Choose: ")
        if choice3 == "1":
            print("\nYou push your car to the limit.")
            print("Too many cops ahead, they blocked off your only way out. BUSTED!")
        elif choice3 == "2":
            print("\nYou enter a parking lot.")
            print("1. Hide the car")
            print("2. Drive straight through")
            choice4 = input("Choose: ")
            if choice4 == "1":
                print("\nYou hide between cars...")
                print("Security spots you, they block you off and cops soround catching you red handed.")
            elif choice4 == "2":
                print("\nYou exit out the other side.")
                print("You lose the cops. YOU ESCAPED!")
            else:
                print("You hesitated and got caught better luck next time...")
        else:
            print("You hesitated and got caught better luck next time...")

    # ---- BACK ALLEYS ----
    elif choice2 == "2":
        print("\nYou take narrow back alleys.")
        print("1. Go deeper into alleys")
        print("2. Cut through a small street")
        choice3 = input("Choose: ")
        if choice3 == "1":
            print("\nThe alley gets tighter...")
            print("Dead end you have nowhere to go. CAUGHT!")
        elif choice3 == "2":
            print("\nYou cut through and confuse the cops ")
            print("YOU ESCAPED!")
        else:
            print("You hesitated and got caught better luck next time...")
    else:
        print("You hesitated and got caught better luck next time...")
else:
    print("You hesitated and got caught better luck next time...")
