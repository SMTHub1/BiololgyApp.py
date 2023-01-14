from Question import Question
def English_1982():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        Though Mr. Iro is a new chairman, he views other members with jaundiced eye.
        A. He takes a rather forceful position on dealing with his members
        B. He takes an unfavourable position concerning his members
        C. He takes a sickly view of his members 
        D. He takes a rather hazy view of his members
        \n\n """,
        """1 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        People are not interested in who rules.
        A. People are not ruled by the leaders they want
        B. People are not concerned about who rules them 
        C. The rulers are not concerned about the people
        D. People who rule are not interested in the ruled
        \n\n """,
        """2 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        It was good to steer a middle course in whatever one does.
        A. It is always good to get midway in anything one does
        B. It is always good to act with moderation
        C. It is always good to move away from the forefront
        D. It is always good to work very hard.
        \n\n """,
        """3 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        The witness said he had no axe to grind with his brothers 
        A. He had no hatred for the brothers
        B. He had no axe and therefore stole the matchet
        C. He had no axe and therefore borrowed their matchet
        D. He had no vested interest in the brothers
        \n\n """,
        """4 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        The footballers moved with their tails between their legs.
        A. they moved happily because they won the match 
        B. they were unhappy because they had been despised by their opponents
        C. they were ashamed because they had been defeated
        D. they moved with their tails between their legs.
        \n\n """,
        """5  
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        The headmaster managed to talk his way out of having to give a speech
        A. he delivered a speech despite the difficulty 
        B. he managed to give a speech out of a difficult situation
        C. he managed to get himself out of a difficult situation
        D. he managed to talk on his way.
        \n\n """,
        """6 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks.
        As regards the matter, we have crossed the rubicon
        A. we are completely at a loss
        B. we are irrevocably committed
        C. we are already qualified
        D. we are perfectly committed
        \n\n """,
        """7 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks. 
        Uche is full of himself
        A. He is conceited
        B. He is complete
        C. He is a rich man
        D. He is careful.
        \n\n """,
        """8 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks. 
        As debutants in that tournament, the Super Eagles were up against their first opponents by three goals to nill
        A. The Super Eagles were playing in the tournament for the first time, but they won their match by three goals to nothing
        B. Though the Super Eagles were rated as the weakest side in the tournament, they won their first match by three goals to nill
        C. Even though the Super Eagles were playing without some of their regulars, they won their match by three goals to nill.
        D. As the best attackers in the match, the Super Eagles easily defeated their opponents by three goals to nothing.
        \n\n """,
        """9 
        select the option that best explains the information conveyed in the sentence.  Each question carries 2 marks. 
        The woman was mournful as her husband was found dead drunk
        A. She was sad because of her husband was absolutely drunk
        B. She was apprehensive that her husband would drink again as soon he recovered from the drunken stupor
        C. She was sad because her husband was drunk and always as helpless as a dead man 
        D. She was mourning because her husband drank and died
        \n\n """,
        """10 
        choose the option opposite in meaning to the word or phrase in italics.   
        I am optimistic about the interview though it was a mindbending exercise
        A. An enervating 
        B.A debilitating 
        C.A difficult
        D. An easy
        \n\n """,
        """11 
        choose the option opposite in meaning to the word or phrase in italics.  
        The trader was amused by the cut-throat rush for the goods
        A. Worrisome
        B. Strange
        C. Lacklustre
        D. Mad
        \n\n """,
        """12 
        choose the option opposite in meaning to the word or phrase in italics. 
        The teacher said that Ali’s essay was full of many redundant details
        A. Unexplained 
        B. Strange
        C. Necessary
        D. Useful
        \n\n """,
        """13 
        choose the option opposite in meaning to the word or phrase in italics.
        His father surmounted the myriad of obstacles on his way
        A. Most
        B. Few
        C. All
        D. Many
        \n\n """,
        """14 
        choose the option opposite in meaning to the word or phrase in italics. 
        Her ingenuous smile drew our attention
        A. Witty
        B. Naïve
        C. Clever
        D. Arrogant
        \n\n """,
        """15  
        choose the option opposite in meaning to the word or phrase in italics. 
        Ndeni gave a flawless speech at the party
        A. A wonderful
        B. A careless
        C. An interesting
        D. An imperfect
        \n\n """,
        """16  
        choose the option opposite in meaning to the word or phrase in italics.
        Beneath Ado’s guff exterior, he’s really very kind-hearted
        A. Nice
        B. Harsh
        C. Rough
        D. Gentle
        \n\n """,
        """17 
        choose the option opposite in meaning to the word or phrase in italics.
        The captain says sports is being debased by commercial sponsorship
        A. Localized
        B. Perverted
        C. Elevated
        D. Overvalued
        \n\n """,
        """18 
        choose the option opposite in meaning to the word or phrase in italics. 
        Governing a country is not always as straightforward as people sometimes imagine
        A. Complicated
        B. Troublesome
        C. Untoward
        D. Irksome
        \n\n """,
        """19
        choose the option opposite in meaning to the word or phrase in italics. 
        The crowd was very receptive to the speaker’s suggestion
        A. Disobedient 
        B. Repellent
        C. Alert
        D. Hostile
        \n\n """,
        """20
        choose the option opposite in meaning to the word or phrase in italics.
        There was a general acquiescence on the new drug law
        A. Resistance
        B. Discrepancy
        C. Compromise
        D. Agreement
        \n\n """,
        """21 In each of question 36 to 50, choose the option opposite in meaning to the word or phrase in italics. 
        Aisha seems to feel ambivalent about her future
        A. Decisive
        B. Anxious
        C. Ambitious
        D. Inconsiderate
        \n\n """,
        """22 
        choose the option opposite in meaning to the word or phrase in italics.
        The report of the committee contained a plethora of details
        A. Shortage
        B. Simplicity
        C. Multitude
        D. Spectrum
        \n\n """,
        """23
        choose the option opposite in meaning to the word or phrase in italics.
        The weather was still very heavy and sultry
        A. Wintry and shadowy 
        B. Cold and friendly
        C. Cloudy and thundery 
        D. Hot and uncomfortable
        \n\n """,
        """24
        choose the option opposite in meaning to the word or phrase in italics.
        Ada gave her husband a look that made words superfluous 
        A. Redundant 
        B. Spurious 
        C. Unnecessary 
        D. Scanty
        \n\n """,
        """25
        choose the option nearest in meaning to the word or phrase in italics
        A political Impasse does not offer the best opportunity for merrymaking 
        A. manifesto 
        B. party 
        C. gridlock 
        D. rally
        C. gridlock 
        \n\n """,
        """26
        choose the option nearest in meaning to the word or phrase in italics
        We were all enthusiastic as we awaited the result of the election 
        A. bemused 
        B. agitated
        C. elated 
        D. nervous
        \n\n """,
        """27 
        choose the option nearest in meaning to the word or phrase in italics
        The uniform makes the guards look absurd
        A. dirty 
        B. smart 
        C. sensible 
        D. ridiculous
        \n\n """,
        """28 
        choose the option nearest in meaning to the word or phrase in italics
        The law is often tardy in reacting to changing attitude 
        A. quick 
        B. slow 
        C. exclusive
        D. generous
        \n\n """,
        """29 
        choose the option nearest in meaning to the word or phrase in italics
        Isa and llu ate sumptuous meal on their brother’s wedding day   
        A. expensive 
        B. foreign
        C. insipid 
        D. cheap
        \n\n """,
        """30 
        choose the option nearest in meaning to the word or phrase in italics
        Kaltume crouched over the paper on her desk 
        A. wrote on 
        B. stood on 
        C. walked over 
        D. bent over
        \n\n """,
        """31
        choose the option nearest in meaning to the word or phrase in italics
        The panacea for a country’s economic mess lies in systematic planning and hardwork 
        A. cure 
        B. hope 
        C. foresight 
        D. trouble
        \n\n """,
        """32 
         choose the option nearest in meaning to the word or phrase in italics \n Thousands of workers have been victims of retrenchment since the military came back to power 
        A. Unemployment 
        B. Trench mentality 
        C. Suffering 
        D. Increase in penury
        \n\n """,
        """33 \n choose the option nearest in meaning to the word or phrase in italics \n The principal gave his speech offhand at the sports meeting 
        A. calmly 
        B. beautifully
        C. unconcerned 
        D. unprepared
        \n\n """,
        """34 \nchoose the option nearest in meaning to the word or phrase in italics \n Jankoli was dressed in an old assortment of clothes 
        A. Avalanche 
        B. Homogeneity 
        C. Sameness 
        D. Melange
        \n\n """,
        """35\n choose the option nearest in meaning to the word or phrase in italics \n The girl’s father was astounded to see her appear from the shrine 
        A. collected 
        B. Overwhelmed 
        C. embarrassed 
        D. Astonished
        \n\n """,
        """36 \n choose the option nearest in meaning to the word or phrase in italics \n The director’s remark was extremely apposite to the issue being discussed  
        A. Appropriate 
        B. Inconsequential 
        C. Emphatic 
        D. Adequate
        \n\n """,
        """37 \n choose the option nearest in meaning to the word or phrase in italics  \n Her reputation is without a blemish 
        A. Struggle 
        B. Problem 
        C. Fault 
        D. Blessing
        \n\n """,
        """38 \nchoose the option nearest in meaning to the word or phrase in italics \nUgo is eligible for the post of secretary 
        A. Nominated 
        B. Invited 
        C. Qualified 
        D. Intelligent
        \n\n """,
        """ 39 \n choose the option nearest in meaning to the word or phrase in italics \n This is an abridged version of No Longer at Ease 
        A. An outdated  
        B. An enlarged 
        C. An illustrated 
        D. A shortened
        \n\n """,
        """40 \n choose the option that best completes the gap(s) \n Lemoti……… as a painter, but also as a sculptor 
        A. is a gifted only not 
        B. is only not gifted 
        C. is gifted not only 
        D. is only gifted
        \n\n """,
        """41 \n choose the option that best completes the gap(s) \nHe can recall the important dates in the nation’s history, it is interesting to listen as he rattles ……… 
        A. off 
        B. over 
        C. up 
        D. out
        \n\n """,
        """42 \nchoose the option that best completes the gap(s)  \nThe boy told his mother …….. 
        A. that was the girl he told her about 
        B. that was the girl I told you about her 
        C. that was the girl I told her about
        D. that is the girl he told her bout
        \n\n """,
        """43 \n choose the option that best completes the gap(s) \n Last Monday his father asked me ……..  
        A. if I had come some days before
        B. if I had come the day before 
        C. did you come yesterday 
        D. had I come yesterday
        \n\n """,
        """44 \nchoose the option that best completes the gap(s)  \n His wife was badly injured in the fracas, but I think she will pull …….  
        A. up 
        B. over
        C. through 
        D. back
        \n\n """,
        """45 \n choose the option that best completes the gap(s)  \n A wide range of options …….. made available to students in the final year last year
        A. is  
        B. were 
        C. are 
        D. was
        \n\n """,
        """46 \nchoose the option that best completes the gap(s)  \n One of the women who …….. in the premises ……. been ordered to quit  
        A. sells/have 
        B. sell/has 
        C. sell/have 
        D. sells/has
        \n\n """,
        """47\nchoose the option that best completes the gap(s)  \n The new trade agreement should facilitate………  
        A. more economic rapid growth
        B. economic more rapid growth 
        C. rapid economic more growth 
        D. more rapid economic growth
        \n\n """,
        """48 \nchoose the option that best completes the gap(s)  \n The principal said that he was pleased……… my effort.  
        A. on 
        B. of 
        C. with 
        D. about
        \n\n """,
        """49 \n choose the option that best completes the gap(s)  \n Paper is made……. Wood pulp  
        A. on 
        B. of 
        C. from 
        D. with
        \n\n """,
        """50 \n choose the option that best completes the gap(s)  \n Long after everyone…….. the hall, obi still sat inside. 
        A. left 
        B. is leaving 
        C. has left 
        D. had left
        \n\n """,
        """51 \n choose the option that best completes the gap(s)  \n They are the…….. dresses 
        A. babys’ 
        B. baby
        C. babies 
        D. babies’
        \n\n """,
        """52 \n choose the option that best completes the gap(s)  \n The politician was sent……. Exile 
        A. onto 
        B. into 
        C. on 
        D. to
        \n\n """,
        """53 \n choose the option that best completes the gap(s)  \n When we looked up, we…….. the plane some miles away 
        A. site 
        B. cited 
        C. sited 
        D. sighted
        \n\n """,
        """54 \nchoose the option that best completes the gap(s)  \n Vital….. is still spread….. word of mouth in most villages in Africa 
        A. information/from 
        B. information/with 
        C. information/by
        D. information/through
        \n\n """,
        """55 \nchoose the option that best completes the gap(s)  \n Western education is one of the….. of colonial rule. 
        A. legacies 
        B. evidence 
        C. remnants 
        D. inheritance
        \n\n """,
        """56 \n choose the option that best completes the gap(s)  \n The federal government has…… child trafficking 
        A. postulated 
        B. projected  
        C. prescribed 
        D. proscribed
        \n\n """,
        """57 \nchoose the option that best completes the gap(s)  \n The man was happy that his son confessed his guilt and so the others were…… 
        A. Implicated
        B. accused 
        C. punished 
        D. proscribed
        \n\n """,
        """58 \n choose the option that best completes the gap(s)  \n Based on the facts before me, I have no alternative…… to hold you responsible 
        A. only
        B. as 
        C. than 
        D. but
        \n\n """,
        """58\n choose the option that best completes the gap(s)  \n Many people would always find reasons to……the law 
        A. arrogate 
        B. debase 
        C. circumvent 
        D. circumspect
        \n\n """,
        """59 \n choose the option that has the same Vowel sound as the one \n represented by the letters underlined. 86. Coup
        A. whup 
        B. hoot 
        C. couple 
        D. scout
        \n\n """,
        """60 \n choose the option that has the same Vowel sound as\n  the one represented by the letters underlined.  87. Indict 
        A. bright 
        B. fish 
        C. pick 
        D. brick
        \n\n """,
        """61\n choose the option that has the same Vowel sound as \n the one represented by the letters underlined.  88. Roared 
        A. towered 
        B. coast 
        C. brought 
        D. rod
        \n\n """,
        """ 62\n choose the option that has  the same consonant sound \nas the one represented by letter(s) underlined 89. Sheath
        A. bathe 
        B. length 
        C. months 
        D. paths
        \n\n """,
        """63 \n choose the option that has  the same consonant sound \nas the one represented by letter(s) underlined  90. High  
        A. what 
        B. honest 
        C. who 
        D. vehicle
        \n\n """,
        """64 \nchoose the option that has  the same consonant sound \n as the one represented by letter(s) underlined  91. Of course 
        A. plough 
        B. dough 
        C. over 
        D. orphan
        \n\n """,
        """65 \nchoose the option that rhymes with the given word. "Boys" 
        A. stays 
        B. moist 
        C. noise 
        D. elbows
        \n\n """,
        """66 \nchoose the option that rhymes with the given word. "Shine" 
        A. clean 
        B. fine 
        C. machine 
        D. lain
        \n\n """,
        """67\n choose the option that rhymes with the given word. "Seer"
        A. snare 
        B. spare 
        C. spear 
        D. square
        \n\n """,
        """68 \nchoose the most appropriate stress pattern from the options. \nThe stressed syllables are written in capital letter(s) \n Political 
        A. poliTIcal 
        B. PoLItical  
        C. POlitical
        D. political
        \n\n """,
        """69 \n choose the most appropriate stress pattern from the options.\n The stressed syllables are written in capital letter(s)  \n Satisfactory 
        A. saTISfactory 
        B. satisFACtory
        C. SATisfactory 
        D. satisfactory
        \n\n """,
        """70 \n choose the most appropriate stress pattern from the options. \nThe stressed syllables are written in capital letter(s)  \n captivity 
        A. captiVIty 
        B. CAPtivity 
        C. capTIvity 
        D. CAPtiviTY
        \n\n """,
        """71 \n the word in capital letters has the emphatic. Choose the option to which the given sentence relates \n EMEKA finished his home work yesterday
        A. Was Emeka helped to do his homework?
        B. Did Emeka do his homework? 
        C. When did Emeka finish his homework?
        D. Who finished his home work yesterday?
        \n\n """,
        """72\n the word in capital letters has the emphatic. \nChoose the option to which the given sentence relates  \n Taiwo SAILED to London
        A. Did Taiwo fly to London?
        B. Did Taiwo sail to Brazil?
        C. Did Taiwo sail to London?
        D. Where did Taiwo sail to?
        \n\n """,
        """73 \n the word in capital letters has the emphatic. Choose the option to which the given sentence relates  \n My bag is made of LEATHER
        A. Whose bag is made of leather
        B. Is my bag made of polythene?
        C. Is Abu’s bag made of leather?
        D. Is my bag made of leather?
        \n\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "D"),
        Question(question_prompts[40], "C"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "B"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "D"),
        Question(question_prompts[46], "D"),
        Question(question_prompts[47], "D"),
        Question(question_prompts[48], "C"),
        Question(question_prompts[49], "C"),
        Question(question_prompts[50], "C"),
        Question(question_prompts[51], "D"),
        Question(question_prompts[52], "C"),
        Question(question_prompts[53], "D"),
        Question(question_prompts[54], "C"),
        Question(question_prompts[55], "A"),
        Question(question_prompts[56], "D"),
        Question(question_prompts[57], "D"),
        Question(question_prompts[58], "C"),
        Question(question_prompts[59], "B"),
        Question(question_prompts[60], "A"),
        Question(question_prompts[61], "A"),
        Question(question_prompts[62], "B"),
        Question(question_prompts[63], "C"),
        Question(question_prompts[64], "C"),
        Question(question_prompts[65], "C"),
        Question(question_prompts[66], "B"),
        Question(question_prompts[67], "B"),
        Question(question_prompts[68], "B"),
        Question(question_prompts[69], "B"),
        Question(question_prompts[70], "C"),
        Question(question_prompts[71], "D"),
        Question(question_prompts[72], "A"),
        Question(question_prompts[73], "B"),
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

    run_test(questions)
    while play_again():
        English_1982()
