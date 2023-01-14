from Question import Question
def Commerce_2020():
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
        """1. Which of the following regulates and controls the activities in the Nigeria Stock Exchange?
A. SEC
B. BPE
C. CBN
D. NDIC
\n """,
"""2. The payment made by a speculator to the buyer when he is unable to deliver stocks on the agreed date is
A. backwardation
B. Franco
C. arbitrage
D. contango
\n """,
"""3. Part payments made on allotted shares by subscribers is usually the
A. issued capital
B. subscribed capital
C. called-up capital
D. authorized capital 
\n """,
"""4. A loan to a customer with a cheque account at a bank in which the account is allowed to go into debit is
A. advance
B. over draft
C. commission
D. interest
\n """,
"""5. Money is generally acceptable for transaction due to
A. the rule of the law
B. its acceptability in the global market
C. the legal backing
D. the Central Bank Governor's signature
\n """,
"""6. Trade fairs in Nigeria are organized by
A. Ministry of commerce and industry
B. chambers of commerce
C. The federal Government 
D. Manufacturer's Association of Nigeria
\n """,
"""7. Goods and services are made available to consumers through
A. the advertising agency
B. sales promotion
C. the channel of distribution
D. the middle men
\n """,
"""8. An organization which focuses on consumer satisfaction is practising
A. marketing concept
B. selling concept
C. consumerism
D. market segmentation
\n """,
"""9. One of the major disadvantages of pipeline transportation is its
A. high maintenance cost
B. high cost of construction
C. Limitation in scope
D. vulnerability to climate changes 
\n """,
"""10. The business organization that can effectively combinemanagement with control is
A. co-operation society
B. public limited liability company
C. private limited liability company
D. sole proprietorship
\n """,
"""11. An arrangement by independent firms to share the market of their products on quota basis is referred to as
A. cartel
B. syndicate
C. trust
D. integration
\n """,
"""12. The warehouse that is owned and controlled by the government is a
A. state warehouse
B. wholesalers' warehouse
C. public warehouse
D. manufacturers' warehouse
\n """,
"""13. In a public limited liability company, planning, is carried out by
A. employees
B. the chairman of the board
C. shareholders
D. manufacturers' warehouse
\n """,
"""14. One of the major problems of a sole proprietor is sourcing for
A. funds
B. labour
C. raw materials
D. machineries
\n """,
"""15. Balance of payments is made up of
A. currency and capital items
B. visible and current items
C. visible and invisible items
D. visible and capital items
\n """,
"""16. The four P's of marketing are:
A. Price, product, property and place 
B. Product, place, process and promotion
C. Price, production, place and property
D. Price, product, place and promotion
\n """,
"""17. The inter for is a system of telecommunications used for
A. sending electronic messages
B. communicating long-distance messages
C. sending and receiving text messages
D. communicating messages through telegrams
\n """,
"""18. The major determinant of fire insurance premium is the
A. usefulness of the property to the owner
B. type and structure of the property to be insured
C. extent of fixed damage anticipated
D. owner of the property to be insured 
\n """,
"""19. Capital to a business is technically
A. an asset
B. a project
C. a liability
D. an expense
\n """,
"""20. The factor which critically determines the choice of occupation is
A. skill
B. training
C. aptitude
D. interest
\n """,
"""21. From which of the following source can partnerships increase their capital?
A. Sales of shares
B. Admission of new partners
C. Discharge of mortgage
D. Grants from relations
\n """,
"""22. In Nigeria, the ministry in charge of registering trade associations is that of 
A. culture and tourism
B. finance
C. industries
D.commerce
\n """,
"""23. The shares of a company listed on the stock exchange for sale are referred to as
A. quoted shares
B. issue shares
C. deferred shares
D. registered shares
\n """,
"""24. Charges for loans paid by commercial banks to the central bank of Nigeria are called
A. Credit charges
B. bank rates
C. bank charges
D. interest rates
\n """,
"""25. The act of a person employing another to enter into contract on his behalf is known as
A. agency 
B. bilateral agreement
C. business
D. sale of goods
\n """,
"""26. Social responsibility is the ability of organization to
A. operate without disrupting the very essence of the environment
B. tackle the socio-economic problems of its community
C. meet the needs of its community
D. contribute to sustaining and developing its community
\n """,
"""27. An author's exclusive right to his published and unpublished works is known as
A. constitutional right
B. copy right
C. author right
D. patent right
\n """,
"""28. Awarding scholarships and sponsoring sports by a business organization are examples of 
A. social responsibility
B. advertising strategy
C. marketing strategy
D. economic responsibility
\n """,
"""29. One way by which government reduces the repatriation of capital is through
A. divestiture
B. naturalization
C. nationalization
D. indigenization
\n """,
"""30. The maximum number of shareholders in a public liability company is
A. one hundred
B. unlimited
C. fifty
D. twenty
\n """,
"""31. Bank overdraft as a shortterm source of fund is
A.a current liability
B.an overdrawn account
C. grade to a newly opened account
D. repayable after more than a year
\n """,
"""32.The above chart represents the
A. marketing mix relationship
B. product mix relationship
C. advertising mix relationship
D. promotion mix relationship
\n """,
"""33. The main documents sent to an importer of goods by the exporter are
A. indent, bill of certificate of origin, invoice and bill of exchange
B. certificate of origin, bill of exchange, invoice insurance,policy, indent and bill of lading  Product  Price Promotion  Customer  Place 
C. bill of lading, invoice, insurance policy, consular invoice, certificate of origin and bill of exchange
D. invoice, consular invoice, certificate of origin, freight note, indent and insurance policy
\n """,
"""34. A company which issues a promissory note in lieu of payment for goods purchased
A. is not bound to renew the note before payment
B. can return the goods purchased and refuse to pay
C. can refuse to pay on due date since it is only a promise
D. is bound to redeem the note for cash on due date
\n """,
"""35. The two main categories under which marine losses fall in to are
A. total loss and partial loss
B. voyage policy loss and time policy loss
C. particular loss and average loss
D. actual loss and general loss.
\n """,
"""36. Chinyere agreed to make address for Halima with September 20,1995 as the delivery date. If the dress was not ready on that date, Halima could
A. seize another gown from chinyere's shop
B. regard the contract between them as terminated
C. sue chinyere for specific performance
D. sue chinyere for damage.
\n """,
"""37. A disadvantage of personal selling is that it 
A. increase a company's number of customers
B. reduces a company area of patronage
C. increases a company's operating costs
D. decreases a company's operating costs.
\n """,
"""38. Which of the following has powers to order withdrawal of a particular food item from circulation?
A. Food and Drugs Department of the Federal Ministry of Health
B. Federal High Courts in Nigeria
C. Standard Organization of Nigeria
D. Local Government Health Inspectors
\n """,
"""39. Nationalization of an industry means that its ownership becomes that of
A. tax payers
B. indigenes
C. government 
D. shareholders
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "A"),
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
        Commerce_2020()

def Commerce_2019():
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
        """1. The rate where a country's exports exchange for its imports is called
