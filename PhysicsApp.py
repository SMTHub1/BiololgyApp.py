from Question import Question
def Physics_2020():
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
                """0 
        A balloon filled with 1000 cm3 of gas at 127oC and pressure of 70 cm Hg. If the pressure changes to 28 cm Hg\n and temperature to -23.3oC, calculate the new volume of the gas.
        A 136 cm3
        B 218 cm3
        C 250 cm3
        D 485 cm3
        \n """,
        """1  
        A density glass bottle contains 44.25 g of a liquid at 0oC and 42.02 g at 50oC Calculate the \nreal cubic expansivity of the liquid (Linear expansivity of glass = 1.0x10-5 K-1)
        A 1.09x10-3 K-1
        B 1.06x10-3 K-1
        C 3.0x10-5 K-1
        D 1.03x10-3 K-1
        \n """,
        """2
        Which of the following properties is not used to measure the temperature of a substance?
        A variation of pressure with temperature
        B mass of a liquid
        C change in resistance of a conductor
        D change in colour with temperature
        \n """,
        """3
        The clinical thermometer is characterized by having a
        A wide range of temperatures
        B wide bore
        C long stem
        D constriction
        \n """,
        """4
        The amount of heat given out or absorbed when a substance changes its state at a constant temperature is know as
        A latent heat
        B heat capacity
        C specific heat capacity
        D specific latent heat
        \n """,
        """5
        A block of aluminium is heated electrically by a 25 W heater. If the temperature rises by 10oC in 5 minutes,\n what is the heat capacity of aluminium?
        A 850 J/K
        B 750 J/K
        C 650 J/K
        D 500 J/K
        \n """,
        """6
        In a gas experiment, if the volume of the gas is plotted against the reciprocal of the pressure, the unit of\n the slope of the resulting curve is:
        A power
        B work
        C temperature
        D force
        \n """,
        """7
        Thermal equilibrium between two objects exist when:
        A the heat capacity of both objects are the same
        B one object loses heat continuously to the other
        C temperature of both objects are equal
        D the quantity of heat in both objects is the same.
        \n """,
        """8
        A shepherd calling to fellow shepherd heard his voice reflected by a rock 3 s later. Calculate the velocity of\n sound in air if the rock is 510 m away.
        A 510 m/s
        B 1.5 m/s
        C 340 m/s
        D 170 m/s
        \n """,
        """9
        An object 3 cm high placed on the axis of a converging lens form an image 30 cm from the lens.\n If the focal length of the lens is 15 cm the height of the image is
        A 3 cm
        B 1 cm
        C 6 cm
        D none of the above
        \n """,
        """10
        An object is placed between two plane mirrors inclined at 60o to each other. If the object\n is equidistant from each find the number of images forme
        A 2
        B 3
        C 4
        D 6
        \n """,
        """11
        Before frying, the volume of 0.8 g/cm3 vegetable oil was 500 cm3. If the density of the oil was 0.5 g/cm3 after\n frying and there was no loss of oil due to spilling, what is the new volume of the oil?
        A 400 cm3
        B 800 cm3
        C 600 cm3
        D 200 cm3
        \n """,
        """12
        A 650 kg car that was initially rest traveled with an acceleration of 4 m/s2.\n Find its kinetic energy after 4 s.
        A 5200 J
        B 31200 J
        C 83200 J
        D 832 kJ
        \n """,
        """13
        The temperature at which the water vapour present in the air and begins to condense is called
        A condensation point
        B dew point
        C boiling point
        D critical point
        \n """,
        """14
        Which of the following types of waves will travel through vacuum? \nI. light waves II. sound waves III. Radio waves
        A I only
        B I and II only
        C II and III only
        D I and III only
        \n """,
        """15
        In a simple pendulum experiment, a student increased the length of the inextensible string\n by a factor of 9. By what factor is the period increased?
        A 3 
        B 1/3 
        C 2
        D ½
        \n """,
        """16
        A vapour is said to be saturated when:
        A the vapour of a substance is in equilibrium with its own liquid
        B the vapour of a substance is in equilibrium with its own gas
        C the vapour of a substance is in equilibrium with its own solid-liquid phase
        D none of the above
        \n """,
        """17
        A wave travels with a velocity of 360 m/s. If its wavelength is 120 cm then its period is:
        A 0.0017 s
        B 0.33 s
        C 33 s
        D 1.7 s
        \n """,
        """18
        The heights of the mercury thread in a mercury-inglass thermometer when melting ice and \nthen in steam are 2 cm and 22 cm respectively. What would be the height of the mercury thread at 70o?
        A 14 cm
        B 12 cm
        C 16 cm
        D 18 cm
        \n """,
        """19
        An object is placed 45 cm in front of a concave mirror of focal length 15 cm. What the linear\n magnification produced?
        A 1/3
        B 2 
        C 3
        D  ½
        \n """,
        """20
        A man has five 40 W electric light bulbs, six 60 W bulbs and two 100 W bulbs in his house. If all the \npoints are on for five hours daily and PHCN charges 12 k per unit, what is his bill for 30 days?
        A N13.68
        B N0.46
        C N2.74
        D none of the above
        \n """,
        """21
        In a resonance tube experiment, the first resonance position is 16 cm when the velocity of sound in air is\n 327.68 m/s. Find the frequency of the tuning fork used
        A 512 kHz
        B 256 Hz
        C 128 Hz
        D 512 Hz
        \n """,
        """22
        Half-life of a radioactive substance is:
        A the average life time of the substance
        B the time it takes the substance to decay to half of its original quantity
        C the time it takes the activity of the substance to decay to half of its original value
        D all of the above
        \n """,
        """23 
        The headlamp bulb of a motor car is rated 60 W, 12 V. Calculate the resistance of its filament.
        A 0.2ohms 
        B 5ohms 
        C 2.4ohms 
        D 2 V
        \n """,
        """24
        In an electrolysis experiment, a cathode of mass 4.5 g weighs 4.52 g after a current \nof 4.5 A flows for 1 hour. The electrochemical equivalent of the deposited substance is:
        A 0.00444 g/C
        B 0.00741 g/C
        C 0.00074 g/C
        D 0.00007 g/C
        \n """,
        """25
        An object falls freely under gravity from a given height. At half way point, its kinetic energy is:
        A exactly half of its initial potential energy
        B exactly half of its kinetic energy
        C exactly half of its final potential energy
        D zero
        \n """,
        """26 
        The silvered walls of a vacuum flask are used to prevent:
        A heat loss due to opacity
        B heat loss due to radiation
        C heat loss due to convection
        D heat loss due to conduction
        \n """,
        """27
        The law of universal gravitation states that:
        A All bodies on the surface of the earth are attracted towards the centre of the universe
        B Any two bodies attract each other with a force which is directly proportional to product \nof their masses and inversely proportional to the square of the distance between them.
        C All bodies attract each other with a force which is directly proportional to product of \ntheir masses and inversely proportional to the square of the distance between them.
        D Any two bodies attract each other with a force which is the product of their masses and \ninversely proportional to the distance between them.
        \n """,
        """28
        The nucleus of an atom consists of:
        A protons and neutrons
        B protons and electrons
        C electrons and neutrons
        D electrons, protons and neutrons
        \n """,
        """29
        A certain quantity of heat increases the temperature of 185 g of water from 10oC to 20oC and increases \nthe temperature of an equal volume of 140 g of oil from 7oC to 18oC The ratio of the specific heat of the oil to that of water is:
        A 0.83
        B 1.26
        C 1.07
        D 0.93
        \n """,
        """30
        The motion of the pendulum bob is:
        A rotational
        B circulatory
        C oscillatory
        D none of the above
        \n """,
        """31
        Which of the following is not one of the factors that affect the capacitance of a capacitor?
        A temperature
        B area of plates
        C distance between the plate
        D dielectric between the plates
        \n """,
        """32
        which of the following statements is true of gamma -rays?
        A they are deflected by electric field
        B they ionize intensely
        C they carry no electric charge
        D they originate outside the nucleus of the atom
        \n """,
        """33
        The virtual image formed of an object placed 10 cm from a convex lens is 2. Find the focal length of the lens.
        A 7.5 cm
        B 15 cm
        C 30 cm
        D 10 cm
        \n """,
        """34
        A milliammeter of resistance 2.5 ฀ and full scale deflection of 50 mA is to be used to measure a\n potential difference of 50 V. What is the resistance of the multiplier?
        A 99.75 
        B 997.5
        C 9975
        D 9.98
        \n """,
        """35
        The ice and steam points of a mercury-in-glass thermometer of centigrade scale and of uniform bore correspond\n respectively to 3 cm and 23 cm lengths of the mercury thread. What is the temperature when the length of the mercury thread is 12 cm?
        A 40oC
        B 60oC
        C 75oC
        D 45oC
        \n """,
        """36
        When a ray of light passes from glass to air, it is:
        A bent towards the normal
        B away from the normal
        C not deviated
        D spread out in a pure spectrum
        \n """,
        """37
        What is the resistance of the filament of an electric lamp rated 220 V, 100 W?
        A 0.45ohms  
        B 2.2ohms 
        C 484ohms  
        D 440ohms
        \n """,
        """38
        Pressure cooker cooks faster because
        A the inside is polished
        B inside the cooker, the boiling point of water is raised
        C inside the cooker, the boiling point of water is lowered
        D inside the cooker, the pressure of water is raised
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "A"),

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
        Physics_2020()
def Physics_2019():
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
                """0
 A stone of mass 50 kg released from a height of 2 m above the ground If the stone falls freely to a \nheight of 5 m above the ground, its velocity is
19.6 m/s 
49.0 m/s 
17.15 m/s
39.2 m/s
\n """,
"""1
 Calculate the kinetic energy of a trolley of mass 40 kg moving with a velocity 0.5 m/s
20 J 
5 J
15 J
10 J
\n """,
"""2
  A car of mass 500 kg accelerates from rest at 1 m/s2. What is the total distance covered in 1 minute?
2000 m 
3600 m 
1800 m 
2400 m
\n """,
"""3
 Niagara falls are 50 m high. Calculate the potential energy of 0.1 cubic meter of water at the top relative\n to the bottom. Density of water is 1000 kg m¯3. Take g = 10 m/s2
48 kJ 
50 kJ
51 kJ 
61kJ
\n """,
"""4
  A bullet of mass 15 g is fired from a riffle with a velocity 100 m/s. If the mass of the riffle is 1 kg.\n What is the recoil velocity of the riffle?
1.5 m/s 
1.8 m/s 
1.2 m/s 
2.1 m/s
\n """,
"""5
  A ball is thrown vertically upwards with a velocity of 30 m/s. Find the greatest height attained
40 m 
50 m 
55 m 
45 m
\n """,
"""6
  The tension in a rope pulling a log is 100 N, the mass of the log is 50 kg and the frictional force \non the log is 20 N. What is the acceleration of the log?
2 m/s2 
1.6 m/s2 
1.8 m/s2
2.2 m/s2
\n """,
"""7
 A body of mass 1 kg falls freely from rest through a height of 150 m. Calculate the velocity of the body \nwhen it strikes the floor (g=10 m/s2).
54.8 m/s
45.2 m/s 
38.7 m/s
65.8 m/s
\n """,
"""8
 A car moving with a velocity of 16 m/s accelerates uniformly at the rate of 1 m/s2 to reach a velocity of 20 m/s.\n Find the distance covered
85 m 
75 m 
82 m 
72 m
\n """,
"""9
 An athlete runs 100 m in 12 s. What is his speed in km/h?
33 km/h 
36 km/h
30 km/h 
27 km/h
\n """,
"""10
  Which of the following statements best describes the specific heat capacity of a substance?
The quantity of heat required to produce a unit temperature rise;
The random kinetic energy of the particles composing a system;
The quantity of heat required to change the temperature of a unit mass of the substance by one degree;
The quantity of heat required to vaporise a unit mass of the substance at constant temperature.
\n """,
"""11
  Determine the temperature whose Fahrenheit and Kelvin scales have the same reading to the nearest degree.
273K
300K 
500K 
574K
\n """,
"""12
  The SI unit of specific heat capacity of a substance is:
JK¯1
Jkg¯1K¯1
Joules
Cal/g°C
\n """,
"""13
 The density of nitrogen at standard temperature and pressure is 1.251 kgm¯3. Calculate the root mean square\n velocity of nitrogen molecules.
240 m/s
1x104 m/s
340 m/s
493 m/s
\n """,
"""14
  A malaria patient has a body temperature of 98.6°F. What is this temperature on the Celsius scale?
37°C
20°C
32°C
35°C
\n """,
"""15
  A thermos bottle containing 250 g of coffee at 90°C is added with a 20 g of milk at 5°C After thorough mixing, \nwhat is the final temperature? c for water, coffee and milk is 1.00Cal/g°C
84°C
84°K
84°F
55°C
\n """,
"""16
  Determine the temperature Tf that results when 150 g of ice at 0°Cis mixed with 300 g of water at 50°C
67°C
6.7°C
48°C
80°C
\n """,
"""17
  The only mode of heat energy transfer that needs no material medium is:
Convection
Radiation
Conduction
Thermal conduction
\n """,
"""18
  When heat energy is added to a system which of the following observations usually occur: \n(I) The internal energy of the system increases; (II) Work may be done on the surroundings; (III) The volume of system is directly proportional to the temperature.
I and II only
I, II and III
III only
None of the above.
\n """,
"""19
 The transfer of heat energy from one part of a body to another part without the actual movement of \nany part of the body is called convection.
True
False
Neither true nor false
I cannot tell.
\n """,
"""20
 . Which of the following quantities are scalars? I. Mass II. Work III. force IV. Magnetic flux
II and III only
I and II only
IV only
I and IV only
\n """,
""" 21
 A force (15i – 16j + 27k)N is added to a force (23j – 40k)N. What is the magnitude of the resultant?
17N
28N
63N
21N
\n """,
"""22
  Which of the following statements is/are correct about an object in equilibrium under parallel forces? \nI. The total force in one direction equals the total force in the opposite direction. II. The body must not rotate. III The resolved components along the x-axis equals the resolved components along the y-axis.
