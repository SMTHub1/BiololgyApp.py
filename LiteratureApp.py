from Question import Question
def Literature_2016():
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
        """0 based on General Literary Principles.  A ballad is meant to be
         acted
         sung
         discussed
         read
        \n """,
        """1 based on General Literary Principles.  In drama, dramaturge is he who
         writes or edits plays
         feature in a play
         directs a play
         acts a film.
        \n """,
        """2 based on General Literary Principles.  Travelogue is a work of art written
         by a famous playwright
         before the death of the author
          by an unpopular novelist
         on a journey
        \n """,
        """3 based on General Literary Principles.  Plays are basically meant to
          change the world
          keep people out of trouble
          be ready for pleasure
          be presented on stage
        \n """,
        """4 based on General Literary Principles.  A character who re-enacts familiar experiences that Leaders easily identify with is
         round character
          flat character
         stock character
         static character
        \n """,
        """5 based on General Literary Principles. The plot of a story generally refers to the
          intrigue made by a character against the hero
          way the writer ends the story
          keep people out of trouble
          way in which the events of the story are organised
        \n """,
        """6 based on General Literary Principles. The metric pattern in a line of poetry with five stressed and five unstressed syllables is
         trochaic decametre
         dactylic metre
         iambic pentameter
         anapaestic metre
        \n """,
        """7 based on literary Appreciation.  Theseus: Now, fairHippolyta, our nuptial hour. Draws on space four happy days bring in. Another moon. But 0, me thinks how slow This old moon wanes, she lingers my desires, Like to a step-dame or a dowager, Long withering out a young man's revenue. William Shakespear. A midsummer Night's Dream The literary devices used in the excerpt above are
          personification and smile
          irony and suspense
          alliteration and synecdoche
         rhyme and refrain.
        \n """,
        """8 based on literary Appreciation.  'You are the silent code of pleasure locked in wordless wonder. You are the hive of treasure, no dragon can plunder' Gbemisola Adeoti :Dream Code. The excerpt above achieves its rhetorical effect through the use of
         repetition and meiosis
         metaphor and rhyme
          caesura and hyperbole
         alliteration and irony
        \n """,
        """9 based on literary Appreciation.  It was not yet closing time, but already most staff were trooping out of their offices. The lift was working now and he squeezed himself into it, breathing with difficulty the body odour emitted by one of the passengers. He sighed with relief when they got to the ground floor and tumbled out of the lift.' Ken Saro-Wiwa: A Forest of Flowers In the excerpt above, the subject's experience in the lift is
         timely.
         comfortable.
         unpleasant
         amusing
        \n """,
        """10 based on literary Appreciation.  'Do not thank me, instead, let me ask you one question, Now you have all come here sprawling vomiting, rubbing tears on one another begging me to do my duty and help you. But what about you yourselves? What have you done to help yourselves? Answer. Or is the land at peace? Are not people ailing and dying?' OIa Rotimi: The Gods Are Not To Blame In the excerpt above, the land is not at peace because of
         chieftaincy tussle
         famine and war
          political unrest
         sickness and death
        \n """,
        """11 based on literary Appreciation.  ‘In those days. When civilization kicked us in the face, when holy water slapped brows. The vultures built in the shadow of their talons.' David Diop: The Vulture The dominant literary device used in the lines above is
         pun
         metaphor
         personification
         simile
        \n """,
        """12 based on literary Appreciation.  I am not afraid of anything; he told them. I have done almost everything in this world. I have you can think of an been committed all c y jailed for most of them. I have been in prison more hours than I have been out of it within the last five years. In recounting his criminal life, the speaker's tone is
          regretful
         boastful
         subdued
         repentant
        \n """,
        """13 based on literary Appreciation.  'I have said too much unto a heart of stone, And laid my honour too unchary on it', There's something in me that reproves my fault,. But such a headstrong potent fault it is That it but mocks reproof.' William Shakespeare: Twelfth Night A heart of stone in the lines above is an example of
          metonymy
         litotes
          assonance
          metaphor
        \n """,
        """14 based on literary Appreciation.  'Blood was prove no solace to the king. The rejection he had suffered at Idama's hands pushed his spirit into a comfortless hole in which, alone with himself, he searched in vain for ways to run from his inner emptiness.' Ayi Kwei Armah: Two Thousand Seasons The narrator’s attitude to the king is one of
         envy
          sympathy
         suspicion
         contempt
        \n """,
        """15 based on literary Appreciation.  'Homage to Peregede the triumphant mother of morning radiant in Chameleon's velvet. Let today's dawn bring on its rails trains of good tidings.' Gbemisola Adeoti: Salutation to the gods The excerpt above is an example of
         invocation
         limerick
          ode
          elegy
        \n """,
        """16 based on literary Appreciation.  The wood decay, the woods decay and fall, The vapour weep their burthen to the ground, Man comes and fills the field and lies beneath, And after many a summer dies the swan. The subject matter of the lines above is
         death
         rainfall
         famine
         storm
        \n """,
        """17 based on J.C. De Graft's Sons and Daughters.  Who is the paternal aunt to Aaron and Maanan?
          Mrs Bonu
          Hannah
          Fosuwa
          Adwao
        \n """,
        """18 based on J.C. De Graft's Sons and Daughters.  From the play, George is a
         laboratory assistant
          pharmacist
         nurse
          medical doctor
        \n """,
        """19 based on J.C. De Graft's Sons and Daughters.  "If you touch me, I shall smash your face with this bottle" The statement is made by
          Manaan to lawyer B
          Manaan to Mrs Bonu
         James to Awere
         Awere to Aaron
        \n """,
        """20 based on J.C. De Graft's Sons and Daughters.‘If you touch me, I shall smash your face with this bottle.’ . The issue at stake is that
         Maanan is trying to compromise
         Lawyer B is trying to kiss Maanan
         James sees Awere as a bad influence
         Mrs Bonu is taunting Maanan for loving her husband
        \n """,
        """21 Shakespeare’s Romeo and Juliet "From forth the fatal loins of these two foes A pair of star-crossed lovers take their life..." The lines above suggest that the tragedy in the play 
        could have been averted
         is predestined
         is brought on enmity
         brought misfortune on the lovers
        \n """,
        """22  O she doth teach the torches to burn bright! It seems she hangs upon the cheek of night A rich jewel in an Ethiop's ear." From the lines above, Juliet's beauty is presented
         in contrast to the dark night
          as a source of envy to all
          in terms of riches
          as being outstanding
        \n """,
        """23  "The all-seeing sun, Ne'er saw match since first the world begun." The lines above were spoken by
          Count Paris in praise of Juliet
          Romeo in praise of Juliet
          Romeo in praise of Roseline
          Lady Capulet in praise of Roseline
        \n """,
        """24 The major role of Mercutio in the play is to
         serve as a contrast to Romeo
          aid and abet Romeo's passion
          annoy Tybalt
          accompany Romeo to Friar Lawrence
        \n """,
        """25  The play shares the feature of classical tragedy through the use of
         violence on stage
         chorus
         comic relief
         flashback
        \n """,
        """26 based on Ferdinand Oyono’s The Old Man and the Medal.  "Meka, kneeling down in his usual fashion with his behind up in the air. Kelara knelt down beside him. Amalia and her husband knelt down as well." The actions of Meka, Kelara, Amalia and her husband signify
          parade
          dance
          prayer
          celebration
        \n """,
        """27 based on Ferdinand Oyono’s The Old Man and the Medal.  "He had knocked his toes against so many things that he had no toenails anymore and the yaws he had suffered from his youth had twisted his toes up so that they pointed to the sky" The description above is in reference to the foot of
          Kelara
          Meka
          Egamba
          Mvondo
        \n """,
        """28 based on Ferdinand Oyono’s The Old Man and the Medal.  "They said their prayers in a monotonous sing-song, kneeling on their bamboo bed like camels waiting to be loaded." The dominant figure of speech in the excerpt above is
          rhetorical question
          simile
          metaphor
         mixed metaphor
        \n """,
        """29 based on Buchi Emecheta’s The joy of Motherhood.  As a symbol of material success and fulfilment, Ibuzza community places a lot of importance on
         childbirth
          wealth
          male child
          female child
        \n """,
        """30 based on Buchi Emecheta’s The joy of Motherhood.  Ona on her dying bed appeals to Agbadi to
          give her a befitting burial
          take good care of her children
          take another wife
          allow Nnu Ego marry a man of her choice
        \n """,
        """31 based on Buchi Emecheta’s The joy of Motherhood. The little money Nnaife makes after returning from Fernando PO is used for
         expanding Nnu Ego's business
         taking care of his family
         sending his children to school
          getting more wives
        \n """,
        """32 based on George Orwell’s Nineteen Eighty-Four.  The novel is mainly classified as a
         metaphor
          hyperbole
         satire
          fiction
        \n """,
        """33 based on George Orwell’s Nineteen Eighty-Four.  Winston writes that the hope of the country lies on the
          ministry of the truth
          proles
          party
          children
        \n """,
        """34 based on George Orwell’s Nineteen Eighty-Four. In the novel, two minutes hate is a programme designed for
          parents
         thought police
         the community
          children
        \n """,
        """35 based on George Orwell’s Nineteen Eighty-Four.  To drop his philosophy of life and imbibe the tenets of the party, Winston is subjected to all forms of torture and inhuman treatment by
         O'Brien
         thought police
         Big Brother
         Goldstein
        \n """,
        """36 based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  The movement in Adeoti's Naked Soles is characterized by
          hope and agreement
          freedom and self-determination
          pricks and tears
         disappointed and disarray
        \n """,
        """37 based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  One of the dominant themes if Rubadin's An African Thunderstorm is the
          relationship between man and woman
          activities of man during rainy seasons
          effect of rain on women and children
         problem of climate change
        \n """,
        """38 based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  In Kunene's A Heritage of Liberation, the weapons are to be preserved for the generation yet unborn by the
          gods
         elders
          people
          government
        \n """,
        """39 based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  Give Me The Minstrel's Seat ends on a clarion call for
          freedom
          peace
          rectitude
          commitment
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "A"),
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
        Literature_2016()
def Literature_2018():
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
        """0 based on Buchi Emecheta’s The Joy of Motherhood . Adaku remains faithful to Nnaife until she
  starts keeping unnecesary friends
  is unable to give birth to a male child
  is rebuked by the Ibuza society for abusing Nnu Ego
  becomes rich and powerful
