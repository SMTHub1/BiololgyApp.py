def biology_1984():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """1. The piercing and sucking mouth parts are found in
        A. grasshoppers
        B. mosquitoes
        C. termites
        D. cockroaches \n """,
        """2. The hormones that regulate plant growth are
        A. ethylene and auxins
        B. auxin and gibberellins
        C. cytokinin and abscisic acid
        D. ethylene and gibberellins  \n """,
        """3. Which of the following pair of organisms exhibit parasitic association?
        A. insect and plant
        B. cattle and egret
        C. shark and remora
        D. tsetse-fly and cattle \n """,
        """4. Which of the following group of animals can withstand the rigour of the arid land?
        A. locust, camel, lizard and snakes
        B. monkeys, chameleon, earthworm andgrasshopper
        C. monkeys, grasshopper, snail and snakes
        D. lungfish, duck, butterfly and lizards  \n """,
        """5. Suture joint is found in the 
        A. hip
        B. ankle 
        C. skull
        D. elbow  \n """,
        """6. The organelle responsible for osmoregulation in Paramecium is
        A. flame cell 
        B. nephridia
        C. contractile vacuole
        D. Malpighian tubule  \n """,
        """8. The platelets in mammalian blood are responsible for
        A. transporting oxygen
        B. initiating clotting
        C. removing carbon (IV) oxide
        D. destroying micro-organisms   \n """,
        """9. The most important factor that determines the different types of vegetation is
        A. light
        B. wind
        C. temperature
        D. rainfall  \n """,
        """10. When testing for the presence of starch in a leaf, the reason for dipping the decolourised leaf in hot water is to 
        A. detect the starch
        B. kill the leaf
        C. soften the leaf
        D. remove the chlorophyll  \n """,
        """11. The relationship between remora and shark can best be described as
        A. parasitism
        B. amensalism
        C. mutualism
        D. commensalism  \n """,
        """12. The major characteristic of a fresh water habitat is the possession of
        A. high turbidity 
        B. high density
        C. low salinity
        D. high current  \n """,
        """13. The causative organism of cholera is
        A. Clostridium sp
        B. shigella sp
        C. vibrio sp
        D. salmonella typhi  \n """,
        """14. The process that takes place in the dark stage of photosynthesis is
        A. oxidation of water 
        B. photolysis of water
        C. oxidation of carbon (IV) oxide
        D. reduction of carbon (IV) oxide  \n """,
        """15. Chlorofluorocarbons are air pollutants that originates from
        A. crude oil refining
        B. coal mining
        C. motor vehicle exhaust
        D. cooling system  \n """,
        """16. Which of the following is organ level of organisation?
        A. Volvox sp
        B. paramecium caudatum
        C. hydra viridis
        D. onion bulb  \n """,
        """17. The simplest form of reproduction is 
        A. conjugation
        B. budding
        C. spore formation
        D. binary fission  \n """,
        """18. Which of the following is a characteristic of wind-pollinated flower?
        A. flowers lack nectar 
        B. flowers are conspicuous
        C. flowers have perianths
        D. flowers are bisexual  \n """,
        """21. In an experiment to determine the humus in a soil sample the following results were obtained Mass of dish - 20g Mass of dry soil - 7.5g Mass of dish + soil after burning = 25g The percentage of humus in the given sample is
        A. 9.1
        B. 37.5
        C. 12.5
        D. 33.3  \n """,
        """22. The presence of termites and earthworms in soil promote
        A. porosity and fertility 
        B. porosity and aeration
        C. aeration and fertility
        D. acidity and aeration  \n """,
        """23. In a 15m2 habitat, the total number of Tridax counted using a 1.6m2 quadrant thrown randomly 50 times was 400. What is the Tridax
        A. 12 
        B. 16
        C. 8
        D. 5  \n """,
        """24. Which of the following is a sex-link character?
        A. Dwarfism 
        B. Albinism
        C. Tongue rolling
        D. Colour blindness  \n """,
        """25. The outer-most tissue of the herbaceous roots is the
        A. cuticle
        B. pericycle
        C. epidermis
        D. endodermis  \n """,
        """26. The respective tissues that transport water and manufactured food in plants are 
        A. xylem and phloem 
        B. phloem and tracheid
        C. phloem and xylem 
        D. xylem and tracheid  \n """,
        """27. An adaptive feature of plants in the savanna is
        A. fissured bark
        B. few grasses
        C. tall trees
        D. long lifespan  \n """,
        """28. A grasshopper's cuticle becomes green during the season and black after fire. The reasons for the change is ---
        A. obtain food
        B. predators
        C. secure mates
        D. escape detection  \n """,
        """29. Which of the following is the most advance plant?
        A. merchantia
        B. Dryopteris
        C. Chlamydomonas
        D. Spirogyra  \n """,
        """30. The soil type with the least ability to retain nutrients is
        A. sandy loam
        B. clay loam
        C. loam 
        D. sand  \n """,
        """31. A humming bird is able to feed on nectar because its beak is
        A. short, slender and ridged
        B. short, strong and conical
        C. long, slender and slightly curved
        D. long, wide and slightly curved  \n """,
        """33. The effect of overcrowding is
        A. immigration
        B. reduced competition
        C. emigration
        D. reduced mortality  \n """,
        """34. The vertebrae that allows the skull to nod and rotate are
        A. axis and cervical
        B. atlas and thoracis
        C. axis and atlas
        D. atlas and cervical  \n """,
        """35. The component of the cell that determines paternity resides in the
        A. centrosome 
        B. ribosome
        C. nucleus
        D. mitochondria  \n """,
        """38. The insect-trapping by the leaves of Venus flytrap is an example of a 
        A. adaptive coloration 
        B. structural adaptation 
        C. environmental adaptation 
        D. behaviour adaptation  \n """,
        """39. Morphological variation in humans include 
        A. height, skin, colour and tongue rolling
        B. weight, finger prints and body shape 
        C. height, weight and blood group 
        D. skin colour, weight and height  \n """,
        """40. Which of the following is correct about blood transfusion?
        A. Group AB can only receive from groups A and B and not from group O
        B. Group O can receive from groups A and B and from AB
        C. Group B can only donate to blood group B and not to AB and O
        D. Group O can donate to groups A, B and AB but cannot receive  \n """

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "D"),
    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1984()
    print("""
        you have biology , english , chemistry and physics
        for biology enter year 1980
        for English enter year 1981
        for Chemistry enter year 1982
        for Physics enter year 1983
        if you decide not to do again enter no""")
    year = input("enter your year")
    year = year.upper()
    if year == "1980":
        biology_1980()
    if year == "1981":
        English_1981()
    if year == "1982":
        Chemistry_1982()
    if year == "1983":
        Physics_1983()
    if year == "1984":
        biology_1984()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")
        print("bye for now")
    print("bye for now")