I and II only
I, II and III
II and III only
I and III only.
\n """,
"""23 
  A car moving with a speed of 90 km/h was brought to rest in 10 s by the application of the brakes.\n How far did the car travel after the brakes were applied
150 m
15 m
250 m
125 m
\n """,
"""24
 A metre rule is found to balance at the 48 cm mark. When a body of mass 60 g is suspended at the 6 cm mark,\n the balance point is found to be at the 30 cm mark. Find the mass of the metre rule.
60 g
360 g 
80 g 
180 g.
\n """,
"""25
  A ball of mass 0.1 kg moving with a horizontal velocity of 15 m/s is shot into a wooden block of mass 0.4 kg\n lying at rest on a smooth horizontal surface. Find their common velocity after impact.
15.0 m/s
3.8 m/s
7.5 m/s
3.0 m/s
\n """,
"""26
A body of mass 2 kg moves velocity of 10 m/s. Neglecting air resistance, determine the kinetic energy of the body.
200 N
200 J
100 J
100 N
\n """,
"""27
Three forces of magnitude 15 N, 10 N and 5 N act on a particle in the direction which make 120o with one another.\n Find the resultant and the angle the resultant makes with the x-axis.
8.66 N, 30o 
4.33 N, 60o
7.4 N, 45o
2.52 N, 60o
\n """,
"""28
Which of the following statements best defines a couple?
Two parallel and opposite forces acting on one another.
Two equal forces acting in the same direction.
Two parallel and opposite forces acting on a body whose lines of action do not coincide
 None of the above.
\n """,
"""29
A force F = (5i + 3j)N acts on a body and causes a displacement r = (7i – j)m. Determine the work done.
53 J
32 J
35 J
21 J.
\n """,
"""30
A force of 0.6 N acts on a body of mass 40 g, initially at rest. What is the resulting acceleration?
35 m/s2
40 m/s2
15 m/s2
25 m/s2
\n """,
"""31
  Which of the following statements is not correct about stable equilibrium?
the body returns to its original position when it is slightly displaced and released
a slight displacement raises its centre of gravity.
a slight displacement lowers its centre of gravity.
a slight displacement does not raise or lower its centre of gravity.
\n """,
"""32
  A body is projected vertically upwards with a velocity of 9.78 m/s. How high does it travel before it comes \nto rest momentarily at the top of its motion?. ( g = 9.78 m/s2)
2.45 m
4.89 m
6.89 m
9.78 m
\n """,
"""33
  Calculate the time taken for a car to cover a distance of 125 m if the initial speed is 5 m/s and it has a \nconstant acceleration of 1.5 m/s2
8 s
10 s
15 s
12 s
\n """,
"""34
  Calculate the braking force to bring a body of mass 1 kg to rest from 25 m/s on a level ground in 60 m with\n uniform retardation.
5.2 N
5.5 N
5.6 N
5.0 N
\n """,
"""35
  A drop hammer is lifted to a height of 50 m above the ground and then allowed to fall from rest on to a forging\n at ground level. Calculate the downward velocity of the hammer when it strikes the forging. (g=10 m/s2)
10.95 m/s
25.8 m/s
31.6 m/s
35.5 m/s
\n """,
"""36
  A uniform rod of weight 10 N is balanced at a point 75 cm from the end B The pivot is removed to point 30 cm from \nA What force must be applied at A to balance the rod horizontally?
25 N
10 N
30 N
15 N
\n """,
"""37
  An equilateral triangular lamina has each side equal to 50 cm. How far is the centre of gravity from each vertex?
34.64 cm
33.3 cm
36.9 cm
28.9 cm
\n """,
"""38
  A man can row a boat at 13 m/s in still water. If he aims at crossing to the opposite bank of a river flowing\n at 5 m/s, at what angle to the bank of the river must he row the boat?
67.4o
21o
56.8o
22.6o
\n """,
"""39
 The lower and upper fixed points of a thermometer are 30 mm and 180 mm respectively. Calculate the temperature\n in degrees Celsius when the thermometer reads 45 mm.
10.0oC
15.0oC
20.0oC
30.0oC
\n """,
"""40
  An immersion heater rated 400 W, 220 V is used to heat a liquid of mass 0.5 kg. If the temperature of the\n liquid increases uniformly at the rate of 2.5oC per second, calculate the specific heat capacity of the liquid assuming no heat loss,
1100 J/kg.K
320 J/kg.K
200 J/kg.K
176 J/kg.K
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "B"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "B"),

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
        Physics_2019()
def Physics_2018():
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
        """0 
        A boy runs 100 m due north and then 100 m due east. What is his displacement?
        200m 45oE 
        141.4 m 45oE
        100m 45oN 
        141.4m 45oW
        \n """,
        """1 The speed of an air force jet was 400 m/s when it flew past an anti-aircraft gun. Calculate its distance from the gun 4 s later when the gun was fire
        100 m
        1600 m
        1600 km
        100km
        \n """,
        """2 
         A mango fruit dropped to the ground from the top of a tree 40 m tall. Find how long it takes the fruit to reach the ground if acceleration due to gravity g = 10 m/s2
        2.8s
        0 s
        4 s
        2 s
        \n """,
        """3  A 0.1-m long elastic band extends 5 mm when a load of 80 N is hung from its end Calculate the strain on the band
        5  
        0.5 
        0.05
        16
        \n """,
        """4  Which of the following statements describes what happened when an ice block that floats in a glass of water that is filled to the brim melts?
        The level of the water remains the same.
        There is a drop in the level of water in the glass due to condensation on its outside.
        The water in the glass overflows
        The water level drops because melted ice occupies less volume.
        \n """,
        """5  A machine with a mass of 4 kg fires a 45 g bullet at a speed of 100 m/s. Find the recoil speed of the machine gun.
        1.1 m/s
        2 m/s
        3.5m/s 
        0 m/s
        \n """,
        """6  Which of the following would you use to determine the weight of an object?
        chemical balance 
        beam balance
        spring balance
        weight balance
        \n """,
        """7 The force that causes an object to move in a circular path is called
        centrifugal force 
        centripetal force
        centre-seeking force 
        none of the above
        \n """,
        """8 A solid suspended by a piece of string is completely immersed in water. On attempting to lift the solid out of the water, the string breaks when the solid is partly out of the water. This is  because
        the tension in the string decreases as the solid is lifted
        the mass of the solid has increase
        the solid apparently weighs less when completely immersed in water than when partially immersed
        part of the solid still in water is exerting more force on the string
        \n """,
        """9  The following statements were made by some students describing what happened during and experiment to determine the melting point of solids 1. The temperature of the solid was constant until melting started 2. The temperature of the solid rose until melting started 3. During melting, the temperature was rising 4. During melting, the temperature was constant 5. The temperature continued to rise after all the solid had melted 6. temperature stopped rising after the solid had melted which of the following gives correct statements in the right order?
        2, 4 and 5 
        2, 3 and 6
        1, 3 and 6 
        1, 3 and 5
        \n """,
        """10  When some grains of table salt were put in a cup of cold water, kept at constant temperature and left undisturbed, all the water tasted salty after some time. This is due to
        capillarity 
        surface tension
        mixing 
        diffusion
        \n """,
        """11  Given that the latent heat of fusion of ice is 80 cal/g, how much heat will change 100 g of ice at 0oC into water at the same temperature?
        8 kcal 
        8 cal 
        800 cal
        8000 kcal
        \n """,
        """12  A blacksmith dropped a 1.5 kg iron bead at 300oC into some quantity of water. If the temperature of the water rose from 15oC to 18oC, what is the mass of the water assuming no heat is lost to the surrounding? (Take the specific heat of iron as 0.46 J kg-1 C-1 and that of water as 4.2x103 J kg-1 C-1)
        15.44 kg 
        194.58 g 
        15.44 g
        194.58 kg
        \n """,
        """13  Which of the following properties are not those of a suitable thermometric liquid? I. It should be a good conductor of heat II. It should be opaque III Its expansion should be regular IV. It should wet glass V It should have a high melting point and low boiling point
        I and II 
        II and III
        III and IV 
        IV and V
        \n """,
        """14  A gas at pressure P1 N/m2 and temperature 30oC is  heated to 61oC at constant volume. Find its new pressure.
        1.1 N/m2 
        1.2 P1 N/m2
        1.01 P1 N/m2
        1.1 P1 N/m2
        \n """,
        """15  A steel bar has a width of 10 cm at 50oC At what temperature will it fit exactly into a hole of constant width 10.005 cm if coefficient of linear expansion of steel is 11x10-6 C-1)?
        75oC 
        0.005oC
        75.5oC 
        -75.5oC
        \n """,
        """16  The amount of heat that is required to raise the temperature of unit mass of a substance one degree Celsius is called
        Heat capacity 
        thermal capacity
        Specific heat 
        Heat energy
        \n """,
        """17 Two lamps rated 60 W and 240 V each are connected in series. What is the total power dissipated in both?
        30 W 
        60 W 
        90 W 
        120W
        \n """,
        """18  If PHCN charges 25 k per kWh, find the cost of operating for 36 hours a lamp requiring 1.5 A on a 240 V line.
        N324 
        N32.4 
        N3.24 
        N0.324
        \n """,
        """19  In order to convert a galvanometer to a voltmeter
        a low resistance shunt is connected in parallel
        a low resistance shunt is connected in series
        a high resistance multiplier is connected in parallel
        a high resistance multiplier is connected in series
        \n """,
        """20 Three resistors connected in parallel have a potential difference of 24 V applied across the combination. What is the current in each resistor?
        8A
        3A
        24
        4A
        \n """,
        """21  Which of the following is not applicable to an ac generator?
        Armature
        Commutator
        Field magnet 
        Slip rings
        \n """,
        """22  A potential difference of 5 V is used to produce a Vcurrent of 4 A for 4 hours through a heating coil. What is the heat produced?
        80 J 
        4.8 kJ 
        20 J 
        4800 kJ
        \n """,
        """23  Determine the absolute temperature at which the Fahrenheit temperature is twice the Celsius temperature.
        299.82K 
        433.15K
        273.25K
        406.35K
        \n """,
        """24  Which of the following law forms the basis of the thermometry?
        Charles' and Gay-Lussac's law
        Fist law of thermodynamics
        Boyle's and pressure law
        Zeroth law of thermodynamics
        \n """,
        """25  An electric heater which produces 900 W of power is used to vaporize water. How much water at 100°C can be changed to steam in 3 mins by the heater? [Heat of vaporization = 2.26×106 J/kg, Specific heat capacity of water = 4.2×103 J/kg. K]
        0.0226 kg 
        0.275 kg
        0.072 kg 
        0.167 kg
        \n """,
        """26 The amount of heat required to produce unit temperature rise in a substance is called:
        Latent heat 
        Heat capacity
        Specific heat capacity
        Specific latent heat
        \n """,
        """27  An ideal gas has a volume 100 cm3 at 1x105 Pa and 27°C What is its volume at 2x105Pa and 60°C?
        42.5 cm3 
        55.5 cm3
        50.2 cm3 
        40.5 cm3
        \n """,
        """28  Which of the following thermometer can be used to measure high temperature up to 1000oC?
        Electrical thermometer 
        Pyrometer
        Bimetal thermometer
        Thermoelectric thermometer
        \n """,
        """29  4000 J of heat is applied to a 1.5 kg silver pendant initially at temperature of 150°C Determine its final temperature [Latent heat = 336 Jkg¯1, specific heat capacity = 233 J/kg. K].
        26.4°C 
        38.4°C
        41.5°C 
        15.5°C
        \n """,
        """30 The specific heat capacity of a substance depends on all the following except:
        Mass of the substance
        Change in temperature
        Surface area of the substance
        Energy needed
        \n """,
        """31  Which of the following quantities is a vector?
        Mass 
        Velocity 
        Distance 
        Speed
        \n """,
        """32  A hose ejects water at 80 cl/s through a hole 2 mm in diameter. The water impinges on a wall and drops off without rebounding. What is the force on the wall?
        2.04 N 
        240.0 N 
        20.4 N 
        24.0 N
        \n """,
        """33  A train travelling at 72 km/h undergoes a uniform retardation of 2 m/s when brakes are applied Find the distance travelled from the place where the brakes were applied
        10m 
        50m
        100m
        250m
        \n """,
        """34  An electric heater which produces 900 W of power is used to vaporize water. How much water at 100°C can be changed to steam in 3 mins by the heater? [Heat of vaporization = 2.26×106 J/kg, Specific heat capacity of water = 4.2×103 J/kg. K]
        0.0226 kg 
        0.275 kg
        0.072 kg 
        0.167 kg
        \n """,
        """35 A 500m long aluminium chair expands when it was placed in the sun. Its temperature increases from 20°C to 60°C Determine its new length. [ά=2.30x 10-5K-1)
        500.46m
        456.65m
        540.28m
        460.32m
        \n """,
        """36  A force of 200 N pulls a sledge of mass 50 kg and overcomes a constant frictional force of 40 N. What is the acceleration of the sledge?
        4.0 m/s 
        50 m/s 
        4.5 m/s 
        3.2 m/s
        \n """,
        """37  An object A of mass 2 kg is moving with a velocity of 3 m/s and collides head-on with another object B of mass 1kg moving in the opposite direction with a velocity of 4 m/s. Assuming the objects move off together after collision, calculate their common velocity.
        0.67 m/s 
        0.50 m/s
        0.35 m/s 
        0.55 m/s
        \n """,
        """38 In elastic collision, which of the following quantities is conserved?
        Kinetic energy 
        Potential energy
        Activation energy 
        Conservation energy
        \n """,
        """39 A weight of 20 N hangs from a fixed point by a light inextensible string. It is pulled aside by a horizontal force with the string inclined at an angle of 30° to the vertical. The tension in the string is
        11 N 
        40 N 
        5 N 
        30 N
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "A"),
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
        Physics_2018()
def Physics_2017():
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
        """0 A gasoline generator is used to power ten 40 W lamps, five 60 W lamps and a musician's 1000 W \n amplifying system. If the generator runs for 5 hours, the energy used is