\n """,
"""1 based on George Orwell’s Nineteen Eighty-four . The Ministry of Love is concerned with
 peace and freedom
 torture and pain
 joy and peace
 hatred and pain
\n """,
"""2 based on George Orwell’s Nineteen Eighty-four . The instruments of power and torture belong to
 the government
 the party
 the thought police
 individuals
\n """,
"""3 based on George Orwell’s Nineteen Eighty-four . The action in the novel is built around
  Winston Smith
  O'Brien
  Julia
  Big Brother
\n """,
"""4 based on George Orwell’s Nineteen Eighty-four . Winston Smith works in the Record Department of the Ministry of
  love
  truth
  peace
  plenty
\n """,
"""5 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse . The dominant poetic technique employed in Adeoti's Naked Soles is
  zeugma
  oxymoron
  hyperbole
  onomatopoeia
\n """,
"""6 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse . Rubadiri's An African Thunderstorm can be described as
  didactic
  dramatic
  traditional
 satirical
\n """,
"""7 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse . 'Since it was you who in all these thin seasons." The device employed in the line above from Kunene's The Heritage of Liberation, is an example of
  apostrophe
  allusion
  anecdote
  aside
\n """,
"""8 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse . "Let me ask for what reason or rhyme women refuse to marry? Woman cannot exist except by man, what is there in that to vex some of them so? The lines above from Give Me The Minstrel's Seat is an example of
  pathetic fallacy
  chiasmus
  ironical statement
  rhetorical question
\n """,
"""9 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse . ‘Time winged chariot’ The line above from Marvell's To His Coy Mistress depicts
  how fast time flies
  the usefulness of time
  the measurement of time
  how fast events unfold
\n """,
"""10 based on selected poems from Johnson, R. et al (eds.): New Poetry from Africa; Soyinka, W. (ed.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds): A Selection of African Poetry; Umukoro M. et al: Exam Focus: Literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides: Poetry for Senior Secondary Schools NWOGA, D.I. (ed.) West African Verse  The language OF Cope’s Sonnet VII past event in a literary work is
 complicated
 simple
 poetic complicated
 difficult
\n """,
"""11 based on General literacy Principles . A device used by a writer to recall past event in a literary work is
  interlude
  anti-climax
  flashback
  foreshadowing
\n """,
"""12 based on General literacy Principles . A paragraph in prose is equivalent to a
  trope in poetry
  verse in poetry
  stanza in poetry
  meter in poetry
\n """,
"""13 based on General literacy Principles . A fable is a brief narrative illustrating wisdom and
 urgency
 origin
 custom
 truth
\n """,
"""14 based on General literacy Principles . A device used in poetry to achieve emphasis or stress a point is known as
  rhyme
  assonance
  repetition
  alliteration
\n """,
"""15 based on General literacy Principles . A literary work that ridicules the shortcomings of people or ideas is
  a masque
  a satire
  an irony
  a fable
\n """,
"""16 based on General literacy Principles . The figure of speech in which the writer means the exact opposite of what he intends to say is
  satire
  irony
  paradox
  metaphor
\n """,
"""17 based on General literacy Principles . Action without speech in a play is
  soliloquy
  aside
  epilogue
  mime
\n """,
"""18 based on General literacy Principles . A mistake committed by the hero which leads to perhaps the plaintive numbers flow his downfall is known as for old, unhappy, far off things
  comic relief And battles long ago.
  terse Or is it some more humble lay,
  climax Familiar matter of today?
  tragic flaw 44. The lines above show that the persona
\n """,
"""19 based on Femi Osofisan's Women of Owu . In the play, the gods are portrayed as
  helpless
 architects of man's destiny
  amorous
  saviours of mankind
\n """,
"""20 based on Femi Osofisan's Women of Owu . Orisaye describes Balogun Kusa as
  a great warrior
  an enemy and a butcher
  a friend in need
  a good leader
\n """,
"""21 based on Femi Osofisan's Women of Owu . Erelu is
  the oldest wife of the Oba Akinjobi
  a courtier to the Alaafin of Oyo
 the most brilliant woman in Owu
  the first wife of the Oba
\n """,
"""22 based on Femi Osofisan's Women of Owu . Balogun Kusa is killed by a
  god
  herbalist
  lunatic
  soldier
\n """,
"""23 based on William Shakespeare's The Tempest . In the play, Ariel is identified as
  leader of the spirits
  Prospero's daughter
  Alonso's wife
  assistant to Sycorax
\n """,
"""24 based on William Shakespeare's The Tempest . Before the shipwreck that occurs at the beginning of the play, Prospero and his daughter have lived in the Island for
  two decades
  twelve years
  forty days
  eighteen months.
\n """,
"""25 based on William Shakespeare's The Tempest . Caliban's intention to rape Miranda is born out of the desire to
  destroy the Island
  compete with Ferdinand
  populate the Island with Calibans
  marry her.
\n """,
"""26 based on William Shakespeare's The Tempest . The character associated with savagery in the play is
  Ariel
  Stephano
  Caliban
  Ferdinand
\n """,
"""27 based on William Shakespeare's The Tempest . Prospero is portrayed as a man who is
  full of mistrust for everybody
  more interested in studying than in governance
  dependent on the spirits for his survival
  eager to conquer the world
\n """,
"""28 based on Asare Konadu's A Woman in Her Prime . The novel explores the theme of
  exploitation of the African woman
  sex discrimination in Ghana
  women liberation in Nigeria
  child quest of an African woman
\n """,
"""29 based on Asare Konadu's A Woman in Her Prime . According to the novel, the worst calamity that can befall a woman is
  inability to bear male
  inability to marry
  divorce children
  barrenness.
\n """,
"""30 based on Asare Konadu's A Woman in Her Prime . In the novel, Asogo is a game in which
  fathers narrate animal stories
  boys abuse girls with music
  girls sing songs of praise admonition
  mothers lure their babies to sleep
\n """,
"""31 based on Chimamanda Adiechie’s Purple Hibiscus . In the novel, one of the changes introduced into St. Agnes’ church by Father is that
  there must be fasting every month
  the Credo must be recited in lgbo
  the Kyrie must be rendered only in Latin
  everyone must take holy communion
\n """,
"""32 based on Chimamanda Adiechie’s Purple Hibiscus . Eugene Achike in the novel is portrayed as
  a soft and gentle husband
  an uncompromising traditionalist
  a fanatical Catholic adherent
  a tough retired soldier.
\n """,
"""33 based on Chimamanda Adiechie’s Purple Hibiscus . In the Achike family, the character who is central to the theme is
  Kambili
  Mama
  Sisi
 Jaja
\n """,
"""34 based on Ernest Hemingway's The Old Man and the Sea. . In the novel, the type of fish caught by Santiag after days of effort is
  shark
  iris
  marlin
  geisha
\n """,
"""35 based on Ernest Hemingway's The Old Man and the Sea. . The novel demonstrates the
  attempt to catch fish
  desire to understand life
  influence of the sea on man
  struggle of man against-defeat
\n """,
"""36 based on Ernest Hemingway's The Old Man and the Sea. . In the novel, the attitude of the old man toward nature is quite
  cautious and sceptical
  hostile and callous
  careless and indifferent
  warm and friendly.
\n """,
"""37 based on Ernest Hemingway's The Old Man and the Sea . Santiago's second dream occurs
  the night before his fishing expedition
  in his house
  at the end of the book
  when he sleeps on the boat for a few hours.
\n """,
"""38 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse . The dominant image in Adeoti's Hard Lines is
  auditory
  gustatory
  visual
  tactile.
\n """,
"""39 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse . The tone of Umeh's Ambassadors of Poverty can be described as
  metaphorical
  sarcastic
  admonitory
  panegyrical
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "C"),

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
        Literature_2018()
