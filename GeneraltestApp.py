from Question import Question
def biology_1980():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """" 1. A group of closely related organisms capable of interbreeding to produce fertile offspring are known as members of a
        A. kingdom 
        B. class
        C. family
        D. species \n""",
        """"
        2. A beaker of pond water containing few specimens of Euglena was placed in a dark room for two weeks. \n At the end of this period, the specimens of Euglena were still alive because they were
        A. able to carry out holozoic nutrition
        B. able to carry out photosynthesis using carbon dioxide in the pond water
        C. better adapted to life in darkness than to life in light
        D. not overcrowded \n """,
        """"
        3. The cytoplasm of the cell is considered a very important component because it
        A. regulates the amount of energy in thecell 
        B. suspends all cell organelles
        C. is the outermost part of the cell 
        D. is solely responsible for cell division \n""",
        """"
        4. Red blood cells were found to have burst open after being placed in distil for an hour. This phenomenon is known as
        A. plasmolysis 
        B. diffusion
        C. haemolysis
        D. wilting \n""",
        """"
        5. The curvature movement of plants in response to the stimulus of water is called
        A. hydrotropism
        B. geotropism
        C. Phototropism
        D. thigmotropism\n """,
        """
        6. The overall reaction in glycolysis can be summarised as
        A. C  6111205 --K31-1403 + 4H +ATP 
        B. C6H1206 ----- 2;11403+ 4H +2ATP 
        C. C61-1,206---.> 2;1-1403 + 4H+ ADP 
        D. C6F11206 2C31-1403+ 4h + 2ADP\n """,
        """"
        7. The longest bone in the body is the 
        A. humerous
        B. femur
        C. scapula
        D. tibia \n""",
        """"
        8. Which of the following structures is not a skeletal material?
        A. Chitin 
        B. Cartilage
        C. Bone
        D. Muscle\n """,
        """"
        9. The reason why the flow of blood through the capillaries is very slow is 
        A. because the walls of capillaries are very thin
        B. to avoid high — blood pressure 
        C. to ensure that the individual does not get dizzy
        D. to allow adequate time for exchange of materials \n""",
        """"
        10. Which of the following groups of organisms has kidney as their excretory organ?
        A. Fishes, amphibians, birds, man
        B. Fishes, amphibians, annelids, insects
        C. Fishes, reptiles, birds, tapeworms
        D. Fishes protozoans, amphibians, man \n """,
        """"
        11. Which of the following features is not a characteristic of arteries? Arteries
        A. possess values at internals throughout their length.
        B. have thick muscular and elastic walls
        C. carry blood away from the heart
        D. transport oxygenated blood with the exception of the pulmonary artery. \n """,
        """"
        12. The reason why hospitals use saline solutions as drip instead of water is
        A. because salt is a preservative
        B. to prevent contamination of the body 
        C. to maintain the composition of body fluids
        D. to increase the number of blood cells \n """,
        """"
        13. The part of the ear which contains nerve cells sensitive to sound vibrations is the
        A. cochlea
        B. ampulla
        C. tympanum
        D. malleus \n""",
        """"
        14. Spectacles with convex lenses correct long-sightedness by
        A. converging the Light rays before they enter the eye
        B. diverging the light rays before they enter the eye
        C. reducing light intensity before it enters the eye
        D. increasing light intensity before it enters the eye\n """,
        """"
        15. A seed of a flowering plant can best be described as 
        A. radicle and plumule
        B. the developed ovule
        C. the embryo and endosperm
        D. developed ovary \n""",
        """"
        16. Which of the following processes removes carbon from the atmosphere?
        A. Putrefaction 
        B. Photosynthesis 
        C. volcanic eruption
        D. Burning fuels\n """,
        """"
        17. Which of the following cycles involves the process of precipitation and transpiration?
        A. Water cycles
        B. Carbon cycle
        C. Nitrogen cycle
        D. oxygen cycle\n """,
        """"
        18. What is the critical limiting factor for plants below the photic zone in an aquatic ecosystem?
        A. Availability of nutrients
        B. Availability of water
        C. intensity of light
        D. Carbon dioxide concentration \n""",
        """"
        19. Which of the following instruments is used to estimate the number o, plants in a habitat? 
        A. Pooter
        B. Pitfall trap
        C. Quadrat
        D. Sweep net \n """,
        """"
        20. Which of the following statements is true about sandy soil? It
        A. has limited air space 
        B. is light and easy to dig
        C. drains slowly
        D. is heavy and poorly aerated \n """,
        """
        21. Which of the following organisms is primary consumer?
        A. Dog 
        B. Sheep
        C. Grass
        D. Fungus \n """,
        """
        22. Which of the following diseases is not hereditary?
        A. Albinism 
        B. Scabies
        C. Haemophilia
        D. Colour blindness \n """,
        """
        23. The immediate product of meiosis in flowering plants is the
        A. sporophyte 
        B. gametophyte
        C. zygote
        D. pollen grains \n """,
        """
        24. DNA in eukaryotic cells is contained in the
        A. central vacuole
        B. nucleus 
        C. lysosome
        D. golgi body \n """,
        """
        25. A man who is heterozygous for the disease haemophilia marries a womanwho is double recessive for haemophilia.\n What percentage of their offspring wouldhave the disease?
        A. 0%
        B. 25%
        C. 50%
        D. 75% \n """,
        """"
        26. Cytokinesis of mitosis is a process that ensures that
        A. each daughter cell gets the necessary organelle
        B. there is distribution of a complete set of genes into each daughter cell.
        C. daughter cells inherit new genetic combinations.
        D. worn out organelles are excluded from daughter cells \n """,
        """
        27. An animal which is active during the day is known as a
        A. nocturnal animal 
        B. diurnal animal
        C. terrestrial animal
        D. homoatomic animal \n """,
        """
        28. Evidence of evolution include the following except
        A. fossil records
        B. comparative anatomy
        C. mutation of genes
        D. geographical distribution of organisms \n """,
        """
        29. An accurate identification of a rapist can be carried out by it conducting a
        A. RNA analysis 
        B. DNA analysis
        C. blood group test  
        D. behavioural traits test\n """,
        """"
        30.A boy who is fond of swimming in a pond finds himself passing urine with traces of blood. He is likely to have contracted
        A. schistosomiasis
        B. onchocerciasis
        C. poliomyelitis
        D. salmonellosis \n """,
        """
        31.The flippers of a whale and the fins of a fish are examples of
        A. divergent evolution
        B. coevolution
        C. continuous variation
        D. convergent evolution"""

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "A"),
    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1980()
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

def English_1981():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
    """" 1. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence. \n23. When asked to state her side of the story, Bunmi started by beating about the bush. This means that Bunmi
    A. went straight to the point
    B. was lost in great thought
    C. followed a bush path
    D. approached the subject without coming to the point. \n""",
            """"
    2. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n24. The amount he donated was small. He said it was his widow's mite. This means that
    A. he was a widow
    B. he was misery.
    C. it was all he could honestly afford
    D. he could have given more. \n """,
            """"
    3. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n25. The friendship between Segun and Shehu has turned sour. This means that Segun and Shehu are
    A. no longer friends 
    B. stilt friends 
    C. better friends now  
    D. getting to understand each other. \n""",
            """"
    4. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n26. The driver smelled a rat when the policemen asked him to stop. This means that the driver was 
    A. reckless 
    B. suspicious 
    C. careful 
    D. offensive. \n""",
            """"
    5. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n27. The students were as advised to face their studies and let the sleeping dog lie. This means that the students should
    A. obey the authorities 
    B. suspicious 
    C. inexperienced
    D. uncivilised. \n """,
            """
    6. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n28. From the way Ngozi behaves, it is obvious she is a greenhorn. This means that Ngozi is
    A. arrogant
    B. cautious 
    C.inexperienced 
    D. uncivilised  \n """,
            """"
    7. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n29. The economic situation is so bad that many wage earners are hardly able to make both ends meet. This means that 
    A. people's income exceed their expenditure
    B. most people are extravagant with their income
    C. people's earnings are not sufficient for their essential needs
    D. most people engage in activities that bring them extra pay.  \n""",
            """"
    8. After each of the following sentences, a list of possible interpretations of the sentence is given.\n  Choose the interpretation that you consider appropriate for each sentence.  \n30. Since I found out his hypocritical nature, I have been keeping him at arm's length. This means that I
    A. avoid being similar with him
    B. ignore his advice
    C. report him to the authority
    D). stop visiting him. \n """,
            """"
    9. After each of the following sentences, a list of possible interpretations of the sentence is given.\n  Choose the interpretation that you consider appropriate for each sentence. \n 31. I knew Okoronkwo's father very well and I must say that his son is a chip off the old block. Thy means that Okoronkwo
    A. has Chosen the game career as its father
    B. is very much like his father
    C. is a I extremely different sort of person from his lather.
    D. has taken up a different profession from his father's.  \n""",
            """"
    10. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n33. Anyone who thinks that he can succeed in life without working hard is living in a fool's paradise. This means is that such a person
    A. be selfish
    B. underrate opponents
    C. be over-confident
    D. attempt to win cheap popularity. \n """,
            """"
    11. After each of the following sentences, a list of possible interpretations of the sentence is given. \n Choose the interpretation that you consider appropriate for each sentence.  \n33. Anyone who thinks that he can succeed in life without working hard is living in a fool's paradise. This means is that such a person
    A. is having an illusion
    B. thinks other people are fools
    C. thinks hat working is merely a joke.
    D. is on the verge of insanity.  \n """,
            """"
    12 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n  34. I am happy to inform you that your boys are conscientious
    A. industrious
    B. carefree
    C. careful
    D. corrupt \n """,
            """"
    13 From these questions, choose the options opposite in meaning to the words or phrases in italics. 35. My father is a very prosperous businessman.
    A. ungrateful
    B. unscrupulous
    C. unskilled
    D. unsuccessful \n """,
            """"
    14 From these questions, choose the options opposite in meaning to the words or phrases in italics. \n 36 My hostess greeted her guest in a very relaxed manner
    A. energetic
    B. athletic
    C. stiff
    D. perplexed \n """,
            """"
    15 From these questions, choose the options opposite in meaning to the words or phrases in italics. 37. Ayo takes his studies rather lightly
    A. humorously
    B. tediously
    C. carefully
    D. seriously \n """,
            """"
    16 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n  38. The doctor was very gentle with his patients in the examining room
    A. harsh
    B. rude
    C. rough
    D. unkind \n """,
            """"
    17. From these questions, choose the options opposite in meaning to the words or phrases in italics. \n 39. The President took exception to the ignoble role the young man played in the matter
    A. honourable
    B. embarrassing
    C dishonourable
    D. extraordinary \n """,
            """"
    18. From these questions, choose the options opposite in meaning to the words or phrases in italics.\n  40. The man who had been seriously ill was convalescing at a seaside resort
    A. regaining health
    B. deteriorating in health
    C. recuperating
    D. relaxing \n """,
            """"
    19 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n  41. For millions of years, the world resources have remained boundless
    A. unlimited
    B. scarce
    C. indomitable
    D. limited \n """,
            """"
    20 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n  42. The difference between the experimental procedures was imperceptible to me
    A. negligible
    B. significant 
    C. obvious
    D. obscure \n """,
            """"
    21 From these questions, choose the options opposite in meaning to the words or phrases in italics. \n 43. His anti-apathy to religion ideas makes him unpopular
    A. remedy
    B. Consciousness
    C. hostility
    D. receptiveness \n """,
            """"
    22 For the questions, choose the options that best complete the gap(s). 44, He was ... [A. assisted B.duped C. enjoined D. encouraged]... by the trickster.
    A. assisted 
    B.duped 
    C. enjoined
    D. encouraged \n """,
            """"
    23 For the questions, choose the options that best complete the gap(s). 45. When the soldiers saw that resistance was \n ... [A. inadequate B. inefficient C. futile D. successful] ..., they stopped fighting
    A. inadequate
    B. inefficient
    C. futile 
    D. successful \n """,
            """"
    24 For the questions, choose the options that best complete the gap(s). 46. You should read all the ... [A.brochures B. prospectus C. tickets D. handouts] ... carefully before you decide where to go on holiday.
    A.brochures 
    B. prospectus 
    C. tickets 
    D. handouts \n """,
            """"
    25 For the questions, choose the options that best complete the gap(s). 47. The Emir and Conqueror of the enemy territories. \n ---[A.arrives B. are to arrive C. arrive D. are arriving] --- next week.
    A.arrives
    B. are to arrive
    C. arrive 
    D. are arriving \n """,
            """"
    26 For the questions, choose the options that best complete the gap(s). 48 We ought to have visited the Governor, ...\n [A. isn't it B, oughtn't we C. shouldn't we D. haven't]
    A. isn't it 
    B, oughtn't we
    C. shouldn't we
    D. haven't \n """,
            """"
    27 For the questions, choose the options that best complete the gap(s). 49. He didn't sense Obi's presence in the room, did he?...\n  [A. yes, he did B. No, he did C. Yes, he didn't D. No, he didn't]
    A. yes, he did 
    B. No, he did 
    C. Yes, he didn't 
    D. No, he didn't \n """,
            """"
    28 For the questions, choose the options that best complete the gap(s). 50. You can stay here --- \n [A. as long B. so long C. in a much D. for as long] --- as you are quiet.
    A. as long 
    B. so long 
    C. in a much 
    D. for as long \n """,
            """"
    29 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n 51. The witness averred that she had seen Dosun at the scene of the crime  
    A. argued 
    B. confirmed 
    C. denied 
    D. affirmed \n """,
            """"
    30 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n  52. The high cost of living these days calls for a lot of frugality 
    A. extravagance 
    B. economy 
    C. recklessness 
    D. prudence. \n """,
            """"
    31 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n  53. Tunde's reaction underscoresthe points I was making. 
    A. justifies 
    B. summarizes 
    C. emphasizes 
    D. clarifies \n """,
            """"
    32 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics.  54. \n Everyone admired themanager's adroit handling of thecrisis in the company 
    A. emphasised 
    B. skilful 
    C. tactless 
    D. clumsy  \n """,
            """"
    33 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics.  55. The principal took exception \n to the ignoble role the teacher plays d in the matter 
    A. embarrassing 
    B. honourable 
    C. extraordinary
    D. dishonourable \n """,
            """"
    34 In each of these questions, choose the option that has the same sound as the one represented by the letter(s) underlined. 56. key
    A. sit 
    B. bet 
    C seat 
    D. tread \n """,
            """"
    35 In each of these questions, choose the option that has the same sound as the one represented by the letter(s) underlined.  57. taught 
    A. law 
    B. aunt 
    C. count 
    D. plateau \n """,
            """"
    36 In each of these questions, choose the appropriate stress item from the options. The syllables are written in capital letters. 58. comfortable 
    A. COMfortable 
    B. comFORtable 
    C. comfortaBLE 
    D. comforTABLE \n """,
            """"
    37  In each of these questions, choose the appropriate stress item from the options. The syllables are written in capital letters. 59. incapacitate 
    A. inCApacitate 
    B. incaPAcitate
    C. INcapacitate 
    D. incapaciTATE. \n """,
            """"
    38  In each of these questions, choose the appropriate stress item from the options. The syllables are written in capital letters.  60. encouragement 
    A. Encouragement 
    B. encouragement
    C. encouRAgement 
    D. encouragement  \n """,

    ]

    questions = [
                    Question(question_prompts[0], "D"),
                    Question(question_prompts[1], "C"),
                    Question(question_prompts[2], "A"),
                    Question(question_prompts[3], "B"),
                    Question(question_prompts[4], "C"),
                    Question(question_prompts[5], "C"),
                    Question(question_prompts[6], "C"),
                    Question(question_prompts[7], "A"),
                    Question(question_prompts[8], "B"),
                    Question(question_prompts[9], "D"),
                    Question(question_prompts[10], "A"),
                    Question(question_prompts[11], "B"),
                    Question(question_prompts[12], "D"),
                    Question(question_prompts[13], "C"),
                    Question(question_prompts[14], "D"),
                    Question(question_prompts[15], "A"),
                    Question(question_prompts[16], "A"),
                    Question(question_prompts[17], "B"),
                    Question(question_prompts[18], "B"),
                    Question(question_prompts[19], "B"),
                    Question(question_prompts[20], "D"),
                    Question(question_prompts[21], "B"),
                    Question(question_prompts[22], "C"),
                    Question(question_prompts[23], "A"),
                    Question(question_prompts[24], "A"),
                    Question(question_prompts[25], "B"),
                    Question(question_prompts[26], "D"),
                    Question(question_prompts[27], "A"),
                    Question(question_prompts[28], "C"),
                    Question(question_prompts[29], "A"),
                    Question(question_prompts[30], "D"),
                    Question(question_prompts[31], "B"),
                    Question(question_prompts[32], "B"),
                    Question(question_prompts[33], "A"),
                    Question(question_prompts[34], "A"),
                    Question(question_prompts[35], "A"),
                    Question(question_prompts[36], "B"),
                    Question(question_prompts[37], "A"),
    ]
    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        English_1981()
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