1.7 kWh
8.5 kWh
1.0 kWh
none of the above
\n """,
"""1  Which of the following statements is not true about sound waves?
Sound waves are longitudinal waves
Sound waves are transverse waves
Sound waves are mechanical waves
Sound waves can not propagate through vacuum
\n """,
"""2  Which of the following statements is not true about the human eye?
the focal length of its lens is fixed
the focal length of its lens is variable
image distance is fixed
all of them
\n """,
"""3  Hypermetropia can be corrected by using
concave spectacle lenses
convex spectacle lenses
plano-concave spectacle lenses
plano-convex spectacle lenses
\n """,
"""4 In the astronomical telescope
there are three convex lenses
the eyepiece has a longer focal length than the objective
the eyepiece has a shorter focal length than the objective
the eyepiece and the objective have the same focal length
\n """,
"""5 Which of the following apparatuses is not needed for the production of pure spectrum?
source of light  
rectangular glass block
slit
convex lens
\n """,
"""6 The principle of moment states that:
Action and reaction are equal and opposite
If a body is in equilibrium under the action of a number of parallel forces, sum of clockwise moment equals\n  sum of anticlockwise moment
If a body is in equilibrium under the action of a number of parallel forces, sum of clockwise moment about a\n  point equals sum of anticlockwise moment about the same point.
If a body is in equilibrium under the action of a number of parallel forces, all forces cancel out
\n """,
"""7  A uniform metre rule of mass 90 g is pivoted at the 40 cm mark. If the metre rule is in equilibrium \n with an unknown mass M placed at the 10 cm mark and a 72 g mass at the 70 cm mark, then M is
162 g
30 g
72 g
102 g
\n """,
"""8  A pole AB of length 10 m weighs 800 N and has its centre of gravity 4 m from the end A, and lies on\n  horizontal ground. The least vertical force required to lift its end B is
320 N
80 N
2000N
20 N
\n """,
"""9  A metre rule is found to balance horizontally at the 48 cm mark. When a body of mass 60 g is suspended \n at the 6 cm mark the balance point shifts to the 30 cm mark. The mass of the metre rule is:
1.33 g
80 g
3.33 g
45 g
\n """,
"""10 The elastic limit of a material is:
the yield point
the limit of stress within which the strain in the material completely disappears when the stress is removed
a point at which a sudden increase in elongation occurs with only a small increase in tension.
none of the above.
\n """,
"""11 A 10 g mass placed on the pan of a spring balance causes an extension of 5 cm. If a 15 g mass\n  is placed on the pan of the same spring balance, the extension produced is:
2.0 cm
30.0 cm
7.5 cm
1.5 cm
\n """,
"""12  Which of the following does not reduce surface of a liquid? I. addition of impurities like\n  detergent or alum to the liquid II. heating the liquid III. cooling the liquid
I only
II only
III only
I and II only
\n """,
"""13  Which of the following is not an application of capillarity?
sap from the soil rises up plant stem.
kerosene rises up the wick of a lamp
blotting paper absorbs ink
none
\n """,
"""14 . Which of the following statements is not correct?
electric charges can be produced by friction
electric charges can be produced by induction
electric charges can be produced by conduction
none
\n """,
"""15  Which of the following is not simple harmonic motion?
The motion of the prongs of a sounding tuning fork
The motion of an object suspended from the free end of a spiral spring
The motion of the plucked string of a musical instrument
The motion of Earth around the sun
\n """,
"""16 The period of a body making simple harmonic motion is defined as:
number of complete oscillation performed in one second
time taken to make one complete oscillation
time taken to make one oscillation
the maximum displacement of the body from its equilibrium position
\n """,
"""17 A machine gun fires a bullet with an initial velocity of 200 m/s at an angle of 60o to the horizontal.\n  If g = 10 m/s2, the total time of flight of the bullet is:
34.64 s 
17.32 s 
51.96 s
69.28 s
\n """,
"""18 A bullet of mass 20 g is fired horizontally at a stationary wooden block of mass 380 g with a\n  velocity of 200 m/s. If the bullet embeds itself in the block, their common velocity is:
10.0 m/s
0.1 m/s
4.0 m/s
0.0 m/s
\n """,
"""19 The velocity ratio of a simple machine is defined as:
the ratio of the distance moved by effort to the distance moved by load
the ratio of the distance moved by load to the distance moved by effort
the ratio of the useful work output of the machine to the total work input
none of the above
\n """,
"""20 A machine has a velocity ratio of 6 and is 80% efficient. The effort needed to lift a load of 300 N\n  with the aid of the machine is:
4.8 N 
300 N
62.5 N
63.5 N
\n """,
"""21 An open organ pipe has a length of 6 m. If the speed of sound in air is 340 m/s and neglecting\n  the endcorrections, the frequency of its first overtone is
56.67 Hz
28.33 Hz
85 Hz
1.3 kHz
\n """,
"""22 A piano wire 0.5 m long has a total mass of 0.01 kg and is stretched with a tension of 800 N. \n The frequency of its fundamental note is:
400 Hz
100 Hz
200 Hz
300 Hz
\n """,
"""23 Two capacitors of 8mf and 10mf are connected in series to a 100V dc supply. The charge on either\n  place of each capacitor is:
2.25x10-1C
4.4 C
4.4x10-3C
4.4x10-4C
\n """,
"""24 A conductor of length 5 m carrying a current of 15A is placed in a uniform magnetic field of \n flux density 0.25 T. If the conductor is placed at 60o to the field then the force on it is:
18.75 N
9 N
16.24N
35 N
\n """,
"""25 When an inclined plane of angle 60 is used as a simple machine, its velocity ratio is:
1/cos60
cos60
1/sin60 
sin60
\n """,
"""26 Which of the following statements is not true of a real image formed by a concave mirror?
It is inverted
It is erect
It can be observed on a screen
None
\n """,
"""27 A 8 kg mass rests on an inclined plane. If the limiting frictional force 50 N and g = 10 m/s2, then the\n  angle of inclination of the plane is:
37.8o
38.7o
87.3o
78.3o
\n """,
"""28 Which of these gives the dimension of torque?
MLT
ML-1T
ML-1T-2
ML2T-2
\n """,
"""29 An object of mass 80 kg is kicked above the ground and in 20 s it has reached a height of 600 cm. Calculate the\n  power of the object.
40 W
240 W
402 W
204 W
\n """,
"""30 Which of these statements is true?
Energy cannot be destroyed and cannot be transformed from one form to another
Momentum before impact is not necessarily equal to the momentum after impact
Impulse the product of force and time
In perfectly elastic collision, there is a small loss of energy.
\n """,
"""31 A load of 2 tonnes is raised with 10 N efforts. Calculate the mechanical advantage of the machine with\n  which the load is raised
200 N
0.20 N
2000
102
\n """,
"""32 An object of mass 4000 g is 60 cm above the ground Calculate its kinetic energy 50 cm above the ground\n  (Take g = 10 m/s2)
4 J
40 J
4 N
40 N
\n """,
"""33 A fast moving object of mass 200 g travels at 100 m/s and hits a block of wood of mass 2 kg. The two bodies\n  moved together after impact. Find the velocity with which they moved together after collision.
9.09 m/s
90.9 m/s
0.910 m/s
1.96m/s.
\n """,
"""34 Determine the distance traveled by a particle whose initial velocity is 48 km/h. The particle accelerated\n  uniformly at the rate of 1.8 m/s2 and attained a velocity of 72 km/h.
6.167 m
61.67 m
616.7 m
6167 m
\n """,
"""35  An object floats in a liquid with one third of its volume above the liquid surface. Determine the density\n  of the liquid, if the object density is 7100 kg/m3 (Take g = 10m/s2)
1056 kg/m3
1560 kg/m3
10650 kg/m3
15.60 kg/m3
\n """,
"""36 A metal block of mass 2125 g displaces 250 cm3 of water. What is its density?
8300 kg/m3
8800 kg/m3
8500 kg/m3
8700 kg/m3
\n """,
"""37 A body starting from rest travels for 100 s with uniform acceleration of 1.5 m/s. What distance does it cover\n  in the last 2 seconds?
27.0 m
26.2 m
29.8 m
30.8 m
\n """,
"""38 A pile driver of mass 125 kg falls through a height of 80 m before striking the pile. What is its momentum at\n  the instance it strikes the pile? g =10m/s2
40 kg.m/s
5000 kg.m/s
1600 kg.m/s
5000 kg.m
\n """,
"""39 A gun weighing 1500 kg fires a shot weighing 50 kg with a velocity 360 m/s. What is the recoil velocity of the gun?
14.0 m/s
12.0 m/s
11.0 m/s
13.0 m/s
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "A"),
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
        Physics_2017()
def Physics_2016():
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
        """0 A car of mass 1000 kg travels with a velocity 45 km/h on a rough road and it is brought to a rest\n after 10s. What is the force exerted on the car?
1333 N
1250 N
1282 N
1067 N
\n """,
"""1  A bridge 100m long weighs 500 kN. A lorry weighing 100 kN is 25 m from one end of it. Find the force exerted\n at this support.
350 kN
300 kN
330 kN
325 kN
\n """,
"""2  What is the kinetic energy of a rock of mass 220 g after it has fallen freely for 5 seconds? g=10 m/s2.
350 J
225 J
275 J
250 J
\n """,
"""3  When equal masses of iron and water are given equal quantity of heat, the piece of iron becomes,much hotter\n than water after a shorter time because:
the specific heat of iron is higher than that of water
the specific heat of iron is lower than that of water
iron is in solid state while water is in liquid state
heat flows faster in solids
\n """,
"""4 The speed of light in air is 3.0x108 m/s. What is its speed in glass having a refractive index of 1.65?
6.0 x108 m/s
4.95 x108 m/s
1.65 x108 m/s
1.82 x108 m/s
\n """,
"""5  Atmospheric pressure is 1.0x105 N/m2. If the barometer liquid has a density of 1250 kg/m3, what is the \nminimum length of the tube required? g=10m/s2.
7.8 m
0.76m
8.0 m
10 m
\n """,
"""6  Young's modulus for steel is 2x1011 N/m2. A weight of 100 N hangs from a steel wire of length 3 m and \ncross-sectional area 1.5x10-6m2. Calculate the extension is 0.25 mm, calculate the extension produced
1 mm
1.5 mm
0.1 mm
0.15 mm
\n """,
"""7  A load of 50 N is attached to one end of a long vertical wire of length 4 m and diameter 2.4 mm whose other \nend is fixed If the extension is 0.25mm, calculate the Young modulus of the material of the wire.
18 N/m2
1800 N/m2
180 N/m2
1.8x1011 N/m2
\n """,
"""8  Which of the following statements is not true about friction force is not correct.
The centre of gravity of a body is the point where the resultant force of attraction or weight of the body acts
The lower the centre of gravity of a body the more stable the body is
The higher the centre of gravity of a body the more stable the body is
it is the point at which the weight of the body appears to be acting
\n """,
"""9  A car travels with a constant velocity of 45 km/h for 10 s. What is the distance it covers in this time?
450 m
400 m
125 m
45 m
\n """,
"""10  A body is projected vertically upwards with a velocity of 9.78 m/s. How high does it travel before it comes \nto rest momentarily at the top of its motion?
4.89 m
500 m
48 m
9.78m
\n """,
"""11  Which of the following statements is not true about the friction force?
Friction always act in such a direction that opposes motion
The limiting frictional force is dependent on the area of contact of the two surfaces
until motion takes place, the frictionally force is always equal to the force tending to produce the motion
when motion takes place, the friction force is less than its limiting value.
\n """,
"""12  A solid of mass 1 kg suspended by a string, is completely immersed in water. If the tension in the string \nis 5 N, calculate the upthrust on the solid Take g= 9.78 m/s2
8.0 N
4.78N
47 N
9.78N
\n """,
"""13  The resistance of a piece of wire of length 20 m, cross-sectional area 8.0 x10-6 m2 and resistivity 4.0 x10-7
0.5ohms  
1.0ohms 
5.0ohms  
10.0ohms
\n """,
"""14  A force of 0.6 N acts on a body of mass 40 kg, initially at rest. What is the resulting acceleration?
24 m/s2
0.6 m/s2
40 m/s2
15 m/s2
\n """,
"""15  An object of mass 10 kg is pulled over a rough surface by a 20 N force. The object accelerates at a rate \nof 1.5 m/s2. Determine the frictional force between the object and the surface.
30N
20N
2N
5N
\n """,
"""16  A body of mass 2 kg, moving with velocity 5 m/s collides with stationary body of mass 0.5 kg if the two\n bodies move together after impact , calculate their common velocity.
10 m/s2
4 m/s2
2.5 m/s
0.5 m/s2
\n """,
"""17  A body of mass 200 g and specific heat capacity 0.4 J/g.K cools from 37oC to 31o<C> Calculate the quantity of\n heat released by the body.
4800J
1200J
480J
202J
\n """,
"""18 The length of mercury thread when it is at 0oC, 100oC and unknown temperature XoC is 200 mm, 220 mm and 270 mm\n respectively. Determine the value of X.
350oC
57 oC
133 oC
300 oC
\n """,
"""19  The linear expansivity of a substance is 1.2x10-4/K. A cube of this substance has a volume of 8.0x103 cm3 \nat 30o<C> Calculate the increase in its volume at 80oC
48 cm3
24 cm3
96 cm3
72 cm3
\n """,
"""20  At what temperature will the volume of a given ideal gas be three times its volume at 0oC?
273oC
300oC
546oC
819oC
\n """,
"""21  A rectangular metal block of volume 10-6m3 at 273K is heated to 573 K. If its coefficient of linear expansion\n is 12x10-5/K, what is the percentage change of its volume?
18
1.8
1.08
1.2
\n """,
"""22 Calculate the time taken, in minutes, to heat 2.0 kg of water from 30oC to 100oC in an electric kettle that \ndraws a current of 3.0 A from 240 V supply. (Specific heat capacity is 4.2x103 J/kg) neglect heat losses to the surrounding.
0.2
1.9
3.6
21.2
\n """,
"""23  The amount of heat needed to raise the temperature of 10 kg of copper by 1k is its:
internal energy
Specific heat capacity
Heat capacity
Molar heat capacity
\n """,
"""24  Calculate the heat energy required to vapourise 50g of water initially at 80oC if the specific heat \ncapacity of water is 4.2 J/g.K. (Specific latent heat of vapourisation of water is 2260 J/g)
1533000 J
1172200 J
230200 J
113000 J
\n """,
"""25  A piece of copper mass 200 g is heated to 100oC and is then quickly transferred to a copper calorimeter of\n mass 10 g, containing 100 g of water whose initial temperature is 15o<C> If the specific heat capacity of copper and water are 400 J/kg.K and 4200 J/kg.K, find the final temperature of the substance.
29.1oC
30.1oC
28.4oC
27.4oC
\n """,
"""26  Which if the following statements is not correct about the assumptions of kinetic theory of gases?
the attraction between the molecules is negligible
the volume of molecules is negligible compared with the volume occupied by the gas
the duration of a collision is negligible compared with the time between collisions
the molecules of the gas behave like perfectly inelastic spheres
\n """,
"""27 The ice and steam points of an ungraduated thermometer are 300 mm apart. Calculate the length of thermometric\n liquid above the ice points which will correspond to a temperature of 75oC
275 mm
250 mm
225 mm
215 mm
\n """,
"""28  A piece of copper of mass 0.55 kg is heated from 57oC to 100oC What is the increase in the internal energy\n of the copper? (c=380 J/kg.K)
8.9x103J
9.8x103J
8.987x103J
9.879x103J
\n """,
"""29  Two metals A and B lose the same quantity of heat when their temperatures drop from 20oC to 15oC If \nthe specific heat capacity of A is thrice that of B, calculate the ratio of mass of A to that of B
1:3
1:2
3:1
3:4
\n """,
"""30 Which of the following is/are observed when heat energy is added to a system? (i) the internal energy of \nthe system increases (ii) the volume of the system is directly proportional to the temperature (iii) work may be done in the surroundings.
(i), (ii) and (iii)
(iii) only
(i) and (iii)
none of the above
\n """,
"""31  A constant volume gas thermometer records a pressure of 240 mmHg at 0oC and 300 mmHg at 100oC \nCalculate the new temperature when the gas pressure is 270 mm of Hg
99oC
95oC
9oC
90oC
\n """,
"""32  In which of the following is expansion of solids a disadvantage?
the balance wheel of a watch
fire alarms
the thermostat
the fitting of wheels in rims.
\n """,
"""33  How long does it take a 800 W heater to raise the temperature of 2 kg of water from 20oC to 60oC? \n(specific heat capacity of water = 4200 J/kg.K)
280 s
420 s
210 s
120 s
\n """,
"""34  A room is heated by means of charcoal fire. A man in the room standing away from the fire is warmed by:
convection
radiation
conduction
reflection
\n """,
"""35  I. The earth is not spherical but elliptical in shape. II. Variation in latitude and longitude. \nIII. Rotation of the earth on its axis. IV. Variation in the density of the earth. On which combination of the above does the weight of an object vary on the earth’s surface?
I, II and III only.
I, II, III and IV.
I and II only.
II, III and IV only.
\n """,
"""36  If a spherical metal bob of radius 3cm is fully immersed in a cylinder containing water and the water \n level rises by 1cm, what is the radius of the cylinder?
6cm
12cm
1cm 
3cm.
\n """,
"""37  The efficiency of a machine is always less than 100% because the
velocity ratio is always greater than the mechanical advantage.
work output is always greater than the work input.
effort applied is always greater than the load lifted.
load lifted is always greater than the effort applied.
\n """,
"""38  The height at which the atmosphere ceases to exist is about 80km. If the atmospheric pressure on the \nground level is 760mmHg, the pressure at a height of 20km above the ground level is
380 mmHg 
190 mmHg
570 mmHg
480 mmHg
\n """,
"""39  Which of the following consists entirely vector quantities?
Work, pressure and moment
Velocity, magnetic flux and reaction.
Displacement, impulse and power.
Tension, magnetic flux and mass.
\n """,
"""40  The diagram below is a block-and-tackle pulley system in which an effort of 80N is used to lift a load of 240N.\n The efficiency of the machine is
40%
33%
60%
50%.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "B"),
        Question(question_prompts[40], "D"),

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
        Physics_2016()
def Physics_2015():
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
        """0 A stone of mass 1kg is dropped from a height of 10m above the ground and falls freely under gravity.\n Its kinetic energy 5m above the ground is then equal to
