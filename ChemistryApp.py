from Question import Question
def Chemistry_2020():
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
         """0  What is the concentration of a solution containing 2g of NaOH in 100cm3 of solution? [Na = 23, O = 16, H = 1]
(A) 0.40 mol dm-³
(B) 0.50 mol dm-³
(C) 0.05 mol dm-³
(D) 0.30 mol dm-³
\n """,
"""1  Which of the following properties is NOT peculiar to matter?
(A) kinetic energy of particles increases from solid to gas
(B) Random motion of particles increases from liquid to gas 
(C) Orderliness of particles increases from gas to liquid
(D) Random motion of particles increases from gas to solid
\n """,
"""2 The principle of column chromatography is based on the ability of the constituents to
(A)  move at different speeds in the column
(B) dissolve in each other in the column
(C) react with the solvent in the column
(D) react with each other in the column
\n """,
"""3 Which of the following questions is correct about the periodic table?
(A)  The non-metallic properties of the elements tend to decrease across each period
(B) The valence electrons of the elements increase progressively across the period
(C) Elements in the same group have the same number of electron shells
(D) Elements in the same period have the number of valence electrons
\n """,
"""4 The relative atomic mass of a naturally occurring lithium consisting of 90% 5Li and 10% 6Li is
(A)  6.9
(B) 7.1 
(C) 6.2
(D) 6.8
\n """,
"""5 An isotope has an atomic number of 15 and a mass number of 31. The number of protons it contain is
(A)  16
(B) 15
(C) 46
(D) 31
\n """,
"""6 The molecular lattice of iodine is held together by
(A)  dative bond
(B) metallic bond
(C) hydrogen bond
(D) van der Waal's forces
\n """,
"""7 The arrangement of particles in crystal lattices can be studied using
(A)  X - rays
(B) γ - rays
(C) α - rays
(D) β – rays 
\n """,
"""8 The importance of sodium aluminate (III) in the treatment of water is to 
(A)  cause coagulation
(B) neutralize acidity
(C) prevent goitre and tooth decay
(D)  kill germs
\n """,
"""9 What type of bond exits between an element X with atomic number 12 and Y with atomic number 17? 
(A)  Electrovalent
(B) Metallic
(C) Covalent
(D)  Dative
\n """,
"""10 Hardness of water is mainly due to the presence of
(A) calcium hydroxide or magnesium hydroxide
(B)calcium trioxocarbonate (IV) or calcium tetraoxosulphate (VI)
(C)sodium hydroxide or magnesium Hydroxide
(D)calcium chloride or sodium chloride salts
\n """,
"""11 A suitable solvent for iodine and nephthalene is
(A) carbon (IV) sulphide
(B)ethanol
(C)water
(D)benzene
\n """,
"""12 Which of the following noble gases is commonly found in the atmosphere?
(A) Xenon
(B)Neon
(C)Helium
(D)Argon
\n """,
"""13  N₂O₄(g) ⇋ 2NO ΔH = +ve
(A) In the reaction above, an increase in temperature will
A. increase the value of the equilibrium constant
B. decreases the value of the equilibrium constant
C. increase in the reactant production
D. shift the equilibrium to the left
\n """,
"""14 CH3COOH(aq) + OH(aq) ⇋CH3COO-(aq) + H2O(l) In the reaction above, CH3COO-(aq) is
(A) conjugate base
(B)acid
(C)base
(D)conjugate acid
\n """,
"""15 How many cations will be produced from a solution of potassium aluminiumtetraoxosulphate (VI)?
(A) 3
(B) 4
(C) 1
(D) 2
\n """,
"""16 Which of the following is NOT an alkali?
(A) NH3
(B) Mg(OH)2
(C) Ca(OH)2
(D) NaOH
\n """,
"""17 An effect of thermal pollution on water bodies is that the
(A) volume of water reduces
(B) volume of chemical waste increase
(C) level of oxides of nitrogen increase
(D) level of oxygen reduces
\n """,
"""18 Which of the following is a deliquescent compound?
(A) Na₂CO₃
(B) CaCl₂
(C) CuO
(D) Na₂CO₃.10H₂O
\n """,
"""19 A chemical reaction which the hydration energy is greater than the lattice energy is referred to as
(A)  a spontaneous reaction
(B) an endothermic reaction
(C) an exothermic reaction
(D) a reversible reaction
\n """,
"""20 The function of zinc electrode in a galvanic cell is that it
(A)  undergoes reduction
(B) serves as the positive electrode
(C)  production electrons
(D) uses up electrons
\n """,
"""21 CH₄(g) + Cl₂(g) → CH₃Cl(s) + HCl(g) The major factor that influence the rate of the reaction above is
(A)  catalyst
(B) temperature 
(C) concentration
(D) light
\n """,
"""22 The condition required for corrosion to take place is the presence of
(A)  water and carbon (IV) oxide
(B) water, carbon (IV) oxide and oxygen
(C) oxygen and carbon (IV) oxide
(D) water and oxygen
\n """,
"""23 MnO4(aq) + Y + 5Fe2+(aq) → Mn2+(aq) + 5Fe2+(aq) + 4H In the equation above, Y is
(A)  5H+(aq)
(B)  4H+(aq)
(C) 10H+(aq)
(D) 8H+(aq)
\n """,
"""24 Given that M is the mass of a substance deposited during electrolysis and Q is the quantity of electricity consumed, then Faraday's first law can be written as [Electrochemical equivalent] 
(A) M=E/Q
(B) M = EQ
(C) M = Q/E
(D) M = E/2E
\n """,
"""25 The impurities formed during the laboratory preparation of chlorine gas are removed by
(A)  H₂O
(B) NH₃
(C) H₂SO₄
(D) HCl
\n """,
"""26 The effect of the presence of impurities such as carbon and sulphur on iron is that they
(A)  give it high tensile strength
(B) make it malleable and ductile
(C) increase its melting point
(D) lower its melting point
\n """,
"""27 A few drops of concentrated HNO3 is added to an unknown solution and boiled for a while. If this produces a brown solution, the cation presents are likely to be 
(A)  Pb2+
(B) Cu2+
(C) Fe3+
(D) Fe2+
\n """,
"""28 The bleaching action of chlorine gas is effective due to the presence of
(A)  hydrogen chloride
(B) water
(C) air
(D) oxygen
\n """,
"""29 In the laboratory preparation of oxygen, dried oxygen is usually collected over
(A)  hydrochloric acid
(B) mercury
(C) calcium chloride
(D) tetraoxosulphate (VI) acid
\n """,
"""30 The property of concentrated H2SO4 that makes it suitable for preparing HNO3 is its
(A)  boiling point
(B) density
(C) oxidizing properties
(D) dehydrating properties
\n """,
"""31 Bronze is preferred to copper in the making of medals because it
(A)  is stronger
(B) can withstand low temperature
(C) is lighter
(D) has low tensile strength
\n """,
"""32 The constituents of baking powder that makes the dough to rise is
(A)  NaHCO₃
(B) NaOH
(C) Na₂CO₃
(D) NaCl
 \n """,
"""33 The ability of carbon to form long chains is referred to as
(A)  alkylation
(B) acylation
(C) catenation
(D) carbonation
\n """,
"""34 Which of the following compounds will undergo polymerization reaction?
(A)  C₂H₄
(B) C₂H₅COOH
(C) C₂H₆
(D) C₂H₅0H
\n """,
"""35 An organic compound has an empirical formula CHO and vapour density of 45. What is the molecular formula?[C = 12, H = 1, O = 16]
(A) C₃H₇OH
(B) C₂H₅OH
(C) C₃H₆0₃
(D) C₂H₄0₂ 
\n """,
"""36 The number of isomers that can be obtained from C₄H₁₀ is
(A)  3
(B)  4
(C)  1
(D)  2
\n """,
"""37 Two organic compounds K and L were treated with a few drops of Fehling's solutions respectively. K formed a brick red precipitate while L, remains unaffected. The compound K is an
(A)  alkanol
(B)  alkane
(C)  alkanal
(D)  alkanone
\n """,
"""38 Which of the followingstatements is true about 2methylpropane and butane
(A)  They are members of the same homologous series
(B)  They have the same boilingpoint
(C)  They have different number ofcarbon atoms
(D)  They have the same chemical properties
\n """,
"""39  CH3COOH + C2H5OH ==== CH3COOC2H5 + H2O  The reaction above is bestdescribed as
(A)  esterification
(B)  Condensation
(C)  saponification
(D)  neutralization
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "A"),

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
        Chemistry_2020()
def Chemistry_2019():
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
         """0 Which of the following methods can be used to obtain pure water from a mixture of sand, water and methanoic acid?
 neutralization with NaOH followed by filtration
 neutralization with NaOH followed by distillation
 fractional distillation
 filtration followed by distillation