def Chemistry_1982():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False
    question_prompts = [
        """"  1 The presence of an impurity in substance will cause the melting point to
        be zero
        reduce
        increase
        be stable \n""",
        """"  2 What volume of carbon (ll) oxide is produced by reacting excess carbon with 10dm3 of oxygen?
        5 dm3
        20 dm3
        15 dm3
        10 dm3 \n""",
        """"  3 The rate of diffusion of a gas Y is twice that of Z If the relative molecular mass of Y is 64 and the two \n gases diffuse under the same conditions, find the relative molecular mass of Z
        32
        4
        8
        16 \n""",
        """"  4 The radioisotope used in industrial radiography for the rapid checking of faults in welds and casting is
        Carbon-14
        phosphorus-32
        cobalt-60
        iodine-131 \n""",
        """"  5  How many unpaired electrons are in the p-orbitals of a fluorine atom?
         3
         0
         1
         2 \n""",
        """"  6 The radioactive emission with the least ionization power is
        α-particles
        X-rays
        γ-rays
        β-particles \n""",
        """"  7 The shape of the carbon (lV) oxide molecule is 
        pyramidal
        linear
        angular
        tetrahedral \n""",
        """"  8 Which of the following molecules is held together by hydrogen bond?
        CH4
        HBr
        H2SO4
        HF \n""",
        """"  9 The bond formed between two elements with electron configurations 1s2 2s2 2p6 3s2 and 1s2 2s2 2p4 is
        metallic
        covalent
        dative
        ionic \n""",
        """" 10 The constituent of air that acts as a diluent is
        nitrogen
        carbon (IV) oxide 
        noble gases
        oxygen \n""",
        """"  11 Steam changes the colour of anhydrous cobalt (ll) chloride from
        white to red
        blue to white
        blue to pink
        white to blue \n""",
        """" 12  An example of a hygroscopic substance is
        CuO(s)
         MgCl(S)
         CaCl2(S)
         NaOH(S) \n""",
        """" 13  If 24.4g of lead (ll) trioxonitrate (V) were dissolved in 42 g of distilled water at 20⁰C; calculate the solubility of the solute in gdm-3
         581.000
         0.581
         5.810 
         58.100 \n""",
        """"  14 The solvent used for removing grease stain is
         turpentine
         ammonia solution
         ethanol
         solution of borax in water \n""",
        """" 15  In a water body, too much sewage leads to
         a decrease in the temperature of the water which cause in death of aquatic animals
         an increase in the number of aquatic animals in the water
         an increase in the bacterial population which reduces the level of oxygen in the water
         a decrease in the bacterial population which increases the level of oxygen in the water \n""",
        """" 16  10.0 dm3 of water was added to 2.0 moldm-3 of 2.5dm3 solution of HCl. What is the concentration of the final solution in mol dm-3? 
         0.4
         8.0
         2.0
         0.5 \n""",
        """"  17 Three drops of a 1.0 mol dm-3 solution of HCl was added to 20cm3 of a solution of pH6.4. The pH of the resulting solution will be
        close to that of pure water
        less than 6.4
        greater than 6.4
        unaltered \n""",
        """"  18 Which of the following substances is not a salt?
        Aluminium oxide
        Sodium hydrogen trioxosulphate (V)
        Sodium trioxocarbonate (V)
        Zinc chloride \n""",
        """" 19  An insoluble salt can be prepared by
         the reaction of trioxocarbonate (V) with an acid 
         double decomposition
         the action of dilute acid on an insoluble base
         the reaction of metals with an acid \n""",
        """" 20 . 2H2O(l) + 2F2(g) → 4HF +O2(g) In the reaction above, the substance that is being reduced is
        A. O2(g)
        B. H2O(g)
        C. F2(g)
        D. HF(g) \n""",
        """" 21  Zn(s) + CuSO4(aq)  → ZnSO4(aq) + Cu(s) In the reaction above, the oxidizing agent is
         CuSO4(s)
         ZnSO4(aq)
         Cu(s)
         Zn(s) \n""",
        """" 22  In an electrochemical cell, polarization is caused by
         chlorine
         oxygen
         tetraoxosulphate (Vl) acid
         hydrogen \n""",
        """" 23  Calculate the volume in cm3 of oxygen evolved as s.t.p. when a current of 5 A is passed through acidified water \n for 193s {F = 96500 Cmol-1, Molar volume of a gas at s.t.p. = 22.4 dm3} 
         224.000 dm3
         0.056 dm3
         0.224 dm3
         56.000 dm3 \n""",
        """" 24  In an endothermic reaction, if there is a loss in entropy the reaction will
         be indeterminate
         be spontaneous
         not be spontaneous
         be at equilibrium \n""",
        """" 25  2SO2(g) + O2(g) ⇋ 2SO3(g) ΔH = −395.7kJmol−1 In the reaction above, the concentration of SO3(g) can be increased by
         decreasing the pressure
         decreasing the temperature
         increasing the temperature
         the addition of catalyst \n""",
        """" 26  The minimum amount of energy required for a reaction to take place is
         lattice energy
         ionization energy
         activation energy
         kinetic energy \n""",
        """" 27 . Which of the following compounds is a neutral oxide?
        A. Carbon (IV) oxide
        B. Sulphur (Vl) oxide
        C. Sulphur (IV) oxide
        D. Carbon (ll) oxide \n""",
        """" 28  In the laboratory preparation of ammonia, the flask is placed in a slanting position so as to
         prevent condensed water from breaking the reaction flask
         enable the proper mixing of the reactions in the flask
         enhance the speed of the reaction
         prevent formation of precipitate \n""",
        """" 29  Which of the gases is employed as an anaesthesia?
         N2O
         NO2
         NH3
         NO \n""",
        """" 30  Sulphur (IV) oxide is a strong reducing agent in the presence of water due to the formation of
         hydroxide ion
         sulphur (Vl) oxide
         hydrogen sulphide
         trioxosulphate (IV) salt \n""",
        """" 31  A metal that forms soluble trioxosulphate (IV) ion is
         barium
         potassium
         manganese
         aluminium \n""",
        """" 32  Copper is displaced from the solution of its salts by most metals because it
         is a transition element
         is at the bottom of the activity series
         is very reactive
         has completely filled 3dorbitals \n""",
        """" 33 The coloured nature of transition metal ions are associated with their partially filled
         f- orbital
         s- orbital
         p-orbital
         d-orbital \n""",
        """" 34 Aluminium containers are frequently used to transport  trioxonitrate (V) acid because aluminium
         has a silvery-white appearance
         has a low density
         does not react with the acid
         does not corrode \n""",
        """" 35 2-methylbutan-2-ol is an example of a
         dihydric alkanol
         tertiary alkanol
         secondary alkanol
         primary alkanol \n""",
        """" 36 The reaction between ammonia and ethyl ethanoate produces
        propanol and ethanamide
        propanol and propanamide
        ethanol and propanamide
        ethanol and ethanamide \n""",
        """" 37 The decarboxylation of ethanoic acid will produce carbon (IV) oxide and
        methane
        ethane
        propane
        butane \n""",
        """" 38  The compound that will react with sodium hydroxide to form salt and water is
         C6H12O6
         (CH3)3COH
         CH3CH=CH2
         CH3CH2COOH \n""",
        """" 39 Which of the following compounds in solution will turn red litmus paper blue?
        ROR
        RCON(R)2
        RNH2
        RCOR \n""",
        """" 40 . The dehydration of ammonium salt of alkanoic acids produces a compound with the general formula
        ROR
        RCONH2
        RNH2
        RCOR \n""",
        """" 41  Which of the following fraction is used as raw material for the cracking process?
         kerosene
         lubricating oil
         bitumen
         diesel oils \n""",
        """" 42 Which of the following fraction is used as raw material for the cracking process?
         kerosene
         lubricating oil
         bitumen
         diesel oils \n""",
        """" 43 An organic compound contains 60% carbon, 13.3% hydrogen and 26.7% oxygen. Calculate the empirical formula (C=12, H =1, O=16)
        C5H12O
        C3H8O
        C6H13O2
        C4H9O \n""",
        ]
    questions = [
                    Question(question_prompts[0], "B"),
                    Question(question_prompts[1], "B"),
                    Question(question_prompts[2], "D"),
                    Question(question_prompts[3], "C"),
                    Question(question_prompts[4], "C"),
                    Question(question_prompts[5], "C"),
                    Question(question_prompts[6], "B"),
                    Question(question_prompts[7], "D"),
                    Question(question_prompts[8], "D"),
                    Question(question_prompts[9], "A"),
                    Question(question_prompts[10], "C"),
                    Question(question_prompts[11], "A"),
                    Question(question_prompts[12], "A"),
                    Question(question_prompts[13], "B"),
                    Question(question_prompts[14], "C"),
                    Question(question_prompts[15], "A"),
                    Question(question_prompts[16], "B"),
                    Question(question_prompts[17], "A"),
                    Question(question_prompts[18], "B"),
                    Question(question_prompts[19], "C"),
                    Question(question_prompts[20], "A"),
                    Question(question_prompts[21], "D"),
                    Question(question_prompts[22], "B"),
                    Question(question_prompts[23], "C"),
                    Question(question_prompts[24], "B"),
                    Question(question_prompts[25], "C"),
                    Question(question_prompts[26], "D"),
                    Question(question_prompts[27], "A"),
                    Question(question_prompts[28], "D"),
                    Question(question_prompts[29], "D"),
                    Question(question_prompts[30], "B"),
                    Question(question_prompts[31], "B"),
                    Question(question_prompts[32], "D"),
                    Question(question_prompts[33], "B"),
                    Question(question_prompts[34], "D"),
                    Question(question_prompts[35], "D"),
                    Question(question_prompts[36], "B"),
                    Question(question_prompts[37], "A"),
                    Question(question_prompts[38], "D"),
                    Question(question_prompts[39], "B"),
                    Question(question_prompts[40], "B"),
                    Question(question_prompts[41], "B"),
                    Question(question_prompts[42], "B"),

    ]
    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print(" you are doing well!!")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")

        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Chemistry_1982()

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

