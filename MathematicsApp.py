from  Question import Question
def  math_jamb_2010():
   question_prompt=[
       '''[1]There are 8 green balls, 4 blue balls and 3 white balls in a box. Then 1 green and 1 blue balls are taken from the box and put aw ay. W hat is the probability that a blue ball is selected at random from the box?
       (a)3/13
       (b)2/13  
       (c)3/15
       (d)4/15\n''',
       '''[2]Find r, if 7r7base8=618base9 
       (a)3 
       (b)2  
       (c)6  
       (d)5\n''',
       '''[3] Simplify (3/4  of 4/9 ÷ 9 1/2)  ÷1 5/19  
       (a)1/5 
       (b)1/4
       (c)1/36
       (d)1/25\n''',
       '''[4] A student measures a πce of rope and found it was 1.27m long. If the actual length of the rope was 1.25m , what was the percentage error in the measurement?
       (a)1.6%
       (b)1.0%
       (c)0.8%
       (d)0.16%\n''',
       '''[5] At what rate will the interest on N500 increase to N25 in 5 years reckoning in simple interest?
       (a)2%
       (b)1%
       (c)4%
       (d)5%\n''',
       '''[6] If p : q = 2/3 : 1/6 and q : r =3/(4) : 1/2 find p : q : r 
       (a)12 : 3 : 2
       (b)12 : 15 : 4
       (c)9 : 10 : 15
       (d)9 : 12 : 15\n''',
       '''[7] Given that log⁡2 = 0.3010 and log⁡7 = 0.8451 Evaluate log⁡224
        (a)2.1461
        (b)2.3501 
        (c)2.0491 
        (d)3.1461\n''',
       '''[8] Rationalize 2√5 + √7 ÷√7 - √5
       (a)3√35 - √17 / 2
       (b)3√35 + √17
       (c)3√35 - √17
       (d)3√35 + √17/2 \n''',
       '''[9] In a survey of 60 newspaper readers, 49 read Nation and 30 read Punch , how many read both papers?
       (a)10  
       (b)5 
       (c)20  
       (d)15\n''',
       '''[10] If  9x^2+6xy+4y2 is a factor of 27x3-8y3 , find the other factor
       (a)2y - 3x
       (b)2y + 3x
       (c)-2y- 3x
       (d)-2x + 3x\n''',
       '''[11] Solve for x and y if x -y= 3 and x2 - y2 
       (a)(-3, 0)
       (b)(0, -3)
       (c)(3, 0)
       (d)(0, 3)\n''',
       '''[12] If y varies directly as the square root of x and y= 3 when x = 25 . Calculate when x =100.
       (a)12 
       (b)3 
       (c)5 
       (d)6\n''',
       '''[13] If x is inversely proportional to y and x= 3 1/2 when y= 2, find x if y= 4.
       (a)1 1/4
       (b)2 3/4
       (c)1 3/4
       (d)2 1/4\n''',
       '''[14] The 3rd term of an arithmetic progression is -8 and the 7 th term is -28. Find the 10th term of the progression.
       (a)-43 
       (b)-164 
       (c)164 
       (d)44\n''',
       '''[15] If p and q are two nonzero numbers and 16(p + q)= ( 16 +p )/q , which of the following must be true.
       (a)p< 1 
       (b)p=16 
       (c)q<1 
       (d)q=16\n''',
       '''[16] A rectangular picture 6cm by 8cm is enclosed by a frame (1/ 2) wide. Calculate the area of the frame.
       (a)15 sq cm
       (b)20 sq cm 
       (c)13 sq cm 
       (d)17 sq cm\n''',
       '''[17] Five years ago, a father was 3 times as old as his son. Now, their combined ages amount to 110 years. Thus, the present age of the father is
       (a)75 years 
       (b)60 years 
       (c)98 years 
       (d)81 years\n''',
       '''[18] Mother reduced the quantity of food bought for the family by when she found that the cost of living had increased by . Thus the fractional increase in the family food bill is now
       (a)1/12 
       (b)6/35 
       (c)19/300 
       (d)7/200\n''',
       '''[19] A man runs a distance of 9km/h for the first 4km and then 2km/h for the rest of the distance. The whole run takes him one hour. His average speed for the first 4km is
       (a)6 km/h  
       (b)8km/h 
       (c)9 km/h 
       (d)11 km/h\n''',
       '''[20] In a circle of radius 10 cm , a chord of length 10 cm is xcm from its centre. What is x.
       (a)10√2 
       (b)5√3
       (c)10√3
       (d)5√2\n''',
       '''[21] The smallest number such that when it is divided by 8 has a remainder of 6 and when it is divided by 9 has a remainder of 7 is
        (a)50 
        (b)70
        (c)80 
        (d)60\n''',
       '''[22] When a dealer sells a bicycle for N 81 he makes a profit of 8% . What did he pay for the bicycle ? 
       (a)N74.52 
       (b)N75
       (c)N75.52
       (d)N74\n''',
       '''[23] If M represents the median and D the mode of the measurements 5, 9, 3, 5, 8 then (M,D) is
       (a)(6, 5)
       (b)(5, 8)
       (c)(5, 7)
       (d)(5, 5)\n''',
       '''[24] A construction company is owned by two partners X and Y and it is agreed that their profit will be divided in the ratio 4:5. at the end of the year. Y received #5,000 more than x. what is the total profit of the company for the year?
       (a)#20,000.00
       (b)#30,000.00
       (c)#15,000.00
       (d)#45,000.00\n''',
       '''[25] Given a regular hexagon, calculate each interior angle of the hexagon.
       (a)60°
       (b)30°
       (c)120°
       (d)45°\n''',
       '''[26] Solve the following equations 4x – 3 = 3x + y = 2y + 5x – 12
       (a)x = 5, y = 2
       (b)x = 2, y =5
       (c)x = -2, y =-5
       (d)x = 5, y =-2\n''',
       '''[27] If x = 1 is root of the equation x3 – 2x2 – 5x + 6, find the other roots
       (a)-3 and 2
       (b)–2 and 2
       (c)3 and –2
       (d)1 and 3\n''',
       '''[28] If x is jointly proportional to the cube of y and the fourth power of z. In what ratio is x increased or decreased when y is halved and z is doubled?
       (a)4 : 1 increase 
       (b)2 : 1 increase
       (c)1 : 4 decrease
       (d)1 : 1 nochange\n''',
       '''[29] If x + 2 and x – 1 are factors of the expressions lx + 2kx^2 + 24, find the values of l and k
       (a)l = -6, k = -9
       (b)l = -2, k = 1
       (c)l = -2, k = -1
       (d)l = 0, k = 1\n''',
       '''[30] The value of (0.303)^3 – (0.02)^3 is
       (a)0.019
       (b)0.0019
       (c)0.00019
       (d)0.000019\n''',
       '''[31] Simplify (x – 7) / (x^2– 9) multiply  (x^2 – 3x) / ( x^2 - 49)
       (a)x/(x-3)(x+7)
       (b)(x+3)(x+7)/x 
       (c)x/(x-3)(x -7)
       (d)x/(x+3)(x+7)\n''',
       '''[32] The lengths of the sides of a right-angled triangle at (3x + 1)cm, (3x - 1)cm and x cm.
       (a)2
       (b)6
       (c)18
       (d)12\n''',
       '''[33] The scores of a set of a final year students in the first semester examination in a paper are 41,29,55,21,47,70,70,40,43,56,73,23,50,50. find the median of the scores.
       (a)47
       (b)48 whole number 1/2
       (c)50
       (d)48\n''',
       '''[34] Find x if (x base 4)^2  = 1001000 base2
       (a)6
       (b)12
       (c)100
       (d)210\n''',
       '''[35] If w varies inversely as V and u varies directly as w3, find the relationship between u and V given that u = 1, when V = 2
       (a)u=8V3 
       (b)V=8/u2
       (c)V=8u2
       (d)U= 8/v3\n''',
       '''[36] [Solve the simultaneous equations for x.] x2 + y – 8 = 0,  y + 5x – 2 = 0
       (a)–28, 7
       (b)6, -28
       (c)0, 5
       (d)6, -1\n''',
       '''[37] Find the angle of the sectors representing each item in a π chart of the following data. 6, 10, 14, 16, 26
       (a)15°, 25°, 35°, 40°, 65°
       (b)60°, 100°, 140°, 160°, 260°
       (c)6°, 10°, 14°, 16°, 26°
       (d)30°, 50°, 70°, 80°, 130°\n''',
       '''[38] The scores of 16 students in a Mathematics test are 65, 65, 55, 60, 60, 65, 60, 70, 75, 70, 65, 70, 60, 65, 65, 70 What is the sum of the median and modal scores?
       (a)125
       (b)130
       (c)140
       (d)150\n''',
       '''[39] The letters of the word MATRICULATION are cut and put into a box. One of the letter is drawn at random from the box. Find the probability of drawing a vowel.
       (a)2/13
       (b)5/13
       (c)6/13
       (d)8/13\n''',
       '''[40] Correct each of the number 59.81789 and 0.0746829 to three significant figures and multiply them, giving your answer to three significant figures.
       (a)4.46
       (b)4.48
       (c)4.47
       (d)4.49\n'''
   ]
   question=[
        Question(question_prompt[0],'b'),
       Question(question_prompt[1],'c'),
        Question(question_prompt[2], 'c'),
        Question(question_prompt[3],'a'),
        Question(question_prompt[4], 'b'),
        Question(question_prompt[5], 'a'),
        Question(question_prompt[6], 'b'),
        Question(question_prompt[7], 'a'),
       Question(question_prompt[8], 'a'),
       Question(question_prompt[9], 'c'),
       Question(question_prompt[10], 'a'),
       Question(question_prompt[11], 'd'),
       Question(question_prompt[12], 'c'),
       Question(question_prompt[13], 'a'),
       Question(question_prompt[14], 'd'),
       Question(question_prompt[15], 'a'),
       Question(question_prompt[16], 'a'),
       Question(question_prompt[17], 'd'),
       Question(question_prompt[18], 'b'),
       Question(question_prompt[19], 'b'),
       Question(question_prompt[20], 'b'),
       Question(question_prompt[21], 'b'),
       Question(question_prompt[22],'a'),
       Question(question_prompt[23], 'd'),
       Question(question_prompt[24], 'c'),
       Question(question_prompt[25], 'a'),
       Question(question_prompt[26], 'c'),
       Question(question_prompt[27], 'b'),
       Question(question_prompt[28], 'a'),
       Question(question_prompt[29], 'd'),
       Question(question_prompt[30], 'd'),
       Question(question_prompt[31],'d'),
       Question(question_prompt[32],'b'),
       Question(question_prompt[33],'b'),
       Question(question_prompt[34],'d'),
       Question(question_prompt[35],'d'),
       Question(question_prompt[36],'d'),
       Question(question_prompt[37],'b'),
       Question(question_prompt[38],'c'),
       Question(question_prompt[39],'b')
   ]
   def run_test(questions):
        des={}
        nam=input('type your name here: ')
        score = 0
        option=['a','b','c','d']
        for question in questions:
            answer = input(question.prompt).lower()
            if answer == question.answer :
                score += 2
                print('\ngood job,you got the answer❤👍\n')
            elif answer not in option:
                   print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
            else:
                print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
        des.update({nam:(str(score)+'/'+str(len(questions)*2))})
        print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,10),'%')
        if score >= 40:
            print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
        else:
            print("\nyou failed the test,go and read your book and try again😭☹👎\n")
   run_test(question)