\n """,
"""1 How many atoms are present in 6.0g of magnesium? [Mg = 24, NA = 6.02 x 1023 mol]
 1.20 x 10²²
 2.41 x 10²²
 1.51 x 10²³
 3.02 x 10²³
\n """,
"""2 50 cm3 of gas was collected over water at 10oC and 765 mm Hg. Calculate the volume of the gas at s.t.p. if the saturated vapour pressure of water at 10⁰C is 5mm Hg
 49.19 cm3
 48.87 cm3
 48.55 cm3
 48.23 cm3
\n """,
"""3 An increase in the pressure exerted on gas at a constant temperature result in
 a decrease in the number of effective collisions
 a decrease in volume
 an increase in the average intermolecular distance
 an increase in volume
\n """,
"""4 2H₂(g) + O₂(g) → 2H₂O(g) In the reaction above, what volume of hydrogen would be left over when 300 cm3 of oxygen and 1000 cm3 of hydrogen are exploded in a sealed tube?
 200 cm3
 400 cm3
 600 cm3
 700 cm3
\n """,
"""5 l. Evaporation. ll. Sublimation. Ill. Diffusion. IV. Brownian motion. Which of the above can correctly be listed as evidences for the particulate nature of matter?
 I and lll only
 ll and lV only
 l, ll and lll only
 l, ll, lll and lV
\n """,
"""6  If the elements X and Y have atomic numbers 11 and 17 respectively, what type of bond can they form? 
 Dative
 Covalent
 Ionic
 Metallic
\n """,
"""7 A hydrogen atom which has lost an electron contains
 one proton only
 one neutron only
 one proton and one neutron
 one proton, one electron and one neutron
\n """,
"""8 The electronic configuration of Mg2+ is
 1s² 2s² 2P⁶ 3s²3P²
 1s² 2s² 2P⁶ 3s2
 1s² 2s² 2P⁶
 1s² 2s² 2P⁶ 
\n """,
"""9 Group VII elements are
 monoatomic
 good oxidizing agents
 highly electropositive
 electron donors
\n """,
"""10 Which of the following is used to study the arrangement of particles in crystal lattices?
 Alpha-particles
 Beta-particles
 Gamma-rays
 X-rays
\n """,
"""11 I. It has a varied composition from one place to another. ll. its constituents can be separated by physical means Ill. It contains unreactive noble gases which of the above shows that air is a mixture? 
 I and ll only
 ll and lll only
 l and lll only
 l, ll and lll
\n """,
"""12 The chemicals used to soften hard water involves the addition of
 insoluble sodium compounds which from soluble solutions of calcium and magnesium 
 soluble sodium compounds which from soluble solutions of calcium and magnesium ions
 soluble sodium compounds which from insoluble precipitates of calcium and magnesium ions
 insoluble precipitates of calcium and magnesium ions
\n """,
"""13 Chlorination of water for town supply is carried out to
 make the water colourless
 remove germs from the water
 make the water tasteful
 remove odour from the water
\n """,
"""14 The solubilities of different solutes in a given solvent can be compared by
 plotting their solubility curves on separate axes
 plotting their solubility curves on the same axes
 plotting some of the solubility curves on the x-axis and others on the y-axis 
 plotting their solubility curves on the x-axis only
\n """,
"""15 Potassium trioxochlorate (V) has a solubility of 1.5 moldm-3 at 45⁰C. On cooling this solution to a temperature of 20⁰C, the solubility was found to be 0.5 moldm-3. What mass of KCIO was crystalized out? [K = 39, Cl = 35.5 O =16]
 1.00g
 10.00g
 12.25g
 122.50g
\n """,
"""16 Which of the following pollutants is associated with brain damage?
 Carbon (ll) oxide
 Radioactive fallout
 Biodegradable waste
 Sulphur (lV) oxide
\n """,
"""17 Which of the following will produce a solution with pH less than 7 at equivalent point? 
 HNO3 + NaOH
 H2SO4 + KOH
 HC +Mg(OH)2
 HNO3 + KOH
\n """,
"""18 The number of hydroxonium ions produced by one molecule of an acid in aqueous solution is its
 basicity
 acid strength
 pH
 concentration
\n """,
"""19 During a titration experiment, 0.05 moles of carbon (lV) oxide is liberated. What is the volume of gas liberated?
 22.40 dm3
 11.20 dm3
 2.24 dm3
 1.12 dm3
\n """,
"""20 A major factor considered in selecting a suitable method for preparing a simple salt is its
 Crystalline form 
 melting point
 reactivity with dilute acids
 solubility in water
\n """,
"""21  The oxidation number of boron in NaBH4 is
 -3
  -1
 +1
 +3
\n """,
"""22 2Na2O2(s) + 2H2O(l) → 4NaOH(s) +O2(s) The substance that is oxidized in the reaction above is
 2NaO2(s)
 NaOH(s)
 H2O(s)
O2(g)
\n """,
"""23 What number of moles of Cu will be deposited by 360 coulombs of electricity? [f = 96500 C mol]
 5.36 x 10-4mole
 1.87 x 10-3mole
 9.35 x 10-4mole
 3.73 x 10-3mole
\n """,
"""24 A metal M displaces zinc from ZnCl, solution. This shows that
 electrons flow from zinc to M
 M is more electropositive than zinc
 M is more electronegative than zinc
 zinc is more electropositive than M
\n """,
"""25 An increase in entropy can best be illustrated by
 mixing of gases
 freezing of water
 the condensation of vapour
 solidifying candle wax
\n """,
"""26 The highest rate of production of carbon (lV) oxide can be achieved using
  0.05 mol-3 HCI and 5g powdered CaCO
 0.05 mol-3 HCI and 5g powdered CaCO3
 0.10 mol-3 HCl and 5g lump  powdered CaCO3
 0.025 mol-3 HCI and 5g powdered CaCO3
\n """,
"""27 2CO(g) + O2(g) ⇋ 2CO2(g) In the reaction above, high pressure will favour the forward reaction because
 high pressure favours gas formation
 the reaction is in dynamic equilibrium
 the reaction is exothermic
 the process occurs with a decrease in volume
\n """,
"""28 A piece of filter paper moistened with lead (ll) ethanoate solution turns black when the paper is dropped into a gas likely to be 
 sulphur (VI) oxide 
 hydrogen chloride
 sulphur (VI) oxide
 hydrogen sulphide
\n """,
"""29 Which of the following gases has a characteristic pungent smell, turns red litmus paper blue and forms dense white fumes with hydrogen chloride gas?
N2
N2O
Cl2
NH3
\n """,
"""30 Commercial bleaching can be carried out using
 sulphur (IV) oxide and ammonia
 hydrogen sulphide and chlorine
 chlorine and sulphur (IV) oxide
 ammonia and chlorine
\n """,
"""31 Mineral acids are usually added to commercial hydrogen peroxide to
 oxidize it 
 decompose it
 minimize its decomposition
 reduce it to water and oxygen
\n """,
"""32 Which of the following compounds will burn with a brickred colour in a nonluminous Bunsen flame?
 LiCI
 NaCl
 CaClN2
 MgClN2
\n """,
"""33 The purest form of iron which contains only about 0.1% carbon is
 pig iron
 wrought iron
 cast iron
 iron pyrite
\n """,
"""34 A common characteristic between zinc and the other transition elements is the ability to
 have variable oxidation states 
 hydrogen chloride
 sulphur (VI) oxide
 hydrogen sulphide
\n """,
"""35 The purest form of iron which contains only about 0.1% carbon is
 pig iron
 wrought iron
 cast iron
 iron pyrite
\n """,
"""36 A common characteristic between zinc and the other transition elements is the ability to
 have variable oxidation states 
 from complex ions
 act as a catalyst
 from coloured ions
\n """,
"""37 Which of the following metals is the least reactive?
 Pb
 Sn
 Hg
 Au
\n """,
"""38 Geometric isomerism can exist in
 hex-3-ene
 hexane
 prop-1-ene
 3-methyl but -1-ene