def Literature_2019():
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
        """0 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse . Owonibi's Homeless, not Hopeless, the persona explains that street beggars
  always worry about heaven
  rarely sleep and dream
  attend conferences in towns
  are concerned with their daily needs.
\n """,
"""1 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse. . Cheney-Coker's Myopia is a
  dirge
 lament
  sonnet
 ballad
\n """,
"""2 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse.  Jared Angira is an African poet from
  Sierra-Leone
  Kenya
  South Africa
  Ghana.
\n """,
"""3 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse.  The dominant technique used in Serenade is
  metaphor
  simile
  oxymoron
 apostrophe
\n """,
"""4 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse.  The sun in Donne's The Sun Rising is depicted through the use of
 invocation
 ellipsis
 enjambment
 apostrophe
\n """,
"""5 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse. . In Raleigh's The Soul's Errand, the soul is portrayed as a
 friend of suffering masses
  fearless message-bearer
 restorer of lost glory
  messenger of hope and peace.
\n """,
"""6 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse.  The allusion in Hughes's The Negro Speaks of Rivers is mainly
  biblical
  historical
  classical
  literary
\n """,
"""7 based on Selected Poems from Ker,D. et al (eds.) New Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K.E. and Vincent, T. (eds.): A Selection of African Poetry; Umukoro, M et a! (eds.): Exam Focus: Literature in English; Ernubetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D.1. (ed): West African Verse.  Fletcher's Upon An Honest Man's Fortune encourages people to
 condemn soothsaying
  move in the direction of God
  accept soothsaying
  accept life as it is.
\n """,
"""8 based on General Literary Principles . An action in a play that stimulates the audience to pity a character is
  pathos
  parody
  pyrrhic
  props
\n """,
"""9 based on General Literary Principles . Purgation of emotion, pity and fear is
  epilogue
  exposition
  catharsis
  catastrophe
\n """,
"""10 based on General Literary Principles . A device in drama where a character speaks alone is
  apostrophe
  dialogue
  soliloquy
  aside
\n """,
"""11 based on General Literary Principles  . A plot in a literary work is about
  resolution of conflicts
  law of poetic justice
  character delineation
 causal arrangement of events
\n """,
"""12 based on General Literary Principles . Tone and mood of a poem refer to
  setting
  space 
  locale
 atmosphere
\n """,
"""13 based on General Literary Principles  A funny incident within a serious situation is
  tragicomedy
  tragic hero
  comedy
  comic relief
\n """,
"""14 based on General Literary Principles . In literature, a flat character can be described as one who
 dies abruptly
 achieves greatness
 is undeveloped
 undergoes changes
\n """,
"""15 based on General Literary Principles . Dramatis personae in a play refers to
  cast list
 protagonist and antagonist
  list of characters
 order of appearance
\n """,
"""16 based on General Literary Principles . The speech made at the end of a dramatic performance is generally called
 a dirge
 a monologue
 a prologue.
  an epilogue
\n """,
"""17 based on General Literary Principles. Which of the following is central to narrative fiction?
  Objectivity
 Subjectivity
 Verisimilitude
  Dialogue
\n """,
"""18 based on Literary Appreciation . He put himself in uniform, made one for his fiveyear-old son, and marched with the infant from dawn till noon every market day, on the main road singing `Kayiwawa beturi… The persona in the excerpt above is portrayed as
  energetic
  a policeman
  a soldier
  abnormal
\n """,
"""19 based on Literary Appreciation. . He is a faithful liar The above is an example of
 epigram
  oxymoron
  euphemism
  antithesis
\n """,
"""20 based on Literary Appreciation.  Fights by the book of arithmetic The figure of speech in the line above is
 hyperbole
  Euphemism
 Litotes
  Innuendo
\n """,
"""21 based on Literary Appreciation . And when you trudge on one horny pads Gullied like the soles of modern shoes Pads that even jiggers cannot conquer Horny pads in the lines above is a reference to a
 policeman
 madman
 sole of a pauper
 sole of a soldier.
\n """,
"""22 based on Literary Appreciation.  'Lift not the painted veil which those who live call life: though unreal shapes be picture there, And it but mimic all we would believe With colours idly spread-behind, lurk fear.' P.B Shelley: Sonnet The stanza above is an example of a
 quatrain
 sonnet
  couplet
 sestet
\n """,
"""23`I wonder how long, you awful parasites, shall share with me this little bed, And awake me, from my sweet dreams be lost, sucking blood from my poor head...' By Mbure: To a Bed-Bu . The lines are an example of a
  limerick
 lampoon
  light verse
  light opera
\n """,
"""24`I wonder how long, you awful parasites, shall share with me this little bed, And awake me, from my sweet dreams be lost, sucking blood from my poor head...' By Mbure: To a Bed-Bug . The poet persona expresses dismay about
  bat
  cockroaches
  grasshoppers
  light opera
\n """,
"""25`I wonder how long, you awful parasites, shall share with me this little bed, And awake me, from my sweet dreams be lost, sucking blood from my poor head...' By Mbure: To a Bed-Bug . The most dominant figure of speech in the excerpt is
 metaphor
  simile
  personification
  hyperbole
\n """,
"""26 based on Literary Appreciation.  You Your head is like a drum that is beaten for spirits. You Your ears are like the fans used for blowing fire. The lines above are a good example of
  caricature
  ridicule
  satire
  lampoon
\n """,
"""27 based on Literary Appreciation. 'This thing you are doing is too heavy for you, he said. I went to school only a little but I have killed many many more years in this world than you have'. G. Okara: The voice It can be inferred from the passage above that the
  listener is wise
  speaker is a porter
  listener is more experienced
  speaker is more experienced.
\n """,
"""28'Busy old fool, unruly sun why windows and through curtains call on us?' The most vivid figure of speech in the lines above from Donne's The Sun Rising is
  simile
 diction
 personification
  pun
\n """,
"""29 The allusion in Hughes's The Negro Speaks of Rivers is mainly
 biblical
 classical
  literary
 historical
\n """,
"""30 In Adeoti's Hard Lines, Sodium cyanide is
  poisonous
 adhesive
  sweet
  fragrant
\n """,
"""31 In owonibi's Honieless, not Hopeless the persona explains that street beggars
 Always worry about in heaven
  Attend conferences towns
  are concerned with their daily needs
  Rarely sleep and dream
\n """,
"""32 The poet persona in Serenade is a
  Suitor
  Mother
  spinster
  Passer-by
\n """,
"""33 In Cheney-Coker's Myopia, peasants refer to
  Under-privileged masses
  Politicians
  farmers
  Rural dwellers
\n """,
"""34 In Angira's Expelled, the poet persona laments the
  Loss of his property
 Harrowing experiences from the stranger's visit
 presence of the strangers
  Problem of his family and their economic implications
\n """,
"""35 Fletcher's Upon An Honest Man's Fortune achieves its lyrical effect through the use of
 Synecdoche
  Antithesis
  enjambment
  Ballad
\n """,
"""36 Rhythm is achieved in Raleigh's The Soul's Errand through the use of
  Metaphor
  Alliteration
   repetition
  Antithesis
\n """,
"""37 The repetition of a consonant sound in quick succession for sound effect is
  Alliteration
  Pun
  onomatopoeia
  Assonance
\n """,
"""38 A play in which the acts succeed one Another without probable or necessary sequence is
 Episodic
 Simple
 linear
 Convoluted
\n """,
"""39 A technique by which a previous scene or action can be recalled in a play to shed light on the present action is
  Climax
 Flashback
 interlude
 Catharsis
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "D"),
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
        Literature_2019()
def  literature_jamb_2011():
   question_prompt=[
      """"how are you doing
      fine
      stupid
      sad
      happy""",
      """2.based on Richard Wright's Native Son. . Mary's lover is ___
       Earlone
        Buckley
        Bigger
        Max""",
      """3.based on Richard Wright's Native Son.  'Suppose Mary had not burned? Suppose she was still there, expose’ The dominant literacy device in the excerpt above is
       apostrophe
       euphemism
       syntactical parallelism
       rhetorical question""",
      """4.based on Richard Wright's Native Son.  Bigger and the gang rob Negroes because
        they are the same
        it is not a crime
        they are helpless
        it is easier""",
      """5.One of the themes in Morris The Proud King is
       arrogance
       greed
      education
      achievement.""",
      """6.The panic Of growing older Spreads fluttering wings from year to year' The dominant figure of speech in the lines above from Peters' The Panic of Growing Older is
      onomatopoeia
      metaphor
      personification
      apostrophe""",
      """7.Kofi Awoonor is a poet from
      Cameroon
      Nigeria
      Ghana
      Kenya""",
      """8.Okara's Piano and Drums symbolizes
      superiority of the white man
       how Africa is becoming complex
      simplicity of the European society
      the complexities of the Western society""",
      """9.But such a tide moving seems asleep, Too full for sound and foam, When that which drew from out the boundless deep Turns again home.' The rhyme scheme in the excerpt above from Tennyson's Crossing the Bar is
     abba
     abab
      abed
     aabb""",
      """10.'So strength first made a way; Then beauty flowed, then wisdom, honour, pleasure.' The lines above from Herbert's The Pulley is an example of
       personification
       paradox
       metaphor
       antithesis""",
      """11.Blake's The School Boy can be referred to as 
      dramatic
      instructive
      satiric
      expository""",
      """12.`If we cry roughly of our torments; Ever increasing from the start of things, What eyes will watch our large mouths; Shaped by the laughter of big children What eyes will watch our large mouths?' The language of the persona of the above excerpt in Diop's Vanity is
      inciting
      submissive
      imploring
      diplomatic""",
      """13.'Dinner tonight conies with; gun wounds, Our desert tongues lick the vegetable; blood-the pepper' From the lines above in Hallowell's The Dining Table, the persona is
       thirsty
      displeased
       hungry
      sick""",
      """14.'blue Peter on empty ships all peters with petered out desires.' It can be deduced from the lines above in Adeoti’s Ambush that the Peters are
       disappointed
       betrayed
       lazy
       greedy""",
      """15.An art that is both literary and theatrical is
     prosody
     a prose
      drama
      a poem""",
      """16.The speech made by a character to himself on stage is
      epilogue
      monologue
      aside
     soliloquy""",
      """17.In literature, a round character is associated with
      change and growth
      simplicity and modesty
     stability and determination
     running down other characters""",
      """18.In a narrative poem, the post attempts to
      summarize a story
     preach a sermon
     describe a place
     tell a story""",
      """19.The continuation of meaning without pause, from one line to the next is
      enjambment
      synecdoche
     alliteration
      melodrama""",
      """20.The plot of a story generally refers to the
      way in which the writer begins the story
      intrigue made by a character against the hero
      way the writer ends the story
     way in which the events of the story are organized""",
      """21.A didactic piece is one in which the writer
      teaches human lessons
     dictates to the reader
      condemns human foibles
      discuses dialectic themes""",
      """22.What basically distinguish literature from other disciplines
      communication of idea
       use of creative imagination
       portrayal of places
       exposition of human experience""",
      """23.A reward or punishment a character receives in a literary work is
      point of attack
      poetic justice
      popular outcry
      poetic license""",
      """24.In literary criticism, the vocabulary or language used by a writer is generally known as
     figure of speech
      diction
     expression
     rhythm""",
      """25.Weep not child, weep not my darling, With these kisses, let me remove your tears The ravening clouds shall no longer be victorious They shall no longer possess the sky ...The speaker of the lines is
      pessimistic
      optimistic
      helpless
      carefree""",
      """26'You see that Benz at the rich's end? Ha! That motoka is motoka,lt belongs to the Minister for fairness. Who yesterday was loaded with a doctorate. At Makerere with whisky and I don't know what Plus I hear the literate thighs of an undergraduate Theo Luzuka: The Motoka The excerpt above can be described as
       sad
       humorous
       strange
      serious""",
      """27.based on Literary Appreciation. . `... for my purpose holds To sail beyond the sunset and the baths; of all the western stars, until I die.'Tennyson: Ulysses. From the excerpt above, the persona does not intend to
       undertake dangerous adventure
       stop travelling
        die
       travel at night""",
      """28.based on Literary Appreciation.   'And my children left their peaceful nakedness for the uniform of iron and blood.' David Diop: Loser of Everything. In the lines above, the imagery depicts a displacement of
       village life by barrack life
       nature by science
       innocence by violence
       the natural by the artificial""",
      """29.based on Literary Appreciation.  'Now we have come to you, And are amazed to find Those you have loved and respected Mock you to your face.' Kwesi Braw: Lest we should Be The Last The lines above convey the feeling of
       satisfaction
        hope
        disappointment
        fear""",
      """30.based on Literary Appreciation.  The times has come when I can fool myself no more I am no man sadiku. My manhood ended near a week ago. The lines above reveal that the speaker
       has become impotent
       loves women
        is tired of marriage
        is disgusted with life.""",
      """31based on Literary Appreciation.  'In those days When civilization kicked us in the face When holy water slapped our cringing brows. The vultures built in the shadow of their talons.' David Diop: The Vulture. The dominant Literary device used in the lines above is
      A. metaphor
      B. pun
      C.simile
      D. personification.""",
      """32.based on Literary Appreciation.  ‘The leaves are withered Roses fold and shrink Dog the panting athlete shows his tongue dwarled A shadow flees Nude under and crack.' Nuts wrinkle and crack.’ W. Kamera: Poems in Four Parts. One dominant image presented in the lines above is that of
       death
       summer
       tiredness
       spent life""",
      """33.based on Literary Appreciation.  When I remember by gone days I think how evening follows morning So many I loved were not yet dead, So many I love not yet born. The period of life the poet has arrived at is
       middle age
       adolescence
       old age
       early childhood""",
      """34.based on Frank Ogodo Ogbeche's Harvest of Corruption . Aloho perceives her pregnancy as a form of
        reward
        blessing
        punishment
        injustice""",
      """35.based on Frank Ogodo Ogbeche's Harvest of Corruption . The play can be referred to as
        dramatic irony
        allegory
        fable
        satire""",
      """36.based on Frank Ogodo Ogbeche's Harvest of Corruption . According to Ochuole, government job is
       a waste of time
       time consuming
        good for hardworking youths
        an avenue to personalize public fund""",
      """37.based on Frank Ogodo Ogbeche's Harvest of Corruption . Aloch is warned about associating with Ochuole be-cause the latter is
       too sophisticated
        proud
        mischievous
        born-again""",
   ]
   question=[
        Question(question_prompt[0],'a'),
        Question(question_prompt[1],'d'),
        Question(question_prompt[2], 'd'),
        Question(question_prompt[3],'d'),
        Question(question_prompt[4], 'a'),
        Question(question_prompt[5], 'c'),
        Question(question_prompt[6], 'c'),
        Question(question_prompt[7], 'b'),
        Question(question_prompt[8], 'b'),
        Question(question_prompt[9], 'a'),
       Question(question_prompt[10], 'b'),
       Question(question_prompt[11], 'c'),
       Question(question_prompt[12], 'b'),
       Question(question_prompt[13], 'b'),
       Question(question_prompt[14], 'a'),
       Question(question_prompt[15], 'a'),
       Question(question_prompt[16], 'a'),
       Question(question_prompt[17], 'a'),
       Question(question_prompt[18], 'a'),
       Question(question_prompt[19], 'a'),
       Question(question_prompt[20], 'a'),
       Question(question_prompt[21], 'd'),
       Question(question_prompt[22],'b'),
       Question(question_prompt[23], 'b'),
       Question(question_prompt[24], 'b'),
       Question(question_prompt[25], 'a'),
       Question(question_prompt[26], 'd'),
       Question(question_prompt[27], 'c'),
       Question(question_prompt[28], 'c'),
       Question(question_prompt[29], 'a'),
       Question(question_prompt[30], 'd'),
       Question(question_prompt[31],'a'),
       Question(question_prompt[32],'b'),
       Question(question_prompt[33],'c'),
       Question(question_prompt[34],'c'),
       Question(question_prompt[35],'d'),
       Question(question_prompt[36],'c'),
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


def literature_jamb_2015():
    question_prompts = ["""
            [1].From the tone of the speech above, the speaker is obviously
            (a)enraged
            (b)lackadaisical
            (c)elated
            (d)happy.
            """,
            """[2].based on Literary Appreciation. 'That year the harvest was sad, like a funeral, and many farmers wept as they dug up the miserable yams. One man tied his cloth to a tree branch and hanged himself'. Chinua Achebe: Things Fall Apart The mood conveyed in the excerpt above is one of
            (a)sadness
            (b)frustration
            (c)sympathy
            (d)dilemma.
          """,
            """[3].based on Literary Appreciation. 'That age is best which is the first, when youth and blood are warmer, But being spent, the worse, and worst Time still succeed the former. The rhyme scheme in the excerpt above is
            (a)bbaa
            (b)aabb
            (c)abab
            (d)abba.
          """,
            """[4].based on Literary Appreciation. But the towering earth was tired sitting in one position. She moved, suddenly, and the houses crumbled, the mountains heaved horribly, and the work of a million years was lost. The subject matter of the extract above is
            (a)storm
            (b)sea waves
            (c)house movement
            (d)earthquake.
          """,
            """[5].based on Literary Appreciation. And your laughter like a flame piercing the shadows Has revealed Africa to me beyond the snow of yesterday. From the poem above, shadow means
            (a)famine
            (b)bleak future
            (c)period of sufferings
            (d)abstract ideas.
           """,
            """[6].based on Literary Appreciation. Don't panic. Be calm, If you are some how upset ...try to regain your exposure. The speaker in the excerpt above is
           (a)hopeless
           (b)uncertain
           (c)afraid
           (d)confident.
           """,
            """[7].based on Literary Appreciation. Move him into the sun Gently its touch awoke him once, At home, whispering of fields unsown Always it woke him even in France Until this morning and this snow If anything might rouse him now This kind old sun will know Think how it wakes the seeds Woke, once, the clays of a cold star Are limbs, so dear achieved, are sides Full nerved still swarm too hard to stir Was it, for this the clay grew tall? 0 what made fatuous sunbeams toil To break earth's sleep at all. The poem can be described as
            (a)a lyric
            (b)an epic
            (c)a sonnet
            (d)an elegy.
           """,
            """[8].based on Literary Appreciation. The theme of the poem is
            (a)futility of life
            (b)distortion of life
            (c)creation of life
            (d)vanity of life
           """,
            """[9].based on Literary Appreciation. A cursing rogue with a merry farce, A bundle of rags upon a crutch, Stumbled upon that windy place Called cruachan, and it was as much. The rhyme scheme of the stanza above is
            (a)aabb
            (b)abab
            (c)bbaa
            (d)abba.
           """,
            """[10].based on J. C De Graft’s Sons and Daughters.  From it’s resolution of conflicts, the pay can be described as
            (a)tragedy
            (b)comedy
            (c)farce
            (d)melodrama
           """,
            """[11].based on J. C De Graft’s Sons and Daughters. The prevailing theme of the play is ----
           (a)love
           (b)affluence
           (c)social decadence
           (d)self-will
           """,
            """[12].based on J. C De Graft’s Sons and Daughters.  The final harassment of Maanan takes place in
           (a)Ofosu’s office
           (b)Lawyer B’s house
           (c)Lawyer B’s chamber
           (d)Ofosu’s house
           """,
            """[13].based on J. C De Graft’s Sons and Daughters.  ‘Everything in this room outrages my sense of beauty, undermines my will to create pictures of lasting appeal....’ The speaker in the quotation above is
            (a)happy
            (b)frustrated
            (c)excited
            (d)tired
           """,
            """[14].based on William Shakespeare’s Romeo and Juliet.  ‘Farewell – God knows when we shall meet again. I have a faint cold fear thrills through my veins, That almost freezes up the heat of lie. I’ll call them back again to comfort me. Nurse! – What should she do here? My dismal scene I need act alone. Come, vial’. The intention of the speaker above is to
           (a)commit
           (b)suicide
           (c)take a temporary harmful substance
           (d)escape from harsh realities of life
           """,
            """[15].based on William Shakespeare’s Romeo and Juliet.  The play reaches the point of denouncement
            (a)at the family feast
            (b)when Romeo kills Paris at the tomb
            (c)at the reconciliation of the feuding families.
            (d)when Romeo is informed of Juliet’s death
           """,
            """[16].based on William Shakespeare’s Romeo and Juliet . The news of Juliet's death is broken to Romeo in Mantua by
           (a)Balthasar
           (b)Friar Lawrence
           (c)Boy
           (d)Friar John
            """,
            """[17].based on William Shakespeare’s Romeo and Juliet.  In the play, Mercutio can be described as
            (a)fraudulent
            (b)quarrelsome
            (c)gentle
            (d)kind-hearted
           """,
            """[18].based on William Shakespeare’s Romeo and Juliet.  The plot of the play is
           (a)simple
           (b)complicated
           (c)convoluted
           (d)chronological
           """,
            """[19].based on Ferdinand Oyono's The Old Man and the Medal.  The heavy downpour on the night of Meka's investiture symbolizes
           (a)revelation
           (b)mockery
           (c)conviction
           (d)blessing
           """,
            """[20].based on Ferdinand Oyono's The Old Man and the Medal.  Vandermayer's attitude and action towards Meka illustrates the church's
            (a)despondency
            (b)suspicion
            (c)infuriation
            (d)hypocrisy
           """,
            """[21].based on Ferdinand Oyono's The Old Man and the Medal.  'As he opened and shut his mouth his lower jaw went down and came up, puffing up and then deflating the skin under his chin.' The subject of description in the lines above is
            (a)the high commissioner
            (b)M. Pipiniakis
            (c)the white chief
            (d)M. Fouconi
           """,
            """[22].based on Buchi Emecheta's The Joy of Motherhood.  For attempted murder, Nnaife was jailed for
            (a)four months
            (b)three months
            (c)five months
            (d)two months
           """,
            """[23].based on Buchi Emecheta's The Joy of Motherhood.  In the novel, Nwokocha Agbadi is famous for his oratorical powers and
           (a)height
           (b)treachery
           (c)illiteracy
           (d)wealth
           """,
            """[24].based on George Orwell's Nineteen Eighty-Four The novel draws a picture of
           (a)a useless past
           (b)a totalitarian future
           (c)an unstable moment
           (d)a peaceful atmosphere
           """,
            """[25].based on George Orwell's Nineteen Eighty-Four The power and oppression of an irresistible evil debased Winston's dreams of __.
           (a)freedom and democracy
           (b)internal security
           (c)wealth and capitalism
           (d)sovereignty
           """,
            """[26].based on George Orwell's Nineteen Eighty-Four  Room 101 symbolizes a place of
           (a)rest
           (b)fun
           (c)humiliation
           (d)tour
           """,
            """[27].based on George Orwell's Nineteen Eighty-Four . The novel can be described as
           (a)optimistic
           (b)antagonistic
           (c)persuasive
           (d)pessimistic
           """,
            """[28].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse . In Naked Soles, Adeoti writes that the carnival of naked soles dances through
           (a)scorching sun
           (b)a dirty room
           (c)blooming thorns
           (d)a cloudy atmosphere
           """,
            """[29].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse. In Rubadiri's An African Thunderstorm, the thunderstorm begins with
           (a)rain from the west
           (b)clouds from the east
           (c)rain from the east
           (d)clouds from the west
           """,
            """[30].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  The theme of Acquah's In the Navel of the Soul is
           (a)the conflict of traditions
           (b)ensuring that traditions were strictly observed
           (c)the futility of man and his tradition
           (d)the strength in diversity of culture and traditional views.
           """,
            """[31].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  In Kuene’s A Heritage of Liberation, the persona is concerned with the
            (a)people's struggle for survival
            (b)criticism of modern tradition
            (c)intolerance of the new generation
            (d)celebration of African tradition.
           """,
            """[32].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  Lanko’s End of the War portrays the
            (a)silence of
            (b)usefulness of praise singers
            (c)irony of life
            (d)arrangement of war
           """,
            """[33].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  'Woman cannot exist except by man, What is there in that to vex some of them so?' The statement above from the poem Give Me The Minstrel's Seat exemplifies
            (a)litotes
            (b)rhetorical question
            (c)transferred epithet
            (d)synecdoche
           """,
            """[34].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse. Marvell, in To His Co Mistress uses the imagery of Coy death to
            (a)appreciate God's power
            (b)underscore life's transience
            (c)condemn the lady
            (d)scare the lady
           """,
            """[35].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  To sustain the interest of readers, Lawrence in Bat uses
           (a)elision
           (b)hyperbole
           (c)suspense
           (d)oxymoron
            """,
            """[36].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse . 'With a running stream and a water-mill beating the darkness. And three trees on the low sky.' • In the excerpt above from Eliot's Journey on the Magi, the dominant literary device is
            (a)oxymoron
            (b)personification
            (c)hyperbole
            (d)alliteration
            """,
            """[37].New Poetry based on selected poems Ker, D. e t al (eds.) Bew Poetry from Africa; Soyinka, (ed.): Poems of Black Africa; Senanu K. E and Vincent, T. (eds.): A Selection of African Poerty; Unukoro, Met al (eds.): Exam Focus: Literature in English; Eruvbetine, A.E. et al(eds.): Longman Examination Guides and Nwoga, D.I (ed): West African Verse.  The tone of Cope's Sonnet VII is generally
            (a)persuasive
            (b)humorous
            (c)optimistic
            (d)mournful
           """,
            """[38].based on General Literary Principles.  The large space above the proscenium in a theatre from which the scenes are controlled is called
           (a)aside
           (b)setting
           (c)anachronism
           (d)flies
           """,
            """[39].based on General Literary Principles.  'Good warriors make others come to them and do not go to others.... When you induce opponents to come to you, then their force is always empty, like attacking emptiness with fullness is throwing on eggs.' Zhang Yu: The Art of War. The theme of the passage above is
            (a)folly of soldiers
            (b)inspiration
            (c)spurring people to action
            (d)war
            """,
            """[40].based on General Literary Principles.  The repetition of single words or phrases at the beginning of lines is
            (a)assonance
            (b)parallelism
            (c)onomatopoeia
            (d)alliteration
                      
                             """]
    questions = [Question(question_prompts[0], "a"),
                 Question(question_prompts[1], "a"),
                 Question(question_prompts[2], "c"),
                 Question(question_prompts[3], "d"),
                 Question(question_prompts[4], "d"),
                 Question(question_prompts[5], "d"),
                 Question(question_prompts[6], "c"),
                 Question(question_prompts[7], "a"),
                 Question(question_prompts[8], "b"),
                 Question(question_prompts[9], "d"),
                 Question(question_prompts[10], "d"),
                 Question(question_prompts[11], "d"),
                 Question(question_prompts[12], "b"),
                 Question(question_prompts[13], "b"),
                 Question(question_prompts[14], "c"),
                 Question(question_prompts[15], "a"),
                 Question(question_prompts[16], "b"),
                 Question(question_prompts[17], "d"),
                 Question(question_prompts[18], "b"),
                 Question(question_prompts[19], "d"),
                 Question(question_prompts[20], "d"),
                 Question(question_prompts[21], "a"),
                 Question(question_prompts[22], "d"),
                 Question(question_prompts[23], "b"),
                 Question(question_prompts[24], "a"),
                 Question(question_prompts[25], "a"),
                 Question(question_prompts[26], "d"),
                 Question(question_prompts[27], "a"),
                 Question(question_prompts[28], "c"),
                 Question(question_prompts[29], "d"),
                 Question(question_prompts[30], "d"),
                 Question(question_prompts[31], "d"),
                 Question(question_prompts[32], "c"),
                 Question(question_prompts[33], "b"),
                 Question(question_prompts[34], "b"),
                 Question(question_prompts[35], "c"),
                 Question(question_prompts[36], "b"),
                 Question(question_prompts[37], "b"),
                 Question(question_prompts[38], "d"),
                 Question(question_prompts[39], "b")
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
        print('your profile is', des, '\nyour percentage:', round((score / len(questions)) * 100, 2), '%')
        if score >= 40:
            print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
        else:
            print("\nyou failed the test,go and read your book and try again😭☹👎\n")

    run_test(questions)
from Question import *
def literature_in_english_2014():
    question_prompts=["""1.based on J.C. De Graft's Sons and Daughters „I simply don't understand what's the matter with everybody today. Everybody let me down, and the speaker above is referring to __.