def math_jamb_2011():
    question_prompt=[
        '''[1] If a rod of length 250cm is measured as 255cm longer in error, what is the percentage error in measurement?
        (a)55
        (b)10
        (c)5
        (d)2\n''',
        '''[2] If (2/3)m x  (3/4)n = 256/729, find the values of m and n
        (a)m = 4, n = 2
        (b)m = -4, n =- 2
        (c)m = -4, n = 2
        (d)m = 4, n =- 2\n''',
        '''[4] Factorize completely 81a^4 – 16b^4
        (a)(3a + 2b) (2a – 3b) (9a2 + 4b2)
        (b)(3a - 2b) (2a – 3b) (4a2 - 9b2)
        (c)(3a - 2b) (3a – 2b) (9a2 + 4b2)
        (d)(3a - 2b) (2a – 3b) (9a2 + 4b2)\n''',
        '''[5] One interior angle of a convex hexagon is 170° and each of the remaining interior angles is equal to x°. find x
        (a)120°
        (b)110°
        (c)105°
        (d)102°\n''',
        '''[6] PQRS is a cyclic quadrilateral in which PQ = PS. PT is a tangent to the circle and PQ makes and angle 50° with the tangent as shown in the figure below. What is the size of QRS?
        (a)50°
        (b)40°
        (c)110°
        (d)100°\n''',
        '''[7] A ship H leaves a port P and sails 30km due South. Then it sails 60km due west.What is the bearing of H from P?
        (a)26° 34’
        (b)243° 26’
        (c)116° 34’
        (d)63° 26’\n''',
        '''[8] On a square paper of length 2.524375cm is inscribed a square diagram of length 0.524375. find the area of the paper no covered by the diagramcorrect to 3 significant figures.
        (a)6.00cm2
        (b)6.10cm2
        (c)6.cm2
        (d)6.09cm2\n''',
        '''[9] If f(X) = 1/x-1 + x - 1/ x2-1 find f(1-x)
        (a)1/x + 1/(x+2)
        (b)x +1/(2x -1)
        (c)-1/x - 1/(x-2)
        (d)-1/x + 1/(x2-1)\n''',
        '''[10] PQR is the diameter of a semicircle RSP with centre at Qand radius of length 3.5cm. If QPT= QRT = 60°. Find the perimeter of the figure (PTRS) π = 22/7
        (a)25cm
        (b)18ccm 
        (c)36cm
        (d)29cm\n''',
        '''[10] PQR is the diameter of a semicircle RSP with centre at Qand radius of length 3.5cm. If QPT= QRT = 60°. Find the perimeter of the figure (PTRS) π = 22/7
        (a)25cm
        (b)18ccm 
        (c)36cm
        (d)29cm\n''',
        '''[11] In a triangle PQR, QR= 3cm, PR= 3cm, PQ= 3cm and PQR = 30°. find angles P and R
        (a)P = 60° and R = 90°
        (b)P = 30° and R = 120°
        (c)P = 90° and R = 60°
        (d)P = 60° and R = 60°\n''',
        '''[12] Find the mean of the following 24.57, 25.63, 25.32, 26.01, 25.77
        (a)25.12
        (b)25.30
        (c)25.26
        (d)25.50\n''',
        '''[13] A man drove for 4hours at a certain speed, he then doubled his speed and drove for another 3 hours. Altogether he covered 600km. At what speed did he drive for the last 3 hours?
        (a)120km/hr
        (b)60km/hr
        (c)600/7km/hr
        (d)50km/hr\n''',
        '''[14] (0.00014323) / (1.940000) = k x 10n where 1 £ k < 10 and n is a whole number. The values of K and are
        (a)7.381 and –11
        (b)2.34 and 10
        (c)3.87 and 2
        (d)7.831 and –11\n''',
        '''[15] P sold his bicycle to Q at a profit of 10%. Q sold it to R for #209 at a loss of 5%. How much did the bicycle cost P?
        (a)#200 
        (b)#196
        (c)#180
        (d)#220 \n''',
        '''[16] If the price of oranges was raised by 1/2k per orange, the number of oranges customer can buy for #2.40 will be less by 16. What is the present price of an orange?
        (a)2 whole number 1/2k
        (b)3 whole number 1/2k
        (c)5 whole number 1/2k
        (d)20k \n''',
        '''[17] A man invested a total of #50,000 in two companies. If these companies pay dividend of 6% and 8% respectively, how much did he invest at 8% if the total yield is #3.700?
        (a)#15,000
        (b)#29,600
        (c)#21,400
        (d)#35,000\n''',
        '''[18] Thirty boys and x girls sat for a test. The mean of the boys’ scores and that of the girls were respectively 6 and 8. find x if the total score was 468.
        (a)38
        (b)24
        (c)36
        (d)22 \n''',
        '''[19] The cost of production of an article is made up as follows Labour #70 , Power #15 , Materials #30, Miscellaneous #5 Find the angle of the sector representing labour in a pie chart.
        (a)210°
        (b)105°
        (c)175°
        (d)150°\n''',
        '''[20] Bola chooses at random a number between 1 and 300. What is the probability that the number is divisible by 4?
        (a)1/3
        (b)¼ 
        (c)1/5
        (d)4/300\n''',
        '''[21] Find without using logarithm tables, the value of (Log27 in base 3)  – (Log64 in base 1/4) / (Log 1/81 in base3)
        (a)7/4
        (b)–7/4
        (c)–3/2
        (d)7/3\n''',
        '''[21] Find without using logarithm tables, the value of (Log27 in base 3)  – (Log64 in base 1/4) / (Log 1/81 in base3)
        (a)7/4
        (b)–7/4
        (c)–3/2
        (d)7/3\n''',
        '''[22] A variable point P(x, y) traces a graph in a two dimensional plane. (0, -3) is one position of P. If x increases by 1 unit, y increases by 4 units. The equation of the graph is
        (a)-3 = y+ 4/ x + 1
        (b)4y= -3 + x
        (c)y/x = -3/4
        (d)y+ 3 = 4x\n''',
        '''[23] A trader in a country where their currency ‘MONT’ (M) is in base five bought 103 in base (5) oranges at M14 in base (5) each. If he sold the oranges at M24 in base (5) each, what will be his gain?
        (a)M103 in base (5)
        (b)M1030 in base(5)
        (c)M102 in base(5)
        (d)M2002 in base(5)\n''',
        '''[24] Simplify (3^n – 3^(n – 1)) / (3^3 x 3^(n – 27) x 3^(n – 1))
        (a)1
        (b)0
        (c)1/27
        (d)3n – 3n – 1\n''',
        '''(25)p varies directly as the square of q an inversely as r. if p = 36, when q = 3 and r = p, find pwhen q = 5 and r = 2
        (a)72
        (b)100
        (c)90
        (d)200\n''',
        '''[26] Factorise 6x^2 – 14x - 12
        (a)2(x +3) (3x - 2)
        (b)6(x - 2) (x +1)
        (c)2(x - 3) (3x +2)
        (d)6(x+ 2) (x - 1)\n''',
        '''[27] A straight line y=mx meets the curve y = x2 – 12x + 40 in two distinct points. If one of them is (5, 5), find the other
        (a)(5, 6)
        (b)(8, 8)
        (c)(8, 5)
        (d)(7, 5)\n''',
        '''[28] The table below is drawn for a graph y = x2 – 3x + 1 From x = -2 to x = 1, the graph crosses the x-axis in the range(s)
        (a)-1 < x < 0 and 0 < x < 1
        (b)-2 < x < -1 and 0< x < 1
        (c)-2 < x < -1 and 0< x < -1
        (d)0< x <1  and 1< x < 2\n''',
        '''[29] In a racing competition.Musa covered a distance of 5xkm in the first hour and (x + 10)kmin the next hour. He was second toNgozi who covered a total distance of 118km in the two hours.Which of the following inequalities is correct?
        (a)0 < -x < 15
        (b)–3 < x < 3
        (c)15 <x < 18
        (d)0 < x < 18\n''',
        '''[30] 2x + 3y = 1 and y = x – 2y = 11, find (x + y)
        (a)5
        (b)–3
        (c)8
        (d)2\n''',
        '''[31] Tunde and Shola can do a πce of work in 18days. Tunde can do it alone in x days, whilst Shola takes 15 days longer to do it alone. Which of the following equations is satisfied by x?
        (a)x^2 – 5x – 18 = 0
        (b)x^2 – 20x + 360 = 0
        (c)x^2 - 21x–270 = 0
        (d)2x^2 + 42x – 190 = 0\n''',
        '''[32] If f(x) = 2(x - 3)2 + 3(x - 3) – 4 and g(y)= Ö5 + y, find g(f(3)) and g{f(4)}
        (a)3 and 4
        (b)–3 and 4
        (c)–3 and –4
        (d)3 and –4\n''',
        '''[33] Find a factor which is common to all three binomial expressions 4a^2 – 9b^2,  a^3 + 27b^3,  (4a + 6b)^2
        (a)4a + 6b
        (b)4a – 6b
        (c)2a + 3b
        (d)2a – 3b\n''',
        '''[34] If (x - 2) and (x + 1) are factors of the expression x3 + px2 + qx + 1, what is the sum of p and q?
        (a)0 
        (b)–3
        (c)3
        (d)–17/3\n''',
        '''[35] A cone is formed by bending a sector of a circle having an angle of 2100. Find the radius of the base of the cone if the diameter of the circle is base of the cone if the diameter of the circle is 12cm
        (a)7.00cm
        (b)1.75cm
        (c)21cm
        (d)3.50cm\n''',
        '''[36] The sides of a triangle are (x + 4)cm, x cmand (x- 4) cm respectively. If the cosine of the largest angle is 1/5, find the value of x
        (a)24cm
        (b)20cm
        (c)28cm
        (d)88/7ccm\n''',
        '''[37] If a = 2x/1 – x and b= 1 + x / 1 – x then a2 – b2 in the simplest form is
        (a)3x+1/(x-1)
        (b)3x2-1/(x-1)2
        (c)3x2+1/(1-x)2
        (d)5x2-1/(1-x)2\n''',
        '''[38] Find the integral values of x which satisfy the inequalities –3 < 2 –5x < 12
        (a)-2, -1
        (b)–2, 2
        (c)–1, 0
        (d)0,1\n''',
        '''[39] In the figure above QRS is a line, PSQ = 35° SPR = 30° and O is the centre of the circle find OQP
        (a)35°
        (b)30°
        (c)130°
        (d)25°\n''',
        '''[40] If pq + 1 = q2 and t = 1/p – 1/pq express t in terms of q
        (a)1/p – q
        (b)1/ q – 1
        (c)1/q + 1
        (c)1 + q
        1/q + 1\n'''
    ]
    question=[
          Question(question_prompt[0],'d') ,
          Question(question_prompt[1],'d') ,
          Question(question_prompt[2],'a') ,
          Question(question_prompt[3],'c') ,
          Question(question_prompt[4],'b') ,
          Question(question_prompt[5],'d') ,
          Question(question_prompt[6],'d') ,
          Question(question_prompt[7],'b') ,
          Question(question_prompt[8],'a') ,
          Question(question_prompt[9],'a') ,
          Question(question_prompt[10],'a'),
          Question(question_prompt[11],'c')  ,
          Question(question_prompt[12],'b')  ,
          Question(question_prompt[13],'d')  ,
          Question(question_prompt[14],'a')  ,
          Question(question_prompt[15],'a')  ,
          Question(question_prompt[16],'d')  ,
          Question(question_prompt[17],'c')  ,
          Question(question_prompt[18],'a')  ,
          Question(question_prompt[19],'b')  ,
          Question(question_prompt[20],'c')  ,
          Question(question_prompt[21],'d') ,
          Question(question_prompt[22],'b') ,
          Question(question_prompt[23],'c') ,
          Question(question_prompt[24],'d') ,
           Question(question_prompt[25],'c') ,
           Question(question_prompt[26],'d') ,
          Question(question_prompt[27],'b') ,
          Question(question_prompt[28],'d') ,
          Question(question_prompt[29],'d') ,
          Question(question_prompt[30],'c'),
          Question(question_prompt[31],'a')  ,
          Question(question_prompt[32],'c')  ,
          Question(question_prompt[33],'b')  ,
          Question(question_prompt[34],'d')  ,
          Question(question_prompt[35],'a')  ,
          Question(question_prompt[36],'a')  ,
          Question(question_prompt[37],'d')  ,
          Question(question_prompt[38],'d')  ,
          Question(question_prompt[39],'c')  ,
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2014():
    question_prompt=[
                """0 Find the least length of a rod which can be cut into exactly equal strips, each of either\n 40cm or 48cm in length.
            120cm
            240ccm
            360cm
            480cm
            \n""",
            """1 A rectangular has lawn has an area of 1815 square yards. If its length is 50 meters, find its\n width in metres. Given that 1 meters equals 1.1 yards
            39.93
            35.00
            33.00
            30.00
            \n""",
            """2 Reduce each number to two significant figures and then evaluate (0.02174 x 1.2047) / 0.023789
            0.8
            0.9
            1.1
            1.2
            \n""",
            """3 A train moves from P to Q at an average speed of 90km/hr and immediately returns from O to P \nthrough the same route and at an average speed of 45km/h. find the average speed for the centre journey.
            5500km/hr
            6000km/hr
            67.50km/hr
            7500km/hr
            \n""",
            """4 If the length of a square is increased by 20% while its width is decreased by20% to form a rectangle,\n what is the ratio of the area of the rectangle to the area of the square?
            6.5
            25.24
            5.6
            24.25
            \n""",
            """5 Two brothers invested a total of #5,000.00 on a farm project. The farm yield was sold for\n # 15, 000.00 at the end of the season. If the profit was shared in the ratio 2:3, what is the difference in the amount of profit received by the brothers?
            #2,000.00
            #4,000.00
            #6,000.00
            #10,000.00
            \n""",
            """6 A man invests a sumofmoney at 4% per annum simple interest. After 3 years, the principal\n amounts to #7,000.00. find the sum invested
            #7,840.00
            #6,250.00
            #6,160.00
            #5,833.33
            \n""",
            """7 By selling 20 oranges for #1.35 a trader makes a profit 8%. What is his percentage gain or loss\n if he sells the same 20 oranges for #1.10?
            8%
            10%
            12%
            15%
            \n""",
            """8 Four boys and ten girls can cut a field in 5 hours. If the boys work at 1/4 the rate of which \nthe girls work, how many boys will be needed to cut the field in 3 hours?
            180
            60
            25
            20
            \n""",
            """9 Simplifywithout using tables (Log6₂– Log3₂) / ((Log8₂) - (2Log1/2₂))
            1/5
            ½
            –1/2 
            Log23/Log27
            \n""",
            """10 The formula Q = 15 + 0 5n gives the cost Q (in Naira) of feeding n people for a week. Find in\n kobo the extra cost of feeding one additional person.
            350k
            200k
            150k
            50k
            \n""",
            """11 If P varies inversely as V and V varies directly as R², find the relationship between P and R \ngiven that R = 7 when P = 2
            P = 98R²
            PR2 = 98
            P = 1/98R
            P = R²/98
            \n""",
            """12 Find two values of y which satisfy the simultaneous equations x + y = 5,  x² – 2y² = 1
            12, -2
            –12, 12
            12, 2
            2, -2
            \n""",
            """13 An (n - 2)² sided figure has n diagonals find the number n of diagonals for a 25 sided figure
            7
            8
            9
            10
            \n""",
            """14 A cubic function f(x) is specified by the graph show above. The values of the independent\n variable for which the function vanishes are
            -1, 0, 1 
            –1 < x < 1
            x, - 1
            x > 1
            \n""",
            """15 Solve the inequality x – 1 > 4(x + 2)
            x> -3
            x< -3
            2< x <3
            –3 < x < -2
            \n""",
            """16 The minimum value of y in the equation y = x² – 6x + 8 is
            8
            3
            0
            –1
            \n""",
            """17 Find the sum of the first 21 terms of the progression –10,  -8,  -6,….
            180
            190
            200
            210
            \n""",
            """18 Find the eleventh term of the progression 4, 8, 16,..
            2^13
            2^12
            2^11
            2^10
            \n""",
            """19 QR//TS, QR :TS = 2 : 3.  find the ratio of the area of triangle PQR to the area of the trapezium QRST
            4 : 9
            4 : 5
            1 : 3
            2 : 3
            \n""",
            """20 XYZ = YTZ = 90°, XT = 9cm and TZ = 16cm. Find YZ
            25cm
            20cm
            16cm
            9cm
            \n""",
            """21 Two chords QR and NP of a circle intersect inside the circle at X. if RQP = 370,  RQN = 49⁰ \nand QPN = 35⁰,  find PRQ
            35°
            37°
            49°
            59°
            \n""",
            """22 PQRS is a rectangle. If the shaded area is 72 cm²  find h
            12cm
            10cm
            8cm
            5cm
            \n""",
            """23 The sine, cosine and tangent of 210° are respectively
            -1/2, 3/2, 3/3
            1/2, 3/2 3/3
            3/2, 3/3, 1
            3/2, 1/2, 1
            \n""",
            """24 From two points X and Y, 8m apart, and in line with a pole, the angle of elevation of the top of\n the pole are 30⁰ and 60° respectively. Find the height of the pole, assuming that X, Y and the foot of the pole are on the same horizontal plane.
            4m
            8√3/2m
            4√3m
            8√3m
            \n""",
            """25 A room is 12m long. 9m wide and 8m high. Find the cosine of the angle which a diagonal of the\n roommakes with the floor of the room
            15/17
            8/17
            8/15
            12/17
            \n""",
            """26. What is the circumference of latitude 0° South if R is the radius of the earth?
            Rcosq
            2πRcos q
            Rsinq
            2πRsinq
            \n""",
            """27 The base of a pyramid is a square of side 8cm. If its vertex is directly above the centre,\n find the height, given that the edge is 4.3cm
            6cm
            5cm
            4cm
            3cm
            \n""",
            """28 What is the locus of the mid-points of all chords of length 6cm within a circle of radius 5cmand\n with centre O.
            A circle of radius 4cm and with centre O
            The perpendicular bisector of the chords
            A straight line passing through center O
            A circle of radius 6cm and with centre O
            \n""",
            """29 Taking the period of daylight on a certain day to be from 5.30a.mto 7.00p.m, calculate the period\n of daylight and of darkness on that day
            187°30 172°30
            135°225
            202°30 157°30
            195°165
            \n""",
            """30 The numbers 3, 2, 8, 5, 7, 12, 9 and 14 are themarks scored by a group by a group of students\n in a class test if P is the mean and Q the median the P + Q is
            18
            17½
            16
            15
            \n""",
            """31 Find the probability of selecting a figure which is parallelogram from a square,\n a rectangle, a rhombus, a kite and a trapezium
            3/5
            2/5
            4/5
            1/5
            \n""",
            """32 If x is the addition of the prime numbers between 1 and 6, and y the H. C.F of 6, 9, 15, \nfind the product of x and y
            27
            30
            33
            90
            \n""",
            """33 A 5.0g of salts was weighed by Tunde as 5.1g. what is the percentage error?
            20
            2
            1.1
            0.2
            \n""",
            """34 Find correct to one decimal place, 0.24633 /0.0306
            0.8
            1.8
            8.0
            8.1
            \n""",
            """35 Two sisters, Taiwo and Kehinde, own a store. The ratio of Taiwo’s share to Kehind’s is 11:9.\n later Kehinde sells 2/3 of her share to Taiwo for #720.00. Find the value of the store.
            #1,080.00
            #2,400.00
            #3,000.00
            #3,600.00
            \n""",
            """36 A basket contains green, black and blue balls in the ratio 5: 2: 1. if there are 10 blue balls,\n find the corresponding new ratio when 10 green and 10 black balls are removed from the basket.
            1 : 1 : 1
            4 : 2 : 1
            5 : 1 : 1
            4 : 1 : 1
            \n""",
            """37 A taxpayer is allowed 1/8th of his income tax free, and pays 20% on the remainder. If he pays\n #490. 00 tax, what is his income?
            #560.00
            #2,450.00
            #2,800.00
            #3,920.00
            \n""",
            """38 Evaluate (8^⅓ x (5^(2/3)) / 10^(2/3))
            2/5
            5/3
            2√5
            3√5
            \n""",
            """39 If Log102 = 0.3010 and Log103 = 0.4771, evaluate, without using logarithm tables log104.5
            0.3010
            0.4771
            0.6532
            0.9542
            \n""",
    ]
    question=[
          	  Question(question_prompt[0],'b') ,
          Question(question_prompt[1],'c') ,
          Question(question_prompt[2],'c') ,
          Question(question_prompt[3],'c') ,
          Question(question_prompt[4],'b') ,
          Question(question_prompt[5],'a') ,
          Question(question_prompt[6],'b') ,
          Question(question_prompt[7],'c') ,
          Question(question_prompt[8],'d') ,
          Question(question_prompt[9],'a') ,
          Question(question_prompt[10],'b'),
          Question(question_prompt[11],'b')  ,
          Question(question_prompt[12],'c')  ,
          Question(question_prompt[13],'a')  ,
          Question(question_prompt[14],'a')  ,
          Question(question_prompt[15],'b')  ,
          Question(question_prompt[16],'b')  ,
          Question(question_prompt[17],'d')  ,
          Question(question_prompt[18],'b')  ,
          Question(question_prompt[19],'b')  ,
          Question(question_prompt[20],'b')  ,
          Question(question_prompt[21],'d') ,
          Question(question_prompt[22],'d') ,
          Question(question_prompt[23],'a') ,
          Question(question_prompt[24],'c') ,
           Question(question_prompt[25],'a') ,
           Question(question_prompt[26],'b') ,
          Question(question_prompt[27],'c') ,
          Question(question_prompt[28],'a') ,
          Question(question_prompt[29],'c') ,
          Question(question_prompt[30],'d'),
          Question(question_prompt[31],'a')  ,
          Question(question_prompt[32],'b')  ,
          Question(question_prompt[33],'b')  ,
          Question(question_prompt[34],'d')  ,
          Question(question_prompt[35],'b')  ,
          Question(question_prompt[36],'d')  ,
          Question(question_prompt[37],'c')  ,
          Question(question_prompt[38],'d')  ,
          Question(question_prompt[39],'c')  ,
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2015():
    question_prompt=[
                    """0 The thickness of an 800-paged book is 18mm. Calculate the thickness of one leaf of the book giving your answer in metres and in standard form.
        2.25 x 10^-4m
        4.50 x 10^-4m
        2.25 x 10^-5m
        4.50 x 10^-5m
        \n""",
        """1 If x varies inversely as the cube root of y and x = 1 when y= 8 find ywhen x = 3
        1/3
        2/3
        8/27
        4/9
        \n""",
        """2  If a = -3, b = 2, c = 4, calculate (a³-b³-c^(1/2)) / (b - 1 - c)
        37
        –37/5
        37/5
        –37
        \n""",
        """3 List the integral values of x which satisfy the inequality 1 < 5 < -2x < 7
        -1, 0, 1, 2
        0, 1, 2, 3
        -1, 0, 1, 2, 3
        -1, 0, 2, 3
        \n""",
        """4 The solution of x² – 2x – 10 are the points of intersection of two graphs. If one of the graphs is y= 2 + x – x², find the second graph.
        y= 1 – x
        y = 1 + x
        y= x – 1
        y= 3x + 3
        \n""",
        """5 If the sum of the 8th and 9th terms of an arithmetic progression is 72 and the 4th termis –6, find the common difference.
        4
        8
        6^2/3
        9^1/3
        \n""",
        """6 If 7 and 189 are the first and fourth terms of a geometric progression respectively find the sum of the first three terms of the progression.
        182
        91
        63
        28
        \n""",
        """7 For which of the following exterior angles is a regular polygon possible?   i.350   ii.180   iii.1150
        i and ii
        ii only
        ii and iii
        iii only
        \n""",
        """8 PS = 7cm and RY= 9cm. If the area of parallelogram PQRS is 56cm2, find the area of trapezium PQTS.
        56 cm²
        112 cm²
        120 cm²
        17 cm²
        \n""",
        """9 A quadrilateral of a circle of radius 6cm is cut away from each corner of a rectangle 25cm long and 18cm wide. Find the perimeter of the remaining figure
        38 cm
        (38 + 12π)cm
        (86 -12π)cm
        (86 - 6π)cm
        \n""",
        """10 STQ = SRP, PT =TQ = 6cm and QS = 5cm. Find SR.
        47/5
        5
        37/5
        22/5
        \n""",
        """11 Four interior angles o f a pentagon are 90° – x⁰, 90⁰ + x⁰, 10° – 2x⁰, 110° + 2x⁰. find the fifth interior angle.
        110°
        120°
        130°
        140°
        \n""",
        """12 Alero starts a 3km walk from P on a bearing 0230. she then walks 4km on a bearing 1130 to Q what is the bearing of Q from P?
        26°52
        52°8
        76°8
        90°
        \n""",
        """13 If cot q = x/y, find cosecq
        1/y(x²+y)
        (x/y)
        1/y√(x²+y²)
        y/x
        \n""",
        """14 If a metal pipe 10cm long has an external diameter of 12cm and a thickness of 1cm, find the volume of the metal used in making the pipe.
        120pcm³ 
        110pcm³
        60pcm³ 
        50pcm³
        \n""",
        """15 If x and y represents the mean and the median respectively of the following set of numbers; 11, 12,13,14,15,16,17,18,19,21,. Find x/y correct to one decimal place.
        1.6
        1.2
        1.1
        1.0
        \n""",
        """16 If two dice are thrown together, what is the probability of obtaining at least a score of 10?
        1/6
        1/12
        5/6
        11/12
        \n""",
        """17 Which of the following is in descending order?
        9/10,4/5,3/4,17/10
        4/5,9/10,3/4,17/20
        9/10,17/20,4/5,3/4
        4/5,9/10,17/10,3/4
        \n""",
        """18 Evaluate 2,700, 000 x 0.03 + 18,000
        4.5 x 10⁰
        4.5 x 10¹
        4.5 x 10²
        4.5 x 10³
        \n""",
        """19 The prime factors of 2,520 are
        2, 9, 5,
        2, 9, 7,
        2, 3, 5, 7,
        2, 3, 7,  9,
        \n""",
        """20 If 12 = x, find x where e =12
        20
        15
        14
        12
        \n""",
        """21 Simplify (∛(64r -6))½
        r
        2/r
        1/2r
        2/r
        \n""",
        """22 What is the difference between 0.007685 correct to three significant figures and 0.007685 correct to four places of decimal?
        10^-5
        1 x 10^-4
        1 x 10^-5
        10^-6
        \n""",
        """23 If a : b = 5 : 8,  x : y = 25 : 16, evaluate a/x : b/y
        125 : 128
        3 : 5
        3 : 4
        2 : 5
        \n""",
        """24 Oke deposited #800.00 in the bank aat the rat of 121/2% simple interest. After some time the total amount was one and half times the principal. For how many years was the money left in the bank
        2
        4
        51/2
        8
        \n""",
        """25 If the surface area of a sphere is increased by 44%. Find the percentage increase in its diameter.
        44
        30
        22
        20
        \n""",
        """26 Find p in terms of q if Log3p + 3log3q = 3
        (3/q)³
        (q/3)⅓
        (q/3)³
        (3/q)⅓
        \n""",
        """27 What are the values of y which satisfy the equation 9y – 4 ( 3y) + 3 = 0
        -1 and 0
        –1 and 1
        1 and 3
        0 and 1
        \n""",
        """28 The cost of dinner for a group of students is partly cconstant and partly varies directly as the number of students. If the cost is #74.00 when the number of students is 20, and #96.00 when the number is 30, find the cost when there are 15 students.
        #68.50
        #63.00
        #60.00
        #52.00
        \n""",
        """29 If f(x) = 2x² + 5x + 3, find f(x + 1)
        2x²– x
        2x² – x + 10
        4x² +3x + 2
        4x² +3x +12
        \n""",
        """30 Solve the positive number x such that 2(x³ – x² – 2x) = 1
        4
        3
        2
        1
        \n""",
        """31 Simplify (32x - 4x²)/(2x + 18)
        2(x - 9)
        2(9+ x )
        81– x²
        –2(x - 9)
        \n""",
        """32 Factorize completely y³ – 4xy + xy³ – 4y
        (x + xy) (y+ 2) (y - 2)
        (y+ xy) (y + 2) (y - 2)
        y(1 + x) (y+ 2) (y - 2)
        y(1 - x) (y+ 2) (y - 2)
        \n""",
        """33 If one of x³– 8 -1 is x – 2–1 , the other factors is
        x² + 2-¹ x – 4-¹
        x² - 2-¹ x – 4-¹
        x² + 2-¹ x + 4-¹
        x² + 2-¹ x –4-¹
        \n""",
        """34 Factorize 4a² + 12ab – c²+ 9b²
        4a(a – 3b) + (3b - c)²
        (2a + 3b – c )(2a + 3b + c)
        (2a – 3b -c)(2a –3b + c)
        4a(a – 3b) + (3b +c)²
        \n""",
        """35 What are K and L respectively if ½ (3y – 4x)² = (8x² +kxy+ Ly²)
        -12, 9/2
        -6, 9
        6, 9
        12, 9/2
        \n""",
        """36 A regular polygon of (2k + 1) sides has 1400 as the size of each interior angel. Find K.
        4
        41/2
        8
        81/2
        \n""",
        """37 PQRS is a rhombus. If PR² + QS² = kPQ². Determine k.
        1
        2
        3
        4
        \n""",
        """38 Solve the pair of equation for x and y respectively 2x-1 – 3y-1 = 4, 4x -1 + y-1 = 1
        -1, 2
        1, 2
        2, 1
        2, -1
        \n""",
        """39 What value ofQ will make the expression 4x² + 5x + Q a complete square?
        25/16
        25/64
        5/8
        5/4
        \n""",
    ]
    question=[
        Question(question_prompt[0], 'c'),
        Question(question_prompt[1], 'c'),
        Question(question_prompt[2], 'a'),
        Question(question_prompt[3], 'a'),
        Question(question_prompt[4], 'a'),
        Question(question_prompt[5], 'd'),
        Question(question_prompt[6], 'b'),
        Question(question_prompt[7], 'c'),
        Question(question_prompt[8], 'c'),
        Question(question_prompt[9], 'b'),
        Question(question_prompt[10], 'a'),
        Question(question_prompt[11], 'd'),
        Question(question_prompt[12], 'c'),
        Question(question_prompt[13], 'c'),
        Question(question_prompt[14], 'd'),
        Question(question_prompt[15], 'd'),
        Question(question_prompt[16], 'a'),
        Question(question_prompt[17], 'c'),
        Question(question_prompt[18], 'a'),
        Question(question_prompt[19], 'c'),
        Question(question_prompt[20], 'a'),
        Question(question_prompt[21], 'b'),
        Question(question_prompt[22], 'c'),
        Question(question_prompt[23], 'd'),
        Question(question_prompt[24], 'b'),
        Question(question_prompt[25], 'd'),
        Question(question_prompt[26], 'c'),
        Question(question_prompt[27], 'd'),
        Question(question_prompt[28], 'b'),
        Question(question_prompt[29], 'a'),
        Question(question_prompt[30], 'c'),
        Question(question_prompt[31], 'd'),
        Question(question_prompt[32], 'c'),
        Question(question_prompt[33], 'a'),
        Question(question_prompt[34], 'c'),
        Question(question_prompt[35], 'a'),
        Question(question_prompt[36], 'a'),
        Question(question_prompt[37], 'd'),
        Question(question_prompt[38], 'd'),
        Question(question_prompt[39], 'a'),
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2018():
    question_prompt=[
                    """0 In a regular pentagon, PQRST, PR intersects QS at O. calculate RQS.
36°
72°
108°
144°
\n""",
"""1 If cos q = 12/13, find 1 + cot 2q
169 / 25
25 / 169
169 / 144
144 / 169
\n""",
"""2 A cylindrical pipe, made of metal is 3cm, thick if the internal radius of the pipe is 10cm.\n Find the volume of metal used in making 3m of the pipe
153πcm³
207πcm³
15,300πcm³
20,700πcm³
\n""",
"""3 If the height of two circular cylinders are in the ratio 2 : 3 and their base radii are in the ratio 9. \nwhat is the ratio of their volume
27 : 32
27 : 23
23 : 32
21 : 27
\n""",
"""4 The locus of a point which moves so that it is equidistant from two intersecting straight lines is the
perpendicular bisector of the two lines
angle bisector of the two lines
bisector of the two lines
line parallel to the two lines
\n""",
"""5 The mean of ten positive numbers is 16. when another number is added, the mean becomes 18. find the \neleventh number.
3
16
18
30
\n""",
"""6 Two numbers are removed at randomfrom the numbers 1, 2, 3 and 4. what is the probability that the sum of the \nnumbers removed is even?
2/3
 ½
1/3
 ¼
\n""",
"""7 Find the probability that a number selected at random from 41 to 56 is a multiple of 9
 1/8
2/15
3/16
7/8
\n""",
"""8 Simplify (3⅓) – (1¼) x (2/3 + 1⅖)
117 / 30
39 / 10
41 / 10
11 / 36
\n""",
"""9 If 2257 is the result of subtracting 4577 from 7056 in base n, find n.
8
9
10
11
\n""",
"""10 Express 62/3 as a decimal correct to 3 significant figures.
20.6 
20.667
20.67
20.7
\n""",
"""11 Factory P produces 20,000 bags of cement per day while factory Q produces 15,000 bags per day. \nIf P reduces production by 5% and Q increases production by 5% determine the effective loss in the number of bags produced per day by the two factories.
250
750
1000
1250
\n""",
"""12 Musa borrows #10.00 at 2% per month interest and repays #8.00 after 4 months. However much does he still owe?
#10.80
#10.67
#2.80
#2.67
\n""",
"""13 If 3 gallons of spirit containing 20% water are added to 5 gallons of another spirit containing 15% water, \nwhat percentage of the mixture is water?
2 whole number 4/5%
16 whole number 7/8%
18 whole number 1/8%
18 whole number 7/8%
\n""",
"""14 Simplify 2log2/5 – log72/125 + log9
1 – 4log 3
–1 + 2log3
–1 +5log2
1-2log2
\n""",
"""15 Multiply (x² –3x - + 1)² by (x - a)
x³ – (3 - a)x² + (1 + 3a)x –1
x³ – (3 - a)x² + 3ax – a
x³ – (3 - a)x² + (1 + 3a) – a
x³ + (3 - a)x² + (1 + 3a) - a
\n""",
"""16 Evaluate (Xy² - X²y)/(x² - xy) when x = -2 and y = 3
-3
–3/5
3/5
3
\n""",
"""17 A car travels from Calabar to Enugu, a distant of pkm with an average speed of u km per hour and \ncontinues to Benin, a distance of q km, with an average speed of w km per hour. Find its average speed from Calabar to Benin.
(p+q) / (up+wq)
u+w
uw(p+q) / (wp+uq)
(wp+uq) / (u+wq)
\n""",
"""18 If w varies inversely as uv/u + v and is equal to 8 when u = 2 and v = 6, find a relationship between u, v, w.
upw= 16(u + v)
16ur = 3w(u + v)
upw= 12(u + v)
12upw= u + r
\n""",
"""19 If g(x) = (x² + 3x ) find g(x + 1) – g(x)
(x+ 2)
2(x+2)
(2x+1)
(x+ 4)
\n""",
"""20 Factorize m³ – m² –m + 2
(m2 +1)(m- 2)
(m+ 1)(m+ 1)(m+2)
(m+ 1)(m+ 1)(m- 2)
(m2 +2)(m- 1)
\n""",
"""21 Factorize 1 – (a - b)²
(1 – a - b)(1 – a - b)
(1– a +b)(1+ a - b)
(1 – a + b)(1 – a + b)
(1 – a - b)(1 + a - b)
\n""",
"""22 Which of the following is a factor of rs + tr – pt –ps?
(p - s)
(s - p)
(r - p)
(r + p)
\n""",
"""23 Find the two values of ywhich satisfy the simultaneous equation 3x + y = 8,  x² + xy = 6
-1 and 5
–5 and 1
1 and 5
1 and 1
\n""",
"""24 Find the range of values of xwhich satisfy the inequality (x/2 + x/3 + x/4) < 1
x < 12/13
x <13
x < 9
x < 13/12
\n""",
"""25 Find the positive number n, such that thrice it s square is equal to twelve times the number.
1
2
3
4
\n""",
"""26 Solve the equation (x - 2)(x - 3) = 12
2, 3
3, 6
–1, 6
1, 6
\n""",
"""27 Evaluate x² (x² - 1) raise to the power of - (1/2)  – (x² – 1) raise to the power of 1/2
(x² – 1) raise to the power of 1/2
(x² – 1)
(x² – 1) raise to the power of-1
(x² – 1) raise to the power of-1/2
\n""",
"""28 Find the gradient of the line passing through the points (-2,0) and (0, -4)
2
–4
–2
 4
\n""",
"""29 At what value of x is the function y = x² – 2x – 3 minimum?
 1
–1
–4
4
\n""",
"""30 What is the nth termof the progression 27, 9, 3,………..?
27 (1/3) raise to the power n – 1
3n + 2
27 + 18 raise to the power (n - 1)
27 + 6 raise to the power (n - 1)
\n""",
"""31 Find the sumof the 20 term in an arithmetic progression whose first term is 7 and last term is 117
2480
1240
620
124
\n""",
"""32 The angles of a quadrilateral are 5x – 30, 4x + 60, 60 – x and 3x + 61. find the smallest of these angles.
5x – 30
4x + 60
60 – x
3x + 61.
\n""",
"""33 The area of a square is 144sqcm. Find the length of its diagonal
11√3cm
12cm
12√2cm
13cm
\n""",
"""34 One angle of a rhombus is 600. the shorter of the two diagonals is 8cm long. Find the length of the longer one
8√3
16/√3
5√3
10/√ 3
\n""",
"""35 If the exterior angles of a pentagon are x°, (x + 5)°, (x + 10)°, (x + 15)° and (x + 20)°, find x
118°
72°
62°
36°
\n""",
"""36 A flag staff stands on the top of a vertical tower. Aman standing 60m away from the tower observes that the \nangles of elevation of the top and bottom of the flag staff are 640 and 620 respectively. Find the length of a flag staff.
60(tan 62°– tan 64°)
60(cot 64° – cot 62°)
60(cot 62° – cot 64°)
60(tan 64° – tan 62°)
\n""",
"""37 From a point Z, 60m, north of X, a man walks 60√3m eastwards to another point Y. find the bearing of y from x.
030°
045°
060°
090°
\n""",
"""38 A surveyor walks 500m up a hill which slopes at an angle of 300. calculate the vertical height through\n which he rises
250m
500√3/3m
250√2m
250√3m
\n""",
"""39 Find the total area of the surface of a solid cylinder whose base radius is 4cm and height is 5cm.
56πcm2
72πcm2
96πcm2
192πcm2
\n""",
    ]
    question=[
        Question(question_prompt[0], 'a'),
        Question(question_prompt[1], 'a'),
        Question(question_prompt[2], 'd'),
        Question(question_prompt[3], 'a'),
        Question(question_prompt[4], 'b'),
        Question(question_prompt[5], 'd'),
        Question(question_prompt[6], 'b'),
        Question(question_prompt[7], 'a'),
        Question(question_prompt[8], 'a'),
        Question(question_prompt[9], 'a'),
        Question(question_prompt[10], 'd'),
        Question(question_prompt[11], 'a'),
        Question(question_prompt[12], 'c'),
        Question(question_prompt[13], 'b'),
        Question(question_prompt[14], 'd'),
        Question(question_prompt[15], 'd'),
        Question(question_prompt[16], 'a'),
        Question(question_prompt[17], 'c'),
        Question(question_prompt[18], 'c'),
        Question(question_prompt[19], 'b'),
        Question(question_prompt[20], 'c'),
        Question(question_prompt[21], 'b'),
        Question(question_prompt[22], 'c'),
        Question(question_prompt[23], 'a'),
        Question(question_prompt[24], 'a'),
        Question(question_prompt[25], 'd'),
        Question(question_prompt[26], 'c'),
        Question(question_prompt[27], 'd'),
        Question(question_prompt[28], 'c'),
        Question(question_prompt[29], 'a'),
        Question(question_prompt[30], 'a'),
        Question(question_prompt[31], 'b'),
        Question(question_prompt[32], 'c'),
        Question(question_prompt[33], 'c'),
        Question(question_prompt[34], 'a'),
        Question(question_prompt[35], 'c'),
        Question(question_prompt[36], 'd'),
        Question(question_prompt[37], 'c'),
        Question(question_prompt[38], 'a'),
        Question(question_prompt[39], 'b'),
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 1
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     scores = int((score / len(questions) * 100))
     print("your score is: " + str(scores) + "%")
     des.update({nam:str(scores)})
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2012():
    question_prompt=[
        '''[1] A right circular cone has a base radius r cm and a vertical 2y. the height of the cone is
        (a)r tan yo cm 
        (b)r sin yo cm
        (c)r cot yocm
        (d)r cost yo cm\n''',
        '''[2] Two fair dice are rolled. What is the probability that both show up the same number of point?
        (a)1/36
        (b)7/36
        (c)½
        (d)1/6\n''',
        '''[3] The larger value of y for which (y - 1)^2 = 4y – 7 is
        (a)2
        (b)4
        (c)6
        (d)7\n''',
        '''[4] If sin q = x/y and 0° < q < 90° then find 1/ tan q
        (a)x/√(y2 – x2) 
        (b)x/y
        (c)√y2 –x2 / y
        (d)√y2 - x2 \n''',
        '''[5] In the figure aboveTSP =PRQ, QR= 8cm. PR= 6cm and ST = 12cm. Find the length SP
        (a)4cm 
        (b)16cm
        (c)9cm
        (d)14cm \n''',
        '''[6] XYZ is a triangle and XW is perpendicular to YZ at W. if XZ = 5cm and WZ = 4cm, calculate XY.
        (a)53cm
        (b)3√5cm
        (c)33cm
        (d)5cm\n''',
        '''[7] Arrange the following numbers in ascending order of magnitude 6/7, 13/15, 0.865
        (a)6/7 < 0.865 < 13/15
        (b)6/7 < 13/15 < 0.865
        (c)13/15 < 6/7 < 0.865
        (d)13/15 < 0.865 < 6/7\n''',
        '''[8] A sum of money was invested at 8% per annum simple interest. If after 4years the money amounts to #330.00, find the amount originally invested.
        (a)#180.00
        (b)#250.00
        (c)#150.00
        (d)#200.00\n''',
        '''[9] In the equation below, solve for x if all the numbers are in base 2? 11/x=1000/(x +101)
        (a)101
        (b)11
        (c)110
        (d)111\n''',
        '''[10] List all integers satisfying the inequality -2 < 2x – 6 < 4
        (a)2, 3, 4, 5
        (b)2, 3, 4
        (c)2, 5
        (d)3, 4, 5\n''',
        '''[11] Find correct to to w decimal places 100+ 1/100 + 3/1000 + 27/10000
        (a)100.02
        (b)1000.02
        (c)100.22
        (d)100.01\n''',
        '''[12] If three number p,q,r are in the ratio 6:4:5 find the value of (3q – q)/(4q + r)
        (a)3/2
        (b)2/3
        (c)2
        (d)3\n''',
        '''[13] Without using tables, evaluate Log24 + Log42 – Log255
        (a)½
        (b)1/5
        (c)0
        (d)5\n''',
        '''[14] John gives one third of his money to Janet who has #105.00. He then finds that his money is reduced to one-fourth of what Janet now has. Find how much money John had at first.
        (a)#45.00
        (b)#48.00
        (c)#52.00
        (d)#58.00\n''',
        '''[15] Find x if Log(x) to base 9  = 1.5
        (a)72.0
        (b)27.0
        (c)36.0
        (d)3.5\n''',
        '''[16] 22 whole number 1/2% of the Nigerian Naira is equal to 17 whole number 1/10% of a foreign currency M. what is the conversion rate of the M to the Naira?
        (a)1M= 1whole number 5/57N
        (b)1M= 21whole number 1/57N
        (c)1M= 1whole number 18/57N
        (d)1M= 3whole number 81/4N\n''',
        '''[17] Find the values of p for which the equation x2 – (p - 2)x + 2p + 1 = 0 has equal roots
        (a)(0, 12)
        (b)(1, 2)
        (c)(21, 0)
        (d)(4, 5)\n''',
        '''[18] In a restaurant, the cost of providing a particular type of food is partly constant and partly inversely proportional to the number of people. If the cost per head for 100 people is 30k and the cost for 40 people is 60k, find the cost for 50 people
        (a)15k
        (b)45k
        (c)20k
        (d)50k\n''',
        '''[19] The factors of 9 – (x2 – 3x - 1)^2 are
        (a)-(x - 4)(x + 1)(x - 1)(x - 2)
        (b)(x - 4)(x - 1)(x - 1)(x +2)
        (c)-(x - 2)(x + 1)(x+ 2)(x +4)
        (d)(x - 4)(x -3)(x - 2)(x +1)\n''',
        '''[20] If 32y – 6(3y) = 27 find y
        (a)1
        (b)–1
        (c)2
        (d)–3\n''',
        '''[21] Factorize abx^2 + 8y– 4bx –2axy
        (a)ax - 4) (bx – 2y)
        (b)(ax + b) (x – 8y)
        (c)(ax – 2y) (by – 4)
        (d)(abx - 4) (x – 2y)\n''',
        '''[22] If the quadrilateral function 3x^2 – 7x + R is a perfect square find R
        (a)49/24
        (b)49/3
        (c)49/6
        (d)49/12\n''',
        '''[23] Solve the following equation 2/(2r – 1) – 5/3 = 1/ (r + 2)
        (a)(-1, 5/2)
        (b)(-1, -5/1)
        (c)(5/2, 1)
        (d)(2, 1)\n''',
        '''[24] Solve for (x,y) in the equations 2x + y= 4: x2 + xy= -12
        (a)(6, -8); (-2,8)
        (b)(3, -4); (-1, 4)
        (c)(8, -4); (-1, 4)
        (d)(-8, 6);(8, -2)\n''',
        '''[25] Solve the simultaneous equations 2x – 3y + 10 = 10x – 6y = 5
        (a)x = 2 whole number 1/2, y = 3 whole number 1/3
        (b)x = 3 whole number 1/2, y = 2 whole number 1/3
        (c)x = 2 whole number 1/4, y = 3
        (d)x = 3 whole number 1/2, y = 2 whole number 1/5\n''',
        '''[26] If f(x - 2) = 4x2 + x + 7 find f(1)
        (a)12
        (b)27
        (c)7
        (d)46\n''',
        '''[27] In DXYZ,XY= 13cm,YZ= 9cm,XZ= 11cm and XYZ = q°. find cos q°
        (a)4/39
        (b)43/39
        (c)209/286
        (d)43/78\n''',
        '''[28] If the hypotenuse of a right angle isosceles triangle is 2, what is the length of each of the other sides?
        root 2
        (a)1/root2
        (b)2root2
        (c)1
        (d)root 2\n''',
        '''[29] If two fair coins are tossed, what is the probability of getting at least one head?
        (a)¼
        (b)½
        (c)¾
        (d)2/3\n''',
        '''[30] The ratio of the length of two similar rectangular blocks is 2:3, if the volume of the larger block is 351cm3, then the volume of the other block is
        (a)234.00cm3
        (b)526.50cm3
        (c)166.00cm3
        (d)729.75cm3\n''',
        '''[31] The bearing of bird on a tree from a hunter on the ground is N720E. what is the bearing of the hunter from the bird?
        (a)S18°W
        (b)S72°W
        (c)S27°W
        (d)S27°E\n''',
        '''[32] In DXYZ above, XKZ =90°, XK= 15cm, XZcm and YK = 8cm. Find the area of the DXYZ.
        (a)180 sq.cm
        (b)210sq.cm
        (c)160sq.cm
        (d)320sq.cm\n''',
        '''[33] Without using tables. Calculate the value of 1 + sec square 30?
        (a)2 whole no 1/3
        (b)2
        (c)1whole no 1/3
        (d)¾\n''',
        '''[34] What is the probability that a number chosen at random from the integers between 1 and 10 inclusive is either a prime or a multiple of 3?
        (a)7/10
        (b)3/5
        (c)4/5
        (d)½\n''',
        '''[35] Find the area of a regular hexagon inscribed in a circle of radius 8cm.
        (a)96 root 3cm2
        (b)192.3 cm2
        (c)16 cm2
        (d)32 cm2\n''',
        '''[36] In the figure above, MNOP is a cyclic quadrilateral, MN and PQ are produced to meet at X and NQ and MP are produced to meet at Y. ifMNQ= 86o andNQP= 122o, find (x0, y0)
        (a)(28°, 36°)
        (b)(36° ,28°)
        (c)(43°, 61°)
        (d)(61°, 43°)\n''',
        '''[37] A solid sphere of radius 4cm has mass of 64kg.What will be the mass of a shell of the same metal whose internal and external radii are 2cm and 3cm respectively?
        (a)5kg
        (b)16kg
        (c)19kg
        (d)25kg\n''',
        '''[38] POQ is the diameter of the circle PQRS. If PSR= 145°, find x°
        (a)25°
        (b)35°
        (c)45°
        (d)55°\n''',
        '''[39] PQRS is a trapezium of area 14cm2 in which PQ//RS, if PQ= 4cm and SR= 3cm, find the area of DSQR in cm2
        (a)7.0
        (b)6.0
        (c)5.2
        (d)5.0\n''',
        '''[40] In a class of 120 students, 18 of them scored an A grade in Mathematics. If the section representing the A grade students on a π chart has angle Z0 at the centre of the circle, what is Z?
        (a)15
        (b)28
        (c)54
        (d)52\n''' ,
    ]
    question=[
        Question(question_prompt[0], 'c'),
        Question(question_prompt[1], 'd'),
        Question(question_prompt[2], 'b'),
        Question(question_prompt[3], 'c'),
        Question(question_prompt[4], 'b'),
        Question(question_prompt[5], 'b'),
        Question(question_prompt[6], 'a'),
        Question(question_prompt[7], 'b'),
        Question(question_prompt[8], 'b'),
        Question(question_prompt[9], 'b'),
        Question(question_prompt[10], 'a'),
        Question(question_prompt[11], 'b'),
        Question(question_prompt[12], 'a'),
        Question(question_prompt[13], 'a'),
        Question(question_prompt[14], 'b'),
        Question(question_prompt[15], 'c'),
        Question(question_prompt[16], 'a'),
        Question(question_prompt[17], 'd'),
        Question(question_prompt[18], 'c'),
        Question(question_prompt[19], 'a'),
        Question(question_prompt[20], 'a'),
        Question(question_prompt[21], 'd'),
        Question(question_prompt[22], 'b'),
        Question(question_prompt[23], 'a'),
        Question(question_prompt[24], 'd'),
        Question(question_prompt[25], 'd'),
        Question(question_prompt[26], 'd'),
        Question(question_prompt[27], 'a'),
        Question(question_prompt[28], 'c'),
        Question(question_prompt[29], 'a'),
        Question(question_prompt[30], 'c'),
        Question(question_prompt[31], 'b'),
        Question(question_prompt[32], 'a'),
        Question(question_prompt[33], 'b'),
        Question(question_prompt[34], 'a'),
        Question(question_prompt[35], 'a'),
        Question(question_prompt[36], 'a'),
        Question(question_prompt[37], 'b'),
        Question(question_prompt[38], 'b'),
        Question(question_prompt[39],'c')
    ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2020():
    question_prompt=[
        '''[1] Solve for y in the equation 10 raise to the power y, X raise to the power(2y-2) x 4 raise to the power(y-1)=1
        (a)¾ 
        (b)2/3
        (c)1
        (d)5/4\n''',
        '''[2] If (2 logy to base 3) + (log x^2 to base 3)  = 4, then y is
        (a)(4 - log3x^2) / 2
        (b)4 / log3x^2
        (c)2/X 
        (d)± 9/X\n''',
        '''[3] Solve without using tables log5 (62.5) - log5 (1/2)
        (a)3 
        (b)4
        (c)5
        (d)8\n''',
        '''[4] If #225.00 yields #27.00 in x years simple interest at the rate of 4% per annum, find x
        (a)3
        (b)4
        (c)12
        (d)27\n''',
        '''[5] If square root of  x^2 + 9 = x+ 1, solve for x
        (a)5
        (b)4
        (c)3
        (d)1\n''',
        '''[6] Make x the subject of the relation 1+ax / 1 - ax = p/q
        (a)p+q / a(p-q)
        (b)p-q / a(p+q)
        (c)p-q / apq
        (d)pq / a(p-q)\n''',
        '''[7] Which of the following is a factor of 15 + 7x – 2x^2?
        (a)x - 3
        (b)x + 3
        (c)x - 5
        (d)x + 5\n''',
        '''[8] Evaluate (x+1/x+1)^2 – (x-1/x-1)^2
        (a)4x^2
        (b)(2/x+2)^2
        (c)4
        (d)4(1+x\n''',
        '''[9] Solve the following simultaneous equations for x. x^2 + y – 5= 0 , y – 7x + 3=0
        (a)-2, 4
        (b)2, 4
        (c)-1, 8
        (d)1, -8\n''',
        '''[10] Solve the following equation (3x-2)(5x-4)=(3x-2) to the power of  2
        (a)-3/2, 1
        (b)1
        (c)2/3, 1
        (d)2/3, 4/5\n''',
        '''[11] If the function f is defined by f(x+2) = 2x2 + 7x – 5, find f(-1)
        (a)-10
        (b)-8
        (c)4
        (d)10\n''',
        '''[12] Divide the expression x^3 + 7x^2 –x –7 by -1 + x^2
        (a)–x^3 + 7x^2 - x - 7
        (b)–x^3 -7x +7
        (c)x-7
        (d)x+7\n''',
        '''[13] Simplify 1/p-1/q –p/q-q/p
        (a)1/p-q
        (b)-1/p+q
        (c)1/pq
        (d)1/pq(p-q)\n''',
        '''[14] Solve the inequality y^2 - 3y > 18
        (a)-2 < y <6
        (b)y <- 3 or y > 6
        (c)y >- 3 or y > 6
        (d)y <-3 or y < 6\n''',
        '''[15] If x is negative, what is the range of values of x within which x + 1/3 > 1/x + 3
        (a)3 < x < 4
        (b)-4 < x < -3
        (c)-2 < x <-1
        (d)-3 < x < 0\n''',
        '''[16] The three sides of an isosceles triangle are of lengths (x + 3), (2x + 3), (2x - 3) respectively. Calculate x.
        (a)0
        (b)1
        (c)3
        (d)6\n''',
        '''[17] A man’s initial salary is #540.00 a month and increases after each period of six months by #36.00 a month. Find his salary in the eighth month of the third year.
        (a)#828.00
        (b)#756.00
        (c)#720.00
        (d)#684.00\n''',
        '''[18] If (k + 1), (2k - 1), (3k+1) are three consecutive terms of a geometric progression, find the possible values of the common ratio.
        (a)0, 8
        (b)-1, 5/3
        (c)2, 3
        (d)1, -1\n''',
        '''[19] A binary operation * is defined on a set of real numbers by x*y = xy for all real values of x and y, if x*2 = x, find the possible values of x
        (a)0, 1
        (b)1, 2
        (c)2, 2
        (d)0,2\n''',
        '''[20] PQRST is a regular pentagon and PQVU is a rectangle with U and V lying on TS and SR respectively as shown in the diagram above. Calculate TUV
        (a)18°
        (b)54°
        (c)90°
        (d)108°\n''',
        '''[21] A regular polygon has 1500 as the size of each interior angle. How many sides has the polygon?
        (a)12
        (b)10
        (c)9
        (d)8\n''',
        '''[22] Calculate the length, in cm, of the arc of the circle of diameter 8cm which subtends an angle of 22 whole number 1/2 degree
        (a)2π
        (b)2/3π
        (c)π/2
        (d)3π\n''',
        '''[23] Find the radius of a sphere whose surface area is 154cm2 (π =22/7)
        (a)7.00cm
        (b)3.50cm
        (c)3.00cm
        (d)1.75cm\n''',
        '''[24] Find the area of the sector of a circle with radius 3m, if the angle of the sector is 600
        (a)4.0m2
        (b)4.1m2
        (c)4.7m2
        (d)5.0m2\n''',
        '''[25] The angle between latitudes 300°S and 130°N is
        (a)17°
        (b)33°
        (c)43°
        (d)53°\n''',
        '''[26] If sin q= cos 0, find 0 between 0° and 360°.
        (a)45°, 225°
        (b)135°, 315°
        (c)45°, 315°
        (d)135°, 225°\n''',
        '''[27] If two angles of a triangle are 300 each and the longest side is 10cm, calculate the length of each of the other sides.
        (a)5cm
        (b)4cm
        (c)3√3cm
        (d)10√3/3cm\n''',
        '''[28] The mean of the ages of ten secondary school pupils is 16 but when the age of their teacher is added to it, the mean becomes 19. Find the age of the teacher.
        (a)27
        (b)35
        (c)38
        (d)49\n''',
        '''[29] A number is selected at random between 20 and 30 both numbers inclusive. Find the probability that the number is a prime
        (a)2/11
        (b)5/11
        (c)6/11
        (d)8/11\n''',
        '''[30] Evaluate (0.36 x 5.4 x 0.63) (4.2 x 9.0 x 2.4) correct to 2 significant figures
        (a)0.013
        (b)0.014
        (c)0.13
        (d)0.14\n''',
        '''[31] Evaluate Log5(0.04) / (Log318 – Log32)
        (a)1
        (b)-1
        (c)2/3
        (d)-2/3\n''',
        '''[32] Without using tables, solve the equation 8 raise to the power of x - 2 = 2/25
        (a)4
        (b)6
        (c)8
        (d)10\n''',
        '''[33] Given that √2 = 1.414, find without using tables, the value of 1/√2
        (a)0.141
        (b)0.301
        (c)0.667
        (d)0.707\n''',
        '''[34] In a science class of 42 students, each offers at least one of Mathematics and Physics. If 22 students offer Physics and 28 students offer Mathematics, find how many students offer Physics only?
        (a)6
        (b)8
        (c)12
        (d)14\n''',
        '''[35] Solve for x if 25 raise to the power of x + 3 raise to the power of (5x) = 4
        (a)1 or -4 
        (b)0
        (c)1
        (d)-4 or 0\n''',
        '''[36] Calculate the standard deviation of the following data. 7, 8, 9, 10, 11, 12, 13.
        (a)2
        (b)4
        (c)10 
        (d)11\n''',
        '''[37] The chances of three independent event X, Y, Z occurring are 1/2 , 2/3, ¼ respectively. What are the chances of y and z only occurring?
        (a)1/8
        (b)1/24
        (c)1/12
        (d)¼\n''',
        '''[38] Calculate (3310 base 5) - (1442 base 5)
        (a)1313 base 5
        (b)2113 base 5
        (c)4302 base 5
        (d)1103 base 5\n''',
        '''[39] Convert 3.1415926 to 5 decimal places
        (a)3.14160
        (b)3.14159
        (c)0.31415
        (d)3.14200\n''',
        '''[40] The length of a notebook 15cm, was measured as 16.8cm. calculate the percentage error to 2 significant figures.
        (a)12.00%
        (b)11.00%
        (c)10.71%
        (d)0.12%\n'''
    ]
    question=[
        Question(question_prompt[0], 'b'),
        Question(question_prompt[1], 'd'),
        Question(question_prompt[2], 'a'),
        Question(question_prompt[3], 'a'),
        Question(question_prompt[4], 'b'),
        Question(question_prompt[5], 'b'),
        Question(question_prompt[6], 'c'),
        Question(question_prompt[7], 'd'),
        Question(question_prompt[8], 'd'),
        Question(question_prompt[9], 'c'),
        Question(question_prompt[10], 'b'),
        Question(question_prompt[11], 'd'),
        Question(question_prompt[12], 'b'),
        Question(question_prompt[13], 'd'),
        Question(question_prompt[14], 'b'),
        Question(question_prompt[15], 'd'),
        Question(question_prompt[16], 'c'),
        Question(question_prompt[17], 'b'),
        Question(question_prompt[18], 'a'),
        Question(question_prompt[19], 'b'),
        Question(question_prompt[20], 'a'),
        Question(question_prompt[21], 'c'),
        Question(question_prompt[22], 'a'),
        Question(question_prompt[23], 'c'),
        Question(question_prompt[24], 'c'),
        Question(question_prompt[25], 'a'),
        Question(question_prompt[26], 'd'),
        Question(question_prompt[27], 'd'),
        Question(question_prompt[28], 'a'),
        Question(question_prompt[29], 'a'),
        Question(question_prompt[30], 'c'),
        Question(question_prompt[31], 'b'),
        Question(question_prompt[32], 'b'),
        Question(question_prompt[33], 'd'),
        Question(question_prompt[34], 'd'),
        Question(question_prompt[35], 'b'),
        Question(question_prompt[36], 'b'),
        Question(question_prompt[37], 'a'),
        Question(question_prompt[38], 'b'),
        Question(question_prompt[39],'a')
    ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2008():
    question_prompt=["""1. Find the minimum value of x^2 – 3x + 2 for all real values of x.
A.-1/4
B.-1/2
C. 1/4 
D. 1/2
""",
"""2. What value of g will make the expression 4x^2 – 18xy – g a perfect square?
A.9
B.9y2/4
C.81y2
D.81y2/4
""",
"""3 Find the value of K if 5+2r/(r+1)(r-2) expressed in partial fraction is K/r-2+ L/r+1, where K and L are constants.
A.3
B. 2
C.1
D.-1
""",
"""4.Let f(x) = 2x + 4 and g(x) = 6x + 7 where g(x) > 0. solve the inequality f(x) / g(x) < 1
A.x < - ¾
B.x > - 4/3
C.x > - 3/4
D.x > - 12
""",
"""5.Find the range of values of x which satisfies the inequality 12x^2 < x + 1
A.-1/4 < x < 1/3
B.¼ < x < 1/3
C.-1/3 < x < 1/4
D.-1/4 < x <- 1/3
""",
"""6. Sn is the sum of the first n terms of a series given by Sn = n^2 – 1. find the nth term.
A.4n + 1
B.4n – 1
C.2n + 1
D.2n – 1
""",
"""7.The nth term of a sequence is given by 31 - n. find the sum of the first three terms of the sequence.
A.23/9
B.1
C.1/3
D.1/9
""",
"""8. Two binary operations * and Ä are defined as m*n = mn – n – 1 and m Ä n = mn + n – 2 for all real numbers m, n. find the values of 3 Ä (4*5).
A.60
B.57
C.54
D.42
""",
"""9. If xy = x + y – xy, find x, when (x*2)+(x*3) = 68
A.24
B.22
C.-12
D.-21
""",
"""10.Each of the base angles of an isosceles triangle is 58° and all the vertices of the triangle lie on a circle. Determine the angle which the base of the triangle subtends at the centre of the circle.
A.128°
B.116°
C.64°
D.58°
""",
"""11.A chord of a circle diameter 42cm subtends an angle of 60° at the centre of the circle. Find the length of the minor arc.[π = 22/7]
A.22 cm
B.44 cm
C.110 cm
D.220 cm
""",
"""12.An arc of a circle subtends an angle of 700 at the centre. If the radius of the circle is 6cm, calculate the area of the sector subtended by the given angle.
A.22 cm2
B.44 cm2
C.66 cm2
D.88 cm2
""",
"""13.A cone with the sector angle of 450° is cut out of a circle of radius r cm. find the base radius of the cone.
A.r/16cm
B.r/8cm
C.r/4cm
D.r/2cm
""",
"""14.A point P moves so that it is equidistant from points L and M. if LM is 16cm, find the distance of P from LM when P is 10cm from L.
A.12cm
B.10cm
C.8cm
D.6cm
""",
"""15.The angle between the positive horizontal axis and a given line is 1350. find the equation of the line if it passes through the point (2, 3).
A.x – y = 1
B.x + y = 1
C.x + y = 5
D.x – y = 5
""",
"""16.Find the distance between the point Q(4, 3) and the point common to the lines 2x – y = 4 and x + y = 2
A.3√10
B.3√5
C.√26
D.√13
""",
"""17.The angle of elevation of a building from a measuring instrument placed on the ground is 30°. if the building is 40m high, how far is the instrument from the foot of the building?
A.20√3m
B.40√3m
C.20√3m
D.40√3m
""",
"""18.In a triangle XYZ, if <XYZ is 600, XY = 3cm and YZ = 4cm, calculate the length of the side XZ.
A.√23cm
B.√13cm
C.2√5cm
D.2√3cm""",
"""19.Differentiate 6x^3 - 5x^2 + 1/3x^2
A.2 + 2 / 3x^3
B.2 + 1/6x
C.2 - 2 / 3x^3
D.2 - 1 / 6x""",
"""20.d/dx cos(3x^2 – 2x) is equal to
A.-sin(6x- 2)
B.-sin(3x^2 – 2x)
C.(6x- 2) sin(3x^2– 2x)
D.(6x- 2) sin (3x^2 –2x)""",
"""21.Find the gradient of the curve y = 2√x – 1/x at the point x = 1
A.0 
B.1 
C.2
D.3
""",
"""22.Integrate 1/x + cos x with respect to x.
A.-1/x2 +sin x+ k
B.1nx+sin x+ k
C.1nx–sin x+ k
D.-1/x2 – sin x + k""",
"""23.If y = x(x^4 + x^2 + 1), evaluate 1 -1dyx
A.11/12
B.11/16
C.5/6
D. 0""",
"""24.The following are the scores of ten students in a test of 20 marks; 15,16,17,13,16,8,5,16,19,17. what is the modal score?
A.13
B.15
C.16
D.19""",
"""25.Find the standard deviation of the following data - 5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
A.2
B.3
C.√10
D.√11""",
"""26.Find the difference between the range and the variance of the following set of numbers 4, 9, 6, 3, 2, 8, 10, 5, 6, 7 where d2 = 60.
A.2
B.3
C.4
D.6""",
"""27.When the expression pm^2 + qm + 1 is divided by (m - 1), it has a remainder 2 and when divided by (m + 1) the remainder is 4. find p and q respectively
A.2, -1
B.-1, 2
C.3, -2
D.-2, 3""",
"""28.Factorize r^2 – r (2p + q) + 2pq
A.(r – 2q) (2r - p)
B.(r - q) (r + p)
C.(r - q) (r – 2p)
D.(2r - q) (r + p)""",
"""29.Solve the equation  √x - √(x - 2) – 1 = 0
A.3/2
B.2/3
C.4/9
D.9/4""",
"""30.Find the range of values of m for which the roots of the equation 3x^2 – 3mx + (m^2 – m - 3) = 0
A.-1 < m < 7
B.-2 < m < 6
C.-3 < m < 9
D.-4 < m < 8""",
"""31.Make a/x the subject of the formula x + a/x – a 
A.m – 1/m + 1
B.1 + m/1 – m
C.1-m/1 + m
D.m + 1/m – 1""",
"""32.Divide (2x^3 + 11x^2 + 17x + 6) by 2x + 1
A.x^2 + 5x + 6
B.2x^2 + 5x + 6
C.2x^2 – 5x + 6
D.x^2 – 5x + 6""",
"""33.Express in partial fractions 11x + 2 / 6x^2 – x – 1
A.1/3x – 1 + 3/2x +1
B.3/3x + 1 – 1/2x – 1
C.3/3x – 1 – 1/2x +1
D.1/3x+ 1 +3/2x- 1""",
"""34.If x is a positive real number, find the range of values for which 1/3x + ½ > 1/4x
A.x > - 1/6
B.x > 0
C.0 < x < 4
D.0 < x < 1/6""",
"""35.In a basket of fruits, there are 6 grapes, 11 bananas and 13 oranges. If one fruit is chosen at random, what is the probability that the fruit is either a grape or a banana?
A. 17/30
B. 11/30
C. 6/30
D. 5/30""",
"""36.A number is selected at random between 10 and 20, both numbers inclusive. Find the probability that the numbers is an even number.
A.5/11
B. 1/2
C.6/11 
D.7/10"""

    ]
    question=[
          Question(question_prompt[0],'a') ,
          Question(question_prompt[1],'d') ,
          Question(question_prompt[2],'a') ,
          Question(question_prompt[3],'c') ,
          Question(question_prompt[4],'a') ,
          Question(question_prompt[5],'d') ,
          Question(question_prompt[6],'a') ,
          Question(question_prompt[7],'c') ,
          Question(question_prompt[8],'d') ,
          Question(question_prompt[9],'a') ,
          Question(question_prompt[10],'a'),
          Question(question_prompt[11],'b')  ,
          Question(question_prompt[12],'b')  ,
          Question(question_prompt[13],'d')  ,
          Question(question_prompt[14],'d')  ,
          Question(question_prompt[15],'d')  ,
          Question(question_prompt[16],'d')  ,
          Question(question_prompt[17],'b')  ,
          Question(question_prompt[18],'d')  ,
          Question(question_prompt[19],'b')  ,
          Question(question_prompt[20],'c')  ,
          Question(question_prompt[21],'b') ,
          Question(question_prompt[22],'d') ,
          Question(question_prompt[23],'c') ,
          Question(question_prompt[24],'d') ,
           Question(question_prompt[25],'c') ,
           Question(question_prompt[26],'a') ,
          Question(question_prompt[27],'b') ,
          Question(question_prompt[28],'c') ,
          Question(question_prompt[29],'d') ,
          Question(question_prompt[30],'a'),
          Question(question_prompt[31],'a')  ,
          Question(question_prompt[32],'d')  ,
          Question(question_prompt[33],'d')  ,
          Question(question_prompt[34],'a')  ,
          Question(question_prompt[35],'c')
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\ntheanswer is',question.answer,"\n")
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2016():
    question_prompt=["""1.The sum of the first two terms of a geometric progression is x and the sum of the last two terms is y. if there are n terms in all, then the common ratio is
a.x/y
b.y/x
c.(x/y)1/2
d.(y/x)1/2""",
"""2.In DPQR, the bisector of QPR meets QR at S. the line PQ is produced to V and the bisector of VQS meets PS produced at T. if QPR = 460 and QST = 750, calculate QTS
a.41°
b.52°
c.64°
d.82°""",
"""3. If PQR is a straight line with OS = = QR, calculate TPQ, if QT//SRand TQS = 3y°.
a.62°
b.56°
c.20° 3/2
d.18° 2/3""",
"""4. If x : y = 5 : 12 and z = 52cm, find the perimeter of the triangle.
a.68cm
b.84cm
c.100cm
d.120cm""",
"""5.The pilot of an aeroplane, flying 10km above the ground in the direction of a landmark, views the landmark to have angle of depression of350 and 550. find the distance between the two points of observation
a.10(sin 350 – sin 550)
b.10(cos 350 – cos 550)
c.10(tan 350 – tan 550)
d.10(cot 350 – cot 550)""",
"""6.A sin2x – 3 = 0, find x if0 < x < 900
a.30° 
b.45°
c.60°
d.90°""",
"""7.A square tile has side 30cm. How many of these tiles cover a rectangular floor of length 7.2cm and width 4.2m?
a.336
b.420
c.576
d.720""",
"""8.A cylindrical metal pipe 1m long has an outer diameter of 7.2cm and an inner diameter of 2.8cm. find the volume of metal used for the cylinder.
a.440πcm3
b.1,100πcm3
c.4,400πcm3
d.11,000πcm3""",
"""9.OXYZW is a pyramid with a square base such that OX = OY = OZ = OW= 5cm and XY = XW= YZ =WZ = 6cm. Find the height OT.
a.2√5
b.3
c.4√7
d.3√7""",
"""10.In preparing rice cutlets, a cook used 75g of rice, 40g of margarine, 105g of meat and 20g of breadcrumbs. Find the angle of the sector which represents meat in a pie chart.
a.30°
b.60°
c.112.5°
d.157.5°""",
"""11.In a family of 21 people, the average age is 14years. If the age of the grandfather is not counted, the average age drops to 12years. What is the age of the grandfather?
a.35years
b.40years
c.42years
d.54years""",
"""12.If n is the median andm is the mode of the following set of numbers. 2.4,  2.1, 1.6, 2.6, 2.6, 3.7, 2.,1, 2.6, then (n, m) is
a.(2.6, 2.6)
b.(2.5, 2.6)
c.(2.6, 2.5)
d.(2.5, 2.1)""",
"""13.The numbers are chosen at random from three numbers 1,3,6. find the probability that the sum of the two is not odd.
a.2/3
b.½
c.1/3
d.1/6
""","""14.The H.C.F. of a2bx + ab2x and a2b – b3 is
a. b
b. a + b
c. a(a + b)
d. abx (a2 – b2)
""","""15.Correct 241.34 (3 x 10-3)^2 to 4 significant figures
a. 0.0014
b. 0.001448
c. 0.0022
d. 0.002172
""","""16.At what rate would a sum of #100.00 deposited for 5 years raise an interest of #7.50?
a.1 wholeno 1/2%
b.2 whole number 1/2%
c.1.5%
d.25%
""","""17.Three children shared a basket of mangoes in such a way that the first child took ¼ of the mangoes and the second ¾ of the remainder. What fraction of the mangoes did the third child take?
a.3/16
b.7/16
c.9/16
d.13/16
""","""18.Simplify and express in standard form (0.00275 x 0.00640/( 0.025 x 0.08)
a. 8.8 x 10^-1
b. 8.8 x 10^2
c. 8.8 x 10^-3
d. 8.8 x 10^3
""","""19.Three brothers in a business deal share the profit at the end of contract. The first received 1/3 of the profit and the second 2/3 of the remainder. If the third received the remaining #12.000.00, how much profit did they share?
a.#60,000.00
b.#54,000.00
c.#48,000.00
d.#42,000.00
""","""20.Simplify (3Log9 to base 6) + (Log12 to base 6) + (Log64 to base 6) – (Log72 to base 6)
a.5
b.6
c.Log631
d.-5
""","""21.Simplify (1/x-1 + 1/ y-1 )raise to the power -1
a. x/y 
b. xy
c. y/x
d. (xy)-1 
""","""22.If a = 2, b = -2 and c = -1/2, evaluate (ab^2 – bc^2) (a^2c - abc)
a.0 
b.–28
c.–30
d.–34
""","""23.Y varies inversely as x^2 and X varies directly as Z^2. find the relationship between Y and Z, if C is a constant.
a.Z^(2)Y = C
b.Y= CZ^2
c.Y= CZ^2
d.Y= C
""","""24.If f(x - 4) = x^2 + 2x + 3, find f(2)
a.6
b.11
c.27
d.51
""","""25.Factorize 9(x + y)^2 – 4(x - y)^2
a.(x+y) (5x+y)
b.(x+y)^2
c.(x+5y) (5x+y)
d.5(x+y)^2
""","""26.If a^2 + b^2 = 16 and 2ab = 7 find all the possible values of (a – b )
a.3, -3
b.2, -2
c.1, -1
d.3, -1
""","""27.Divide x^3 – 2x^2 – 5x + 6 by (x - 1)
a.x2 – x –6
b.x2 – 5x + 6
c.x2 – 7x + 6
d.x2 – 5x - 6
""","""28.If x + = 4, find the x2 + 1/x
a.16
b.14
c.12
d. 9
""","""29.What must be added to 4x^2 – 4 to make it a perfect square?
a.-1/x^2
b.1/x^2
c.1
d.-1
""","""30.The lengths of the sides of a right-angled triangle are xcm. (3x-1)cm and (3x + 1)cm. Find x
a.5
b.7
c.8
d.12
""","""31.The perimeter of a rectangular lawn is 24m, if the area of the lawn is 35m2, howwide is the lawn?
a.5m
b.7m
c.12m
d.14m
""","""32.Find the sum of the first twenty terms of the arithmetic progression Log a, Log a2, Log a3
a.log a20
b.log a21
c.log a200
d.log a210
""","""33.A carpainter charges #40.00 per day for himself and #10.00 per day for his assistant. If a fleet of a cars were painted for #2,000.00 and the painter worked 10 days more than his assistant, how much did the assistant receive?
a.#32.00
b.#320.00
c.#340
d.#420
""","""34.Find the sum of the first 18 terms of the progression 3, 6,12………..
a.3(2^(17 - 1))
b.3(2^(18)) + 1)
c.3(2^(18 + 1))
d.3(2^(18 - 1))
""","""35.What is the equation of the quadratic function represented by the graph above?
a.y = x^2 + x - 2
b.y = x^2 – x –2
c.y = -x^2 – x + 2
d.y = -x + x + 2
""","""36.At what value of x is the function x^2 + x + 1 minimum?
a.-1 
b.–1/2
c. 1/2
d.3/4
""","""37.The angle of a sector of a circle, radius 10.5cm, is 480. calculate the perimeter of the sector
a.8.8cm
b.25.4cm
c.25.6cm
d.29.8cm
""","""38.In triangle XYZ and XQP, XP = 4cm, XQ= 5cm and PQ = QY= 3cm. Find ZY
a.8cm
b.6cm
c.4cm
d.3cm
""","""39.Find the length of a side of a rhombus whose diagonals are 6cm and 8cm.
a.8cm
b.5cm
c.4cm
d.3cm
""","""40.Each of the interior angles of a regular polygon is 1400. how many sides has the polygon?
a.9
b.8
c.7
d.5"""
    ]
    question=[
          Question(question_prompt[0],'d') ,
          Question(question_prompt[1],'d') ,
          Question(question_prompt[2],'c') ,
          Question(question_prompt[3],'d') ,
          Question(question_prompt[4],'d') ,
          Question(question_prompt[5],'c') ,
          Question(question_prompt[6],'a') ,
          Question(question_prompt[7],'a') ,
          Question(question_prompt[8],'c') ,
          Question(question_prompt[9],'d') ,
          Question(question_prompt[10],'c'),
          Question(question_prompt[11],'b')  ,
          Question(question_prompt[12],'c')  ,
          Question(question_prompt[13],'b')  ,
          Question(question_prompt[14],'d')  ,
          Question(question_prompt[15],'c')  ,
          Question(question_prompt[16],'a')  ,
          Question(question_prompt[17],'c')  ,
          Question(question_prompt[18],'b')  ,
          Question(question_prompt[19],'a')  ,
          Question(question_prompt[20],'a')  ,
          Question(question_prompt[21],'d') ,
          Question(question_prompt[22],'b') ,
          Question(question_prompt[23],'d') ,
          Question(question_prompt[24],'c') ,
           Question(question_prompt[25],'a') ,
           Question(question_prompt[26],'a') ,
          Question(question_prompt[27],'b') ,
          Question(question_prompt[28],'b') ,
          Question(question_prompt[29],'d') ,
          Question(question_prompt[30],'a'),
          Question(question_prompt[31],'d')  ,
          Question(question_prompt[32],'b')  ,
          Question(question_prompt[33],'d')  ,
          Question(question_prompt[34],'b')  ,
          Question(question_prompt[35],'d'),
          Question(question_prompt[36], 'd'),
          Question(question_prompt[37], 'b'),
          Question(question_prompt[38], 'b'),
          Question(question_prompt[39], 'a'),
       ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\nthe answer is',question.answer,"\n")
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
def math_jamb_2009():
    question_prompts=["""[1].A worker’s present salary is #24,000 per annum. His annual increment is 10% of his basic salary.What would be his annual salary at the beginning of the third year?
(a)#28,800
(b)#29,040
(c)#31,200
(d)#31,944
""",
"""[2].Express the product of 0.0014 and 0.011 in standard form.
(a)1.54 x 10^2
(b)1.54 x 10^-3
(c)1.54 x 10^4
(d)1.54 x10^-5
""",
"""[3].Evaluate (81 raise to the power 3/4 - 27 raise to the power 1/3) / (3 x 2 raise to the power3)
[
(a)]27 
(b)1
(c)1/3
(d)1/8
""",
"""[4].Four members of a school first eleven cricket team are also members of the first fourteen rugby team. How many boys play for at least one of the two teams?
(a)25
(b)21
(c)16
(d)3
""",
"""[5]If S = (x : x^2 = 9, x > 4), then S is equal to
(a)0
(b){0} 
(c)empty 
(d){f}
""",
"""[6].If x – 1 and x + 1 are both factors of the equation x^3 + px^3 + qx + 6 = 0, evaluate p and q
(a)–6, -1
(b)6, 1
(c)-1
(d)6, -6
""",
"""[7].Find a positive value of p if the equation 2x^2 – px + p leaves a remainder 6 when added
(a)1
(b)2
(c)3
(d)4
""",
"""[8].Factorize completely the expression abx^2 + 6y – 3ax –2byx
(a)(ax – 2y) (bx - 3)
(b)(bx + 3) (2y - ax)
(c)(bx + 3) (ax – 2y)
(d)(ax – 2y) (ax - b)
""",
"""[9].Solve the following inequality (x - 3) (x - 4) less than or equal to 0
(a)3 less than or equal to x less than or equal to 4 
(b)3 < x < 4
(c)3 £ x < 4
(d)3 < x less than or equal to 4
""",
"""[10].The 4th term of an A.P is 13cm while the 10th term is 31. find the 31st term.
(a)175
(b)85
(c)64
(d)45
""",
"""[11].Simplify x^2 - 1/ x^3 + 2x^2 – x - 2
(a)1/x + 2
(b)x – 1/x + 1
(c)x – 1/x + 2
(d)1/x – 2
""",
"""[12].Express 5x -12/ (x - 2) (x - 3) in partial fraction
(a)2/x – 2 – 3/x –3
(b)2/x – 2 + 3/x – 3
(c)2/x – 3 – 3x –2
(d)5/x – 3 + 4/x – 2
""",
"""[13].Which of the following binary operation is commutative in a set of integers?
(a)a*b = a + 2b
(b)a*b = a + b – ab
(c)a*b = a^2 + b
(d)a*b = a(b + 1) / 2
""",
"""[14].Find the sum to infinity of the following sequence 1, 9/10, (9/10)^2, (9/10)^3
(a)1/10
(b)9/10
(c)10/9
(d)10
""",
"""[15].PT is a tangent to the circle TYZX, YT = YX and < PTX = 50°. calculate <TZY
(a)50°
(b)65°
(c)85°
(d)130°
""",
"""[16].In a triangle XYZ, <YXZ = 44° and <XYZ = 112°. calculate the acute angle between the internal triangle of <XYZ and <XZY.
(a)42°
(b)56°
(c)68°
(d)78°
""",
"""[17].Find the distance between two towns P(450°N, 300°N) and Q(150°S, 300°W) if the radius of the earth is 7,000km.
(a)1100/3km
(b)2200/3km
(c)22000/3km
(d)11000/3km
""",
"""[18].Two perpendicular lines PQ and QR intersect at (1, -1). If the equation of PQ is x – 2y+ 4 = 0, find the equation of QR.
(a)x – 2y + 1 = 0
(b)2x + y – 3 – 0
(c)x – 2y – 3 = 0
(d)2x + y – 1 = 0
""",
"""[19].P is on the locus of a point equidistant form two given pointsX andY. UVis a straight line through Yparallel to the locus. If < PYU is 400 find <XPY
(a)100°
(b)80°
(c)50°
(d)40°
""",
"""[20].A schoolboy lying on the ground 30m away from the foot of a water tank lower observes that the angle of elevation of the top of the tank is 600. Calculate the height of the water tank.
(a)60m
(b)30.3m
(c)20.3m
(d)10.3m
""",
"""[21].QRS is a triangle with QS = 12m, <RQS = 300 and <QRS = 450, calculate the length of RS.
(a)18√2m
(b)12√2m
(c)6√2m
(d)3√2m
""",
"""[22]The derivative of cosecx is
(a)tan x cosec x
(b)– cot x cosec x
(c)tan x sec x
(d)–cot x sec x
""",
"""[23]For what value of x is the tangent o the curve y = x^2 – 4x + 3 parallel to the x – axis?
(a)3
(b)2
(c)1
(d)0
""",
"""[24].Two variables x and y are such that dy/dx = 4x – 3 and y = 5 when x = 2. find y in terms of x
(a)2x^2 – 3x + 5
(b)2x^2 – 3x + 3
(c)2x^2 – 3x
(d)4
""",
"""[25].Find the area bounded by the curve y = 3x^2 – 2x + 1, the coordinates x = 1 and y = 3 and the x - axis
(a)24.
(b)22 
(c)21
(d)20
""",
"""[26].The mean and the range of the set of numbers 0.20,  1.00,  0.90,  1.40,  0.80,  0.80,  1.20,  and 1.10 are m and r respectively. Find m + r
(a)1.11
(b)1.65
(c)1.85
(d)2.45
""",
"""[27].The variance of the scores 1, 2, 3, 4, 5 is
(a)1.2
(b)1.4 
(c)2.0
(d)3.0
""",
"""[28].Let P be a probability function on set S, where S =(a1, a2, a3, a4) find P(a1) if P(a2) = P(a3) = 1/6 and P(a4)1/5
(a)7/10
(b)2/3 
(c)1/3
(d)3/10
""",
"""[29].A die has four of its faces coloured while and the remaining two coloured black .What is the probability that when the die is thrown two consecutive times, the top face will be white in both cases?
(a)2/3
(b)1/9
(c)4/9
(d)1/36
""",
"""[30].If (1PO3)in base 4 = 115in base 10, find P
(a)0
(b)1
(c)2
(d)3
""",
"""[31].Evaluate 64.7642 – 35.2362 correct to 3 significant figures
(a)2960
(b)2950
(c)2860
(d)2850
""",
"""[32].Find the value of (0.006)^3 + (0.004)^3 in standard form.
(a)2.8 X 10^-9
(b)2.8 X 10^-8
(c)2.8 X 10^-7
(d)2.8 X 10^-6
""",
"""[33].Given that loga2 = 0.693 and loga3 = 1.097, find loga13.5
(a)1.404
(b)1.790
(c)2.598
(d)2.790
""",
"""[34].Simplify log96 in base 2 – 2log6 in base 2
(a)2 - log23
(b)3 – log23
(c)log23 – 3
(d)log23 – 2
""",
"""[35].If 8x/2 = [23/8][43/4], find x
(a)3/8 
(b)¾
(c)4/5 
(d)5/4
""",
"""[36].Find the simple interest rate per cent per annum at which #1000 accumulates to #1240 in 3 years.
(a)6%
(b)8%
(c)10%
(d)12%
""",
"""[37].If U = {S, P, L, E, N, D, O, U, R} X = {S, P, E, N, D} Y = {P, N, O, U, R} Find XÇ(Y’UZ).
(a){P, O, U, R}
(b){S, P, D, R}
(c){P, N, D}
(d){N, D, U}
""",
"""[38].A survey of 100 students in an institution shows that 80 students speak Hausa and 20 students Igbo, while only 9 students speaks both languages. How many students neither Hausa nor Igbo?
(a)0 
(b)9
(c)11
(d)20
""",
"""[39].If the function (x) = x3 + 2x2 + qx – 6 is divisible by x + 1, find q.
(a)-5
(b)-2
(c)2
(d)5
""",
"""[40].Solve the simultaneous equations (2/x – 3/y = 2), (4/x + 3/y = 10)
(a)x = 3/2, y = ½
(b)x = ½, y = 3/2
(c)x = -1/2, y = -3/2
(d)x = ½, y = - 3/2
"""]
    questions=[Question(question_prompts[0],"b"),
               Question(question_prompts[1],"d"),
               Question(question_prompts[2], "b"),
               Question(question_prompts[3], "b"),
               Question(question_prompts[4], "c"),
               Question(question_prompts[5], "a"),
               Question(question_prompts[6], "b"),
               Question(question_prompts[7], "a"),
               Question(question_prompts[8], "a"),
               Question(question_prompts[9], "c"),
               Question(question_prompts[10], "a"),
               Question(question_prompts[11], "b"),
               Question(question_prompts[12], "c"),
               Question(question_prompts[13], "d"),
               Question(question_prompts[14], "b"),
               Question(question_prompts[15], "b"),
               Question(question_prompts[16], "c"),
               Question(question_prompts[17], "d"),
               Question(question_prompts[18], "b"),
               Question(question_prompts[19], "b"),
               Question(question_prompts[20], "c"),
               Question(question_prompts[21], "b"),
               Question(question_prompts[22], "b"),
               Question(question_prompts[23], "b"),
               Question(question_prompts[24], "b"),
               Question(question_prompts[25], "b"),
               Question(question_prompts[26], "c"),
               Question(question_prompts[27], "d"),
               Question(question_prompts[28], "c"),
               Question(question_prompts[29], "d"),
               Question(question_prompts[30], "b"),
               Question(question_prompts[31], "c"),
               Question(question_prompts[32], "c"),
               Question(question_prompts[33], "b"),
               Question(question_prompts[34], "a"),
               Question(question_prompts[35], "b"),
               Question(question_prompts[36], "c"),
               Question(question_prompts[37], "b"),
               Question(question_prompts[38], "a"),
               Question(question_prompts[39], "b"),
               ]
    def run_test(questions):
     des={}
     nam=input('type your name here: ')
     score = 0
     option=['a','b','c','d']
     for question in questions:
         answer = input(question.prompt).lower()
         if answer == question.answer :
             score += 2
             print('\ngood job,you got the answer❤👍\n')
         elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
         else:
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
     des.update({nam:(str(score)+'/'+str(len(questions)*2))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(questions)
def  math_jamb_2013():
    question_prompt = [
        """1.A bag contains 4white balls and 6 red balls. Two Red balls are taken from the bag without replacement. What is the probability that they are both red?
        1/3
        2/9
        2/15
        1/
        """,

        """2.Two points X and Y both on latitude 60°S have longitudes 147°E and 153°W respectively. Find to the nearest kilometre the distance between X and Y measured along the parallel of latitudes (Take 2 π R = 4 x 104km, where R is the radius of the earth).
        28850km
        16667km
        8333km
        6667km
        """,

        """3.Evaluate (212)base3 – (121)base3 + (222)base3
        (313) base3
        (1000) base3
        (1020) base3
        1222) base3
        """,

        """4.If Musa scored 75 in Biology instead of 57, his average mark in four subjects would have been 60. what was his total mark?
        282
        240
        222
        210
        """,

        """5.Divide the L.C.M. of 48, 64 and 80 by their H.C.F
        20
        30
        48
        60
        """,

        """6.Find the smallest number by which 252 can be multiplied to obtain a perfect square
        2
        3
        5
        7
        """,

        """7.Find the reciprocal of 2/3 / 1/2 + 1/3
        4/5
        5/4
        2/5
        6/7
        """,

        """ 8.Three boys shared some oranges. The first receive 1/3 of the oranges, the second received 2/3 of the remainder, if the third boy received the remaining 12 oranges. How many oranges did they share?
        60
        54
        48
        42
        """,

        """9. If P = 18, Q = 21, R= -6 and S = -4 calculate (P -Q) + S2
        -11/216
        11/216
        -43/115
        41/116
        """,

        """10.Simplify 0.03 x 4x 0.00064 / 0.48 x 0.012
        3.6x 102
        36 x102
        3.6x 10-3
        3.6x 104
        """,

        """11.Udoh deposited #150 00 in the bank. At the end of 5 years the simple interest on the principal was #55 00. At what rate per annum was the interest paid?
        11%
        7 whole number 1/3%
        5%
        3 whole number 1/2%
        """,

        """12.A number of pencils were shared out among Bisi, Sola and Tunde in the ratio 2:3:5 respectively. If Bisi got 5, how many were shared out?
        15
        25
        30
        50
        """,

        """ 13The ages of Tosan and Isa differ by 6 and the product of their ages is 187. write their ages in the form (x, y), where x > y
        (12, 9)
        (23,17)
        (17,11)
        (18,12)
        """,
        """14.In 1984, Ike was 24 years old and is father was 45 years old in what year was Ike exactly half his father’s age?
        1982
        1981
        1979
        1978
        """,

        """15.Find n if Log2raise to the power of 4 + Log2raise to the power of 7 – Log2raise to the power of n = -1
        10
        14
        27
        28
        """,

        """16.If x varies directly as y3 and x = 2 when y = 1, find x when y = 5
        2
        10
        125
        250
        """,

        """17.Factorize completely. 8a+ 125ax3
        (2a+ 5x2)(4 + 25ax)
        a(2+ 5x)(4 – 10x + 25ax2)
        (2a + 5x)(4 - 10ax +25ax2)
        a(2+ 5x)(4+ 10ax + 2)
        """,
    """If y = x/(x – 3) + x/(x + 4) find ywhen x = -2
    -3/5
    3/5
    –7/5
    7/5
    """,

    """18.Find all the numbers x which satisfy the inequality 1/3(x + 1) – 1 > 1/5 (x + 4)
    x < 11
    x < -1
    x > 6
    x > 11
    """,

    """19.Factorize x^2 + 2a + ax+ 2x
    (x+ 2a)(x +1)
    (x+ 2a)(x - 1)
    (x2 - 1)(x + a)
    (x+ 2)(x +a)
    """,
    """20.Simplify. 1/ 5x +5 + 1/7x + 7
    12/35+7
    1/35(x+1)
    12x/35(x+1)
    12/35x+ 35
    """,

    """21.Factorize (4a + 3)^2 – (3a - 2)^2
    (a + 1)(a + 5)
    (a - 5)(7a - 1)
    (a + 5)(7a + 1)
    a(7a + 1)
    """,

    """22.If 5^(x + 2y) = 5^(x + 3y) = 16, find 3(x +y)
    0
    1
    3
    27
    """,

    """23.Simplify 1/ x - 2  +  1/ x + 2  +  2x / x2 - 4
    2x/ (x-2) (x+2) (x2 - 4)
    2x/x2 - 4
    x/x2 - 4
    4x/ x2 - 4
    """,

    """24.Find the values of x which satisfy the equation 16^x – 5 x (4^(x + 4)) = 0
    1 and 4 
    –2 and 2
    0 and 1
    -1 and 0
    """,
    """25.a/b –c/d = k, find the value of (3a^2 – ac + c^2)/(3b^2 – bd + d^2) in term of k
    3k2
    3k – k2
    17k2/4
    k2
    """,

    """26.At what point does the straight line y = 2x + 1 intersect the curve y = 2x^2 + 5x – 1?
    (-2,-3) and (1/2, 2)
    (-1/2 0) and (2, 5)
    (1/2, 2) and (1, 3)
    (1, 3) and (2, 5)
    """,

    """27.A regular polygon on n sides has 160° as the size each interior. Find n.
    18
    16
    14 
    12
    """,

    """28In the diagram below, PQ and RS are chords of a circle centre O which meet at T outside the circle. If TP = 24cm, TQ= 8cmand TS = 12cm, findTR.
    16cm
    14cm
    12cm
    8cm
    """,


    """29.The angle of elevation of the top of a vertical tower 50 metres high froma point Xon the ground is 300. From a point Y on the opposite side of the tower, the angle of elevation of the top of the tower is 600. find the distance between the points X and Y.
    14.43m
    57.73m
    101.03m
    115.47m
    """,


    """30.A girl walk 45 metres in the direction 050° froma point Q to a point X. She then walks 24 metres in the direction 140° from X to a point Y. Howfar is she then from Q?
    69m
    57m
    51m
    21m
    """,


    """31.An arc of circle of radius 6cm is 8cm long. Find the area ofthe sector.
    51/3cm2
    24cm2
    36cm2
    48cm2
    """,


    """32.PQT is an isosceles. PQ = QT. SRQ = 35°, TQ = 20° and PQR is a straight line. Calculate TSR.
    20°
    55°
    75°
    140°
    """,

    """33If U and V are two distinct fixed points and W is a variable point such that UWV is a straight angle.What is the locus of W?
    The perpendicular bisector ofUV
    A circle with UV as radius
    Aline parallel to the lineUV
    A circle with the line UV as the diameter
    """,

    """34PQ//ST, RS//UV. If PQR = 35° and QRS= 65°, find STV
    30°
    35°
    55°
    65°
    """,

    """35.A man kept 6 black, 5 brown and 7 purple shirts in a drawer.What is the probability of his picking a purple shirt with his eyes closed?
    1/7
    11/18
    7/18
    7/11
    """,

    """36.An open rectangular box externallymeasures 4m x 3m x 4m. find the total cost of painting the box externally if it costs #2.00 to paint one square metre.
    #96.00
    #112.00
    #136.00
    #160.00
    """,

    """37.Find the median of the numbers 89, 141, 130, 161, 120, 131, 131, 100, 108 and 119
    131
    125
    123
    120
    """,

    """38Find the probability that a number selected at random from 40 to 50 is a prime
    3/11
    5/11
    3/10
    4/11
    """,

    """39.Convert 241 in base 5 to base 8
    71 in base 8
    107 in base 8
    176 in base 8
    241 in base 8
    """,
    ]
    question = [
        Question(question_prompt[0], 'a'),
        Question(question_prompt[1], 'b'),
        Question(question_prompt[2], 'c'),
        Question(question_prompt[3], 'c'),
        Question(question_prompt[4], 'd'),
        Question(question_prompt[5], 'd'),
        Question(question_prompt[6], 'b'),
        Question(question_prompt[7], 'b'),
        Question(question_prompt[8], 'b'),
        Question(question_prompt[9], 'c'),
        Question(question_prompt[10], 'b'),
        Question(question_prompt[11], 'b'),
        Question(question_prompt[12], 'c'),
        Question(question_prompt[13], 'b'),
        Question(question_prompt[14], 'b'),
        Question(question_prompt[15], 'd'),
        Question(question_prompt[16], 'a'),
        Question(question_prompt[17], 'd'),
        Question(question_prompt[18], 'b'),
        Question(question_prompt[19], 'b'),
        Question(question_prompt[20], 'c'),
        Question(question_prompt[21], 'b'),
        Question(question_prompt[22], 'b'),
        Question(question_prompt[23], 'd'),
        Question(question_prompt[24], 'd'),
        Question(question_prompt[25], 'c'),
        Question(question_prompt[26], 'a'),
        Question(question_prompt[27], 'd'),
        Question(question_prompt[28], 'd'),
        Question(question_prompt[29], 'c'),
        Question(question_prompt[30], 'b'),
        Question(question_prompt[31], 'b'),
        Question(question_prompt[32], 'c'),
        Question(question_prompt[33], 'd'),
        Question(question_prompt[34], 'a'),
        Question(question_prompt[35], 'a'),
        Question(question_prompt[36], 'd'),
        Question(question_prompt[37], 'c'),
        Question(question_prompt[38], 'a'),
    ]

    def run_test(questions):
        des = {}
        nam = input('type your name here: ')
        score = 0
        option = ['a', 'b', 'c', 'd']
        for question in questions:
            answer = input(question.prompt).lower()
            if answer == question.answer:
                score += 2
                print('\ngood job,you got the answer❤👍\n')
            elif answer not in option:
                print('\nyour answer is not in the option🤦‍♂️🤦‍♂️🤦‍♂️😒\n')
            else:
                print('\nsorry,you failed the question😣😣😦😦😭😢😟\n')
        des.update({nam: (str(score) + '/' + str(len(questions) * 2))})
        print('your profile is', des, '\nyour percentage:', round((score / len(questions)) * 100, 10), '%')
        if score >= 40:
            print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
        else:
            print("\nyou failed the test,go and read your book and try again😭☹👎\n")

    run_test(question)