\n """,
"""39  Alkanals can be distinguished from alkanones by the reaction with
 Sudan lll stain
 starch iodide paper
 lithium tetrahydrido aluminate (lll)
 Fehling’s solution
\n """,
"""40 The isomers of C3H8O are
 1 - propanol and 2 - propanol
 1 - propanol and 1 - propanol
 2 - propanol and 2 - propanone
 2 - propanol and 1 - propanol
\n """,
"""41 Carbohydrates are large molecules with the molecular formula Cx(H2O)y. In which of the following pairs is x not equal to y?
 glucose and starch
 maltose and starch
 sucrose and fructose
 maltose and starch
\n """,
"""42 A compound contains 40.0% C, 6.7% H 53.3% O. If the molecular mass of the compound is 180, its molecular formula is [C =12, H =1, 0]
CH20
C3H6HO3
C6H6O3
C6H12O6
\n """,
"""43 The alkyne that will give a white precipitate silver trioxonitrate (V) is
 CH3CH2C ≡ CCH
 CH3C ≡ CCH2CH3
 CH3 CH2 CH2 CH2 C ≡ CH
 CH3 CH2CH2C ≡ CCH3
\n """,
"""44 The saponification of an alkanoate to produce soap and alkanol involves
 dehydration
 esterification
 hydrolysis
 oxidation
\n """,
"""45 2 - methyl propan -2- ol is an example of a
 primary alkanol
 secondary alkanol
 tertiary alkanol
 quaternary alkanol
\n """,
"""46 The final oxidation product of alkanol, alkanal and alkanoes is
 alkanoic acid
 alkanoyyl halide
 alkanoate
 alkanamide
\n """,
"""47 Ethanol reacts with concentrated tetraoxosulphate (V) acid at a temperature above 170⁰C to form
 ethanone
 ethene
 ethyne
 ethanal
\n """,
"""48 An example of oxidation – reduction enzyme is
 amylase
 protease
 lipase
 dehydrogenase
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "D"),
        Question(question_prompts[43], "C"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "A"),
        Question(question_prompts[47], "B"),
        Question(question_prompts[48], "D"),

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
        Chemistry_2019()
def Chemistry_2018():
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
        """0 The presence of an impurity in substance will cause the melting point to
         be zero
         reduce
         increase
         be stable
        \n """,
        """1 What volume of carbon (ll) oxide is produced by reacting excess carbon with 10dm3 of oxygen?
         5 dm3
         20 dm3
         15 dm3
         10 dm3
        \n """,
        """2 The rate of diffusion of a gas Y is twice that of Z If the relative molecular mass of Y is 64 and the two gases diffuse under the same conditions, find the relative molecular mass of Z
         32
         4
         8
         16
        \n """,
        """3 The radioisotope used in industrial radiography for the rapid checking of faults in welds and casting is
         Carbon-14
         phosphorus-32
         cobalt-60
         iodine-131
        \n """,
        """4 How many unpaired electrons are in the p-orbitals of a fluorine atom?
         3
         0
         1
         2
        \n """,
        """5 The radioactive emission with the least ionization power is
         α-particles
         X-rays
         γ-rays
         β-particles
        \n """,
        """ 6 The shape of the carbon (lV) oxide molecule is 
         pyramidal
         linear
         angular
         tetrahedral
        \n """,
        """7 Which of the following molecules is held together by hydrogen bond?
         CH4
         HBr
         H2SO4
         HF
        \n """,
        """ 8 The bond formed between two elements with electron configurations 1s2 2s2 2p6 3s2 and 1s2 2s2 2p4 is
         metallic
         covalent
         dative
         ionic
        \n """,
        """9 The constituent of air that acts as a diluent is
         nitrogen
         carbon (IV) oxide 
         noble gases
         oxygen
        \n """,
        """10  Steam changes the colour of anhydrous cobalt (ll) chloride from
         white to red
         blue to white
         blue to pink
         white to blue
        \n """,
        """11. An example of a hygroscopic substance is
        CuO(s)
         MgCl(S)
         CaCl2(S)
         NaOH(S)
        \n """,
        """12 If 24.4g of lead (ll) trioxonitrate (V) were dissolved in 42 g of distilled water at 20⁰C; calculate the solubility of the solute in gdm-3
         581.000
         0.581
         5.810 
         58.100
        \n """,
        """13 The solvent used for removing grease stain is
         turpentine
         ammonia solution
         ethanol
         solution of borax in water
        \n """,
        """14 In a water body, too much sewage leads to
         a decrease in the temperature of the water which cause in death of aquatic animals
         an increase in the number of aquatic animals in the water
         an increase in the bacterial population which reduces the level of oxygen in the water
         a decrease in the bacterial population which increases the level of oxygen in the water
        \n """,
        """15 10.0 dm3 of water was added to 2.0 moldm-3 of 2.5dm3 solution of HCl. What is the concentration of the final solution in mol dm-3? 
         0.4
         8.0
         2.0
         0.5
        \n """,
        """16 Three drops of a 1.0 mol dm-3 solution of HCl was added to 20cm3 of a solution of pH6.4. The pH of the resulting solution will be
         close to that of pure water
         less than 6.4
         greater than 6.4
         unaltered
        \n """,
        """17 Which of the following substances is not a salt?
         Aluminium oxide
         Sodium hydrogen trioxosulphate (V)
         Sodium trioxocarbonate (V)
         Zinc chloride
        \n """,
        """18 An insoluble salt can be prepared by
         the reaction of trioxocarbonate (V) with an acid 
         double decomposition
         the action of dilute acid on an insoluble base
         the reaction of metals with an acid
        \n """,
        """19. 2H2O(l) + 2F2(g) → 4HF +O2(g) In the reaction above, the substance that is being reduced is
        A. O2(g)
        B. H2O(g)
        C. F2(g)
        D. HF(g)
        \n """,
        """20 Zn(s) + CuSO4(aq)  → ZnSO4(aq) + Cu(s) In the reaction above, the oxidizing agent is
         CuSO4(s)
         ZnSO4(aq)
         Cu(s)
         Zn(s)
        \n """,
        """21 In an electrochemical cell, polarization is caused by
         chlorine
         oxygen
         tetraoxosulphate (Vl) acid
         hydrogen
        \n """,
        """22 Calculate the volume in cm3 of oxygen evolved as s.t.p. when a current of 5 A is passed through acidified water for 193s {F = 96500 Cmol-1, Molar volume of a gas at s.t.p. = 22.4 dm3} 
         224.000 dm3
         0.056 dm3
         0.224 dm3
         56.000 dm3
        \n """,
        """23 In an endothermic reaction, if there is a loss in entropy the reaction will
         be indeterminate
         be spontaneous
         not be spontaneous
         be at equilibrium
        \n """,
        """24 2SO2(g) + O2(g) ⇋ 2SO3(g) ΔH = −395.7kJmol−1 In the reaction above, the concentration of SO3(g) can be increased by
         decreasing the pressure
         decreasing the temperature
         increasing the temperature
         the addition of catalyst
        \n """,
        """25 The minimum amount of energy required for a reaction to take place is
         lattice energy
         ionization energy
         activation energy
         kinetic energy
        \n """,
        """26. Which of the following compounds is a neutral oxide?
        A. Carbon (IV) oxide
        B. Sulphur (Vl) oxide
        C. Sulphur (IV) oxide
        D. Carbon (ll) oxide
        \n """,
        """27 In the laboratory preparation of ammonia, the flask is placed in a slanting position so as to
         prevent condensed water from breaking the reaction flask
         enable the proper mixing of the reactions in the flask
         enhance the speed of the reaction
         prevent formation of precipitate
        \n """,
        """28 Which of the gases is employed as an anaesthesia?
         N2O
         NO2
         NH3
         NO
        \n """,
        """29 Sulphur (IV) oxide is a strong reducing agent in the presence of water due to the formation of
         hydroxide ion
         sulphur (Vl) oxide
         hydrogen sulphide
         trioxosulphate (IV) salt
        \n """,
        """30 A metal that forms soluble trioxosulphate (IV) ion is
         barium
         potassium
         manganese
         aluminium
        \n """,
        """31  Copper is displaced from the solution of its salts by most metals because it
         is a transition element
         is at the bottom of the activity series
         is very reactive
         has completely filled 3dorbitals
        \n """,
        """32The coloured nature of transition metal ions are associated with their partially filled
         f- orbital
         s- orbital
         p-orbital
         d-orbital
        \n """,
        """33 Aluminium containers are frequently used to transport  trioxonitrate (V) acid because aluminium
         has a silvery-white appearance
         has a low density
         does not react with the acid
         does not corrode
        \n """,
        """34 2-methylbutan-2-ol is an example of a
         dihydric alkanol
         tertiary alkanol
         secondary alkanol
         primary alkanol
        \n """,
        """35 The reaction between ammonia and ethyl ethanoate produces
        propanol and ethanamide
        propanol and propanamide
        ethanol and propanamide
        ethanol and ethanamide
        \n """,
        """36 The decarboxylation of ethanoic acid will produce carbon (IV) oxide and
        methane
        ethane
        propane
        butane
        \n """,
        """37  The compound that will react with sodium hydroxide to form salt and water is
         C6H12O6
         (CH3)3COH
         CH3CH=CH2
         CH3CH2COOH 
        \n """,
        """38 Which of the following compounds in solution will turn red litmus paper blue?
        ROR
        RCON(R)2
        RNH2
        RCOR
        \n """,
        """39 . The dehydration of ammonium salt of alkanoic acids produces a compound with the general formula
        ROR
        RCONH2
        RNH2
        RCOR
        \n """,
        """40 Which of the following fraction is used as raw material for the cracking process?
         kerosene
         lubricating oil
         bitumen
         diesel oils
        \n """,
        """41 Which of the following fraction is used as raw material for the cracking process?
         kerosene
         lubricating oil
         bitumen
         diesel oils
        \n """,
        """42 An organic compound contains 60% carbon, 13.3% hydrogen and 26.7% oxygen. Calculate the empirical formula (C=12, H =1, O=16)
        C5H12O
        C3H8O
        C6H13O2
        C4H9O
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "D"),
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
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "B"),
        Question(question_prompts[39], "B"),
        Question(question_prompts[40], "B"),
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
        Chemistry_2018()
def Chemistry_2017():
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
        """0 A mixture is different from a compound because
 the properties of a compound are those of its individual constituents while those of a mixture differ from its constituents
 a mixture is always homogeneous while a compounds not
 the constituent of a compound are chemically bound together while those of a mixture are not
 a mixture can be represented by a chemical formula while a compound cannot
