#Game Name: Orphanage Simulator
status = "active"
equipement = "toy"
print("\n⁺‧₊˚ ཐི⋆♱⋆ཋྀ ˚₊‧⁺")
print("Year of Our Lord: 1331\nPlace: Monastery Orphanage")
print("\nThou art an orphan. Thou art 11 years of age. Thy friend Amis doth depart the orphanage, bound for an apprenticeship!\nShe taketh her leave at the dawn to wait by the main gate, thou dost perceive her beloved toy left behind.\nThou art compelled to sneak forth and return it to her.")
print("\nThou shall know, Sister Royse is kind and maybe shall aid thee,\nbut beware Sister Jane, lest thou befall the task of cleaning horse dung...a fate thou wouldst surely wish to avoid!")
print("\nForget not, thou must also find a snack for Tommy, the orphan who doth watch o'er the main gate or present him a key to the\ngate.")
print("\nThou shall enter the precise spelling of the words presented and not write numbers with letters to proceed.")
print("\n\tThou depart from the general bedroom, walking through a darkened hall. \n\tThe sound doth reach thee that the chapel Mass is near its end.")
choice = input("⚬ Now thou art faced with choice: go through the library or the cookhouse? (library/cookhouse): ").strip().lower()
print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
#LIBRARY/COOKHOUSE ARC
if choice == "cookhouse":
    print("𓎩 Thou entered the cookhouse through the back door.\nThou dost espy a bowl overflowing with biscuits, so numerous that a single one would go unnoticed...𔓐\nTommy dothe crave biscuits and thou requirest passage,\nyet as thou seizest a biscuit, a spoon of metal doth tumble and clang.\nThou perceivest a shadow near the front door of the coookhouse.")
    react = input("\n⚬ Dost thou flee or seek concealement? (flee/conceal): ").strip().lower()
    print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
    if react == "flee":
        print("Upon thy swift departure through the front door of the cookhouse, a nun doth appear startling thee\nyet 'tis Sister Royse. She, who claimed a passage to the library, heard a sound and inquires thy presence.\nHer gaze falls upon Amis' toy and the biscuit, questioning thine intend. Thou confessed.\nWhereupon, she doth escort thee to the final hall by the entryway and \ngifting thee a key to the gate 🗝, caustions thee against tardiness for breakfast, thence takes her leave.")
        equipement = "biscuit" + "key"
    elif react == "conceal":
        print("Sister Mary doth enter through the front door of the cookhouse and by fortune observeth naught amiss.\nShe then departs through front, whereat thou hearest her converse with Sister Royse, and thereafter take her leave.")
        next = input("\n⚬ Dost thou desire to greet Sister Royse or wait until she hath passed and then make thine own exit? (greet/wait): ").strip().lower()
        print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
        if next == "greet":
            equipement = "biscuit" + "key"
            print("Thou depart thine concealement and greet Sister Royse, who claimed a passage to the library, \nyet heard a sound and inquires thy presence.\nHer gaze falls upon Amis' toy and the biscuit as she quesions thine intend. Thou confessed.\nWhereupon, she doth escort thee to the final hall by the entryway and \ngifting thee a key to the gate 🗝, caustions thee against tardiness for breakfast, then takes her leave.")
        elif next == "wait":
            equipement = "biscuit"
            print("After a moment thou dost emerge and stealthy creep through the hall. \nThou art seized upon hearing the voice of Sister Jane, yet by grace she passes thee by. \nNow thou art in the final hall by the entryway.")
        else:
             print("\nThou shalt make thy selection from amongst the presented options.")
             status = "fail"
    else:
        print("\nThou shalt make thy selection from amongst the presented options.")
        status = "fail"
elif choice == "library":
    print("🕮 Thou dost enter through the back door and behold slender rows brimming with tomes, as thou find thine way betwix them.\nThen thou hearest a soul enter through the front door of the library.")
    react2 = input("\n⚬ Dost thou ascend a ladder to espy the newcomer, or conseal thyself behind a shelf? (espy/conceal): ").strip().lower()
    print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
    if react2 == "espy":
        equipement = "key"
        print("As thou ascend, thou espy Sister Royse bearing a Holy Bible. \nCease thy creeping and offer a wave, to which she responds with bewilderment. \nThou dost approach her and ufold thy scheme, whereupon she doth grant thee a key to the main gate 🗝,\nbidding thee to not tarry past the hour of breakfast. \nThere she dost guide thee through the halls, unto the last one before the front door, then leaves thee there.")
    elif react2 == "conceal":
        print("A figure enters whom thou fail to recognise, placing a weighty tome upon a shelf and thence exiting through the back door.\nThou emergist from the library through the front door only to be espied by Sister Mary as she doth traverse the hall.\nAlas, fight is futile: She doth chide thee and commmand thy return to the general bedroom, escort thee there. ")
        status = "fail"
        print("\nThy plans have come to naught!")
    else:
        print("\nThou shalt make thy selection from amongst the presented options.")
        status = "fail"