def Physics_1983():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False
    question_prompts = [
    """"1. What is the least possible error encountered when taking measurement with a meter rule?  
    A. 0.5 mm 
    B. 1.0 mm. 
    C. 0.2 mm. 
    D. 0.1 mm \n""",
    """"2. The electromotive force in the secondary winding is  
    A. stabilizing 
    B. reducing 
    C. increasing 
    D. varying \n""",
    """"3. If a pump is capable of lifting 5000 kg of water through a vertical height of 60 in 15 mins, the power of the pump is  
    A. 3.3 x 103J −1  
    B. 2.5 x 104J −1  
    c. 2.5 x 105J −1 
    D. 3.3 x 102J −1 \n""",
    """" 4. Calculate the temperature change when 500J of heat is supplied to 100g of water. 
    A. 12.1°C 
    B. 2.1°C 
    C. 1.2°C 
    D. 0.1°C \n""",
    """"5. Which of the following particles CANNOT be deflected by both electric and magnetic fields? 
    A. Gamma rays 
    B. Alpha particles. 
    C. Wave particles 
    D. Beta particles. \n""",
    """"6. Under which of the following conditions do gasses conduct electricity?  
    A. High pressure and low p.d 
    B. Low pressure and high p.d 
    C. Low pressure and low p.d 
    D. High pressure and high p.d \n""",
    """"7. Dispersion occurs when white light passes through a glass prism because of the  
    A. defects in the glass. 
    B. high density of the glass. 
    C. different speeds of the colour in the glass. 
    D. different hidden colours in the glass. \n""",
    """"8. Calculate the e.m.f of the cell in the above circuit if its internal resistance is negligible.  
    A. 12V 
    B. 36V 
    C. 2V 
    D. 8V \n""",
    """"9. An object of mass 80kg is pulled on a horizontal rough ground by a force of 500N. \n Find the coefficient of static friction. [ g ≈ 10m −2]  
    A. 0.6. 
    B. 0.4 
    C. 1.0 
    D. 0.8. \n""",
    """"10. A glass plate 0.9 cm thick has a refractive index of 1.50. \n How long does it take for a pulse of light to pass through the plate? [c= 3.0 x 108m −1] 
    A. 3.0 x 10−10 s 
    B. 4.5 x 10−11 s 
    C. 3.0 x 10−11 s 
    D. 4.5 x 10−10 s \n""",
    """"11. The main purpose of the transformer in an a.c radio set is to  
    A. increase power to the radio. 
    B. convert energy from a.c. to d.c 
    C. step up the voltage. 
    D. step down he voltage. \n""",
    """"12. The energy associated with the emitted photon when a mercury atom changes from one state to another is 3.3   . \n Calculate the frequency of the photon. 
    A. 3.2 x 10−53 Hz. 
    B. 3.1 x 10−53 Hz 
    C. 1.3 x 10−53 Hz 
    D. 8.0 x 10−53 Hz \n""",
    """"13. To protect a material from the influence of an external magnetic field, the material should be kept in a  
    A. soft iron ring. 
    B. loop of copper wire. 
    C. triangular zinc ring. 
    D. square steel ring. \n""",
    """"14.Thermal equilibrium between two objects exists when 
    A. the heat capacities of both objects are the same 
    B. the quantity of heat in both objects are the same. 
    C. the temperature of both objects are equal 
    D. one object loses heat continuously to the other. \n""",
    """"15. Which of the following is a characteristic of stationary waves?  
    A. The antinode is a point of minimum displacement. 
    B. The distance between two successive nodes is one wavelength. 
    C. They can be transverse or longitudinal 
    D. They are formed by two identical waves travelling in opposite directions. \n""",
    """"16. The height at which the atmosphere ceases to exist is about 80km. if the atmospheric pressure at a height of 20km above the ground level is  
    A. 480mmhg 
    B. 570mmhg 
    C.190mmhg 
    D. 380mmhg \n""",
    """"17. A metal of mass 0.5kg is heated to 100⁰ and then transferred to a welllagged calorimeter of heat capacity 80jk-1 containing \n water of heat capacity of the metal  
    A. 92 j kg-1 
    B. 286 j kg-1 k-1 
    C. 133 j kg-1 k-1 
    D. 887 j kg-1 k-1 \n""",
    """18 1. In the series a.c circuit shown below, the p.d across the inductor is 8 V.r.m.s. The effective voltage is  
    A. 10v 
    B. 2v 
    C. 14v 
    D. 48v \n""",
    """"19 . In a closed organ pipe producing a musical note, an antinode will always be produced at  
    A. the closed end 
    B. the middle 
    C. the open end 
    D. all the parts of the pipe. \n""",
    """"20 . What happens when a certain quantity of pure ice is completely changed to water at 0⁰C ?  
    A. Latent heat is absorbed, the mass decreases and the volume increases. 
    B. latent heat is absorbed, the mass remains constant and the volume decreases. 
    C. latent heat is given out, the mass increases and the volume remains constant 
    D. latent heat is given out, the mass remains constant and the volume decreases. \n""",
    """" 21. If two parallel conductors carry currents flowing in the same direction, the conductors will 
    A. repel each other 
    B. attract each other 
    C. both move in the same direction. 
    D. have no effect on each other \n""",
    """" 22 . Which of the following correctly explain(s) why a green leaf appears green in a bright daylight?  \n I. It absorbs only the green component of sunlight II. It absorbs all colours in sunlight except green III. It reflects only the green component of sunlight  
    A. I only 
    B. II and III only 
    C. I and II only 
    D. II only. \n""",
    """"23. Which of the following factors has no effect on the e.m.f of a primary cell?  
    A. nature of plate 
    B. size of the cell 
    C. temperature 
    D. nature of the electrolyte. \n""",
    """"24. When the bottom tip of a vibrating tuning fork is held in contact with a wooden box, a louder sound is heard. this phenomenon is known as  
    A. beats 
    B. echoing 
    C. reverberation 
    D. resonance. \n""",
    """"25. The electrochemical equivalent of silver is 0.0012g/C if 36.0g of silver is to be deposited by electrolysis\n on a surface by passing a steady current for 5.0 minutes, the current must be  
    A. 6000A 
    B. 100A 
    C. 100A 
    D. 1.0A \n""",
    """"26. The principle of operation of an induction coil is based on ___  
    A. Ohm’s 
    B. ampere’s law 
    C. faraday’s law 
    D. coulomb’s law \n""",
    """"27. Mercury is suitable as a barometric fluid because it  
    A. expands uniformly 
    B. is several times denser than water 
    C. is opaque 
    D. is a good conductor of heat \n""",
    """"28. Which of the following features is NOT a characteristic of natural radioactivity?  
    A. radioactivity is a nuclear phenomenon 
    B. radioactivity is exhibited only by the element of mass number greater than 206 
    C. The radioactivity of an element is affected by electric and magnetic fields in the surroundings. 
    D Radioactive substances emit three types of radiations ∝-rays, β-rays and γ-rays.\n""",
    """". 29 Which of the following is a correct explanation of the INERTIA of a body? 
    A. Reluctance to start moving at rest and its reluctance to stop moving once it has begun move 
    B. Reluctance to stop moving 
    C. Readiness to start moving 
    D. Reluctance to start moving and its readiness to stop moving once it has begun to move \n""",
    """"30. If the force on a charge of 0.2 coulomb in an electric field intensity of the field is  
    A. 0.8 
    B. 20.0 N/C 
    C. 0.8N/C 
    D. 4.2N/C \n""",
    """"31. The point beyond which a stretched spring does not return to its original length is called the  
    A. breaking point 
    B. sprint constant 
    C. elastic limit 
    D. elasticity point. \n""",
    """"32. Which of the following statements is applicable to a real image formed by a concave mirror?  \n I. It can be observed on a screen II. It is always inverted and in  front of the mirror III. It only seems to exist IV. It is formed by the actual converging of rays of light.  
    A. I, II and III only 
    B. I, II and IV only 
    C. I and III only) 
    D. I and II only. \n""",
    """"33. which of the following does not cause a reduction of the surface tension of water?  
    A. soap solution 
    B. detergent 
    C. alcohol 
    D. grease \n""",
    """"34. in what range of temperature is the expansion of water anomalous?  
    A. +208⁰c to +212⁰c 
    B. -800⁰c +-76⁰c 
    C. 0⁰c to 4⁰c 
    D. -4⁰c TO 0⁰ \n""",
        ]
    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "C"),

    ]
    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("good job and thrive more to get the next answer right!!!")
                score+=1
            else:
                print("wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1983()

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
        C. phillen and xylem 
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
            else:
                print("wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1984()

def biology_1985():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """1. Which of the following has the most primitive respiratory system?
        A. insect
        B. fish
        C. snail
        D. mouse \n """,
        """2. One adaptation shown by hydrophytes in fresh water habitats is the
        A. waxy cuticle on shoot surface
        B. poor development of roots and xylem  tissues
        C. well-developed roots and supporting  system
        D. leaves reduced to spines \n """,
        """3. Which of the following use diffusion as the principal method of gaseous exchange?
        A. grasshopper
        B. rat spines
        C. lizard
        D. earthworm \n """,
        """4. The theory which supports the view that the large muscles developed by an athlete will be passed on to the offspring was proposed by
        A. Mendel
        B. Darwin
        C. Lamark
        D. Pasteur \n """,
        """5. The chromosomes of members of the kingdom Monera are within the
        A. nucleoplasm
        B. nucleus
        C. nucleolus
        D. cytoplasm \n """,
        """6. The mangrove swamp in Nigeria is restricted to the
        A. Sahel savanna 
        B. Guinea savanna 
        C. Tropical rainforest 
        D. Sudan savanna \n """,
        """7. The pancrease secretes enzymes for the digestion of
        A. fats, proteins and carbohydrates
        B. fats, vitamins and cellulose
        C. fats, carbohydrates and vitamins
        D. proteins, cellulose and minerals \n """,
        """8. The causative agent of bird flu is a
        A. protozoan
        B. virus
        C. bacterium
        D. fungus \n """,
        """9. A water medium is necessary for fertilization in
        A. conifers
        B. angiosperms
        C. ferns
        D. fungi \n """,
        """10. An example of a sex-linked trait is the
        A. colour of the skin in humans
        B. ability to roll the tongue
        C. possession of facial hair in adult humans
        D. ability to grow. long hair in females \n """,
        """11. In which of the following Nigerian states can montane vegetation be found?
        A. Bauchi
        B. Plateau
        C. Taraba
        D. Enugu \n """,
        """12. Which of the following is true of cloning?
        A. it is welcomed as an ethically and normally sound science
        B. it involves the asexual multiplication of the tissues of the original organism
        C. the clone is similar to but not exactly like the original organism 
        D. only one cell of the original organism is needed to imitate the process  \n """,
        """13. The process of shedding the exoskeleton of an arthropod is known as
        A. ecdysis
        B. in star formation
        C. metamorphosis
        D. osmosis \n """,
        """14. Which of the following is a major cause of constipation in humans?
        A. lack of roughage
        B. vitamin B
        C. vitamin E
        D. lack of salts \n """,
        """15. In mammals, the organ directly on top of the kidney is the
        A. adrenal gland
        B. prostate gland
        C. pancrease
        D. thyroid gland \n """,
        """16. An accurate identification of a rapist can be carried out by conducting a
        A. RNA analysis
        B. blood group test
        C. behavioural traits test
        D. DNA analysis \n """,
        """17. An example of a fish that aestivates is
        A. croaker
        B. lung fish
        C. shark
        D. cat fish \n """,
        """18. The opening and closing of the stoma are regulated by
        A. respiration
        B. osmosis
        C. diffusion
        D. transpiration \n """,
        """19. Which of the following is common to the mosquito, housefly and blackfly? 
        A. they are parasites of man
        B. their immature stages are aquatic
        C. they undergo complete metamorphosis
        D. their adults have two pairs of wings \n """,
        """20. The organs that will be most useful to giant African rats in finding their way in underground habitats are the
        A. nostrils
        B. eyes
        C. vibrissae
        D. tails \n """,
        """21. A crucible of 5gm weighed 10gm after filling with fresh soil. It is then heated in an oven at 1000C for 1 hour. \n After cooling in a desiccator, the weightwas 8gm. The percentage of water in thesoil is
        A. 0.8
        B. 0.2
        C. 0.4
        D. 0.6 \n """,
        """22. The waste product of plants used in the conversion of hide to leather is
        A. alkaloid
        B. resin
        C. tannin
        D. gun \n """,
        """23. The correct sequence of the movement of urea during formation is
        A. glomerulus - Bowman's capsule -convoluted tubule - Henle's loop -collecting tubule
        B. convoluted tubule - glomerulus -Henle's loop - Bowman's capsule -collecting tubule
        C. glomerulus - Bowman's capsule-convoluted tubule - Henle's loop collecting tubule 
        D. convoluted tubule - Bowman's capsule- Henle's loop -glomerulus - collectingtubule \n """,
        """24. In lizards, the lowing of the gularfold is used to
        A. defend their territory
        B. attract mates
        C. frighten enemies
        D. catch insects \n """,
        """25. The photosynthetic pigments include
        A. chloroplast and cytochromes
        B. melanin and haemoglobin
        C. chlorophyll and carotenoids
        D. carotenoids and haemoglobin \n """,
        """26. The highest level of ecological organization is the
        A. ecosystem
        B. niche
        C. biosphere
        D. population \n """,
        """27. A biotic factor which affects the distribution and abundance of organism in a terrestrial habitat is
        A. pH
        B. competition
        C. temperature
        D. light \n """,
        """28. The eye defect that rises because the cornea is not curved smoothly is
        A. astigmatism
        B. short-sightedness
        C. long-sightedness
        D. presbyopia \n """,
        """29. Which of the following is an example of parasitism?
        A. a squirrel living in an abandoned nest of a bird 
        B. mistletoe growing on an orange tree 
        C. fungi growing on a dead tree branch 
        D. cattle egrets taking tasks from thebody of cattle \n """,
        """30. The increasing order of the particle size in the following soil types is
        A. cattle sand – clay-gravel
        B. clay - silt sand – gravel
        C. silt - clay - sand - gravel
        D. clay - sand - silt – gravel \n """,
        """31. Which of following factors can bring about competition population?
        A. emigration
        B. drought
        C. mortality
        D. dispersion \n """,
        """32.Stunted growth and poor root development are a result of a deficiency in
        A. phosphorus
        B. calcium
        C. sulphur
        D. iron \n """

        ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "A"),

        ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print("wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1985()

def Physics_1986():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
                """1. The focal length of a concave  mirror is 2.0 cm. If an object is  placed 8.0cm from it,\n  the image is  at. 
        A. 2.7m 
        B. 2.3m 
        C.2.5m 
        D. 2.0m \n """,
        """2. PHCN measures is electrical  energy in 
        A. Wh. 
        B. Kwh 
        C. J 
        D. W. \n """,
        """3. The resultant of two forces is  50N. If the forces are  perpendicular to each other and  one of them \n makes an angle 30°  with the resultant. Find its  magnitude.  
        A. 100.0N 
        B. 57.7N 
        C. 25.0N  
        D. 43.3N \n """,
        """4. A piece of radioactive material  contains 1000 atoms. If its half life is 20 seconds, the time taken  \n for 125 atoms to remain is 
        A. 20 seconds 
        B. 40 seconds 
        C. 60 seconds 
        D. 80 seconds \n """,
        """7. In a discharge tube, most of  the gas is pumped out so that  electricity is concluded at 
        A. steady voltage 
        B. high pressure 
        C. low pressure. 
        D. low voltage. \n """,
        """8. I. Moon II. Sun  III. Street light  IV. Stars   Which of the above is a natural  source of light?  
        A. I, II and IV only 
        B. I, II and III only 
        C. III and IV only 
        D. II and IV only \n """,
        """9. An object placed at the bottom  of a well full of clear water  appears closer to the surface due to 
        A. refraction. 
        B. reflection. 
        C. am inverter 
        D. a magnifier \n """,
        """10. A boy drags a bag of rice  along a smooth horizontal flow  with a force of 2N applied at an  angle of\n  60° to the flow. The work done after a distance of 3m is 
        A. 6J. 
        B. 4 J 
        C. 5 J 
        D. 3 J \n """,
        """11. The spheres of masses 5.0kg  and 10.0kg are 0.3m apart.  Calculate the force of attraction  between them. 
        A. 3.57 X 10−2 N. 
        B. 3.71 X 10−2 N. 
        C. 4.00 X 10−2 N. 
        D. 3.50 X 10−2 N. \n """,
        """12. When very hot water is  poured into two identical thin and  thick glass tumblers in equal  volumes,\n  the thick one cracks  because 
        A. of the even expansion of lass. 
        B. glass is a good conductor of  heat. 
        C. glass is a crystal 
        D. of the uneven expansion of  glass \n """,
        """14. Transverse waves can be  distinguished from longitudinal  waves using the characteristic of  
        A. diffraction 
        B. reflection. 
        C. polarization. 
        D. refraction. \n """,
        """15. Which of the following pairs of  light rays shows the widest  separation in the spectrum of  white light? 
        A. Green and yellow. 
        B. Blue and red 
        C. Indigo and violet 
        D. Orange and red. \n """,
        """17. A transistor functions mainly  as a 
        A. switch and an amplifier 
        B. rectifier and an amplifier 
        C. charge storer and a switch 
        D. charge storer and an amplifier \n """,
        """18. A thin wire with heavy  weights attached to both ends is  hung over a block of ice resting  on two \n supports. If the wire cuts  through the ice block while the  lock remains solid behind the  wire, the process is called  
        A. fusion 
        B. sublimation 
        C. regelation 
        D. condensation. \n """,
        """19. The inner diameter of a small  test tube can be measured  accurately using a 
        A. micrometer screw gauge 
        B. pair of Vernier callipers 
        C. metre rule 
        D. pair of dividers. \n """,
        """20. A platinum resistance  thermometer records 3.0W at 0°C  and 8/0w at 100°C. If it records  6.0W in a \n certain environment,  the temperature of the medium is  
        A. 60°C 
        B. 80°C 
        C. 50°C 
        D. 30°C \n """,
        """22. Which of the following is the  dimension of pressure? 
        A. ML2T−3 
        B. MLT−2 
        C. ML2−1T−2 
        D. ML−3\n """,
        """23. A capacitor 8μF, is charged to  a potential difference of 100V.  The energy stored by the  capacitor is 
        A. 1.0 x 104  
        B. 4.0 x 10−2  
        C. 1.25 x 10   
        D. 8.0 x 10 \n """,
        """ 24. Which of the following  statements correctly describe(s)  cathode rays?   I. They consist of tiny \n  particles carrying negative  electric charges  II. They are deflected in a  magnetic field but not in an  electric filed.  III. They consist of fast moving neutrons and  deflected in an electric filed. 
        A. I only 
        B. III only 
        C. I and II only 
        D. II and III only. \n """,
        """25. A concave mirror has a radius  of curvature of 36cm. At what  distance from the mirror should  an object\n  be placed to give a real  image three times the size of the  object? 
        A. 12cm 
        B. 24cm 
        C. 48cm 
        D. 108cm \n """,
        """27. A sonometer wire of length 100cm under a tension of 10N,  has a frequency of 250Hz.  Keeping the length\n  of the wire  constant, the tension is adjusted  to produce a new frequency of  350HZ. The new tension is  
        A. 5.1N 
        B. 19.6N 
        C. 14.0N 
        D. 7.1N \n """,
        """28. In a sound wave in air, the  adjacent rarefactions and  compressions are separated by a  distance of 17cm.\n  If the velocity of the sound wave is 340m −1. Determine the frequency. 
        A. 10Hz 
        B. 20Hz 
        C. 5780Hz 
        D. 1000Hz \n """,
        """29. A note is called an octave of  another note when 
        A. the notes have the same  fundamental frequency 
        B. its frequency is half of the first note. 
        C. its frequency is twice that of  the first note. 
        D. its periodic time is twice that of  the first note. \n """,
        """31. Which of the following is in a  neutral equilibrium? 
        A. A heavy weight suspended on a  string 
        B. The beam of a balance in use 
        C. A heavy-based table lamp 
        D. A cone resting on its slant edge \n """,
        """32. A convex mirror is used as a  driving mirror because   I. Its image is erect  \n II. It has a large field of view  III. It has a long focal length.  Identify the CORRECT  statement(s). 
        A. I and III only 
        B. I and II only 
        C. II and III only 
        D. I, II and III only \n """,
        """33. What is the cost of running  five 50W lamps and four 100W  lamps for 10 hours \n if electrical  energy costs 2 kobo per kWh? 
        A. ₦ 0.13 
        B. ₦ 0.65 
        C. ₦ 3.90 
        D. ₦39.00 \n """,
        """34. The specific latent heat of  vaporization of a substance is  always 
        A. less than its specific latent heat  of fusion 
        B. equal to its specific latent heat  of fusion 
        C. greater than its specific latent of fusion 
        D. all of the above depending on  the nature of the substance. \n """,
        """35. A hydrometer is an  instrument for measuring the 
        A. depth off water in a vessel 
        B. relative humidity of the air 
        C. relative density of a liquid by  finding the apparent loss in  weight 
        D. relative density of a liquid by  the method of flotation \n """,
        """36. A transformer has 300 turns  of wire in the primary coil and 30  turns in the secondary coil. \n If the  input voltage is 100 volts, the  output voltage is 
        A. 10 volts 
        B. 5 volts 
        C. 15 volts 
        D. 20 volts. \n """,
        """37. The activity of a radioactive  substance depends on  
        A. temperature and purity 
        B. purity and age 
        C. temperature and age 
        D. age, purity and temperature \n """,
        """38. The speed of light in air is 3 x 108  −1. If the refractive index of light from air-to-water is 4/3,\n  then which of the following is the  correct value of the speed of light  in water? 
        A. 4 x 108m −1 
        B. 2.23 x 108m −1 
        C. 2.25 x 108m −2 
        D. 4/9 x 108m −1 \n """,
        """39. A magnet is moved through a  coil of wire. The e.m.f. produced  in the wire depends on 
        A. the number of turns in the coil 
        B. the strength of magnet 
        C. the speed at which the magnet is moved 
        D. all of the above. \n """,
        """40. A charge of one coulomb  liberated 0.0033g of copper in an  electrolytic process. \n ow long will  it take a current of 2A to liberate  1.98g of copper in such a  process? 
        A. 30 minutes 
        B. 5 minutes 
        C. 50 minutes 
        D. 60 minutes.\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "B"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1986()

def biology_1987():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """0. Which of the following organism is not classified as an animal? 
        A. Amoeba 
        C. Euglena 
        B. Paramecium 
        D. Obelia \n """,
        """1. An organisation that operates physiological activities by using its at the cellular level of organisation, carries out its 
        A. cell membrane 
        C. small size 
        B. organelles 
        D. cytoplasm \n """,
        """2. The organelle which eliminates water from the bodyof a protozoam is the ___ 
        A. plasma membrane 
        B. contractile vacuole 
        C. nucleus 
        D. cell wall \n """,
        """3. Which of the following cell types has the least number of mitochondria? 
        A. cardiac cells of the heart 
        C. muscle cells of the bladder 
        B. cells of the cornified layer 
        D. muscle cells of the diaphragm \n """,
        """4. A typical plant cell is mainly distinguished from an animal cell by the possession of ___ 
        A. chloroplast and nucleus 
        C. chloroplast and cell wall 
        B. cell wall and cytoplasm 
        D. cell wall and mitochondria \n """,
        """5. Which of the following characteristics do fungi share in  common with animals? 
        A. presence of digestive tract 
        B. movement from one place to another 
        C. storage of carbohydrate as glycogen 
        D. movement of centrioles during cell division \n """,
        """6. Which of the following processes involve diffusion? 
        A. opening and closing of stomatal pores 
        B. turgidity of herbaceous plants 
        C. absorption of water through root hairs 
        D. absorption of digested food into the villi \n """,
        """7. The mechanism of opening and closing of the stomata in plants is based on ___ 
        A. turgidity and diffusion 
        B. turgidity and flaccidity 
        C. osmosis and diffusion 
        D. diffusion and flaccidity \n """,
        """8. In cellular respiration, energy is made available to organism by ___
        A. removal of a phosphate group from ADP 
        B. breaking off a phosphate group from ATP
         C. adding a phosphate group to glucose 
        D. breaking off a hydrogen ion from NADPH \n """,
        """9. Excretion in Paramecium is by diffusion because ___ 
        A. its habitat is water and moist places 
        B. it has simple, small and few internal organs 
        C. it has a large surface area to volume ratio 
        D. it has a large efficient meganucleus \n """,
        """10. Which of the following statement is true about transpiration? It is the ___ 
        A. loss of water in form of vapour from the surface of the leaf 
        B. loss of water in form of vapour from the body of the leaf 
        C. absorption of water in form of vapour from the body of the plant 
        D. movement of water through the body of the plant \n """,
        """11. A moss plant can withstand drought by means of its  
        A. spores 
        C. antheridia 
        B. rhizoids 
        D. achegonia \n """,
        """12. The main reason for the conservation of wildlife is to ___ 
        A. create national parks for recreation 
        B. maintain ecological balance in communities 
        C. prevent hunters from being cruel to animals 
        D. save some species from extinction \n """,
        """13. Which of the following is an example of variation? 
        A. blood group 
        C. reproduction 
        B. tongue rolling 
        D. growth \n """,
        """14. The parameters of size, population of living things are height, weight and colour in a examples of ___ 
        A. environmental variation 
        B. non-heritable variation 
        C. continuous variation 
        D. discontinuous variation \n """,
        """15. Fingerprints are useful in crime detection because ___ 
        A. the police have sophisticated fingerprint machines 
        B. thieves may leave their prints at the scene of crime 
        C. no two people have the same fingerprints 
        D. fingerprints are easy to make \n """,
        """16. A person with blood group O can be given blood from persons who have blood belonging to 
        ___ 
        A. group O only 
        C. groups A and O 
        B. group A only 
        D. groups A, B and O \n """,
        """17. Which of the following statements about heredity is not true? In heredity, the traits are 
        ___
        A. carried by genes 
        B. contained in ovum and sperm 
        C. always transmitted by one parent 
        D. transmitted from parents to offsprings \n """,
        """18. In evolution, analogous structures are significant because they show  
        A. physiological diversity 
        B. functional diversity 
        C. genetic diversity 
        D. structural diversity \n """,
        """19. Which of the following animals exhibit territoriality? 
        A. Rabbit 
        C. Lizard 
        B. Earthworm 
        D. Toad \n """,
        """20. The branch of Biology that deals with the principles of classification of organisms is known as ___ 
        A. biological index 
        B. nomenclature 
        C. taxonomy 
        D. ecology \n """,
        """21. Which of the following structures is a tissue? 
        A. vessel element 
        C. sieve tube element 
        B. blood 
        D. erythrocytes \n """,
        """22. Which of the following cells are not regarded as specialized?
        A. sperm cells 
        C. muscle cells 
        B. root tip cells 
        D. somatic cells \n """,
        """23. Which of the following pairs of cells carry out the same function? 
        A. check cell and red blood cell 
        C. palisade cell and epidermal cell 
        B. spermatozoan and ovum 
        D. root tip cell and guard cell \n """,
        """24. If Amoeba is placed in a salt solution, the contractile vacuoles would ___
        A. be bursting more frequently 
        B. be more numerous 
        C. be formed less frequently 
        D. grow bigger before they burst \n """,
        """25. Cells that utilizes a lot of presence of a large number of energy are characterised by the ___
        A. vacuoles 
        B. mitochondria 
        C. endoplasmic reticulum 
        D. ribosomes \n """,
        """26. During sexual reproduction in does the zygote divide to produce Paramecium, how many 
        times eight nuclei?
        A. 1 
        C. 3 
        B. 2 
        D. 4 \n """,
        """27. Which of the following statements is not true about continuous variation? It _
        A. is usually controlled by several genes 
        B. can be influenced by environmental factor 
        C. follows a normal distribution curve 
        D. is usually controlled by one or two pairs of genes\n """,
        """28. Acquired characters are  
        A. received from parents 
        B. passed to offspring 
        C. caused by the environment 
        D. caused by mutation \n """,
        """29. Differences in the individual of the same species is characteristics observed between known as ___ 
        A. trait 
        B. phenotype 
        C. mutation 
        D. variation \n """,
        """30. Natural selection is a consequence of ___
        A. distribution of organism 
        C. variation in organisms 
        B. adverse conditions 
        D. inbreeding \n """,
        """31. A vestigial structure in humans is ___ 
        A. earlobe 
        C. tail bone 
        B. toe bone 
        D. spleen \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "C"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1987()

def biology_1988():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """1. Which of the following structures is a protective adaptive feature of the Agama Lizard to the environment? 
    A. Nuchal crest
    B. Claws
    C. Scaly skin
    D. Gular fold. \n """,
    """2. Which of the following adapts an insect for feeding?
    A. suitable mouthparts
    B. paired antennae
    C. segmented body
    D. jointed appendages \n """,
    """3. Which of the following results from the cross between Yy and Yy?
    A. 2Yy-2yy
    B. 2Yy:yy:YY
    C. YY:2Yy:yy
    D. YY: Yy:2yy \n """,
    """4. Which of the following is NOT part of thecarbon cycle?
    A. Organic carbon
    B. Decomposition
    C. Nitrates formation
    D. Photosynthesis \n """,
    """5. I. Tissues II. System III. Cell IV. Organs Which of the above is the level of organization of a leaf?
    A. IV
    B. I.
    C. III.
    D. II. \n """,
    """6. In cellular respiration, energy is stored in the form of
    A. heat energy
    B. adenosine diphosphate
    C. adenosine monophosphate 
    D. adenosine triphosphate \n """,
    """7. The principal organ for the manufacture of food in autotrophy is the
    A. root hair
    B. growing root
    C. mature fruit
    D. green leaf \n """,
    """8. A disease that results from lack of iodine in the diet of humans is
    A. beriberi
    B. scurvy
    C. rickets
    D. goiter \n """,
    """9. The process whereby some organism with certain favourable features get establishedin an area is
    A. gene mutation
    B. dispersal
    C. overcrowding
    D. natural selection \n """,
    """10. The rise and fall of ocean water during the day is referred to as
    A. gravity
    B. a pull
    C. tide
    D. zone \n """,
    """11. Which of the following is a producer in an aquatic habitat?
    A. Nymphaea
    B. Dryopteris
    C. planarian
    D. Similium \n """,
    """12. The relationship that exist between a shark and Remora is
    A. parasitism
    B. commensalism
    C. saprophytism
    D. symbiosis \n """,
    """13. I. Tissue II. System III. Cell IV Organ The correct sequence of increasing level of complexity is
    A. IV-II-III
    B. I-II-III-IV
    C. IV-III-I-II
    D. III-I-IV-II \n """,
    """14. Which of the following is not an inheritable disease?
    A. Poliomyelitis
    B. Sickle-cell anaemia
    C. Mental illness
    D. Haemophilia \n """,
    """15. Which of the finger print types occur most frequently in the population of human beings 
    A. Double-loop
    B. Whorl
    C. Arch
    D. Loop \n """,
    """16. Beriberi results from a deficiency of
    A. vitamin A
    B. vitamin E.
    C. vitamin B
    D. vitamin C \n """,
    """17. Bacteria which add atmospheric nitrogen to the soil are
    A. putrefying bacteria
    B. nitrifying bacteria
    C. nitrogen fixing bacteria
    D. denitrifying bacteria \n """,
    """18. The spines of the hedgehog is an adaptive features for
    A. Courtship
    B. defence
    C. water conservation 
    D. obtaining food \n """,
    """19. The dental formula of carnivores is represented by 
    A. I 0⁄3, C 1⁄1, pm 4⁄4, m 2⁄3
    B. I 0⁄2, C 1⁄1, pm 4⁄4, m 2⁄4
    C. I 2⁄3, C 2⁄1, pm 3⁄4, m 2⁄3
    D. I 3, C 1⁄1, pm 4⁄4, m 2⁄2 \n """,
    """20. Which of the following instruments is used to measure temperature?
    A. Thermometer
    B. Hygrometer
    C. Anemometer
    D. Hydrometer \n """,
    """21. In human, puffiness and water retention in the body is a possible symptom of
    A. bladder malfunction
    B. poor digestion
    C. kidney malfunction
    D. obesity \n """,
    """22. The theory of evolution which postulates that all living organisms have a common ancestor was proposed by
    A. Linnaeus
    B. Darwin
    C. Lamarck
    D. Mendel \n """,
    """23. Mammals requires roughage in their food to
    A. provide energy
    B. slow down aging
    C. ease digestion
    D. prevent disease \n """,
    """24. Variation can occur among offspring of living organism because 
    A. seeds are produced by self-pollination
    B. zygotes are produced by cross fertilisation
    C. they are produced by binary fission
    D. they are produced without fertilisation \n """,
    """25. The most important biotic factors which affect plants and animals in the habitat are
    A. temperature and rainfall
    B. temperature and turbidity
    C. salinity and relative humidity
    D. rainfall and relative humidity \n """,
    """26. The lowest unit of classification is the
    A. Kingdom
    B. class
    C. phylum
    D. species \n """,
    """27. Two important process involved in the absorption and transport of materials in plants are
    A. flaccidity and turgidity
    B. diffusion and plasmolysis
    C. plasmolysis and capillarity
    D. osmosis and diffusion \n """,
    """28. A series of organism existing in an ecosystem through which energy is transformed can be referred to as
    A. food cycle
    B. food chain
    C. pyramid on numbers
    D. food web \n """,
    """29. The cell organelle solely responsible for respiration is the
    A. nucleus
    B. nucleolus
    C. endoplasmic reticulum
    D. mitochondrion \n """,
    """30. In which part of Nigeria are Mangrove swamps found?
    A. Chad Basin
    B. Niger Delta
    C. Benue Valley
    D. Mambilla Plateau \n """,
    """31. The breeding methods that are useful in selective breeding of animals and plants are 
    A. inbreeding and cross- breeding
    B. inbreeding and hetero-breeding
    C. inbreeding and out-breeding
    D. inbreeding and self-breeding \n """,
    """32. In a small unicellular organism, diffusion is sufficient for transport because
    A. the surface area to volume ratio is small
    B. they have lungs for diffusion
    C. materials have to move over long distance
    D. the surface area to volume ratio is large \n """,
    """33. The function of the spinal cord is to
    A. stand the body structure erect
    B. control involuntary actions
    C. transmit impulses to the brain
    D. regulates developmental changes \n """,
    """34. The first vertebrates to ventures out of water and lives on land are the
    A. Pisces
    B. Amphibians
    C. Reptiles
    D. Aves \n """,
    """35. Which of the following factors mostly determine the major biomes of the world.
    A. pressure and wind speed
    B. temperature and wind speed
    C. pressure and rainfall
    D. Temperature and rainfall \n """,
    """36. I. Strong winds II. high temperature III. Dry and porous soils. Which group of plants are specially adapted \n to grow under environmental conditions stated above?
    A. Thallophytic
    B. Mesophytes
    C. Xerophytes
    D. Hydrophytes \n """,
    """37. The lowest unit of a biogeographical plant species is
    A. micro flora
    B. macro fauna
    C. micro fauna
    D. macro flora \n """,
    """38. Which of the following is rich source of vitamin K?
    A. Tomato
    B. Guava
    C. Milk
    D. Onion \n """,
    """39. Severe diarrhea, dehydration and weakness are symptoms of 
    A. cholera
    B. chickenpox
    C. malaria
    D. yellow fever \n """,
    """40. A common characteristic found among the crustaceans is the possession of
    A. a pair of antennae
    B. a pair of walking legs on each segment
    C. four pairs of walking legs on the cephalothorax
    D. two pairs of antennae \n """,
    """41. In which of the following groups of invertebrates are flagella and cilia found
    A. annelids
    B. protists
    C. coelenterates
    D. Anthropods \n """,
    """42. Physiological variation in human population is evidence in the
    A. difference in the fingerprints
    B. physical appearance of individuals
    C. differences in height and weight
    D. ability to roll the tongue \n """,
    """43. In photosynthesis, oxygen is liberated during 
    A. conversion of energy 
    B. photolysis
    C. splitting of carbon (IV)oxide
    D. glycolysis \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "B"),
        Question(question_prompts[42], "D"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        biology_1988()

def Chemistry_1989():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
            """" 0. Which of the following statements is correct?
        A The average kinetic enemy of a gas is directly proportional to its  temperature
        B At constant temperature, the volume of a gas increases as the pressure increases.
        C The pressure of a gas is inversely proportional to its volume.
        D The temperature of gas is directly proportional to its volume.\n""",
        """" 1 Which are the correct IUPAC names for H–CO2CH3 and CH≡CH
        A Methyl methanoate and ethene
        B Metanoic acid and ethyne
        C Ethyl methanoate and ethyne
        D Methyl methanoate and ethyne \n""",
        """" 2 A solution X on mixing with AgNO3 solution, gives a white precipitate soluble in NH3. A solution Y, when\n added to X, also gives a white precipitate which is soluble on boiling. Solution Y contains
        A Ag+ ion
        B Pb2+ ion
        C Pb4+ ion
        D Zn2+ ion \n""",
        """" 3 Methane is a member of the homologous series called
        A alkenes
        B alcohols
        C esters
        D alkanes \n""",
        """"  4Which of the following bonds exists in crystalline ammonium chloride (NHCL)?
        A ionic covalent
        B ionic and co-ordinate
        C ionic, covalent and co- ordinate
        D covalent, co-ordinate and metallic \n""",
        """" 5 Some copper (II) sulphate pentahydrate (CuSO4 .5H2O), was heated at 120°C with the following results: Wt of \ncrucible =10.00 g; Wt of crucible +CuSO4.5H2O = 14.98g; Wt of crucible + residue = 13.54g. How many molecules of water of crystallization were lost? [H= 1, Cu = 63.5, O =16, S = 32]
        A 1
        B 2
        C 3
        D 4 \n""",
        """" 6 12.0g of a mixture of potassium carbonate and potassium chloride were dissolved in a 250cm3 standard flask. \n25cm3 of this solution required 40.00cm3 of 0.1M HCI neutralization. What is the percentage by weight of K2CO3 in the mixture (K = 39, O = 16, C = 12)
        A 60
        B 72
        C 82
        D 92 \n""",
        """" 7  Which of the following, groups of physical properties increases from left to right of the Periodic Table? \n 1. Ionization energy 2. Atomic radius 3. Electronegativity  4. Electron affinity
        A 1 and 2
        B 1, 2 and 3
        C 3 and 4
        D 1, 2, 3 and 4 \n""",
        """" 8 An element Z, contained 90% of 8Z 16 and 10% of 8Z 18 . its relative atomic mass is
        A 16.0
        B 16.2
        C 17.0
        D 17.8 \n""",
        """" 9 What are the possible oxidation numbers for an element if its atomic number is 17?
        A -1 and 7
        B -1 and 6
        C -3 and 5
        D -2 and 6 \n""",
        """" 10 How many valence electrons are contained in the element represented by 31P15?
        A 3
        B 5
        C 15
        D 31 \n""",
        """" 11 10.0 dm3 of air containingH2S as an impurity was passed through a solution of Pb(NO3)2 until all the H2S \n had reacted. The precipitate of PbS was found to weigh 5.02 g. According to the equation:Pb(NO3)2 + H2S → PbS + 2HNO3 the percentage by volume of hydrogen sulphide in the air is
        A 50.2
        B 47.0
        C 4.70
        D 0.47 \n""",
        """" 12 A quantity of air was passed through a weighed amount of alkaline pyrogallol. An increase in the weight \n of the pyrogallol would result from the absorption of
        A nitrogen
        B neon 
        C argon
        D oxygen \n""",
        """" 13 Water for town supply is chlorinated to make it free from
        A bad odour
        B bacteria
        C temporary hardness
        D permanent hardness \n""",
        """" 14. 4.0 g of sodium hydroxide in 250cm3 of solution contains
        A. 0.40 moles per dm3
        B. 0.10 moles per dm3
        C. 0.04 moles per dm3
        D. 0.02 moles per dm3 \n""",
        """" 15 A major effect of oil pollution in coastal waters is the
        A destruction of marine life
        B desalination of the water
        C increase in the acidity of the water
        D detoxification of the water \n""",
        """" 16 In general, an increase in temperature increases the solubility of a solute in water because
        A more solute molecules collide with each other
        B most solutes dissolve with the evolution of heat
        C more solute molecules dissociate at higher temperatures
        D most solutes dissolve with absorption of heat.\n""",
        """" 17 The relatively high boiling points of alkanols are due to
        A ionic bonding
        B aromatic character
        C covalent bonding
        D hydrogen bonding. \n""",
        """" 17 Given that 15.00cm3 of H was required to completely neutralize 25.00cm3 of 0.125 mol dm3 NaOH, calculate the molar concentration of the acid solution
        A 0.925 mol dm3 
        B 0.156 mol dm3
        C 0.104 mol dm3
        D 0.023 mol dm3 \n""",
        """" 18 What volume of 0.1 mol dm3 solution of tetraoxosulphate (VI) acid would be needed to dissolve 2.86g of sodium trioxocarbonate (IV) decahydrate crystals?[H = 1, C = 12, O = 16, S= 32,Na 23].
        A 20cm3
        B 40cm3
        C 80cm3
        D 100cm3 \n""",
        """" 19 The solution with the lowest pH value is
        A 5 ml of  ⁄10 HCL
        B 10 ml of  ⁄10 HCL
        C 15 ml of  ⁄5 HCL
        D 20 ml of  ⁄8 HCL \n""",
        """" 20 In which order are the  following salts sensitive to light? 
        A Agl > AgCl > AgBr 
        B AgCl> Agl > AgBr
        C AgBr > AgCI > Agl
        D AgCI > AgBr > Agl \n""",
        """" 21 A metal m displaces Zinc from Zinc chloride solution. This shows that
        A M is more electronegative than Zinc
        B Zinc is above hydrogen in the series.
        C M is more electropositive than zinc.
        D electrons flow from zinc to m. \n""",
        """" 22 Steam changes the colour of anhydrous cobalt (II) chloride from
        A blue to pink
        B white to red
        C white to green
        D blue to white \n""",
        """" 23 When at equilibrium, which of the reactions below will shift to the right if the pressure is increased and the temperature is kept constant?
        A 2SO3(g) === 2SO2(g) + O
        B 2CO2(g) === 2CO(g) + O
        C 2H2(g) + O2(g)=== 2H
        D 2NO(g)=== N2(g) + O \n""",
        """" 24 2CO(g)+ O2(g) → 2Co2(g) Given that ΔH [CO] is -110.4kJmol-1 and ΔH [CO] is -393.0kJmol-1, the energy change for the reaction above is
        A -503.7 kJ
        B -282.6 kJ
        C +282.6 kJ
        D +503.7 kJ \n""",
        """" 25 Which of these properties gives a solid its definite shape?
        A Strong intermolecular attraction
        B High melting point
        C High boiling point
        D Weak intermolecular attraction \n""",
        """" 26 When a crystal was added to the clear solution of its salt, the crystal did not dissolve and the solution remained unchanged. This showed that the solution was
        A supersaturated
        B concentrated
        C unsaturated
        D saturated \n""",
        """" 27 If the electron configuration of an element is 1s2 2s2 2p5 , how many unpaired electrons are there?
        A 2
        B 5
        C 1
        D 4 \n""",
        """" 28 The substance that is used in the steel industry for the removal of carbon, sulphur and phosphorus impurities from pig iron is
        A oxygen
        B chlorine 
        C nitrogen
        D hydrogen \n""",
        """" 29 Hydrogen sulphide gas can act as
        A an oxidizing agent
        B a dehydrating agent
        C a bleaching agent
        D a precipitating agent. \n""",
        """" 30 Which of the following is used as a rocket fuel?
        A HNO3
        B CH3COOH
        C H2SO4
        D HCI. \n""",
        """" 31 The bleaching action of chlorine is effective due to the presence of
        A Hydrogen chloride
        B Water
        C Air
        D Oxygen \n""",
        """" 32 Mineral acids are usually added to commercial hydrogen peroxide to
        A Oxidize it
        B decompose it
        C minimize its decomposition
        D reduce it to water and oxygen.\n""",
        """" 33 Aluminium containers are frequently used to transport trioxonitrate (v) acid because aluminium
        A has a low density
        B does not react with the acid
        C does not corrode
        D has a silvery - white appearance \n""",
        """" 34 Ethyne is passed through a hot tube containing organo-nickel catalyst to produce
        A Isoprene
        B polythene
        C ethanol
        D benzene \n""",
        """" 35 The process of converting starch to ethanol is
        A cracking
        B distillation
        C fermentation
        D oxidation\n""",
        """" 36 An endothermic reaction is one during which heat is ____and can be represented by the symbol____. Which of the following combinations can be used accurately to complete the above definition?
        A liberated -ΔH
        B liberated +ΔH
        C absorbed -ΔH
        D absorbed +ΔH \n""",
        """" 37 Consider the following exothermic reaction 2SO2(g) + O2(g) = 2SO3(g) . If the temperature of the reaction is reduced from 800⁰C to 500°C, and no other change takes place, then
        A the reaction rate increases 
        B concentration of SO decreases
        C concentration of SO2 increases
        D SO2 gas becomes unreactive \n""",
    ]
    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print(" you are doing well!!")
                score += 1
            else:
                print("Wow! you can do more to imporve your scores guy!")

        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Chemistry_1989()

def English_1990():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
            """0 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the \n information conveyed in the sentence 36. Ramatu expressed her feelings in no uncertain terms 
        (a) she expressed it feebly and sickly 
        (b) she expresses it quietly and cautiously 
        (c) she expressed it secretly and courageously 
        (d) she expressed it clearly and strongly \n""",
        """1 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information \n conveyed in the sentence  37. Usman needs to get his act together if he wants to pass the examination 
        (a) he needs to put on his stage costume  
        (b) he needs to be fast when writing the examination 
        (c) he needs to organise himself
        (d) he needs to put all points down in the examination \n""",
        """2 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n  conveyed in the sentence  38. As the drama unfolded, Olatinuke was advised to keep her shirt on  
        (a) she was advised to stay calm
        (b) she was advised to commit herself 
        (c) she was advised to join the club 
        (d) she was advised to wear her shirt \n""",
        """3 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information \n conveyed in the sentence  39. The team's poor performance at the tournament plumbed the depths of horror. 
        (a) the team's performance was rewarded 
        (b) the team's performance took them to the next round 
        (c) the team's performance was enjoyed by all  
        (d) the team's performance was full of disappointment \n""",
        """4 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information \n conveyed in the sentence  40. He is a clinging child 
        (a) He is a bully 
        (b) He likes to cling with his sister
        (c) He is possessive 
        (d) He is a handsome young man \n""",
        """5 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n  conveyed in the sentence 41. You need to brush up on your Spanish 
        (a) you need a brush from Spain
        (b) you need to study the history of Spain 
        (c) you need to learn to play with a Spaniard 
        (d) you need to improve your skills.\n""",
        """6 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  42. Tolu and Chinedu live in each other's pockets 
        (a) They are long-term business partners 
        (b) They are very close to each other
        (c) They blackmail each other 
        (d) They steal from each other \n""",
        """7 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  43. Zinana'a examination result was not unfavourable 
        (a) She failed her examination
        (b) Her result could not earn her admission 
        (c) She was successful in the examination
        (d) she was deceitful \n""",
        """8 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n  conveyed in the sentence  44. can't wait to become a mother. 'the new bride declared 
        (a) she sees motherhood as a burden 
        (b) she will be patient as a mother 
        (c) She is not keen on becoming a mother 
        (d) She is excited about motherhood.\n""",
        """9 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information \n conveyed in the sentence 45. Amaka would pass for beauty queen 
        (a) she was acting as a beauty queen  
        (b) she would pass the drink to the queen who is sitting next to her 
        (c) she would be accepted by all as a beauty queen 
        (d) she walked past the beauty queen \n""",
        """10 For these questions, choose the option opposite in meaning to the word or phrase in italics 46. The \n relationship between the couple has been frosty 
        (a) amenable 
        (b) fraudulent 
        (c) frugal 
        (d) cordial \n""",
        """11 For these questions, choose the option opposite in meaning to the word or phrase in italics 47. \n The dressmaker unpicked the seam of the shirt 
        (a) tore up 
        (b) sewed up 
        (c) threaded
        (d) picked up \n""",
        """12 For these questions, choose the option opposite in meaning to the word or phrase in italics 48. \n Some of my neighbours have an antipathy to dogs 
        (a) enmity towards 
        (b) alarm for 
        (c) acronym 
        (d) affection for \n""",
        """13 For these questions, choose the option opposite in meaning to the word or phrase in italics 49. \n Chibuzor gave a curt nod and walked away 
        (a) rude 
        (b) polite 
        (c) gentle 
        (d) shocking \n""",
        """14 For these questions, choose the option opposite in meaning to the word or phrase in italics 50. \n The girl took a cursory glance at the letter and hid it 
        (a) brief 
        (b) sententious 
        (c) lasting 
        (d) concise \n""",
        """15 For these questions, choose the option opposite in meaning to the word or phrase in italics 51. \n The accused was eventually convicted 
        (a) initially 
        (b) finally  
        (c) subsequently 
        (d) consequently \n""",
        """16 For these questions, choose the option opposite in meaning to the word or phrase in italics 52. My niece\n  has an unquenchable thirst for adventure stories 
        (a) an illegitimate 
        (b) a spurious 
        (c) an inextinguishable 
        (d) a reduced \n""",
        """17 For these questions, choose the option opposite in meaning to the word or phrase in italics 53.\n  Musa is a gifted but erratic player 
        (a) regular 
        (b) strong 
        (c) unstable 
        (d) unpredictable \n""",
        """18 For these questions, choose the option opposite in meaning to the word or phrase in italics 54. The \n testimony of the witness was vague
        (a) real 
        (b) factual 
        (c) true 
        (d) clear \n""",
        """19 For these questions, choose the option opposite in meaning to the word or phrase in italics  55. As \n a student, Isa tried communal living for a few years 
        (a) shared 
        (b) private 
        (c) collective 
        (d) general \n""",
        """20 For these questions, choose the option opposite in meaning to the word or phrase in italics 56.\n  The lamb is a feeble little animal 
        (a) fat
        (b) weak 
        (c) loving 
        (d) quite \n""",
        """21 For these questions, choose the nearest in meaning to the word or phrase in italics 57. The chairman\n  admires incessant meetings 
        (a) planned 
        (b) unusual 
        (c) irregular
        (d) constant \n""",
        """22 For these questions, choose the nearest in meaning to the word or phrase in italics  58. The exhibition\n  was an eye opener to all 
        (a) dispatch 
        (b) examination 
        (c) style 
        (d) display \n""",
        """23 For these questions, choose the nearest in meaning to the word or phrase in italics  59. The first round\n  of the tournament was a doddle 
        (a) exasperating 
        (b) balanced 
        (c) dodgy
        (d) easy \n""",
        """24 For these questions, choose the nearest in meaning to the word or phrase in italics  60. As a journalist,\n  Bala has always had a nose for stories 
        (a) a command 
        (b) cynical statement 
        (c) soft comment 
        (d) an instinct \n""",
        """25 For these questions, choose the nearest in meaning to the word or phrase in italics  61. The actress \n screamed when she noticed an object behind her 
        (a) wailed 
        (b) protested 
        (c) waded in 
        (d) stormed out \n""",
        """26 For these questions, choose the nearest in meaning to the word or phrase in italics  62. Today's weather \n is favourable for a game of tennis 
        (a) impartial 
        (b) abnormal 
        (c) encouraging 
        (d) disapproving \n""",
        """27 For these questions, choose the nearest in meaning to the word or phrase in italics  63. All the candidates \n looked aghast at the first reading of the questions 
        (a) fulfilled 
        (b) dismayed 
        (c) satisfied 
        (d) again \n""",
        """28 For these questions, choose the nearest in meaning to the word or phrase in italics  64. \n I am tired of your eternal argument 
        (a) open 
        (b) strong 
        (c) constant 
        (d) useless \n""",
        """29 For these questions, choose the nearest in meaning to the word or phrase in italics  65. Joke gave\n  Muhammad a jaunty smile 
        (a) frightful 
        (B) cheerful 
        (c) discouraging 
        (d) Inviting \n""",
        """30 From questions 65 to 85, choose the option that best completes the gap(s) 66. You live in the city now, __ ? 
        (a) are you
        (b) don't you 
        (c) didn't you 
        (d) haven't you \n""",
        """31 From questions 65 to 85, choose the option that best completes the gap(s) 67. Concrete is made of __ 
        (a) sand and cement 
        (b) a sand and a cement 
        (c) sand and a cement 
        (d) a sand and cement \n""",
        """32 From questions 65 to 85, choose the option that best completes the gap(s) 68. Suana___ that hexagons had\n  five sides, but later he knew they were six-sided figures. 
        (a) would have believed 
        (b) had believed 
        (c) believes 
        (d) has believed \n""",
        """33 From questions 65 to 85, choose the option that best completes the gap(s) 69. The___ to the fallen heroes\n  was erected at the market square 
        (a) exhibition 
        (b) monument 
        (c) myth
        (d) picture \n""",
        """34 From questions 65 to 85, choose the option that best completes the gap(s) 70. The Flying Eagles of Nigeria \n couldn't have won the match if they hadn't prepared well,___? 
        (a) can't they 
        (b) couldn't they 
        (c) could they 
        (d) can they \n""",
        """35 From questions 65 to 85, choose the option that best completes the gap(s) 71. They all gathered to exhume\n  the___musician's corpse for examination 
        (a) posthumous 
        (b) post-mortem 
        (c) post-natal  
        (d) orthopaedic
        (b) post-mortem \n""",
        """36 From questions 65 to 85, choose the option that best completes the gap(s) 72. I have been doing this exercise___ 
        (a) for five minutes 
        (b) five minutes ago 
        (c) since five minutes 
        (d) during five minutes \n""",
        """37 From questions 65 to 85, choose the option that best completes the gap(s) 73. \n loyede always sleeps like a baby,___ ?
        (a) does he 
        (b) could he 
        (c) doesn't he 
        (d) did he \n""",
        """38 From questions 65 to 85, choose the option that best completes the gap(s) 74. The man was given degree \n despite the fact that he did not attend a___ university 
        (a an honorary 
        (b) an honourable 
        (c) a ceremonial 
        (d) a ceremonious \n""",
        """39 From questions 65 to 85, choose the option that best completes the gap(s) 75. My father has just bought___ 
        (a) a peugeot brand new car 
        (b) a car brand new peugeot 
        (c) a new brand peugeot car 
        (d) a brand new peugeot \n""",
        """40 From questions 65 to 85, choose the option that best completes the gap(s) 76. The university is a \n corporate body made___ different colleges 
        (a) in with 
        (b) of with 
        (c) up of 
        (d) up from \n""",
        """41 From questions 65 to 85, choose the option that best completes the gap(s) 77. The secretary hadn't___ \n money left. 
        (a) any 
        (b) anything 
        (c) none 
        (d) no \n""",
        """42 From questions 65 to 85, choose the option that best completes the gap(s) 78. The King was recognised___ \n the scar on his face. 
        (a) with 
        (b) to 
        (c) by 
        (d) for \n""",
        """43 From questions 65 to 85, choose the option that best completes the gap(s) 79. Nkiru has lots of friends, \n but I have___
        (a) only a little 
        (b) little 
        (c) only a few 
        (d) few \n""",
        """44 From questions 65 to 85, choose the option that best completes the gap(s) 80. The HOD says she considers \n her degree certificate___ than as a prize through labour
        (a) rather as a gift of God 
        (b) rather God as a gift 
        (c) as a gift rather of God 
        (d) as a rather gift of God \n""",
        """45 From questions 65 to 85, choose the option that best completes the gap(s) 81. Mr Ojo instructed his son to\n  replace the faulty___ tube 
        (a) flurescent 
        (b) flourescent 
        (c) fluorescent 
        (d) florescent \n""",
        """46 From questions 65 to 85, choose the option that best completes the gap(s) 82. The employer, not the \n salesmen___responsible for the loss 
        (a) have been 
        (b) was 
        (c) were 
        (d) will be \n""",
        """47 From questions 65 to 85, choose the option that best completes the gap(s) 83. She was___ as anyone could have had 
        (a) as patient as teacher 
        (b) as a patient a teacher
        (c) as patient teacher 
        (d) a patient a teacher \n""",
        """48 From questions 65 to 85, choose the option that best completes the gap(s) 84. There was a serious___ \n between the new couple over feeding allowance 
        (a) arguement
        (b) argeument 
        (c) arguement 
        (d) argument \n""",
        """49 From questions 65 to 85, choose the option that best completes the gap(s) 85. They thought Musa___ agree\n if they altered some of the conditions 
        (a) can 
        (b) may
        (c) might  
        (d) ought \n""",
        """50 For these questions, choose the option that has the same sound as the one represented by the letter(s) \n underlined 86. WAIter 
        (a) flavour 
        (b) cite 
        (c) road 
        (d) hair \n""",
        """51 For these questions, choose the option that has the same sound as the one represented by the letter(s) underlined 87. FlEE
        (a) field 
        (b) skate 
        (c) faith 
        (d) rid \n""",
        """52 For these questions, choose the option that has the same sound as the one represented by the letter(s)\n  underlined 88. PALm 
        (a) florid 
        (b) ranch 
        (c) blunt 
        (d) lunch \n""",
        """53 For these questions, choose the option that has the same sound as the one represented by the letter(s)\n  underlined 89. Phantom  
        (a) physics 
        (b) pew 
        (c) phew 
        (d) party \n""",
        """54 AFor these questions, choose the option that has the same sound as the one represented by the letter(s)\n underlined 90. Chest 
        (a) fixture 
        (b) school 
        (c) charisma
        (d) mass \n""",
        """55 For these questions, choose the option that has the same sound as the one represented by the letter(s)\n  underlined 91. Epitaph 
        (a) pneumonia 
        (b) fan 
        (c) paper
        (d) pseudo \n""",
        """56 For these questions, choose the option that rhymes with the given word 92. Ever 
        (a) never 
        (b) heavier 
        (c) fever 
        (d) favour \n""",
        """57 For these questions, choose the option that rhymes with the given word 93. Cable 
        (a) bible 
        (b) mabel 
        (c) able 
        (d) marble \n""",
        """58 For these questions, choose the option that rhymes with the given word 94. Mail 
        (a) bale 
        (b) slate 
        (c) girl 
        (d) galle \n""",
        """59 For these questions, choose the appropriate stress pattern from the options, the stress syllables are \n written in capital letter(s) 95. Advantages 
        (a) advantaGES 
        (b) adVANtages 
        (c) ADvantages 
        (d) advanTAges \n""",
        """60 For these questions, choose the appropriate stress pattern from the options, the stress syllables are written \n in capital letter(s)  96. Intentional 
        (a) inTENtional 
        (b) INtentional
        (c) intentionAL 
        (d) intentioNAL \n""",
        """61 For this question, choose the option that is stressed on the first syllable 97. 
        (a) guitar 
        (b) guilty 
        (c) confuse 
        (d) relief \n""",
        """62 In the question, the words in capital letter has the emphatic stress. Choose the option to which the given\n  sentence relates. 98. I left my bag on the TABLE
        (a) Is the bag left under the table?
        (b) Did I leave the shoe on the table?
        (c) Who left the bag on the table?
        (d) Where did I leave the bag? \n""",
        """63 In the question, the words in capital letter has the emphatic stress. Choose the option to which the given \n sentence relates.  99. Kanu can play FOOTBALL
        (a) Who can play football?
        (b) What can Kanu play?
        (c) What can Kanu do with football?
        (d) Why should Kanu play football? \n""",
        """64 In the question, the words in capital letter has the emphatic stress. Choose the option to which the given \n sentence relates.  100. Aisha plays TENNIS always
        (a) Who plays tennis always?
        (b) Does Aisha watch tennisalways?
        (c) What does Aisha play always?
        (d) When does Aisha play tennis? \n""",

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "D"),
        Question(question_prompts[40], "C"),
        Question(question_prompts[41], "C"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "D"),
        Question(question_prompts[44], "B"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "B"),
        Question(question_prompts[47], "B"),
        Question(question_prompts[48], "D"),
        Question(question_prompts[49], "C"),
        Question(question_prompts[50], "A"),
        Question(question_prompts[51], "A"),
        Question(question_prompts[52], "B"),
        Question(question_prompts[53], "A"),
        Question(question_prompts[54], "D"),
        Question(question_prompts[55], "B"),
        Question(question_prompts[56], "A"),
        Question(question_prompts[57], "C"),
        Question(question_prompts[58], "A"),
        Question(question_prompts[59], "B"),
        Question(question_prompts[60], "A"),
        Question(question_prompts[61], "D"),
        Question(question_prompts[62], "D"),
        Question(question_prompts[63], "B"),
        Question(question_prompts[64], "C"),
    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("Wow ! you got it and do more to get more point right")
                score += 1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        English_1990()

def Physics_1991():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
            """0. A piece of rubber 10cm long stretches 6mm when a load of 100N is hung from it. What is the strain?  
        A. 6 X 10-3 
        B. 6 
        C. 60 
        D. 6.0 X 10-3 \n""",
        """1.  A body of mass 6kg rests on an inclined plane. The normal reaction R and the limiting \nfrictional force is F as shown in the diagram (Fig. 2). If F is 30N and g=10ms-2, then the angle of inclination Ө is  
        A. 15° 
        B. 60° 
        C. 45° 
        D. 30° \n""",
        """2. The speed of light in air is 3.0 x 103ms-1. Its speed in glass having a refractive index of 1.65 is  
        A. 1.82 x 108 ms-1 
        B. 3.00 x 108 ms-1 
        C. 4.95 x 108 ms-1 
        D. 1.65 x 108 ms-1 \n""",
        """3. Longitudinal waves do not exhibit 
        A. refraction 
        B. polarization 
        C. diffraction 
        D. reflection \n""",
        """4. A device that converts sound energy into electrical energy is 
        A. the horn of a motor car 
        B. the telephone earpiece 
        C. a loudspeaker 
        D. a microphone.\n""",
        """5. A good calorimeter should be of 
        A. low specific heat capacity andlow heat conductivity 
        B. high specific heat capacity and low heat conductivity 
        C. high specific heat capacity and low heat conductivity 
        D. low specific heat capacity and high heat conductivity.  \n""",
        """6. Which of the following is most strongly deflected by a magnetic field? 
        A. β-particles 
        B. χ-particles 
        C. γ-rays. 
        D. χ-rays \n""",
        """7. If a beaker is filled with water, it is observed that the surface of the water is not\n horizontal at the glass-water interface. This behaviour is due to  
        A. friction 
        B. surface tension 
        C. viscosity 
        D. evaporation \n""",
        """8. A dynamo primarily conducts 
        A. potential energy into kinetic energy 
        B. electrical energy into kinetic energy 
        C. mechanical energy into electrical energy 
        D. kinetic energy into potential energy  \n""",
        """9. A particle is injected perpendicularly into an electric field. It travels along a curved path \nas depicted in the figure 3. The particle is?
        A. gamma ray 
        B. a proton 
        C. a neutron 
        D. an electron \n""",
        """10. A calibrated potentiometer is used to measure the e.m.f. of a cell because the  
        A. internal resistance of a cell is small compared with that of the potentiometer 
        B. potentiometer takes no current from the cell 
        C. potentiometer has a linear scale 
        D. resistance of the potentiometer is less than that of a voltmeter that of the potentiometer\n""",
        """11. Which of the following is a vector? 
        A. Electric charge 
        B. Electric potential difference 
        C. Electric field 
        D. Electrical capacitance. \n""",
        """12. The photocell works on the principle of the  
        A. voltaic cell 
        B. photographic plate 
        C. emission of protons by incident electrons 
        D. emission of electrons by incident radiation \n""",
        """13. When an atom loses or gains a charge, it becomes  
        A. an ion 
        B. an electron 
        C. a neutron 
        D. a proton \n""",
        """14. Which of the following characteristics of a wave is used in the measurement of the\n depth of the sea? 
        A. Diffraction 
        B. Reflection 
        C. Refraction 
        D. Interference \n""",
        """15. Which of the following are produced after a nuclear fusion process?I. One heavy nucleus \nII. Neutrons III. Protons IV. Energy  
        A. I and II 
        B. II and III 
        C. I and IV 
        D. II and IV. \n""",
        """16. Two similar kettles containing equal masses of boiling water are placed on a table. If the surface of\n one is highly polished and the surface of the other is covered with soot, which of the following observations is correct? 
        A. The two kettles will cool down at the same rate 
        B. The polished kettle cools down more quickly by conduction 
        C. The kettle covered with soot cools down more quickly because it is a good radiator of heat 
        D. The kettle covered with soot cools down more quickly by the process ofheat convection. \n""",
        """17. Total eclipse of the sun occurs when the  
        A. moon is between the sun and the earth 
        B. sun is between the moon and the earth 
        C. the earth is between the moon and the sun 
        D. ozone layer is threatened. \n""",
        """18. Which of the following pairs of colours gives the widest separation in the spectrum of white light? 
        A. Green and Yellow 
        B. Red and violet 
        C. Red and indigo 
        D. Yellow and violet. \n""",
        """19. Which of the following with respect to a body performing simple harmonic motion are in phase? 
        A. Displacement and velocity of the body 
        B. Displacement and force on the body 
        C. Velocity and acceleration of the body 
        D. Force acting on the body and the acceleration \n""",
        """20. A uniform metre rule weighing 0.5.V is to be pivoted on a knifeedge at the 30cm-mark. Where will a force\n of 2N be placed from the pivot to balance the metre 
        rule? 
        A. 95cm 
        B. 5cm 
        C. 20cm 
        D. 25cm \n""",
        """21. A solid weighs 10.0N in air, 6.0N when fully immersed in water and 7.0N when fully immersed in a certain\n liquid X.  Calculate the relative density of the liquid. 
        A. 3/4 
        B. 4/3 
        C. 5/3 
        D. 7/10 \n""",
        """22. the process of energy production in the sun is  
        A. nuclear fission 
        B. nuclear fusion 
        C. electron collision 
        D. radioactivity decay \n""",
        """23. the particle is responsible fornuclear fusion in a nuclear reactor is  
        A. electron 
        B. Photon 
        C. proton. 
        D. Neutron \n""",
        """24. if the uncertainty in the measurement of the position of a particle is 5×10-10m, the uncertainty in the \n momentum of the particle is? [h=6.6 ×10-34J]
        A. 1.32 × 10-24 Ns 
        B. 3.30 × 10-44 Ns 
        C. 1.32 × 10-44 Ns 
        D. 3.30 × 10-24 Ns  \n""",
        """25. The change in volume when 450kg of ice is completely melted is  [density of ice =900kgm-3 Densityof \nwater=1000 kgm-3]  
        A. 0.50m 
        B. 0.45m3 
        C. 4.50m3 
        D. 0.05m3 \n""",
        """26. When impurities are added to semiconductor  
        A. decreases 
        B. increases then decreases 
        C. decreases 
        D. remains constant \n""",
        """27 A. photo emission 
        B. thermionic emission 
        C. photon emission 
        D. electron emission \n""",
        """28. The production of pure spectrum could easily be achieved using a 
        A. Triangular prism only 
        B. Triangular prism with two concave lens 
        C. Glass prism with a pin 
        D. Triangular prism with two convex lens. \n""",
        """29. A short chain is something attached to the back of a petrol tanker to 
        A. Conduct excess charges to the earth 
        B. Ensure the balancing of the tanker 
        C. Caution the driver when over speeding 
        D. Generate more friction \n""",
        """30. A perfect emitter or absorber of radiant energy is a 
        A. White body 
        B. Red body 
        C. Conductor 
        D. Black body \n""",
        """31. Six identical cells, each of e.m.f 2V are connected as shown above. The effective e.m.f of the cell is  
        A. 4V 
        B. 0V 
        C. 6V 
        D. 12V \n""",
        """32. If a pump is capable of lifting 5000Kg of water through a vertical height of 60 m in 50 mins, \nthe power of the pump is   
        A. 2.5×105Js-1 
        B. 3.3 × 103Js-1 
        C. 2.5 ×104Js-1 
        D. 3.3 × 102Js-1 \n""",
        """33. The distance between two successive crest of a wave is 15 cm and the velocity is 300ms-1.Calculate\n the frequency. 
        A. 4.5 × 105 Hz 
        B. 4.5 × 102 Hz 
        C. 2.0 × 103 Hz 
        D. 2.0 × 102 Hz \n""",
        """34. An electric lamp marked 240V, 60 Watts is left to operate for an hour. How much energy is generated by\n the filament?  
        A. 3.86 × 105 J 
        B. 2.16 × 105 J 
        C. 1.80 × 104 J 
        D. 3.56 × 105 J \n""",
        """35 . In comparing the camera and human eye, the film of the camera functions as the  
        A. Iris 
        B. Pupil 
        C. Retina 
        D. Cornea \n""",
    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1991()

def Physics_1992():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
            """ 0. When a brick is taken from the earth’s surface to the moon, its mass 
        A. remains constant 
        B. reduces. 
        C. increases. 
        D. becomes zero. \n""",
        """1. The resultant of two forces is 50N. If the forces are perpendicular to each other and one of them \n makes an angle of 30° with the resultant, find  its magnitude. 
        A. 100.0N 
        B. 57.7N 
        C. 43.3 N 
        D. 25.0N \n""",
        """ 2 The pair pf physical quantities that are scalar only are  
        A. volume and area 
        B. moment and momentum 
        C. length and displacement. 
        D. impulse and time. \n""",
        """ 3 A simple pendulum of length 0.4m has a period of 2s. What is the period a similar pendulum of length 0.8m\n at the same place? 
        A. 8s 
        B. 4s 
        C. 2√2  
        D. √2 \n""",
        """4  A train with an initial velocity of 20m −1 is subjected to a uniform deceleration of 2 −2. \n The time required to bring the train to a complete halt   is 
        A. 5s. 
        B. 10s. 
        C. 20s. 
        D. 40s. \n""",
        """4 Calculate the apparent weight loss of a man weighing 70kg in an elevator moving downwards with \n an acceleration of 1.5m −2.[ g ≈10m −2]  
        A. 686N. 
        B. 595N. 
        C. 581N. 
        D. 1105N \n""",
        """5 A piece of cork floats in a liquid. What fraction of its volume will be immersed in the liquid?\n  [Density of the cork = 0.25 x 103  −3, density of  the liquid = 1.25 x 103kg −3] 
        A. 0.8. 
        B. 0.5. 
        C. 0.2. 
        D. 0.1. \n""",
        """6 An object is moving with a velocity of 5m −1. At what height must a similar body be situated to have a\n  potential energy equal in value with kinetic  energy of the moving body? 
        A. 25.0m 
        B. 20.0m. 
        C. 1.3m. 
        D. 1.0m.  \n""",
        """7 If a pump is capable of lifting 5000kg of water through a vertical height of 60 m in 15 min,\n  the power of the pump is 
        A. 2.5 x 105Js −1 
        B. 2.5 x 104Js −1 
        C. 3.3 x 103Js−1 
        D. 3.3 x 102Js −1 \n""",
        """8 The coefficient of friction between two perfectly smooth surface is 
        A. infinity. 
        B. one 
        C. half. 
        D. zero. \n""",
        """9 What effort will a machine of efficiency 90% apply to lift a load of 180N if its effort arm is twice\n  as long as its load arm?  
        A. 80N 
        B. 90N. 
        C. 100N. 
        D. 120N. \n""",
        """10 Calculate the work done when a force of 20N stretches a spring by 50mm. 
        A. 0.5J. 
        B. 1.5J. 
        C. 2.0J. 
        D. 2.5J.\n""",
        """11 At what depth below the sealevel would one experience a change of pressure equal to one atmosphere? \n [Density of sea water = 1013k −3 one atmosphere = 0.01 x 105 N −2 g=10m −2] 
        A. 0.1 m. 
        B. 1.0m. 
        C. 10.0m. 
        D. 100.0m \n""",
        """12 What volume of alcohol will have same mass as 4.2 −3 of petrol? 
        A. 0.8 3. 
        B. 1.4 3. 
        C. 3.6 3. 
        D. 4.9 3. \n""",
        """13 Calculate the length which corresponds to a temperature of 20°C if the used steam points of an\n  ungraduated thermometer are 400 mm apart. 
        A. 20mm. 
        B. 30mm. 
        C. 60mm 
        D. 80mm. \n""",
        """14 A wire of length 100.0m at 30°C has linear expansivity of 2 x 10−5 −1. Calculate the length \n of the wire at a temperature of 10°C.  
        A. 100.08m. 
        B. 100.04m. 
        C. 99.96m 
        D. 99.92m. \n""",
        """15 A gas at a pressure of 105  −2 expands from 0.6 −3 to 1.2 3 at constant temperature, the work done is 
        A. 7.0 x 106 . 
        B. 6.0 x 106 . 
        C. 6.0 x 105J. 
        D. 6.0 x 104 . \n""",
        """16 Two liquids X and Y having the same mass are supplied with the same quantity of heat.If the \n temperature rise in X is twice that of Y, the ratio of specific heat capacity of V to that of Y is 
        A. 2:1. 
        B. 1:2. 
        C. 4:1. 
        D. 1:4.\n""",
        """17 Foods cook quicker in salt water than in pure water because of the effect of 
        A.dissolved substances on the boiling point. 
        B. atmospheric pressure on the boiling point. 
        C. food nutrients on the thermal energy. 
        D. salts on the thermal conductivity of water. \n""",
        """18 Steam from boiling water causes more damage on the skin that does boiling water because 
        A. water has a high specific heat. 
        B. steam has latent heat of fusion. 
        C. the steam is at higher temperature than the water. 
        D. steam brings heat more easily by convection. \n""",
        """19 What will happen to the boiling point of pure water when it is heated in a place 30m below sea level? 
        A. It will be more than 100°C. 
        B. It will be less than 100°C. 
        C. It will still be at 100°C. 
        D. It will be fluctuating. \n""",
        """20 The rise or fall of liquid in a narrow tube is because of the ____?
        A. viscosity of the liquid. 
        B. surface tension of the liquid. 
        C. friction between the walls of the tube and the liquid. 
        D. osmotic pressure of the liquid. \n""",
        """21. The mechanism of heat  transfer from one point to another  through the vibration of the \n  molecules of the medium is  
        A. convection. 
        B. conduction 
        C. radiation 
        D. diffusion \n""",
        """22. A wave travels through  stretched strings is known as  
        A. electromagnetic wave. 
        B. micro wave. 
        C. mechanical wave. 
        D. seismic wave. \n""",
        """23. A transverse wave and a  longitudinal wave travelling in the  same direction in a \n medium differ  essentially in their 
        A. frequency. 
        B. amplitude. 
        C. direction of vibration of the  particles of the medium 
        D. period of vibration of the  particles of the medium. \n""",
        """24. What is the velocity of sound  at 100°C, if the velocity of sound at 0°C is 340m −1? 
        A. 497m −1 
        B. 440m −1 
        C. 397m −1 
        D. 240m −1 \n""",
        """ 25. If a sonometer has a  fundamental frequency of 450Hz,  what is the frequency of the fifth  overtone? 
        A.2700Hz 
        B. 456Hz 
        C.44Hz 
        D.75Hz \n""",
        """26. A man 1.5m tall is standing  3m in front of a pinhole camera  whose distance between the hole  \n and the screen is 0.1m. What is  the height of the image of the  man on the screen?  
        A. 0.05m 
        B. 0.15m. 
        C. 0.30m. 
        D. 1.00m. \n""",
        """27. A ray of light passing through the centre of curvature of a  concave mirror is reflected \n by the  mirror at 
        A. 0°. 
        B. 45°. 
        C. 90°. 
        D. 180° \n""",
        """28. From the diagram below,  calculate the incident angle i.  
        A. 41°. 
        B. 49°. 
        C. 55°. 
        D. 61°. \n""",
        """29. Total internal reflection will  not occur when light travels from  
        A. water to air. 
        B. water into glass. 
        C. glass to air. 
        D. glass into water. \n""",
        """30. If the linear magnification of  the objective and eyepiece convex  lenses of a compound microscope\n   are 4 and 7 respectively, calculate  the angular magnification of the  microscope. 
        A. 2. 
        B. 3. 
        C. 11. 
        D. 28. \n""",
        """31. The angle of deviation of light  of various colours passing through  a triangular prism \n increases in the  order 
        A. red → green → blue. 
        B. green → violet → blue. 
        C. blue → red → green. 
        D. blue → green → red. \n""",
        """32. Calculate the force acting on an electron of charge 1.5 x 10−19C  placed in an electric field \n of intensity 105V −1. 
        A. 1.5 x 10−11N 
        B. 1.5 x 10−12N 
        C. 1.5 x 10−13N 
        D. 1.5 x 10−14N \n""",
        """33. Capacitors are used in the  induction coil to 
        A. control circuits. 
        B. dissipate energy. 
        C. prevent electric sparks. 
        D. prevent distortion of electric fields. \n""",
        """34. A cell of emf 1.5V is connected in series with a 1Ω  resistor and a current of 0.3A \n  flows through the resistor. Find  the internal resistance of the cell. 
        A. 4Ω. 
        B. 3.0Ω. 
        C. 1.5Ω. 
        D. 1.00Ω. \n""",
        """35. Which of the following obeys  ohms law? 
        A. electrolytes. 
        B. metals. 
        C. diode. 
        D. glass. \n""",
        """36. A house has ten 40W and five  100W bulbs. How much will it cost  the owner of the house to keep\n   them lit for 10 hours if the cost of a unit is ₦5? 
        A. ₦90. 
        B. ₦50. 
        C. ₦45 
        D. ₦40. \n""",
        """37. An electric device is rated  2000V, 250V. Calculate the  maximum current it can take. 
        A. 9A. 
        B. 8A. 
        C. 7A. 
        D. 6A. \n""",
        """38. When a charge moves  through an electric circuit in the  direction of an electric force, it ___ 
        A. gains both potential and kinetic  energy. 
        B. gains potential energy and  kinetic energy. 
        C. loses potential energy and  gains kinetic energy. 
        D. loses both potential and kinetic  energy. \n""",
        """39. To convert a galvanometer to  voltmeter, a __ 
        A. high resistance is connected to  it in series. 
        B. high resistance is connected to  it in parallel. 
        C. low resistance is connected to  it in series. 
        D. low resistance is connected to  it in parallel. \n""",
        """40. Induced emfs are best  explained using 
        A. Ohm’s law. 
        B. Faraday’s law. 
        C. Coulomb’s law. 
        D. Lenz’s law. \n""",
        """41. If a current of 2.5A flows  through an electrolyte for 3 hours   and 1.8g of a substance is  deposited,\n  what is the mass of the substance that will be deposited if  a current of 4A flows through it  for 4.8 hours? 
        A. 2.4g 
        B. 3.2g 
        C. 4.6g. 
        D. 4.8g. \n""",
        """42. Calculate the energy of the  third level of an atom if the  ground state energy is -24eV 
        A. -9.20eV. 
        B. -8.20eV. 
        C. -2.75eV. 
        D. -1.75eV. \n""",
        """43. In photo-emission, the  number of photoelectrons ejected  per second depends on the ___. 
        A. frequency of the beam. 
        B. work function of the metal. 
        C. threshold frequency of the metal. 
        D. intensity of the beam. \n""",
        """44. The particle nature of light is  demonstrated by the 
        A. photoelectric effect. 
        B. speed of light. 
        C. colours of light. 
        D. diffraction of light. \n""",
        """45. The energy of a photon having a wavelength of 10−10m is (h= 6.63 x 10−34   c= 3.0 x 108  −1) 
        A. 2.0 x 10−15  
        B. 1.7 x 10−13  
        C. 2.0 x 10−12  
        D. 1.7 x 10−12\n""",
        """46. The bond between silicon and  germanium is ___ 
        A. dative. 
        B. covalent. 
        C. trivalent. 
        D. ionic. \n""",
    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "D"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "D"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "B"),
        Question(question_prompts[44], "D"),
        Question(question_prompts[45], "A"),
        Question(question_prompts[46], "D"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1992()

def Physics_1993():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
             """0. In order to remove the error of parallax when taking measurements with a metre rule,\n  the eye should be focused  
        A.slantingly towards the left on the markings 
        B. slantingly towards the right on the markings 
        C. vertically downwards on the markings 
        D. vertically upwards on the markings. \n""",
        """1 A load is pulled at a uniform speed along horizontal floor by a rope at 45⁰ to floor. \n If the force in the rope is 1500N, what is the frictional  force on the load? 
        A. 1524N 
        B. 1350N 
        C. 1260N 
        D. 1061N  \n""",
        """2 From the velocity-time graph shown above, which of the following quantities CANNOT be determined? 
        A. Deceleration. 
        B. Initial velocity. 
        C. Total distance travelled. 
        D. Initial acceleration  \n""",
        """3 Calculate the total distance covered by a train before coming to rest if its initial speed is 30ms-1\n  with a constant retardation of 0.1ms-2. 
        A. 5500m 
        B. 4500m 
        C. 4200m 
        D. 3000m.  \n""",
        """4 A car starts from rest and moves with a uniform acceleration of 30ms-2 for 20s. Calculate the \n  distance covered at the end of the motion. 
        A. 6km 
        B. 12km 
        C. 18km 
        D. 24km.  \n""",
        """5 A rocket is fired from the earth’s surface to a distant planet. By Newton’s law of universal gravitation,\n the force F will 
        A. increase as a reduces 
        B. increase as G varies 
        C. remains constant 
        D. increases as r increases  \n""",
        """6 If a freely suspended object is pulled to one side and released, it oscillates about the point of \n suspension because the 
        A. acceleration is directly proportional to the displacement 
        B. motion is directed away from the equilibrium point 
        C. acceleration is directly proportional to the square of the displacement 
        D. velocity is minimum at the equilibrium point.  \n""",
        """7 An object moves in a circular path of radius 0.5m with a speed of 1ms-1. What is its angular velocity? 
        A. 8 rads-1 
        B. 4 rads -1 
        C. 2 rads-1 
        D. 1 rads-1  \n""",
        """8 The diagram above shows a wooden block just about to slide down an inclined plane whose \n inclination to the horizontal is α. The coefficient of  frictional force between the block and the plane is 
        A. sin oc 
        B. tan oc 
        C. cot oc 
        D. cos oc  \n""",
        """9 An object of mass 20kg slides down an inclined plane at an angle of 30° to the horizontal. \n The coefficient of an active friction is ?[g ≈10ms-2]
        A. 0.2 
        B. 0.3 
        C. 0.5 
        D. 0.6  \n""",
        """10 A block and tackle is used to raise a load of 25N through a vertical distance of 30m. \n What is the efficiency of the system if the work done against  friction is 1500J? [g ≈10ms-2] 
        A. 62.5% 
        B. 73.3% 
        C. 83.3% 
        D. 94.3%  \n""",
        """11 If a load of 1kg stretches a cord by 1.2cm, what is the force constant of the cord?  [g ≈10ms-2]  
        A. 866 Nm-1 
        B. 833 Nm-1 
        C. 769 Nm-1 
        D. 667 Nm-1  \n""",
        """12 An object of volume 1m3 and mass 2kg is totally immersed in a liquid of density 1kgm-3. \n Calculate its apparent weight. 
        A. 20 N 
        B. 10 N 
        C. 2 N 
        D. 1 N  \n""",
        """13 The pressure at any point in a liquid at rest depends only on the
        A. depth and the density 
        B. mass and the volume 
        C. quantity and the surface area 
        D. surface area and the viscosity.  \n""",
        """14 A balloon whose volume is 300m3 is filled with hydrogen. If the density of air is 1.3kgm-3, \n find the up thrust on the balloon. [g ≈10ms-2] 
        A. 3000N 
        B. 3800N 
        C. 3900N 
        D. 4200N  \n""",
        """15 Clinical thermometers are examples of ?
        A. pressure gas thermometer 
        B. resistance thermometer 
        C. alcohol thermometer 
        D. mercury-in-glass thermometer.  \n""",
        """16 Two metals P and Q are heated through the same temperature difference. If the ratio of the\n  linear expansivities of P to Q is 2:3 and the ratio of  their lengths is 3:4 respectively, the ratio of the increase in lengths of P to Q is?
        A. 1:2 
        B. 2:1 
        C. 8:9 
        D. 9:8  \n""",
        """17 2000cm3 of a gas is collected at 27°C and 700mmHg. What is the volume of the gas\n at standard temperature and pressure? 
        A. 1896.5cm3
        B. 1767.3cm3 
        C. 1676.3cm3 
        D. 1456.5cm3  \n""",
        """18 Calculate the temperature change when 500 J of heat is supplied to 100g of water. \n (Specific heat capacity of water = 4200Jkg-1K-1)
        A. 12.1°C 
        B. 2.1°C 
        C. 1.2°C 
        D. 0.1°C  \n""",
        """19 Which of the following is NOT a factor that can increase the rate of evaporation of water in a lake? 
        A. Increase in the pressure of the atmosphere 
        B. Rise in temperature 
        C. Increase in the average speed of the molecules of water 
        D. Increase in the kinetic energy of the molecules of water.  \n""",
        """20 The quantity of heat energy required to melt completely 1kg of ice at -30°C is\n  (latent heat of fusion = 3.5 x 105 Jkg-1, specific heat capacity of  ice = 2.1 x 103Jkg-1 K-1) 
        A. 4.13 x 105J 
        B. 4.13 x 105J 
        C. 3.56 x 104J 
        D. 3.56 x 102J   \n""",
        """21 I. It is a rapid, constant and irregular motion of tiny particles.  II. It gives evidence that tiny\n  particles of matter called molecules exist.   III. It takes place only in gases.  IV. It gives evidence that molecules are in a constant state of random motion.  Which of the combinations above is correct about Brownian motion? 
        A. I, II and III 
        B. II, III and IV only 
        C. I, III and IV only 
        D. I, II and IV only  \n""",
        """22 The equation of a wave travelling in a horizontal direction is expressed as y=15 sin    (60t-x) \n what is its wavelength? 
        A. 60m 
        B. 15m 
        C. 5m 
        D. 2m  \n""",
        """23 Which of the following factors will affect the velocity of sound? 
        A. An increase in the pitch of the sound 
        B. An increase in the loudness of the sound 
        C. Wind travelling in the same direction of the sound 
        D. A change in the atmospheric pressure at constant temperature.  \n""",
        """24 The characteristics of a vibration that determines its intensity is the 
        A. Frequency 
        B. Overtone 
        C. Wavelength 
        D. Amplitude  \n""",
        """25 Where a man can place his face to get an enlarged image when using a concave mirror to shave. 
        A. between the centre of curvature and the principle focus 
        B. at principle focus 
        C. between the principle focus and the pole 
        D. At the centre of the curvature 
        C. between the principle focus and the pole  \n""",
        """26 A pinhole camera is placed 300m in front of a building so that the image is formed on a screen 5cm \n from the pinhole. If the image is 2.5cm high,  the height of the building will be  
        A. 25m 
        B. 50m 
        C. 100m 
        D. 150m  \n""",
        """27 The magnification of an object 2cm tall when placed 10cm in front of a plane mirror is  
        A. 6.0 
        B. 1.0 
        C. 0.7 
        D. 0.6  \n""",
        """28 After reflection from the concave mirror, rays of light from the sun converges 
        A. At the radius of curvature 
        B. At the focus 
        C. Beyond the radius of curvature 
        D. Between the focus and radius of curvature  \n""",
        """29 A glass block of thickness 10cm is placed on an object. If an observer views the object vertically, \nthe displacement of the object is  
        A. 3.33cm 
        B. 5.00cm 
        C. 6.67cm 
        D. 8.50cm  \n""",
        """30 I. Rays of light travel from a less dense medium to a denser medium II. The angle of incidence is greater\n than critical angle. III. Rays of light  travel from a denser medium to a less dense medium. Which of the statements above are conditions for total internal reflection to occur? 
        A. I & II only 
        B. I & III only 
        C. II & III only 
        D. II only  \n""",
        """31 The use of lenses is NOT applicable in the 
        A. projector 
        B. human eye 
        C. periscope 
        D. telescope  \n""",
        """32 Dispersion of white light is the ability of white light to 
        A. Penetrate air, water and glass 
        B. Move in a straight line 
        C. Move around corners 
        D. Separate to its component colours  \n""",
        """33 A newly charged 12V accumulator can easily start a car whereas eight new dry cells in series with \nan effective e.m.f. of 12V cannot start the same  car because 
        A. The current capacity is high 
        B. The current capacity is low  
        C. It cannot be re-charged 
        D. It cannot easily be connected to a car  \n""",
        """34 Six identical cells, each of e.m.f. 2V are connected as shown above. The effective e.m.f. of the cell is 
        A. 0V 
        B. 4V 
        C. 6V 
        D. 12V  \n""",
        """35 The fuse in an electric devise is always connected to the ---- 
        A. Neutral side of an electric supply 
        B. Earth side of an electric supply 
        C. Live side of an electric supply 
        D. Terminal side of an electric supply  \n""",
        """36 A particle carrying a charge of 1.0 x 10-8C enters a magnetic field at 3.0 x 102ms-1 at right angles\n to the field. If the force on this particle is  1.8 x 10-8N, what is the magnitude of the field? 
        A. 6.0 x 10-1T 
        B. 6.0 x 10-2T 
        C. 6.0 x 10-3T 
        D. 6.0 x 10-4T  \n""",
        """37 The current output form of an a.c. source is given as I = 10 sin ωt. The d.c. equivalent of the current is 
        A. 5.0A 
        B. 7.1A 
        C. 10.0A 
        D. 14.1A  \n""",
        """38 A conductor of length 1m moves with a velocity of 50ms-1 at an angle of 30° to the direction of a \nuniform magnetic field of flux density 1.5 Wbm-2.  What is the e.m.f. induced in the conductor?  
        A. 37.5V 
        B. 50.5V 
        C. 75.0V 
        D. 80.5V  \n""",
        """39 The process of detecting a pin mistakenly swallowed by a child x–ray 
        A. Diagnosis 
        B. Therapy 
        C. Crystallography 
        D. mammography  \n""",
        """40 Which of the following particles CANNOT be deflected by both electric and magnetic fields? 
        A. Gamma rays 
        B. Alpha particles 
        C. Wave particles 
        D. Beta particles  \n""",
        """41 A piece of radioactive material contains 1000 atoms. If its halflife is 20 seconds, the \ntime taken for 125 atoms to remain is 
        A. 20 seconds 
        B. 40 seconds 
        C. 60 seconds 
        D. 80 seconds  \n""",
        """42  The p-n junction diodes can act as rectifiers because they 
        A. Conduct current when forward biased 
        B. Conduct current when reverse- biased 
        D. Conduct current in both directions 
        B. Conduct current when reverse- biased  \n""",
        """43 If a reverse-biased voltage is applied across a p-n junction, the depletion layer width is 
        A. Increased 
        B. Decreased 
        C. Constant 
        D. halved  \n""",
        """44 I. Small size II. Low power requirement  III. Not easily damaged by high Temperature \n IV. Highly durable  Which of the above are the advantages of semiconductors? 
        A. I, II and III only 
        B. II, III and IV only 
        C. I, II and IV only 
        D. I, II III and IV  \n""",
    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "C"),
        Question(question_prompts[42], "B"),
        Question(question_prompts[43], "B"),
        Question(question_prompts[44], "B"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1993()

def Physics_1994():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
            """0 A carpenter on top of a roof 20.m high dropped a hammer of mass 1.5kg and it fell \n freely to the ground.The kinetic energy of the hammer just before hitting the ground is ....... [g = 10ms-2] 
        A. 450 J 
        B. 600 J 
        C. 150 J 
        D. 300 J \n""",
        """1 Two balls X and Y weighing 5g and 50kg respectively were thrown up vertically at the same\n time with a velocity of 100ms-1. How will their positions be one second later? 
        A. X and Y will both be 500m from the point of throw 
        B. X and Y will be 500m from each other 
        C. Y will be 500 m ahead of X 
        D. X will be 500m ahead of Y. \n""",
        """2 A man standing on a lift that is descending does not feel any weight because 
        A. there is no gravitational pull on the man in the lift 
        B. the inside of the lift is air tight 
        C. the lift is in vacuum 
        D. there is no reaction from the floor of the lift. \n""",
        """3 An object of mass 2kg moves with a velocity of 10ms-1 round a circle of radius 4m. Calculate the\n  centripetal force on the object. 
        A. 40 N 
        B. 25 N 
        C. 100 N 
        D. 50 N \n""",
        """4 If it takes an object 3s to fall freely to the ground from a certain height, what is the distance \n covered by the object? [g = 10ms-2] 
        A. 60 m 
        B. 90 m 
        C. 30 m 
        D. 45 m. \n""",
        """5 If a tube of small radius opened at both ends is placed in a liquid, the liquid will 
        A. rise above the liquid level if the liquid does not wet the glass 
        B. remain at the same level irrespective of whether the liquid wets the glass or not 
        C. fall below the liquid level if the liquid wets the glass 
        D. fall below the liquid level if the liquid does not wet the glass. \n""",
        """6 I. Density of the liquid   II. Depth below the surface of the liquid.   III. Surface area of the liquid.\n  In which of the statement above will pressure be dependent?
        A. I and III only 
        B. I and II only 
        C. II and III only 
        D. I, II and III. \n""",
        """7 I. High thermal capacity II. High sensitivity   III. Easy readability  IV. Accuracy over a wide range\n  of temperatures From the statements above, the qualities of a good thermometer are
        A. II, III and IV 
        B. I and II 
        C. I, II, III and IV 
        D. I, III and IV. \n""",
        """8 A machine is used to lift a load of 20 N through a height of 10m. if the \n efficiency of the machine is 40%, how much work is done? 
        A. 120 J 
        B. 80 J 
        C. 500 J 
        D. 300 J. \n""",
        """9 Which of the following could be effectively used to reduce friction? 
        A. Petrol 
        B. Kerosene 
        C. Grease 
        D. Water. \n""",
        """10 A copper wire was subjected to a tensile stress of 7.7 x 107 Nm-2. Calculate \n the tensile strain of the wire. [Young modulus = 1.1 x 1011Nm-2] 
        A. 2.2 x 10-4 
        B. 2.0 x 10-5
        C. 7.0 x 10-3
        D. 7.0 x 10-4 \n""",
        """11 An object weighs 22kg in water and 22kg in water an 30kg in air.What is the\n  upthrust exerted by the liquid on the object? [g = 10 ms-2] 
        A. 80 N 
        B. 50 N 
        C. 520 N 
        D. 220 N. \n""",
        """12 A block of aluminium is heated electrically by a 30 W heater. If the temperature \n rises by 100˚C in 5 minutes, the heat capacity of the aluminium is 
        A. 200 JK-1 
        B. 900 JK-1 
        C. 90 JK-1 
        D. 100 JK-1 \n""",
        """13 A perfect emitter or absorber of radiant energy is a 
        A. red body 
        B. conductor 
        C. black body 
        D. white body. \n""",
        """14 The phenomenon that shows that increase in pressure lowers the melting point can be observed in 
        A. regelation 
        B. sublimation 
        C. condensation 
        D. coagulation. \n""",
        """15 If the volume of a gas increases steadily as the temperature decreases at\n  constant pressure, the gas obeys 
        A. Charles’ law 
        B. Graham’s law 
        C. Boyle’s law 
        D. pressure law. \n""",
        """16 Steam burn is more severe than that of boiling water because 
        A. steam burn is dependent on relative humidity 
        B. steam burn is independent of relative humidity 
        C. steam possess greater heat energy per unit mass 
        D. water boils at a higher temperature \n""",
        """17 Which of the following types of waves needs a medium for propagation? 
        A. X-rays 
        B. Sound waves 
        C. Light waves 
        D. Radio waves. \n""",
        """18 The ground is always cold at night because the 
        A. atmosphere reflects the sun’s energy at night 
        B. atmosphere absorbs the sun’s energy at night 
        C. earth radiates heat to the atmosphere at night 
        D. sun no longer shines at night. \n""",
        """19 A metal of volume 40cm3 is heated from 30⁰C to 90⁰C, the increase in volume is ..... \n [Linear expansivity of the metal= 2.0 x 10-5K-1] 
        A. 0.40cm3 
        B. 0 14cm3 
        C. 0.12cm3 
        D. 1.20cm3 \n""",
        """20 I. Change of state  II. Diffusion III. Radiation  IV. Osmosis  Which of the processes \n above can be explained using the kinetic theory? 
        A. I, II and IV 
        B. I, II, III and IV 
        C. I, II and III 
        D. I, III and IV. \n""",
        """21 When the human eye loses its power of accommodation, the detect is known as 
        A. long-sightedness 
        B. short-sightedness 
        C. presbyopia 
        D. astigmatism. \n""",
        """22 A length of wire has a frequency of 255Hz when stretched by a force of 225 N. If the force \n increases to 324 N, what is the new frequency of vibration? 
        A. 356 Hz 
        B. 306 Hz 
        C. 512 Hz 
        D. 488 Hz. \n""",
        """23 A certain far-sighted person cannot see objects that are closer to the eye than 50cm clearly. \n Determine the power of the converging lens which will enable him to see at 25cm. 
        A. 0.04 D 
        B. 0.06 D 
        C. 0.02 D 
        D. 0.03 D. \n""",
        """24 Which of the following electromagnetic waves has the highest frequency? 
        A. X-rays 
        B. Ultra-violet rays 
        C. Radio waves 
        D. Infrared-rays. \n""",
        """25 When a red rose flower isobserved in blue light, what colour does the observer see? 
        A. Yellow 
        B. Red 
        C. Blue 
        D. Magenta. \n""",
        """26 The eclipse of the sun occurs when the ____
        A. moon’s umbra falls on some part of the earth 
        B. moon is between the sun and the earth 
        C. earth is between the sun and the moon 
        D. moon is not completely hidden in the earth’s shadow. \n""",
        """27 A cannon is fired from town X. After how long is the sound heard at a town Y 4.95 km away? \n [velocity of sound in air = 333 ms-1] 
        A. 15 s 
        B. 0 s 
        C. 10 s 
        D. 12 s \n""",
        """28 An image in a convex lens is upright magnified 3 times. If the focal length of the lens is 15cm,\n  what is the object distance? 
        A. 14 cm 
        B. 10cm 
        C. 25 cm 
        D. 26cm. \n""",
        """29 The capacitance of a parallel plate capacitor is 20 μF in air and 60 μF in the presence of a dielectric.\n  What is the dielectric constant? 
        A. 2.0 
        B. 0.3 
        C. 6.0 
        D. 3.0. \n""",
        """30 In the circuit below, three resistors, 2Ω, 4 Ω and 12 Ω are connected in parallel and a 12 V battery \n is connected across the combination. The current flowing through the 12 Ω resistor is 
        A. 9.6 A 
        B. 14.4 A 
        C. 1.0 A 
        D. 3.2 A. \n""",
        """31 If the charge of electricity per kWh is N4, what is the cost of operating an electrical appliance \n rated 2.50 V, 2 A for 6 hours? 
        A. ₦24 
        B. ₦0.12 
        C. ₦12 
        D. ₦16. \n""",
        """32 Three similar cells each of e.m.f 2V and internal resistance 2 Ω are connected in parallel,\n the total e.m.f and total internal resistance are respectively 
        A. 6 V, 0.7 Ω 
        B. 6 V, 6.0 Ω 
        C. 2 V, 0.7 Ω 
        D. 2 V, 6.0 Ω \n""",
        """ 33 In homes, electrical appliances and lamps are connected in parallel because 
        A. less voltage will be used 
        B. parallel connection does not heat up the wires 
        C. series connection uses high voltage 
        D. less current will be used. \n""",
        """34 Two resistors 5 Ω and 10 Ω are arranged first in series and later in parallel to a 24 V source.\n The ratio of total power dissipated in the series and parallel arrangement respectively is  
        A. 3:5 
        B. 5:3 
        C. 1:50 
        D. none of the above \n""",
        """35 Which of the following will be applied when a metal x in electrolysis? 
        A. Y is the anode and very high current is used 
        B. X is the anode and very high current is used 
        C. X is the cathode and Y is the anode 
        D. Y is the cathode and X is the anode \n""",
        """36 A radioactive isotope has a decay constant of 10-5s-1. Calculate its half-life.
        A. 6.93 x 104s
        B. 6.93 x 10-6s
        C. 6.93 x 10-5s 
        D. 6.93 x 105s \n""",
        """37  Which of the following is a property of steel? 
        A. It can easily be magnetized and demagnetized 
        B. It cannot retain its magnetism longer than iron 
        C. It can be used for making temporary magnets 
        D. It can be used for making permanent magnets.  \n""",
        """38 If the threshold frequency for tungsten is 1.3 x 1015Hz, what is its work function? \n [h = 6.6 x 10-34 Js] 
        A. 8.85 x 10-18 J 
        B. 8.58 x 10-19 J 
        C. 8.58 x 10-15 J 
        D. 8.58 x 10-17 J \n""",
        """39 Two inductors of inductances 4H and 8H are arranged in series and a current of 10A \n is passed through them. What is the energy stored in them? 
        A. 250 J 
        B. 500 J 
        C. 50 J 
        D. 133 J. \n""",
        """40 Under which of the following conditions do gasses conduct electricity? 
        A. High pressure and high p.d 
        B. Low pressure and low p.d 
        C. low pressure and high p.d 
        D. High pressure and low p.d \n""",
        """41 In measuring high frequency a.c., the instrument used is the 
        A. hot wire ammeter 
        B. d.c. ammeter 
        C. moving coil ammeter 
        D. moving iron ammeter. \n""",
        """42 The bond between silicon and germanium is 
        A. electrovalent 
        B. covalent 
        C. ionic 
        D. dative. \n""",
        """43 Which of the following materials has an increase in resistance with temperature? 
        A. Electrolyte 
        B. Water 
        C. Metals 
        D. Wood. \n""",
        """44 The electrical properties of germination can be altered drastically by the addition of impurities. \n The process is referred to as 
        A. doping 
        B. saturation 
        C. bonding 
        D. amplification. \n""",
    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "B"),
        Question(question_prompts[42], "C"),
        Question(question_prompts[43], "D"),
        Question(question_prompts[44], "B"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1994()

def Physics_1995():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
        """0 Two cars moving in the same direction have speeds of 100kmh1 and 130kmh-1. \nWhat is the velocity of the faster cars as measured by an observer in  the slower car? 
         A.130 kmh-1 
         B.230 kmh-1 
         C.200 kmh-1 
         D.30 kmh-1 \n""",
        """1 The diagram above shows a velocity-time graph. The  statement that is true about this motion is that, \nthe car 
         A.decelerates between points F and H 
         B.accelerates between points F and G 
         C.has a constant speed between points E and 
         D.has no acceleration between point F and G. \n""",
        """2 A stone and a feather dropped from the same height above the earth surface. Ignoring air resistance,\n which of the following is correct? 
         A.The stone and feather will both reach the ground at the same time. 
         B.The stone will reach the ground first 
         C.The feather will reach the ground first 
         D.The feather will be blown away by the wind while stone will drop steadily \n""",
        """3 A car moves with an initial velocity of 25 ms-1 and reaches a velocity of 45 ms-1 in 10s. \nWhat is the acceleration of the car? 
         A. 5 ms-2 
         B. 25 ms-2 
         C. 20 ms-2 
         D. 2 ms-2 \n""",
        """4 An object is weighed at different locations on the earth. What will be the right observation? 
         A.Both the mass and weight vary 
         B.The weight is constant while the mass varies 
         C.The mass is constant while the weight varies 
         D.Both the mass and weight are constant. \n""",
        """5 A bob of weight 0.1N hangs from a massless string of length 50cm. A variable horizontal force\n which increases from zero is applied to pull the bob  until the string makes an angle of 600 with the vertical. The work done is 
         A. 0.250 J 
         B. 0.025 J 
         C. 0.050 J 
         D. 0.500 J \n""",
        """6 The surfaces of conveyor belts are made rough so as to ______
         A. prevent the load from slipping 
         B. make them stronger 
         C. enable them to carry more load 
         D. protect them while carrying load. \n""",
        """7 A machine of velocity ratio 6 requires an effort of 400N to raise a load of 800N through 1m.\n Find the efficiency of the machine. 
         A. 50% 
         B. 22.2% 
         C. 33.3% 
         D. 55.6% \n""",
        """8 If a wire 30cm long is extended to 30.5cm by a force of 300N. Find the strain energy of the wire.  
         A. 7.50 J 
         B. 750.00 J 
         C. 75.00 J 
         D. 0.75 J \n""",
        """9 In a hydraulic press,the pump piston exerts a pressure of 100 Pa on the liquid. What force is\n exerted in the second piston of crosssectional area 3  m2? 
         A.200 N 
         B. 100 N 
         C. 150 N 
         D. 300 N \n""",
        """10 The accurate measurement of the relative density of a substance in its powered form is done \nwith a beam balance and _______
         A. an eureka can 
         B. a burette 
         C. a pipette 
         D. a density bottle. \n""",
        """ 11 A hydrometer is an instrument used in measuring  ____
         A. density of liquid 
         B. relative density of a liquid 
         C. relative humidity of a liquid 
         D. vapour pressure of a fluid \n""",
        """12 One special advantage of alcohol water over mercury as a thermometric liquid is its 
         A. low freezing point 
         B. low boiling point 
         C. high specific heat capacity 
         D. low density. \n""",
        """13 Two metals P and Q of lengths l1 and l2 are heatedthrough the same temperature difference. If the ratio \nof the linear expansivities of P to Q  is 2:3 and the ratio of their lengthsis 3:4. What is the ratio of increase in lengths of P to Q? 
         A. 5:7 
         B. 2:1 
         C. 1:2 
         D. 7:5 \n""",
        """14 The density of a certain oil on frying becomes 0.4kgm-3 with a volume of 20m-3. What will be its\n initial volume when its initial density is  0.8kgm-3 assuming no loss of oil due to spillage? 
         A. 10 kgm-3 
         B. 5 kgm-3 
         C. 8 kgm-3 
         D. 12 kgm-3 \n""",
        """15 Heat is radiated by all hot objects in the form of 
         A. light energy 
         B. solar energy 
         C. infrared ray 
         D. x-rays. \n""",
        """16 If a container is filled with ice to the brim, what happens to the level of water \nwhen the ice completely melts? 
         A. The water in the glass outflows. 
         B. The level of water drops. 
         C. The level of water remains unchanged 
         D. The level of water goes up. \n""",
        """17 The small droplet of water that forms on the grass in the early hours of the morning is 
         A. dew 
         B. mist 
         C. fog 
         D. hail. \n""",
        """18 A vapour is said to be saturated when 
         A.a dynamic equilibrium exists such that more molecules return to the liquid than are leaving it. 
         B. the vapour pressure is atmospheric 
         C. the temperature of the vapour varies 
         D. a dynamic equilibrium exists between liquid molecules and the vapour molecules.  \n""",
        """19 The pressure of one mole of an ideal gas of volume 10-2m3 at a temperature of 27⁰C is .....\n [Molar gas constant = 8.3 Jmol-1K-1] 
         A. 2.24 x 104 Nm-2
         B. 2.24 x 105 Nm-1 
         C. 2.49 x 105 Nm-1 
         D. 2.49 x 104 Nm-1.  \n""",
        """20 Which of the following has no effect on radiation? 
         A. density. 
         B. temperature. 
         C. surface area. 
         D. nature of the surface.  \n""",
        """21 The wavelength of a wave travelling with a velocity of 420ms-1 is 42m. What is its period? 
         A. 1.0s 
         B. 0.1s 
         C. 0.5s 
         D. 1.2s  \n""",
        """22 The sound of an electric bell dies down slowly when air is slowly pumped out from a bottle because 
         A. sound cannot pass through the bottle 
         B. sound can pass through a vacuum 
         C. sound needs a material medium 
         D. the wavelength of sound becomes greater in the bottle.  \n""",
        """23 During a thunderstorm, the sound is heard over a long time. This phenomenon is referred to as 
         A. refraction of sound. 
         B. reverberation .
         C. superposition. 
         D. diffraction of sound.  \n""",
        """24 The velocity of sound in air at 16⁰C is 340ms-1. What will it be when the pressure is \ndoubled and its temperature raised to 127⁰C? 
         A. 4,000ms-1 
         B. 160,000 ms-1  
         C. 8,000 ms-1 D. 400 ms-1 
         D. 400 ms-1  \n""",
        """25 In comparing the camera and the human eye, the film of the camera functions as the ____
         A. iris 
         B. pupil 
         C. cornea 
         D. retina  \n""",
        """26 An object 4 cm high is placed 15 cm from a concave mirror of focal length 5 cm. The size of the image is?
         A. 3 cm 
         B. 5 cm 
         C. 4 cm 
         D. 2 cm  \n""",
        """27 An object is embedded in a block of ice, 10cm below the plane surface. If the refractive index of \nthe ice is 1.50, the apparent depth of the object  below the surface is? 
         A. 67 cm 
         B. 7.63 cm 
         C. 7.50 cm 
         D. 2.50 cm  \n""",
        """28 Which of the following is used for the correction of short sightedness? 
         A. Concave lens. 
         B. Concave mirror. 
         C. Convex mirror. 
         D. Convex lens.  \n""",
        """29 Dispersion occurs when white light passes through a glass prim because of the 
         A. different speeds of the colours in the glass. 
         B. high density of the glass. 
         C. defects in the glass. 
         D. different hidden colours in the glass.  \n""",
        """30 When a positively charged rod is brought nearer the cap of a positively charged electroscope, \nthe leaves divergence will. 
         A. converge 
         B. remain constant 
         C. diverge 
         D. be induced.  \n""",
        """31 Three capacitors of capacitance, 2μF, 4μF and 8μF are connected in parallel and a p.d of 6V is\n maintained across each capacitor, the total energy  stored is 
         A. 6.90 x 10-6 J 
         B. 6.90 x 10-4 J 
         C. 2.52 x 10-4 J 
         D. 2.52 x 10-6 J  \n""",
        """32 A cell of emf 12V and internal resistance 4Ω is connected to an external resistor of resistance 2 Ω\n Find the current flow. 
         A. 4 A 
         B. 2 A 
         C. 3 A 
         D. 5 A  \n""",
        """33 Three 4Ω resistors connected in parallel have 3 potential difference of 16V applied across them.\n What is the total current in the circuit 
         A. 12 A 
         B. 8 A 
         C. 10 A 
         D. 14 A  \n""",
        """34 In the diagram above,a 200 W bulb is lighted by a 240 V a.c mains supply. If 1kWh is sold at \nN40,the cost of keeping the bulb lighted for a day is. 
         A. N 192.00 
         B. N 1.92 
         C. N 19.20 
         D. N 1,920.00.  \n""",
        """35  Power supply is transmitted ata very high voltage and low current in order to 
         A. increase the power supply 
         B. prevent overheating of the coil 
         C. make it travel fast 
         D. make it pass through thetransformers.  \n""",
        """36 south-poles of two magnets stroke a steel bar, the polarities at T and V will respectively be 
         A. north and south 
         B. south and south 
         C. north and north 
         D. south and north.  \n""",
        """37 A galvanometer with full-scale deflection of 10mA is to be converted to a voltmeter with fullscale \ndeflection of 5 V. If a series resistance of  498Ω is used for the conversion,theresistance of the galvanometer is 
         A. 2 Ω 
         B. 10 Ω 
         C. 5 Ω 
         D. 1 Ω  \n""",
        """38 Two inductors of inductances 5 mH and 15mH are connected in series and a current of 5A flows through\n them.The total energy stored in the inductors  is 
         A. 250.0 J 
         B. 50.0 J 
         C. 62.5 J 
         D. 500.0 J  \n""",
        """39 In Faraday’s law of electrolysis, a graph of mass deposited against the quantity of electricity \nis plotted. The slope of the graph gives 
         A. the electrochemical equivalent 
         B. the charge released 
         C. the current flowing 
         D. the energy released  \n""",
        """40 In a discharge tube, most of the gas is pumped out so that electricity is conducted at 
         A. steady voltage 
         B. high pressure 
         C. high pressure 
         D. low voltage.  \n""",
        """41 The radioisotope 23592U decays by emitting two alphaparticles, three beta particles and a gamma ray. \nWhat is the massand atomic numbers of the  resulting daughter element? 
         A. 91 and 227 
         B. 92 and 238 
         C. 227 and 91 
         D. 215 and 88.  \n""",
        """42 Transistors are used for the 
         A. conversion of a.c. to d.c. 
         B. conversion of d.c. to a.c. 
         C. amplification of signals 
         D. rectification of signals.  \n""",
        """43  A typical transistor characteristic is represented as Which of the following is a pure semiconductor? 
         A. Silicon 
         B. Phosphorus 
         C. Transistor 
         D. Carbon 
         A. Silicon \n""",
    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "B"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "C"),
        Question(question_prompts[43], "A"),

    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("You are correct and thrive to get the next one guy!")
                score += 1
            else:
                print(
                    "wow! you didnt do badly but you can improve your point by thriving hard in the next question")
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
        score = int((score / len(questions) * 100))
        print("your score is: " + str(score) + "%")

    run_test(questions)
    while play_again():
        Physics_1995()
    print("""
    you have biology , english , chemistry and physics
    for biology enter year 1980
    for English enter year 1981
    for Chemistry enter year 1982
    for Physics enter year 1983
    for biology enter year 1985
    for physics enter year 1986
    for biology enter year 1987
    for biology enter year 1988
    for Chemistry enter year 1989
    for English enter year 1990
    for Physics enter year 1991
    for Physics enter year 1992
    for Physics enter year 1993
    for Physics enter year 1994
    for Physics enter year 1995
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
    if year == "1985":
        biology_1985()
    if year == "1986":
        Physics_1986()
    if year == "1987":
        biology_1987()
    if year == "1988":
        biology_1988()
    if year == "1989":
        Chemistry_1989()
    if year == "1990":
        English_1990()
    if year == "1991":
        Physics_1991()
    if year == "1992":
        Physics_1992()
    if year == "1993":
        Physics_1993()
    if year == "1994":
        Physics_1994()
    if year == "1995":
        Physics_1995()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")