def English_1983():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
            """0. LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information \n conveyed in the sentence. The team’s poor performance at the tournament plumb the depths of horror.
        A. The team’s performance took them to the next round.
        B. The team’s performance was enjoyed by all 
        C. The team’s performance was full of disappointment.
        D. The team’s performance was rewarded.
        \n """,
        """1 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information \n conveyed in the sentence. Tolu and Chinedu live in each other’s pockets.
        A. They are long-term business partners
        B. They steal from each other.
        C. They blackmail each other.
        D. They are very close to each other.
        \n """,
        """2 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information  \nconveyed in the sentence. As the drama unfolded, Olatinuke was advised 
        A. She was advised to wear her shirt
        B. She was advised to commit herself
        C. She was advised to stay calm.
        D. She was advised to join the club.
        \n """,
        """3 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information  \nconveyed in the sentence. He is a clinging child.
        A. He is a handsome young man 
        B. He is possessive
        C. He likes to cling with his sister
        D. He is a bully.
        \n """,
        """4 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information  \nconveyed in the sentence. Zinana’s examination result was not unfavourable.
        A. She failed her examination
        B. Her examination did not meet her expectation.
        C. She was successful in the examination
        D. Her result could not earn her admission.
        \n """,
        """5 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information \n conveyed in the sentence. You need to brush up on your Spanish.
        A. You need to study the history of Spain
        B. You need to improve your skills
        C. You need a brush from Spain
        D. You need to learn to play with a Spainard.
        \n """,
        """6 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information \n conveyed in the sentence. Amaka Would pass for a beauty queen
        A. She would pass the drink to the queen who is sitting next to her.
        B. She would be accepted by all as a beauty queen.
        C. She walked past the beauty queen.
        D. She was acting as a beauty queen.
        \n """,
        """7 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information  \nconveyed in the sentence. ‘I can’t wait to become a mother,’ The new bride declared
        A. She sees motherhood as a burden
        B. She is excited about motherhood
        C. She is not keen on becoming a mother
        D. She will be patient as a mother.
        \n """,
        """8 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains the information \n conveyed in the sentence. Usman needs to get his acts together if he wants to pass the examination. 
        A. He needs to put all points down in the examination
        B. He needs to organize himself. 
        C. He needs to be fast when writing the examination.
        D. He needs to put on his stage costume.
        \n """,
        """9 LEXIS, STRUCTURE AND ORAL FORMS In each of question, select the option that best explains  \nthe information conveyed in the sentence. Ramatu ‘expressed her feelings in no uncertain terms.
        A. She expressed it dearly and strongly.
        B. She expressed it secretly and courageously.
        C. She expressed it quietly and cautiously.
        D. She expressed it feebly and sickly.
        \n """,
        """10 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nChibuzor gave a curt nod and walked away.
        A. gentle.
        B. rude.
        C. polite.
        D. shocking. 
        \n """,
        """11 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe girl took a cursory glance at the letter and hid it.
        A. sententious.
        B. concise.
        C. brief.
        D. lasting.
        \n """,
        """12 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe relationship between the couple has been frosty.
        A. fraudulent.
        B. cordial.
        C. amenable.
        D. frugal.
        \n """,
        """13 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe Nobel laureate’s activity in the field of science is heinous. 
        A. indelible.
        B. laudable.
        C. deplorable.
        D. forgettable.
        \n """,
        """14 In each of question, choose the option opposite in meaning to the word or phrase in italics. The accused was eventually convicted. 
        A. initially.
        B. consequently. 
        C. subsequently.
        D. finally.
        \n """,
        """15 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe plebs can be found in every society of the world.
        A. masses
        B. middle class
        C. elite
        D. politicians
        \n """,
        """16 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nEveryone’s condition was appalling.
        A. simple
        B. cloudy
        C. pleasant
        D. complex
        \n """,
        """17 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe man’s mordant wit is apparent to the entire village.
        A. Kind
        B. scathing
        C. caustic
        D. withering
        \n """,
        """18 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe war against malaria keeps waxing. 
        A. happening
        B. decreasing
        C. increasing
        D. wavering
        \n """,
        """19 In each of question, choose the option opposite in meaning to the word or phrase in italics.  \nThe soldiers tried in their dogged defence of the city.
        A. indifferent
        B. strong
        C. miserable
        D. classical
        \n """,
        """20 choose the option nearest in meaning to the word or phrase in italics.  \nAyodeji is an ardent supporter of education for the girl child.
        A. an optimistic
        B. a cogent
        C. a passionate
        D. an ignorant
        \n """,
        """21 choose the option nearest in meaning to the word or phrase in italics.  \n The scholars’ epitaph was demolished.
        A. monument
        B. embodiment
        C. farmland
        D. book
        \n """,
        """22 choose the option nearest in meaning to the word or phrase in italics.  \nMohammed does his work with so much ardour.
        A. enthusiasm
        B. discouragement
        C. knowledge
        D. indifference
        \n """,
        """23 choose the option nearest in meaning to the word or phrase in italics.  \n The athlete is proud to be in the vanguard of sports development.
        A. unforgettable position
        B. leading position
        C. destructive position
        D. emerging position
        \n """,
        """24 choose the option nearest in meaning to the word or phrase in italics.  \n Nwankwo was on the verge of signing a two-year contract with the club.
        A. shore
        B. brink
        C. summit 
        D. height
        \n """,
        """25 choose the option nearest in meaning to the word or phrase in italics.  \n I am tired of your eternal argument 
        A. open
        B. constant
        C. strong
        D. useless
        \n """,
        """26 choose the option nearest in meaning to the word or phrase in italics. \n  The lamb is a feeble little animal.
        A. fat
        B. quiet
        C. loving
        D. weak
        \n """,
        """27 choose the option nearest in meaning to the word or phrase in italics.  \n The actress screamed when she noticed an object behind her
        A. wailed
        B. protested
        C. waded in
        D. stormed out
        \n """,
        """28 choose the option nearest in meaning to the word or phrase in italics.  \n The exhibition was an eye opener to all.
        A. dispatch
        B. display
        C. style
        D. examination
        \n """,
        """29 choose the option nearest in meaning to the word or phrase in italics.  As a journalist,  \nBala has always had a nose for stories.
        A. soft comment
        B. cynical statement
        C. an instinct
        D. a command
        \n """,
        """30 The girl says she is averse... what others admire.
        A. for
        B. from
        C. to
        D. with
        \n """,
        """ 31 . Our teacher defined... in his introductory
        A. onomatopiea 
        B. onomatopoeia
        C. onomatopoeia
        D. onomatopea
        \n """,
        """32 The philanthropist devoted himself... the poor
        A. to helping
        B. in helping
        C. by helping
        D. to be helping
        \n """,
        """33 Tinu likes apples... she does not like oranges.
        A. or
        B. for
        C. so
        D. but
        \n """,
        """34 The students had a ... on Independence Day.
        A. march past
        B. match pass
        C. marcch pass
        D. match pass
        \n """,
        """35 Do you mind ... another hour or two
        A. to wait
        B. to have waited
        C. wait
        D. waiting
        \n """,
        """36 The continuous rain has really ... the soil.
        A. melted up
        B. mopped up
        C. satiated
        D. saturated
        \n """,
        """37 The police described the boy as being... hand
        A. on by
        B. up to
        C. over at
        D. out of
        \n """,
        """38 It was very easy for the two political parties to form a... government 
        A. co-operative 
        B. colonial
        C. collusion
        D. coalition
        \n """,
        """39 All farmers were encouraged... carry out fumigation on their farms
        A. to
        B. from
        C. in
        D. with
        \n """,
        """40 There are lots of... in the park.
        A. luxury buses moving fast
        B. luxury buses fast moving
        C. moving fast luxury buses
        D. fast-moving luxury buses
        \n """,
        """41  Yours is to command... is to obey
        A. their
        B. theirs
        C. theirs'
        D. their's
        \n """,
        """42 Local governments are authorized to pass ---
        A. bye's-law
        B. bye-law
        C. bye-laws
        D. byes'-laws
        \n """,
        """43 Umar: I have never visited the dentist. Aliyu:___
        A. neither have l
        B. I also never
        C. neither myself
        D. I myself haven't
        \n """,
        """44 Usman would have won the race....
        A. if he had run faster faster
        B. although he ran faster
        C. only if he could run fast
        D. if he had run faster
        \n """,
        """45 My father told me to take the money from....it
        A. ever who offers 
        B. whoever offers
        C. whomever offers
        D. whomsoever offer
        \n """,
        """46 Our teacher defined... as the killing of one's mother.
        A. patriach
        B. matricide
        C. matriarch
        D. patricide
        \n """,
        """47 If you are confused... anything, phone my office.
        A. about
        B. for
        C. of
        D. with
        \n """,
        """48 We have a family mutiny... our hands.
        A. from
        B. of
        C. on
        D. for
        \n """,
        """49 We should try to help... 
        A. the less fortunate
        B. this less fortunate
        C. the less fortunate
        D. less fortunate.
        \n """,
        """50 In each of question, choose the option that has the same vowel sound as the one ran letter(s) in Quote.  \n"glasier" 
        A. gleam 
        B. flat 
        C. feign 
        D. glass
        \n """,
        """51 In each of question, choose the option that has the same vowel sound as the one ran letter(s) in Quote.  \n"laud" 
        A. lavatory 
        B. loud 
        C. lathe 
        D. core
        \n """,
        """52 In each of question, choose the option that has the same vowel sound as the one ran letter(s) in Quote. \n "coma" 
        A. colonel 
        B. cogent 
        C. come  
        D. comma
        \n """,
        """53 In each of questions, choose the option that has the same consonant sound as the one represented by the \n letter(s) in Quote. "lose"
        A. mouse 
        B. nurse 
        C. noise 
        D. horse
        \n """,
        """54 In each of questions, choose the option that has the same consonant sound as the one represented by the  \nletter(s) in Quote. "guitar" 
        A. jam 
        B. strange 
        C. judge 
        D. rogue
        \n """,
        """55 In each of questions, choose the option that has the same consonant sound as the one represented by the  \nletter(s) in Quote. "loose"
        A. sell 
        B. fuse 
        C. close 
        D. rouse 
        \n """,
        """56 In each of question choose the option that rhymes with the given word. "rite" 
        A. list 
        B. wit 
        C. wright 
        D. rim
        \n """,
        """57 In each of question choose the option that rhymes with the given word. "Joys" 
        A. elbow 
        B. pots 
        C. boys 
        D. stays
        \n """,
        """58 In each of question choose the option that rhymes with the given word. "Call" 
        A. wall 
        B. quail 
        C. dull 
        D. slate
        \n """,
        """59 In each of questions choose the most appropriate stress pattern from the  options. The stressed syllables  \nare written in capital letters "dedication" 
        A. dedicaTION 
        B. deDlcation 
        C. dediCAtion 
        D. Dedication
        \n """,
        """60 In each of questions choose the most appropriate stress pattern from the  options. The stressed syllables \n are written in capital letters "international"
        A. interNAtional 
        B. internaTIONal 
        C. INternational 
        D. inTERnational
        \n """,
        """61 In each of questions, choose the most appropriate stress pattern from the  options. The stressed syllables  \nare written in capital letters "information"
        A. inforMAtion 
        B. informaTION
        C. inFORmation 
        D. INformation
        \n """,
        """62 The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates.  \n[Adamu is leaving a CAR behind].
        A. What is Adamu leaving behind?
        B. Is Adamu driving the car in front?
        C. Who is leaving a car behind?
        D. Where is Adamu leaving a car?
        \n """,
        """63 The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n [Lambusa TOOK OFF the wig].
        A. Who took off the wig?
        B. What did Lambusa do?
        C. Did Lambusa take off a wig?
        D. Did Lambusa take off the ring?
        \n """,
        """64 The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n [The bed is IN the room].
        A. Is the bed in the parlour?
        B. Was the bed in the room?
        C. What is in the room?
        D. Where is the bed?
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "B"),
        Question(question_prompts[42], "C"),
        Question(question_prompts[43], "A"),
        Question(question_prompts[44], "D"),
        Question(question_prompts[45], "B"),
        Question(question_prompts[46], "B"),
        Question(question_prompts[47], "A"),
        Question(question_prompts[48], "C"),
        Question(question_prompts[49], "D"),
        Question(question_prompts[50], "D"),
        Question(question_prompts[51], "B"),
        Question(question_prompts[52], "B"),
        Question(question_prompts[53], "C"),
        Question(question_prompts[54], "D"),
        Question(question_prompts[55], "A"),
        Question(question_prompts[56], "C"),
        Question(question_prompts[57], "C"),
        Question(question_prompts[58], "A"),
        Question(question_prompts[59], "C"),
        Question(question_prompts[60], "A"),
        Question(question_prompts[61], "A"),
        Question(question_prompts[62], "A"),
        Question(question_prompts[63], "B"),
        Question(question_prompts[64], "D"),
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

    run_test(questions)
    while play_again():
        English_1983()
def English_1984():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
            """0. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. select the option that best explains \n the information conveyed in the sentence. 26. If he were here, it could be more fun
        (a) He was expected but did not show up to make the occasion lively.
        (b) There was no fun because he was not present.
        (c) He did not show up and so the occasion lacked much fun.
        (d) He was being expected to supply more fun.
        \n """,
        """1. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. The secretary said \n that the postponement of the meeting was due to unforeseen circumstances.
        (a) The date of the meeting was shifted as a result of unexpected reasons.
        (b) The meeting’s date was put off for strange reasons.
        (c) The meeting was called off as a result of obstacles hitherto unknown.
        (d) The meeting broke off as a result of unusual difficulties.
        \n """,
        """2. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. The hunter has a bird’s-eye view of the animals.
        (a) He views the animal from a high position.
        (b) He views the bird’s eye.
        (c) He views the birds on the tree with one eye.
        (d) He watches animals and birds closely.
        \n """,
        """3. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. Even though Susan was the last in the examination,\n  her result wasn’t too different from what had been expected.
        (a) Her result was poor.  
        (b) Her result was a disappointment.
        (c) Her result was as expected.
        (d) She had not been serious with her studies.
        \n """,
        """4. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions.\n  Mrs. Adasu does all her work with more haste, less speed.
        (a) She accepts whatever she does with more haste and speed.
        (b) She approaches whatever she does hurriedly.
        (c) She addresses everything she does very quickly to avoid mistakes.
        (d) She does everything carefully to avoid mistakes.
        \n """,
        """5. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. \n She stopped her education as her uncle left her in the lurch.
        (a) Her uncle deceived her.
        (b) Her uncle disinherited her.
        (c) Her uncle refused to help her
        (d) Her uncle disrespected her
        \n """,
        """6. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. \n The plan to upgrade the dispensary to a general hospital did not materialize.
        (a) The plan did not meet the required specifications.
        (b) The arrangement did not work out as wished.
        (c) It was difficult to obtained the materials.
        (d) The materials purchased ware not the right ones.
        \n """,
        """7. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. Okon’s company took a hit last year.
        (a) His company improved last year.
        (b) His company made a huge success last year.
        (c) His company was badly damaged last year.
        (d) His company was established last year.
        \n """,
        """8. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. My eldest son, who is in Lagos is studying English.
        (a) Only my son is in Lagos studying English.
        (b) My only son is in Lagos studying English.
        (c) One of my son is in Lagos studying English
        (d) My sons are in Lagos but only one is studying English.
        \n """,
        """9. LEXIS, STRUCTURE AND ORAL FORMS  In each of questions. If I went to the village, I would visit the king.
        (a) If I go to the village I will visit the king.
        (b) I did not go to the village and I did not visit the king
        (c) All the times I went to village I also visited the King
        (d) I will visit the king when I go to the village
        \n """,
        """10 choose the option nearest in meaning to the word or phrases in italics. .\n  Since its inception in 1983, the newspaper has attracted thousands of readers. 
        (a) renaissance
        (b) coming
        (c) commencement
        (d) publication
        \n """,
        """11  choose the option nearest in meaning to the word or phrases in italics. .\n  Mrs. Asio wanted her sister to stop being so detached
        (a) friendly
        (b) careless
        (c) indifferent
        (d) passionate
        \n """,
        """12  choose the option nearest in meaning to the word or phrases in italics.  .\n  Lantana dwelt in a ruined cottage on the hillside.
        (a) sat
        (b) worked
        (c) slept
        (d) lived
        \n """,
        """13  choose the option nearest in meaning to the word or phrases in italics.  .\n  The mistake brought the show to an ignominious end
        (a) a good
        (b) a palatable
        (c) a disgraceful
        (d) a satisfactory
        \n """,
        """14  choose the option nearest in meaning to the word or phrases in italics. .\n  He compliments me on my way of doing things.
        (a) complements
        (b) imitates
        (c) disgusts
        (d) praises
        \n """,
        """15  choose the option nearest in meaning to the word or phrases in italics.  .\n  The girl is angry with her friend who had ensnared her into this relationship.
        (a) tricked
        (b) encouraged
        (c) encouraged
        (d) forced
        \n """,
        """16 choose the option nearest in meaning to the word or phrases in italics.  .\n  Their new house was roofedwith corrugated sheets.
        (a) folded
        (b) iron
        (c) aluminium
        (d) corrupted
        \n """,
        """17  choose the option nearest in meaning to the word or phrases in italics. .\n  The stockbroker said it was an astute move to sell the shares then. 
        (a) a bad
        (b) a shrewd
        (c) an unprofitable
        (d) an insincere
        \n """,
        """18  choose the option nearest in meaning to the word or phrases in italics.  .\n  The principal described uche as the most tactful person he had ever worked with.
        (a) passionate
        (b) discrete
        (c) hard-working
        (d) innovate
        \n """,
        """19  choose the option nearest in meaning to the word or phrases in italics. .\n  The old woman is suffering from dementia.
        (a) lucidity
        (b) senility
        (c) insanity
        (d) sagacity
        \n """,
        """20  choose the option nearest in meaning to the word or phrases in italics. .\n  Some drugs have deleterious effect on a child’s development.
        (a) debilitating
        (b) helpful
        (c) harmful
        (d) healing 
        \n """,
        """21 choose the option nearest in meaning to the word or phrases in italics.  . Fila has always described as belligerent.
        (a) beautiful
        (b) attractive
        (c) combative
        (d) innocent
        \n """,
        """22  choose the option nearest in meaning to the word or phrases in italics.\n   . Laraba saw a forlorn little figure sitting outside the class.
        (a) wise and intelligent
        (b) lonely and unhappy
        (c) smart and healthy
        (d) short and ugly
        \n """,
        """23  choose the option nearest in meaning to the word or phrases in italics.  .\n  The circular supersedes all previous correspondence on the matter.
        (a) supports
        (b) displaces
        (c) eliminates
        (d) circumvent
        \n """,
        """24 choose the option nearest in meaning to the word or phrases in italics.   .\n  Her problem was exacerbated by the loss of her father.
        (a) exaggerated 
        (b) solved
        (c) aggravated
        (d) infuriated
        \n """,
        """25  choose the word that is opposite in meaning to the word or phrase in italics  .\n  The warring communities were coerced into negotiation a settlement
        (a) driven
        (b) compelled
        (c) persuaded
        (d) pressured
        \n """,
        """26 choose the word that is opposite in meaning to the word or phrase in italics  .\n  His father served as a mercenary in the army
        (a) preacher
        (b) regular
        (c) recruit
        (d) officer
        \n """,
        """27  choose the word that is opposite in meaning to the word or phrase in italics  .\n  Jummai is cruel to her husband
        (a) harsh
        (b) brutal
        (c) passionate
        (d) ferocious
        \n """,
        """28 choose the word that is opposite in meaning to the word or phrase in italics . \n The teacher who beat the student was treated with mercy
        (a) disrespect
        (b) contempt
        (c) vengeance
        (d) kindness
        \n """,
        """29  choose the word that is opposite in meaning to the word or phrase in italics . \n His wife hated his garrulous attitude.
        (a) outspoken
        (b) unfriendly
        (c) reticent
        (d) thoughtful
        \n """,
        """30  choose the word that is opposite in meaning to the word or phrase in italics .\n  Agoshito is a callow youth; said the teacher
        (a) An ignorant
        (b) An experience
        (c) An idle
        (d) An organized
        \n """,
        """31 choose the word that is opposite in meaning to the word or phrase in italics .\n  What you are asking me to do is a herculean task
        (a) a strenuous
        (b) a demanding
        (c) a lovely
        (d) an easy
        \n """,
        """32 choose the word that is opposite in meaning to the word or phrase in italics  .\n  Nkechi was a novice when she was first employed
        (a) manager
        (b) clerk
        (c) supervisor
        (d) professional
        \n """,
        """33 choose the word that is opposite in meaning to the word or phrase in italics  .\n  ‘I do not trust him ‘he said, in a rare moment of candour
        (a) reproach
        (b) dishonesty
        (c) frankness
        (d) fairness
        \n """,
        """34  choose the word that is opposite in meaning to the word or phrase in italics . \n Mrs Akunilo looks anaemic today
        (a) strange
        (b) sick 
        (c) weak
        (d) strong
        \n """,
        """35  choose the word that is opposite in meaning to the word or phrase in italics .\n  It is inconceivable that the sun shone in the night
        (a) credible
        (b) unthinkable
        (c) impossible
        (d) contestable
        \n """,
        """36 choose the word that is opposite in meaning to the word or phrase in italics  .\n  She only gives a superficial impression of warmth and friendliness
        (a) a strong
        (b) a fake
        (c) a deep
        (d) an unrealistic
        \n """,
        """37 choose the word that is opposite in meaning to the word or phrase in italics  .\n  As a prudent businessman, Adayi does not leave anything to chance
        (a) A frugal
        (b) Shrewd
        (c) careless
        (d) unsuccessful
        \n """,
        """38 choose the word that is opposite in meaning to the word or phrase in italics .\n  His antipathy affected the growth of his business
        (a) hatred
        (b) receptiveness
        (c) loyalty
        (d) hostility
        \n """,
        """39  choose the word that is opposite in meaning to the word or phrase in italics .\n  Okonkwo’s lethal right foot did the magic in the footballmatch
        (a) Weak
        (b) wicked
        (c) fat
        (d) harmless
        \n """,
        """40  choose the option that best complete the gap  .\n  When his car tyre ….. on the way, he did not know what to do
        (a) has burst
        (b) had burst
        (c) bursted
        (d) burst
        \n """,
        """41  choose the option that best complete the gap  . \n Lami’s father …. As a gardener when he was young, but now he is a driver
        (a) had been working
        (b) use to work
        (c) has worked
        (d) used to work
        \n """,
        """42 choose the option that best complete the gap  .\n  ……. He switches on the light,the shadow disappears
        (a)whenever
        (b) except
        (c) since
        (d) until
        \n """,
        """43 choose the option that best complete the gap  . \n It is important that you clear the refuse in front of your houseevery ……
        (a) fourtnight
        (b) fortnight
        (c) fourthnight
        (d) forthnight
        \n """,
        """44 choose the option that best complete the gap  . \n The policemen became suspicious as the hoodlums…… in their office
        (a) ferreted
        (b) ferreted
        (c) ferreted about
        (d) ferreted about
        \n """,
        """45  choose the option that best complete the gap  . Suara needn’t come with us...?
        (a) does she
        (b) will she
        (c) can she
        (d) need she
        \n """,
        """46 ,choose the option that best complete the gap  .\n  Unoka…. the whole house to find his missing wristwatch
        (a) scourged
        (b)scoured
        (c) scored
        (d) scouted
        \n """,
        """47 choose the option that best complete the gap  .\n  Ife asked me….
        (a) what time it was
        (b) what is it by my time
        (c) what time is it
        (d) what time it is
        \n """,
        """48  choose the option that best complete the gap  . \n There are many ways to kill a rat, so we should be …. In our approach to the task ahead of us
        (a) ecletic
        (b) eclectic
        (c) eclektic
        (d) eclectik
        \n """,
        """49 choose the option that best complete the gap \n  . Audu took these action purely…. His own career
        (a) on furtherance of
        (b) in furtherance of
        (c) to furtherance in
        (d) in furtherance with
        \n """,
        """50  choose the option that best complete the gap \n   Here is Mr. Odumusu who teaches English … in our school
        (a) pronuntiation
        (b) pronounciation
        (c) pronunciation
        (d) pronountiation
        \n """,
        """51  choose the option that best complete the gap \n  Instead of… she lied
        (a) pleading
        (b) her to plead
        (c) her pleading
        (d) plead
        \n """,
        """52 choose the option that best complete the gap\n   Of the three girls, Uka is the….
        (a) so much notorious
        (b) notorious
        (c) naught
        (d) naughtiest
        \n """,
        """53  choose the option that best complete the gap\n  I wonder how he will … being absent from school for a long time
        (a) make in
        (b) make up
        (c) make off
        (d) make out
        \n """,
        """54 choose the option that best complete the gap \n  Please sit on the…
        (a) carier
        (b) career
        (c) carrier
        (d) carrear
        \n """,
        """55 choose the option that best complete the gap \n  I want to … his chance to acquaint you with the latest development
        (a) size
        (b) seize
        (c) sieze
        (d) cease
        \n """,
        """56 choose the option that best complete the gap\n   Getting a well-paid job nowadays is on….. task
        (a) utmost
        (b) upbeat
        (c) uphill
        (d) upfield
        \n """,
        """57choose the option that best complete the gap \n The secretary has no right to … my affairs
        (a) spy from
        (b) meddle in
        (c) toy at
        (d) complain into
        \n """,
        """58choose the option that best complete the gap  \n  Bola studiously avoided… the question
        (a) parrying
        (b) answering
        (c) projecting
        (d) destroying
        \n """,
        """59choose the option that best complete the gap  \n  The school authority dismissed him for …. But I won’t tell you about it yet
        (a) certain reason
        (b) a reason
        (c) more reason
        (d) a certain reason
        \n """,
        """60choose the option that has the same vowel sound as the one represented by the letter(s) underlined \n . bubble
        (a) guy
        (b) bull
        (c) bumper
        (d) gurgle
        \n """,
        """61choose the option that has the same vowel sound as the one represented by the letter(s) underlined  \n . Weight
        (a) whale
        (b) while
        (c) wheat
        (d) writhe
        \n """,
        """62choose the option that has the same vowel sound as the one represented by the letter(s) underlined  \n . Leach
        (a) gear
        (b) cedar
        (c) cheer
        (d) death
        \n """,
        """63 choose the option that has the consonant sound as the one represented by the letter(s) underlined \n . mention
        (a) that
        (b) machine
        (c) church
        (d) test
        \n """,
        """64choose the option that has the consonant sound as the one represented by the letter(s) underlined \n . prestige
        (a) bag
        (b) badge
        (c) reggae
        (d) leisure
        \n """,
        """65choose the option that has the consonant sound as the one represented by the letter(s) underlined  \n . knot
        (a) cot
        (b) keep
        (c) norm
        (d) king
        \n """,
        """66choose the option that rhymes with the given word \n . Fuel
        (a) cruel
        (b) fool
        (c) rule
        (d) field
        \n """,
        """67choose the option that rhymes with the given word \n  match
        (a) harsh
        (b) batch
        (c) such
        (d) watch
        \n """,
        """68 choose the option that rhymes with the given word \n . Sheer
        (a) Sheila
        (b) care
        (c) ear
        (d) sherry 
        \n """,
        """69 choose the appropriate stress pattern from the option.The syllables are written in capital letters.\n . Termination
        (a) terminaTION
        (b) TERmination
        (c) termiNAtion
        (d) terMInation
        \n """,
        """70 choose the appropriate stress pattern from the option.The syllables are written in capital letters.  \n . meditative
        (a) meDItative
        (b) mediTAtive
        (c) Meditative
        (d) meditaTIVE
        \n """,
        """71 choose the appropriate stress pattern from the option.The syllables are written in capital letters. \n . Sugestible
        (a) suggeSTIble
        (b) Suggestible
        (c) suGGEstible
        (d) suggestible
        \n """,
        """72 The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates.\n  Uche LOVES Toyota cars
        (a) Who loves Toyota cars?
        (b) What brand of car does Uche love?
        (c) Does Uche hate Toyota cars?
        (d) Does Uche love bicycles?
        \n """,
        """73  The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates.\n  The POLICE arrested the suspect
        (a) Did the police placate the suspect?
        (b) Who arrested the suspect?
        (c) Who did the police arrest?
        (d) Did the police arrest the suspect?
        \n """,
        """74. The word in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n Maiduguri is the CAPITAL of Borno state
        (a) Is Maiduguri the capital of plateau state?
        (b) Which state is Maiduguri the capital of? 
        (c) Is Maiduguri a town in Borno state?
        (d) What is the capital of Borno state?
        \n """,

    ]

    questions = [
            Question(question_prompts[0], "C"),
            Question(question_prompts[1], "A"),
            Question(question_prompts[2], "A"),
            Question(question_prompts[3], "C"),
            Question(question_prompts[4], "D"),
            Question(question_prompts[5], "C"),
            Question(question_prompts[6], "B"),
            Question(question_prompts[7], "B"),
            Question(question_prompts[8], "C"),
            Question(question_prompts[9], "C"),
            Question(question_prompts[10], "C"),
            Question(question_prompts[11], "C"),
            Question(question_prompts[12], "D"),
            Question(question_prompts[13], "C"),
            Question(question_prompts[14], "D"),
            Question(question_prompts[15], "A"),
            Question(question_prompts[16], "B"),
            Question(question_prompts[17], "B"),
            Question(question_prompts[18], "B"),
            Question(question_prompts[19], "B"),
            Question(question_prompts[20], "C"),
            Question(question_prompts[21], "C"),
            Question(question_prompts[22], "B"),
            Question(question_prompts[23], "B"),
            Question(question_prompts[24], "C"),
            Question(question_prompts[25], "C"),
            Question(question_prompts[26], "B"),
            Question(question_prompts[27], "C"),
            Question(question_prompts[28], "C"),
            Question(question_prompts[29], "C"),
            Question(question_prompts[30], "B"),
            Question(question_prompts[31], "D"),
            Question(question_prompts[32], "D"),
            Question(question_prompts[33], "B"),
            Question(question_prompts[34], "D"),
            Question(question_prompts[35], "A"),
            Question(question_prompts[36], "C"),
            Question(question_prompts[37], "C"),
            Question(question_prompts[38], "B"),
            Question(question_prompts[39], "A"),
            Question(question_prompts[40], "D"),
            Question(question_prompts[41], "D"),
            Question(question_prompts[42], "A"),
            Question(question_prompts[43], "B"),
            Question(question_prompts[44], "C"),
            Question(question_prompts[45], "A"),
            Question(question_prompts[46], "B"),
            Question(question_prompts[47], "A"),
            Question(question_prompts[48], "B"),
            Question(question_prompts[49], "B"),
            Question(question_prompts[50], "C"),
            Question(question_prompts[51], "A"),
            Question(question_prompts[52], "D"),
            Question(question_prompts[53], "B"),
            Question(question_prompts[54], "C"),
            Question(question_prompts[55], "B"),
            Question(question_prompts[56], "C"),
            Question(question_prompts[57], "B"),
            Question(question_prompts[58], "B"),
            Question(question_prompts[59], "A"),
            Question(question_prompts[60], "C"),
            Question(question_prompts[61], "C"),
            Question(question_prompts[62], "A"),
            Question(question_prompts[63], "B"),
            Question(question_prompts[64], "D"),
            Question(question_prompts[65], "C"),
            Question(question_prompts[66], "A"),
            Question(question_prompts[67], "B"),
            Question(question_prompts[68], "C"),
            Question(question_prompts[69], "C"),
            Question(question_prompts[70], "C"),
            Question(question_prompts[71], "C"),
            Question(question_prompts[72], "C"),
            Question(question_prompts[73], "B"),
            Question(question_prompts[74], "C"),
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

    run_test(questions)
    while play_again():
        English_1984()
def English_1985():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
                """0. LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the \n information conveyed in the sentence. Each question carries 2 marks 26.\n Hardworking students must not have a finger in very pie at school.
        (a) Hardworking students must not have a role to play in most activities in the school
        (b) Only hardworking students must participate in all activities in the school
        (c) Hardworking students do not participate in all activities in the school
        (d) Hardworking students must ask others to participate in school activities.
        \n """,
        """1 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 27. The vice chancellor is \n riding the crest of the last quarter of his administration.
        (a) The vice chancellor enjoys the acknowledgement of the success of his administration
        (b) The vice chancellor does not enjoy the people’s criticism of his administration
        (c) The vice chancellor hopes to overcome soon, the poor comments on his administration
        (d) The vice chancellor does not talk of his successes on office
        \n """,
        """2 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 28. She was absolved by the course from the charge. 
        (a) She was convicted for the charge
        (b) She was blamed and charged to court
        (c) Her case was resolved by the court
        (d) She was declared free from the charge
        \n """,
        """3 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information\n conveyed in the sentence. Each question carries 2 marks 29. The landlord is fond of throwing his weight about
        (a) The landlord likes healthy exercise
        (b) The landlord is overweight
        (c) The landlord gives orders to people
        (d) The landlord is respected by his tenants 
        \n """,
        """4 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information\n conveyed in the sentence. Each question carries 2 marks 30. The company ought to have issued warrants for one billion shares.
        (a) The company has issued one billion shares
        (b)The management expected the company to issue more than one billion shares
        (c) Members of the company bought less than one billion shares
        (d) The company did not issue one billion shares
        \n """,
        """5 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 31. He needed not to have played in the position of quarterback in the volley ball.
        (a) He participated in the game in his unusual position
        (b) Nobody expected him to have participated in the game
        (c) He wanted to play in a position other than the one he was offered.
        (d) Someone did not want him to play in the position that he played
        \n """,
        """6 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 32. I wouldn’t have responded tohis rude talk, if I were you.
        (a) The advice was taken by the respondent, so he did not respond to the talk
        (b) The adviser put himself in the respondent’s position, so he did not respond to the talk
        (c) The respondent replied to the speaker’s talk, although he ought not have done so
        (d) What was advisable was that the respondent gave it back to the speaker
        \n """,
        """7 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 33. He could not speak out because he had a feet of clay.
        (a) His feet was muddy
        (b) He was weak and cowardly
        (c) He was clumsy and lazy
        (d) He was shy and timid
        \n """,
        """8 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 34. The player wasted a golden opportunity during the penaltyshoot-out.
        (a) The player first the bar 
        (b) The player did not score the shot
        (c) The player scored the shothat made them win the gold cup
        (d) Instead of a silver cup, they received the golden one
        \n """,
        """9 LEXIS, STRUCTURE AND ORAL FORMS In each of question \n, select the option that best explains the information \nconveyed in the sentence. Each question carries 2 marks 35. As far as Abu is concerned Mero should be given fifty naira athe most
        (a) All Abu is saying is that Merprobably deserves more than fiftnaira and not less
        (b) All Abu is concerned with ithat Mero should be given nothinmore than fifty naira
        (c) In Abu’s estimation, Mermerits not more than fifty naira
        (d) In Abu’s opinion, Merdeserves fifty naira or probablmore
        \n """,
        """10 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or phrase \nin italics. 36. As an idiot, the boy is weak in class.
        (a) a deviant
        (b) a dunce
        (c) an expert
        (d) a genius
        \n """,
        """11 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or phrase\n in italics.  37. We were shocked by the news that he had lost the money.
        (a) astonished
        (b) disconcerted
        (c) unconcerned
        (d) surprised
        \n """,
        """12 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  38. The principal was advised to be flexible on critical issues.
        (a) livid
        (b) cautious
        (c) evasive
        (d) rigid
        \n """,
        """13 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  39. Bola always looks sober.
        (a) excited
        (b) serious
        (c) worried
        (d) helpless
        \n """,
        """14 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or\n phrase in italics. 40. Dupe was promoted for her efficiency.
        (a) ability
        (b) incompetence
        (c) inconsistency
        (d) rudeness
        \n """,
        """15 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or\n phrase in italics.  41. The management wants to consider her reticent behaviour in due course.
        (a) disapproving
        (b) disciplinarian
        (c) contemplative
        (d) loquacious
        \n """,
        """16 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  42. Election process often become volatile.
        (a) calm
        (b) strange
        (c) sudden
        (d) latent 
        \n """,
        """17 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or\n phrase in italics.  43.uche entered the principal’s office in a rather abrasive manner.
        (a) gentle
        (b) rude
        (c) lackadaisical
        (d) indifferent
        \n """,
        """18 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or\n phrase in italics.  44. Otokpa is a member of the adhoc committee on stock acquisition.
        (a) improvised
        (b) formal
        (c) temporary
        (d) fact-finding
        \n """,
        """19 (Question 36 to 100 carry mark each.)In each of question\n the option opposite in meaning to the word or \nphrase in italics.  45. His gift to the poor was always infinitesimal.
        (a) large
        (b) small
        (c) supportive
        (d) shameful
        \n """,
        """20 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  46. The economist concluded that several factors have been adduced to explain the fall in the birth rate.
        (a) affirmed
        (b) diffused
        (c) mentioned
        (d) refuted
        \n """,
        """21 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  47. The presidential system is an antidote to some political ailments.
        (a) an answer
        (b) a reply
        (c) an injury
        (d) an obstacle
        \n """,
        """22 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or\n phrase in italics.  48. Ola thought that her father was very callous.
        (a) parlous
        (b) compassionate
        (c) wicked
        (d) cheerful
        \n """,
        """23 (Question 36 to 100 carry mark each.)In each of question \n the option opposite in meaning to the word or \nphrase in italics.  49. He was very much respected,though he had no temporal power.
        (a) spiritual
        (b) mundane
        (c) permanent
        (d) ephemeral
        \n """,
        """24 (Question 36 to 100 carry mark each.)In each of question \n to 50choose the option opposite in meaning to \nthe word or phrase in italics.  50. The way the worship was organized was rather hit-andmiss.
        (a)systematic
        (b)hasty
        (c)slow
        (d)funny
        \n """,
        """25 choose the option nearest in meaning to the word or phrase in italics \n Some men will continue to cause \noffences until they are given a taste of their own medicine.
        (a) placated
        (b) revenged on
        (c) recompensed for
        (d) cured
        \n """,
        """26 choose the option nearest in meaning to the word or phrase in italics \n Okibe was rusticated for hiderogated \nremark about theprincipal
        (a) complimentary
        (b) unsavoury
        (c) unwarranted
        (d) lacklustre
        \n """,
        """27 choose the option nearest in meaning to the word or phrase in italics \n Justice is difficult to enforce because\n people are unwilling toaccept any loss of sovereignty.
        (a) autonomy
        (b) position
        (c) leadership
        (d) kingdom
        \n """,
        """28 choose the option nearest in meaning to the word or phrase in italics \n There are still virtuous women\n in our society today.
        (a) clever
        (b) upright
        (c) devilish
        (d) intelligent
        \n """,
        """29 choose the option nearest in meaning to the word or phrase in italics \n The type of response is typical\n of a lazy teacher.
        (a) symptomatic
        (b) characteristic
        (c) universal
        (d) incontestable
        \n """,
        """30 choose the option nearest in meaning to the word or phrase in italics \n Akin is an inveterate gambler.
        (a) a selfish and self-centred
        (b) an extremely unlucky but popular
        (c) an incurable but fearful
        (d) a long time and incorrigible
        \n """,
        """31 choose the option nearest in meaning to the word or phrase in italics \n  He was too petrified to give the\n closing remarks at the conference.
        (a) frightened
        (b) delighted
        (c) agitated
        (d) happy
        \n """,
        """32 \n choose the option nearest in meaning to the word or phrase in italics \n During a particular time of the day,\n the road shimmers in the heat.
        (a) darkens
        (b) lightens
        (c) shines 
        (d) beams
        \n """,
        """33 choose the option nearest in meaning to the word or phrase in italics \n Every human being is vulnerable to\n communicable diseases.
        (a) liable
        (b) lifted
        (c) immuned
        (d) closed
        \n """,
        """34 choose the option nearest in meaning to the word or phrase in italics \n Mariam looks rather furtive to Shehu.
        (a) intoxicated
        (b) unfriendly
        (c) sad
        (d) sly
        \n """,
        """35 ,choose the option nearest in meaning to the word or phrase in italics \n. The student’s union leader delivered\n his speech extempore.
        (a) out-of-hand
        (b) off the cuff
        (c) accurately
        (d) courageously
        \n """,
        """36 choose the option nearest in meaning to the word or phrase in italics \n. His story gave us an inkling of what\n he passed through during the strike.
        (a) a possible idea
        (b) a taste
        (c) a summary
        (d) the right view
        \n """,
        """37 choose the option nearest in meaning to the word or phrase in italics \n These policies have been expoused by\n the ruling party.
        (a) condemned
        (b) rejected
        (c) supported
        (d) outlined
        \n """,
        """38 choose the option nearest in meaning to the word or phrase in italics \n We must not foreclose reconciliation\n as the purpose of his trip.
        (a) exclude
        (b) consider
        (c) underestimate
        (d) forgo
        \n """,
        """39 choose the option nearest in meaning to the word or phrase in italics \n. Her finding exploded widely held\n beliefs about learning.
        (a) challenged 
        (b) debunked
        (c) projected
        (d) confirmed
        \n """,
        """40 choose the option that best complete the gap(s)\n He was both a writer and a politician,\n but he was better __a singer
        A. as if
        B. like
        C. as 
        D. to be
        \n """,
        """41 choose the option that best complete the gap(s) \n Vacancies in the company will be notified by __
        A. bulletin
        B.publication
        C. publicity  
        D.advertisement
        \n """,
        """42 choose the option that best complete the gap(s) \n The driver was short of petrol,so he __ down the hills\n with the engine switched off.
        A. glided
        B. coasted
        C.wheeled
        D. taxies
        \n """,
        """43 choose the option that best complete the gap(s) \n He started his career as an __ teacher.
        A. auxillary 
        B. auxilliary 
        C.auxilary 
        D. auxiliary
        \n """,
        """44 choose the option that best complete the gap(s) \n His many years of success in legal practice, __didn’t come\n without challenges.
        A. indeed 
        B. but  
        C. in spite of it all 
        D. however
        \n """,
        """45 choose the option that best complete the gap(s)\n One should be careful how__behaves in the public, shouldn’t___?
        A. one/one 
        B. he/he 
        C.she/one 
        D. one/he
        \n """,
        """46 choose the option that best complete the gap(s) \n. __,a good leader must have two characteristics.
        A. First and formost 
        B.First and formust 
        C. First and farmost 
        D. First and foremost
        \n """,
        """47 choose the option that best complete the gap(s)\n We visited his house__three times.
        A.like 
        B. for like 
        C. about 
        D. for about
        \n """,
        """48 choose the option that best complete the gap(s) \n She was__the verge of tears
        A. at
        B. on 
        C. by 
        D. with
        \n """,
        """49 choose the option that best complete the gap(s)\n Everyone makes mistakes occasionally; nobody is__ 
        A.incorrigible 
        B. Imperfect 
        C.Infallible 
        D. indestructible
        \n """,
        """50 choose the option that best complete the gap(s) \n The woman would not part with her__pot
        A. discarded earthen black 
        B. discarded black earthen 
        C. earthen discarded black 
        D.black earthen discarded
        \n """,
        """51 choose the option that best complete the gap(s) \n We stood up when the principal came in__ 
        A. isn’t it 
        B.didn’t we 
        C. not so 
        D. did us
        \n """,
        """52 choose the option that best complete the gap(s)\n The professor of __ medicine has__ the mystery of flu.
        A. vetinary / unraveled 
        B.vertrinary/unravelled 
        C.veterinary/unraveled 
        D.veterinary/unravelled 
        \n """,
        """53 choose the option that best complete the gap(s) \n Her mother brought her some__ 
        A. clothes 
        B. yards 
        C. cloth 
        D.clothing
        \n """,
        """54 choose the option that best complete the gap(s) \n Many workers were__as a result of the textile closure.
        A. laiddown 
        B. laid off 
        C. laid out 
        D. laid up 
        \n """,
        """55 choose the option that best complete the gap(s) \n The driver died in the __ road accident.
        A.fatal 
        B. brutal 
        C. serious 
        D.pathetic
        \n """,
        """56 choose the option that best complete the gap(s) \n. __ your parents frown __ our friendship, we shouldn’t \nsee each other anymore.
        A.Because / over 
        B. Since / at 
        C. Although /at 
        D. As / upon 
        \n """,
        """57 choose the option that best complete the gap(s) \n For more productivity, the company is focusing attention \non the possible___ of available recourses.
        A. synergy
        B.tapping 
        C. alignment 
        D.arrangement 
        \n """,
        """58 choose the option that best complete the gap(s) \n. __ she didn’t trust him, she married him.
        A. After 
        B. Much as 
        C.Since 
        D. Though
        \n """,
        """59 choose the option that best complete the gap(s) \n I wanted to know his political beliefs, so I asked him what __
        A. this was 
        B. these are 
        C. this is 
        D. these were
        \n """,
        """60 choose the option that has the same vowel sound as the one represented by the letter(s) underlined.\n book 
        A. cool  
        B. cook 
        C. fool 
        D. tool
        \n """,
        """61 choose the option that has the same vowel sound as the one represented by\n the letter(s) underlined. \n village 
        A. page 
        B. pig 
        C. made 
        D. came
        \n """,
        """62 choose the option that has the same vowel sound as the one represented\n by the letter(s) underlined. \n patch  
        A. starch 
        B. fare 
        C. mad 
        D. brave
        \n """,
        """63 choose the option that has the same consonant sound as the one represented\n by the letter(s) underlined.\n tangerine
        (a) gear
        (b) danger
        (c) girl 
        (d) ignore
        \n """,
        """64 choose the option that has the same consonant sound as the one represented by\n the letter(s) underlined.\n hair
        (a) heir
        (b) hour
        (c) honest
        (d) house
        \n """,
        """65 choose the option that has the same consonant sound as the one represented\n by the letter(s) underlined. \n edition
        (a) bash
        (b) catch
        (c) bastion
        (d) rating
        \n """,
        """66 choose the appropriate stress pattern from the options. The syllables are written in capital letters.\ndemarcation
        (a) demarCAtion
        (b) DEmarcation
        (c) deMARcation
        (d) demarcaTIOn
        \n """,
        """67 choose the appropriate stress pattern from the options. The syllables are written in capital letters.\n impossible
        (a) imPOSible
        (b) IMposible
        (c) imposSIble
        (d) impossiBLE
        \n """,
        """68 choose the appropriate stress pattern from the options. The syllables are written in capital letters. \n imperialism
        (a) IMperialism
        (b) imPErialism
        (c) impeRIAlism
        (d) imperialiSM
        \n """,
        """69 choose the option that has the stress on the first syllable.\n
        (a). madam
        (b) eighteen
        (c) invent
        (d) command
        \n """,
        """70 choose the option that has the stress on the first syllable.\n 
        (a) nineteen
        (b) mother
        (c) estate
        (d) announce
        \n """,
        """71 choose the option that has the stress on the first syllable.\n 
        (a) commute 
        (b) import (verb)
        (c) intend
        (d) export (noun)
        \n """,
        """72 the word in capital letters has the emphatic stress.Choose the option to which the given sentence relates.\nThe traditional chief NARRATED the story to the children.
        (a) The children heard the story from the traditional chief
        (b) Who narrated the story to the children?
        (c) The children could not listen to the story by the traditional chief
        (d) Did the chief hide the story from the children?
        \n """,
        """73 the word in capital letters has the emphatic stress.Choose the option to which the given sentence relates. \n. The ACCOUNTANT paid the workers’ July salary in September.
        (a) When were the workers paid 
        (b) Did the cashier pay the workers’ salary in September
        (c) Workers received their July salary in September?
        (d) The September salary was paid in July?
        \n """,
        """74 the word in capital letters has the emphatic stress.Choose the option to which the given sentence relates. \n. The cat DEVOURED the rat.
        (a) Did the rat devoured the cat?
        (b) What devoured the rat?
        (c) Did the cat pet the rat?
        (d) Is this the rat the cat devoured?
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "D"),
        Question(question_prompts[40], "C"),
        Question(question_prompts[41], "D"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "D"),
        Question(question_prompts[44], "A"),
        Question(question_prompts[45], "D"),
        Question(question_prompts[46], "D"),
        Question(question_prompts[47], "C"),
        Question(question_prompts[48], "A"),
        Question(question_prompts[49], "C"),
        Question(question_prompts[50], "C"),
        Question(question_prompts[51], "B"),
        Question(question_prompts[52], "D"),
        Question(question_prompts[53], "A"),
        Question(question_prompts[54], "B"),
        Question(question_prompts[55], "A"),
        Question(question_prompts[56], "B"),
        Question(question_prompts[57], "B"),
        Question(question_prompts[58], "D"),
        Question(question_prompts[59], "D"),
        Question(question_prompts[60], "D"),
        Question(question_prompts[61], "B"),
        Question(question_prompts[62], "C"),
        Question(question_prompts[63], "B"),
        Question(question_prompts[64], "D"),
        Question(question_prompts[65], "A"),
        Question(question_prompts[66], "A"),
        Question(question_prompts[67], "A"),
        Question(question_prompts[68], "B"),
        Question(question_prompts[69], "B"),
        Question(question_prompts[70], "B"),
        Question(question_prompts[71], "D"),
        Question(question_prompts[72], "D"),
        Question(question_prompts[73], "B"),
        Question(question_prompts[74], "C"),
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

    run_test(questions)
    while play_again():
        English_1985()