A. terms of payments
B. terms of trade
C. balance of payments
D. balance of trade.
\n """,
 """2. The use of coin-operated machines to sell goods is a form of
A. mail-order selling
B. personal selling
C. retailer
D. wholesaling.
\n """,
 """3. The insurance policy which provides full cover against all risks at sea is known as
A. marine voyage policy insurance
B. marine freight insurance
C. policy free of particular average
D. policy with particular average.
\n """,
"""4. The practices by which an insurance company accept a very large risk and latter shares it with other insurance companies is called
A. contribution
B. indemnity
C. subrogation
D. re-Insurance.
\n """,
"""5. A machine which enables sales without the physical presence of a sales attendant is a
A. vending machine
B. computer machine
C. fax machine
D. telex machine.
\n """,
"""6. What document is required when a country imposes ad valorem import duties on goods?
A. Consular invoice
B. A bill of lading
C. A shipping note
D. A mail transfer.
\n """,
"""7. A business whose owners enjoy loan facilities on the basis of personal goodwill.
A. community bank
B. co-operative society
C. commercial bank
D. thrifts society.
\n """,
 """8. Which of the foli0Wing is not a veritable source of funds to a public limited liability company?
A. advances and loans from bank
B. government financial grants
C. funds from the sale of shares
D. internally generated funds.
\n """,
 """9. The tern Plc implies that the shares are available
A. publicity on the stock exchange
B. publicity in commercial bank
C. privately on the stock exchange
D. to the public at the company.
\n """,
 """10. Which of these is both merit and demerit in partnership? 
A. Its unlimited nature
B. The number of partners
C. The withdrawal of a major of partner
D. The bearing of risk.
\n """,
 """11. A factor necessary for siting of a warehouse is nearness to
A. labour
B. capital
C. consumers
D. raw materials.
\n """,
 """12. Pooling of risk in insurance means that
A. two people can pool their risks to be insured
B. compensation are paid out of a common fund
C. insurance companies should encourage taking risks
D. two insurance companies canA. Benin and Nigeria
\n """,
 """14. A core investor in the current phase of privatization in Nigeria is one who
A. has the technical know-how of the enterprises
B. can mobilize foreign currency equivalent to the value of enterprises
C. will be at the core of the enterprises
D. can afford to buy most of the shares of the enterprises.
\n """,
 """15. The process of dividing tasks into jobs and departments and delegating authority is known as
A. organizing
B. staffing
C. leading
D. directing.
\n """,
 """16. Communication process involves the transmission of a message over a selected channel to the
A. encoder
B. receiver
C. audience
D. sender.
\n """,
 """17. A transporter who had to sell perishable goods without the prior authority of the owner becomes an agent by
A. estoppel
B. conduct
C. necessity
D. ratification
\n """,
 """18. Poor sewage disposal oil spill and indiscriminate refuse dumping all lead to
A. land and water pollution
B. air and water pollution
C. land pollution
D. water pollution.
\n """,
 """19. A major function of a Chamber of Commerce
A. promoting both home and foreign trade
B. increasing productivity
C. maximizing profit
D. promoting trade in a particular
\n """,
 """20. Which of the middle men in the channel of distribution has title to the goods he distributes?
A. The retailer
B. The limited wholesaler
C. The agents
D. The merchant wholesaler.
\n """,
 """21. A seller attracts and retains patronage by
A. rendering pre-sales services
B. enhancing sales promotion
C. render customer service
D. enhancing public relations.
\n """,
 """22. A bond which attracts only interest but leaves the capital unpaid is referred to as 
A. a redeemable bond
B. an irredeemable bond
C. a long-term loan
D. a development bond.
\n """,
 """23. An announcement of a person's willingness to enter into a contract is referred to as
A. consideration
B. an acceptance
C. a proxy
D. an offer.
\n """,
 """24. The macro-environmental forces and trends which are a constraint on business operations are referred to as
A. external factors
B. internal factors
C. economic factors
D. technological factors.
\n """,
 """25. A proposed company may not be registered if
A. it has no paid up capital
B. it has no asset of its own 
C. it does not put “limited” after its proposed name
D. the name conflicts with that of another.
\n """,
 """26. An example of a cartel is
A. EU
B. AU
C. OPEC
D. ECOWAS.
\n """,
 """27. In which of the following will the number of words used determine the cost of message sent?
A. E-mail
B. Telex
C. Telegram
D. Telephone.
\n """,
 """28. The Transmission of telephone services from one country to another is facilitated by
A. international facility
B. communication satellite
C. internet services 
D. interconnectivity.
\n """,
 """29. After-sales service is a function usually rendered by
A. an entrepreneur
B. an agent
C. wholesale
D. a retailer.
\n """,
 """30. The activity which entails buying of goods in bulk and selling in small quantities to retailers is
A. wholesaling
B. assembling
C. retailing
D. merchandising.
\n """,
 """31. An individual that links the producer with the retailer is
A. a principal
B. an agent
C. an entrepreneur
D. a wholesale.
\n """,
 """32. One of the functions of a retailer is the
A. breaking of bulk
B. financing of production activities
C. provision of credit facilities to relations
D. provision of jobs for customers.
\n """,
 """33. The type of letters that are delivered through the normal mail or by airmail express service is referred to as
A. airmail letters
B. inland letters
C. registered letters
D. express letters.
\n """,
 """34. A business organization that exploits the capabilities of a member to remedy the weaknesses of another is a
A. co-operative
B. joint venture
C. partnership 
D. nominal partnership.
\n """,
 """37. Insurance against burglary is an example of
A. non-indemnity insurance
B. fidelity guarantee insurance
C. non-insurable risk
D. indemnity insurance.
\n """,
 """38. The principle which requires the insurance company to disclose to the proposer all material facts of the risk to be covered is
A. contribution
B. subrogation
C. proximate cause
D. uberrimae fidei.
\n """,
 """39. The document that explains the types of shares available for sale to the public is
A. an invoice
B. an open indent
C. a closed indent
D. a prospectus.
\n """,
 """40. Which of the following attracts only interest but leaves the capital unpaid?
