from Question import Question
def Biology_2020():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0 The function of the red head in male Agama lizards is to
        A. conceal and camouflage the animal from predators
        B. scare other males from the territory
        C. attract female lizards for mating purposes
        D. warm predators of the distastefulness of the animal 
        \n """,
        """1 In which of the following species is the  biomass of an individual the smallest?
        A. Agama sp.
        B. Bufo sp. 
        C. Spirogyra sp.
        D. Tilapia sp. 
        \n """,
        """2 Seed plants are divided into 
        A. tracheophytes and ferns
        B. angiosperms and gymnosperms
        C. monocotyledons and dicotyledons
        D. thallophytes and bryophytes 
        \n """,
        """3 In which of the following groups of vertebrates is parental care mostly exhibited?
        A. Reptilia 
        B. Amphibia
        C. Aves
        D. Mammalia 
        \n """,
        """4 The adaptive importance of nuptial flight from termite colonies is to
        A. disperse the reproductives in order to establish new colonies
        B. provide abundant food for birds and other animals during the early rains
        C. ensure cross-breeding between members of one colony and another
        D. expel the reproductives so as to provide enough food for other members 
        \n """,
        """5  Which of the following can cause  shrinkage of living cells?
        A. Hypotonic solution
        B. Isotonic solution 
        C. Deionized water
        D. Hypertonic solution 
        \n """,
        """6  Which of the following is true of  leucocytes?
        A. they are respiratory pigments 
        B. they are most numerous and ramify all cells
        C. they are large and nucleated
        D. they are involved in blood clotting 
        \n """,
        """7 The conversion of a nutrient into a molecule in the body of a consumer is referred to as
        A. digestion
        B. assimilation
        C. absorption
        D. inhibition 
        \n """,
        """8 The ability of living organism to detect  and respond to changes in the  environment is referred to as 
        A. locomotion 
        B. irritability
        C. growth
        D. taxis 
        \n """,
        """9 In mammals, the exchange of nutrients  and metabolic products occurs in the
        A. lungs
        B. oesophagus 
        C. trachea
        D. lymph 
        \n """,
        """10 An example of an endospermous seed is 
        A. maize gain
        B. cashew nut
        C. cotton seed
        D. been seed 
        \n """,
        """11 I. Parasitism → Sundew. II. Autotrophism →Amoeba. III. Saprophytism → Alga. IV Heterotrophism → Agama.  Which of the above modes of nutrition is correctly matched with the organism that exhibits it?
        A. II
        B. III
        C. II
        D. I 
        \n """,
        """12 I. Test tube containing cane sugar and water. II. Test tube containing cane sugar and diluted acid. III. Test tube containing cane sugar and its degrading enzyme. In which of the test tubes will glucose be detected after complete hydrolysis?
        A. I and II only
        B. II and III only
        C. I only
        D. I, II and III 
        \n """,
        """13 The enzyme involved in the hydrolysis is
        A. rennin
        B. erepsin 
        C. sucrase 
        D. maltase 
        \n """,
        """14 The part of the mammalian ear responsible for the maintenance of balance is the 
        A. cochlea
        B. pinna
        C. perilymph
        D. ossicles 
        \n """,
        """15 The path followed by air as it passes  through the lungs in mammals is
        A. trachea → bronchi → bronchioles →alveoli
        B. bronchi → trachea → alveoli →bronchioles
        C. trachea → bronchioles →bronchi→alveoli
        D. bronchioles → alveoli → bronchi →trachea
        \n """,
        """16 The movement response of a cockroach away from a light source can be described as
        A. positive phototaxism
        B. negative phototaxism
        C. negative phototropism
        D. positive phototropism 
        \n """,
        """17  The vascular tissues in higher plants are  responsible for
        A. the movement of food and water 
        B. suction pressure
        C. transpiration pull
        D. the transport of gases and water 
        \n """,
        """18 Which of the following organs regulates  the levels of water, salts, hydrogen ions and urea in the mammalian blood?
        A. Liver
        B. Kidney
        C. Bladder
        D. Colon 
        \n """,
        """19 The sequence of the one-way gaseous  exchange mechanism in a fish is
        A. operculum → gills → mouth
        B. gills → operculum → mouth 
        C. mouth → operculum → gills 
        D. mouth → gills → operculum 
        \n """,
        """20 The type of asexual reproduction that is common to both Paramecium and protists is
        A. budding
        B. sporulation
        C. fragmentation
        D. fission 
        \n """,
        """21  In nature, plants and animals are  perpetually engaged in mutualism because
        A. they are rivals 
        B. all animals rely on food produced by plants
        C. they utilize respiratory wastes of each other
        D. they are neighbours 
        \n """,
        """22 In an experiment to determine the percentage of humus and water in a soil sample, the following results were obtained:  Weight of the evaporating basin alone = 80.5g Weight of basin and soil = 101.5g Weight after drying the soil in the oven = 99.0g Weight of basin and roasted soil  = 95.5g The percentage of humus in the soil sample is
        A. 16.7%
        B. 17.6%
        C. 26.7%
        D. 16.2% 
        \n """,
        """23 An example of a filter -feeding animal is
        A. shark
        B. butterfly
        C. whale
        D. mosquito 
        \n """,
        """24  Which of the following is a feature of the population pyramid of a developing country?
        A. long lifespan 
        B. low birth rate 
        C. low death rate 
        D. short lifespan
        \n """,
        """25 The interaction of a community of organisms with its abiotic environment constitutes
        A. niche
        B. a food chain
        C. an ecosystem
        D. a microhabitat 
        \n """,
        """26 The vector of the malaria parasite is 
        A. female Aedes mosquito
        B. female Anopheles mosquito 
        C. male Culex mosquito
        D. female Culex mosquito 
        \n """,
        """27  Which of the following instruments is  used to measure relative humidity?
        A. Hydrometer 
        B. Thermometer
        C. Hygrometer
        D. Anemometer 
        \n """,
        """28  Exo-erythrocytic phase of the life cycle of malaria parasite occurs in the
        A. liver of humans
        B. reticuloendothelial cells of humans
        C. Malpighian tubules of mosquito
        D. brain of humans 
        \n """,
        """29. Habitats are generally classified into
        A. biotic and abiotic
        B. aquatic and terrestrial
        C. arboreal and marine biomes
        D. microhabitats and macrohabitats 
        \n """,
        """30. Dracunculiasis can be contacted through 
        A. eating contaminated food
        B. drinking contaminated water 
        C. bathing in contaminated water
        D. bites of blackfly 
        \n """,
        """31 Which of the following groups of  environmental factors are density- dependent?
        A. Food, salinity, accumulation of metabolites and light
        B. Temperature, salinity predation and disease
        C. Food predation, disease and accumulation of metabolites 
        D. Temperature food disease and light 
        \n """,
        """32 Millet, sorghum, maize and onions are common crops growth in Nigeria in the
        A. tropical rainforests
        B. Sudan savanna
        C. montane forests
        D. Sahel savanna 
        \n """,
        """33 In which of the following biomes is the  south western part of Nigeria located?
        A. Temperate forest
        B. Tropical rainforest
        C. Tropical woodland
        D. Desert 
        \n """,
        """34  The inheritable characters that are  determined by a gene located on the X- chromosome is
        A. recessive 
        B. sex-linked
        C. homozygous
        D. dominant 
        \n """,
        """35 Lack of space in a population could lead to an increase in
        A. water scarcity
        B. birth rate 
        C. disease rate
        D. drought 
        \n """,
        """36 If the cross of a red-flowered plant with  a white-flowered plant produces a pink- flowered plant, it is an example of
        A. codominance
        B. incomplete dominance
        C. mutation
        D. linkage 
        \n """,
        """37 Which of the following theories was NOT considered by Darwin in his evolutionary theory?
        A. Variation
        B. Survival of the fittest
        C. Use and disuse
        D. Competition 
        \n """,
        """38 The crossing of individuals of the same  species with different genetic characters is
        A. cross breeding 
        B. polygenic inheritance
        C. non-disjunction
        D. inbreeding 
        \n """,
        """39  The number of alleles controlling blood groups in humans
        A. 3
        B. 4
        C. 5
        D. 2 
        \n """,
        """40  During blood transfusion, agglutination may occur as a result of the reaction between
        A. contrasting antigens and antibodies
        B. two different antigens
        C. two different antibodies
        D. similar antigens and antibodies 
        \n """,
        """41 The fallacy in Lamarck's evolutionary theory was the assumption that
        A. traits are acquired through disuse of body parts
        B. acquired traits are heritable
        C. acquired traits are seldom formed
        D. traits are acquired through the use of body parts 
        \n """,
        """42 The bright coloured eye spots on the wings of moth are an example of
        A. warning colouration
        B. disruptive colouration
        C. crypsis
        D. mimicry 
        \n """,
        """43 The wings of a bat and those of a bird are examples of
        A. convergent evolution
        B. continuous variation
        C. coevolution
        D. divergent evolution 
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "D"),
        Question(question_prompts[43], "D"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2020()
def Biology_2019():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0 Which of the following characterizes a  mature plant cell?
A. the cytoplasm fills up the entire cell space
B. the nucleus is pushed to the centre ofthe cell
C. the cell wall is made up of cellulose
D. the nucleus is small and irregular in shape  the cell
\n """,
"""1  Which of the following is NOT a function of the nucleus of a cell?
A. it controls the life processes of the cell
B. it translates genetic information for the manufacture of proteins
C. it stores and carries hereditary information
D. it is reservoir of energy for the cell 
\n """,
"""2 The dominant phase in the life cycle of a  fern is the?
A. gametophyte 
B. prothallus
C. sporophyte
D. antheridium 
\n """,
"""3 Parental care is exhibited by
A. toads
B. snails
C. earthworms
D. birds 
\n """,
"""4 Which of the following groups of cells is devoid of true nuclei
A. algae
B. monera
C. fungi
D. viruses 
\n """,
"""5  Which of the following is true of the  transverse section of a dicot system?
A. the epidermis is completely encircled by the cortex
B. the xylem is more interiorly located than the phloem
C. the cambium lies between the cortex and the vascular bundles
D. the vascular bundles are randomly scattered within the cortex 
\n """,
"""6  Which of the following is lacking in the  diet of a person with kwashiorkor?
A. vitamins 
B. proteins
C. carbohydrates 
D amino acid 
\n """,
"""7 The mode of nutrition of sun dew and bladder wort can be described as
A. autotrophic 
B. saprophytic
C. holozoic
D. chemosynthetic 
\n """,
"""8  When the mixture of a food substance and Benedict's solution was warmed, the solution changed from blue to black-red. This indicates the presence of
A. reducing sugar
B. fatty acid
C. sucrose
D. amino acid 
\n """,
"""9 The primary structure responsible for  pumping blood for circulation through the mammalian circulatory systems is the 
A. veins
B. right auricle
C. arteries
D. left ventricle 
\n """,
"""10 Circulation of blood to all parts of the  body except the lungs is through
A. the pulmonary artery 
B. systemic circulation
C. the lymphatic system
D. pulmonary circulation 
\n """,
"""11 Yeast respires anaerobically to convert  simple sugar to carbon (IV) oxide and
A. alcohol 
B. acid
C. oxygen
D. water 
\n """,
"""12 The sheet of muscle that separates the thoracic and the abdominal cavities is the
A. diaphragm
B. intercostal muscle
C. pleural membrane
D. pericardium 
\n """,
"""13  The oily substance that lubricates the  mammalian hair to keep it flexible and water repellent is secreted by the 
A. sweet glands 
B. sebaceous glands
C. fatty cells
D. granular layer 
\n """,
"""14  The outer layer of the kidney where the  Bowman's capsules are found is the
A. cortex 
B. pelvis
C. medulla
D. pyramid 
\n """,
"""15 Which of the following stimuli is likely to  elicit a nastic response in an organism?
A. Touch 
B. Light intensity
C. Chemical substances
D. Gravity 
\n """,
"""16 In the male reproductive system of a mammal, sperm is stored in the
A. van deferens
B. urethra
C. epididymis
D. seminiferous tubules 
\n """,
"""17  Chemosynthetic organisms are capable  of manufacturing their food from simple inorganic substances through the process of 
A. oxidation
B. denitrification 
C. reduction
D. phosphorylation 
\n """,
"""18 The part of the human gut that has an acidic content is the
A. stomach 
B. duodenum
C. ileum
D. colon 
\n """,
"""19 I. Stomata → Spirogyro II. Alveoli → Earthworm III. Malpighian tubule → Mammal IV. Contractile vacuole → Protozoa. Which of the above structures is correctly matched with the organisms in which it is found?
A. III
B. II 
C. I
D. IV 
\n """,
"""20. A food chain always begins with a
A. consumer
B. decomposer
C. producer
D. primary consumer 
\n """,
"""21 Mycorrhizae promote plant growth by 
A. absorbing inorganic ions from the soil
B. protecting it from infection
C. helping it to utilize atmospheric nitrogen
D. serving as a growth regulator 
\n """,
"""22  The barrier between maternal and foetal  blood is the
A. placenta 
B. liver
C. umbilical chord
D. uterine wall 
\n """,
"""23 The blood component that has the greatest affinity for oxygen is the
A. lymphocytes
B. leucocytes
C. erythrocytes
D. thrombocytes 
\n """,
"""24  Which of the following organisms is mainly found in the marine habitat?
A. Achatina 
B. Tilapia
C. Dog fish
D. Tortoise 
\n """,
"""25  The two halves of the pelvic girdle are  joined together at the
A. public symphysis 
B. ilium
C. pubis
D. obturator foramen 
\n """,
"""26 I. Adoption of appropriate nocturnal habits II. Burrowing III. Adjusting their internal body temperature. IV. Possession of many sweat pores.  Which of the above are ways in which  desert animals adapt to extreme heat of the environment?
A. I and IV only 
B. II and III only
C. I and II only
D. I, II and III only 
\n """,
"""27  Low annual rainfall, sparse vegetation, high diurnal temperatures and cold nights are characteristic features of the
A. tropical rainforest
B. desert
C. montane forest
D. guinea savanna 
\n """,
"""28  The activity of an organism which  affects the survival of another organism in the same habitat constitutes
A. an edaphic factor
B. an abiotic factor
C. a biotic factor
D. a physiographic factor 
\n """,
"""29  The average number of individuals of a species per unit area of the habitat is the
A. population density
B. population frequency 
C. population size
D. population distribution 
\n """,
"""30 The vector for yellow fever is 
A. Aedes mosquito
B. Anopheles mosquito
C. tsetse fly 
D. blackfly
\n """,
"""31 The loss of soil through erosion can be reduced by 
A. watering
B. crop rotation
C. manuring
D. irrigation 
\n """,
"""32 The protozoan plasmodium falciparum is transmitted by
A. female Anopheles mosquitoes
B. female Aedes mosquitoes
C. female Culex mosquitoes
D. Female blackfly 
\n """,
"""33  A dilute solution of phenylthiocarbamide tastes bitter to some people and is tasteless to others. This is an example of 
A. taste bud variation
B. discontinuous variation 
C. morphological variation
D. continuous variation 
\n """,
"""34 Thyroxine and adrenalin are examples  of hormones which control
A. blood grouping 
B. tongue rolling
C. behavioural patterns
D. colour variation 
\n """,
"""35 A pair of genes that control a trait is  referred to as
A. an allele 
B. recessive
C. dominant
D. a hybrid 
\n """,
"""36  The chromosome number of a cell before  and after the process of meiosis is conventionally represented as 
A. 2n → 2n
B. n → n 
C. n → 2n
D. 2n → n 
\n """,
"""37 If both parents are heterozygous for a  trait, the probability that an offspring will be recessive for that trait is 
A.3/4
B. 1⁄2 
C.1⁄4
D. 1 
\n """,
"""38 At what stage in the life history of a mammal is the sex of an individual set? 
A. at adolescence
B. at puberty
C. at birth
D. at conception 
\n """,
"""39 The main distinguishing features between the soldier termite and other members of the caste are the
A. presence of wings, possession of a small head and large thorax
B. presence of wings, possession of a large thorax and a small head
C. absence of wings, possession of strong mandibles and a large head
D. absence of wings, possession of big head and the absence of mandible 
\n """,
"""40 The flippers of a whale and the fins of a  fish are examples of
A. divergent evolution
B. coevolution 
C. continuous variation
D. convergent evolution 
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "A"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2019()
def Biology_2018():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. The lowest level of organization in living organisms is
A. organ
B. cell
C. system
D. tissue 
\n """,
"""1. Which of the following is the most complex according to their cellular level of organization?
A. Heart
B. Hair 
C. Euglena
D. Hydra 
\n """,
"""2. Which of the following organisms is multi-cellular?
A. Chlamydomonas
B. Spirogyra
C. Amoeba
D. Euglena 
\n """,
"""3. In bryophytes, sex organs are produced in the
A. protonema
B. sporophyte
C. gametophyte
D. rhizoid 
\n """,
"""4. Seed plants are the most dominant vegetation on land because of
A. their motile gametes
B. their ability to photosynthesize
C. efficient seed dispersal
D. availability of water 
\n """,
"""5. Which of the following is an arboreal organism?
A. Elephant
B. Fish
C. Antelope
D. Bird 
\n """,
"""6. A circulatory system is very essential in mammals but not in smaller organisms like Amoeba because
A. amoeba lives in freshwater
B. diffusion is sufficient to transport materials in Amoeba
C. amoeba lacks blood containing haemoglobin
D. amoeba exhibits anaerobic respiration 
\n """,
"""7. In vascular plants, the sieve tubes and  companion cells are present in the
A. cambium 
B. cortex
C. xylem
D. phloem 
\n """,
"""8. The stomata of leaves are similar in function to the
A. pharynx of humans
B. scales of fish 
C. spiracle of insects
D. trachea of toads 
\n """,
"""9. The use of moist skin for respiration in  amphibians is known as
A. cellular respiration
B. cutaneous respiration
C. buccal respiration 
D. pulmonary respiration
\n """,
"""10. Water in plants is removed as water vapour through the process of
A. diffusion
B. osmosis
C. evaporation
D. transpiration 
\n """,
"""11. An example of an organ of perennation in plants is
A. rhizome
B. seed
C. petal of a flower
D. calyx of flower 
\n """,
"""12. Alternation of generation is a feature shown in
A. mosses
B. fungi
C. grasses
D. conifers 
\n """,
"""13. I. Growth is mainly apical II. Growth is specific with definite shape III. Growth is throughout life.  Which of the above correctly describes the growth pattern in plants?
A. I, II and III only
B. II and III only
C. I and II only
D. I and III only 
\n """,
"""14. Coordination and regulation of body activities in mammals are achieved by the
A. nerves and muscle
B. nerves and hormones
C. nerves only
D. hormones only 
\n """,
"""15. The Cerebellum of the Brain controls 
A. reflex action
B. muscular activity 
C. emotional expressions
D. the Endocrine system 
\n """,
"""16. The part of the brain responsible for  peristalsis is the
A. Olfactory Lobe 
B. Medulla Oblongata
C. Hypothalamus
D. Thalamus 
\n """,
"""17. Which of the following instruments is used for measuring atmospheric pressure?
A. Hydrometer
B. Hygrometer
C. Thermometer
D. Barometer 
\n """,
"""18. The influence of soil on organisms in a  habitat is referred to as
A. edaphic 
B. physiographic
C. biotic
D. topographic 
\n """,
"""19. The genetic make-up of an organism is  described as
A. allele 
B. chromosome 
C. phenotype
D. genotype 
\n """,
"""20. The major limiting factor of productivity  in the aquatic habitat is
A. food
B. temperature
C. water
D. sunlight 
\n """,
"""21. Which of the following group of  organisms feeds directly on green plants?
A. Primary Consumers
B. Secondary Consumers
C. Producers
D. Decomposers 
\n """,
"""22. A characteristic feature of tropical rainforest is that it
A. Contains trees with narrow leaves
B. Contains large number of plant species
C. Contains fewer number of plant species
D. Has total annual rainfall of less than 50cm 
\n """,
"""23. The study of how and why population size change over time is
A. Population estimation
B. Population dynamics
C. Population ecology
D. Population Cycle 
\n """,
"""24. A severe and long dry season is a  characteristic feature of
A. Sahel Savanna
B. Mangrove Swamps 
C. Sudan Savanna
D. Guinea Savanna 
\n """,
"""25. Which of the following is a nitrogen-  fixing blue-green algae of soil?
A. Rhizobium 
B. Nitrosomonas
C. Clostridium
D. Anabaena 
\n """,
"""26. The soil with highest water-retaining  capacity is
A. Clayey Soil 
B. Stoney soil
C. Sandy soil
D. Loamy Soil 
\n """,
"""27. The causative agent of Poliomyelitis is 
A. Virus
B. Fungus
C. Protozoan 
D. Bacterium
\n """,
"""28. One of the ways of controlling noise pollution in urban areas is
A. by siting industries away from  residential areas
B. that fuel should be completely  combusted by engines
C. by planting trees on both sides of the  road
D. by wearing ear devices 
\n """,
"""29. A constituent of the exhaust fumes from  electricity generating sets which causes serious pollution is 
A. Carbon (II) Oxide
B. Water Vapour
C. Ozone
D. Carbon (IV) Oxide 
\n """,
"""30. Which of the following is true of small  pox?
A. It is transmitted by bacteria
B. It can effectively be controlled with antibiotics
C. It can effectively be controlled by vaccination
D. It is a water-borne infection 
\n """,
"""31. A pollutant that is mostly associated  with acid rain is
A. Nitrogen (IV) Oxide 
B. Ozone
D vaccination
C. Fluorine 
\n """,
"""32. When the adults have reach a certain  degree of weakness, the process of binary fission is replaced by conjugation in 
A. Paramecium
B. Euglena
C. Amoeba
D. Plasmodium 
\n """,
"""33. Whorls, arches, loops and compounds are types of variation in 
A. Colour
B. Finger prints
C. Hair Colour
D. Blood group 
\n """,
"""34. A couple has 10 children, all female. Which of the following best explains the situation?
A. The sex determination was by the man's X chromosome
B. The man's sperm count is low 
C. The woman is not capable of producing male children
D. The sex determination was by the man's Y chromosome 
\n """,
"""35. A biological agent with antiviral property is
A. Interferon
B. enzyme
C. antibiotic 
D. disinfectant
\n """,
"""36. One of the advantages of outbreeding is
A. pests tolerance
B. disease resistance
C. fast growth 
D. tall height
\n """,
"""37. An individual with blood group AB can receive blood from those in blood group(s)
A. A, B, AB, O
B. A, AB and O only
C. AB only
D. A and B only 
\n """,
"""38. The stream-lined shape of fishes is an adaptation for
A. Securing mates
B. easy movement
C. obtaining food
D. defence and attack 
\n """,
"""39. An example of a poikilothermic  organism is a
A. Lizard
B. Cockroach 
C. rabbit
D. bird
\n """,
"""40. All living organisms are constantly invovled in a struggle for existence. this was proposed by 
Morgan 
Darwin 
Lamarck 
Wallace
\n """,
"""41. Adaptive radiation is illustrated in 
Modified insect mouthparts
dentition in mammals 
wings in birds and bats
appendages in insects 
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "B"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "B"),
        Question(question_prompts[41], "C"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2018()
def Biology_2017():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. The piercing and sucking mouth parts are found in
        A. grasshoppers
        B. mosquitoes
        C. termites
        D. cockroaches
        \n """,
        """1. The hormones that regulate plant growth are
        A. ethylene and auxins
        B. auxin and gibberellins
        C. cytokinin and abscisic acid
        D. ethylene and gibberellins
        \n """,
        """2. Which of the following pair of organisms exhibit parasitic association?
        A. insect and plant
        B. cattle and egret
        C. shark and remora
        D. tsetse-fly and cattle
        \n """,
        """3. Which of the following group of animals can withstand the rigour of the arid land?
        A. locust, camel, lizard and snakes
        B. monkeys, chameleon, earthworm andgrasshopper
        C. monkeys, grasshopper, snail and snakes
        D. lungfish, duck, butterfly and lizards 
        \n """,
        """4. Suture joint is found in the 
        A. hip
        B. ankle 
        C. skull
        D. elbow 
        \n """,
        """5. The organelle responsible for osmoregulation in Paramecium is
        A. flame cell 
        B. nephridia
        C. contractile vacuole
        D. Malpighian tubule
        \n """,
        """6. The platelets in mammalian blood are responsible for
        A. transporting oxygen
        B. initiating clotting
        C. removing carbon (IV) oxide
        D. destroying micro-organisms 
        \n """,
        """7. The most important factor that determines the different types of vegetation is
        A. light
        B. wind
        C. temperature
        D. rainfall 
        \n """,
        """8. When testing for the presence of starch in a leaf, the reason for dipping the decolourised leaf in hot water is to 
        A. detect the starch
        B. kill the leaf
        C. soften the leaf
        D. remove the chlorophyll 
        \n """,
        """9. The relationship between remora and shark can best be described as
        A. parasitism
        B. amensalism
        C. mutualism
        D. commensalism 
        \n """,
        """10. The major characteristic of a fresh water habitat is the possession of
        A. high turbidity 
        B. high density
        C. low salinity
        D. high current 
        \n """,
        """11. The causative organism of cholera is
        A. Clostridium sp
        B. shigella sp
        C. vibrio sp
        D. salmonella typhi 
        \n """,
        """12. The process that takes place in the dark stage of photosynthesis is
        A. oxidation of water 
        B. photolysis of water
        C. oxidation of carbon (IV) oxide
        D. reduction of carbon (IV) oxide 
        \n """,
        """13. Chlorofluorocarbons are air pollutants that originates from
        A. crude oil refining
        B. coal mining
        C. motor vehicle exhaust
        D. cooling system 
        \n """,
        """14. Which of the following is organ level of organisation?
        A. Volvox sp
        B. paramecium caudatum
        C. hydra viridis
        D. onion bulb 
        \n """,
        """15. The simplest form of reproduction is 
        A. conjugation
        B. budding
        C. spore formation
        D. binary fission 
        \n """,
        """16. Which of the following is a characteristic of wind-pollinated flower?
        A. flowers lack nectar 
        B. flowers are conspicuous
        C. flowers have perianths
        D. flowers are bisexual 
        \n """,
        """17. In an experiment to determine the humus in a soil sample the following results were obtained Mass of dish - 20g Mass of dry soil - 7.5g Mass of dish + soil after burning = 25g The percentage of humus in the given sample is
        A. 9.1
        B. 37.5
        C. 12.5
        D. 33.3 
        \n """,
        """18. The presence of termites and earthworms in soil promote
        A. porosity and fertility 
        B. porosity and aeration
        C. aeration and fertility
        D. acidity and aeration 
        \n """,
        """19. In a 15m2 habitat, the total number of Tridax counted using a 1.6m2 quadrant thrown randomly 50 times was 400. What is the Tridax
        A. 12 
        B. 16
        C. 8
        D. 5 
        \n """,
        """20. Which of the following is a sex-link character?
        A. Dwarfism 
        B. Albinism
        C. Tongue rolling
        D. Colour blindness 
        \n """,
        """21. The outer-most tissue of the herbaceous roots is the
        A. cuticle
        B. pericycle
        C. epidermis
        D. endodermis 
        \n """,
        """22. The respective tissues that transport water and manufactured food in plants are 
        A. xylem and phloem 
        B. phloem and tracheid
        C. phloem and xylem 
        D. xylem and tracheid 
        \n """,
        """23. An adaptive feature of plants in the savanna is
        A. fissured bark
        B. few grasses
        C. tall trees
        D. long lifespan 
        \n """,
        """24. A grasshopper's cuticle becomes green during the season and black after fire. The reasons for the change is ---
        A. obtain food
        B. predators
        C. secure mates
        D. escape detection 
        \n """,
        """25. Which of the following is the most advance plant?
        A. merchantia
        B. Dryopteris
        C. Chlamydomonas
        D. Spirogyra 
        \n """,
        """26. The soil type with the least ability to retain nutrients is
        A. sandy loam
        B. clay loam
        C. loam 
        D. sand
        \n """,
        """27. A humming bird is able to feed on nectar because its beak is
        A. short, slender and ridged
        B. short, strong and conical
        C. long, slender and slightly curved
        D. long, wide and slightly curved 
        \n """,
        """28. The effect of overcrowding is
        A. immigration
        B. reduced competition
        C. emigration
        D. reduced mortality 
        \n """,
        """29. The vertebrae that allows the skull to nod and rotate are
        A. axis and cervical
        B. atlas and thoracis
        C. axis and atlas
        D. atlas and cervical 
        \n """,
        """30. The component of the cell that determines paternity resides in the
        A. centrosome 
        B. ribosome
        C. nucleus
        D. mitochondria 
        \n """,
        """31. The insect-trapping by the leaves of Venus flytrap is an example of a 
        A. adaptive coloration 
        B. structural adaptation 
        C. environmental adaptation 
        D. behaviour adaptation 
        \n """,
        """32. Morphological variation in humans include 
        A. height, skin, colour and tongue rolling
        B. weight, finger prints and body shape 
        C. height, weight and blood group 
        D. skin colour, weight and height 
        \n """,
        """33. Which of the following is correct about blood transfusion?
        A. Group AB can only receive from groups A and B and not from group O
        B. Group O can receive from groups A and B and from AB
        C. Group B can only donate to blood group B and not to AB and O
        D. Group O can donate to groups A, B and AB but cannot receive 
        \n """,

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
        Question(question_prompts[21], "A"),
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
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2017()
def Biology_2016():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. A group of closely related organisms capable of interbreeding to produce fertile offspring are known as members of a
        A. kingdom 
        B. class
        C. family
        D. species 
         \n """,
        """1. A beaker of pond water containing few specimens of Euglena was placed in a dark room for two weeks. At the end of this period, the specimens of Euglena were still alive because they were
        A. able to carry out holozoic nutrition
        B. able to carry out photosynthesis using carbon dioxide in the pond water
        C. better adapted to life in darkness than to life in light
        D. not overcrowded 
         \n """,
        """2. The cytoplasm of the cell is considered a very important component because it
        A. regulates the amount of energy in thecell 
        B. suspends all cell organelles
        C. is the outermost part of the cell 
        D. is solely responsible for cell division
         \n """,
        """3. Red blood cells were found to have burst open after being placed in distil for an hour. This phenomenon is known as
        A. plasmolysis 
        B. diffusion
        C. haemolysis
        D. wilting 
         \n """,
        """4. The curvature movement of plants in response to the stimulus of water is called
        A. hydrotropism
        B. geotropism
        C. Phototropism
        D. thigmotropism 
         \n """,
        """5. The overall reaction in glycolysis can be summarised as
        A. C  6111205 --CO2 + 4H2O +ATP 
        B. C6H1206 ----- CO2+ 4H2O +2ATP 
        C. C61-1,206---.> CO2 + 4H2O + ADP 
        D. C6F11206 2C31-1403+ 4h + 2ADP 
         \n """,
        """6. The longest bone in the body is the 
        A. humerous
        B. femur
        C. scapula
        D. tibia 
         \n """,
        """7. Which of the following structures is not a skeletal material?
        A. Chitin 
        B. Cartilage
        C. Bone
        D. Muscle 
         \n """,
        """8. The reason why the flow of blood through the capillaries is very slow is 
        A. because the walls of capillaries are very thin
        B. to avoid high — blood pressure 
        C. to ensure that the individual does not get dizzy
        D. to allow adequate time for exchange of materials 
         \n """,
        """9. Which of the following groups of organisms has kidney as their excretory organ?
        A. Fishes, amphibians, birds, man
        B. Fishes, amphibians, annelids, insects
        C. Fishes, reptiles, birds, tapeworms
        D. Fishes protozoans, amphibians, man 
         \n """,
        """10. Which of the following features is not a characteristic of arteries? Arteries
        A. possess values at internals throughout their length.
        B. have thick muscular and elastic walls
        C. carry blood away from the heart
        D. transport oxygenated blood with the exception of the pulmonary artery. 
         \n """,
        """11. The reason why hospitals use saline solutions as drip instead of water is
        A. because salt is a preservative
        B. to prevent contamination of the body 
        C. to maintain the composition of body fluids
        D. to increase the number of blood cells 
         \n """,
        """12. The part of the ear which contains nerve cells sensitive to sound vibrations is the
        A. cochlea
        B. ampulla
        C. tympanum
        D. malleus 
         \n """,
        """13. Spectacles with convex lenses correct long-sightedness by
        A. converging the Light rays before they enter the eye
        B. diverging the light rays before they enter the eye
        C. reducing light intensity before it enters the eye
        D. increasing light intensity before it enters the eye 
         \n """,
        """14. A seed of a flowering plant can best be described as 
        A. radicle and plumule
        B. the developed ovule
        C. the embryo and endosperm
        D. developed ovary
         \n """,
        """15. Which of the following processes removes carbon from the atmosphere?
        A. Putrefaction 
        B. Photosynthesis 
        C. volcanic eruption
        D. Burning fuels 
         \n """,
        """16. Which of the following cycles involves the process of precipitation and transpiration?
        A. Water cycles
        B. Carbon cycle
        C. Nitrogen cycle
        D. oxygen cycle 
         \n """,
        """17. What is the critical limiting factor for plants below the photic zone in an aquatic ecosystem?
        A. Availability of nutrients
        B. Availability of water
        C. intensity of light
        D. Carbon dioxide concentration 
         \n """,
        """18. Which of the following instruments is used to estimate the number o, plants in a habitat? 
        A. Pooter
        B. Pitfall trap
        C. Quadrat
        D. Sweep net 
         \n """,
        """19. Which of the following statements is true about sandy soil? It
        A. has limited air space 
        B. is light and easy to dig
        C. drains slowly
        D. is heavy and poorly aerated 
         \n """,
        """20. Which of the following organisms is primary consumer?
        A. Dog 
        B. Sheep
        C. Grass
        D. Fungus 
         \n """,
        """21. Which of the following diseases is not hereditary?
        A. Albinism 
        B. Scabies
        C. Haemophilia
        D. Colour blindness 
         \n """,
        """22. The immediate product of meiosis in flowering plants is the
        A. sporophyte 
        B. gametophyte
        C. zygote
        D. pollen grains 
         \n """,
        """23. DNA in eukaryotic cells is contained in the
        A. central vacuole
        B. nucleus 
        C. lysosome
        D. golgi body 
         \n """,
        """24. A man who is heterozygous for the disease haemophilia marries a womanwho is double recessive for haemophilia.What percentage of their offspring wouldhave the disease?
        A. 0%
        B. 25%
        C. 50%
        D. 75% 
         \n """,
        """25. Cytokinesis of mitosis is a process that ensures that
        A. each daughter cell gets the necessary organelle
        B. there is distribution of a complete set of genes into each daughter cell.
        C. daughter cells inherit new genetic combinations.
        D. worn out organelles are excluded from daughter cells 
         \n """,
        """26. An animal which is active during the day is known as a
        A. nocturnal animal 
        B. diurnal animal
        C. terrestrial animal
        D. homoatomic animal 
         \n """,
        """27. Evidence of evolution include the following except
        A. fossil records
        B. comparative anatomy
        C. mutation of genes
        D. geographical distribution of organisms 
         \n """,
        """28. An accurate identification of a rapist can be carried out by it conducting a
        A. RNA analysis 
        B. DNA analysis
        C. blood group test  
        D. behavioural traits test 
         \n """,
        """29.A boy who is fond of swimming in a pond finds himself passing urine with traces of blood. He is likely to have contracted
        A. schistosomiasis
        B. onchocerciasis
        C. poliomyelitis
        D. salmonellosis 
         \n """,
        """30.The flippers of a whale and the fins of a fish are examples of
        A. divergent evolution
        B. coevolution
        C. continuous variation
        D. convergent evolution 
         \n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "D"),
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
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "A"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2016()
def Biology_2015():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """4. Which of the following is most advanced in the evolutionary trend of animals?
A. Liver fluke
B. Earthworm
C. Snail
D. Cockroach 
\n """,
"""5. Which of the following is the lowest category of classification?
A. Class
B. Species
C. Family 
D. Genus 
\n """,
"""6. Plants that show secondary growth are usually found among the
A. thallophytes
B. pteridophytes
C. monocotyledons
D. dicotyledons 
\n """,
"""7. The fungi are distinct group of eukaryotes mainly because they have
A. spores
B. no chlorophyll
C. many fruiting bodies
D. sexual and sexual reproduction 
\n """,
"""8. An arthropod that is destructive at early stage of its life cycle is
A. butterfly
B. mosquito
C. bee
D. millipede 
\n """,
"""9. An animal body that can be cut along its axis in any plane to give two identical parts is said to be
A. radially symmetrical
B. bilaterally symmetrical
C. asymmetrical
D. symmetrical 
\n """,
"""10. Which of the following possesses mammary gland?
A. Dogfish
B. whale
C. shark
D. catfish 
\n """,
"""11. The feature that links birds to reptiles in evolution is the possession of
A. feathers
B. break
C. skeleton
D. scales 
\n """,
"""12. Countershading is an adaptive feature that enables animals to
A. fight enemies
B. remain undetected
C. warn enemies
D. attract mates 
\n """,
"""13. Which of the following plant structures lacks a waterproof cuticle?
A. leaf
B. stem
C. root
D. shoot 
\n """,
"""14. In the mammalian male reproductive system, the part that serves as a passage for both urine and semen is the
A. urethra
B. ureter
C. bladder
D. seminal vesicle 
\n """,
"""15. In plants which of the following is required in minute quantities for growth?
A. Copper
B. Potassium
C. Phosphorus
D. Sodium 
\n """,
"""16. Which of the following organisms is both parasitic and autotrophic?
A. Sundew
B. Loran thus
C. Rhizopus
D. Tapeworm 
\n """,
"""17. A function of the hydrochloric acid produced in the human stomach during digestion is to
A. neutralise the effect of bile
B. coagulate milk protein and emulsify fats
C. stop the action of ptyalin 
D. break up food into smaller particles 
\n """,
"""18. Which of the following is a polysaccharide?
A. Glucose
B. Sucrose
C. Maltose
D. Cellulose 
\n """,
"""21. In the kidney of mammals, the site of  ultrafiltration is the
A. uriniferous tubule
B. Bowman's capsule
C. loop of Henle
D. renal tubule 
\n """,
"""22. Which of the following is involved in secondary thickening in plants?
A. Collenchyma and xylem cells
B. Vascular cambium
C. Vascular cambium and cork cambium
D. Cork cambium and sclerenchyma 
\n """,
"""23. An example of a fruit that develops from a single carpel is 
A. okro
B. tomato
C. bean
D. orange 
\n """,
"""25. The function of the part labelled lll is to 
A. produce egg cells
B. protect sperms during fertilization
C. secrete hormones during coitus 
D. protect the developing embryo
\n """,
"""26. Plant growth can be artificially stimulated by the addition of
A. gibberellin
B. kinin
C. abscisic acid
D. ethylene 
\n """,
"""27. The autonomic nervous system consists  of neurons that control the
A. voluntary muscles 
B. heart beat
C. tongue
D. hands 
\n """,
"""28. Plants of temperate origin can be grown in tropical areas in the vegetation zones of the
A. rain forest
B. Guinea savanna 
C. Sudan savanna
D. montane forest 
\n """,
"""29. The water cycle is maintained mainly by 
A. evaporation of water in the environment
B. evaporation and condensation of water in the environment
C. condensation of water in the environment
D. transpiration and respiration in plants 
\n """,
"""30. Organisms living in an estuarine habitat are adapted to
A. withstand wide fluctuations in temperature
B. survive only in water with low salinity
C. withstand wide fluctuations in salinity
D. feed only on phytoplankton and dead organic matter 
\n """,
"""31. The presence of stilt roots, pneumatophores, sunken stomata and salt glands are adaptive features of plants found in the
A. tropical rainforest
B. mangrove swamps
C. grassland
D. montane forest 
\n """,
"""32. Which of the following animals can exist solely on the water they get from food and metabolic reactions?
A. forest arboreal dweller
B. Desert dwellers
C. forest-ground dweller
D. rainforest dwellers 
\n """,
"""33. The most likely first colonizers of a bare rock are
A. mosses 
B. ferns
C. lichen
D. fungi 
\n """,
"""34. The carrying capacity of a habitat is  reached when the population growth begins to
A. increase slowly 
B. increase exponentially
C. slow down
D. remain steady 
\n """,
"""35. The abiotic factors that control human  population include
A. disease and famine 
B. space and rainfall
C. flooding and earthquake
D. temperature and disease 
\n """,
"""36. An indigenous method of renewing and  maintaining soil fertility is by
A. clearing farms by burning 
B. planting one crop type 
C. adding inorganic fertilizers yearly
D. crop rotation and shifting cultivation 
\n """,
"""37. The diseases caused by water-borne  pathogens include
A. gonorrhoea and poliomyelitis
B. typhoid and syphilis
C. tuberculosis and cholera
D. typhoid and cholera 
\n """,
"""40. Which of the following is true in blood  transfusion?
A. person of blood group AB can donate blood only to another person of blood group AB
B. persons of blood groups A and B can donate or receive blood from each other
C. A person of blood group AB can receive blood only from persons of blood group A or B
D. A person of blood group O can donate only to a person of blood group O 
A. \n """,
"""41. A yellow maize is planted and all the  fruits obtained are of yellow seeds. When they are cross-bred, yellow seeds and  white seeds are obtained in a ratio 3:1. The yellow seed is said to be 
A. non-heritable
B. sex-linked
C. a recessive trait
D. a dominant trait 
\n """,
"""42. When a colour-blind man marries a carrier woman. What is the probability of their offspring being colour blind?
A. 25%
B. 50%
C. 75%
D. 100% 
\n """,
"""43. The correct base pairing for DNA is 
A. adenine → thymine and guanine → cytosine
B. adenine → guanine and thymine → cytosine
C. adenine → cytosine and guanine → thymine
D. adenine → adenine and cytosine → cytosine 
\n """,
"""46. The short thick break in birds is an adaptation for
A. crushing seeds
B. sucking nectar
C. tearing flash
D. straining mud 
\n """,
"""47. The basking of Agama lizards in the sun is to
A. change the colour of their body
B. raise their body temperature to become active
C. fight to defend their territories
D. attract the female for courtship 
\n """,
"""48. The significance of a very large number of termites involved in nuptial swarming is to
A. provide birds with plenty of food
B. ensure their perpetuation despite predatory pressure
C. search for a favourable place to breed
D. ensure that every individual gets a mate 
\n """,
"""49. The use and disuse of body parts and the inheritance of acquired traits were used to explain 
A. Darwin's theory
B. Lamarek's theory
C. genetic drift
D. gene flow 
\n """,
"""50. From his study of Galapagos finches, Darwin derived his theory of evolution from
A. comparative anatomy
B. comparative physiology
C. fossil remains
D. comparative embryology 
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "B"),
        Question(question_prompts[39], "B"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2015()
def Biology_2014():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. The process in which complex substances are broken down into simpler ones is referred to as
A. anabolism
B. catabolism
C. metabolism
D. tropism 
 \n """,
"""1. The organ which is sensitive to light in Euglena is the
A. gullet
B. flagellum
C. chloroplast
D. eyespot 
 \n """,
"""2. The organelles present in cells that are actively respiring and photosynthesizing are
A. lysosomes and ribosomes
B. Golgi apparatus and endoplasmic reticulum
C. nucleus and centrioles
D. mitochondria and chloroplast 
 \n """,
"""3. Taenia solium can be found in
A. cow
B. goat
C. dog
D. pig 
 \n """,
"""4. The structure labelled II is the
A. spermathecal pore
B. cocoon
C. clitellum
D. chaetae 
 \n """,
"""5. The organism is found in soils rich in
A. mud
B. humus
C. clay
D. sand 
 \n """,
"""6. Which of the following describes a characteristic of arthropods?
A. The organism finds it easy to grow freely
B. the organism has a pair of jointed appendages
C. the body is not divided into a number of segments seg
D. the body is covered by chitin 
 \n """,
"""7. Which of the following distinguishes a butterfly from a moth?
A. the wings of butterfly rest horizontally but those of moth rest vertically
B. Both are active during the day
C. they have similar antennae
D. the abdomen of moth is fatter than that of butterfly 
 \n """,
"""8. Which of the following types of feathers is used for flight in birds?
A. Quill
B. Filo plume
C. Covert
D. Down 
 \n """,
"""9. The plants that grow in deserts or very dry areas are referred to as
A. mesophytes 
B. hydrophytes 
C. epiphytes
D. xerophytes 
 \n """,
"""10. Which of the following is the simplest living organism?
A. Paramecium
B. Virus
C. Amoeba
D. Chlamydomonas 
 \n """,
"""11. Proboscis is a structure that is mostly found in
A. insects
B. tapeworms
C. amphibians
D. molluscs 
 \n """,
"""12. The structural adaptation of desert plants for water conservation is
A. broad leaves with numerous stomata
B. spongy mesophyll
C. spiny leaves
D. prominent stomata in leaves 
 \n """,
"""13. The long and sharp clawed feet of birds is an adaptation for
A. crushing seeds
B. scooping mud
C. tearing flesh
D. grasping prey 
 \n """,
"""14. During the manufacture of food by plants, which of the following organism use energy from the sun?
A. anabaena
B. sulphur bacteria
C. Nitrosomonas sp.
D. Nitrobacter sp. 
 \n """,
"""15. Movement of minerals and chemical compounds with a plant occurs during
A. osmosis
B. translocation
C. transpiration
D. diffusion 
 \n """,
"""16. The enzyme that is present in the saliva  is 
A. rennin
B. lipase
C. pepsin
D. ptyalin 
 \n """,
"""17. Plants that have special devices for trapping and digesting insects are
A. carnivorous
B. symbiotic
C. parasitic
D. saprophytic 
 \n """,
"""18. The process of transforming the chemical energy of cellular fuels into the high energy bonds of ATP in plants is
A. autotropism
B. photosynthesis
C. photolysis
D. respiration 
 \n """,
"""19. Fungi are referred to as hetotrophs because they
A. are filamentous
B. lack chlorophyll
C. have mycelium
D. lack roots 
 \n """,
"""20. An example of a parasitic protozoan is
A. Paramecium
B. Plasmodium
C. Euglena
D. Chlamydomonas 
 \n """,
"""21. Which blood cell are involved in the immune response of vertebrates?
A. Phagoecytes
B. lymphocytes
C. erythrocytes
D. monocytes 
 \n """,
"""22. The blood circulatory system of vertebrates consists of
A. heart, arteries, capillaries and veins 
B. heart, aorta, capillaries and veins 
C. heart, aorta, arteries and veins 
D. heart, vena cava, arteries, and veins 
 \n """,
"""23. A plant tissue that carries water and mineral salts is the
A. cambium
B. xylem
C. cortex
D. phloem 
 \n """,
"""24. Which of the following helps in the clotting of blood?
A. Red blood cells
B. White blood cells
C. Plasma
D. Platelets 
 \n """,
"""25. Which of the following forms about 55% of the volume of the blood in man?
A. leucocytes
B. platelets
C. plasma
D. erythrocytes 
 \n """,
"""26. The part of the mammalian skin involved in excretion is the
A. sweat glands
B. Malpighian layer
C. sebaceous gland
D. horny layer 
 \n """,
"""27. Which of the following is a waste product of an insect?
A. Alkaloids
B. Uric acid
C. Sweat
D. Mucilage
 \n """,
"""28. The main structure in vertebrates that supports and protects the body is the
A. skeleton
B. ligament
C. muscle
D. joint 
 \n """,
"""29. The chitin in the exoskeleton of many arthropods is strengthened by
A. lids
B. proteins
C. calcium compounds
D. organic salt 
 \n """,
"""30. The transfer of pollen grains from the anther to a sigma is
A. propagation
B. placentation
C. pollination
D. fertilization 
 \n """,
"""31. The male reproductive organ of a flower is the
A. carpel
B. stamen
C. petal
D. sepal 
 \n """,
"""32. The gland that is found just below the hypothalamus is the
A. parathyroid
B. adrenal
C. pituitary
D. thyroid 
 \n """,
"""33. The most important plant hormone is
A. cytokinin
B. abscisic acid
C. auxin
D. gibberellin 
 \n """,
"""34. The sensory cell that responds to dim light is referred to as the
A. cone
B. lens
C. rod
D. iris 
 \n """,
"""35. The absence of anti-diuretic hormone in humans results in 
A. decreasing dehydration 
B. drastic dehydration 
C. eliminating dehydration
D. increasing dehydration 
 \n """,
"""36. Oestrogen is a hormone that is synthesized in the
A. ovaries
B. testes
C. anterior pituitary
D. adrenal cortex 
 \n """,
"""37. The eye defect cause by the development of cloudy areas in the lenses is
A. presbyopia
B. glaucoma
C. cataract
D. astigmatism 
 \n """,
"""38. A pollutant that is biodegradable is
A. crude oil
B. heavy metals
C. cellophane
D. sewage 
 \n """,
"""39. A tropical disease caused by Trypanosoma is
A. sleeping sickness
B. river blindness
C. yellow fever
D. malaria 
 \n """,
"""40. The solid part of the ecosystem is referred to as the
A. atmosphere
B. hydrosphere
C. biosphere
D. lithosphere 
 \n """,
"""41. Which of the following is caused by Treponema palladium?
A. Gonorrhoea
B. Leprosy
C. Tuberculosis 
D. Syphilis 
 \n """,
"""42. To which blood group do universal recipients belong?
A. B
B. A
C. O
D. AB 
 \n """,
"""43. The clumping together of red blood cells is
A. agglutination
B. fusion
C. transfusion
D. compatibility 
 \n """,
"""44. Physiological adaptation to very dry conditions in animals demonstrates
A. rejuvenation
B. xeromorphism
C. hibernation
D. aestivation 
 \n """,
"""45. One of adaptation of Cactus opuntia to conserve water is the reduction of
A. internodes
B. stem to leaves
C. leaves to spine
D. flower size 
 \n """,
"""46. Which of the following structure is adapted for feeding in a bird of prey?
A. Hooked break and sharp claws
B. Smooth beak and strong claws
C. Big beaks and strong feet
D. Pointed beak and strong claws 
 \n """,
"""47. The special pigment for colour change in chameleon is
A. melanin
B. carotenoid
C. chromatin
D. chromatophore 
 \n """,
"""48. The behavioural adaptation in social  insects could best be described as 
A. symbiosis 
B. saprophytism 
C. parasitism 
D. commensalisms  
 \n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "D"),
        Question(question_prompts[42], "D"),
        Question(question_prompts[43], "A"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "A"),
        Question(question_prompts[47], "A"),
        Question(question_prompts[48], "A"),

    ]
    def run_test(questions):
        score = 0
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2014()
def Biology_2013():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """1. Which of the following has the most primitive respiratory system?
A. insect
B. fish
C. snail
D. mouse 
 \n """,