a. Fosuwa and Maidservant
b. Hannah and George
c. Aaron and Maanan
d. Lawyer B and Mrs. B
""","""2.based on J.C. De Graft's Sons and Daughters „ . Maanan expresses dislike for Lawyer B because of __.
a. his condemnation of her choice of career
b. his recent advances towards her
c. the betrayal of her father's trust
d. the betrayal of his wife's trust.
""","""3.based on J.C. De Graft's Sons and Daughters „ . The traditional order in the play is represented by __ .
a.  Mrs. B
b. Hannah
c.  Maanan
d. Aunt
""","""4.based on J.C. De Graft's Sons and Daughters „5. Where does the play take place?
a. On the street
b. In George's place
c. In Aunt's house
d. In Ofosu's place.
""","""5.based on William Shakes ear's Romeo and Juliet   '0' deadly sin!O rude unthankfulness! Thy fault our law calls death, but the kind Prince, Taking thy part, hath rushed aside the law And turned that black word...' Deadly sin refers to the __.
 a. suicide of Juliet
 b. suicide of Romeo
 c. murder of Paris
d. murder of TybaIt
""","""6.based on William Shakes ear's Romeo and Juliet . The play is mostly written in __.
a.  blank verse
b. free verse
c. metres
d. foot.
""","""7.based on William Shakes ear's Romeo and Juliet  '0' serpent heart, hid with a flowering face!' The statement above refers to __
a. Juliet
b. Romeo
c. Tybalt
d. Benvolio.
""","""8.based on William Shakes ear's Romeo and Juliet . The spatial setting of the play is __.
a.  Athens
b.  Verona
c. Padua
d. Venice
""","""9.based on William Shakes ear's Romeo and Juliet .Romeo is banished to Mantua because he __.
 a. kills Tybalt in a street duel
 b. marries Juliet without parental consent
 c. attends Capulet's party uninvited
 d. attempts to kill paris his rival.