A. A redeemable bond
B. a long-term loan
C. a development bond
\n """,


    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "B"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),

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
        Commerce_2019()
def Commerce_2018():
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
        """1. Compulsory dissolution of a business can arise from
A. a declaration by  a court
B. an agreement by the owners
C. an unfavourable economic climate
D. the termination of its life.
\n """,
"""2. A proforma invoice is not required when
A. goods are sent on approval
B. quoting for the supply of goods
C. final prices are uncertain
D. dealing regularly with a customer.
\n """,
"""3. Given:     ₦ Opening stock    40,000 Purchases    115,000 Closing stock    60,000 Sales     250,000 What is the cost of goods sold?
A. ₦50,000
B. ₦30,000 
C. ₦95,000
D. ₦155,000
\n """,
"""4. In the channel of distribution, which of the following sets is entirely made up of middle men?
A. Manufacturers, consumers and retailers
B. Wholesalers, retailers and agents
C. Retailers, manufacturers, and wholesalers
D. Wholesalers, agents and consumers
\n """,
"""7. The conversion of raw materials into finished product creates
A. form utility
B. marginal utility
C. time utility
D. place utility
\n """,
"""8. Commerce makes it possible for man to live in a
A. complex and organized society
B. simple and organized society 
C. society characterized by subsistency
D. society characterized by dependency
\n """,
"""9. The insurance principle that requires full disclosure of information on the insured is known as
A. caveat empto
B. subrogation
C. uberrimae fidei
D. indemnity
\n """,
"""10. Production involves
A. changing the form of goods, moulding and making, them available as needed
B. making goods available when and where needed
C. the assembling of all necessary parts to produce
D. the manufacturing of goods and provision of services
\n """,
"""11. A merchant wholesaler is referred to as 
A. a factor
B. rack gobber
C. a broker
D. del-credere agent
\n """,
"""12. A proforma invoice is sent to inform a buyer about the
A. prices of goods
B. quantity of goods
C. quality of goods
D. designation of goods
\n """,
"""13. Capital as a factor of production can be used for
A. goods that are useful in business
B. money that is regarded as assets
C. services that provide satisfaction
D. input for further production
\n """,
"""14. The agency that currently oversees the privatization and commercialization processes in Nigeria is the
A. Bureau of public enterprises
B. Nigerian stock exchange
C. Technical committee on privatization and commercialization
D. securities and exchange commission
\n """,
"""15. The payment made periodically in respect of an insurance policy entered into is known as
A. premium
B. surrender
C. bond
D. commission
\n """,
"""16. An example of services rendered by NIPOST is
A. courier
B. electronic mail
C. mail delivery
D. Telephone
\n """,
"""17. Ships that sail across the ocean and operate on scheduled time tables are 
A. coastal liners
B. tramp steamer
C. ocean liners
D. ferries
\n """,
"""18. Non-insurable risks include
A. death
B. marine problems
C. damage to property
D. gambling
\n """,
"""19. The most important right of the employee in discharging his duties to the employer is the right to
A. job securities
B. annual leave
C. regular enrolments
D. working facilities
\n """,
"""20. The most dangerous pollution is
A. Air pollution
B. water pollution
C. Soil pollution
D. noise pollution 
\n """,
"""21. Tourism can be classified as
A. visible exports
B. invisible exports
C. tangible imports
D. intangible imports
\n """,
"""22. The inputs. output and central processing units are the basic components of a
A. software
B. hardware
C. memory
D. printer
\n """,
"""23. Consumers require protection against exploitation to ensure
A. the sale of quality products
B. increased aggregate demand
C. adequate consumer awareness
D. availability of product variety
\n """,
"""24. The business environment that takes into cognizance the age distribution, ethnic mix and educational level of Consumer is
 A. cultural environment
B. national environment
C. demographic environment
D. economic environment
\n """,
"""25. An activity that involves derivation of raw materials from land and sea is
A. agricultural
B. extraction
C. construction
D. farming
\n """,
"""26. The art of soap-making is an example of
A. secondary occupation
B. primary occupation
C. construction occupation
D. tertiary occupation
\n """,
"""27. The central focus of commercial activities is
A. pricing
B. marketing
C. advertising
D. farming 
\n """,
"""28. An aid to trade associated with communication is
A. insurance
B. ware housing
C. banking
D. transportation
\n """,
"""29. Which of the following can be used to differentiate skilled and unskilled labour?
A. Available resources
B. Education and training,
C. Salaries and wages
D. Level of commitment
\n """,
"""30. A doctor who attends to patients at home after his official duty is
A. a direct and indirect service worker
B. An indirect service worker
C. A direct service worker
D a community developer
\n """,
"""31. An oil exploration company is engaged in 
A. extractive occupation
B. constructive occupation
C. secondary production
D. tertiary production
\n """,
"""32. Services rendered to the public is provided by
A. governments
B. domestic servants
C. professionals
D. civil servants
\n """,
"""33. If a customer pays within nine days of receiving goods and takes advantage of 3% off the invoice price, this is stated as
A. 30; net 9/3
B. 9/30; net 3
C. 9/27 net 30
D. 3/9; net 30
\n """,
"""34. Which of the following is a characteristic of a bearer cheque?
A. it is made payable to whoever presents it
B. it is made with transverse lines 
C. it is only payable into the payee's account
D. it is made without transverse
\n """,
"""35. A country is said to be experiencing an unfavourable balance of trade if her
A. exports exceed imports.
B. visible exports exceed visible imports.
C. imports and exports are equal.
D. visible imports exceed visible exports.
\n """,
"""36. The type of labour that makes use of physical efforts in production procession is the
A. skilled labour
B. unskilled labour
C. white-collar job
D. blue-collar job.
\n """,
"""37. Cooperation and friendliness are enhanced among nations through inter-dependence necessitated by
A. Agriculture
B. social-cultural activities
C. Tourism
D. Commerce
\n """,
"""38. One of the products of an extractive industry is
A. a shoe
B. a textile material
C. an iron ore
D. an air plane
\n """,
"""39. An important feature of land is that
A. is an active factor of production
B. has elastic supply
C. is subject to return to scale
D is heterogeneous in nature
\n """,
"""40. One of the major determinants of the volume of production is
A. the availability of bank
B. the market size
C. government policy
D. sex distribution
\n """,



    ]

    questions = [

        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),

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
        Commerce_2018()
def Commerce_2017():
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
        """1. A proforma invoice is not required when