\n """,
"""1 What is the percentage of sulphur in sulphur (IV) oxide?
 66%
 25%
 40%
 50%
\n """,
 """2 A gas X diffuses twice as fast as gas Y. If the relative molecular mass of X is 32, calculate the relative molecular mass of Y.
 128
 8
 16
 64
\n """,
"""3 200cm3 of a gas at 25⁰C exerts a pressure of 700 mmHg. Calculate its pressure if its volume increases 350 cm3 at 75⁰C.
 342.53 mmHg
 1430.54 mmHg
 467.11 mmHg
 400.00 mmHg
\n """,
"""4 An element X has electron configuration 1s2 2s2 2p6 3s5 Which of the following statements is correct about the element?
 lt has a completely filled porbital
 lt has 5 electrons in its outermost shell.
 lt belongs to group ll on the periodic table
 lt is a halogen
\n """,
"""5 Beryllium and aluminium have similar properties because they
 are both metals
 belong to the same group
 belong to the same period
 are positioned diagonally to each other
\n """,
"""6 If the difference in electronegativity of elements P and Q is 3.0. The bond that will be formed between them is
 metallic
 covalent 
 co-ordinate
 ionic
\n """,
"""7 How many protons, neutrons and electrons respectively are present in the element 60Co27?
 27, 33 and 33
 33, 27 and 27
 27, 33, and 27
 60, 33 and 60
\n """,
"""8 The radioactive radiation used in studying the arrangement of particles in giant organic molecules is
 γ- rays
 α- particles
 X- rays
 β – particles
\n """,
"""9 A silicon-containing ore has 92%28Si , 5% 29Si and 3% 30Si. Calculate the relative atomic mass of the silicon.
 14.00
 29.00 
 28.11
 28.00
\n """,
"""10 The nitrogen obtained from air has a density higher than the one from nitrogen-containing compounds because the one from air is contaminated with
 water vapour
 oxygen
 rare gases
 carbon (IV) oxide
\n """,
"""11 Water is said to be temporarily hard when it contains
 Ca(HCO3)2 and Mg(HCO3) salts
 Ca(HCO3)2 and CaCO salts
 Mg(HCO3)2 and CaSO3 salts
 CaSO4 and Ca(HCO3)4 salts
\n """,
"""12 On exposure to the atmosphere, a hydrated salt loses its water of crystallization to become anhydrous. This phenomenon is referred to as
 efflorescence 
 deliquescence
 hygroscopy
 hydrolysis
\n """,
"""13 16.55g of lead (ll) trioxonitrate (V) was dissolved in 100g of distilled water at 20⁰C, calculate the solubility of the solute in moldm-3 [Pb = 207, N = 14, O = 16]
 0.05 g
 2.00 g
 1.00 g
 0.50 g
\n """,
"""14 The dispersion of a liquid in a liquid medium will give
 an emulsion
 a fog
 a gel
 an aerosol
\n """,
"""15 The major and most effective way of controlling pollution is to
 improve machinery so that the substances released from combustion are less harmful
 pass strict laws against it by individuals and companies
 educate people on the causes and effects of pollution
 convert chemical wastes to harmless substances before releasing them into the environment
\n """,
"""16 The basicity of CH3COOH is
 4
 1
 2
 3
\n """,
"""17 The colour of litmus in a neutral medium is
purple
pink
yellow
orange
\n """,
"""18 The mathematical expression of pH is 
 log10[OH]
 log10[1/H30+]
 log10[H3O+]
 log10[1/[OH-]
\n """,
"""19 Which of the following salts will turn blue litmus red?
 Sodium tetrahydroxozincate (ll)
 Potassium hydrogen tetraoxosulphate (lV)
 Sodium trioxocarbonate (lV)
 Zinc chloride hydroxide
\n """,
"""20 Zn(s) + CuSO4(aq) → ZnSO4 + Cu(s)In the reaction above, the oxidation number of the reducing agent changes from
 0 to +4
 0 to +2
 +1 to +2
 +1 to +3
\n """,
"""21 H2O(g) + C(s) → H2(g) + CO(g)  The oxidizing agent in the reaction above is
 CO2(g)
 C(s)
 H2O(g)
 H2(g)
\n """,
"""22 Calculate the quantity of electricity in coulombs required to liberate 10g of copper from a copper compound [Cu=64, F = 96500 Cmol-1]
 32395.5
 30156.3
 60784.5
 15196.5
\n """,
"""23 How many faraday of electricity is required to produce 0.25 mole of copper?
 1.00F
 0.01F
 0.05F
 0.50F
\n """,
"""24 If the change in free energy of a system is -899 Jmol-1 and the entropy change is 10Jmol-1 at 25°C, calculate the enthalpy change.
 +2081 Jmol-1
 -2081 Jmol-1
 -649 Jmol-1
 +649 Jmol-1
\n """,
"""25 In an equilibrium reaction, which of the following conditions indicates that maximum yield of the product will be obtained?
Equilibrium constant is very large
ΔH -TΔS
ΔH>TΔS
Equilibrium constant is less than zero
\n """,
"""26 In a chemical reaction, the change in concentration of a reactant with time is
 entropy of reaction
 enthalpy of reaction
 rate of reaction
 order of reaction
\n """,
"""27 Which of the following will liberate hydrogen from dilute tetraoxosulphate (VI) acid?
 Lead
 Magnesium
 Copper
 Gold
\n """,
"""28 Fluorine does not occur in the free state in nature because
 it is a poisonous gas
 it belongs to the halogen family
 it is inert
 of its high reactivity
\n """,
"""29 In the extraction of sodium from fused sodium chloride, the anode is made of platinum because
 sodium is formed at the anode
 chlorine is formed at the anode
 sodium does not react with platinum
 chlorine does not react with platinum
\n """,
"""30 A compound that gives a brick-red colour to a nonluminous flame is likely to contain
 copper ions
 sodium ions
 calcium ions
 aluminium ions
\n """,
"""31 In the electrolytic extraction of calcium from calcium chloride, the cathode is
 zinc
 graphite
 platinum
 iron
\n """,
"""32 A few drops of NaOH solution was added to an unknown salt forming a white precipitate which is insoluble in excess solution. The cation likely present is
 Zn2+
 Pb2+
 Ca2+
 Al3+
\n """,
"""33 The general formula of haloalkanes where X represents the halide is
 CnH2n-1X.
 CnH2nX
 CnH2n+2X
 CnH2n+1X
\n """,
"""34 CH2(OH)CH(Cl)CH(Br)CH3 The IUPAC nomenclature of the  compound above is
 2-bromo-3-chlorobutanol
 3-bromo-2-chlorobutanol
 3-chloro-2-bromobutanol
 2-chloro-3-bromobutanol
\n """,
"""35 The alkanol obtained from the production of soap is
 propanol
 ethanol
 glycerol
 methanol
\n """,
"""36 Ethyne is passed through a hot tube containing organo-nickel catalyst to produce
 isoprene
 polythene
 ethanol
 benzene
\n """,
"""37 Due to the unstable nature of ethyne, it is stored by dissolving in
 ethane-1,2-diol
 propanol
 ethanoic acid
 propanone
\n """,
"""38 The process of converting starch to ethanol is
  cracking
 distillation
 fermentation
 oxidation
\n """,
"""39  The polymer used in making car rear lights is
 Perspex
 Bakelite
 polystyrene
 polyacrylonitrile  
\n """,
"""40 CH3COOC2H5(l) + H2O ⇌ CH3COOH(aq) + C2H5OH The purpose of H+(aq) in the reaction above is to
 increase the yield of products
 maintain the solution at a constant pH
 increase the rate of the hydrolysis
 decrease the rate of the reverse reaction
\n """,
"""41 A hydrocarbon has an empirical formula CH and a vapour density of 39. Determine its molecular formula. [C = 12, H = 1]
 C2H6
 C3H
 C3H
 C6H6
\n """,
"""42 Polystyrene is widely used as packaging materials for fragile objects during transportation because of its
 lightness
 low density
 high density
 high compressibility
\n """,
"""43 The process of converting linear alkanes to branched chain and cyclic hydrocarbons by heating in the presence of a catalyst to improve the quality of petrol is referred to as
 refining
 cracking
 reforming
 blending
\n """,
"""44 The petroleum fraction that is used in heating furnaces in industries is
 diesel oil
 gasoline
 kerosene
 lubricating oil
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "B"),
        Question(question_prompts[41], "D"),
        Question(question_prompts[42], "D"),
        Question(question_prompts[43], "C"),
        Question(question_prompts[44], "A"),

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
        Chemistry_2017()