"""2. One adaptation shown by hydrophytes in fresh water habitats is the
A. waxy cuticle on shoot surface
B. poor development of roots and xylem  tissues
C. well-developed roots and supporting  system
D. leaves reduced to spines 
 \n """,
"""3. Which of the following use diffusion as the principal method of gaseous exchange?
A. grasshopper
B. rat spines
C. lizard
D. earthworm 
 \n """,
"""4. The theory which supports the view that the large muscles developed by an athlete will be passed on to the offspring was proposed by
A. Mendel
B. Darwin
C. Lamark
D. Pasteur 
 \n """,
"""5. The chromosomes of members of the kingdom Monera are within the
A. nucleoplasm
B. nucleus
C. nucleolus
D. cytoplasm 
 \n """,
"""6. The mangrove swamp in Nigeria is restricted to the
A. Sahel savanna 
B. Guinea savanna 
C. Tropical rainforest 
D. Sudan savanna 
 \n """,
"""7. The pancrease secretes enzymes for the digestion of
A. fats, proteins and carbohydrates
B. fats, vitamins and cellulose
C. fats, carbohydrates and vitamins
D. proteins, cellulose and minerals 
 \n """,
"""8. The causative agent of bird flu is a
A. protozoan
B. virus
C. bacterium
D. fungus 
 \n """,