A. dealing regularly with a customer
B. quoting for the supply of goods
C. goods are sent on approval
D. final prices are uncertain.
\n """,
"""2. A distinguishing characteristic of a limited liability company is that
A. is a collection of many sole proprietors
B. can sue and be sued
C. is a multiple partnership
D. has limited resources
\n """,
"""3. Construction activities include the building of houses and roads as well as
A. shoe-making
B. black smiting
C. brick laying
D. car assembling
\n """,
"""4. Which of the following information is contained in the Articles of Association of a limited liability company?
A. Objectives of the company
B. Rights and obligations of directors
C. Amount of share capital
D. Limitation of liability of share holders
\n """,
"""5. Which of the following contributed least to the evolution of commercial activities in Nigeria?
A. Development of banks
B. Development of transportation
C. Development of currencies
D. Development of trader's union.
\n """,
"""6. One of the factors which critically determines the choice of occupation is
A. skill
B. training 
C. interest
D. aptitude
\n """,
"""7. Tourists with no fixed address in a town may receive letters from the post office through 
A. poste resante
B. recorded delivery
C. post master
D. parcel post
\n """,
"""8. On liquidation of a public limited liability company, the residual owners are the
A. debenture holders
B. creditors
C. preference shareholders
D. ordinary shareholders
\n """,
"""9. The major factors that facilitate merchandising are
A. banking_ insurance and transportation
B. management, insurance, and advertising 
C. communication. advertising, and banking
D. trading, warehousing and production
\n """,
"""10. The pivot on which the wheel of commerce rotates is
A. tariff
B. taxation
C. price
D. trade
\n """,
"""11. The major procedures in the purchase and sale of goods are enquiry
A. order, sale and invoice
B. quotation, order and invoice
C. placement, order and invoice
D. bargain, order and invoice.
\n """,
"""12. An advantage of hire purchase to the customer is the
A. low interest rate chargeable
B. increase in turn over and profits 
C. economics of scale in production
D. possession of goods before payment
\n """,
"""13. The agency in Nigeria which ensures that products confirm to government quality specifications is the
A. Nigerian Consumers Association
B. Standards Organization of Nigeria
C. Nigerian Chamber of Commerce
D. Manufacturer's Association of Nigeria.
\n """,
"""14. The most widely used computer language that focuses on solving science oriented problems is
A. COBOL
B. ADA
C. BASIC
D. FORTRAN
\n """,
"""15. An essential factor for evaluating the different sources of funds for a business is the
A. ownership structure of the business concern
B. burden of cost and repayment
C. size and the type of the business
D. decree establishing the business
\n """,
"""16. In the primary market, new shares are issued through
A. personal selling, publicity and advertising
B. advertising, a prospectus and a bill of exchange
C. a prospectus, an offer for sale and placing
D. a prospectus, offer for sale and a bill of exchange
\n """,
"""17. One of the advantages of commercialization is that it
A. increases the salaries of workers 
B. encourages entrepreneurship
C. gives workers on-the-job training
D. motivates government to establish more business
\n """,
"""18. Given:     ₦Sales     15,000Opening stock    5,600 Purchases    9,700 Closing stock    4,400 Gross profit    4,500Net profit     2,000 From the above data, calculate the rate of turn over
A. 218 times
B. 3.50 times
C. 3.00 times
D. 2.00 times
\n """,
"""20. The type of communication from a superior to a subordinate in an organization is referred to as
A. Consular invoice
A. downward communication
B. horizontal communication
C. lateral communication
\n """,
"""21. The safety and quality of products are the social responsibility of
A. the Manufacturer's Association of Nigeria
B. the Corporate Affairs Commission
C. business organization
D. the Standard Organization of Nigeria
\n """,
"""22. The members of ECOWAS include?
A. Togo, Nigeria and Ghana
B. Burkina Faso, Nigeria, Niger and Mauritania 
C. Guinea, Mali, Cameroon and Nigeria
D. Nigeria, Chad, Gabon and Cape Verde
\n """,
"""23. One of the functions of Nigeria Ports Authority is the provision of
A. facilities to ensure that goods get to their destinations
B. courier services to ensure specific delivery
C. shelter for operators of cargoes
D. facilities to enhance the speedy loading and offloading of cargoes
\n """,
"""24. A document which advertises the shares of a company is known as
A. deed
B. prospectus
C. dividend warrant
D. memorandum of satisfaction.
\n """,
"""25. An association to which all Chambers of Commerce in Nigeria are affiliated is the 
A. National Association of Chambers of Commerce
B. Nigeria Labour Congress
C. Nigeria Stock Exchange
D. Nigeria Association of Chambers of Commerce, Industry, Mines and Agriculture.
\n """,
"""26. An aspect of commerce that facilitates the distribution of product is
A. advertising
B. branding
C. transportation
D. trading.
\n """,
"""27. Unresolved disputes between the employer and employees are usually referred to the
A. industrial arbitration tribunal
B. disciplinary committee
C. code of conduct bureau
D. personal unit.
\n """,
"""28. A chain store usually combines the features of
A. hyper markets and stalls
B. multiple shops and hyper markets
C. multiple shops and departmental shops
D. mail order business and multiple shop.
\n """,
"""29. Which of the following is a matter of personal preference on the part of a superior officer?
A. Delegation of authority
B. Unity of direction
C. Span of control
D. Unity of command.
\n """,
"""30. Manufacturing and constructive activities are classified under
A. direct-service
B. primary production
C. tertiary production
D. secondary production.
\n """,
"""32. The three main classification of occupation are
A. industry, commerce and services.
B. manufacturing, industry and trading
C. farming, banking and trading
D. construction, trade and services.
\n """,
"""33. The person who undertakes life assurance is said to be an  Commerce  Trade I  II Foreign  Retailer Wholesaler Export Import
A. assurer
B. insurer
C. insured
D. assured.
\n """,
"""34. A business organization must always consider the overall effect of its actions on the
A. profit
B. society
C. product
D. competitor.
\n """,
"""35. An undertaking given by a person to another assuring his integrity is
A. subrogation
B. insurable interest
C. proximate clause
D. fidelity guarantee.
\n """,
"""36. Which of the following is a quality of money?
A. scarcity
B. availability
C. convertibility 
D. indivisibility.
\n """,
"""37. The distribution of petroleum products in Nigeria is through
A. the bank
B. air
C. sea
D. road.
\n """,
"""38. The business that focuses attention on the quality of the goods produced by precisely knowing what the consumers desire is said to be operating the
A. marketing concept
B. promotion mix
C. product orientation
D. product mix.
\n """,
"""39. A floating policy is an example of
A. marine insurance
B. motor insurance
C. fire insurance
D. actuaries insurance.
\n """,
"""40. The art of soap making is an example of a
A. construction occupation
B. tertiary occupation
C. primary occupation
D. secondary occupation.
\n """,



    ]

    questions = [

        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "A"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "A"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),

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
        Commerce_2017()
def Commerce_2016():
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
        """2. Cooperation and friendliness are enhanced among nations through interdependence necessitated by