def Chemistry_2016():
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
        """0  Which of the following statements is correct?
 The average kinetic enermy of a gas is directly proportional to its  temperature
 At constant temperature, the volume of a gas increases as the pressure increases.
 The pressure of a gas is inversely proportional to its volume.
 The temperature of gas is directly proportional to its volume.
\n """,
"""1 Which are the correct IUPAC names for H–CO2CH3 and CH≡CH
 Methyl methanoate and ethene
 Metanoic acid and ethyne
 Ethyl methanoate and ethyne
 Methyl methanoate and ethyne
\n """,
 """2 A solution X on mixing with AgNO3 solution, gives a white precipitate soluble in NH3. A solution Y, when added to X, also gives a white precipitate which is soluble on boiling. Solution Y contains
 Ag+ ion
 Pb2+ ion
 Pb4+ ion
 Zn2+ ion
\n """,
"""3 Methane is a member of the homologous series called
 alkenes
 alcohols
 esters
 alkanes
\n """,
"""4 Which of the following bonds exists in crystalline ammonium chloride (NHCL)?
 ionic covalent
 ionic and co-ordinate
 ionic, covalent and co- ordinate
 covalent, co-ordinate and metallic
\n """,
"""5 Some copper (II) sulphate pentahydrate (CuSO4 .5H2O), was heated at 120°C with the following results: Wt of crucible =10.00 g; Wt of crucible +CuSO4.5H2O = 14.98g; Wt of crucible + residue = 13.54g. How many molecules of water of crystallization were lost? [H= 1, Cu = 63.5, O =16, S = 32]
 1
 2
 3
 4
\n """,
"""6 12.0g of a mixture of potassium carbonate and potassium chloride were dissolved in a 250cm3 standard flask. 25cm3 of this solution required 40.00cm3 of 0.1M HCI neutralization. What is the percentage by weight of K2CO3 in the mixture (K = 39, O = 16, C = 12)
 60
 72
 82
 92
\n """,
"""7  Which of the following, groups of physical properties increases from left to right of the Periodic Table?  1. Ionization energy 2. Atomic radius 3. Electronegativity  4. Electron affinity
 1 and 2
 1, 2 and 3
 3 and 4
 1, 2, 3 and 4
\n """,
"""8 An element Z, contained 90% of 8Z 16 and 10% of 8Z 18 . its relative atomic mass is
 16.0
 16.2
 17.0
 17.8
\n """,
"""9 What are the possible oxidation numbers for an element if its atomic number is 17?
 -1 and 7
 -1 and 6
 -3 and 5
 -2 and 6
\n """,
"""10 How many valence electrons are contained in the element represented by ³¹P₁₅?
 3
 5
 15
 31
\n """,
"""11 10.0 dm3 of air containingH2S as an impurity was passed through a solution of Pb(NO3)2 until all the H2S had reacted. The precipitate of PbS was found to weigh 5.02 g. According to the equation:Pb(NO3)2 + H2S → PbS + 2HNO3 the percentage by volume of hydrogen sulphide in the air is
 50.2
 47.0
 4.70
 0.47
\n """,
"""12 A quantity of air was passed through a weighed amount of alkaline pyrogallol. An increase in the weight of the pyrogallol would result from the absorption of
 nitrogen
 neon 
 argon
 oxygen
\n """,
"""13 Water for town supply is chlorinated to make it free from
 bad odour
 bacteria
 temporary hardness
 permanent hardness
\n """,
"""14 4.0 g of sodium hydroxide in 250cm3 of solution contains
A. 0.40 moles per dm3
B. 0.10 moles per dm3
C. 0.04 moles per dm3
D. 0.02 moles per dm3
\n """,
"""15 A major effect of oil pollution in coastal waters is the
 destruction of marine life
 desalination of the water
 increase in the acidity of the water
 detoxification of the water
\n """,
"""16 In general, an increase in temperature increases the solubility of a solute in water because
 more solute molecules collide with each other
 most solutes dissolve with the evolution of heat
 more solute molecules dissociate at higher temperatures
 most solutes dissolve with absorption of heat.
\n """,
"""17 The relatively high boiling points of alkanols are due to
 ionic bonding
 aromatic character
 covalent bonding
 hydrogen bonding.
\n """,
"""18 Given that 15.00cm3 of H was required to completely neutralize 25.00cm3 of 0.125 mol dm3 NaOH, calculate the molar concentration of the acid solution
 0.925 mol dm3 
 0.156 mol dm3
 0.104 mol dm3
 0.023 mol dm3
\n """,
"""19 What volume of 0.1 mol dm3 solution of tetraoxosulphate (VI) acid would be needed to dissolve 2.86g of sodium trioxocarbonate (IV) decahydrate crystals?[H = 1, C = 12, O = 16, S= 32,Na 23].
 20cm3
 40cm3
 80cm3
 100cm3
\n """,
"""20 The solution with the lowest pH value is
 5 ml of  ⁄10 HCL
 10 ml of  ⁄10 HCL
 15 ml of  ⁄5 HCL
 20 ml of  ⁄8 HCL
\n """,
"""21 In which order are the  following salts sensitive to light? 
 Agl > AgCl > AgBr 
 AgCl> Agl > AgBr
 AgBr > AgCI > Agl
 AgCI > AgBr > Agl
\n """,
"""22 A metal m displaces Zinc from Zinc chloride solution. This shows that
 M is more electronegative than Zinc
 Zinc is above hydrogen in the series.
 M is more electropositive than zinc.
 electrons flow from zinc to m.
\n """,
"""23 Steam changes the colour of anhydrous cobalt (II) chloride from
 blue to pink
 white to red
 white to green
 blue to white
\n """,
"""24 When at equilibrium, which of the reactions below will shift to the right if the pressure is increased and the temperature is kept constant?
 2SO3(g) === 2SO2(g) + O
 2CO2(g) === 2CO(g) + O
 2H2(g) + O2(g)=== 2H
 2NO(g)=== N2(g) + O
\n """,
"""25 2CO(g)+ O2(g) → 2Co2(g) Given that ΔH [CO] is -110.4kJmol-1 and ΔH [CO] is -393.0kJmol-1, the energy change for the reaction above is
 -503.7 kJ
 -282.6 kJ
 +282.6 kJ
 +503.7 kJ
\n """,
"""26 Which of these properties gives a solid its definite shape?
 Strong intermolecular attraction
 High melting point
 High boiling point
 Weak intermolecular attraction
\n """,
"""27 When a crystal was added to the clear solution of its salt, the crystal did not dissolve and the solution remained unchanged. This showed that the solution was
 supersaturated
 concentrated
 unsaturated
 saturated
\n """,
"""28 If the electron configuration of an element is 1s2 2s2 2p5 , how many unpaired electrons are there?
 2
 5
 1
 4
\n """,
"""29 The substance that is used in the steel industry for the removal of carbon, sulphur and phosphorus impurities from pig iron is
 oxygen
 chlorine 
 nitrogen
 hydrogen
\n """,
"""30 Hydrogen sulphide gas can act as
 an oxidizing agent
 a dehydrating agent
 a bleaching agent
 a precipitating agent.
\n """,
"""31 Which of the following is used as a rocket fuel?
 HNO3
 CH3COOH
 H2SO4
 HCI.
\n """,
"""32 The bleaching action of chlorine is effective due to the presence of
 Hydrogen chloride
 Water
 Air
 Oxygen
\n """,
"""33 Mineral acids are usually added to commercial hydrogen peroxide to
 Oxidize it
 decompose it
 minimize its decomposition
 reduce it to water and oxygen.
\n """,
"""34 Aluminium containers are frequently used to transport trioxonitrate (v) acid because aluminium
 has a low density
 does not react with the acid
 does not corrode
 has a silvery - white appearance
\n """,
"""35 Ethyne is passed through a hot tube containing organo-nickel catalyst to produce
 Isoprene
 polythene
 ethanol
 benzene
\n """,
"""36 The process of converting starch to ethanol is
 cracking
 distillation
 fermentation
 oxidation
\n """,
"""37 An endothermic reaction is one during which heat is ____and can be represented by the symbol____. Which of the following combinations can be used accurately to complete the above definition?
 liberated -ΔH
 liberated +ΔH
 absorbed -ΔH
 absorbed +ΔH
\n """,
"""38  Consider the following exothermic reaction 2SO2(g) + O2(g) = 2SO3(g) . If the temperature of the reaction is reduced from 800⁰C to 500°C, and no other change takes place, then
 the reaction rate increases 
 concentration of SO decreases
 concentration of SO2 increases
 SO2 gas becomes unreactive
\n """,

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
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "C"),

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
        Chemistry_2016()