"""9. A water medium is necessary for fertilization in
A. conifers
B. angiosperms
C. ferns
D. fungi 
 \n """,
"""10. An example of a sex-linked trait is the
A. colour of the skin in humans
B. ability to roll the tongue
C. possession of facial hair in adult humans
D. ability to grow. long hair in females 
 \n """,
"""11. In which of the following Nigerian states can montane vegetation be found?
A. Bauchi
B. Plateau
C. Taraba
D. Enugu 
 \n """,
"""12. Which of the following is true of cloning?
A. it is welcomed as an ethically and normally sound science
B. it involves the asexual multiplication of the tissues of the original organism
C. the clone is similar to but not exactly like the original organism 
D. only one cell of the original organism is needed to imitate the process  
 \n """,
"""13. The process of shedding the exoskeleton of an arthropod is known as
A. ecdysis
B. in star formation
C. metamorphosis
D. osmosis 
 \n """,
"""14. Which of the following is a major cause of constipation in humans?
A. lack of roughage
B. vitamin B
C. vitamin E
D. lack of salts 
 \n """,
"""15. In mammals, the organ directly on top of the kidney is the
A. adrenal gland
B. prostate gland
C. pancrease
D. thyroid gland 
 \n """,
"""16. An accurate identification of a rapist can be carried out by conducting a
A. RNA analysis
B. blood group test
C. behavioural traits test
D. DNA analysis 
 \n """,
