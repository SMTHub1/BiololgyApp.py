from Question import Question

question_prompts = [
        """" 1. A group of closely related organisms capable of interbreeding to produce fertile offspring are known as members of a
        A. kingdom 
        B. class
        C. family
        D. species \n
        """,""""
        2. A beaker of pond water containing few specimens of Euglena was placed in a dark room for two weeks. \n At the end of this period, the specimens of Euglena were still alive because they were
        A. able to carry out holozoic nutrition
        B. able to carry out photosynthesis using carbon dioxide in the pond water
        C. better adapted to life in darkness than to life in light
        D. not overcrowded \n 
        """,""""
        3. The cytoplasm of the cell is considered a very important component because it
        A. regulates the amount of energy in thecell 
        B. suspends all cell organelles
        C. is the outermost part of the cell 
        D. is solely responsible for cell division \n
        """,""""
        4. Red blood cells were found to have burst open after being placed in distil for an hour. This phenomenon is known as
        A. plasmolysis 
        B. diffusion
        C. haemolysis
        D. wilting \n
        """,""""
        5. The curvature movement of plants in response to the stimulus of water is called
        A. hydrotropism
        B. geotropism
        C. Phototropism
        D. thigmotropism\n 
        ""","""
        6. The overall reaction in glycolysis can be summarised as
        A. C  6111205 --K31-1403 + 4H +ATP 
        B. C6H1206 ----- 2;11403+ 4H +2ATP 
        C. C61-1,206---.> 2;1-1403 + 4H+ ADP 
        D. C6F11206 2C31-1403+ 4h + 2ADP\n 
        """,""""
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
        Question(question_prompts[0],"D"),
        Question(question_prompts[1],"A"),
        Question(question_prompts[2],"B"),
        Question(question_prompts[3],"C"),
        Question(question_prompts[4],"A"),
        Question(question_prompts[5],"B"),
        Question(question_prompts[6],"B"),
        Question(question_prompts[7],"D"),
        Question(question_prompts[8],"D"),
        Question(question_prompts[9],"A"),
        Question(question_prompts[10],"A"),
        Question(question_prompts[11],"A"),
        Question(question_prompts[12],"A"),
        Question(question_prompts[13],"A"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "A"),
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)