its kinetic energy on the ground.
half its initial potential
its initial potential energy.
twice its initial potential energy.
\n """,
"""1  The resultant of two forces acting on an object is maximum if the angle between them is
45o
180o
0o
90o
\n """,
"""2  The terrestrial telescope has one extra lens more than the astronomical telescope. The extra lens is for
erection of the image.
improving the sharpness.
crating an inverted image.
magnification of the image.
\n """,
"""3  A plane sound wave of frequency 85.5Hz and velocity 342ms-1 is reflected from a vertical wall. At what \ndistance from the wall does the wave have an antinode?
1m 
1.2m
2m
3m
\n """,
"""4 A string is fastened tightly between two walls 24cm apart. The wavelength of the second overtone is
12cm
24cm
8cm
16cm
\n """,
"""5  A ray of light strikes a plane mirror at an angle of incidence of 35o. If the mirror is rotated through 10o,\n through what angle is the reflected ray rotated?
45o
20o
70o
25o
\n """,
"""6  A gas with initial volume 2 x 10-6m3 is allowed to expand to six times its initial volume at constant\n pressure of 2 x 10-5Nm-2. The work done is
4.0J
12.0J
2.0J
1.2J
\n """,
"""7  the driving mirror of a car has a radius of curvature of 1m. A vehicle behind the car is 4m from the mirror. \nFind the image distance behind the mirror.
7/ 8 
7/4 
9/4 
2 /9
\n """,
"""8  The thermometric substance of an absolute thermometer is
helium
alcohol
platinum
mercury.
\n """,
"""9  Find the frequencies of the first three harmonics of a piano string of length 1.5m, if the velocity of \nthe waves on the string is 120ms-1.
180Hz, 360Hz, 540Hz.
360Hz, 180Hz, 90Hz.
40Hz, 80Hz, 120Hz.
80Hz, 160Hz, 240Hz.
\n """,
"""10  The pressure of a given mass of a gas changes from 300Nm-2 to 120Nm-2 while the temperature drops \nfrom 127oC to –73oC. The ratio of the final volume to the initial volume is
2 : 5
4 : 5
5 : 2
5 : 4
\n """,
"""11  Ice cubes are added to a glass of warm water. The glass and water are cooled by
convection and radiation.
conduction only.
convection only.
conduction and convection.
\n """,
"""12  A working electric motor takes a current of 1.5A when the p.d. across it is 250V. If its efficiency is 80%,\n the power output is
469.0W
300.0W
4.8W
133.0W.
\n """,
"""13  In a Daniel Cell, the depolarizer, positive and negative electrodes are respectively
sulphuric acid, lead oxide and lead.
copper sulphate, copper and zinc.
potassium hydroxide, nickel and iron.
manganese dioxide, carbon and zinc.
\n """,
"""14  The cost of running five 6W lamps and four 100W lamps for 20 hours if electrical energy costs N10.00 per KWh is
N280.00
N160.00
N140.00
N120.00
\n """,
"""15  A bread toaster uses a current of 4A when plugged in a 240 volts line. It takes one minute to toast \nslices of bread. What is the energy consumed by the toaster?
3.60 x 103J
5.76 x 104J
1.60 x 102J
1.60 x 104J
\n """,
"""16  What is the angle of dip at the magnetic equator?
0o
45o
90o 
180o
\n """,
"""17  When a piece of rectangular glass block is inserted between two parallel plate capacitors, at constant \nplate area and distance of separation, the capacitance of the capacitor will
remain constant
decrease, then, increase
decrease
increase.
\n """,
"""18 A cell can supply currents of 0.4A and 0.2A through a 4.0ohms and 10.0ohms resistors respectively. \nThe internal resistance of the cell is
A. 1.5ohms
1.0ohms
2.5ohms
2.0ohms
\n """,
"""19  A cell of internal resistance r supplies current to a 6.0ohms resistor and its efficiency 75%, find the value of r.
2.0ohms
1.0ohms
4.5ohms
8.0ohms
\n """,
"""20 A resistance R is connected across the terminal of an electric cell of internal resistance 2 and the voltage\n was reduced to 5/3 of its nominal value. The value of R is
1ohms
2ohms
3ohms
6ohms
\n """,
"""21 A student is at a height 4m above the ground during a thunderstorm. Given that the potential difference between\n the thunderstorm and the ground is 107V, the electric field created by the storm is
2.0 x 106NC-1.
4.0 x 107NC-1.
1.0 x 107NC-1.
2.5 x 106NC-1.
\n """,
"""22  At resonance, the phase angle in an a.c. circuit is
0o
60o
90o
180o
\n """,
"""23  The process of energy production in the sun is
radioactive decay
electron collision.
Nuclear fission.
Nuclear fusion.
\n """,
"""24 I. Low pressure. II. High pressure. III. High p.d. IV. Low p.d. Which combination of the above is true\n of the conduction of electricity through gases?
II and III only.
II and IV only.
I and III only.
I and IV only.
\n """,
"""25  A capacitor of 20 x 10-12F and an inductor are joined in series. The value of the inductance that will\n give the circuit a resonant frequency of 200 KHz is
1/64
1/32
1/16
1/8
\n """,
"""26  Which of the following metals will provide the greatest shield against ionizing radiation?
Lead
Manganese
Aluminium
Iron.
\n """,
"""27  Energy losses through eddy currents are reduced by using
low resistance wires.
high resistance wires.
few turns of wire.
insulated soft iron wires.
\n """,
"""28  The particle emitted when 39K 19 decays to 39K 19 is
electron
beta
alpha
gamma.
\n """,
"""29 The magnetic force on a charged particle moving with velocity v is
independent of the magnitude of the charge.
proportional to both the magnitude of the charge and the velocity v.
proportional to the velocity v only.
proportional to the magnitude of the charge only.
\n """,
"""30 The force on a current carrying conductor in a magnetic field is greatest when the
conductor is at right angles with the field.
force is independent of the angle between the field and the conductor.
conductor is parallel with the field.
conductor makes an angle of 60o with the field.
\n """,
"""31 The primary coil of a transformer has N turns and is connected to a 120V a.c.power line. If the secondary \ncoil has 1000 turns and a terminal voltage of 1200 volts, what is the value of N?
1000
120
100
1200
\n """,
"""32  A copper cube weights 0.25 N in air, o.17N when completely immersed in paraffin oil and o.15N when completely \nimmersed in water. The ratio of upthrust in oil to upthrust in water is
3 : 5
4 :5
7:10
13:10
\n """,
"""33 A wheel and axle is used to raise a load of 500 N by the application of an effort of 250N. If the radii of the wheel and the axle are 0.4cm and o.1cm respectively, the efficiency of the machine is
20%
40%
50%
60%
\n """,
"""34 The hydrostatic blood pressure difference between the head and feet of a boy standing straight is 1.65 x 104 Nm-2. \nFind the height of the boy.[Density of blood = 1.1 x 10m3kgm-3, g = 10m-2]
0.5m
0.6m
1.5m
2.0m
\n """,
"""35  A body weighing 80N stands in an elevator that is about to move. The force exerted by the floor on the body\n as the elevator moves upward with an acceleration of 5ms-2
40 N
80 N
120N
160N
\n """,
"""36  If the distance between two suspended masses 10kg each is tripled, the gravitational force of attraction \nbetween them is reduced by
one half
one third
one quarter
one ninth
\n """,
"""37 If the total force acting on a particle is zero, the linear momentum will
increase
decrease
be constant
increase then decrease
\n """,
"""38 Two force each of 10N act on a body, one towards the north and the other towards the east. The magnitude and the\n direction of the resultant force are
20N, 450E
20N, 450W
10 2 N, 45oW
10 2N , 45oE
\n """,
"""39  A particle in circular motion performs 30 oscillations in 6 seconds. Its angular velocity is
5 rad s-1
6 rad s-1
5 pierad s-1
10 pierad s-1
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "D"),

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
        Physics_2015()