"""17. An example of a fish that aestivates is
A. croaker
B. lung fish
C. shark
D. cat fish 
 \n """,
"""18. The opening and closing of the stoma are regulated by
A. respiration
B. osmosis
C. diffusion
D. transpiration 
 \n """,
"""19. Which of the following is common to the mosquito, housefly and blackfly? 
A. they are parasites of man
B. their immature stages are aquatic
C. they undergo complete metamorphosis
D. their adults have two pairs of wings 
 \n """,
"""20. The organs that will be most useful to giant African rats in finding their way in underground habitats are the
A. nostrils
B. eyes
C. vibrissae
D. tails 
 \n """,
"""21. A crucible of 5gm weighed 10gm after filling with fresh soil. It is then heated in an oven at 1000C for 1 hour. After cooling in a desiccator, the weightwas 8gm. The percentage of water in thesoil is
A. 0.8
B. 0.2
C. 0.4
D. 0.6 
 \n """,
"""22. The waste product of plants used in the conversion of hide to leather is
A. alkaloid
B. resin
C. tannin
D. gun 
 \n """,
"""23. The correct sequence of the movement of urea during formation is
A. glomerulus - Bowman's capsule -convoluted tubule - Henle's loop -collecting tubule
B. convoluted tubule - glomerulus -Henle's loop - Bowman's capsule -collecting tubule
C. glomerulus - Bowman's capsule-convoluted tubule - Henle's loop collecting tubule 
D. convoluted tubule - Bowman's capsule- Henle's loop -glomerulus - collectingtubule 
 \n """,