A. tourism
B. commerce
C. agriculture
D. socio-cultural activities
\n """,
"""3. One of the products of an extractive industry is
A. an airplane
B. an iron ore
C. a shoe
D. a textile material
\n """,
"""4. The payment for direct service is usually made by the
A. local authority
B. community
C. government
D. individual
\n """,
"""5. An important feature of land is that it
A. has an elastic supply
B. is an active factor of production
C. is heterogeneous in nature
D. is subject to returns to scale
\n """,
"""6. One of the major determinants of the volume of production is
A. the market size
B. the availability of banks
C. sex distribution
D. government policy
\n """,
"""7. Mrs. Jones who lives in the riverine community of Rivers State makes her living through crabbing and fishing. This type of occupation she is in is
A. commercial
B. manufacturing
C. service
D. extractive
\n """,
"""8. To eliminate middlemen, there should be a retail outlet such as
A. producer co-operative
B. consumer co-operative
C. multiple shop
D. departmental store
\n """,
"""9. The document issued by a port authority for goods deposited is a
A. bill of lading
B. bill of sight
C. consular invoice
D. warehouse warrant
\n """,
"""10. The document submitted to the customs authority when full description of imported goods is not provided is
A. a bill of sight
B. an invoice
C. an indent
D. a bill of entry
\n """,
"""11. The role of customs and exercise authority includes the
A. control of the flow of goods in and out of the country
B. control of security agents within and out of the borders
C. provision of dockyards for ship repairs and maintenance
D. provision of transport system to facilitate imports and exports
\n """,
"""12. A document recording the transactions of an organization with its customer for a specified period which normally shows the indebtedness of one to the other is a
A. statement of account
B. consular invoice
C. proforma invoice
D. statement affairs
\n """,
"""13. In response to an inquiry from a customer, a wholesaler is expected to send back
A. a consignment note
B. an order
C. a quotation
D. an advice note
\n """,
"""14. A carton of noodles valued at ₦2,00 was invoiced at ₦200 only. The accounting procedure to correct this error is to issue
A. an invoice for ₦200
B. a debit note for ₦2,00
C. a credit note for ₦1,800
D. a debit note for ₦1,800
\n """,
"""15. Tourists with no fixed address in a town may receive their letters from post office through a
A. poste restante
B. parcel post
C. private mail bag
D. recorded delivery
\n """,
"""16. Endowment policy in insurance business is an aspect of
A. accident insurance policy
B. fidelity guarantee insurance policy
C. motor vehicle insurance policy
D. life assurance policy
\n """,
"""17. Insurance against burglary is an example of
A. indemnity insurance
B. fidelity guarantee insurance
C. non-insurable risk
D. non-indemnity insurance
\n """,
"""18. The principle which requires the insurance company to disclose to the proposer all material facts of the risk to be covered is
A. subrogation
B. proximate cause
C. uberrimae fidei
D. contribution
\n """,
"""19. The insurance principle that allows an insurance an insurance company to take over the rights of the insured once he has been compensated is
A. indemnity
B. proximate cause
C. utmost good faith
D. subrogation
\n """,
"""20. A trader who experienced loss through fire can be restored by
A. an insurance company
B. a trade association
C. the bank
D. an advertising agency
\n """,
"""21. The distribution of petroleum products in Nigeria is through
A. rail
B. road
C. sea
D. air
\n """,
"""22. The deliberate effort geared towards discarding some cargoes in order to lighten the vessel is 
A. caveat emptor
B. uberrimae fidei
C. demurrage
D. jettison
\n """,
"""23. The major aim of establishing a public corporation is to
A. establish a monopoly
B. provide essential services
C. provide employment opportunities
D. encourage specialization
\n """,
"""24. The coming together of a manufacturing business with a firm that markets its products is 
A. backward integration
B. a consortium
C. forward integration
D. a syndicate
\n """,
"""25. An association of voluntary organizations that work together for a common aim while retaining their independence is a
A. syndicate 
B. merger
C. cartel
D. consortium
\n """,
"""26. The document that explains the types of shares available for sale to the public is
A. a prospectus
B. an invoice
C. an open indent
D. a closed indent
\n """,
"""27. Which of the following attracts only interest but leaves the capital unpaid?
A. a long-term loan
B. a development bond
C. a redeemable bond
D. an irredeemable bond
\n """,
"""28. A loan to a customer with a cheque account at a bank in which the account is allowed to go into debit is
A. overdraft
B. advance 
C. interest
D. commission
\n """,
"""29. Part payments made on allotted shares by subscribers is usually the
A. subscribed capital
B. authorized capital
C. issued capital
D. called-up capital
\n """,
"""30. The net profit is the excess of gross profit and sources of income over all the expenses. This implies that net profit is
A. the difference between gross profit and trade expenses
B. the different between gross profit and net sales
C. sales less cost of sales including sales returns
D. opening stock add purchases less closing stock
\n """,
"""31. A form of money with face value which is greater than the value of the metal content is 
A. legal tender
B. bank notes
C. token money
D. commodity money
\n """,
"""32. An agent who transacts business with the broker in the stock exchange is a
A. stag
B. bull
C. del credere
D. jobber
\n """,
"""33. A document sent by a broker to his client to confirm a purchase of sale made on his behalf is
A. delivery note
B. consignment note
C. transfer form
D. contract note
\n """,
"""34. Cum div differs from ex div in that, the later
A. entitles the purchaser to receive a company's current dividend 
B. entitles the vendor to receive a company's current dividend
C. confirms a purchase or sale made on behalf of a share holder
D. is a document used to transfer ownership of shares
\n """,
"""35. The payment made by a speculator to the buyer when he is unable to deliver stocks on the agreed date is
A. arbitage
B. Franco
C. contango
D. backwardation
\n """,
"""36. Which of the following regulates and controls the activities in the Nigerian Stock Exchange?
A. BPE
B. SEC
C. NDIC
D. CBN
\n """,
"""37. The principle of management that emphasizes on the number of subordinates under the direct supervision of a manager is
A. span of control
B. unity of command
C. scalar chain
D. unity of direction
\n """,
"""38. Marketing differs from selling in that, the latter only creates
A. possession utility
B. marginal utility
C. form utility
D. place utility
\n """,
"""39. A business that focuses attention on the quality of the goods produced by precisely knowing what the consumers desire is said to be operation the
A. product mix
B. promotion mix
C. marketing concept
D. product orientation.
\n """,
"""40. The physical and psychological satisfaction a  customer derives from the purchase of goods and services is
A. price mix
B. product mix
C. marketing mix
D. promotion mix
\n """,
"""41. Which of the following aspects of marketing stimulates buying by providing free gifts?
A. a personal selling
B. sales promotion
C. advertising
D. publicity
\n """,
"""42. Which of the following is used as pricing policy?
A. labelling
B. packaging
C. market selection
D. market skimming
\n """,
"""43. Mr. Taiwo entered into a contract to let a car to Mr. Bunmi for his wedding for two days. However, the car had an accident subordinates under the direct supervision of a manager is before the first day. Mr. Bunmi attempted to claim damages but failed. This implies the contract was terminated by
A. bankruptcy
B. frustration
C. breach
D. lapse of time
\n """,
"""44. Hire purchase is advantageous to the seller in that
A. it elevates his living standard
B. his turnover will increase
C. people pay instalmentally
D. it enhances high level of patronage
\n """,
"""45. The difference between a factor and a broker is that the former
A. is licensed to sell goods on auction
B. has a lien on the goods he possesses?
C. is not in possession of the goods 
D. cannot sell in his own name
\n """,
"""46. A contract which is devoid of legal effect is
A. void contract
B. unenforceable contract
C. voidable contract
D. valid contract
\n """,
"""47. The three functional units of a modern computer are
A. input, processor and output units
B. processor, FOTRAN and output units
C. black box, output and input units
D. basic, COBOL and output units
\n """,
"""48. Which of the following computers can be used in weather forecast?
A. Hybrid computer
B. Digital computer
C. Mainframe computer
D. Analog computer 
\n """,
"""49. A Digital Versatile Disk is an example of a
A. transmission control protocol
B. microprocessor
C. file transfer protocol
D. computer storage device
\n """,
"""50. The social responsibility factor of an organization is geared towards
A. contributing to the sustenance and development of its host community
B. operating without disrupting the very essence of the environment
C. tackling the soci-economic problems of the state
D. meeting the needs and demands of the shareholders
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
        Commerce_2016()