def Physics_2014():
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
        """0 the effect of a particle in a fluid attaining its terminal velocity is that the
acceleration is maximum
weight is equal to the retarding force
buoyancy force is equal to the viscous retarding force
buoyancy force is more than the weight of the fluid displaced
\n """,
"""1  A coin placed below a rectangular glass block of thickness 9cm and refractive index 1.5 is viewed vertically \nabove the block. The apparent displacement of the coin is
3cm
5cm
6cm
8cm
\n """,
"""2  The radiator of a motor car is cooled by
radiation
conduction
convection
radiation and conduction
\n """,
"""3  I. Temperature. II. Density of air molecules. III. Pressure. IV. Pitch. Which of the above will affect the\n velocity of sound in air?
I and II only.
II and IV only.
I, II and IV only.
I, II, III and IV.
\n """,
"""4  Which of the following is a characteristic of stationary wave?
They are formed by two identical waves traveling in opposite directions.
They can be transverse or longitudinal.
The distance between two successive nodes is one wavelength.
The antinode is a point of minimum displacement.
\n """,
"""5 To produce an enlarged and erect image with a concave mirror, the object must be positioned
at the principal focus.
beyond the centre of curvature.
between the principal focus and the centre of curvature.
between the principal focus and the pole.
\n """,
"""6  The property that is propagated in a traveling wave is
frequency
amplitude.
energy
wavelength
\n """,
"""7  Which of the following eye defects can be corrected using a cylindrical lens?
Myopia
Astigmatism
Presbyopia
Chromatic aberration
\n """,
"""8 The time rate of loss of heat by a body is proportional to the
difference in temperature between the body and its surroundings
temperature of its surroundings
ratio of the temperature of the body to that of its surroundings
temperature of the body.
\n """,
"""9  If tension is maintained on a stretched string of length 0.6m such that its fundamental frequency of 220Hz \nis excited, determine the velocity of the transverse wave in the string.
528ms-1
264ms-1
132ms-1
66ms-1
\n """,
"""10 A concave mirror of radius of curvature 40cm forms a real image twice as large as the object. The\n object distance is
10cm
30cm
40cm
60cm.
\n """,
"""11  Water is a poor thermometric liquid because it
is opaque
is a poor conductor.
wets glass.
has low vapour pressure.
\n """,
"""12  A ray of light which strikes a glass slab from air at normal incidence passes through the slab
undeviated and undisplaced at a lower speed.
deviated and undisplaced at a lower speed.
deviated and displaced at a lower speed.
undeviated and displaced at a faster speed.
\n """,
"""13  Blowing air over a liquid aids evaporation by
increasing its surface area.
decreasing its vapour pressure.
increasing temperature.
decreasing its density.
\n """,
"""14  The phenomenon that makes sound persist when its source has been removed is known as
acoustic vibration
rarefaction
echo
reverberation.
\n """,
"""15  The pressure of 3 moles of an ideal gas at a temperature of 27oC having a volume of 10-3m3 is [R = 8.3J mol-1K-1]
2.49 x 105Nm-2
7.47 x 105Nm-2
2.49 x 106Nm-2
7.47 x 106Nm-2
\n """,
"""16  Vibration in a stretched spring cannot be polarized because they are
stationary waves.
transverse waves.
longitudinal waves.
mechanical waves.
\n """,
"""17  The colours seen in soap bubbles are due to
diffraction
refraction
dispersion
interference.
\n """,
"""18  The energy stored in a capacitor of capacitance 10microF carrying a charge of 100microC is
5 x 104J
4 x 102J
4 x 10-3J
5 x 10-4J
\n """,
"""19  When connected to a mains of 250V, the fuse rating in the plug of an electric device of 1 kW is
2A
3A
4A
5A.
\n """,
"""20 The eye controls the amount of light reaching the retina by adjusting the
cornea
iris
retina
optic nerve.
\n """,
"""21  An electric iron is rated 1000W, 230V. What is the resistance of its element?
51.9
52.9
55.9
57.6
\n """,
"""22 The electromagnetic wave that can produce a heating effect on the environment is
X-rays
ultraviolet rays
infra-red rays
gamma rays
\n """,
"""23 An electric cell with nominal voltage E has a resistance of 3 connected across it. If the voltage\n falls to 0.6E, the internal resistance of the cell is
1ohms
2ohms
3ohms
4ohms
\n """,
"""24  Pure silicon can be converted to a ptype material by adding a controlled amount of
trivalent atoms
tetravalent atoms
pentavalent
hexavalent atoms
\n """,
"""25  The energy associated with the photon of a radio transmission at 3 x 105Hz is [h = 6.63 x 10-34Js]
2.00 x 10-28J
1.30 x 10-28J
2.00 x 10-29J
1.30 x 10-29J
\n """,
"""26  The percentage of the original nuclei of a sample of a radioactive substance left after 5 half-lives is
8%
5%
3%
1%
\n """,
"""27  From the generating station to each substation, power is transmitted at a very high voltage so as to reduce
hystersis loss
eddy current loss
magnetic flux leakage
heating in the coils.
\n """,
"""28 The particle that is responsible for nuclear fission in a nuclear reactor is
neutron
proton
electron
photon.
\n """,
"""29 A transistor is used in the amplification of signals because it
controls the flow of current.
consumes a lot of power.
allows doping.
contains electron and hole carriers.
\n """,
"""30  The carbon-granule microphone works on the principle of change in
inductance 
resistance
capacitance
voltage.
\n """,
"""31  At what frequency would a capacitor of 2.5miroF used in a radio circuit have a reactance of 250ohms?
pie/800 Hz
800/pie Hz
200pieHz
2000pieHz
\n """,
"""32  A current of 0.5A flowing for 3 hours deposits 2g of a metal during electrolysis. The quantity of the same \nmetal that would be deposited by a current of 1.5A flowing in 1 hour is
2g
6g
10g
18g
\n """,
"""33  Which of the following statements is true of the properties of a moving coil galvanometer?
The coil has a small area.
There are strong hair springs to give a large control couple.
There is a strong permanent magnet to give high magnetic flux.
It has a small number of turns of coil.
\n """,
"""34  A bead traveling on a straight wire is brought to rest at 0.2m by friction. If the mass of the bead is 0.01kg \nand the coefficient of friction between the bead and the wire is 0.1, determine the workdone by the friction.[g = 10 ms-1.]
2 x 10-4J
2 x 10-3J
2 x 101J
2 x 102J
\n """,
"""35  On top of a spiral spring of force constant 500Nm-1 is placed a mass of 5 x 10-3 kg. If the spring is \ncompressed downwards by a length of 0.02m and then released, calculate the height to which the mass is projected.
8m
4m
2m
1m
\n """,
"""36 A test tube of radius 1.0cm is loaded to 8.8g. If it is placed upright in water, find the depth to which it \nwould sink.[g = 10ms–2; density of water = 1000kgm-3]
2.8cm
5.2cm
25.5cm
28.0cm
\n """,
"""37  A hose of cross-sectional area 0.5m2 is used to discharge water from a water tanker at a velocity of 60ms-1 \nin 20s into a container. If the container is filled completely, the volume of the container is
240m3
600m3
2400m3
6000m3
\n """,
"""38  If an object just begins to slide on a surface inclined at 30o to the horizontal, the coefficient of friction is
∫3
∫3 / 2
1/∫2 
1/∫3 
\n """,
"""39 A force of 100N is used to kick a football of mass 0.8kg. Find the velocity with which the ball moves\n if it takes 0.8s to be kicked.
32ms-1
50ms-1
64ms-1
100ms-1
\n """,
"""40 Water does not drop through an open umbrella of silk material unless the inside of the umbrella is touched.\n This is due to
capillarity
osmotic pressure
viscosity
surface tension.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "D"),
        Question(question_prompts[40], "D"),

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
        Physics_2014()
def Physics_2013():
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
        """0 The stylus of a phonograph record exerts a force of 7.7 x 10-2N on a groove of radius 10-5m. \nCompute the pressure exerted by the stylus on the groove.
2.45 x 108Nm-2
3.45 x 108Nm-2
4.90 x 108Nm-2
2.42 x 109Nm-2
\n """,
"""1  A piece of stone attached to one end of a string is whirled round in a horizontal circle and the string \nsuddenly cuts. The stone will fly off in a direction
perpendicular to the circular path.
parallel to the circular path.
tangential to the circular path.
towards the centre of the circle.
\n """,
"""2  A 90cm uniform lever has a load of 30N suspended at 15cm from one of its ends. If the fulcrum is at the\n centre of gravity, the force that must be applied at its other end to keep it in horizontal equilibrium is
15N
20N
30N
60N.
\n """,
"""3  A satellite is in a parking orbit if its period is
less than the period of the earth.
more than the period of the earth.
equal to the period of the earth.
the square of the period of the earth.
\n """,
"""4  A tuning fork of frequency 340 Hz is vibrated just above a cylindrical tube of height 1.2m. If water is\n slowly poured into the tube, at what maximum height will resonance occur?[Speed of sound in air = 340ms-1].
0.95m
0.60m
0.50m
0.45m
\n """,
"""5  By what factor will the size of an object placed 10cm from a convex lens be increased if the image is seen\n on a screen placed 25cm from the lens?
15.0
2.5
1.5
0.4
\n """,
"""6  Thermal equilibrium between two objects exists when
the temperatures of both objects are equal.
the quantity of heat in both objects is the same.
the heat capacities of both objects are the same.
one object loses heat continuously to the other.
\n """,
"""7  An open pipe closed at one end produces its first fundamental note. If the velocity of sound in air is v and l \nthe length of the pipe, the frequency of the note is
2v/I
v/5I
v/4I
v/2I
\n """,
"""8  Given that Young’s modulus for aluminium is 7.0 x 1010 Nm-2 and density is 2.7 x 103kgm-3, find the \nspeed of the sound produced if a solid bar is struck at one end with a hammer.
5.1 x 103ms-1
4.2 x 103ms-1
3.6 x 103ms-1
2.8 x 103ms-1
\n """,
"""9 On a fairly cool rainy day when the temperature is 20oC, the length of a steel railroad track is 20cm.\n What will be its length on a hot dry day when the [Coefficient of linear expansion of steel = 11 x 10-6 K-1]. temperature is 40oC?
20.013m
20.009m
20.004m
20.002m
\n """,
"""10 If an object is placed between two parallel plane mirrors with their reflecting surfaces facing each other,\n how many images of the object will be formed?
Infinite
Eight
Four
Two.
\n """,
"""11 The phenomenon whereby the water droplets in the atmosphere combine with dust particles in the air to reduce\n visibility is
cloud
mist
hail
fog.
\n """,
"""12  At what position will an object be placed in front of a concave mirror in order in order to obtain an\n image at infinity?
At the pole of the mirror.
At the principal focus.
At the centre of curvature
Between the principal focus and the centre of curvature.
\n """,
"""13  If the distance from a point source of sound is doubled, by what factor does the intensity decrease?
4.00
2.00
0.50
0.25
\n """,
"""14  A 2000W electric heater is used to heat a metal object of mass 5kg initially at 10oC. If a temperature rise\n of 30oC is obtained after 10 min, the heat capacity of the material is
6.0 x 104JoC-1
4.0 x 104JoC-1
1.2 x 104JoC-1
8.0 x 103JoC-1
\n """,
"""15  If 1.2 x 106 J of heat energy is given off in 1 sec from a vessel maintained at a temperature gradient of\n 30Km-1, the surface area of the vessel is
1.0 x 102 m2
9.0 x 102 m2
1.0 x 103 m2
9.0 x 104 m2
\n """,
"""16  A positively charged rod X is brought near an uncharged metal sphere Y and is then touched by a finger\n with X still in place. When the finger is removed, the result is that Y has
no charge and a zero potential.
a positive charge and a zero potential
a negative charge and a positive potential.
a negative charge and a negative potential.
\n """,
"""17 The operation of an optical fibre is based on the principle of
dispersion of light
interference of light
refraction of light
polarization of light.
\n """,
"""18  A ray of light is incident on an equilateral triangular prism of refractive index 3/2. Calculate the \nangle through which the ray is minimally deviated in the prism.
30.0o
37.2o
42.0o
48.6o
\n """,
"""19  A wire of 5Ω resistance is drawn out so that its new length is two times the original length. If the resistivity of the wire remains the same and the crosssectional area is halved, the new resistance is
40Ω
20 Ω
10 Ω
5 Ω
\n """,
"""20  An electron of charge 1.6 x 10-19C is accelerated between two metal plates. If the kinetic energy of the\n electron is 4.8 x 10-17J, the potential difference between the plates is
30V
40V
300V
400V
\n """,
"""21  A magnetic field is said to exist at a point if a force is
exerted on a stationary charge at the point.
exerted on a moving charge at the point.
deflected at the point.
strengthened at the point.
\n """,
"""22 I. It retains its magnetism much longer than steel. II. It is more easily magnetized than steel. III. It is more \neasily demagnetized than steel. IV. It produces a stronger magnet than steel. Which combination of the above makes iron preferable to steel in the making of electromagnets?
I and II only
II and III only
I, III and IV only.
II, III and IV only.
\n """,
"""23  Which of the following pairs of light rays shows the widest separation in the spectrum of white light?
Blue and red.
Green and yellow
Indigo and violet
Orange and red.
\n """,
"""24 The most suitable cell used for short interval switches in electric bells is a
lead-acid accumulator.
Daniel Cell
Leclanche Cell
nickel-iron accumulator.
\n """,
"""25  A ray incident on a glass prism undergoes minimum deviation when the
incident angle is equal to the angle of refraction.
refraction angle equals 90o.
incident angle equals 90o
incident angle is equal to the angle of emergence.
\n """,
"""26  In the calibration of an ammeter using Faraday’s law of electrolysis, the ammeter reading is kept constant at 1.20A.\n If 0.990g of copper is deposited in 40 minutes, the correction to be applied to the ammeter is [e.c.e. of copper = 3.3 x 10-4gC-1]
0.30A
0.04A
0.05A
0.06A.
\n """,
"""27  The count rate of a radioactive material is 800 count/min. If the half-life of the material is 4 days, what would\nbe the count rate 16 days later?
200 count/min.
100 count/min.
50 count/min.
25 count/min.
\n """,
"""28  A circuit has an area of 0.4m2 and consists of 50 loops of wire. If the loops are twisted and allowed to \nrotate at a constant angular velocity of 10 rad s-1 in a uniform magnetic field of 0.4T, the amplitude of the induced voltage is
8V
16V
20V
80V.
\n """,
"""29  If the uncertainty in the measurement of the position of a particle is 5 x 10-10m, the uncertainty in the \nmomentum of the particle is
1.32 x 10-44Ns
3.30 x 10-44Ns
1.32 x 10-24Ns
3.30 x 10-24Ns
\n """,
"""30  The force on a charge moving with velocity v in a magnetic field B is half of the momentum force when the angle\n between v and B is
90o
45o
30o
0o.
\n """,
"""31  The maximum kinetic energy of the photoelectrons emitted from a metal surface is 0.34eV. If the work function of\n the metal surface is 1.83eV, , find the stopping potential.
2.17V
1.49V
1.09V
0.34V
\n """,
"""32  When an alternating current given by I = 10sin(120π)t passes through a 12Ω resistor, the power dissipated in \nthe resistor is
1200W
600W
120W
30W
\n """,
"""33  In a fission process, the decrease in mass is 0.01%. How much energy could be obtained from the fission of\n 1.0g of the material?[c = 3.0 x 108ms-1]
9.0 x 109J
9.0 x 1010J
6.3 x 1011J
9.0 x 1011J
\n """,
"""34  In a semi-conductor junction diode, as the depletion or barrier layer is forwardbiased, the layer
widens
narrows
remains constant
widens then narrows.
\n """,
"""35  An electron makes a transition from a certain energy level Ek to the ground state Eo. If the frequency of\n emission is 8.0 x 1014Hz, the energy emitted is [h = 6.6 x 10-34Js]
8.25 x 10-19 J
5.28 x 10-19J
5.28 x 1019J
8.25 x 1019J
\n """,
"""36 The major difference between a pure semi-conductor and a pure metal is that
metals are harder than semiconductors.
while the resistance of metals decreases with temperature, the reverse is the case for semiconductors.
the resistance of metals increases with temperature while for semiconductors, it is the reverse.
metals have forbidden gaps while semi-conductors have not.
\n """,
"""37  When a nucleus is formed by bringing protons and neutrons together, the actual mass of the formed nucleus is\n less than the sum of the masses of the constituent protons and neutrons. The energy equivalent of this mass difference is the
lost energy
work function
binding energy
stability energy.
\n """,
"""38  Which types of mirrors are capable of producing parallel beams of light such as those arising from the \nheadlamps of a car?
Cylindrical mirrors
Parabolic mirrors
Spherical mirrors
Plane mirrors.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "C"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "B"),

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
        Physics_2013()