""","""10.based on Buchi Emecheta's The Joys of Motherhood.In the novel, the society puts high value on __.
a.  egalitarianism
b.  male ascendancy
c.  procreation
d.  gender equity.
""","""11.based on Buchi Emecheta's The Joys of Motherhood. The medicine man links the lump discovered on the head of Nnu Ego at birth, to the __.
a.  possession of physical admirable qualities that makes her an epitome of perfection.
b.  wound inflicted on the slave woman buried with Agbadi‟s wife
c.  coming back of the Agunwa to the society to live again
d.  ill-luck and tragic events attributed to a predestined fate
""","""12.based on Buchi Emecheta's The Joys of Motherhood. The constant companions of Nnaife's family are __.
a. togetherness and happiness
b. poverty and hunger
c.  sickness and joblessness
d.  disagreement and humiliation
""","""13.based on Ferdinand Oyano's The Old Man and the Medal. The disagreement between Mvondo and Nti centres on the latter‟s claim to have __.
a.  assisted Meka in getting the medal
b. eaten the entire entrails of a sheep
c. eaten more than his share of the food
d. been in a white man‟s office
""","""14.based on Ferdinand Oyano's The Old Man and the Medal. Meka can be best be described as__.
a.  an egocentric old man
b.  a simple-hearted old man
c. an impulsive old man
d. an old religious bigot
""","""15.based on Ferdinand Oyano's The Old Man and the Medal  .In the novel, the colonialists treat the Africans with __.
 a. Kids‟ gloves
