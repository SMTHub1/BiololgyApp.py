def Commerce_2015():
    students = dict()
    names = input("type your name here")

    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False

    question_prompts = [
 """2. The wealth of a nation depends on the volume of its?
A. bilateral trade activities
B. commercial activities
C. multilateral trade activities
D. stock market
\n """,
"""3. Which of the following can be used to differentiate skilled and unskilled labour?
A. Education and training
B. Available resources
C. Level of commitment
D. Salaries and wages
\n """,
"""4. A doctor who attends to patients at home after his official duty is?
A. a community development worker
B. a direct service worker
C. an indirect service worker
D. a direct and an indirect service worker
\n """,
"""5. Manufacturing and constructive activities are classified under?
A. primary production
B. tertiary production
C. secondary production
D. direct service
\n """,
"""6. The rewards of rents, wages, interests and profits accrue from?
A. capital, labour, land and entrepreneur respectively
B. land, entrepreneur, labour and capital respectively
C. land, labour, capital and entrepreneur respectively 
D. labour, entrepreneur, land and capital respectively
\n """,
"""7. The factor of production that is subject to depreciation is?
A. capital
B. land
C. labour
D. entrepreneur
\n """,
"""8. Division of labour ultimately leads to?
A. conservation
B. integration
C. specialization
D. repetition
\n """,
"""9. A worker who process rice is engaged in?
A. constructive activity
B. commercial activity
C. extractive activity
D. manufactural activity
\n """,
"""10. After-sales service is a function usually rendered by? 
A. a retailer
B. a wholesaler
C. an agent
D. an entrepreneur
\n """,
"""11. A trend in retailing which enables consumers to have free access to different products is?
A. after-sales services
B. branding
C. self-services
D. vending machine
 \n """,
"""12. The activity which entails buying of goods in bulk and selling in small quantities to retailers is?
A. assembling
B. wholesaling
C. retailing
D. merchandising
\n """,
"""13. The comparison of a country's visible and invisible exports and imports expressed in monetary term is?
A. balance of payment
B. terms of trade
C. balance of trade
D. terms of payment
\n """,
"""14. The document that gives an importer a freehand to obtain goods from any manufacturer is?
A. a consular invoice
B. a closed indent
C. an open indent
D. a freight note
\n """,
"""15. Entrepot trade usually occurs in?
A. exchanging goods within a
nation
B. exchanging goods among
countries
C. importing goods to be reexported
D.exporting goods to be reimported
\n """,
"""16.The document issued to a port authority when goods are deposited is a? 
A. dock landing account
B. bill of sight
C. bill of lading
D. dock warrant
\n """,
"""17. The details of the goods required by the purchaser is outlined in?
A. a consular invoice
B. an indent
C. an invoice
D. a certificate of origin
\n """,
"""18. Selling goods in foreign countries at price below their marginal cost is?
A. dumping
B. depreciation
C. devaluation
D. discounting
\n """,
"""19. A process of creating more market for a product is through?
A. consumerism
B. marketing
C. advertising
D. repositioning
\n """,
"""20. One of the merits of television as a medium of advertising is that it?
A. is prone to censorship
B. is relatively cheap
C. has more sensory stimulation
D. has more network coverage
\n """,
"""21. The best mode of ensuring that items posted got to the named address through?
A. recorded delivery
B. registered mail
C. certificate of posting
D. express mail
\n """,
"""22. A businessman who undertakes the hull insurance policy is aiming at?
A. concerting losses on damages to the cargo
B. protecting injured crew in the ship
C. averting payment of the freight 
D. covering damages to the body of the ship
\n """,
"""23. An agent who brings a customer into business contact with his principle is known as?
A. a del credere agent
B. an auctioneer
C. a factor
D. a broker
\n """,
"""24. A major hindrance to tourism growth in Nigeria is?
A. absence of genuine touroperators
B. lack of tourism master plan
C. inadequate tourist centres
D. non-compliance to immigrationlaws
\n """,
"""25. The warehouse that is ownedand controlled by the government is a?
A. wholesalers' warehouse
B. public warehouse
C. state warehouse
D. manufacturers' warehouse
\n """,
"""26. One of the main features of a partnership is?
A. limited liability
B. lack of corporate existence
C. unlimited membership
D. lack of mutual confidence
\n """,
"""27. An arrangement by independent firms to share the market of their products on quota basis is referred to as?
A. trust
B. integration
C. syndicate
D. cartel
\n """,
"""28. An illegal arrangement by manufacturers to control the price or condition of sale in a product is
A. Ring
B. factoring
C. consortium
D. merger
\n """,
"""29. A public company with an authorized capital of N60,000,  issued N36,000 shares at 150k each. What is its capital?
A. ₦60,000
B. ₦36,000
C. ₦54,000
D. ₦90,000
\n """,
"""30. One of the functions of NACCIMA is?
A. negotiating with labour unions in matters of wages and conditions of service
B. pooling of members' resources for longterm investment
C. disseminating information to members on matters relating to tariffs
D. ensuring uniformity in labour matters and industrial relations
\n """,
"""31. A characteristics of money which ensures that its value is not lost is?
A. homogeneity
B. easy portability
C. divisibility 
D. relative scarcity
\n """,
"""32. The instrument used in the capital market is?
A. treasury bills
B. bill of exchange
C. stock
D. debenture
\n """,
"""33. A per-requisite for admission into the Second Tier Securities Market is for a company to?
A. make 20% of its equity share available to the public for subscription
B. have a minimum of 100 shareholders
C. have a maximum of 100 shareholders
D. make 10% of its equity share available to the public for subscription
\n """,
"""34. The three components of staffing are? 
A. recruitment, interview and appointment
B. recruitment, test and placement
C. recruitment, selection and appointment
D. recruitment, selection and placement
\n """,
"""35. Which of the following is a matter of personal preference on the part of a superior officer?
A. Unity of command
B. Span of control
C. Delegation of authority
D. Unity of direction
\n """,
"""36. The conversion of raw materials into finished goods leads to the creation of?
A. form utility
B. product utility
C. possession utility
D. place utility
\n """,
"""37. The main concern of marketing concept is to?
A. reduce the number of retail outlets
B. identify consumer needs and satisfy them
C. increase sales to meet consumer needs
D. encourage division of labour
\n """,
"""38. The best pricing strategy for a company that produces warm clothing is?
A. target return pricing
B. bid pricing
C. variable pricing
D. product line pricing
\n """,
"""39. The deliberate and sustained efforts of an organization towards the creation of goodwill for its products and services is through?
A. public relations
B. advertising
C. sales promotion
D. rebranding
\n """,
"""40. The label on a product such as 'pampers' is a type of? 
A. trademark
B. branding
C. packaging
D. patent right
\n """,
"""41. An opportunity to reject a binding contract at will by a third party is said to be a?
A. valid contract
B. quasi contract
C. voidable contract
D. conditional 
\n """,
"""42. An agency contract must involve?
A. a principal and a consumer
B. a principal and a producer
C. a principal and a third party
D. a principal and an agent
\n """,
"""43. The difference between trademark and patent right is that the latter?
A. gives exclusive right to import a particular good
B. is conferred by the government 
C. confers monopoly on a product
D. confers exclusive right to publish literary works
\n """,
"""44. Which of the following is a function of consumerism?
A. Protecting consumers' rights
B. providing consumers' choice
C. providing consumers' needs
D. Making profiteering impossible
\n """,
"""45. A printed copy of processed information from the computer is the?
A. soft copy
B. file copy
C. scanned copy
D. hard copy
\n """,
"""46. The central working system of a computer used for data processing is the?
A. memory unit
B. monitor
C. floppy disk drive
D. hard drive 
\n """,
"""47. The major problem confronting Cyber Cafe operators is?
A. advance fee fraud by clientele
B. poor network coverage
C. high operating costs
D. copyright violations by clients
\n """,
"""48. A device that enables the downloading of information from the internet is the?
A. floppy drive
B. compact disk
C. modem
D. Bluetooth
\n """,
"""49. In e-banking, ATM means
A. Authentic Teller Machine
B. Automatic Teller Machine
C. All-purpose Teller Machine
D. Automated Teller Machine
\n """,
"""50. One way by which a business can discharge its social responsibility to its community is to?  
A. hold monthly meetings of its customers
B. building houses for its executives
C. award scholarship to staff children
D. build public health centres
\n """,

    ]
questions = [

        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "C"),
        Question(question_prompts[39], "B"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "C"),
        Question(question_prompts[42], "B"),
        Question(question_prompts[43], "B"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "A"),
        Question(question_prompts[46], "A"),
        Question(question_prompts[47], "D"),
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
        Commerce_2015()