def Physics_2012():
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
        """0 A person can focus an object only when it lies within 200cm from him. Which spectacles should be used to \nincrease his maximum distance of distinct vision to infinity?
Concave lens 
Plane glasses
Binoculars 
Convex lens.
\n """,
"""1  In which of the following material media would sound travel faster?
Water 
Oil 
Metal 
Gas.
\n """,
"""2  Calculate the angle of minimum deviation for a ray which is refracted through an equiangular prism of\n refractive index 1.4.
29o 
60o 
99o 
90o.
\n """,
"""3  What happens to the rays in a parallel beam of light?
They diverge as they travel.
They meet at infinity.
They intersect
They converge as they travel.
\n """,
"""4 If u is the object distance and v the image distance, which of the following expressions gives the linear\n magnification produced by a convex lens of focal length f?
u/v + f 
u/f - f 
v/f -1
v/u +1
\n """,
"""5  A ray of light makes an angle of 35o with a plane mirror. What is the angle of reflection?
55o 
35o 
70o 
65o
\n """,
"""6 The pitch of a sound note depends on
timbre 
harmonics 
quality
frequency.
\n """,
"""7  If the angle between two vectors P and Q is 0o, the vectors are said to
be perpendicular 
be parallel
interest at angle 60o.
intersect at angle 45o.
\n """,
"""8  A machine whose efficiency is 60% has a velocity ratio of 5. If a force of 500N is applied to lift a load P,\n what is the magnitude of P?
750N 
4166N
500N 
1500N
\n """,
"""9  A body of mass 4kg is acted on by a constant force of 12N for 3 seconds. The kinetic energy gained by the\n body at the end of the time is
162J 
144J 
72J 
81J
\n """,
"""10  As the pressure of a fluid increases, its viscosity
decreases 
remains constant
increases then decreases
increases.
\n """,
"""11  I. Jet-propelled aircraft II. Rocket propulsion III. The recoil of a gun IV. A person walking. Which of the\n above is based on Newton’s third law of motion?
I, II, III and IV 
I and III only
I and II only
I, II and III only.
\n """,
"""12  In a hydraulic press, a force of 40N is applied on the effort piston of area 0.4m2. If the force exerted on the \nload piston is 400N, the area of the large piston is
8m2 
4m2 
2m2 
1m2
\n """,
"""13  A 100kg box is pushed along a road with a force of 500N. If the box moves with a uniform velocity,\n the coefficient of friction between the box and the road is
0.5 
0.4 
1.0 
0.8
\n """,
"""14  The earth is four times the size of the moon and the acceleration due to gravity on the earth is 80 times that\n on the moon. The ratio of the mass of the moon to that of the earth is
1 : 320 
1 : 1280
1 : 80 
1 : 4
\n """,
"""15 A radioisotope has a decay constant of 10-7s-1. The average life of the radioisotope is
6.93 x 108s 
1.00 x 10-7s
1.00 x 107s 
6.93 x 107s
\n """,
"""16  A moving coil galvanometer has a fullscale deflection of 3A equivalent to 30o deflection. The sensitivity of\n the instrument is
10.0 
33.0 
90.0 
0.1
\n """,
"""17  The binding energy of helium He 42 is [atomic mass of proton = 1.00783 U, atomic mass of neutron = 1.00867 U]
2.017 U 
0.033 U 
4.033 U
0.330 U
\n """,
"""18  In a tuned radio receiver, L, C series circuit for resonance, the inductive and capacitive reactance XL and Xc\n respectively are related as
XL = 1/XC
XL = 1/2XC
XL = XC
XL = 2XC
\n """,
"""19  For semi-conductors to have negative temperature coefficient of resistance implies that
they have electrons and holes at high temperatures.
their resistance is constantly changing with temperature.
their resistance increases with temperature
their resistance decreases with temperature.
\n """,
"""20  Fluorescent tubes produce light by the
refraction of light by gas molecules
excitation of gas molecules.
conduction of solar energy
thermal agitation of electrons in the tube.
\n """,
"""21  In a reversed biased junction diode, current flows in by
electrons alone
majority carriers.
minority carriers.
positive holes alone.
\n """,
"""22  The energy stored in an inductor of inductance 5mH when a current of 6A flows through it is
1.8 x 10-2 J 
9.0 x 10-3 J
1.4 x 10-2 J 
9.0 x 10-2 J
\n """,
"""23  X-rays can be used in the study of crystal structures because they
have an extremely short wavelength.
have a very long-reaching wavelength.
are very fast.
are invisible.
\n """,
"""24  An a.c. circuit of e.m.f. 12V has a resistor of resistance 8Ω connected in
series to an inductor of inductive reactance 16Ω and a capacitor ofcapacitive reactance 10Ω. The current
flowing in the circuit is
1.4A 
14.0A 
1.2A 
12.0A
\n """,
"""25  A generator-manufacturing company was contracted to produce an a.c. dynamo but inadvertently produced a \nd.c. dynamo. To correct this error, the
commutator should be replaced with slip rings.
commutator should be replaced with split rings.
Armature coil should be made of aluminium.
Armature coil should be made of silver.
\n """,
"""26  Transverse waves can be distinguished from longitudinal waves using the characteristic of
diffraction 
polarization
reflection 
refraction.
\n """,
"""27  A man exerts a pressure of 2.8 x 103 Nm-2 on the ground and has 4 x 10-2m2 of his feet in contact\n with the ground. The weight of the man is
112N 
140N 
102N 
140N
\n """,
"""28  When left in a freezer, a bottle full of water cracks on freezing into ice because of the
decrease in the volume of water.
contraction of the bottle.
expansion of the bottle.
increase in the volume of water.
\n """,
"""29  The change in volume when 450kg of ice is completely melted is [Density of ice = 900 kgm-3;\n Density of water =1000 kgm-3]
0.05m3 
0.45m3
4.50m3 
0.50m3
\n """,
"""30  If a force of 50N stretches a wire from 20m to 20.01m, what is the amount offorce required to stretch the\n same material from 20m to 20.05m?
100N
50N
250N
200N.
\n """,
"""31  Tea pots are often silver-coated to prevent heat loss by
convection and conduction
radiation only
conduction only
convection only
\n """,
"""32  Metal rods of length 20m each are laid end to end to form a bridge at 25oC. What gap will be provided between \nconsecutive rails for the bridge to withstand 75oC?
0.22m 
0.25m 
0.02m
0.20m
\n """,
"""33  A 50W electric heater is used to heat a metal block of mass 5kg. If in 10 minutes, a temperature rise of 12oC\n is achieved, the specific heat capacity of the metal is
500 J kg-1 K-1 
130 J kg-1 K-1
390 J kg-1 K-1 
400 J kg-1 K-1
\n """,
"""34  I. Wavelength II. Medium of propagation III. Wave velocity IV. Frequency. V. Energy. Which of the above are used\n for characterizing waves?
I, II and V 
III, IV and V.
I and IV. 
I, III and IV.
\n """,
"""35  The instrument used for securing a large number of similar charges by induction is called
capacitor 
electrophorus
electroscope 
proof-plane
\n """,
"""36  A steady current of 2A flows in a coil of emf 12V for 0.4s. A back emf of 3V was induced during this period.\nThe stored energy in the loop that can be utilized is
7.2J 
12.0J 
2.4J 
9.6J
\n """,
"""37  If 16mA of current flows through a conductor in one second, the number of electrons transported per second is
1.00 x 1020 
1.00 x 1017
2.56 x 10-17 
2.56 x 10-18
\n """,
"""38  The difference between X-rays and gamma rays is that
X-rays arise from energy changes in the electronic structure of atoms while gamma rays come from the nucleus.
X-rays are electromagnetic radiations while gamma rays are negatively charged radiations.
X-rays have higher frequencies than gamma rays.
X-rays are more penetrating than gamma rays.
\n """,
"""39  To protect a material from the influence of an external magnetic field, the material should be kept in a
square steel ring
loop of copper wire
triangular zinc ring
soft iron ring.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "D"),

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
        Physics_2012()
def Physics_2011():
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
        """0 Which of the following is an electrolyte?
Grape juice 
Sugar solution
Alcohol 
Paraffin
\n """,
"""1  Electrical appliances in homes are normally earthed so that
both the a.c. and d.c. sources can be used
a person touching the appliances is safe from electric shock.
the appliances are maintained at a higher p.d. than the earth.
the appliances are maintained at a lower p.d. than the earth.
\n """,
"""2  A cell whose internal resistance is 0.5Ω delivers a current of 4A to an external resistor. The lost voltage \nof the cell is
1.250V 
8.000V
0.125V
2.000V
\n """,
"""3  Given three capacitors 0.3μF, 0.5μF and 0.2μF, the joined capacitance when arranged to give minimum capacitance is
0.3 μF 
1.0 μF 
0.1 μF
0.5 μF
\n """,
"""4  The pair of physical quantities consisting of vectors only are
A. displacement and torque
B. momentum and power.
C. acceleration and speed.
D. velocity and distance.
\n """,
"""5 A motorcyclist traveling at 30ms-1 starts to apply his brakes when he is 50m from the traffic light that had just \nturned red. If he reached the traffic light, his deceleration is
18 ms-2 
10 ms-2
9 ms-2 
5 ms-2
\n """,
"""6 An object is projected from a height of 80m above the ground with a velocity of 40ms-1 at an angle of 30o to the\n horizontal. The time of flight is [g = 10ms-2]
16s 
10s 
8s 
4s
\n """,
"""7  A force of 200N acts between two objects at a certain distance apart. The value of the force when the distance is\n halved is
800N 
400N 
200N 
100N
\n """,
"""8  An elastic material has length of 36cm when a load of 40N is hung on it and a length of 45cm when a load of 60N is \nhung on it. The original length of of the string is
20cm 
18cm 
15cm 
12cm
\n """,
"""9  Two liquids L1 and L2 are contained in a U-tube. The height and the density of L1 are 8cm and 103 kgm-3 \nrespectively. If the density of L2 is 800 kgm-3, its height measured from the same level is
16cm 
12cm 
10cm 
8cm.
\n """,
"""10  A body of mass 36kg falls through a viscous liquid which offers a drag force of 260N on the body. The upthrust \non the body at terminal velocity is [g = 10 ms-2]
50N 
100N 
310N 
620N
\n """,
"""11  A 3m3 volume of liquid W of density 200 kgm-3 is mixed with another liquid of volume 7 m3 and density 150 kgm-3.\n The density of the mixture is
350 kgm-3 
265 kgm-3
165 kgm-3 
100 kgm-3
\n """,
"""12  I. Reproducibility II. Sensitivity III. High thermal capacity IV. High accuracy. The qualities of a good\n thermometer include
II, III and IV only
I, II and III only.
I, II and IV only.
I, III and IV only.
\n """,
"""13  When very hot water is poured into two identical thin and thick glass tumblers inequal volumes, the thick one cracks because
glass is a good conductor of heat.
of the uneven expansion of glass.
glass is a crystal.
of the even expansion of glass.
\n """,
"""14  106J of heat is required to boil off completely 2kg of a certain liquid. Neglecting heat loss to the\n surroundings, the latent heat of vaporization of the liquid is
5.0 x 106 Jkg-1 
2.0 x 106 Jkg-1
5.0 x 105 Jkg-1 
2.0 x 105 Jkg-1
\n """,
"""15  The process whereby a liquid turns spontaneously into vapour is called
boiling 
evaporation
sublimation 
relegation.
\n """,
"""16  When the temperature difference between the wet and dry bulbs of a hygrometer is high, this indicates that
the relative humidity is high.
the relative humidity is low.
it is about to rain.
there is plenty of sunshine
\n """,
"""17 The process whereby the molecules of different substances move randomly is called
osmosis 
capillarity
diffusion 
surface tension.
\n """,
"""18. I. Melting II. Boiling III. Refraction IV. Conduction. Which combination of the above is evident of the\n molecular nature of matter?
I, II and III only 
II, III and IV only
I, II and IV only.
I, III and IV only.
\n """,
"""19  The velocity of sound in air will be doubled if its absolute temperature is
halved 
doubled 
quadrupled
constant.
\n """,
"""20  Marching soldiers crossing a suspension bridge are usually advised to break their steps to avoid damaging \nthe bridge owing to
resonance 
swinging 
vibration
oscillation.
\n """,
"""21  The sharpness of the boundary of the shadow of an object is determined by the
nature of the object
opacity of the object.
rays of light passing through the object
intensity of light striking the object.
\n """,
"""22  A real image three times the size of an object is formed 24cm from a converging mirror. What is the \nfocal length of the mirror?
6cm 
8cm 
12cm 
16cm
\n """,
"""23  A thin converging lens has a power of 4.0 diopters. Determine its focal length.
0.03m
0.25m 
2.50m 
5.00m
\n """,
"""24 Satellite communication network makes use of
sound wave 
radio wave
infra-red rays 
visible light.
\n """,
"""25 If the distance between two point charges is increased by a factor of four, the magnitude of the \nelectrostatic force between them will be
4 times its former value
1/2 of its former value.
1/4 of its former value.
1/16 of its former value.
\n """,
"""26  The electric field intensity in a place where a charge of 10-10C experiences a force of 0.4N is
8.0 x 109NC-1 
4.0 x 109NC-1
4.0 x 10-11NC-1 
8.0 x 10-12NC-131. 
\n """,
"""27 A car battery rated 45AH is charged with a charger whose rating is 2.5A. How long will it take to charge \nthe battery fully?
25 hrs 
20 hrs
18 hrs 
10 hrs
\n """,
"""28  The resistance of a piece of wire of length 20m and cross-sectional area 8 x 10-6m2 is
0.5Ω 
1.0Ω 
5.0Ω 
10.0Ω 
\n """,
"""29 An electric device is rated 2000W, 250V. The correct fuse rating of the device is
6A 
7A 
8A 
9A
\n """,
"""30  Two charged particles are projected into a region where there is a magnetic field perpendicular to their \nvelocities. If the charges are deflected in opposite directions, which of the following statements is true of the charges?
The charges are electrically neutral
The charges must be of opposite signs.
The charges are of the same sign.
Positive charges are more in number.
\n """,
"""31  The North pole of a magnet can never be separated from the South pole because of a property known as
magnetic monopole
magnetic dipole
magnetic quadrupole
magnetic octopole.
\n """,
"""32  A proton moving with a speed of 1.0 x 106 ms-1 through a magnetic field of 1.0T experiences a magnetic\n force of magnitude 8.0 x 10-14N. The angle between the proton’s velocity and the field is
90o 
60o 
45o 
30o.
\n """,
"""33  A transformer is rated 240V. If the primary coil is 4000 turns and the secondary voltage 12V, determine\n the number of turns in the secondary coil.
100 
150 
200 
250
\n """,
"""34  If two inductors of inductances 3H and 6H are arranged in series, the total inductance is
0.5H 
2.0H 
9.0H 
18.0H
\n """,
"""35  In an a.c. circuit that contains only a capacitor, the voltage lags behind the current 
30o 
60o 
90o 
180o
\n """,
"""36  The charge carriers in gases are
electrons only 
ions only
electrons and ions
electrons and holes.
\n """,
"""37 The amount of energy released when 0.5kg of uranium is burnt completely is
1.5 x 108J 
4.5 x 108J
1.5 x 1016J 
4.5 x 1016J. 
\n """,
"""38  The time it will take a certain radioactive material with a half-life of 50 days to reduce to1/32 of \nits original number is
150 days 
200 days 
250 days
300 days.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "C"),
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
        Physics_2011()