b. disdain
c. indifference
d. honour
""","""16.based on George Orwell's Nineteen Eighty-four .The Ministry of peace is concerned with making _.
 a. instruments
b. weapons
c. wars
d. reconciliation
""","""17.based on George Orwell's Nineteen Eighty-four .The subject matter of the novel is __.
a.  totalitarian dictatorship
b.  exploitation and cruelty
c.  retributive justice
d. class segregation.
""","""18.based on George Orwell's Nineteen Eighty-four .How did Winston start his rebellion against the state __.
a.  By engaging in anti-party activities
b.  By keeping a private diary
c.  When he started a secret affair
d.  When he spied on the party.
""","""19.based on George Orwell's Nineteen Eighty-four .The party seeks power for __.
a.  the nation
b. its own sake
c.  its members
d.  peoples' sake
""","""20.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse.   As the dancers move through paths strewn with glass chips, the images in Adeoti's Naked Soles change from __.
 a. joy to excitement
 b. inaction to action
 c. pain to grief
 d. sorrow to joy.
""","""21.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse. Rubadiris's An African Thunderstorm, says that during thunderstorm in the village
a.  women cook their food
b.  children play in the rain
c. children are delighted while women move in and out
d. both women and children are delighted.
""","""22.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse.  'Yet in their finger upon Our navel The midwives of the spirit say They feel a foetal throb. The dominant literary device used in the extract above from Acquahs' In the Navel of the Soul is 
a.  epigram
b. allegory
c. enjambment
d. rhythm.
""","""23.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse.In Kunene's A heritage of Liberation, the poet persona requests that the weapons of warfare be handed to their __.
a.  friends
b.  relations
c. grand children
d.  families
""","""24.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse .The predominant device in Launko's End of the War is __.
a. onomatopoeia
b.  antithesis
c.  oxymoron
d.  paradox
""","""25.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse .The theme of the poem Give Me The Minstrel's Seat centres on __
a.  divorce
b.  fortune
c. marriage
d. companionship.
""","""26.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse. The poet persona in Marvell's To His Coy Mistress is willing to praise the lady's eyes for
 a. thirty thousand years
 b. six decades
c. two centuries
 d. a century.
""","""27.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse. In Lawrence's Bat, the poet persona mistakes the bats for
a. owls
b.  swallows
c. pipistrello
d. sparrows
""","""28.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse. In Eliot's Journey of the Magi, the magi are aided on their journey by
a. donkeys
b.  horses
c. camels
d. chariots.
""","""29.based on selected poems from Ker, D. et al (eds.) New Poetry from African; Soyinka, (ed.) Poems of Black Africa; Senanu K.E. and Vincent T. (eds.): A selection of African Poetry; Umukoro, M et al (eds.) Exam Focus: literature in English; Eruvbetine, A.E. et al (eds.): Longman Examination Guides and Nwoga, D. I. (ed): West African Verse. According to Cope‟s Sonnet VII, poetry is basically__.
a. boring
b. therapeutic
c. philosophical
d. inspiring
""","""30.based on General Literary Principles. A play which mainly aims at provoking excessive laughter is called
a. tragic-comedy
b. comedy
c.  a farce
d. satire
""","""31.based on General Literary Principles. Both comedy and tragedy have __.
 a. happy ending
b. climax
 c. tragic hero
d. stanza
""","""32.based on General Literary Principles. A formal dignified speech or writing praising a person or a thing for past or present deeds is
 a. premiere
 b. eulogy
 c.anthology
 d. lampoon
""","""33.based on General Literary Principles. The narrative style in which the hero tells his own story directly is the __.
a. objective
 b. subjective
 c. first- person
 d. third-person.
""","""34.based on General Literary Principles. The physical, historical or cultural background of a literary work is referred to as
 a. episode
 b. plot
 c. time
 d. setting
""","""35.based on General Literary Principles .A plot structure that defies chronology can be described as
 a. open-ended
 b. circular
 c. episodic
 d. organic
""","""36.based on General Literary Principles. Pun as a literary device deals with
 a. placing two opposite phrases
 b. placing words side by side
 c. playing on words
d. arrangement of words
""","""37.based on General Literary Principles. In a narrative poem, the poet attempts to
 a. summarize a story
 b. describe a place
 c. preach a sermon
 d. tell a story
""","""38.based on General Literary Principles .The account of experiences of an individual during the course of a journey is known as
 a. a travelogue
 b. an autobiography
 c. a catalogue
 d. a memoir
""","""39.based on General Literary Principles. Satirical writing employs _.
 a. epigram
 b. synecdoche
 c. irony
 d. onomatopoeia.
""","""40.„Basha: You dumb skull of a bone head . . . you will face court martial for this. You look everywhere? You search inside toilet bowl? Wole Soyinka: King Baabu The person being addressed above is a
 a. soldier
b. student
 c. domestic servant
 d. lawyer"""]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'b'),
        Question(question_prompts[2], 'd'),
        Question(question_prompts[3], 'd'),
        Question(question_prompts[4], 'd'),
        Question(question_prompts[5], 'b'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'b'),
        Question(question_prompts[8], 'a'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'd'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'c'),
        Question(question_prompts[13], 'd'),
        Question(question_prompts[14], 'b'),
        Question(question_prompts[15], 'd'),
        Question(question_prompts[16], 'b'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'd'),
        Question(question_prompts[20], 'c'),
        Question(question_prompts[21], 'c'),
        Question(question_prompts[22], 'c'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'd'),
        Question(question_prompts[25], 'd'),
        Question(question_prompts[26], 'a'),
        Question(question_prompts[27], 'c'),
        Question(question_prompts[28], 'b'),
        Question(question_prompts[29], 'c'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'b'),
        Question(question_prompts[32], 'c'),
        Question(question_prompts[33], 'd'),
        Question(question_prompts[34], 'd'),
        Question(question_prompts[35], 'c'),
        Question(question_prompts[36], 'd'),
        Question(question_prompts[37], 'a'),
        Question(question_prompts[38], 'c'),
        Question(question_prompts[39], 'a'),
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
def literature_in_english_2017():
    question_prompts=["""1.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  "...the youthful hue/sits on thy skin like a morning dew..." The excerpt above from Marvell's To His Coy Mistress is an example of