def Commerce_2015():
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
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "A"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "C"),
        Question(question_prompts[40], "D"),
        Question(question_prompts[41], "C"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "D"),
        Question(question_prompts[44], "B"),
        Question(question_prompts[45], "C"),
        Question(question_prompts[46], "C"),
        Question(question_prompts[47], "D"),
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
        Commerce_2015()
def Commerce_2014():
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
        """0 . One of the major benefits of commerce to government is to
A. improve the standard of living
B. generate revenue for growth and development
C. encourage cooperation among public organisations
D. encourage the development of sociocultural values
\n """,
"""1 An example of an activity in the construction industry is
A. blacksmithing
B. bricklaying
C. car assembling 
D. shoemaking
\n """,
"""2 One of the inputs in production that can be motivated by remuneration is
A. capital
B. entrepreneur
C. labour
D. land
\n """,
"""3 The allocation of tasks to different skills in a production process is referred to as
A. production technique
B. production function
C. division of labour
D. delegation of responsibility
\n """,
"""4 The sales of goods through a medium that accepts money and delivers the items to the customer is
A. an automated teller machine
B. a vending machine
C. a counting machine 
D. a branding machine
\n """,
"""5 The main purpose of branding is to
A. create identity for a product
B. make a product look attractive
C. create product awareness
D. increase sales volume
\n """,
"""6 The basis for international trade is embedded in the principle of
A. absolute advantage
B. globalization
C. deregulation
D. comparative advantage
\n """,
"""7 The major problem encountered in international trade is that of
A. distance
B. differences in culture
C. politics
D. differences in currency
\n """,
"""8 The document a seller uses in dispatching goods to a customer by a carrier is
A. a bill of landing
B. an invoice
C. an advice note
D. a delivery note
\n """,
"""9 A document which serves as an order with details of goods required by an intending purchaser is
A. a freight note
B. an indent
C. a bill of landing
D. a way bill
\n """,
"""10 If a customer pays within nine days of receiving goods and takes advantage of 3% off the invoice price, this is stated as
A. 3/9;net 30
B. 9/27;net 30
C. 30;net 9/3
D. 9/30;net 3
\n """,
"""11 Which of the following is a characteristic of a bearer cheque?
A. it is made with transverse lines
B. it is made payable to whoever presents it
C. it is made without transverse lines
D. it is only payable into the payees account
\n """,
"""12 A bill of exchange paid before its due date at an amount less than its face value is said to have been
A. accepted
B. rejected
C. discounted
D. dishonoured
\n """,
"""13 The most effective type of advertising for branded products is
A. mass advertising
B. persuasive advertising
C. informative advertising
D. competitive advertising 
\n """,
"""14 A current account holder pays fees for services in form of
A. bank charges
B. interest rates
C. commission on turnover
D. minimum lending rate
\n """,
"""15 Printed messages sent by cable are recorded as
A. telegram
B. SMS
C. telex
D. MMS
\n """,
"""16 Communication is relevant to business activities because it
A. creates wealth for people
B. reduces the cost and risk of travelling
C. connects people
D. enhances delivery of goods and services
\n """,
"""17 The right of an insurance company to stand in place of an insured against a third party, who is liable for the occurrence of a loss, is the principle of
A. proximate cause
B. insurable interest
C. insurance priority
D. subrogation
\n """,
"""18 Assurance is different from insurance in that the former is based on
A. probability
B. possibility
C. risk
D. uncertainty
\n """,
"""19 A person who undertakes life insurance is said to be an
A. insurer
B. assurer
C. assured
D. insured
\n """,
"""20 Tourism serves the purpose of
A. cross-cultural understanding and peaceful interaction 
B. opening values for leaving the country
C. economic development and naturalization
D. exploiting the country's natural endowment
\n """,
"""21 The type of letters that are delivered through the normal mail or by airmail express service is referred to as
A. inland letters
B. registered letters
C. airmail letters express letters
D. express letters
\n """,
"""22 A business organization that exploits the capabilities of a member to remedy the weaknesses of another is
A. joint venture
B. partnership
C. nominal partnership
D. cooperative
\n """,
"""23 The most important business objective is to 
A. improve investments
B. provide quality products
C. target consumers for satisfaction
D. carve a niche for the business
\n """,
"""24 In case of a liquidation of a public limited liability company, those that are first paid are
A. ordinary shareholders
B. preference shareholders
C. cumulative preferenceshareholders
D. debenture holders
\n """,
"""25 A feature common to public and private limited liability companies is that
A. both can sue and be sued
B. the minimum number of their shareholders is five
C. the transfer of their shares is not restricted
D. their annual accounts are published for public use
\n """,
"""26 A business organization can obtain long term financing through
A. bank overdraft
B. the sale of shares
C. credit purchases
D. bureau de change
\n """,
"""27 The portion of the authorized share capital given out to the public for subscription is
A. called-up capital
B. issued capital
C. paid-up capital
D. reserved capital
\n """,
"""28 A company has an authorized capital of 40 million shares at N1 each, out of which 32 million are issued and fully paid-up. What happens to the remaining 8 million shares?
A. it has been issued but not paid-up
B. it has been applied for but not issued 
C. it is not paid-up
D. it has not yet been issued
\n """,
"""29 If the rate of turnover of a company in 1999 was 4 times while the average stock was ₦49,600, determine the turnover.
A. ₦199,400
B. ₦198,400
C. ₦100,200
D. ₦99,200
\n """,
"""30 Given: opening stock ₦1,800, purchases ₦2,800, sales ₦8,000, closing stock ₦350, carriage on sales ₦500 Calculate the value of the unused stock.
A. ₦800
B. ₦500
C. ₦350
D. ₦320
\n """,
"""31 The main objective of a trade association is to
A. protect its members against litigation
B. boost the trade of its members
C. secure credit for its members
D. protect its members against victimization
\n """,
"""32 The promotion and protection of trade industry and agriculture through trade fairs is a function of
A. NACRDB
B. NACCIMA
C. the consumer protection council
D. the chamber of commerce
\n """,
"""33 Dealing in quoted securities on the Nigerian Stock Exchange is restricted to authorized
A. companies
B. brokers
C. investors
D. principals
\n """,
"""34 Securities that entitle the investor to coupon rates are
A. bonds
B. equities
C. warrants
D. treasury bills
\n """,
"""35 Under what management function will the motivation of employees fall
A. staffing
B. controlling
C. organizing
D. directing
\n """,
"""36 The promotion of team spirit in an organization is referred to as
A. unity of direction
B. espirit de corps
C. unity of purpose
D. discipline
\n """,
"""37 One of the characteristics of a good organizational chart is that it should 
A. be rigid
B. show government policy
C. facilitate communication
D. be acceptable
\n """,
"""38 An organization which focuses on consumer satisfaction is practicing
A. consumerism
B. market segmentation
C. selling concept
D. marketing concept
\n """,
"""39 Good and services are made available to consumers through
A. the channel of distribution
B. sales promotion
C. the advertising agency
D. the middle men
\n """,
"""40 A person who in consideration for an extra commission takes responsibility for goods sold on credit and in case of default is a
A. commission agent
B. del credere agent 
C. broker
D. factor
\n """,
"""41 Yahaya bought a piece of furniture on a credit sale agreement from Ahmed and resold it to Ali before all instalments were made. The court upheld that Ahmed could not recover possession of the items from Ali. The reason for the judgement was because
A. ownership was transferred on completion of instalment
B. ownership was transferred on delivery
C. Yahaya could not pass title to a third party
D. Ali was still indebted to Yahaya
\n """,
"""42 The body which ensures that consumers are protected against harmful products in Nigeria is
A. NAFDAC
B. NDLEA
C. SON
D. CPC 
\n """,
"""43 The process of decoding data in a computer is known as
A. dilution
B. default drive
C. decryption
D. data security
\n """,
"""44 Which of the following is a type of system software?
A. utility programmes
B. registers
C. hard drives
D. packages
\n """,
"""45 Computers that process all data as binary zeros and ones are
A. analog computers
B. digital computers
C. hybrid computers
D. desktop computers
\n """,
"""46 Modern means of payment is greatly facilitated by
A. e-commerce
B. paper money 
C. e-banking
D. credit transfer
\n """,
"""47. The provision of quality and safe products which guarantee the health of consumers is an example of
A. quality control
B. price control
C. civic responsibility
D. social responsibility
\n """,
"""48 A business organization must always consider the overall effect of its actions on the
A. competitor
B. product
C. profit
D. society
\n """,
    ]

    questions = [

        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "D"),
        Question(question_prompts[39], "A"),
        Question(question_prompts[40], "B"),
        Question(question_prompts[41], "B"),
        Question(question_prompts[42], "A"),
        Question(question_prompts[43], "C"),
        Question(question_prompts[44], "A"),
        Question(question_prompts[45], "B"),
        Question(question_prompts[46], "C"),
        Question(question_prompts[47], "A"),
        Question(question_prompts[48], "C"),

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
        Commerce_2014()