def Chemistry_2015():
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
        """0 An element X has two isotopes 20X10 and 22X10 present in the ratio 1:3. The relative atomic mass of x would be 
 20.5
 21.0
 21.5
 22.0
\n """,
"""1 200cm3 of oxygen diffuse through a porous plug in 50 seconds. how long, will 80cn3 of methane take to diffuse through the same porous plug under the same conditions
 40sec
 20sec
 14sec
 7sec
\n """,
"""2 Which of the following terms indicates the number of bonds that can be formed by an atom?
 oxidation number
 Valence 
 Atomic number
 Electronegativity
\n """,
"""3 Which of the following gases is the most dangerous pollutant?
 Hydrogen sulphide.
 Carbon Monoxide
 Sulphur(iv)oxide
 Carbon Dioxide
\n """,
"""4 A Side effect or Soft water is that. 
 It gives offensive taste
 excess calcium is precipitated
 it attacks lead contained in pipes
 it encourages the growth of bacteria.
\n """,
"""5 Farmlands affected by crude oil spillage can be decontaminated by
 adding acidic solutions
 using aerobic bacteria
 pouring water on the affected area
 burning off the oil from the area
\n """,
"""6 Which of the following functional groups will give gas bubbles when treated with a saturated solution of sodium hydrogen trioxocarbonate(iv)?
 —NH3 
 —OH 
 >C = 0
COOH
\n """,
"""7 The oxidation state of Cr inK2Cr2O7 is
 +7
 +6
 +5
 +4
\n """,
"""8 2Na2O2(s) + 2H2O(l) → 4Na0H + O2 The substance that is oxidized in the reaction above is
 2Na2O2
 NaOH(aq)
 H2O
 O2
\n """,
"""9 The nucleus of an atom contains
 protons only
 neutrons only
 protons and electrons
 protons and neutrons
\n """,
"""10 Which of the following does NOT happen when a Zinc rod is introduced into a solution of Copper (II) sulphate?
 Electrons flow towards the zinc rod
 The Zinc rod dissolves
 The temperature of the soil chances
 The blue colour of the solution gradually disappears.
\n """,
"""11 Which of the following statements is correct during the electrolysis of a caustic soda  solution using platinum electrodes?
 Oxygen gas is given off at the cathode
 Hydrogen gas is given off at the anode
 Sodium metal is deposited at the cathode
 Alkalinity at the cathode increases.
\n """,
"""12 Which of the following statements is INCORRECT?
 Fractional distillation of crude petroleum will give the following hydrocarbon fuels in order of increasing boiling point. Butane < Petrol < Kerosene
 H2C = CH will serve as a monomer in the preparation of polythene
 both but-i-ene and but-i-yne will decolourize bromine readily
 Calcium carbide will react with water to form any alkyne
\n """,
"""13 The iron (iii) oxide impurity in bauxite can be removed by
 fractional crystallization in acid solution
 dissolution in sodium hydroxide and filtration
 extraction with concentrated ammonia and reprecipitation
 electrolysis of molten mixture
\n """,
"""14 Aluminium is extracted commercially from its ore by
 heating aluminium oxide with coke in a furnace
 the electrolysis of fused aluminium oxide in cryolite
 treating cryolite with sodium hydroxide solution under pressure
 heating sodium aluminium silicate to a high temperature.
\n """,
"""15 Which of the following compounds gives a yellow residue when heated and also reacts with aqueous sodium hydroxide to give a white gelatinous precipitate  soluble in excess sodium hydroxide solution?
 (NH4)2CO3
 ZnCO3
 Al3(SO)3
 PbCO3
\n """,
"""16 The least easily oxidized of the metals below is
 Cu
 Na
 Zn
 Al
\n """,
"""17 Which of the following chlorides would exhibit the least ionic character?
 MgCl
 CaCl
 LiCl
 AlCl
\n """,
"""18 Which of the following CANNOT be obtained by fractional distillation of petroleum?
 Ether
 Methane
 Butane
 Hydrogen
\n """,
"""19 Which of the following is used as an antiknock in automobile engines?
 tetramethylsilane
 lead tetraethyl
 Glycerol
 n-heptane
\n """,
"""20 The Avogadro number of 24g of magnesium is the same as that of
 1g of hydrogen molecules
 16g of oxygen molecules
 32g of Oxygen molecules
 35.5g of chlorine molecules.
\n """,
"""21 In an electrolyte set-up to protect iron from corrosion, the iron is
 made the cathode
 made the anode 
 used with a metal of lower electropositive potential
 initially coated with tin
\n """,
"""22 The removal of rust from iron by treatment with tetraoxosulphate (vi) acid is based on the
 hydrolysis of the iron
 reaction of acid with base
 oxidation of the rust
 dehydration of the iron.
\n """,
"""23 The substance often used for vulcanization of rubber is
 Chlorine
 hydrogen peroxide
 Sulphur
 tetraoxosulphate (vi) acid
\n """,
"""24 Metals of the first transition series have special properties which are different from those of groups I and II elements because they have partially filled.
 s-orbitals
 p-orbitals
 d-orbitals
 f-orbitals
\n """,
"""25 A particle that contains 11 protons, 12 neutrons and 10 electrons is probably a
 Neutral non-metal
 metallic ion
 non-metallic ion
 neutral metal.
\n """,
"""26 A catalyst increases the rate of a chemical reaction by providing a path that
 raises the activation energy
 increases the temperature
 lowers the activation energy
 increases the concentration
\n """,
"""27 A metal M displaces Zinc from ZnCl  solution. This shows that
 electrons flow from Zinc to M
 M is more electropositive than Zinc 
 M is more electronegative than Zinc
 Zinc is more electropositive than M.
\n """,
"""28 Calculate the quantity of electricity in coulombs required to liberate 10g of copper from a copper compound.[Cu 64 F = 96500c]
 32395.5
 30156.3
 60784.5
 15196.6
\n """,
"""29 The IUPAC names for the compounds CH3COOH and CH2=CH2 are respectively
 acetic acid and ethane
 ethanoic- acid and ethene
 methanoic acid and ethylene
 ethanol and ethene.
\n """,
"""30 The boiling point of water is higher than that of methanol because
 water is an oxide while methanol is an alcohol
 inter-molecular forces in water are stronger than those in methanol
 Water is an inorganic compound while methanol is organic
 Water is a compound while methanol is a covalent compound
\n """,
"""31 Which combination of the following statements is correct?  1. Lowering the activation energy 2. conducting the reaction in a gaseous state.  3. Increasing the temperature.   4. removing the products as soon as they are formed.  5. Powdering the reactant if solid 
 1, 2 and 3
 1, 3 and 5
 2, 3 and 5
 3 and 4
\n """,
"""32 An element with atomic number twelve is likely to be
 electrovalent with a valency of 1
 electrovalent with a valency of 2
 covalent with a valency of 2.
 covalent with valency of 4.
\n """,
"""33 Which of the following physical properties decreases across the periodic Table? 
 ionization potential
 Electron affinity
 Electronegativity
 Atomic radius.
\n """,
"""34 If a gas occupies a container of volume 146cm3 at 18⁰c and 0.971 atm, its volume in cm3 at s.t.p is
 133
 146
 266
 292
\n """,
"""35 50cm3 of carbon (ii) oxide was exploded with 150cm3 of air containing 20% oxygen by volume, which of the reactants was in excess?
 Carbon (ii) oxide
 Carbon (iv) oxide
 Oxygen
 Nitrogen
\n """,
"""36 The formula CH2O for ethanoic acid is regarded as its
 molecular formula
 general formula
 empirical formula
 Structural formula
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "C"),

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
        Chemistry_2015()
def Chemistry_2014():
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
        """0 The periodic classification of the elements is an arrangement of the elements in order of their
 atomic weights
 isotopic weights
 molecular weights
 atomic numbers