else:
     print("\nThou shalt make thy selection from amongst the presented options.")
     status = "fail"
if not status == "fail": #MADELEINE ARC
    print("\nThou art now within the hall and still doth reach thine ears a song, like unto Madeleine, one of the orphans that doth learn \nsinging from Sister Jane. ♬⋆.˚ \nLo, she doth approach thee, yet thou canst not flee down the hall, for Sister Jane's voice doth echo thence. \nThou art compelled to parley with Madeleine, who treatens to inform Sister Jane. \nThou, desiring to avoid this, inquirest what offering would stay her tongue.")
    if "biscuit" in equipement: #you went to cookhouse
        print("She doth desire thine biscuit.")
        decision = input("\n⚬ Thou mayest relinquish the biscuit or attempt to flee through the entryway (relinquish/flee): ").strip().lower()
        print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
        if decision == "relinquish":
            print("She doth smile and trips onwards with a merry tune upon her lips as she nimples the biscuit. \nThou dost venture forth, exiting the building throught the entryway.")
            if "key" in equipement:
                equipement = "key"  #you went to cookhouse, got a key, so no need for apple, gave up biscuit, don't need anything
            else:
                equipement = "missing_snack" #you went to cookhouse, didn't get a key, missing a snack, gave up biscuit, need 1 apple for T
        elif decision == "flee":
            print("Thou sprinest hence, whilst she seeks Sister Jane, who comes near and doth chide thee firecely.")
            if "key" in equipement:
                print("Fortunately, Sister Royse doth appear and bidding Sister Jane to hold her wrath, tells for 'twas she who bade thee to the \nmain gate, \nThou smilest and walkest free out the entryway.")
                equipement = "key" + "biscuit" # went to cookhouse, got a biscuit, got a key, don't need to get anything
            elif not "key" in equipement:
                print("Thou art led to the general bedroom, shamed before all, and must cleanse the stables... A dire fate!")
                status = "fail"
                print("Thy plans have come to naught!")
            else:
                print("\nThou shalt make thy selection from amongst the presented options.")
        else:
            print("\nThou shalt make thy selection from amongst the presented options.")
            status = "fail"
    elif not "biscuit" in equipement: #you came from library
        print("She doth desire an apple from the garden. ")
        decision = input("⚬ Thou mayest agree to seek the apple, or attempt to flee through the entryway. (agree/flee): ").strip().lower()
        print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
        if decision == "agree":
            print("Madeleine doth smile and trips onwards with a merry tune upon her lips. \nThou dost venture forth, exiting the building through the entryway.")
            equipement = "key" + "obligation" #you went to library, got key, gotta get M's apple
        elif decision == "flee":
            print("Thou sprinest hence, whilst she seeks Sister Jane, who comes near and doth chide thee firecely")
            if "key" in equipement:
                equipement = "key"  #got a key, so no need for T's and fled so no M's apple, go to gate
                print("Fortunately, Sister Royse doth appear and bidding Sister Jane to hold her wrath, tells for 'twas she who bade thee to the main gate, \nThou smilest and walkest free out the entryway!")
            elif not "key" in equipement:
                print("Thou art led to the general bedroom, shamed before all, and must cleanse the stables... A dire fate!")
                status = "fail"
                print("Thy plans have come to naught!")
        else:
            print("\nThou shalt make thy selection from amongst the presented options.")
            status = "fail"
if not status == "fail": #GARDEN ARC
    print("\nNow thou art beyond the threshold.")
#at this point you either have (key, obligation), (key), (missing_snack), (key, biscuit)
    if equipement == "key" or "biscuit" in equipement:
        status = "pass"
    elif "obligation" in equipement:
        print("Thou art now bound to bringeth Madeleine an apple, so thou walkest to the garden, 𖡼.𖤣𖥧𖡼.𖤣𖥧 \nwhere divers trees and berry bushes flourish, alongside planted vegetables and greens. \nAs thou takest an apple, Sister Agnes doth appear, declaring that thou art forbidden to take apples without leave. \nYet she offers her consent, shouldst thou lend her aid. \nBut thou art troubled, wondering if Amis yet remains and whether thou shouldst tarry any longer. ")
    elif "missing_snack" in equipement:
        print("For thou dost yet need snack for Tommy to pass, and thou art bound to bringeth Madeleine an apple, thou walkest to the garden, 𖡼.𖤣𖥧𖡼.𖤣𖥧 \nwhere divers trees and berry bushes flourish, alongside planted vegetables and greens. \nAs thou takest two apples, Sister Agnes doth appear, declaring that thou art forbidden to take apples without leave. \nYet she offers her consent, shouldst thou lend her aid. \nBut thou art troubled, wondering if Amis yet remains and whether thou shouldst tarry any longer. ")