def Commerce_2013():
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
        """0  The type of labour that makes use of physical effort in production processes is the
 A. unskilled labour
 B. skilled labour
 C. blue-collar job
 D. white-collar job
\n """,
"""1 The assembling of products into usable forms is known as
 A. creation
 B. manufacturing
 C. construction
 D. formation
\n """,
"""2 The final link in the chain of distribution is
 A. middlemen
 B. wholesaling
 C. consumer
 D. retailing
\n """,
"""3 A country is said to be experiencing an unfavourable balance of trade if her
 A. exports exceed imports
 B. visible exports exceed visible imports
 C. imports and exports are equal
 D. visible imports exceed visible exports
\n """,
"""4 Trading position of Nigeria is the same as her
 A. desire to trade with many countries
 B. willingness to grant credit to foreigners
 C. balance of trade
 D. terms of trade 
\n """,
"""5 The role of customs and exercise authority includes the
 A. provision of a good transport system to facilitate imports and exports
 B. provision of security at the port
 C. control of the flow of goods in and out of the country
 D. provision of dockyards for ship repairs
\n """,
"""6 The document lodged with the customs authorities before a ship can leave the port is a
 A. shipping note
 B. ship report
 C. ship manifest
 D. dock warrant
\n """,
"""7 The document which must be endorsed by the ambassador of a country of destination before shipment of goods is a
 A. consular invoice
 B. certificate of origin
 C. bill of lading 
 D. close indent
\n """,
"""8 A country's terms of trade are said to improve when the ratio of her export
 A. decreases
 B. remains constant
 C. increases
 D. equals import
\n """,
"""9 Which of the following advertising medium appeals to only the literate in the society?
 A. radio advertising
 B. print media advertising
 C. television advertising
 D. cinema advertising
\n """,
"""10 The two main forms of communication are
 A. oral and written
 B. verbal and non-verbal
 C. e-mail and fax
 D. traditional and modern media
\n """,
"""11 The most reliable and efficient means of conveying urgent documents is through
 A. postal order
 B. ordinary letters
 C. registered letters
 D. courier services
\n """,
"""12 An undertaking given by a person to another assuring his integrity is
 A. proximate cause
 B. fidelity guarantee
 C. subrogation
 D. insurable interest
\n """,
"""13 The difference between indemnity insurance and nonindemnity insurance is that the latter provides
 A. cover for exporters against risks
 B. cover for importers against risks
 C. full payment to the insured
 D. consolation payment to the insured
\n """,
"""14  An importance of warehousing is in the
 A. production of goods
 B. transportation of goods
 C. importation of goods
 D. repackaging of goods
\n """,
"""15 In order to increase the capital owned, a sole trader may
 A. seek for bank loan
 B. issue debentures
 C. acquire extra shop fittings on credit
 D. draw less of his profit for personal use
\n """,
"""16 A business partner who provides capital but abstains from participation in administration of a firm is a
 A. general partner
 B. nominal partner
 C. secret partner
 D. dormant partner
\n """,
"""17 Which of the following will not be stated in a Memorandum of Association?
 A. Name clause
 B. rights of shareholders
 C. object clause
 D. registered office
\n """,
"""18 The amount of authorized capital that shareholders have subscribed to is
 A. issued share capital
 B. authorized share capital
 C. owner's equity
 D. working capital
\n """,
"""19 The rate of turnover of a firm in a given year is 5 times while the average stock is ₦12,500. What is the turnover of the firm?
 A. ₦24,000
 B. ₦46,500
 C. ₦62,500
 D. ₦65,000
\n """,
"""20 A lawyer that defrauds his client may be derobed by the Nigerian Bar association in order to
 A. protect other lawyers
 B. protect the integrity of the association
 C. compensate the affected client
 D. prevent the client from suing the association
\n """,
"""21  In the Nigerian GSM industry, a parliament is organized by the Nigerian Communications Commission in order to
 A. increase profit of service providers
 B. protect the interest of government
 C. encourage more people into the business
 D. protect the interest of consumers
\n """,
"""22 Trade fairs in Nigeria are organised by
 A. the Federal Government
 B. Manufacturers' Association of Nigeria
 C. Ministry of Commerce and Industry
 D. Chambers of Commerce
\n """,
"""23 Money is generally accepted for transactions due to
 A. the legal backing
 B. the rule of law
 C. its acceptability in the global market
 D. the Central Bank Governor's signature
\n """,
"""24Which of the following is a quality
 A. Availability
 B. Scarcity
 C. Indivisibility
 D. Convertibility
\n """,
"""25 Money can simply be referred to as a
 A. measure of value
 B. standard of value
 C. means of settlement
 D. durable asset for doing business
\n """,
"""26 Gilt-edged securities are issued mainly by
 A. individuals
 B. non-governmental organisations
 C. Government
 D. multi-national companies
 \n """,