\n """,
"""1 If 1 litre of 2.2M sulphuric acid is poured into a bucket containing 10 litres of water, and the resulting solution mixed thoroughly, the resulting sulphuric acid concentration will be
2.2 M
1.1 M
0.22 M
0.11 M
\n """,
"""2 A correct electrochemical series can be obtained from K, Na, Ca, Al, Mg. Zn, Fe, Pb, H, Cu, Hg, Ag, Au by interchanging
A. Al and Mg
B. Zn and Fe
C. Zn and Pb
D. Pb and H
\n """,
"""3 A basic postulate of the kinetic theory of gases is that the molecules of a gas move in straight lines between collisions. This implies that
collisions are perfectly elastic
forces of repulsion exist
forces of repulsion and attraction are in equilibrium 
collisions are inelastic.
\n """,
"""4 On which of the following is the solubility of a gaseous substance dependent?  I. Nature of solvent  II. Nature of solute III. Temperature  IV. Pressure
 I, II, III and IV
 I and II only
 II only
 I, III and IV only.
\n """,
"""5 Which of the following statements is correct about the periodic table?
 Elements in the same period have the same number of valence electrons
 The valence electrons of the elements in the same period increase progressively across the period. 
 Elements in the same group have the same number of electron shells
 The non-metallic properties of the elements tend to decrease across each period.
\n """,
"""6 The boiling of fat and aqueous caustic soda is referred to as
 hydrolysis
 esterification
 acidification
 saponification
\n """,
"""7 Which of the following pairs of substances will react further with oxygen to form a higher oxide?
CO2 and H2O
NO and H2O
CO and CO
SO2 and NO
\n """,
"""8 In the preparation of oxygen by heating KCIO3 in the presence of MnO2 , only moderate heat is needed because the catalyst acts by 
lowering the pressure of the reaction
increasing the surface area of the reaction 
increasing the rate of the reaction 
lowering the energy barrier of the reaction
\n """,
"""9 What volume of oxygen will remain after reacting 8cm3 of hydrogen gas with 20cm3 of oxygen gas? 
 10cm3
 12cm3
 14cm3
 16cm3
\n """,
"""10  If one of the following oxides is heated with hydrogen or carbon using a Bunsen burner, it is not reduced to the metal. Which one is it?
 lead oxide
 Magnesium oxide
 Copper oxide
 Tin oxide
\n """,
"""11 The name for CH(CH3)2CH2CH3
 1 -methylpentane 
 3-methylbutane
 2-methylbutane
 1 -dimethylpropane
\n """,
"""12 An aqueous solution of a metal salt M, gives a white precipitate with NaOH which dissolves in excess NaOH. With aqueous ammonia, the solution of M also gives a white precipitate which dissolves in excess ammonia. Therefore, the cation in M is
 Zn2+
 Ca2+
 Al3+
 Pb2+
\n """,
"""13  What is the concentration of a solution containing 2g of NaOH in 100cm3 of solution?[Na = 23, O =16, H =1]
 0.40 mol dm-3
 0.50 mol dm-3
 0.05 mol dm-3
 0.30 mol dm-3
\n """,
"""14 How many atoms are present in 6.0g, of magnesium?[Mg =24, NA =6.02 x 1023 mol].
1.20 x 1022
2.41 x 1022 
1.51 x 1023
3.02 x 1023
\n """,
"""15 The radio isotope used in industrial radiography for the rapid checking of faults in welds and casting is
 carbon - 14
 Phosphorus - 32
 Cobalt
 Iodine - 131
\n """,
"""16 Beryllium and Aluminium have similar properties because they 
 are both metals
 belong to the same group
 belong to the same period
 are positioned diagonally to each other
\n """,
"""17 mE + Nf ⇄ pG + qH  In the equation above, the equilibrium constant is given by
[E]M[F]N/[G]p[H]q
[E][F]/[G][H]
[G]p[H]2/[E]M[F]N
[G][H]/[E][F]
\n """,
"""18 (i) 3CuO(s) + 2NH3(g) ⇄ 3Cu + 3H2O(l) +N2 (ii) 2NH3(g) + 3CI2(g) ⇄ 6HCI + N2 (iii) 4NH3(g) + 3O2(g) ⇄ 6H20 +2N2(g) The reactions represented by the equations above demonstrate the
 basic properties of ammonia
 acidic properties of ammonia
 reducing properties of ammonia
 oxidizing properties of ammonia
\n """,
"""19  The salt that reacts with dilute hydrochloric acid to produce a pungent smelling gas which (s)decolourizes acidified purple potassium tetraoxomanganate (VII) solution is
 Na2SO4
 Na2SO3
 Na2S
 Na2CO3
\n """,
"""20 The refreshing and characteristic taste of soda water and other soft drinks is as a result of the presence in them of
 carbon (IV) oxide
 carbon (II) oxide
 soda
 glucose
\n """,
"""21 Which of the following are mixtures?  i. Petroleum  ii. Rubber latex.  iii. Vulcanizer's solution  iv. Carbon (II) sulphide
 i, ii and iii
 i, ii and iv 
 i and ii only
 i and iv.
\n """,
"""22 A balanced chemical equation obeys the law of
 conservation of mass
 definite proportions
 multiple proportions
 conservation of energy
\n """,
"""23 A given amount of gas occupies 10.0 dm3 at 4 atm and 273°C. The number of moles of the gas present is[Molar volume of a gas at stp. =22.4 dm3]
0.89 mol
1.90 mol
3.80 mol
5.70 mol
\n """,
"""24 According to Charles' law, the volume of a gas becomes zero at
 0°C
 -100°C
 -273°C 
 -373°C
\n """,
"""25 A substance that is used as a ripening agent for fruits is
 ethene
 propane
 methane
 butane
\n """,
"""26 The Sulphide which is insoluble in dilute hydrochloric acid is
 FeS
 CuS
 ZnS
 NaS
\n """,
"""27 What is the pH of 0.001 moldm-3 solution of the sodium hydroxide?
 14
 13
 12
 11
\n """,
"""28 The type of bonding in [Cu(NH3)4]2+ is
 coordinate
 electrovalent
 metallic
 covalent.
\n """,
"""29 Which of the following is an example of a chemical change?
 dissolution of salt in water
 rusting of iron
 melting of ice
 separating a mixture by distillation