"""24. In lizards, the lowing of the gularfold is used to
A. defend their territory
B. attract mates
C. frighten enemies
D. catch insects 
 \n """,
"""25. The photosynthetic pigments include
A. chloroplast and cytochromes
B. melanin and haemoglobin
C. chlorophyll and carotenoids
D. carotenoids and haemoglobin 
 \n """,
"""26. The highest level of ecological organization is the
A. ecosystem
B. niche
C. biosphere
D. population 
 \n """,
"""27. A biotic factor which affects the distribution and abundance of organism in a terrestrial habitat is
A. pH
B. competition
C. temperature
D. light 
 \n """,
"""28. The eye defect that rises because the cornea is not curved smoothly is
A. astigmatism
B. short-sightedness
C. long-sightedness
D. presbyopia 
 \n """,
"""29. Which of the following is an example of parasitism?
A. a squirrel living in an abandoned nest of a bird 
B. mistletoe growing on an orange tree 
C. fungi growing on a dead tree branch 
D. cattle egrets taking tasks from thebody of cattle 
 \n """,
"""30. The increasing order of the particle size in the following soil types is
A. cattle sand – clay-gravel
B. clay - silt sand – gravel
C. silt - clay - sand - gravel
D. clay - sand - silt – gravel 
 \n """,