if not status == "fail" and not status == "pass":
    garden_choice = input("\n⚬ Thou art to decide, aid her, or flee hence? (aid/flee): ").strip().lower()
    print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
    if garden_choice == "aid":
        print("\nShe doth impart that seeds have arrived at the main gate, which she intends to plant this very day. \nThus, she desires a soul to tread hence and deliver them unto her. \nThou dost smile and declare that thou shalt gladly undertake this task.")
        status = "seed_task"
    elif garden_choice == "flee":
        print("\nAs thou dost run, she doth chide thee and become frustrated, \nwhilst Sister Mary and Sister Jane take a stroll in the forecourt. \nThey apprehend thee and rebuke thee, escorting thee to the common chamber, verbally humbling thee. \nNow 'tis thy burden to cleanse after the steeds...")
        print("\nThy plans have come to naught!")
        status = "fail"
    else:
        print("\nThou shalt make thy selection from amongst the presented options.")
        status = "fail"
if not status == "fail":
    print("\nAs thou dost wend thy way towards the main gate, thou beholdest Sister Mary with Sister Jane upon their promenade. \nThey doth mark thee, drawing nigh, and withal, chide thee for thine absence from the general bedroom.")
    if status == "pass":
        print("Thou dost present unto them the key to the gate, which thou gladly possessest.\nSisters doth release thee.")
    elif status == "seed_task":
        print("Thou dost declare that Sister Agnes hath bid thee fetch seeds from the main gate.\nSisters doth release thee.")
if not status == "fail": #GATE ARC
    #so you meet Tommy and give an apple, if biscuit or missing-snack and show key if have key
    if "biscuit" in equipement:
        print("\nThou dost encounter Tommy, who sits upon a stool 'neath yonder tree by main gate. \nThou givest him a biscuit 𔓐, which doth bring him much joy, and he doth partake of it forthwith.")
    elif "missing_snack" in equipement:
        print("\nThou dost encounter Tommy, who sits upon a stool 'neath yonder tree by main gate. \nThou givest him an apple 𑣿, which doth bring him much joy, and he doth partake of it forthwith.")
    elif "key" in equipement:
        print("\nThou dost encounter Tommy, who sits upon a stool 'neath yonder tree by main gate.\nThou doth present him the key 🗝. He doth nod in assent.")
    print("But then, with a gaze most stern, he doth declare thath \nthou art bound to answer yet another question ere thou mayest pass.")
    try:
        age = int(input("⚬ He doth inquire: \"Of what age are thou?\" (*thou were told at the start): ").strip().replace(" ", ""))
        print("\n═════════════════════════════════════════════════════════════════════════════════════════════════════════")
    except:
        print("\nWrite ye a number, not in script.")
        status = "fail"
if not status == "fail":
    if age < 10:
        print("\"Thou art forbidden to pass through this gate if thy years be less than ten.\"")
        status = "fail"
    elif age > 17:
        print("\"At such an age thou told, thou art not meant to dwell within the confines of an orphanage.")
        status = "fail"
    elif 17 > age > 10:
        print("\n\"Hark, thou are free to pass!\"")
if not status == "fail":
    print("\nThe hour is upon thee; thou unlockest the gate, yet findest...none. \nHath she fled? A cart's rear doth vanish from thy sight. Disappointment grips thee, and sorrow, that Amis shall not \nhave her toy, despite thy trials.\n But hark! Tommy doth declare that Amis shall tarry another day at the orphanage... \nThis lifts thy spirits, for thy friend remains to play, and shall receive her toy. \nMoreover, thou art spared the chore of tending horses. Thou dost hasten back to the orphanage.")
    if status == "seed_task":
        print("Before leaving the gate, you ask Tommy for seeds, and on your way to monastery, bring them to Sister Agnes. 𓇢")
    if "obligation" in equipement:
        print("On your way to breakfast room, you find Madeleine, and give her that apple she wanted. 𑣿")
    print("𓌉◯𓇋 Entering the eatery, where children gather for their morning meal, thou embracest Amis, \nand grantest her the toy she feared lost. \n\nWell done! Thy task is complete!!\n-ˋˏ ༻❁༺ ˎˊ-")