a. simile
b. anaphora
c. paradox
d. onomatopia
a. simile
""","""2.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  In Lawrence's Bat, the poet compares bats with
a. sparrows
b. swans
c. swallows
d. crows
a. sparrows
""","""3.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  Elliot's The Journey of the Magi could be said to examine the issues of
a. three trees on the low sky
b. empty wine-skins
c. spiritual rebirth
d. holy pilgrimage
c. spiritual rebirth
""","""4.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  "We would be believing we dreamt it" The figure of speech in the line above from Acquah's In the Navel of the Soul is
a. apostrophe
b. assonance
c. antithesis
d. alliteration
d. alliteration
""","""5.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  The casualties in Launko's End of the War
a. women
b. children
c. men
d. soldiers
d. soldiers
""","""6.based on selected poems from Johnson, R, et al (eds.): New Poetry from Africa; Soyinka, W. (ED.): Poems of Black Africa; Senanu, K.E. and Vincent, T. (eds.): A Selection of African Poetry: U. Maduka, C.T et al: Exam Focus: Longman Examination Guides; Nwoga, D.I. (ed.): West African Verse and Adeoti G: Naked Soles.  The theme of Cope's Sonnet VII is
a. art of poetry
b. adventure
c. contempt for literature
d. isolation
a. art of poetry
""","""7.based on general Literary Principles.  A literary work in which the characters and events are used as symbols is known as
a. characterization
b.  allegory
c.  metaphor
d.  parallelism
b. allegory
""","""8.based on general Literary Principles.  Characterization in a novel refers to the
a.  writer's opinion of the characters
b. way the characters are revealed to the reader
c.  characters and the way they behave
d. reader's opinion of the characters
c. characters and the way they behave
""","""9.based on general Literary Principles.  In literary work, verbal irony refers to a
a. device in which the speaker means the opposite of what he says
b.  situation in which a character speaks or acts against the trend of events
c.  difficult situation which defies a logical or rational resolution
d.  device in which the actor on stage means exactly what he says
a.  device in which the speaker means the opposite of what he says
""","""10.based on general Literary Principles.  In the theater, words spoken by a character that are meant to be heard by the audience but not by the other characters on stage is called
a. aside
b. soliloquy
c. acoustic
d. tone
a. aside
""","""11.based on general Literary Principles.  Drama is the representation of a complete series of actions by means of
a.  movement and gesture for the screen and audience
b.  speech, movement and gesture for the stage only
c.  speech, movement and gesture for the stage, screen and radio
d.  speech, gesture and movement for the screen and radio
b.  speech, movement and gesture for the stage only
""","""12.based on general Literary Principles.  A poet's use of regular rhythm is known as
a. allegory
b. assonance
c. metre
d. onomatopoeia
c. metre
""","""13.based on general Literary Principles.  A literary genre which directly imitates human action is
a. drama
b. comedy
c. prose
d. poetry
a. drama
""","""14.based on general Literary Principles.  A fable is a story in which
 a. allegations are made about characters
 b. animals or things are used as characters
 c. there is an important setting
 d. the story is told in poetic form
 b. animals or things are used as characters
""","""15.based on general Literary Principles.  The juxtaposition of two contrasting ideas in a line of poetry is
a. euphemism
b. synedoche
c. catharsis
d. oxymoron
d. oxymoron
""","""16.based on general Literary Principles.  The main aim of caricature is to
 a. describe
 b. expose
 c. emphasize
 d. ridicule
d. ridicule
""","""17.based on Literary Appreciation . O! Ceremony, show me but thy worth What is thy soul of adoration The figure of speech in the lines above is
a.  antithesis
b.  invocation
c.  personification
d. apostrophe
d.  apostrophe
""","""18.based on Literary Appreciation . "What eyes will watch our large mouths, Shaped by the laughter of big children What eyes will watch our large mouths?" Birage Diop:Vanity The tone of the lines above is one of
a. sarcasm
b. sacrilege
c. chiasmus
d. eulogy
a. sarcasm
""","""19.based on Literary Appreciation . The old man slept in his favourite chair The wind ran its fingers through his hair He looked like a tree gone dry of sap And his hands were dry upon his lap The rhyme a scheme of the poem above is
a. bbaa
b. aabb
c. abab
d. baba
b. aabb
""","""20.based on Literary Appreciation . Unequal laws unto a savage race, That board, and sleep, and feed.... The lines above show that the speaker
a. detects discrimination
b. is desirous of adventure
c. hates his old wife
d. knows much of his city men
a. detects discrimination
""","""21.based on Literary Appreciation . ....How can I look at Oyo and say I hate long shiny cars? How can I come to the children and despise international schools? And Koomson comes, and the family sees Jesus Christ in him.... The feeling conveyed by the speaker above is one of
a. anger
b. alienation
c. hope
d. despair
a. anger
""","""22.based on Literary Appreciation . "Hide me now, when night children haunt the earth" Wole Soyinka:Night Night children in the stanza above reflects the consciousness of
a. birds
b. armed robbers
c. animals
d. spirit beings
d. spirit beings
""","""23.based on Literary Appreciation . "Serrated shadows, through dark leaves, Til, bathed in warm suffusion of your dapped cells Sensation pained me, faceless, silent as night thieves." Wole Soyinka: Night The dominant mood in the lines above is one of
a. apprehension
b. defiance
c. joy
d. indifference
a. apprehension
""","""24.based on Literary Appreciation . "The drums overwhelmed the guns..." J.P Clark: Casualties The poet in the excerpt above uses
a. litotes
b. symbolism
c. onomatopoeia
d. alliteration
c. onomatopoeia
""","""25.based on Literary Appreciation . ‘....They do not see the funeral piles At home eating up the forests...’ J.P. Clark:Casualties The imagery created in the above excerpt is achieved through
a. metaphor
b. personification
c. synecdoche
d. metonym
a. metaphor
""","""26.based on Literary Appreciation . "I cannot rest from travel: I will drink Life to the lees, all times I have enjoyed Greatly, have suffered greatly" A.L. Tennyson: Ulysses The lines above inform the reader that the poet
a. is determined to suffer
b. has his poetic imagination kindled
c. will cure his sour mood
d. will not drink much
b. has his poetic imagination kindled
""","""27.James: Let me swear, woman. And I will swear by my father's coffin that if.... . The lines depict James as a
a. traditionalist
b. Christian
c. pagan
d. Muslim
a. traditionalist
""","""28.James: Let me swear, woman. And I will swear by my father's coffin that if.... . The speaker is referring to
a. Fosuwa
b. Awere
c. Maanan
d. Hannah
b. Awere
""","""29.based on J.C. De Graft's Sons and Daughters.. . Aaron'...All I need really is a place in an Art school, engineering can go hang itself. The dominant figure of speech in the excerpt above is
a. metonymy
b. synecdoche
c. personification
d. metaphor
c. personification
""","""30.based on J.C. De Graft's Sons and Daughters.. . From the play, the character of Aaron represents the
a. painters
b. art work
c.  new generation
d. old generation
c. new generation
""","""31.'Uncle, this is a Montague, our foe; A villain that is hither come in spite, To scorn at our solemnity this night.' The villain in the excerpt above is
a.  attempting to steal
b.  attending a feast uninvited
c.  engaging in a shouty match
d.  holding a sword to commit murder
b.  attending a feast uninvited
""","""32."What, drawn and talk of peace? I hate the word As I hate hell, all Montagues, and thee Have at thee,coward!" Based on William Shakespeare's Romeo and Juliet, the lines above reveal the speaker as a
a.  violence seeker
b.  peace maker
c.  real Montague
d.  trouble shooter
d.  trouble shooter
""","""33.Romeo’s mood, at the beginning of the play can be described as
a.  melancholic and sentimental
b.  dreamy and hopeful
c.  frustrated and pensive
d.  gay and elated
c.  frustrated and pensive
""","""34."O'deadly sin! O rude unthankfulness! Thy fault our law calls death, but the kind Prince, taking thy part, hath rushed aside the law, And turned that black word "death" to banishment." The speaker in the passage above is
a.  Lord Montague
b.  Friar Lawrence
c.  Apothecary
d.  Lord Capulet
a.  Lord Montague
""","""35."....Put up thy sword Or manage it to part these men with me." The speech above was made when
a.  Tybalt challenges Romeo to duel
b.  Prince Escalus arrives to make peace between the families
c.  Romeo and Paris engaged themselves in a fight
d.  Benvolio tries to separate the servants of the feuding families
d.  Benvolio tries to separate the servants of the feuding families
""","""36.based on Ferdinand Oyono's the Old Man and the Medal . For his sacrifices to the church, Meka gets
a. appointed into the church elders' council
b. the privilegde to choose a permanent place to sit
c.  a place near an aged leper
d.  a land to build a new house
a.  appointed into the church elders' council
""","""37.based on Ferdinand Oyono's the Old Man and the Medal . "Since I came to this country, I have never seen cocoa as well dried as yours." The speaker above is
a. Nkolo
b. the Commandant
c. the Catechist
d. Nua
b. the Commandant
""","""38.based on Ferdinand Oyono's the Old Man and the Medal . To the white men, the medal that is given symbolizes
a.  harmonious relationship
b.  love
c.  peace
d.  friendship
d.  friendship
""","""39.based on Buchi Emecheta’s The Joy of Motherhood. . Nnu Ego is blamed for the misfortunes of her
a. parents
b. husband
c. siblings
d. children
d. children
""","""40.based on Buchi Emecheta’s The Joy of Motherhood. According to the novel Nnaife becomes frustrated when
 a. Oshiaju secures a scholarship to study abroad
 b. he is arrested and charged for attempted murder of his in-law
 c. his wife gives birth to female twins
 d. he is recruited into the army
 c. his wife gives birth to female twins"""]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'c'),
        Question(question_prompts[3], 'd'),
        Question(question_prompts[4], 'd'),
        Question(question_prompts[5], 'a'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'c'),
        Question(question_prompts[8], 'a'),
        Question(question_prompts[9], 'a'),
        Question(question_prompts[10], 'b'),
        Question(question_prompts[11], 'c'),
        Question(question_prompts[12], 'a'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'd'),
        Question(question_prompts[16], 'd'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'a'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'd'),
        Question(question_prompts[22], 'a'),
        Question(question_prompts[23], 'c'),
        Question(question_prompts[24], 'a'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'a'),
        Question(question_prompts[27], 'b'),
        Question(question_prompts[28], 'c'),
        Question(question_prompts[29], 'c'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'd'),
        Question(question_prompts[32], 'c'),
        Question(question_prompts[33], 'a'),
        Question(question_prompts[34], 'd'),
        Question(question_prompts[35], 'a'),
        Question(question_prompts[36], 'b'),
        Question(question_prompts[37], 'd'),
        Question(question_prompts[38], 'd'),
        Question(question_prompts[39], 'c'),
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
def literature_in_english_2020():
    question_prompts=["""1. Criticism is a literary activity which seeks to