def English_1986():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
        """0. LEXIS, STRUCTURE AND ORAL FORMS.select the option that best explains the information conveyed in the \n sentence. Each question carries 2 marks. 36. The minister considered the ministry’s budget to a drop\n  in the ocean in view of the number of projects in the pipeline.
        A. The amount available may be inadequate for projected expenditure
        B. The minister maybe dropped for failing to complete a number of projects. 
        C. The money approved cannot compete the pipeline project across the ocean.
        D. The pipeline project across the ocean will be abandoned unless budgetary allocation improves
        \n """,
        """1 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in\n  the sentence. Each question carries 2 marks. 37. The police are looking \n for the woman who framed her children out to her neighbours.
        A. The woman and her children are in the habit of working in neighbour’s farm and the police are not well\n  disposed to this.
        B. The police may arrest the woman for allowing her neighbours to take care of her children
        C. The woman may be arrested for allowing her children to be a nuisance to her neighbours
        D. The police wanted remarked for allowing her children to destroy her neighbour’s crops.
        \n """,
        """2 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks. 38 Jummai's father \n remarked that pigs would fly before she passed.
         A. It would be possible to pass only if she worked harder
        B it would never be possible for her to pass
        C. He would have to bribe her teachers to enable her to pass
        D. She would have to cheat in order to pass
        \n """,
        """3 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the \n sentence. Each question carries 2 marks. 39. The president said that he found himself \n between a rock and a hard place when the press said that he had resigned
        A. He dreamt that he was abandoned
        B. He thought that hard places were unsafe
        C. He had a hard decision to make
        D Hard places are dangerous for the president
        \n """,
        """4 LEXIS, STRUCTURE AND ORAL FORMS.  select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks.\n  Kunana is like a bear with a sore head.
        A. He is a bully
        B. He is grumpy
        C. He is ugly 
        D. He is quiet
        \n """,
        """5 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the \n sentence. Each question carries 2 marks. \n . Olu gave his brother a bumpy ride
        A. Olu's brother rode on Olu's back to success.
        B. Olu took his brother on a bumpy road
        C. Olu gave his brother a difficult time
        D. Olu gave his brother a ride in his car
        \n """,
        """6 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks. \n . Adeola dosen't have to go the farm today.
        A. Adeola may go to the farm today if he so wishes
        B. Adeola ought not to have gone to the farm today
        C. Adeola must not go to the farm today
        D. Adeola should not go to the farm today
        \n """,
        """7 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks. \n . My boss asked me to take my eyes off the ball. 
        A. I should stop paying attention to what is most important
        B. I should be focused when I am about stay off football
        C. I should stay off football after sustaining an injury
        D. I should be focused when playing football.
        \n """,
        """8 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks. \n . The robber was hedged in by the people.
        A. The robber was surrounded by the people
        B. The robber was killed by the people
        C. The robber was exposed by the people
        D. The robber was caught by the people
        \n """,
        """9 LEXIS, STRUCTURE AND ORAL FORMS. select the option that best explains the information conveyed in the\n  sentence. Each question carries 2 marks. \n . Many workers are not happy because they live a hand-tomouth life.
        A. They work hard with their hands
        B. They are voracious and avaricious 
        C. They are barely surviving
        D. They have rejected the use of spoons.
        \n """,
        """10  choose the option opposite in meaning to the word or phrase in italics.Prolonged strike action\n  debilitated the industry.
        A. invigorated
        B. isolated
        C. weakened
        D. destroyed
        \n """,
        """11 choose the option opposite in meaning to the word or phrase in italics.One of the students bought\n  a plagiarized copy of the book
        A. a used
        B. an original
        C. a revised
        D. an annotated
        \n """,
        """12 choose the option opposite in meaning to the word or phrase in italics.  The young girl was taken\n  aback by her father's gift of a car.
        A. shocked 
        B. unmoved
        C. surprised
        D. nonplussed
        \n """,
        """13 choose the option opposite in meaning to the word or phrase in italics. Musa is a gifted but\n  erratic player
        A. strong
        B. regular
        C. unpredictable
        D. unstable
        \n """,
        """14  choose the option opposite in meaning to the word or phrase in italics.The lamp shades were \n translucent
        A. opaque
        B. interested
        C. luminous
        D. transparent
        \n """,
        """15  choose the option opposite in meaning to the word or phrase in italics.My niece has an\n  unquenchable thirst for adventure stories.
        A. a spurious
        B. an illegitimate
        C. a reduced
        D. an inextinguishable 
        \n """,
        """16  choose the option opposite in meaning to the word or phrase in italics. Some of my neighbours\n  have an antipathy to dogs.
        A. enmity towards
        B. affection for
        C. acronym for
        D. alarm for
        \n """,
        """17  choose the option opposite in meaning to the word or phrase in italics. The dressmaker-...- unpicked\n  the seam of the shirt
        A. threaded
        B. sewed up
        C. picked up
        D. tore for
        \n """,
        """18  choose the option opposite in meaning to the word or phrase in italics. \n  The testimony of the witness was vague.
        A. disturbing
        B. true
        C. ambiguous
        D. clear
        \n """,
        """19  choose the option opposite in meaning to the word or phrase in italics.  \n As a student, Isa tried communal living for a few years
        A. collective
        B. general 
        C. shared
        D. private.
        \n """,
        """20  choose the option nearest in meaning to the word orphrase in italics.\n  The chairman admires incessant meetings.
        A. unusual
        B. planned
        C. constant
        D. irregular
        \n """,
        """21 choose the option nearest in meaning to the word orphrase in italics. \n  Today's weather is favourable for a game of tennis.
        A. impartial
        B. abnormal
        C. encouraging
        D. disapproving
        \n """,
        """22  choose the option nearest in meaning to the word orphrase in italics. \n  the candidates looked aghast at the first reading of the questions.
        A. fulfilled 
        B. dismayed
        C. satisfied
        D. relaxed
        \n """,
        """23  choose the option nearest in meaning to the word orphrase in italics. \n  Joke gave Muhammed a jaunty smile.
        A. a discouraging
        B. an inviting
        C. a frightful
        D. a cheerful.
        \n """,
        """24 choose the option nearest in meaning to the word orphrase in italics. \n  The first round of the tournament was a doddle.
        A. easy
        B. balanced
        C. dodgy
        D. exasperating
        \n """,
        """25 choose the option nearest in meaning to the word orphrase in italics. \n The lazy man cast a lustful glance at his neighbour's wife.
        A. hateful
        B. quick
        C. covetous
        D. envious
        \n """,
        """26  choose the option nearest in meaning to the word orphrase in italics.\n They accused him of fomenting political unrest.
        A. inciting
        B. discouraging
        C. preventing
        D. guiding.
        \n """,
        """27 choose the option nearest in meaning to the word orphrase in italics.\n You can learn a great deal just from watching other players.
        A. invent
        B. accumulate
        C. allow
        D. discover.
        \n """,
        """28  choose the option nearest in meaning to the word orphrase in italics. \n  All the researchers were asked to garner information on the new viral infection.
        A. collect
        B disseminate
        C. distort
        D. give.
        \n """,
        """29  choose the option nearest in meaning to the word orphrase in italics. \n The dispute between the two countries has resulted in the severing of diplomatic relations 
        A. breaking
        B. securing
        C. swapping
        D. strengthening
        \n """,
        """30 choose the option that best completes the gap \n  The House and The Senate will __ At noon next Wednesday\n  to hear address by the president
        A. convene
        B. adjourn
        C. rise
        D. collude
        \n """,
        """31 choose the option that best completes the gap  \n  At the --- of the century many ways of doing things were introduced.
        A. turn
        B. event
        C. birth
        D. sight
        \n """,
        """32 choose the option that best completes the gap \n  You may have the pencil, but you can't have the ballpoint ... 
        A. either
        B. furthermore
        C. also
        D. as well
        \n """,
        """33 choose the option that best completes the gap \n The president said that the country was not out of the.... yet. 
        A. forest
        B. fog
        C. water
        D. wood
        \n """,
        """34  choose the option that best completes the gap \n He went to the restaurant to enjoy the special.
        A. suite
        B. cuisine
        C. a la carte
        D. chef
        \n """,
        """35   choose the option that best completes the gap \n  The invigilator--- to know how long the examination.... going on.
        A. wanted/has been
        B wants/had been
        C. wants/have been
        D. wanted/had been 
        \n """,
        """36 choose the option that best completes the gap \n The guard spent all the night pacing---
        A. from and to
        B. fro and to
        C. to and from
        D. to and fro
        \n """,
        """37  choose the option that best completes the gap \n  The woman refused to testify.... Her husband
        A. in
        B. at
        C. against
        D. from
        \n """,
        """38 choose the option that best completes the gap \n Abike must have found the very interesting movies quite....
        A. absolving
        B. absorbing
        C. nauseating
        D. perverting
        \n """,
        """39 choose the option that best completes the gap \n The words___ divided between the end of one line.
        A. have been
        B. have being 
        C. has been
        D. has being
        \n """,
        """40  choose the option that best completes the gap \n  Those___ are very beautiful.
        A. flowers of her
        B. flowers of her's
        C. our flower
        D. flowers ours
        \n """,
        """41 choose the option that best completes the gap \n Cooking has never been Jumoke’s---
        A. recital
        B. purview
        C. style
        D. forte
        \n """,
        """42 choose the option that best completes the gap  \n  When the strike is over, there will probably be an increase in wages and a __ increase in prices
        A. sporadic
        B. concordant
        C. concurrent
        D. chronic
        \n """,
        """43 choose the option that best completes the gap \n My mother was—annoyed with me for coming late. 
        A. very
        B. neither
        C. hotly
        D. just
        \n """,
        """44 choose the option that best completes the gap \n The chairman is too much--- an idealist for this government
        A. from
        B. about
        C. of
        D. with
        \n """,
        """45  choose the option that best completes the gap \n  The clock--- 12 O’clock two hours ago.
        A. strikes
        B. strike
        C. struck
        D. striking
        \n """,
        """46 choose the option that best completes the gap\n Whats is the jury’s --- the matter
        A. verdict on
        B. verdict from
        C. verdict at
        D. verdict with.
        \n """,
        """47  choose the option that best completes the gap  \n  The unconscious man was---- after receiving first aid.
        A. reawakened
        B. reformed
        C. restored
        D. revived
        \n """,
        """48  choose the option that best completes the gap \n  The laughter –his face for a moment.
        A. improved
        B. controlled
        C. animated
        D. remade
        \n """,
        """49 choose the option that best completes the gap \n She traced her family history--matrilineal descent.
        A. in
        B. by
        C. with
        D. at.
        \n """,
        """50  choose the option that has the same vowel sound as the one represented by the letter(s) underlined. \n . cOOl
        A. full
        B. luke
        C. look
        D. should
        \n """,
        """51 choose the option that has the same vowel sound as the one represented by the letter(s) underlined. \n  odOUR
        A. flow
        B. sugar
        C. hold
        D. floor
        \n """,
        """52 choose the option that has the same vowel sound as the one represented by the letter(s) underlined.  \n  pALm
        A. ranch
        B. florid
        C. lunch
        D. plait
        \n """,
        """53  choose the option that has the same consonant sound as the one represented by the letter(s) underlined.\n  viSIon 
        A. instruction 
        B. mansion 
        C. nation 
        D. enclosure.
        \n """,
        """54  choose the option that has the same consonant sound as the one represented by the letter(s) underlined. \n  GNash 
        A. forge 
        B. new 
        C. king 
        D. ring
        \n """,
        """55  choose the option that has the same consonant sound as the one represented by the letter(s) underlined. \n  epitaPH
        A. pseudo 
        B. fan 
        C. paper 
        D. pneumonia.
        \n """,
        """56 Choose the option that rhymes with the given word.  ever 
        A. favour 
        B. fever 
        C. never 
        D. heavier
        \n """,
        """57 Choose the option that rhymes with the given word.   keep 
        A. reap 
        B. seethe 
        C. threat 
        D. dead
        \n """,
        """58 Choose the option that rhymes with the given word.  tax 
        A. box 
        B. lacks 
        C. back 
        D. ask
        \n """,
        """59  choose the most appropristress pattern from options. The stressed syllabare written in capital letter.\n   valedictory 
        A. valeDICtory 
        B. valedicTORY 
        C. VAledictory 
        D. vaLEdictory
        \n """,
        """60  choose the most appropristress pattern from options. The stressed syllabare written in capital letter.\n   . congratulation 
         A. congraTUlation 
        B. congratuLAtion 
        C. CONgratulation
        D. conGRAtulation
        \n """,
        """61 choose the most appropristress pattern from options. The stressed syllabare written in capital letter.\n  . conspiracy 
        A. conspiRAcy 
        B. conspiraCY
        C. consPIracy 
        D. CONspiracy
        \n """,
        """62  the world in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n  My mother brought a BICYCLE yesterday.
        A. What did you mother buy yesterday?
        B. Whose mother bought a bicycle yesterday?
        C. Did my mother steal a bicycle yesterday? 
        D. When did my mother buy a bicycle?
        \n """,
        """63 the world in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n  AMINA went to Abuja by air.
        A. Is Amina going to Abuja by air?
        B. Who went to Abuja by air?
        C. Did Amina go to Abuja by road?
        D. Did Amina go to Jos by air?
        \n """,
        """64 the world in capital letters has the emphatic stress. Choose the option to which the given sentence relates. \n   Musa is STAYING in Enugu.
        A. Is Musa passing through Enugu?
        B. Is Musa staying on the outskirt of Enugu?
        C. Is Audu staying in Enugu?
        D. Was Musa staying in Enugu?
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "D"),
        Question(question_prompts[42], "C"),
        Question(question_prompts[43], "A"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "A"),
        Question(question_prompts[47], "D"),
        Question(question_prompts[48], "C"),
        Question(question_prompts[49], "B"),
        Question(question_prompts[50], "A"),
        Question(question_prompts[51], "D"),
        Question(question_prompts[52], "A"),
        Question(question_prompts[53], "D"),
        Question(question_prompts[54], "B"),
        Question(question_prompts[55], "B"),
        Question(question_prompts[56], "C"),
        Question(question_prompts[57], "A"),
        Question(question_prompts[58], "D"),
        Question(question_prompts[59], "A"),
        Question(question_prompts[60], "C"),
        Question(question_prompts[61], "B"),
        Question(question_prompts[62], "A"),
        Question(question_prompts[63], "B"),
        Question(question_prompts[64], "A"),

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

    run_test(questions)
    while play_again():
        English_1986()
def English_1987():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
                    """0. From these questions, select the options that best explain the information conveyed in the sentence.\n Amedu's actions provoked severe criticism
        a. His actions were seriously rejected
        b. His action were severe and accepted
        c. His action were itemized because he was young
        d. His action provoked the humour
        \n """,
        """1 From these questions, select the options that best explain the information conveyed in the sentence. \n I haven't seen the movie and my brother hasn't either
        a. I have seen the movie but neither of my brother have
        b. My brother and I haven't seen the movie
        c. Only my brother has seen the movie
        d. I was the only one that has seen the move
        \n """,
        """2 From these questions, select the options that best explain the information conveyed in the sentence. \n Sule would have been given the car if his father had hot complained.
        A. He wasn't given the car because his father complained
        B. He was given the car because his father complained 
        C. His father complained about the car and he was given.
        D. He was given the car even though his father didn't complain.
        \n """,
        """3 From these questions, select the options that best explain the information conveyed in the sentence.  \n Adayi cannot halt the march of time.
        A. she is willing to march on
        B. She cannot change the way things happen.
        C. She halts the march on time.
        D. She cannot alter the peace march.
        \n """,
        """4 From these questions, select the options that best explain the information conveyed in the sentence.  \n The lecture is Uye s road to Damascus.
        A. The lecture is an opportunity to travel to Damascus.
        B. The lecture is an experience that changes the way she thinks
        C. The lecture talks exclusively about Damascus.
        D. The lecture is an experience that cannot be changed.
        \n """,
        """5 From these questions, select the options that best explain the information conveyed in the sentence.  \n Ado is one of the backwoodsmen. 
        A. He is one of those that live in a distant and underdeveloped area
        B. He is one of the active member of the community
        C. He is one of the honest men that lives in the community
        D. He is one of those that live in the most developed part of the city.
        \n """,
        """6 From these questions, select the options that best explain the information conveyed in the sentence.  \n. Bello said he would pitch his tent with the club.
        A. He would support the club.
        B. He would build a pitch in the club
        C. He would build a tent on the pitch.
        D. He would distance himself from the club.
        \n """,
        """7 From these questions, select the options that best explain the information conveyed in the sentence.  \n Try not to lose heart, said the man.
        A. Try not to be bold and weak
        B. Try not to become sad and hopeless
        C. Try not to be happy and feeble 
        D. Try not to be timid and hopeful.
        \n """,
        """8 From these questions, select the options that best explain the information conveyed in the sentence.  \n. Kasim would have attended the party if he had been invited. 
        A. He would not have attended even if he eat
        B. He attended the party before he was invited.
        C. He was not invited and so, he did not attend
        D. He attended the party without invitation.
        \n """,
        """9 For these questions, choose the option opposite in meaning to the word or phrase in italics \n Adewale's arrival always triggers a media FRENZY
        A. Violence. 
        B. Agitation 
        C. Calm 
        D. Excitement.
        \n """,
        """10 For these questions, choose the option opposite in meaning to the word or phrase in italics \n She said, the experience was HARROWING. 
        A. Educating 
        B. Frightening 
        C. Pleasant 
        D. Strange
        \n """,
        """11 For these questions, choose the option opposite in meaning to the word or phrase in italics \n The house was INVADED by the young officers 
        A. Set up 
        B. Put down 
        C. Defended 
        D. built.
        \n """,
        """12 For these questions, choose the option opposite in meaning to the word or phrase in italics \n I like Adamu WEIRD attitude. 
        A.Buoyant 
        B. Peculiar 
        C. Zestful 
        D. Normal. 
        \n """,
        """13 For these questions, choose the option opposite in meaning to the word or phrase in italics \n We travelled to an OBSCURE little town 
        A. rugged 
        B. Distinguished 
        C. Secluded  
        D. inglorious
        \n """,
        """14 For these questions, choose the option opposite in meaning to the word or phrase in italics \n She is known for her BIZARRE  dressing. 
        A. Natural 
        B. Weird 
        C. Obsolete 
        D. Odious
        \n """,
        """15 For these questions, choose the option opposite in meaning to the word or phrase in italics \n Lami normally SCURRIES around town 
        A. Scampers 
        B. Dashes 
        C. Dawdles 
        D. Scuttles
        \n """,
        """16 For these questions, choose the option opposite in meaning to the word or phrase in italics \n Sule’s poem is always EXPLICIT and compelling 
        A. Exciting 
        B. Clear 
        C. Ambiguous
        D. Long.
        \n """,
        """17 For these questions, choose the option opposite in meaning to the word or phrase in italics \n Usman smiled in a SCORNFUL way 
        A. Respectful 
        B. Derisive 
        C. Sarcastic 
        D. Deluded.
        \n """,
        """18 For these questions, choose the option opposite in meaning to the word or phrase in italics \n Alade is noted for his ERRATIC  behaviour. 
        A. Fitful 
        B. Bizarre 
        C. Consistent 
        D. Euphoric
        \n """,
        """19 For these questions, choose the option opposite in meaning to the word or phrase in italics \n The priest knows Ochai as an ABSTAINER 
        A. Someone who never drinks alcohol 
        B. Someone who holds onto his ideas 
        C. Someone who reads a lot 
        D. Someone who never cares about others
        \n """,
        """20 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n She gave a caustic remark on the occasion
        A. tangible 
        B. Friendly 
        C. insignificant 
        D. Sarcastic.
        \n """,
        """21 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n It was a good try but it didn't quite work out. 
        A. Come to 
        B. come off 
        C. come from 
        D. come for
        \n """,
        """22 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n Garuba’s performances in the competition was horrid. 
        A. terrible 
        B. encouraging 
        C. Commendable 
        D. rigid.
        \n """,
        """23 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n Just me the basic facts with needless details
        A. relevant 
        B. extraneous  
        C. essential 
        D. critical
        \n """,
        """24 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n. Usman likes toys made with bright and animated colours. 
        A. dull 
        B. sparkling 
        C. black
        D. deep
        \n """,
        """25 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n. The man has strong distaste for alcohol. 
        A. love 
        B. aversion 
        C. desire 
        D. excitement.
        \n """,
        """26 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n The schism in the' organization is on the increase. 
        A. disagreement 
        B. understanding 
        C. opportunity
        D. rot
        \n """,
        """27 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n Sule admires people who have unbending character  
        A. mobile 
        B. steady 
        C. wavering 
        D. unstable
        \n """,
        """28 From these questions, choose the option nearest in meaning to the word or phrase in italics. \n. He detests honesty 
        A. likes 
        B. hates 
        C. encourages 
        D. commands.
        \n """,
        """29   choose the option that best completes the gap(s) \n. The number of stores will be increased ... twenty to thirty. 
        A. from 
        B. on 
        C. at 
        D. into
        \n """,
        """30   choose the option that best completes the gap(s) \n. ... bomb had earlier been defused 
        A. A leaf
        B. An alive  
        C. A life 
        D. A live
        \n """,
        """31   choose the option that best completes the gap(s) \n The mechanic did not tell me the brakes ... bad 
        A. were 
        B. are 
        C. is 
        D. was.
        \n """,
        """32   choose the option that best completes the gap(s) \n Tayo could have supplied the goods but it was --- into two 
        A. splitting 
        B. split 
        C. splited
        D. splits.
        \n """,
        """33   choose the option that best completes the gap(s) \n Had Aisha realized what marriage entails she – 
        A. could have not rush into it 
        B. would have rushes into it 
        C. would not have rushes into it
        D. would not have rushed into it.
        \n """,
        """34   choose the option that best completes the gap(s) \n The company deals ... computer software
        A. with 
        B. for 
        C. in 
        D. to.
        \n """,
        """35   choose the option that best completes the gap(s) \n There is no logic --- any of their claims. 
        A. with 
        B. in 
        C. from 
        D. up
        \n """,
        """36   choose the option that best completes the gap(s) \n. ... the house was an easy task for the demolition squad. 
        A. Bringing forth 
        B. Tearing down 
        C. Bringing up 
        D. Tearing with.
        \n """,
        """37  choose the option that best completes the gap(s) \n. The player sat on the bench ... the match lasted. 
        A. since 
        B. when  
        C. that 
        D. while
        \n """,
        """38   choose the option that best completes the gap(s) \n. He ran out when he saw the teacher ...? 
        A. didn't he 
        B. isn't he 
        C. does he 
        D. is he.
        \n """,
        """39 choose the option that best completes the gap(s) \n Parents should be good examples ... their children. 
        A. to 
        B. at 
        C. from 
        D. by.
        \n """,
        """40 choose the option that best completes the gap(s) \n He travelled ... last week 
        A. somewhat 
        B. somewhere 
        C. some at 
        D. somewhere
        \n """,
        """41  choose the option that best completes the gap(s) \n He was present at the party ....? 
        A. wasn't he 
        B. did he 
        C. could he 
        D. didn't he.
        \n """,
        """42   choose the option that best completes the gap(s) \n The prisoners had been ... from all contacts
        A. kept upon 
        B. kept apart 
        C. kept for 
        D. kept on.
        \n """,
        """43  choose the option that best completes the gap(s) \n We detest these... declared the woman 
        A. types of programme 
        B. type of programmes 
        C. types of programmes 
        D. type of programme.
        \n """,
        """44   choose the option that best completes the gap(s) \n lima doesn't like working in the dark ...? 
        A. has she 
        B. does she 
        C. will she 
        D. did she.
        \n """,
        """45   choose the option that best completes the gap(s) \n Oboro will always ... his friends. 
        A. stand up for
        B. stand down for 
        C. stand across for 
        D. stand besides for.
        \n """,
        """46  choose the option that best completes the gap(s)\n She arrived ... air for the occasion. 
        A. for 
        B. in 
        C. with 
        D. by
        \n """,
        """47   choose the option that best completes the gap(s) \n. Audu overbalanced and ... the water. 
        A. fell into 
        B. fell from 
        C. fell for 
        D. fell at.
        \n """,
        """48 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined.\n bORE
        A. call 
        B. curl 
        C. slot 
        D. hum
        \n """,
        """49 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined. 87. HEAd 
        A. said 
        B. heard 
        C. herd 
        D. shirt
        \n """,
        """50 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined.\n SkY
        A. cite 
        B. eats 
        C. breaks 
        D. coil
        \n """,
        """51 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined. \n. LoaTH
        A. breathe 
        B. that 
        C. thaw 
        D. tank
        \n """,
        """52 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined. \n Van  
        A. of 
        B. often 
        C. off 
        D. physics.
        \n """,
        """53 For this question, choose the option that has the same sound as the one represented\n by the letter(s) underlined. \n Lodge 
        A. soldier 
        B. rogue 
        C. go 
        D. measure.
        \n """,
        """54 For this question, choose the option that rhymes with the given word. \n Suite 
        A. tree 
        B. breath 
        C. bleat 
        D. sweet.
        \n """,
        """55 For this question, choose the option that rhymes with the given word. \n Cart 
        A. lash 
        B. cat 
        C. part 
        D. pack. 
        \n """,
        """56 For this question, choose the option that rhymes with the given word. \n. Sight 
        A. skate 
        B. short 
        C. cite 
        D. plait
        \n """,
        """57 For this question, choose the choose the appropriate stress pattern from the options. \nthe stress syllables are written in capital letter(s)  Programmatic 
        A. proGRAMmatic 
        B. PROgrammatic 
        C. programMATIC
        D. programmatIC
        \n """,
        """58 For this question, choose the choose the appropriate stress pattern from the options.\n the stress syllables are written in capital letter(s)  Certification 
        A. certiFIcation 
        B. CERtification 
        C. certifiCAtion 
        D. cerTIfication.
        \n """,
        """59 For this question, choose the choose the appropriate stress pattern from the options.\n the stress syllables are written in capital letter(s) . Motivation 
        A. moTIvation 
        B. motivaTION
        C. motiVAtion 
        D. MOtivation.
        \n """,
        """60 In the question, the words in capital letter has the emphatic stress.\n Choose the option to which the given sentence relates.  . Bukola’s UNCLE is a strict teacher
        A. Is Bukola’s uncles a strict cook?
        B. Is Tunde’s uncle a strict teacher?
        C. Is Bukola’s aunt a strict teacher?
        D. Is Bukola’s uncle an easy going teacher?
        \n """,
        """61 In the question, the words in capital letter has the emphatic stress.\n Choose the option to which the given sentence relates.  . She puts spoon on the CHAIR.
        A. Did she put the fork on the chair?
        B. Did she put the spoon on the chair? 
        C. Who put the spoon on the chair?
        D. Who took the spoon on the chair?
        \n """,
        """62 In the question, the words in capital letter has the emphatic stress.\n Choose the option to which the given sentence relates.  ASA is a lawyer
        A. Is Asa a robber?
        B. Who is a lawyer?
        C.Is Asa the lawyer?
        D. Was Asa the lawyer?
        \n""",

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "B"),
        Question(question_prompts[43], "A"),
        Question(question_prompts[44], "B"),
        Question(question_prompts[45], "A"),
        Question(question_prompts[46], "D"),
        Question(question_prompts[47], "A"),
        Question(question_prompts[48], "C"),
        Question(question_prompts[49], "A"),
        Question(question_prompts[50], "A"),
        Question(question_prompts[51], "C"),
        Question(question_prompts[52], "A"),
        Question(question_prompts[53], "A"),
        Question(question_prompts[54], "D"),
        Question(question_prompts[55], "C"),
        Question(question_prompts[56], "C"),
        Question(question_prompts[57], "C"),
        Question(question_prompts[58], "C"),
        Question(question_prompts[59], "C"),
        Question(question_prompts[60], "C"),
        Question(question_prompts[61], "B"),
        Question(question_prompts[62], "B"),
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

    run_test(questions)
    while play_again():
        English_1987()
def English_1988():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
                    """0. LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the\n information conveyed in the sentence 36. Ramatu expressed her feelings in no uncertain terms 
        (a) she expressed it feebly and sickly 
        (b) she expresses it quietly and cautiously 
        (c) she expressed it secretly and courageously 
        (d) she expressed it clearly and strongly
        \n """,
        """1 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  37. Usman needs to get his act together if he wants to pass the examination 
        (a) he needs to put on his stage costume  
        (b) he needs to be fast when writing the examination 
        (c) he needs to organise himself
        (d) he needs to put all points down in the examination
        \n """,
        """2 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information conveyed in the sentence  38. As the drama unfolded, Olatinuke was advised to keep her shirt on  
        (a) she was advised to stay calm
        (b) she was advised to commit herself 
        (c) she was advised to join the club 
        (d) she was advised to wear her shirt
        \n """,
        """3 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  39. The team's poor performance at the tournament plumbed the depths of horror. 
        (a) the team's performance was rewarded 
        (b) the team's performance took them to the next round 
        (c) the team's performance was enjoyed by all  
        (d) the team's performance was full of disappointment
        \n """,
        """4 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  40. He is a clinging child 
        (a) He is a bully 
        (b) He likes to cling with his sister
        (c) He is possessive 
        (d) He is a handsome young man
        \n """,
        """5 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence 41. You need to brush up on your Spanish 
        (a) you need a brush from Spain
        (b) you need to study the history of Spain 
        (c) you need to learn to play with a Spaniard 
        (d) you need to improve your skills.
        \n """,
        """6 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  42. Tolu and Chinedu live in each other's pockets 
        (a) They are long-term business partners 
        (b) They are very close to each other
        (c) They blackmail each other 
        (d) They steal from each other
        \n """,
        """7 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  43. Zinana'a examination result was not unfavourable 
        (a) She failed her examination
        (b) Her result could not earn her admission 
        (c) She was successful in the examination
        (d) she was deceitful 
        \n """,
        """8 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence  44. can't wait to become a mother. 'the new bride declared 
        (a) she sees motherhood as a burden 
        (b) she will be patient as a mother 
        (c) She is not keen on becoming a mother 
        (d) She is excited about motherhood.
        \n """,
        """9 LEXIS, STRUCTURE AND ORAL FORMS: In these questions, select the option that best explains the information\n conveyed in the sentence 45. Amaka would pass for beauty queen 
        (a) she was acting as a beauty queen  
        (b) she would pass the drink to the queen who is sitting next to her 
        (c) she would be accepted by all as a beauty queen 
        (d) she walked past the beauty queen
        \n """,
        """10 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 46. The relationship between the couple has been frosty 
        (a) amenable 
        (b) fraudulent 
        (c) frugal 
        (d) cordial
        \n """,
        """11 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 47. The dressmaker unpicked the seam of the shirt 
        (a) tore up 
        (b) sewed up 
        (c) threaded
        (d) picked up 
        \n """,
        """12 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 48. Some of my neighbours have an antipathy to dogs 
        (a) enmity towards 
        (b) alarm for 
        (c) acronym 
        (d) affection for
        \n """,
        """13 For these questions, choose the option opposite in meaning to the word or phrase in italics \n49. Chibuzor gave a curt nod and walked away 
        (a) rude 
        (b) polite 
        (c) gentle 
        (d) shocking
        \n """,
        """14 For these questions, choose the option opposite in meaning to the word or phrase in italics \n50. The girl took a cursory glance at the letter and hid it 
        (a) brief 
        (b) sententious 
        (c) lasting 
        (d) concise
        \n """,
        """15 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 51. The accused was eventually convicted 
        (a) initially 
        (b) finally  
        (c) subsequently 
        (d) consequently
        \n """,
        """16 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 52. My niece has an unquenchable thirst for adventure stories 
        (a) an illegitimate 
        (b) a spurious 
        (c) an inextinguishable 
        (d) a reduced
        \n """,
        """17 For these questions, choose the option opposite in meaning to the word or phrase in italics \n53. Musa is a gifted but erratic player 
        (a) regular 
        (b) strong 
        (c) unstable 
        (d) unpredictable
        \n """,
        """18 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 54. The testimony of the witness was vague
        (a) real 
        (b) factual 
        (c) true 
        (d) clear
        \n """,
        """19 For these questions, choose the option opposite in meaning to the word or phrase in italics\n  55. As a student, Isa tried communal living for a few years 
        (a) shared 
        (b) private 
        (c) collective 
        (d) general
        \n """,
        """20 For these questions, choose the option opposite in meaning to the word or phrase in italics\n 56. The lamb is a feeble little animal 
        (a) fat
        (b) weak 
        (c) loving 
        (d) quite
        \n """,
        """21 For these questions, choose the nearest in meaning to the word or phrase in italics\n 57. The chairman admires incessant meetings 
        (a) planned 
        (b) unusual 
        (c) irregular
        (d) constant
        \n """,
        """22 For these questions, choose the nearest in meaning to the word or phrase in italics\n  58. The exhibition was an eye opener to all 
        (a) dispatch 
        (b) examination 
        (c) style 
        (d) display
        \n """,
        """23 For these questions, choose the nearest in meaning to the word or phrase in italics\n  59. The first round of the tournament was a doddle 
        (a) exasperating 
        (b) balanced 
        (c) dodgy
        (d) easy
        \n """,
        """24 For these questions, choose the nearest in meaning to the word or phrase in italics \n 60. As a journalist, Bala has always had a nose for stories 
        (a) a command 
        (b) cynical statement 
        (c) soft comment 
        (d) an instinct
        \n """,
        """25 For these questions, choose the nearest in meaning to the word or phrase in italics \n 61. The actress screamed when she noticed an object behind her 
        (a) wailed 
        (b) protested 
        (c) waded in 
        (d) stormed out
        \n """,
        """26 For these questions, choose the nearest in meaning to the word or phrase in italics\n  62. Today's weather is favourable for a game of tennis 
        (a) impartial 
        (b) abnormal 
        (c) encouraging 
        (d) disapproving
        \n """,
        """27 For these questions, choose the nearest in meaning to the word or phrase in italics\n  63. All the candidates looked aghast at the first reading of the questions 
        (a) fulfilled 
        (b) dismayed 
        (c) satisfied 
        (d) again
        \n """,
        """28 For these questions, choose the nearest in meaning to the word or phrase in italics\n  64. I am tired of your eternal argument 
        (a) open 
        (b) strong 
        (c) constant 
        (d) useless
        \n """,
        """29 For these questions, choose the nearest in meaning to the word or phrase in italics\n  65. Joke gave Muhammad a jaunty smile 
        (a) frightful 
        (B) cheerful 
        (c) discouraging 
        (d) Inviting
        \n """,
        """30 From questions 65 to 85, choose the option that best completes the gap(s)\n 66. You live in the city now, __ ? 
        (a) are you
        (b) don't you 
        (c) didn't you 
        (d) haven't you
        \n """,
        """31 From questions 65 to 85, choose the option that best completes the gap(s)\n 67. Concrete is made of __ 
        (a) sand and cement 
        (b) a sand and a cement 
        (c) sand and a cement 
        (d) a sand and cement
        \n """,
        """32 From questions 65 to 85, choose the option that best completes the gap(s)\n 68. Suana___ that hexagons had five sides, but later he knew they were six-sided figures. 
        (a) would have believed 
        (b) had believed 
        (c) believes 
        (d) has believed
        \n """,
        """33 From questions 65 to 85, choose the option that best completes the gap(s)\n 69. The___ to the fallen heroes was erected at the market square 
        (a) exhibition 
        (b) monument 
        (c) myth
        (d) picture
        \n """,
        """34 From questions 65 to 85, choose the option that best completes the gap(s)\n 70. The Flying Eagles of Nigeria couldn't have won the match if they hadn't prepared well,___? 
        (a) can't they 
        (b) couldn't they 
        (c) could they 
        (d) can they
        \n """,
        """35 From questions 65 to 85, choose the option that best completes the gap(s)\n 71. They all gathered to exhume the___musician's corpse for examination 
        (a) posthumous 
        (b) post-mortem 
        (c) post-natal  
        (d) orthopaedic
        \n """,
        """36 From questions 65 to 85, choose the option that best completes the gap(s)\n 72. I have been doing this exercise___ 
        (a) for five minutes 
        (b) five minutes ago 
        (c) since five minutes 
        (d) during five minutes
        \n """,
        """37 From questions 65 to 85, choose the option that best completes the gap(s)\n 73. Oloyede always sleeps like a baby,___ ?
        (a) does he 
        (b) could he 
        (c) doesn't he 
        (d) did he
        \n """,
        """38 From questions 65 to 85, choose the option that best completes the gap(s)\n 74. The man was given degree despite the fact that he did not attend a___ university 
        (a an honorary 
        (b) an honourable 
        (c) a ceremonial 
        (d) a ceremonious
        \n """,
        """39 From questions 65 to 85, choose the option that best completes the gap(s)\n 75. My father has just bought___ 
        (a) a peugeot brand new car 
        (b) a car brand new peugeot 
        (c) a new brand peugeot car 
        (d) a brand new peugeot
        \n """,
        """40 From questions 65 to 85, choose the option that best completes the gap(s)\n 76. The university is a corporate body made___ different colleges 
        (a) in with 
        (b) of with 
        (c) up of 
        (d) up from
        \n """,
        """41 From questions 65 to 85, choose the option that best completes the gap(s)\n 77. The secretary hadn't___ money left. 
        (a) any 
        (b) anything 
        (c) none 
        (d) no
        \n """,
        """42 From questions 65 to 85, choose the option that best completes the gap(s)\n 78. The King was recognised___ the scar on his face. 
        (a) with 
        (b) to 
        (c) by 
        (d) for 
        \n """,
        """43 From questions 65 to 85, choose the option that best completes the gap(s)\n 79. Nkiru has lots of friends, but I have___
        (a) only a little 
        (b) little 
        (c) only a few 
        (d) few
        \n """,
        """44 From questions 65 to 85, choose the option that best completes the gap(s)\n 80. The HOD says she considers her degree certificate___ than as a prize through labour
        (a) rather as a gift of God 
        (b) rather God as a gift 
        (c) as a gift rather of God 
        (d) as a rather gift of God
        \n """,
        """45 From questions 65 to 85, choose the option that best completes the gap(s)\n 81. Mr Ojo instructed his son to replace the faulty___ tube 
        (a) flurescent 
        (b) flourescent 
        (c) fluorescent 
        (d) florescent
        \n """,
        """46 From questions 65 to 85, choose the option that best completes the gap(s)\n 82. The employer, not the salesmen___responsible for the loss 
        (a) have been 
        (b) was 
        (c) were 
        (d) will be
        \n """,
        """47 From questions 65 to 85, choose the option that best completes the gap(s) \n83. She was___ as anyone could have had 
        (a) as patient as teacher 
        (b) as a patient a teacher
        (c) as patient teacher 
        (d) a patient a teacher
        \n """,
        """48 From questions 65 to 85, choose the option that best completes the gap(s) \n84. There was a serious___ between the new couple over feeding allowance 
        (a) arguement
        (b) argeument 
        (c) arguement 
        (d) argument
        \n """,
        """49 From questions 65 to 85, choose the option that best completes the gap(s)\n 85. They thought Musa___ agree if they altered some of the conditions 
        (a) can 
        (b) may
        (c) might  
        (d) ought
        \n """,
        """50 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 86. WAIter 
        (a) flavour 
        (b) cite 
        (c) road 
        (d) hair
        \n """,
        """51 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 87. FlEE
        (a) field 
        (b) skate 
        (c) faith 
        (d) rid
        \n """,
        """52 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 88. PALm 
        (a) florid 
        (b) ranch 
        (c) blunt 
        (d) lunch
        \n """,
        """53 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 89. Phantom  
        (a) physics 
        (b) pew 
        (c) phew 
        (d) party
        \n """,
        """54 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 90. Chest 
        (a) fixture 
        (b) school 
        (c) charisma
        (d) mass
        \n """,
        """55 For these questions, choose the option that has the same sound as the one represented\n by the letter(s) underlined 91. Epitaph 
        (a) pneumonia 
        (b) fan 
        (c) paper
        (d) pseudo
        \n """,
        """56 For these questions, choose the option that rhymes with the given word 92. Ever 
        (a) never 
        (b) heavier 
        (c) fever 
        (d) favour 
        \n """,
        """57 For these questions, choose the option that rhymes with the given word 93. Cable 
        (a) bible 
        (b) mabel 
        (c) able 
        (d) marble
        \n """,
        """58 For these questions, choose the option that rhymes with the given word 94. Mail 
        (a) bale 
        (b) slate 
        (c) girl 
        (d) galle
        \n """,
        """59 For these questions, choose the appropriate stress pattern from the options, the stress\n syllables are written in capital letter(s) 95. Advantages 
        (a) advantaGES 
        (b) adVANtages 
        (c) ADvantages 
        (d) advanTAges
        \n """,
        """60 For these questions, choose the appropriate stress pattern from the options, the stress\n syllables are written in capital letter(s)  96. Intentional 
        (a) inTENtional 
        (b) INtentional
        (c) intentionAL 
        (d) intentioNAL
        \n """,
        """61 For this question, choose the option that is stressed on the first syllable 97. 
        (a) guitar 
        (b) guilty 
        (c) confuse 
        (d) relief
        \n """,
        """62 In the question, the words in capital letter has the emphatic stress. Choose the option to which the\n given sentence relates. 98. I left my bag on the TABLE
        (a) Is the bag left under the table?
        (b) Did I leave the shoe on the table?
        (c) Who left the bag on the table?
        (d) Where did I leave the bag?
        \n """,
        """63 In the question, the words in capital letter has the emphatic stress. Choose the option to which the\n given sentence relates.  99. Kanu can play FOOTBALL
        (a) Who can play football?
        (b) What can Kanu play?
        (c) What can Kanu do with football?
        (d) Why should Kanu play football?
        \n """,
        """64 In the question, the words in capital letter has the emphatic stress. Choose the option to which the \ngiven sentence relates.  100. Aisha plays TENNIS always
        (a) Who plays tennis always?
        (b) Does Aisha watch tennisalways?
        (c) What does Aisha play always?
        (d) When does Aisha play tennis?
        \n """,

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
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "B"),
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
        Question(question_prompts[41], "A"),
        Question(question_prompts[42], "C"),
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
        Question(question_prompts[54], "A"),
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

    run_test(questions)
    while play_again():
        English_1988()
def English_1989():
    def play_again():
        response =input("do you want to take the quiz again? (type yes or no)")
        response= response.upper()
        if response=="YES":
            return True
        else:
            return False

    question_prompts = [
                        """0 For this question, select the option that best explains the information conveyed in the \n sentences 26. The government didn't mind my mentioning his name
        (a) He was not angry when I mentioned his name
        (b) He was angry when I mentioned his name
        (c) He told me not to mention his name
        (d) He forgot to mention his name to me
        \n """,
        """1 For this question, select the option that best explains the information conveyed in the sentences  \n 27. The leader said he was not unaware of the plight of the people
        (a) He knew of their plight
        (b) He was not informed of their plight
        (c) He could not understand their plight
        (d) He felt their plight
        \n """,
        """2 For this question, select the option that best explains the information conveyed in the sentences \n  28. But for the expense, I'd buy bigger car
        (a) I want to buy a bigger car because it is more expensive
        (b) I will not buy bigger car because it is too expensive
        (c) I would buy a bigger car if I had more money 
        (d) I would like to buy a bigger car if it was not so expensive
        \n """,
        """3 For this question, select the option that best explains the information conveyed in the sentences \n  29. No sooner had he got into the pool than the telephone rang
        (a) He didn't get into the pool because the telephone rang
        (b) The telephone rang just after he got into the pool
        (c) The telephone rang as he was getting into the pool
        (d) The telephone rang before he got into the pool
        \n """,
        """4 For this question, select the option that best explains the information conveyed in the sentences \n  30. My father said I might just as well stay at home for another year
        (a) I should stay at home because I had no other choice
        (b) I might stay at home and do well 
        (c) Staying at home was probably the best thing for me
        (d) I ought to stay at home in order to do well
        \n """,
        """5 For this question, choose the option opposite in meaning to the word or phrase in italics.\n  31. The King's security men relegated to the east 
        (a) discharge from 
        (b) known in 
        (c) accepted in 
        (d) hated by
        \n """,
        """6 For this question, select the option that best explains the information conveyed in the sentences \n  32. The minister averred his commitment 
        (a) denied 
        (b) pledged 
        (C) undertook 
        (d) accented
        \n """,
        """7 For this question, select the option that best explains the information conveyed in the sentences \n  33. The company was on the brink of a financial abyss. 
        (a) difficult 
        (b) scandal 
        (c) services 
        (d) stability
        \n """,
        """8 For this question, select the option that best explains the information conveyed in the sentences \n  34. Nosa is indisposed  
        (a) anxious 
        (b) fragile
        (c) healthy 
        (d) cautious
        \n """,
        """9 For this question, select the option that best explains the information conveyed in the sentences \n  35. A conscientious student should not receive a reward 
        (a) An irresponsible 
        (b) A persistent
        (c) busy 
        (d) An active
        \n """,
        """10 For this question, select the option that best explains the information conveyed in the sentences \n  36. The poem appealed to my sixth sense 
        (a) brain 
        (b) mind 
        (c) instinct 
        (c) intelligence
        \n """,
        """11 For this question, select the option that best explains the information conveyed in the sentences \n  37. Sophie anticipated the celebration of her tenth birthday 
        (a) suggested 
        (b) hoped for 
        (c) imagined 
        (d) waited for
        \n """,
        """12 For this question, select the option that best explains the information conveyed in the sentences \n  38. Mr. Bola is an irascible young man 
        (a) a weak 
        (b) a crabbed 
        (c) a hilarious 
        (d) a rude
        \n """,
        """13 For this question, select the option that best explains the information conveyed in the sentences \n  39. She became neurotic as a result of her performance 
        (a) balanced 
        (b) disturbed 
        (c) rational 
        (d) excited
        \n """,
        """14 For this question, select the option that best explains the information conveyed in the sentences \n  40. Malam Aliyu lived in lack 
        (a) surplus 
        (b) penury 
        (c) plenitude 
        (d) opulence
        \n """,
        """15 For this question, choose the option that best completes the gap(s). \n 41. You have to ...... how to make the whole week a memorable one 
        (a) thick up 
        (b) thick on 
        (c) thick about 
        (d) think at
        \n """,
        """16 For this question, select the option that best explains the information conveyed in the sentences \n  42. Last week I ........ your friend in the salon 
        (a) came into 
        (b) came by 
        (c) came across 
        (d) came over
        \n """,
        """17 For this question, select the option that best explains the information conveyed in the sentences \n  43. We might wait a little longer, but he would not it ..... soon 
        (a) turn out 
        (b) turn up 
        (c) turn in 
        (d) turn over
        \n """,
        """18 For this question, select the option that best explains the information conveyed in the sentences \n  44. His are tied, so he could not do anything to help her 
        (a) shoulders 
        (b) arms 
        (c) hands 
        (d) legs
        \n """,
        """19 For this question, select the option that best explains the information conveyed in the sentences \n   45. If you want to be part of the conference, you have to ...... a form on me 
        (a) fill up 
        (b) fill out 
        (c) fill on 
        (d) fill over
        \n """,
        """20 For this question, select the option that best explains the information conveyed in the sentences\n   46. The flight..... has been postponed 
        (a) schedule 
        (b) timetable 
        (c) menu \n 
        (d) manifest
        \n """,
        """21 For this question, select the option that best explains the information conveyed in the sentences \n  47. My wife should not worry about this trial, I will always .... her 
        (a) stand for 
        (b) stand by
        (c) stand on 
        (d) stand over
        \n """,
        """22 For this question, select the option that best explains the information conveyed in the sentences \n  48. I can tell from the way he talks that he ....... his mentor  
        (a) takes after 
        (b) takes up 
        (c) takes from 
        (d) takes back
        \n """,
        """23 For this question, select the option that best explains the information conveyed in the sentences\n   49. We have time to -- before the gallery opens
        (a) Make 
        (b) waste 
        (c) conserve 
        (d) keep
        \n """,
        """24 For this question, select the option that best explains the information conveyed in the sentences \n  50. The time has now come ....... policy change in Nigeria 
        (a) to 
        (b) for 
        (c) by 
        (d) at
        \n """,
        """25 For this question, choose the option that has the same sound as the one represented by the letter(s)\n  underlined 51. tolerAted 
        (a) stale  
        (b) kneel 
        (c) met 
        (d) mat
        \n """,
        """26 For this question, choose the option that has the same sound as the one represented by the letter(s)\n  underlined  52. gEARbox 
        (a) bare 
        (b) feature
        (c) beer 
        (d) teacher
        \n """,
        """27 For this question, choose the option that has the same sound as the one represented by the letter(s)\n  underlined  53. confuSIon  
        (a) measure 
        (b) mission 
        (c) correction 
        (d) caution
        \n """,
        """28 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined \n  54. terTiary 
        (a) shame 
        (b) question 
        (c) catch
        (d) chair
        \n """,
        """29 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined\n   55. pOster 
        (a) jotter 
        (b) counter  
        (c) heater
        (d) motor
        \n """,
        """30 For this question, choose the option that has the same sound as the one represented by the letter(s) underlined\n   56. cOWed 
        (a) low
        (b) flow 
        (c) loud 
        (d)cooed
        \n """,
        """31 distribution 
        (a) distriBUtion 
        (b) DIStribution
        (c) disTRIbution 
        (d) distribution’
        \n """,
        """32. irrevocable
        (a) irreVOcable
        (b) Irrecocable
        (c) iRREvocable 
        (d) irrevocaBLE
        \n """,
        """33 My house is ACROSS the road
        (a) is her house the road?
        (b) Is my room across the road?
        (c) Is my house on the road? 
        (d) Is my house across the street?
        \n """,
        """34 The shop closes AT 4pm
        (a) Does the shop close by 4pm?
        (b)Does the shop opens at 4pm?
        (c) Does the stall close at 4pm?
        (d) Does a shop close at 4pm?
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "A"),
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

    run_test(questions)
    while play_again():
        English_1989()