\n """,
"""30 To what temperature must a gas at 273K be heated in order to double both its volume and pressure?
 298K
 546K
 819K
 1092K
\n """,
"""31 According to the Kinetic Theory, an increase in  temperature causes the kinetic energy of particles to:
 decrease
 increase
 be zero
 remain constant
\n """,
"""32 An element used in the production of matches is
 nitrogen
 aluminium
 copper
 Sulphur
\n """,
 """33 Which of the following gases may not be dried with concentrated sulphuric acid?
 HCl
 NH3
 CI2
 SO2
\n """,
"""34  Consecutive members of an alkane homologous series differ by
CH
CH2
CH3
CnHn
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),

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
        Chemistry_2014()
def Chemistry_2013():
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
        """0  Which of the following is an example of a mixture?
 Common salt
 Blood
 Sand
 Washing soda
\n """,
 """1 Calculate the percentage by mass of nitrogen in calcium trioxonitrate (V) [Ca = 40, N = 14, O = 16]
 8.5%
 13.1%
 17.1%
 27.6%
\n """,
 """2 The droplets of water observed around a bottle of milk taken out of the refrigerator is due to the fact that the
 water vapour in the air around the bottle gains some energy from the bottle
 temperature of the milk drops as it loses heat into the surroundings
 saturated vapour pressure of the milk is equal to the atmospheric pressure
 water vapour in the air around the bottle loses some of its energy to the bottle
\n """,
"""3 The volume of a given gas is Vcm3 P mm Hg. what is the new volume of the gas if the pressure is reduced to half at constant temperature?
 4 V cm3
 2 V cm3
  1⁄2 cm3
 V cm3 
\n """,
"""4 Moving from left to right across a period, the general rise in the first ionization energy can be attributed to the
 decrease in nuclear charge
 increase in nuclear charge
 decrease in screening effect
 increase in screening effect
\n """,
"""5 How many unpaired electron(s) are there in the nitrogen sublevels?
3
2
1
none
\n """,
"""6 The stability of the noble gases is due to the fact that they
have no electron in their outermost shells
 have duplet or octet electron configurations
 belong to group zero of the periodic table
 are volatile in nature 
\n """,
"""7 The maximum number of electrons in the L shell of an atom is
 2
 8
 18
 32
\n """,
"""8 Elements in the same period in the periodic table have the same
 number of shells
 atomic number
 chemical properties
 physical properties
\n """,
"""9 A noble gas with a high power of fog penetration used in aerodrome beacons is 
 krypton
 argon
 helium
 neon
\n """,
"""10 Permanent hardness of water can be removed by
 filtration
 adding slaked lime
 adding caustic soda
 boiling
\n """,
"""11 Substance employed as drying agents are usually
 amphoteric
 hydroscopic
 efflorescent
 acidic
\n """,
"""12 Calculate the solubility in moldm-3 of 40g of CuSO4 dissolved in 100g of water at 120⁰C.[Cu = 64, S = 32, O = 16]
 4.00
 2.50
 0.40 
 0.25
\n """,
"""13 Coffee stains can best be removed by
 Kerosene
 turpentine
 a solution of borax in water
 ammonia solution
\n """,
"""14 Carbon (II) oxide is considered dangerous if inhaled mainly because it
 can cause injury to the nervous system
 competes with oxygen in the blood
 competes with carbon (IV) oxide in the blood
 can cause lung cancer
\n """,
"""15 The acid that is used to remove rust is
 boric
 hydrochloric
 trioxonitrate (V)
 tetraoxosulphate (VI) 
\n """,
"""16 Calculate the volume of 0.5mol dm-3 H2SO4 that is neutralized by 25 cm3 of 0.1 mol dm-3 NaOH
 5.0 cm3
 2.5 cm3
 0.4 cm3
 0.1 cm3
\n """,
"""17 The colour of methyl orange in alkaline medium is
 yellow
 pink
 orange
 red
\n """,
"""18 Which of the following salts is slightly soluble in water?
 AgCl
 CaSO4
 Na2CO3
 PbCl
\n """,
"""19 The IUPAC nomenclature of the compound LiAlH4 is
 lithiumtetrahydridoaluminate(III)
 aluminium tetrahydrido lithium
 tetrahydrido lithium aluminate(III)
 lithium aluminium hydride
\n """,
"""20 Iron can be protected from corrosion by coating the surface with
 gold
 silver
 copper
 zinc
\n """,
"""21 What quantity of aluminium is deposited when a current of 10A is passed through a solution of an aluminium salt for 1930s?[Al = 27, F = 96500 C mol-1] 
 0.2 g
 1.8 g
 5.4 g
 14.2 g
\n """,
"""22 In which of the following is the entropy change positive?
 Thermal dissociation of ammonium chloride
 Reaction between an acid and a base
 Addition of concentrated acid to water
 Dissolution of sodium metal in water
\n """,
"""23 If a reaction is exothermic and there is a great disorder, it means that
 the reaction is static
 the reaction is in a state of equilibrium
 there will be a large increase in free energy
 there will be a large decrease in free energy
\n """,
"""24 In the preparation of oxygen by heating KClO3 in the presence of MnO2, only moderate heat is needed because the catalyst acts by
 lowering the pressure of the reaction
 increasing the surface area of the reactant
 increase the rate of the reaction
 lowering the energy barrier of the reaction
\n """,
"""25 2H2(g) + O2(g) ⇋ 2H2O ΔH = ve. What happens to the equilibrium constant of the reaction above if the temperature is increased?
 it is unaffected
 it becomes zero
 it decrease
 it increases
\n """,
"""26 To a solution of an unknown compound, a little dilute tetraoxosulphate (VI) acid was added with some freshly prepared iron (II) tetraoxosulphate (VI) solution. The brown ring observed after the addition of a stream of concentrated tetraoxosulphate (VI) acid confirmed the presence of
 CO
 Cl-
 SO 
 NO
\n """,
"""27 Which of the following is used in rocket fuels?
 HNO3
 CH3COOH
 H2SO4
 HCl
\n """,
"""28 A constituent common to bronze and solder is
 lead
 silver
 copper
 tin
\n """,
"""29 When iron is exposed to moist air, it gradually rusts. This is due to the formation of
 hydrate iron (III) oxide
 anhydrous iron (III) oxide
 anhydrous iron (II) oxide 
 hydrate iron (II) oxide 
\n """,
"""30 A compound gives an orangered colour to non-luminous flame. This compound is likely to contain
 Na+
 Ca2+
 Fe3+
 Fe2+
\n """,
"""31 Stainless steel is used for making
 magnets
 tools
 coins and medals
 moving parts of clocks
\n """,
"""32 The residual solids from the fractional distillation of petroleum are used as
 coatings of pipes
 raw materials for the cracking process
 fuel for the driving tractors
 fuel for jet engines
\n """,
"""33  Which of the following is used as fuel in miners' lamp?
 Ethanal
 Ethyne
 Ethene
 Ethane
\n """,
"""34 Which of the following organic compounds is very soluble in water?
 CH3COOH
 C2H2
 C2H4
 CH3COOC2H5
\n """,
"""35 Benzene reacts with hydrogen in the presence of nickel catalyst at 180⁰C to give
 xylene
 toluene
 cyclopentane
 cyclohexane
\n """,
"""36 Which of the following is used to hasten the ripening of fruit?
 Ethene
 Ethanol
 Ethyne
 Ethane
\n """,
"""37 The final products of the reaction between methane and chlorine in the presence of ultraviolet light are hydrogen chloride and
 tricloromethane
 dichloromethane
 tetrachloromethane
 chloromethane
\n """,
"""38 One of the major uses of alkane is
 as domestic and industrial fuel
 in the hydrogenation of oils
 in the textile industries
 in the production of plastics
\n """,
"""39  The haloalkanes used in drycleaning industries are
trichloromethane and tetrachloromethane
 chloroethene and dichloroethene
 trichloroethene and tetrachloroethene
 chloroethane and dichloroethane 
\n """,
"""40 Two hydrocarbons X and Y were treated with bromine water. X decolorized the solution and Y did not not. Which class of compound does Y belong?
 Benzene
 Alkynes
 Alkenes
 Alkanes
\n """,
"""41 The compound that is used as an anaesthetic is
 CCl4
 CHCl3
 CH2Cl2
 CH3Cl
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "B"),

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
        Chemistry_2013()