def Physics_2010():
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
         """0 The ray which causes gas molecules to glow is known as
gamma ray 
molecular ray
cathode ray 
anode ray.
\n """,
"""1  Which of the following materials is a conductor?
Sodium 
Glass 
Plastic
Wax.
\n """,
"""2  A silicon material is dropped with an element of a certain group and an ntype semi-conductor is formed. \nThe most likely group of the element is
I 
II 
III 
V.
\n """,
"""3  When impurities are added to semiconductors, the conductivity of the semi-conductor
increases 
decreases
remains constant.
increase then decreases.
\n """,
"""4  The current in a reverse-biased junction is due to
majority carriers 
holes
minority carriers 
electrons.
\n """,
"""5  A glass plate 0.9cm thick has a refractive index of 1.50. How long does it take for a pulse of light to pass\n through the plate?
3.0 x 10-11 s 
4.5 x 10-11 s
3.0 x 10-10 s 
4.5 x 10-10 s
\n """,
"""6 The fundamental frequency of a plucked wire under a tension of 400N is 250 Hz. When the frequency is changed\n to 500 Hz at constant length, the tension is
40N 
160N 
400N 
1600N
\n """,
"""7  The production of pure spectrum could easily be achieved using a
triangular prism only
triangular prism with two concave lenses
triangular prism with two convex lenses
glass prism with a pin.
\n """,
"""8  I. They should be identical. II. They should originate from the same source. III. they should be coherent.\n IV. They should be monochromatic. From the statements above, the conditions for two waves to interfere are
I, III and IV only
I, II. III and IV
I, II and III only
II, III and IV only.
\n """,
"""9  The instrument used by designers to obtain different colour patterns is called
episcope 
periscope
kaleiodoscope 
sextant
\n """,
"""10  When an object is placed between the principal focus and the optical centre of a convex lens, it could be used\n as a
reflecting lens
compound microscope
projector
simple microscope.
\n """,
"""11  In a large telecommunications auditorium, perforated absorbent materials are used to line the ceiling so as to
reduce the reverberation of sound in the hall.
reduce the height of the ceiling from the floor.
increase the reverberation of sound in the hall.
increase the amount of echo in the hall.
\n """,
"""12 The phenomenon of light bending round an obstacle is
 reflection 
 polarization
 refraction 
  diffraction
\n """,
"""13 The energy E of a photon and its wavelength are related by Eλ = X. The numerical value of X is[h = 6.63 x 1034 Js,\n c = 3 x 108 ms-1].
  1.99 x 10-27 
  6.60 x 10-26
   1.99 x 10-25 
  6.60 x 10-25
\n """,
"""14  A radioactive substance has a half-life of 20 days. What fraction of the original radioactive nuclei will remain\n after 80 days?
1/16
1/18
1/4
1/32
\n """,
"""15  Silicon doped with aluminium and germanium doped with arsenic become
  n-type semi-conductors
  p-type semi-conductors
  n- and p-types respectively
  p- and n-types respectively.
\n """,
"""16  A photon of wavelength 6.0 x 10-7 behaves like a particle of a certain mass.[h = 6.63 x 10-34Js, c = 3 x 108ms-1].\n The value of that mass is
  1.1 x 10-35 kg 
  2.2 x 10-27 kg
  3.5 x 10-36 kg 
  2.2 x 10-35 kg
\n """,
"""17 The bond that forms a semi-conductor is
  ionic 
 metallic 
  covalent
  electrovalent.
\n """,
"""18  The instrument that measures both a.c. and d.c. is
an inverter 
a current balance.
a moving coil ammeter.
a moving iron ammeter.
\n """,
"""19  Lenz’s law is a law of the conservation of
 energy 
 momentum
 electric 
 electric charge.
\n """,
"""20  A 120V, 60W lamp is to be operated on 220V a.c. supply mains. Calculate the value of non-inductive \nresistance that would be required to ensure that the lamp is run on correct value.
  500Ω 
  300Ω 
  200Ω 
  100Ω
\n """,
"""21  118.8 cm2 surface of the copper cathode of a voltameter is to be coasted with 10-6m thick copper of \ndensity 9 x 103 kgm-3. How long will the process run with 10A constant current?[e.c.e. of copper = 3.3 x 10-7 kg C-1].
  10.8 min 
  20.0 min.
 5.4 min. 
 15.0 min.
\n """,
"""22  A conductor has a diameter of 1.00mm and length 2.00m. If the resistance of the material is 0.1Ω, its resistivity\n is
 3.93 x 10-8 Ωm 
  3.93 x 10-6 Ωm
  2.55 x 102 Ωm 
  2.55 x 102 Ωm
\n """,
"""23  A charge 50μC has an electric field strength of 360 NC-1 at a certain point. The electric field strength due\n to another charge 120μC. kept at the same distance apart and in the same medium is
 18 NC-1 
 144 NC-1
 150 NC-1 
 864 NC-1
\n """,
"""24  Two long parallel wires X and Y carry currents 3A and 5A respectively. If the force experienced per unit\n length by X is 5 x 10-5N, the force per unit length experienced by wire Y is
 3 x 10-5N 
 3 x 10-6N
  5 x 10-4N 
 5 x 10-5N
\n """,
"""25 A 40 kW electric cable is used to transmit electricity through a resistor of resistance 2.0Ω at 800V. The power\n loss as internal energy is
 5.0 x 102W 
 4.0 x 103W
 5.0 x 103W 
 4.0 x 102W
\n """,
"""26  If two charged plates are maintained at a potential difference of 3 kV, the work done in taking a charge of 600μC\n across the field is
 9.0J 
 0.8J 
 18.0J 
 1.8J
\n """,
"""27  I. Mass II. Density III. Temperature IV. Nature of substance Which of the above affect diffusion?
  I, II and IV only
 II, III and IV only
  I, II, III and IV.
  I and II only.
\n """,
"""28  A string of length 4m is extended by 0.02m when a load of 0.4 kg is suspended at its end. What will be the[g = 10ms-2].\n length of the string when the applied force is 15N?
  5.05m 
  6.08m 
  4.05m
  4.08m. 
\n """,
"""29  I. Use a liquid with a high melting point II. Use a liquid of high volume expansivity III. Use a capillary tube \nof large diameter. Which of the above best describes how the sensitivity of a liquid-in-glass thermometer can be enhanced?
 II only 
 II and III only
 I only 
 I and III only.
\n """,
"""30  The blade of a hoe feels colder to touch in the morning than the wooden handle because the
  handle contains stored energy in form of heat.
 blade is placed at a lower temperature than the handle.
 handle is a better conductor of heat than the blade.
 blade is a better conductor of heat than the handle.
\n """,
"""31  Which of the following gas laws is equivalent to the work done?
 Pressure Law
 Van der Waal’s Law
 Boyle’s Law 
 Charles’ Law
\n """,
"""32  A piece of iron weighs 250N in air and 200N in a liquid of density 1000 kgm-3. The volume of the iron is\n[g = 10ms-2]
  2.0 x 10-3m3 
  2.5 x 10-3m3
  4.5 x 10-3m3 
 5.0 x 10-3m3
\n """,
"""33  I. Increase the melting point of the liquid. II. Increase the boiling point of the liquid. III. decrease the \nmelting point of the liquid. IV. decrease the boiling point of the liquid. Which of the statements above about the effects of increase in pressure in a liquid are correct?
 II and III only
 III and IV only
 I and III only
 I and II only.
\n """,
"""34  A blacksmith heated a metal whose cubic expansivity is 6.3 x 10-6K-1. The area expansivity is
  6.3 x 10-6K-1
  4.2 x 10-6K-1
  2.1 x 10-6K-1 
  2.0 x 10-6K-1
\n """,
"""35  The differences observed in solids, liquids and gases may be accounted for
 their relative masses
 their melting points
 the different molecules in each of them.
 the spacing and forces acting between the molecules.
\n """,
"""36  A reservoir 500m deep is filled with a fluid of density 850kg-3. If the atmospheric pressure is 1.05 x 105 Nm-2,\n the pressure at the bottom of the reservoir is[g = 10ms-2]
 4.36 x 106Nm-2 
 4.25 x 106Nm-2
 4.72 x 106Nm-2 
 4.28 x 106Nm-2
\n """,
"""37 A clinical thermometer is different from other mercury in glass thermometers owing to
  its long stem.
 the constriction on its stem.
  its wide range of temperature.
 the grade of mercury used in it.
\n """,
"""38  2 kg of water is heated with a heating coil which draws 3.5A from a 200V mains for 2 minutes. What is\n the increase in temperature of the water?
 25oC 
 15oC
 10oC 
 30oC
\n """,
"""39 A boy drags a bag of rice along a smooth horizontal floor with a force of 2N applied at an angle of 60o \nto the floor. The work done after a distance of 3m is
 6J 
 5J 
 4J 
 3J
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "D"),

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
        Physics_2010()
def Physics_2009():
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
        """0 Two spheres of masses 5.0 kg and 10.0 kg are 0.3m apart. Calculate the force of attraction between them.\n[G = 6.67 x 10-11Nm2kg-2]
        3.71 x 10-8N 
        3.57 x 10-2N
        4.00 x 102N 
        3.50 x 10-10N
       \n """,
        """1  A car of mass 1500 kg goes round a circular curve of radius 50m at a speed of 40ms-1. The magnitude of \nthe centripetal force on the car is
         1.2 x 102N 
          1.2 x 103N
         4.8 x 103N 
         4.8 x 104N
        \n """,
        """2 The unit of moment of a couple can be expressed in
         Nm 
         Nm-1 
         Nm2 
         Nm-2
        \n """,
        """3  A machine has a velocity ratio of 4. If it requires 800N to overcome a load of 1600N, what is the \nefficiency of the machine?
          2% 
          40% 
         50% 
         60%.
        \n """,
        """4  A gramophone record takes 5s to reach its constant angular velocity of 4π 32 rads-1 from rest. Find its\n constant angular acceleration.
         20.0π rads-2 
         1.3π rads-2
         0.08π rads-2 
          0.4π rads-2
        \n """,
        """5  A particle of weight 120N is placed on a plane inclined at an angle 30o to the horizontal. If the plane\n has an efficiency of 60%, what is the force required to push the weight uniformly up the plane?
         210N 
          175N 
         100N 
         50N.
        \n """,
        """6  The dimensions of electromotive force are
          ML2T-3I-1 
          ML2T-3I-2
          M2LT2I-1 
          M2L2T-1I-1
        \n """,
        """7 I. Force(N)II. Torque (Nm-1) III. Current (A) IV. Power (W) Which of the above are the correct \nS. I.Units of the quantities indicated?
          I and II only 
         I and III only
         I, II and III only 
          I, III and IV only
        \n """,
        """8 The resultant of two forces 12N and 5N is 13N. What is the angle between the two forces?
          0o 
         45o 
         90o 
         180o
        \n """,
        """9  Which of the following is NOT a vector quantity?
          Altitude 
         Acceleration
         Displacement
          Weight
        \n """,
        """10 A force F is required to keep a 5kg mass moving round a cycle of radius 3.5m at a speed of 7ms-1. What is\n the speed, if the force is tripled?
        4.0ms-1 
        6.6ms-1
         12.1ms-1 
        21.0ms-1
        \n """,
        """11  If a wheel 1.2m in a diameter rotates at one revolution per second, calculate the velocity of the wheel.
         3.6ms-1 
         3.8ms-1
          4.0ms-1 
          7.5ms-1
        \n """,
        """12 A body of mass 4 kg resting on a smooth horizontal plane is simultaneously acted upon by two perpendicular\n forces 6N and 8N. Calculate the acceleration of the motion.
          2.5ms-2 
         3.0ms-2
         4.0ms-2 
          4.5ms-2
        \n """,
        """13 I. All the three forces must be concurrent. II. The upward force is equal to the downward force. \nIII. The algebraic sum of the moment about any point must be zero. Which of the above conditions must hold for a body acted upon by a system of three coplanar forces in equilibrium?
         I and II only 
         I and III only
         II and III only 
         I, II and III.
        \n """,
        """14  What is the frequency of vibration if the balance wheel of a wristwatch makes 90 revolutions in 25s? 
          0.01Hz 
          0.04Hz
         2.27Hz 
         3.60Hz
        \n """,
        """15  Counting of currency notes with moist fingers is based on the principles of
         diffusion 
          cohesion
          adhesion 
          viscosity
        \n """,
        """16  A motorcycle of mass 100kg moves round in a circle of radius 10m with a velocity of 5ms-1. Find the\n coefficient of friction between the road and the tyres. [g  10ms-2]
          25.00
          2.50 
         0.50
          0.25 
        \n """,
        """17  A spring of force constant 500Nm-1 is compressed such that its length shortens by 5cm. The energy stored \nin the spring is
          0.625J 
         6.250J
         62.500J 
         625.000J
        \n """,
        """18  In the Hare’s apparatus, water rises to a height of 26.5cm in one limb. If a liquid rises to a \nheight of 20.4cm in the other limb, what is the relative density of the liquid?
         0.8 
         1.1 
         1.2 
         1.3
        \n """,
        """19 When cold water is poured on a can containing hot water, the can collapses because the
         steam condenses and occupies the partial vacuum in the can 
         external air pressure counterbalances the pressure within the can
         steam expands to occupy the vacuum remaining in the can
         external pressure becomes greater than the pressure within the can
        \n """,
        """20  An empty density bottle weighs 2N. If it weighs 5N when filled with water and 4N when filled with \nolive oil, the relative density of olive oil is
        1/3
        2/3
        1/5
        2/5
        \n """,
        """21  The thermometric property of a thermocouple is the change in
         equivalent resistance
         electromotive force
         colour
          pressure.
        \n """,
        """22  During summer, the balance wheel of a clock expands. What effect does this have on the accuracy of \nthe clock?
         The clock gains time.
         The accuracy of the clock is not affected.
         The clock loses time.
         The clock stops working.
        \n """,
        """23  A sealed flask contains 600cm3 of air at 27oC and is heated to 35oC at constant pressure. \nThe new volume is
         508cm3 
         516cm3
          608cm3 
         616cm3
        \n """,
        """24  A block of aluminium is heated electrically by a 25W heater. If the temperature rises by 10oC in \n5 minutes, the heat capacity of the aluminium is
         850JK-1 
         750JK-1
         650JK-1
         500JK-1
        \n """,
        """25 If the partial pressure of water vapour at 27oC is 18mm Hg and the saturated vapour pressure of the\n atmosphere at the same temperature is 24mm Hg, the relative humidity at this temperature is
          25% 
         33%
         75% 
          82%
        \n """,
        """26 In a good thermos flask, the main cause of heat loss is
         conduction through the cork
         the plastic base of the thermos flask
          the silvered walls and shiny metals
         the outer cover or jacket.
        \n """,
        """27  Given the progressive wave equation y = 5 sin (2000t – 0.4x), calculate the wavelength.
         12.4m 
         15.7m
         17.5m 
         18.6m
        \n """,
        """28 The fundamental property of a propagating wave which depends only on the source and not the medium of \npropagation is the
          wavelength 
          harmonics
          frequency 
         velocity.
        \n """,
        """29  When the length of a vibrating string is reduced by one-third, its frequency becomes
         three times its former value
         twice its former value
         one-third of its former value
         one-sixth of its former value.
        \n """,
        """30 I. Total internal reflection of light II. Conservation of light energy III. Relative motion of the earth,\n sun and moon. IV. Rectilinear propagation of light. Which of the above is a phenomenon of total solar eclipse?
         I and IV only
         II and IV only
         I and III only
         III and IV only.
        \n """,
        """31  An object of height 4cm is placed in front of a cuboid pinhole camera of size 6cm. If the image formed \nis 2cm high, how far is the object from the pinhole?
         3.0cm 
         8.0cm
         12.0cm 
         16.0cm
        \n """,
        """32  An object of height 5cm is placed at 20cm from a concave mirror of focal length 10cm. The image height is
          20cm 
          15cm
          10cm 
          5cm
        \n """,
        """33 Convex mirrors are used as driving mirrors because images formed are
         erect, virtual and diminished
         erect, real and diminished
         erect, virtual and magnified
         inverted, virtual and diminished.
        \n """,
        """34  If a convex lens of focal length 12cm is used to produce a real image four times the size of the object,\n how far from the lens must the object be placed?
         10cm 
         15cm
         20cm 
         25cm.
        \n """,
        """35  An object placed at the bottom of a well full of clear water appears closer to the surface due to
         diffraction 
         reflection
         refraction 
         polarization
        \n """,
        """36  In the microscope, the eyepiece lens merely acts as
          an inverter 
          a refiner
          a diminisher 
         a magnifier
        \n """,
        """37  An observer with normal eyes views an object with a magnifying glass of focal length 5cm. The angular\n magnification is [least distance of distinct vision D = 25cm]
          -6 
          -5 
         5 
          6
        \n """,
        """38  A short chain is sometimes attached to the back of a petrol tanker to
          generate more friction
          ensure the balancing of the tanker
          caution the driver when overspeeding
         conduct excess charges to the earth
        \n """,
        """39  An electric generator has an e.m.f. of 240V and an internal resistance of 1ohms. If the current supplied\n by the generator is 20A when the terminal voltage is 220V, find the ratio of the power supplied to the power dissipated.
         11 : 1 
         1 : 11
         12 : 11 
         11 : 12
        \n """,
        """40  A generator is on daily use and in the process, ten 60W and five 40W tungsten bulbs are on for the same\n time interval. The energy consumed daily is
          0.96kWh 
          1.92kWh
         9.60kWh 
         19.20kWh
        \n """,
        """41  The d.c. generator has essentially the same components as the a.c. generator except the presence of
          slip-ring 
          carbon brushes
          split ring 
         armature
        \n """,
        """42  A step-down transformer has a power output of 50W and efficiency of 80%. If the mains supply voltage is 200V, \ncalculate of the primary current of the transformer.
         0.31A 
         3.20A
          3.40A 
          5.00A
        \n """,
        """43  If electrons are accelerated from rest through a potential difference of 10kV, what is the wavelength of \nthe associated electron?[m = 9.1 x 10-31kg, e = 1.6 x 10-19C,h = 6.6 x 10-34Js]
          1.22 x 10-11m 
          3.87 x 10-10m
          2.27 x 1011m 
         2.27 x 1014m
        \n """,
        """44  Caesium has a work function of 3 x 10-19J. The maximum energy of liberated electrons when it is illuminated \nby light of frequency 6.7 x 1014Hz is[h = 6.6 x 10-35Js]
          1.42 x 10-19J 
          3.00 x 10-19J
          4.42 x 10-19J 
          7.42 x 10-19J
        \n """,
        """45  Zener diode is used for
         current amplification
          power amplification
          voltage regulation
         energy conversion.
        \n """,
        """46  When a pure semiconductor is heated, its resistance
        A. increases 
          decreases
          remains the same
         increases and then decreases.
        \n """,
        """47  I. For current amplification II. For voltage stabilization III. For power amplification IV. As a switch.\n Which of the above are the uses of a transistor?
         I, II, III and IV
          I, III and IV only
          I, II and III only
          I, II and IV only.
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "A"),
        Question(question_prompts[44], "A"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "B"),
        Question(question_prompts[47], "A"),

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
        Physics_2009()