def English_1990():
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
            """0 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 23. When asked to state her side of the story, Bunmi started by beating about the bush. This means that Bunmi
        A. went straight to the point
        B. was lost in great thought
        C. followed a bush path
        D. approached the subject without coming to the point.
        \n """,
        """1 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 24. The amount he donated was small. He said it was his widow's mite. This means that
        A. he was a widow
        B. he was misery.
        C. it was all he could honestly afford
        D. he could have given more.
        \n """,
        """2 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 25. The friendship between Segun and Shehu has turned sour. This means that Segun and Shehu are
        A. no longer friends 
        B. stilt friends 
        C. better friends now  
        D. getting to understand each other.
        \n """,
        """3 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 26. The driver smelled a rat when the policemen asked him to stop. This means that the driver was 
        A. reckless 
        B. suspicious 
        C. careful 
        D. offensive.
        \n """,
        """4 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 27. The students were as advised to face their studies and let the sleeping dog lie. This means that the students should
        A. obey the authorities 
        B. suspicious 
        C. inexperienced
        D. uncivilised.
        \n """,
        """5 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 28. From the way Ngozi behaves, it is obvious she is a greenhorn. This means that Ngozi is
        A. arrogant
        B. cautious 
        C.inexperienced 
        D. uncivilised 
        \n """,
        """6 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence.\n  29. The economic situation is so bad that many wage earners are hardly able to make both ends meet. This means that
        A. people's income exceed their expenditure
        B. most people are extravagant with their income
        C. people's earnings are not sufficient for their essential needs
        D. most people engage in activities that bring them extra pay.
        \n """,
        """7 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence.\n  30. Since I found out his hypocritical nature, I have been keeping him at arm's length. This means that I
        A. avoid being similar with him
        B. ignore his advice
        C. report him to the authority
        D). stop visiting him.
        \n """,
        """8 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence. \n 31. I knew Okoronkwo's father very well and I must say that his son is a chip off the old block. Thy means that Okoronkwo
        A. has Chosen the game career as its father
        B. is very much like his father
        C. is a I extremely different sort of person from his lather.
        D. has taken up a different profession from his father's.
        \n """,
        """9 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence.\n  32. The debating team was warned to make convincing points and not to play to the gallery. This means that the team should not
        A. be selfish
        B. underrate opponents
        C. be over-confident
        D. attempt to win cheap popularity.
        \n """,
        """10 After each of the following sentences, a list of possible interpretations of the sentence is given.\n Choose the interpretation that you consider appropriate for each sentence.\n  33. Anyone who thinks that he can succeed in life without working hard is living in a fool's paradise. This means is that such a person
        A. is having an illusion
        B. thinks other people are fools
        C. thinks hat working is merely a joke.
        D. is on the verge of insanity.
        \n """,
        """11 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 34. I am happy to inform you that your boys are conscientious
        A. industrious
        B. carefree
        C. careful
        D. corrupt
        \n """,
        """12 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 35. My father is a very prosperous businessman.
        A. ungrateful
        B. unscrupulous
        C. unskilled
        D. unsuccessful 
        \n """,
        """13 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 36 My hostess greeted her guest in a very relaxed manner
        A. energetic
        B. athletic
        C. stiff
        D. perplexed
        \n """,
        """14 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 37. Ayo takes his studies rather lightly
        A. humorously
        B. tediously
        C. carefully
        D. seriously
        \n """,
        """15 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 38. The doctor was very gentle with his patients in the examining room
        A. harsh
        B. rude
        C. rough
        D. unkind
        \n """,
        """16 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 39. The President took exception to the ignoble role the young man played in the matter
        A. honourable
        B. embarrassing
        C dishonourable
        D. extraordinary
        \n """,
        """17 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 40. The man who had been seriously ill was convalescing at a seaside resort
        A. regaining health
        B. deteriorating in health
        C. recuperating
        D. relaxing
        \n """,
        """18 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 41. For millions of years, the world resources have remained boundless
        A. unlimited
        B. scarce
        C. indomitable
        D. limited
        \n """,
        """19 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 42. The difference between the experimental procedures was imperceptible to me
        A. negligible
        B. significant 
        C. obvious
        D. obscure
        \n """,
        """20 From these questions, choose the options opposite in meaning to the words or phrases in italics.\n 43. His anti-apathy to religion ideas makes him unpopular
        A. remedy
        B. Consciousness
        C. hostility
        D. receptiveness
        \n """,
        """21 For the questions, choose the options that best complete the gap(s). 44, He was ...\n [A. assisted B.duped C. enjoined D. encouraged]... by the trickster.
        A. assisted 
        B.duped 
        C. enjoined
        D. encouraged
        \n """,
        """22 For the questions, choose the options that best complete the gap(s). 45. When the soldiers saw that \nresistance was ... [A. inadequate B. inefficient C. futile D. successful] ..., they stopped fighting
        A. inadequate
        B. inefficient
        C. futile 
        D. successful
        \n """,
        """23 For the questions, choose the options that best complete the gap(s). 46. You should read all the ... \n[A.brochures B. prospectus C. tickets D. handouts] ... carefully before you decide where to go on holiday.
        A.brochures 
        B. prospectus 
        C. tickets 
        D. handouts
        \n """,
        """24 For the questions, choose the options that best complete the gap(s). 47. The Emir and Conqueror of the enemy territories. ---\n[A.arrives B. are to arrive C. arrive D. are arriving] --- next week.
        A.arrives
        B. are to arrive
        C. arrive 
        D. are arriving
        \n """,
        """25 For the questions, choose the options that best complete the gap(s). 48 We ought to have visited the Governor, ...\n[A. isn't it B, oughtn't we C. shouldn't we D. haven't]
        A. isn't it 
        B, oughtn't we
        C. shouldn't we
        D. haven't
        \n """,
        """26 For the questions, choose the options that best complete the gap(s). \n49. He didn't sense Obi's presence in the room, did he?... [A. yes, he did B. No, he did C. Yes, he didn't D. No, he didn't]
        A. yes, he did 
        B. No, he did 
        C. Yes, he didn't 
        D. No, he didn't
        \n """,
        """27 For the questions, choose the options that best complete the gap(s).\n 50. You can stay here --- [A. as long B. so long C. in a much D. for as long] --- as you are quiet.
        A. as long 
        B. so long 
        C. in a much 
        D. for as long
        \n """,
        """28 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n51. The witness averred that she had seen Dosun at the scene of the crime  
        A. argued 
        B. confirmed 
        C. denied 
        D. affirmed
        \n """,
        """29 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n 52. The high cost of living these days calls for a lot of frugality 
        A. extravagance 
        B. economy 
        C. recklessness 
        D. prudence.
        \n """,
        """30 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics.\n  53. Tunde's reaction underscoresthe points I was making. 
        A. justifies 
        B. summarizes 
        C. emphasizes 
        D. clarifies
        \n """,
        """31 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n 54. Everyone admired themanager's adroit handling of thecrisis in the company 
        A. emphasised 
        B. skilful 
        C. tactless 
        D. clumsy 
        \n """,
        """32 In each of these questions, choose the option nearest in meaning to the word(s) or phrase in italics. \n 55. The principal took exception to the ignoble role the teacher plays d in the matter 
        A. embarrassing 
        B. honourable 
        C. extraordinary
        D. dishonourable
        \n """,
        """33 In each of these questions, choose the option that has the same sound as the one represented by the letter(s)\n underlined. 56. key
        A. sit 
        B. bet 
        C seat 
        D. tread
        \n """,
        """34 In each of these questions, choose the option that has the same sound as the one represented by the letter(s)\n underlined.  57. taught 
        A. law 
        B. aunt 
        C. count 
        D. plateau
        \n """,
        """35 In each of these questions, choose the appropriate stress item from the options. The syllables are written\n in capital letters. 58. comfortable 
        A. COMfortable 
        B. comFORtable 
        C. comfortaBLE 
        D. comforTABLE
        \n """,
        """36 In each of these questions, choose the appropriate stress item from the options. The syllables are written\n in capital letters. 59. incapacitate 
        A. inCApacitate 
        B. incaPAcitate
        C. INcapacitate 
        D. incapaciTATE.
        \n """,
        """37 In each of these questions, choose the appropriate stress item from the options. The syllables are written\n in capital letters.  60. encouragement 
        A. Encouragement 
        B. encouragement
        C. encouRAgement 
        D. encouragement 
        \n """,

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
        English_1990()