"""31. Which of following factors can bring about competition population?
A. emigration
B. drought
C. mortality
D. dispersion 
 \n """,
""" 32.Stunted growth and poor rootdevelopment are a result of a deficiency in
A. phosphorus
B. calcium
C. sulphur
D. iron 
 \n """,

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
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2013()
def Biology_2012():
    students = dict()
    names = input("type your name here")
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """1. Which of the following structures is a protective adaptive feature of the Agama Lizard to the environment? 
        A. Nuchal crest
        B. Claws
        C. Scaly skin
        D. Gular fold. 
         \n """,
        """2. Which of the following adapts an insect for feeding?
        A. suitable mouthparts
        B. paired antennae
        C. segmented body
        D. jointed appendages 
         \n """,
        """3. Which of the following results from the cross between Yy and Yy?
        A. 2Yy-2yy
        B. 2Yy:yy:YY
        C. YY:2Yy:yy
        D. YY: Yy:2yy 
         \n """,
        """4. Which of the following is NOT part of thecarbon cycle?
        A. Organic carbon
        B. Decomposition
        C. Nitrates formation
        D. Photosynthesis 
         \n """,
        """5. I. Tissues II. System III. Cell IV. Organs Which of the above is the level of organization of a leaf?
        A. IV
        B. I.
        C. III.
        D. II. 
         \n """,
        """6. In cellular respiration, energy is stored in the form of
        A. heat energy
        B. adenosine diphosphate
        C. adenosine monophosphate 
        D. adenosine triphosphate 
         \n """,
        """7. The principal organ for the manufacture of food in autotrophy is the
        A. root hair
        B. growing root
        C. mature fruit
        D. green leaf 
         \n """,
        """8. A disease that results from lack of iodine in the diet of humans is
        A. beriberi
        B. scurvy
        C. rickets
        D. goiter 
         \n """,
        """9. The process whereby some organism with certain favourable features get establishedin an area is
        A. gene mutation
        B. dispersal
        C. overcrowding
        D. natural selection 
         \n """,
        """10. The rise and fall of ocean water during the day is referred to as
        A. gravity
        B. a pull
        C. tide
        D. zone 
         \n """,
        """11. Which of the following is a producer in an aquatic habitat?
        A. Nymphaea
        B. Dryopteris
        C. planarian
        D. Similium 
         \n """,
        """12. The relationship that exist between a shark and Remora is
        A. parasitism
        B. commensalism
        C. saprophytism
        D. symbiosis 
         \n """,
        """13. I. Tissue II. System III. Cell IV Organ The correct sequence of increasing level of complexity is
        A. IV-II-III
        B. I-II-III-IV
        C. IV-III-I-II
        D. III-I-IV-II 
         \n """,
        """14. Which of the following is not an inheritable disease?
        A. Poliomyelitis
        B. Sickle-cell anaemia
        C. Mental illness
        D. Haemophilia 
         \n """,
        """15. Which of the finger print types occur most frequently in the population of human beings 
        A. Double-loop
        B. Whorl
        C. Arch
        D. Loop 
         \n """,
        """16. Beriberi results from a deficiency of
        A. vitamin A
        B. vitamin E.
        C. vitamin B
        D. vitamin C 
         \n """,
        """17. Bacteria which add atmospheric nitrogen to the soil are
        A. putrefying bacteria
        B. nitrifying bacteria
        C. nitrogen fixing bacteria
        D. denitrifying bacteria 
         \n """,
        """18. The spines of the hedgehog is an adaptive features for
        A. Courtship
        B. defence
        C. water conservation 
        D. obtaining food 
         \n """,
        """19. The dental formula of carnivores is represented by 
        A. I 0⁄3, C 1⁄1, pm 4⁄4, m 2⁄3
        B. I 0⁄2, C 1⁄1, pm 4⁄4, m 2⁄4
        C. I 2⁄3, C 2⁄1, pm 3⁄4, m 2⁄3
        D. I 3, C 1⁄1, pm 4⁄4, m 2⁄2
         \n """,
        """20. Which of the following instruments is used to measure temperature?
        A. Thermometer
        B. Hygrometer
        C. Anemometer
        D. Hydrometer 
         \n """,
        """21. In human, puffiness and water retention in the body is a possible symptom of
        A. bladder malfunction
        B. poor digestion
        C. kidney malfunction
        D. obesity 
         \n """,
        """22. The theory of evolution which postulates that all living organisms have a common ancestor was proposed by
        A. Linnaeus
        B. Darwin
        C. Lamarck
        D. Mendel 
         \n """,
        """23. Mammals requires roughage in their food to
        A. provide energy
        B. slow down aging
        C. ease digestion
        D. prevent disease 
         \n """,
        """24. Variation can occur among offspring of living organism because 
        A. seeds are produced by self-pollination
        B. zygotes are produced by cross fertilisation
        C. they are produced by binary fission
        D. they are produced without fertilisation 
         \n """,
        """25. The most important biotic factors which affect plants and animals in the habitat are
        A. temperature and rainfall
        B. temperature and turbidity
        C. salinity and relative humidity
        D. rainfall and relative humidity 
         \n """,
        """26. The lowest unit of classification is the
        A. Kingdom
        B. class
        C. phylum
        D. species 
         \n """,
        """27. Two important process involved in the absorption and transport of materials in plants are
        A. flaccidity and turgidity
        B. diffusion and plasmolysis
        C. plasmolysis and capillarity
        D. osmosis and diffusion 
         \n """,
        """28. A series of organism existing in an ecosystem through which energy is transformed can be referred to as
        A. food cycle
        B. food chain
        C. pyramid on numbers
        D. food web 
         \n """,
        """29. The cell organelle solely responsible for respiration is the
        A. nucleus
        B. nucleolus
        C. endoplasmic reticulum
        D. mitochondrion 
         \n """,
        """30. In which part of Nigeria are Mangrove swamps found?
        A. Chad Basin
        B. Niger Delta
        C. Benue Valley
        D. Mambilla Plateau 
         \n """,
        """31. The breeding methods that are useful in selective breeding of animals and plants are 
        A. inbreeding and cross- breeding
        B. inbreeding and hetero-breeding
        C. inbreeding and out-breeding
        D. inbreeding and self-breeding 
         \n """,
        """32. In a small unicellular organism, diffusion is sufficient for transport because
        A. the surface area to volume ratio is small
        B. they have lungs for diffusion
        C. materials have to move over long distance
        D. the surface area to volume ratio is large 
         \n """,
        """33. The function of the spinal cord is to
        A. stand the body structure erect
        B. control involuntary actions
        C. transmit impulses to the brain
        D. regulates developmental changes 
         \n """,
        """34. The first vertebrates to ventures out of water and lives on land are the
        A. Pisces
        B. Amphibians
        C. Reptiles
        D. Aves 
         \n """,
        """35. Which of the following factors mostly determine the major biomes of the world.
        A. pressure and wind speed
        B. temperature and wind speed
        C. pressure and rainfall
        D. Temperature and rainfall 
         \n """,
        """36. I. Strong winds II. high temperature III. Dry and porous soils. Which group of plants are specially adapted to grow under environmental conditions stated above?
        A. Thallophytic
        B. Mesophytes
        C. Xerophytes
        D. Hydrophytes 
         \n """,
        """37. The lowest unit of a biogeographical plant species is
        A. micro flora
        B. macro fauna
        C. micro fauna
        D. macro flora 
         \n """,
        """38. Which of the following is rich source of vitamin K?
        A. Tomato
        B. Guava
        C. Milk
        D. Onion
         \n """,
        """39. Severe diarrhea, dehydration and weakness are symptoms of 
        A. cholera
        B. chickenpox
        C. malaria
        D. yellow fever 
         \n """,
        """40. A common characteristic found among the crustaceans is the possession of
        A. a pair of antennae
        B. a pair of walking legs on each segment
        C. four pairs of walking legs on the cephalothorax
        D. two pairs of antennae 
         \n """,
        """41. In which of the following groups of invertebrates are flagella and cilia found
        A. annelids
        B. protists
        C. coelenterates
        D. Anthropods 
         \n """,
        """42. Physiological variation in human population is evidence in the
        A. difference in the fingerprints
        B. physical appearance of individuals
        C. differences in height and weight
        D. ability to roll the tongue 
         \n """,
        """43. In photosynthesis, oxygen is liberated during 
        A. conversion of energy 
        B. photolysis
        C. splitting of carbon (IV)oxide
        D. glycolysis 
         \n """,

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
        Question(question_prompts[8], "D"),
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
        Question(question_prompts[25], "A"),
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
        print("Enter  A OR B OR C OR D or E as the case may be  AS YOUR ANSWER ")
        for question in questions:
            answer = input(question.prompt)
            answer = answer.upper()
            if answer == question.answer:
                print("you got it!! congratulation to You.")
                score+=1
            else:
                print("Wow! you can do more to imporve your scores guy!")
        print("You got " + str(score) + "/" + str(len(questions)))
        score = int((score/ len(questions) * 100))
        print("your score is: " + str(score) + "%")
        scores=[]
        scores.append(score)
        students[names]= scores
        print("created your profile",students)

    run_test(questions)
    while play_again():
        Biology_2013()