"""27 The initial function of a manager is
 A. setting up an organisation
 B. coordinating
 C. planning
 D. provision of welfare package
\n """,
"""28 The most suitable organizational structure for small or medium sized enterprises is
 A. line structure
 B. staff structure
 C. committee structure
 D. functional structure
\n """,
"""29 In a staff-authority relationship, the opinion of a specialist in one department to another is
 A. a directive
 B. an advice
 C. a command
 D. a delegation
\n """,
"""30 Management of a business involves the development of ideas for the
 A. distribution of goods and services that human wants
 B. transportation of goods and services that human wants
 C. transfer of title of ownership of goods and services to individuals
 D. production of goods and services that satisfy human needs
\n """,
"""31 Which of the following is used as a pricing policy?
 A. Packaging 
 B. Market selection
 C. Labelling
 D. Market skimming
\n """,
"""32 The essential utility derived from the use of a product is known as
 A. augmented benefit
 B. branded benefit
 C. core benefit
 D. formal benefit
\n """,
"""33The breaking down of a market into separate and identifiable elements is known as
 A. differentiation
 B. segmentation
 C. skimming
 D. penetration
\n """,
"""34 A contract that is acknowledged before the law court is referred to as
 A. informal contract
 B. formal contract
 C. contract of records
 D. specialty contract
\n """,
"""35 An agent employed to sell goods delivered to him by the principal is referred to as a
 A. special agent
 B. del credere agent
 C. factor
 D. universal agent
\n """,
"""36 A motor dealer who agreed to sell a car to Mr. X but delivered it to Mr. Y on the delivery date agreed with Mr. X. He has discharged the contract by
 A. performance
 B. frustration
 C. an agreement
 D. breach
\n """,
"""37 A contract can be terminated through
 A. physical combat
 B. family intervention
 C. frustration
 D. consultation
\n """,
"""38 The right to retain possession of goods until the contract price is paid is referred to as
 A. a promise
 B. ultra vires
 C. a breach
 D. a lien
\n """,
"""39  The sole legal right held by the author to publish his book is
 A. trademark
 B. copyright
 C. patent right
 D. bookmark
\n """,
"""40The process of transferring data from one computer to another is referred to as
 A. downloading
 B. faxing
 C. browsing
 D. decoding
\n """,
"""41 The physical component of a computer system is
 A. software
 B. hardware
 C. hard disk
 D. floppy disk
\n """,
"""42 A computer accessory through which information can be retrieved is the
 A. hard disk
 B. input device
 C. control unit
 D. floppy disk
\n """,
"""43  The type of computer software used mainly for management information is
 A. Corel draw
 B. AutoCAD
 C. data base
 D. word perfect
\n """,
"""44 To meet security requirements before gaining access to data, a computer operator supplies
 A. an e-mail address 
 B. a yahoo address
 C. a password
 D. a modem
\n """,
"""45 A major factor that affects business operations is
 A. technology
 B. supply
 C. product
 D. rivalry
\n """,
"""46 The environmental hazard that is most difficult to control is
 A. land pollution
 B. water pollution
 C. air pollution
 D. political unrest
\n """,
    ]

    questions = [

        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "C"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "D"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "A"),
        Question(question_prompts[39], "B"),
        Question(question_prompts[40], "A"),
        Question(question_prompts[41], "B"),
        Question(question_prompts[42], "D"),
        Question(question_prompts[43], "C"),
        Question(question_prompts[44], "C"),
        Question(question_prompts[45], "A"),
        Question(question_prompts[46], "C"),

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
        Commerce_2013()