a. Find faults in a literary work
b. Analyse and evaluate a literary work 
c. compare and contrast novels
d. Discover the beauty of a literary work
""","""2. Analyse and evaluate a literary work 
 A situation where an actor addresses the audience without the other actors hearing him is called
a. Soliloquy
b.  Chorus
c. aside
d. Solo
""","""3. A band of singers and dancers in drama who act as a link between the play and the audience is the
a.  Chorus
b. Clown
c. Playwright
d. Cast
""","""4. A character whose name is used as the title of the text is
a. Antagonist
b. Round
c. eponymous
d. Flat
""","""5. In poetry, the term license implies 
a. Freedom to sell poems
b. Liberty the poets take with language
c. approval given to poets to compose poems
d. Honour given to deserving poets
""","""6. The person who takes the leading role in a play or novel is the
a. Protagonist
b. Actor
c.  antagonist
d. Actress
""","""7. A form of writing in which the poet write with nostalgia about simple village life is
a.  Ballad
b. Romance
c. epic
d. pastoral
""","""8. „We all make decisions. Sometimes it is wrong, sometimes it is right.' The speaker in the lines above is
a. Afraid
b. Excited
c. pessimistic
d. Reassuring
""","""9. 'Her neck is rope-like thin, long and skinny and her face sickly pale.' Okot p' Bitek: Song of Lawino. The style used in the lines is
a. Narrative
b.  Argumentative
c.  dramatic
d.  Descriptive
""","""10. 'once upon a time son, they used to laugh with their eyes; but now they only laugh with their teeth, while their ice-block-cold eyes search behind my shadow' G. Okara: Once upon a time The lines above are expressive of
a. Friendliness
b.  Insincerity
c.  jealousy
d. Sympathy
""","""11. 'when she opens her heart the savior's image!' Traditional: Love Song. the allusion in the lines above shows
 a. That the poet is a Christian
 b. That his love had a heart surgery
 c. the climax of love relationship
d. the anti-climax of love relationship
""","""12. 'Ay, your times were fine times indeed you have been telling us of them for many a long year. Here we live in an old rumbling mansion, that looks for all the world like an inn, but we never see company.' Goldsmith: She Stoops to Conquer. The figure of speech in the world like an inn is
a.  Irony
b. Euphemism
c. simile
d. Metaphor
""","""13. 'She gave out colanuts and together they ate to appease the angry earth and amadioha spoke through lightning and thunder.‟ The figure of speech in the third line above is
a. Personification
b.  Simile
c.  hyperbole
d.  Metaphor
""","""14. 'Ay, your times were fine times indeed you have been telling us of them for many a long year. Here we live in an old rumbling mansion, that looks for all the world like an inn, but we never see company.' Goldsmith: She Stoops to Conquer. The figure of speech in the world like an inn is 
a. hopeful
b. frustrated
c. regretful
d. Happy
""","""15. 'Her neck is rope-like thin, long and skinny and her face sickly pale.‟ Okot p‟ Bitek:Song of Lawino.The style used in the lines is
a.  Ridicule
b.  admonition
c.  anger
d.  sympathy
""","""16. „Ah. sunflower, weary of time who contests the steps of the sun seeking after that sweet golden clime where the travellers' Journey is done. The figure of speech in the second line above is
a.  Simile
b. metaphor
c. irony
d. Hyperbole
""","""17. „There is no art to find the minds construction on the face he was a gentleman on whom I built an absolute trust.' Shakespeare: Macbeth, The gentleman in the lines above
a. Annoys the speaker
b. fights with the speaker
c. detests the speaker
d. Betrays the speaker
""","""18. The flourishing fish market in the novel Is located In
a. St. Louis
b. Canary Island
c. Cleveland
d. Havana
""","""19. In summary, the old man can be described as
a. A Marxist
b.  an idealist
c. an optimist
d.  A realist
""","""20. As he struggled with fish and the sharks, the old man constantly talks to himself because
a.  He is afraid of the sea
b.  that is what all fishermen do
c.  it will make the sharks leave
d. The boy has left him
""","""21. To the old man, mandolin is
a. A symbol of oppression 
b. the cause of the ill-luck
c. a source of encouragement
d. Typical of lazy youths
""","""22. The subject matter of the novel is
a. Domestic violence
b.  religious zeal
c. child abuse
d. Marital infidelity
""","""23. In the Achike family, the character who is central to the theme is
a. Kambili
b.  mama
c. sisi
d. Jaja
""","""(24) ... The usual works you know these things. We'll dangle this babe before the Chief fora price. He will employ her and we can make use of her to get what we want. She will run the errands while we pick the bucks'. The babe in the excerpt aboverefers to
a.  Ogeyi
b. Alice
c. Ochuole
d. Aloho
""","""(25).'0! God forgive me. Is this a trap or what? God! Poor girl! Whatever is her reason for this dangerous decision.'
a.  Chief
b.  Doctor
c.  Inspector Inaku
d. ACP Yakubu
""","""26.based on Frank Ogodo0gbecheis Harvest of Corruption  . The central setting of the play is
a.  Mabu
b. Gbossa
c.  Darkin
d.  Jabu
""","""27.based on Frank OgodoOgbeche's Harvest of Corruption . ‘Good day (He says without looking up.) See me there by 4 p.m. Okay? Bye!' there in the excerpt above refers to the
a.  Court room
b.  Police station
c.  Airport
d. Akpara hotel
""","""28.based on Frank OgodoOgbeche's Harvest of Corruption5. Chief Ade Amaka is involved in which of the following crime?
a. Child trafficking
b. Land grabbing
c. Smuggling
d. Rigging
""","""29.based on Williams Shakespeare's Othello . 'ill-starred wench, pale as thy smock, When we shall meet at compt.' The device used in the lines above is
a. simile
b. pun
c. metaphor
d.  paradox
""","""30.based on Williams Shakespeare's Othello . Othello kills Desdemona because the
a. former is jealous
b. former's race is insulted
c. latter is a witch.
d. metaphor
""","""31.   Brabantio is opposed to the relationship between Othello and Desdemona because
a.  he prefers lago
b.  Othello is a Moor
c.  Roderigo woos her first.
d.  Desdemona is too young
""","""32.based on Williams Shakespeare's Othello . 'soft you; a word or two before you go. I have done the state some service, and they know't No more of that, I pray you, in your letters, When you shall these unlucky deeds relate ', The speech above is made. when the speaker is
a. travelling
b.  sick
c.  dying
d.  eloping
""","""33.based on Williams Shakespeare's Othello . '0 heaven; How got she out? 0 treason of the blood. Father, from hence trust not your daughters' minds By what you see them act. Is there not charms By which the property of youth and maidhood May be abused? The speaker of the excerpt above is
a. Brabantio
b. Othello
c. Gratiano
d. Roderigo
""","""34.based on Ammadarko's Faceless . The name of Kabria's husband is
a.  Kwei
b.  Kpakpo
c. Adade
d. Ottu
""","""35.based on Ammadarko's Faceless . 'She was both a child and an adult and could act like both The character being referred to in the excerpt above is
a.  Fofo
b.  Baby T.
c.  Odarley
d.  Obea.
""","""36.based on Ammadarko's Faceless . The question is based on AmmaDarko's Faceless. The writer of the novel is from
a. Germany
b.  Scotland
c. Ghana
d. Nigeria
""","""37.based on BayoAdebowale's Lonely Days. . Windows in mourning in Kufi wear garments that are
a. red
b. black
c. white
d. dull
""","""38.based on BayoAdebowale's Lonely Days  . In the novel bage cap signifies everlasting
a. happiness
b. sorrow
c. freedom
d. despair
""","""39.based on BayoAdebowale's Lonely Days . Yaremiss only son is
a.  Alani
b.  Wande
c. Olode
d. Deyo
""","""40.based on Richard Wright's Native Son  . Bigger burns Mary body in the
 a. toilet
b. basement
c.  backyard
d.  wardrobe"""]
    question = [
        Question(question_prompts[0], 'b'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'd'),
        Question(question_prompts[3], 'a'),
        Question(question_prompts[4], 'b'),
        Question(question_prompts[5], 'a'),
        Question(question_prompts[6], 'c'),
        Question(question_prompts[7], 'd'),
        Question(question_prompts[8], 'd'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'c'),
        Question(question_prompts[11], 'c'),
        Question(question_prompts[12], 'a'),
        Question(question_prompts[13], 'c'),
        Question(question_prompts[14], 'a'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'd'),
        Question(question_prompts[17], 'c'),
        Question(question_prompts[18], 'a'),
        Question(question_prompts[19], 'd'),
        Question(question_prompts[20], 'c'),
        Question(question_prompts[21], 'b'),
        Question(question_prompts[22], 'a'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'a'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'd'),
        Question(question_prompts[27], 'c'),
        Question(question_prompts[28], 'a'),
        Question(question_prompts[29], 'b'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'c'),
        Question(question_prompts[32], 'a'),
        Question(question_prompts[33], 'c'),
        Question(question_prompts[34], 'a'),
        Question(question_prompts[35], 'c'),
        Question(question_prompts[36], 'b'),
        Question(question_prompts[37], 'c'),
        Question(question_prompts[38], 'a'),
        Question(question_prompts[39], 'b'),
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