def Physics_2008():
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
        """1. A man walks 1 km due east and then 1km due north. His displacement is _____
A. √2   N 45° E
B. 1km N 30°E
C. 1km N 15° E
D. D.√2 km N 60° E
\n """,
"""2. The density of 400cm of palm oil was 0.9g before frying. If the density of the oil was 0.6 after frying, assuming\n no loss of oil to spilling, its new volume was 
A. 360  3
B. 600  3
C. 240  3
D. 800  3
\n """,
"""3. Which of the following is true of an electrical charge?
A. Positive charge means deficit electrons 
B. Negative charge means excess  of electrons 
C. Electric current means movement of electrons
D. All of the above
\n """,
"""4. Natural radioactivity consists of the emission of -------.
A. ∝-particles and β-rays
B. ∝-particles and X-rays
C. ∝-particles, β-rays and g-rays
D. γ-rays and X-rays
\n """,
"""5. Which of the following does NOT describe the image formed by a plane mirror?
A. Erect
B. Laterally inverted
C. Same distance from mirror asobject
D. Magnified
\n """,
"""6. What is the resultant resistance of the circuit given above?
A. 8Ω
B. 11Ω
C. 4Ω
D. 3.6Ω
\n """,
"""7. Which of the following best describes the energy changes which take place when a steam engine drives a generator\n which lights a lamp?
A. Heat → Light → Sound→ Kinetic
B. Heat→ Kinetic → Electricity→ Heat and Light
C. Kinetic→ Light → Heat →Electricity
D. Electricity →Kinetic→ Heat→ Light
\n """,
"""8. Cathode rays are ______
A. High-energy electromagnetic waves
B. protons
C. neutrons 
D. streams of electrons
\n """,
"""9. A narrow beam of white light can be split into different colours by a glass prism. The correct explanation is that
A. white light is an electromagnetic wave
B. the prism has all the colours of the white light
C. different colours of white light travel with different speeds in glass
D. white light has undergone total internal reflection in the prism.
\n """,
"""10. Figure 2 represents a block- and- tackle pulley system on which an effort of W Newtons supports a  load of 120.0N.\n If the efficiency of the machine is 40, then the value of W is
A. 28.0 N
B. 48.0 N
C. 288.0 N
D. 50.0 N
\n """,
"""11. The amount of heat needed to raise the temperature of 10kg of copper by 1K its ____
A. specific heat capacity
B. latent heat
C. heat capacity
D. internal energy
\n """,
"""12. The electrochemical equivalent of silver 0.0012g/C/ of 36.0g of silver is to be deposited by electrolysis on a\n surface by passing a steady current for 5.0 minutes, the current must be
A. 6000A
B. 100A
C. 10A
D. 1A
\n """,
"""13. Shadows and eclipses result from the
A. refraction of light
B. reflection of light.
C. defraction of light
D. rectilinear propagation of light
\n """,
"""14. Which of the following obeys Ohm’s Law?
A. All metals
B. Diode only
C. All electrolytes
D. Glass
\n """,
"""15. Which of the following statements are TRUE OF ISOTOPES? I. Isotopes of an element have the same chemical\n properties because they have the same number of electrons II. Isotopes of elements are normally separated using physical properties III. Isotopes of an element has the same number of protons in their nuclei.
A. I and II only
B. I and III only
C. II and III only
D. I, II and III.
\n """,
"""16. Which of the following may be used to explain a mirage? I. Layers of air near the road surface have varying \nrefractive indices in hot weather II. Road surfaces sometimes become good reflectors in hot weather. III. Light from the sky can be reflected upwards after coming close to and the road surface.
A. I and III only
B. II and III only
C. II only
D. I, II and III
\n """,
"""17. In the diagram below, if the atmosphere pressure is 760mm, the pressure in the chamber G is 
A. 660mm 
B. 830mm
C. 690mm
D. 860mm
\n """,
"""18 Which of the following has the lowest internal resistance when new?
A. Leclanche cell
B. Daniel cell
C. Torch battery
D. Accumulator
\n """,
"""19 The pitch of an acoustic  device can be increased by
A. decreasing the loudness
B. increasing the amplitude 
C. increasing the frequency
D. decreasing the intensity.
\n """,
"""20 One of the features of the fission process is that 
A. it leads to chain reaction
B. its products are not radioactive
C. neutrons are not released.
D. the sum of the masses of the reactants equals the sum of the masses of the products.
\n """,
"""21 A lead bullet of mass 0.05kg is fired with a velocity of 200  
into a lead block of mass 0.95kg.  Given that the lead block can 
move freely, the final kinetic energy after impact is
A. 150 J
B. 100 J
C. 50 J
D. 200 J
\n """,
"""22 In a series R-L-C circuit at resonance, the voltages across the resistor and the inductor are 20V and 40V \nrespectively. What is the voltage across the capacitor?
A. 30 V
B. 70 V
C. 50 V
D. 40 V
\n """,
"""23 If the fraction of the atoms of a radioactive material left after 120 years is 1/64, what is the half-life of \nthe material?
A. 20 years
B. 10 years
C. 2 years
D. 24 years
\n """,
"""24 The time rate of loss of heat by a body is proportional to the
A. temperature of its surroundings
B. temperature of the body
C. difference in temperature between the body and its surroundings
D. ration of the temperature of the boy to that of its surroundings.
\n """,
"""25 A positive charged rod X is brought near an uncharged metal sphere Y and is then touched by a finger with X still\n in place. When the finger is removed, the result is that Y has
A. no charge and a zero potential
B. a positive charge and a zero potential.
C. a negative charge and a positive potential.
D. a negative charge and a negative potential.
\n """,
"""26 Electrical appliances in homes are normally earthed so that
A. a person touching the appliances is safe from electric shock.
B. both the a.c. and d.c. sources can be used. 
C. the appliances are maintained at a higher p.d. than the earth.
D. the appliances are maintained at a lower p.d. than the earth.
\n """,
"""27 The process whereby a liquid turns spontaneously into vapour is called
A. regelation 
B. evaporation.
C. boiling.
D. sublimation.
\n """,
"""28 The differences observed in solids, liquids and gases may be accounted for by
A. their relative masses.
B. their melting points.
C. the spacing and forces acting between the molecules.
D. the different molecules in each of them.
\n """,
"""29 Convex mirrors are used as driving mirrors because images formed are
A. erect, virtual and diminished
B. erect, real and diminished
C. erect, virtual and magnified
D. inverted, virtual and diminished.
\n """,
"""30 Musical instruments playing the same note can be distinguished from one another owing to the differences in their
A. quality.
B. pitch.
C. intensity
D. loudness
\n """,
"""31 In homes, electrical appliances and lamps are connected in parallel because
A. less current will be used
B. less voltage will be used.
C. parallel connection does not heat up the wires
D. series connection uses high voltage
\n """,
"""32 An object moves in a circular path of radius 0.5m with a speed of 1m −1. What is its angular velocity?
8rads-1
4rads-1
1rads-1
2rads-1
\n """,
"""33 What effort will a machine of efficiency 90% apply to lift a load of 180N if its efforts arm is twice  as long\n as its load arm? 
A. 100N 
B. 90N
C. 80N
D. 120N
\n """,
"""34 Calculate the effective  capacitance of the circuit above.
A. 4μf
B. 3 μf
C. 2 μf
D. 1 μf.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "A"),
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
        Physics_2008()