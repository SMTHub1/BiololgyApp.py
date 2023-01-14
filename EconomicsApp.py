from Question import Question
def Economics_2020():
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
        """0 From the diagram above, the arrow marked M indicates
         payments made for foods and services
         payments made to factors of production
         the flow of capital goods
         the flow of economics rent
        \n """,
        """1 A change in the quantity supplied of a commodity is influenced by
         the price of substitutes
         the price of the commodity
         consumer's tastes
         technological know-how
        \n """,
        """2 One of the functions of money deposit banks in economic development is
         that it is banker to the government
         the provision of credits facilities
         the formulation of monetary policies
         issuing of currency notes
        \n """,
        """3 One of the arguments against the practice of monopoly is
         merging of producers
         competition
         exploitation
         non-government ownership
        \n """,
        """4 The main reason why countries engaged in international trade is the
          opportunity to earn high profit in trading
         use of capital-intensive method of productions
         difference in their endowment of economic resources
         difference in their endowment of economic resources
        \n """,
        """5 A well conducted census is important for
          economic planning
          providing economic opportunities in the rural areas
         distribution of educational materials in the cities
          revenue generation
        \n """,
        """6 The cost-saving advantages which a large firm can achieve on its own is called
         internal economies of scale
         diseconomies of large scale
         externa diseconomies of scale
          external economies of scale
        \n """,
        """7 A country uses the foreign exchange control measure to eliminate balance of payments deficit by
          limiting her imports to its currency value of exports
          limiting her exports to its currency value of imports
          overvaluing the country's currency
         reducing the nation's domestic price level
        \n """,
        """8 Occupational distribution of population is mainly influenced by
         economic factors
         religious factors
         geographical factors
         social factors.
        \n """,
        """9 The reward for capital is
         interest
          rent
          risk
         premium.
        \n """,
        """10 The reduction in the value of a country's currency in relation to the value of the currencies of other nations is known as
          deflation
          inflation
          devaluation
         revaluation
        \n """,
        """11 Mortgage banks give loans to investors on a long- term basis to
         finance agriculture
         establish banks
         acquire machinery
         build houses.
        \n """,
        """12 In a capitalist economy, factors of production are owned and controlled by the
         citizens
         businessmen
         government
         foreigners.
        \n """,
        """13 The establishment of industries in rural areas will help to reduce
         urban-rural migration
         rural-urban migration
         rural-rural migration
         urban-urban migration.
        \n """,
        """14 International trade is an application of the principle of
         industrial production
         mass production
         regional production
         comparative cost advantage.
        \n """,
        """15 The number of people who are qualified to work and who offer themselves for employment is called
          migrant labour
          working population
         labour turnover
         mobility of labour.
        \n """,
        """16  Which of the following is an advantage of localisation of industry?
          Development of subsidiary firms
          creation of parallel markets
          Development of slums
          Attraction of foreign capital.
        \n """,
        """17 The Economic Community of West African States (ECOWAS) has been slow in achieving its objectives because of
         the activities of multinationals
         inadequate personnel at the secretariat
         political instability
         inadequate international support.
        \n """,
        """18 Joint ventures are partnership involving
         the poor and the rich
         employers and workers
          government and private investors
         multinationals and individuals.
        \n """,
        """19  In which of the following business units are the owners mostly the customers?
         co-operatives
         limited liability companies
         partnership
         public corporations.
        \n """,
        """20 The formula index of export prices x 100, is index of import prices used to measure the
          volume of trade between countries
         direction of international trade
         commodity terms of trade
          volume of imports.
        \n """,
        """21  Which of the following is an invisible item?
          Petroleum services
          Processed rice
          Processed milk
          Banking services
        \n """,
        """22 The full meaning of OPEC is
         Oil and Petroleum Exporting Countries
         Original Petroleum Exporting Countries
         Organisation of Petrol Exporting Countries
         Organisation of Petroleum Exporting Countries.
        \n """,
        """23 The main concern of economists is to
         control the growth of population
          redistribute income between the rich and the poor
          satisfy all human wants
          allocate scarce resources to satisfy human wants.
        \n """,
        """24  Productive resources can also be called
         principles of production
         factors of production
         items of production
         labour and materials resources.
        \n """,
        """25  The study of Economics becomes necessary because of the
          large population size of the world
          scarcity of resources
         opportunity cost of goods and services
         need to satisfy every desire of man.
        \n """,
        """26  The type of demand that exists between torchlight and battery is
         competitive demand
         complementary demand
         composite demand
         independent demand.
        \n """,
        """27  The population density of a town made up of 50 square kilometre land area and 100 million people is
         50,000 people per square kilometre
         0.2 million people per square kilometre
         0.5 million people per square kilometre
         20 million people per square kilometre
        \n """,
        """28  Human wants are insatiable because wants are
          limited while means are scarce
          unlimited and means are also unlimited
         limited and means are also limited
         unlimited while means are scarce.
        \n """,
        """29 Which of the following items is not an example of circulating capital?
          Raw material
          Money
          Fuel
         Machinery
        \n """,
        """30 The principle of comparative cost advantage was propounded by
         David Ricardo
         Alfred Marshal
         J.S. Mill
         Adam Smith
        \n """,
        """31 The rate at which a country's exports is exchanged for her imports is
         trade balance
         balance of payments
         terms of trade
         balance of currency account.
        \n """,
        """32 Efficiency of labour in a country is determined by the following except the
         social attitude to work
         education and training
         total population
         working conditions of workers.
        \n """,
        """33 Taxes and government expenditures are instruments of
         monetary policy
         tax policy
         economic policy
         fiscal policy.
        \n """,
        """34 A situation in which a commodity is sold abroad below its cost of production in the home country is known as
         dumping
         counter trade
         bilateral trade
         trade liberalisation.
        \n """,
        """35 The Family Support Programme in Nigeria essentially focuses on
         the generation of employment
         the alleviation of poverty
         agricultural and industrial development
         economic emancipation of women.
        \n """,
        """36 The Economic Commission for Africa was set up by the
         UNO
         ECOWAS
         OAU
         IMF
        \n """,
        """37 Utility is the satisfaction derived from
         production
         distribution
         consumption
         demand.
        \n """,
        """38 When a union is composed of workers with the same skill it is called
         an industrial union
         a workers' union
          a craft union
         a technical union.
        \n """,
        """39 The major objective, of a revenue allocation formula in a country is to
         share revenue between the public and private sectors
         ensure the financial viability of the country
         share revenue between the different tiers of government
         divert revenue from areas of surplus to areas of needs.
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "A"),
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
        Economics_2020()
def Economics_2019():
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
        """0 Given: Qd = 30 — 3P and Qs = 9P —15, determine the equilibrium price
        ₦12.00
        ₦3.75
        ₦2.80
        ₦3.00
        \n """,
        """1The problem of economic development in Nigeria is that of
        poor weather conditions
        overpopulation
        surplus skilled manpower
        inadequate infrastructure.
        \n """,
        """2 The combination of two commodities that yield the same level of satisfaction is illustrated by
        a budget line
        an isocost curve
        a production possibility curve
        an indifference curve
        \n """,
        """3 The demand for inferior goods is inversely related to change in
        income
        price
        supply
        taste.
        \n """,
        """4 The minimum number of shareholders for partnership is
          7
          4
          2
         3
        \n """,
        """5 When diminishing returns sets in, the total variable cost begins to
        rise at an increasing rate
        fall at a decreasing rate
        rise at a decreasing rate
        fall at an increasing rate.
        \n """,
        """6 Given: 32, 18, 24, 17, 16, 32, 28, 68, 71 and 15, what is the range?
         26
         32
         56
         68
        \n """,
        """7 If P = 1/4 (Qs + 30), what is the quantity supplied at ₦18?
         64.5
         42.0
         2.4
         30.0
        \n """,
        """8  When a consumer is at equilibrium, The MRS x is equal to the
         product of the two prices
         sum of the two prices
         ratio of the two prices
         difference of the two prices.
        \n """,
        """9 One of the major factors militating against industrialization in Nigeria is
         low level of foreign investment
         frequent break-down of equipment
         inadequacy of infrastructural facilities
        \n """,
        """10 One of the factors that is considered in the location of a cement industry is nearness to
         market
         raw materials
         infrastructural facilitates
         skilled manpower.
        \n """,
        """11 A problem facing the development of the Nigerian Petroleum industry in Nigeria is
         persistent gas flaring
         instability in demand for the products
         dominance of multinationals
         declining oil reserves.
        \n """,
        """12 At full employment level, a contractionary monetary policy will Lead to a
         rise in aggregate supply
         rise in aggregate demand
         rise in level of inflation rate
         fall in the level of inflation
        \n """,
        """13 A country where the available population is unable to guarantee efficient utilization of available resources is experiencing
         under population
         over-population
         high population density
         optimum population.
        \n """,
        """14 One of the causes of instability in farmers' income is
         high level of illiteracy
         unfriendly land tenure
         unfavourable weather condition
         poor management of extension services
        \n """,
        """15 If the arithmetic mean of 2, 3, 5, 8, Z, 10 and 12 is 7, what is the value of Z?
          8
          9
          10
          7
        \n """,
        """16 The most important function of agriculture to the Nigerian economy is
          the guarantee of food security
          technical skill development
          technological development
          industrial development
        \n """,
        """17 Given that Qd=15-2P and Qs=5+3P, determine the equilibrium price.
          N3.00
          N5.00
          N2.00
          N6.00
        \n """,
        """18 Scale of preference is referred to as the
         choices consumers make
         array of consumer's needs
         consumer preference for luxurious goods
         consumer wants in order of priority
        \n """,
        """19 One of the basic assumptions of monopoly is
          perfect information of the market condition
          the ability to either control price or output
          perfect mobility of factors of production
          large number of buyers and sellers
        \n """,
        """20 The major advantage of a public limited liability company over a private limited liability company's
         limited liability enjoyed by owner
         separate legal entity
         easy transferability of shares
         perpetual existence
        \n """,
        """21 The main activity in the upstream oil sector in Nigeria is
        marketing of petroleum products
        distribution of petroleum products
        extraction of crude oil
        refining of crude oil
        \n """,
        """22 The natural growth of population is calculated as
          birth rate + death rate
         labour force + dependant
         death rate - birth rate
          birth rate - death rate
        \n """,
        """23 The study of age structure of a population is important because it
         determine the exchange rate
         provide the government with statistics on the prevailing interest rate
         reveals the cost of living
         provides the government with statistics on present size of the labour force
        \n """,
        """24 If the demand for palm oil is for the purpose of soap production and cooking, the demand is said to be
         competitive
         complementary
         composite
         derived
        \n """,
        """25 The institution established to enhance the activities of Nigeria's exports is
         Nigerian Export and Import Bank
         Import-substitution strategy
         Nigeria Export Promotion Council
         Bank of Industry
        \n """,
        """26 A sustained increase in per capita income accompanied by an increase in output is
         economies of scale
         economic efficiency
         economic development
         economic growth
        \n """,
        """27  The reward for capita as a factor of production is
          interest
          rent
          profit
          wage
        \n """,
        """28  The type of inflation that emanates from excess demand over supply is
          galloping inflation
          cost-push inflation
          demand-pull inflation
          imported inflation
        \n """,
        """29 Which of the following problems is associated with national income measurement?
          High interest rate
          Inflation and deflation
          Overpopulation
          population growth
        \n """,
        """30 Freedom of consumption and production are characteristics of
          socialism
          feudalism
          capitalism
          communism
        \n """,
        """31  Cost of raw materials in production is an example of
         marginal cost
         variable cost
         total cost
         fixed cost
        \n """,
        """32  Foreign exchange control in Nigeria is administered by the
         Money deposit banks
         Central Bank of Nigeria
         Discount houses
         Security and Exchange Commission
        \n """,
        """33 The volume of output in an economy is determined by
         the foreign exchange rate
         the standard of living of citizens
         population density of a country
         efficiency in the use of factors of production
        \n """,
        """34 Given Qd = 30 - 3P, Qs = 9P – 18. Determine the equilibrium quantity
         18
         20
         25
         27
        \n """,
        """35 In Nigeria, industrial development can be enhanced by
          ensuring stable prices for manufactured goods
         reducing government expenditure on imported goods
          providing efficient infrastructure
          increasing the rate of interest
        \n """,
        """36 Capital gains tax is an example of
         Value Added Tax
         purchase tax
         sales tax
         income tax
        \n """,
        """37 Which of the following is NOT a source of government revenue?
          Taxes, fees, licenses and fines
          Interest, dividends, profits and earnings
          Personal income, disposable income and transfer earnings
          Grants, aids and borrowing
        \n """,
        """38 One of the important qualities that money must possess is
         heterogeneity
         easy availability
         homogeneity
         flexibility in value Price
        \n """,
        """39 The graph above represents
         a decrease in quality supplied
         an increase in supply
         an increase in quantity supplied
         a decrease in supply Wages
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "A"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "C"),
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
        Economics_2019()
def Economics_2018():
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
        """0  In the theory of production, the price of a factor input is determined by
the prevailing exchange rates
its elasticity of demand
the existence of large market
the prevailing interest rates.
\n """,
"""1 When the selling price of a monopolist is below his short-run marginal cost, he is said to be making
an economic profit
Losses
profit
supernormal profit.
\n """,
"""2 The overall economic performance of a country can be assessed through
overlooking of its agricultural sector
employment estimates
national income estimates
balance of payment.
\n """,
"""3 The supply of agricultural products is mainly determined by
consumers' taste
consumers' income
technology
consumers.
\n """,
"""4 Determine the median of 6 10, 5, 12, 20, 18, 20 and 4
 11
 9.67
 12.56
 12.
\n """,
"""5  The failure of the Nigeria industrial sector is mainly associated with
lack of raw materials
inadequate market for industrial goods
underdeveloped infrastructural facilities
inadequate capital.
\n """,
"""6 If Qd = 40-4P and P = N4, what is the quantity demanded?
30
32
24
26.
\n """,
"""7  The long-run total cost curve shows the cost of
all fixed factors of production
the average fixed cost
all factor inputs that are employed
variable factors of production.
\n """,
"""8 The supply of farm produce is mainly determined by
consumers’ income
weather condition
population
consumers’ taste
\n """,
"""9 A country embarks on deficit financing in order to
reduce aggregate demand
increase revenue
stimulate investment
curb inflation
\n """,
"""10 The money market provides business firms with the avenue to
purchase goods and services
purchase capital equipment’s
obtain short- term funds
obtain long-term funds
\n """,
"""11 The optimum level of output for pure monopolist occurs where
P is highest
P=AC
P=MC
MR=MC
\n """,
"""12 According to the demographic transition theory, Africa can be said to be at stage
2 and 3
3 only
2 only
1 and 3
\n """,
"""13 The Economic Community of West African States (ECOWAS) is an example of
globalization
regional marketing board
economic integration
economic union.
\n """,
"""14 Given: 32, 18, 24, 17, 16, 32, 28, 68, 71 and 15, the mode of the distribution is
71
56
32
15
\n """,
"""15 The major determinant of income elasticity of demand is
government policy
the availability of substitutes
the price of the good
the level of consumer's income
\n """,
"""16 Given: 2, 4, 6, 8, 4 and 6, the absolute mean deviation is
 6.00
 1.67
 30.00
 0.60
\n """,
"""17 The precautionary demand for money is determined by
the level of savings
the rate of interest
general price level
the level of income.
\n """,
"""18 If the output of a firm experiencing economies of scale increases, the average cost would
be at minimum
rise
be at maximum
fall.
\n """,
"""19 The demand curve for a normal good is negatively sloped because
price is an incentive to producers
price is an incentive to consumers
demand always exceeds supply
price and quantity move in the same direction.
\n """,
"""20 The major role of multinational companies in the Nigerian petroleum industry is
 oil marketing only
 oil marketing and prospecting
 establishment of refineries
 oil prospecting only.
\n """,
"""21 Life insurance companies contribute to economic development by holding a part of their assets in
long-term financial instruments
equipment
cash and near money
money-market instruments.
\n """,
"""22 The wage rate is mostly related to
marginal productivity of labour 
average productivity of labour 
marginal efficiency of investment
total productivity of Labour.
\n """,
"""23 The choice of how to produce in a command economy is determined by
consumers
government
industries
labour unions.
\n """,
"""24  The co-efficient of price elasticity of supply is
% change in supply % change in price
% change in quantity supplied % change in price
% change in quantity supplied %change in income
% change in quantity demanded %change in income
\n """,
"""25  A change in supply of a commodity is due to a change in the
price of the commodity
cost of production
price of substitute
population growth rate.
\n """,
"""26 In a limited liability company, the greatest risk is borne by the
preference shareholders
debentures shareholders
ordinary shareholders
board of directors.
\n """,
"""27 A market characterized by absence of close substitutes of goods and services is an example of
a monopoly
an oligopoly
a perfect competition
a monopolistic competition.
\n """,
"""28 An inflation that co-exists with high rate of unemployment is
hyperinflation
cost-push inflation
stagflation
demand-pull inflation.
\n """,
"""29 The growth and development of small and medium scale enterprises in Nigeria is hampered by
poor regulatory framework
poor access to credit facilities
poor management
the small size of the market.
\n """,
"""30 A major determinant of demand is
incentives to workers
level of technology
population
cost of production.
\n """,
"""31 Which of the following can be used to measure the Gross National Product
 C+I+G-F(X+M)
 C+I+G+(X-M)
 C+I+G+X
 C+I+G
\n """,
"""32 Find the median of the following set of data 35, 10, 14, 38, 15, 18, 22, 30 and 28.
 10
 22
 38
 35
\n """,
"""33 The problem of what to produce is determined by
consumption pattern
the distribution pattern
the state of technology
the volume of production
\n """,
"""34 The main function NNPC is to
develop the oil producing areas
oversee the development of the oil sector
ensure regular supply of products
fix the prices of petroleum products
\n """,
"""35 A major feature of an underdeveloped economy is
low rate of population growth
excess capacity utilization
low level of unemployment
low level of standard living.
\n """,
"""36 A tax on land will ultimately fall
partly on agents and users
partly on users and owners
entirely on owners
entirely on users.
\n """,
"""37 The deregulation on the petroleum sector in Nigeria will bring about
efficiency in pricing and distribution of the products
fixing appropriate production quotas
an end to the importation of fuel
an end to foreign firms' dominance.
\n """,
"""38 One of the ways of correcting a deficit balance of payments is to
devalue a country's currency
predenominate a country's currency
reduce imports
reduce exports.
\n """,
"""39 A nation's net export is negative when her
 export is adjusted upwards
 external reserves deplete
 depreciation exceeds investments
 imports exceeds exports.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "D"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "C"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "A"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "D"),
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
        Economics_2018()
def Economics_2017():
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
        """0  An accurate census figure is an important tool for planners in
 providing employment
 siting industries
 providing social amenities
 allocating resources
\n """,
"""1 An accurate population census is important in other to
produce more food for the growing population
provide employment opportunities for the people
estimate a country's per capita income
fast track industrial development
\n """,
"""2 A major determinant of floating exchange rate is
the highest denomination of the currency
an Act of the parliament
the system of government
fast track industrial development
\n """,
"""3 If the importation of a commodity is limited to a definite quantity, the trade control measure imposed is
  excise duties
  import duties
  quotas
  tariff
\n """,
"""4 The main objective of WTO is to
ensure adequate protection of infant industries
provide a mechanism for tariff reduction
assist countries with chronic balance of payments problem
assist developing countries to execute developmental projects
\n """,
"""5  The major determinant of the total volume of output in an economy is the
level of total expenditure
composition of consumer spending
number of farmers
size of the labour force
\n """,
"""6 The labour force of a country is determined by the
age structure of the population
geographical distribution of the population
sex distribution of the population
number of people available for work
\n """,
"""7 The major implication of high dependency ratio on an economy is
high capital formation
vicious cycle of poverty
low cost of living
high standard of living.
\n """,
"""8 One of the major problems of agricultural sector in Nigeria is
low literacy level of farmers
small size of farms
pest attack on crops
inadequate modem farm implements.
\n """,
"""9 Cooperative societies are characterized with
divergent interest of members
limited liability
free entry and exit
unlimited size of membership.
\n """,
"""10 The marginal propensity to save measures the
ratio of change in saving
change in supply as a result of a change in consumption
ratio of change in consumption to a change in the level of income
average propensity to consume.
\n """,
"""11 Structural unemployment is mainly caused by
a change in the consumption pattern
a change in the business cycle
decrease in the output level
Seasonal variation.
\n """,
"""12 One of the major problems of census in Nigeria is
inadequate skilled personnel
high dependency ratio
distortion of census figures
High cost of conducting census.
\n """,
"""13 A decrease in government expenditure in an economy will cause general price level to
remain constant
fluctuate
fall
Rise.
\n """,
"""14  In the theory of consumer behaviour, the sum of all marginal utilities is
average marginal utility
the initial marginal utility
total utility
diminishing marginal utility.
\n """,
"""15 In a pure capitalist economy, the means and forces of production are owned and controlled by the
public and private sectors
feudal lords
public sector
private sector.
\n """,
"""16 The demand for money is referred to as the
amount of money in fixed deposit
desire to hold money intangible assets
need for money to invest
Desire to hold money in liquid form rather than investing it.
\n """,
"""17 If the cash reserve ratio is 30%, a new deposit of ₦20 million will increase supply by
₦57.8m
₦47.9m
₦69.78m
₦66.7m.
\n """,
"""18 A fall in the price c f ostentatious goods will
increase the quantity demanded
decrease the quantity demanded
decrease demand
increase demand.
\n """,
"""19 Payment of interests on loans and the repayment of capital sum at a future date is
balance debt
debt servicing
debt relief
debt retaking.
\n """,
"""20 The most difficult measure of central tendency to determine in a grouped data is
range
variance
mean
mode.
\n """,
"""21 Localization of industry is mainly determined by
diseconomies of scale
population growth
division of labour
access to raw materials.
\n """,
"""22 Geographical distribution of a population is affected by
low birth rate
the availability of skilled manpower
the availability of agricultural land
high birth ratenomic rent
\n """,
"""23 A tax burden on a commodity will be shared equally if the demand is
fairly elastic
perfectly inelastic
fairly inelastic
unitary elastic.
\n """,
"""24  Higher income taxes can be used to control
demand-pull inflation
high interest rates
cost- push inflation
hyperinflation.
\n """,
"""25 An indifference map is made up of a set of
consumers' total utility
consumer surplus
budget lines
indifference curves.
\n """,
"""26 Recapitalization policy will enable commercial banks to
employ more qualified workers
open more branches
reduce interest rate
have a very strong capital base
\n """,
"""27 The number of persons required to form a private company ranges from
ten to twenty
two to fifty
two to seven
seven to ten.
\n """,
"""28 The major function of international monetary funds is the
provision of short-run loans to medium scale industries
provision of long-term loans for infrastructure
development of agriculture in member countries
maintenance of stable exchange rates
\n """,
"""29 One of the major activities in the upstream sector of the Nigeria petroleum industry includes
transportation of finished products
refining of crude oil
marketing of refined petrol
exploration of crude oil.
\n """,
"""30 The law of supply states that the
higher the price the higher the quantity supplied
quantity supplied is always equal to the quantity demanded
lower the price the higher the quantity supplied
higher the price the lower the quantity supplied.
\n """,
"""31 One of the features of a perfect competitive firm is
restrictions to entry and exit
price discrimination
absence of transportation cost
product differentiation
\n """,
"""32  The basis for international trade is the
differences in natural resources endowment
differences in the population size
prevailing interest rate on multilateral loans
economic system in practice.
\n """,
"""33  Training farmers on the improved farming techniques is the major activity of
intermediate workers
middlemen
extension workers
creditors.
\n """,
"""34 In a free market economy, prices are determined by
consumers
producers
the central government
the forces of demand and supply.
\n """,
"""35 The basic economic problem of what to produce in an economy is determined by
the availability of labour
the means of distribution
the availability of resources
technological know-how.
\n """,
"""36 In Nigeria, a fall in the supply of petrol would generally affect the
import of goods and services
export of goods and services
general price level in the country
exchange rate of the Naira.
\n """,
"""37 The short-run equilibrium point of a perfectly competitive firm is attained at a point where
is equal to total cost
the demand curve is tangential to the marginal cost
the marginal cost curve is equal to the marginal revenue curve
the marginal cost is equal to the price of the firm.
\n """,
"""38 Government can protect consumers from exploitative prices by introducing
minimum price
price differentiation
price floor
maximum price.
\n """,
"""39 If a fall in the price of commodity K brought about an increase in the demand for commodity Y, the two commodities are
composites
derived in nature
substitutes
complements.
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "D"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "D"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "D"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "C"),
        Question(question_prompts[34], "D"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "C"),
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
        Economics_2017()
def Economics_2016():
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
        """0 The rate of interest change on loans depends largely on
the prevailing exchange rate
marginal efficiency of capital
the risk associated with the loan
the prevailing tax rate
\n """,
"""1 A valid explanation for real wage growth Is
an increase in the rate of productivity
the rising cost of capital accumulation
a contraction of employment in service industries
an increase in the quantity of labour
\n """,
"""2  If Mr. X lost his clerical job at a store and searched for a similar job for ten months before finding one this implies that Mr. X was
structurally unemployed
frictionally unemployed
seasonally unemployed
cyclically unemployed
\n """,
"""3 The choice of how to produce in a command economy is determined by
government
consumer
industrialists
labour unions
\n """,
"""4 In capitalist economies, questions about what to produce are ultimately answered by
income level of households
available technical skills in the economy
output decisions of firms
holding decision of households
\n """,
"""5 The best measure of dispersion to determine the tallest tree in a forest is
range
variance
standard deviation
mean deviation
\n """,
"""6 What is the percentage contribution of services to the national income?
15%
10%
54%
24%
\n """,
"""7 If the national income is 360m, the contribution of the manufacturing sector is
312m
39m
318m
317m
\n """,
"""8 Given that Qd = 40-2P and Qs = 6P+24. Calculate the equilibrium price.
₦34
₦32
₦36
₦16
\n """,
"""9 A change in demand for a normal goods implies that, there is a
change in the quantity demanded as price changes
shift in the demand curve
movement along a given demand curve
change in the price elasticity of demand
\n """,
"""10 A rightward shift of the budget line is caused by a
fall in consumer income
change in consumer taste
fall in the commodity relative price
rise in the commodity relative price
\n """,
"""11 Given the supply function P = 1/4(Qs+10) when P = N10, what is Qs?
20
15
50
30
\n """,
"""12 When price is set below equilibrium, this will lead to
an increase in the quantity supplied
a new equilibrium
a decrease in the quantity supplied
a fall in price
\n """,
"""13 Price mechanism determines the prices of commodities through
auctioning
market forces
the sales of treasury bills
government legislation
\n """,
"""14 If the production of a large firm is higher than that of a small firm, it is experiencing.
external economies of scale
external diseconomies of scale
internal economies of scale
internal diseconomies of scale
\n """,
"""15 Division of labour requires that, the tasks in a production line be performed
by specialists
in stages
by all workers
by unskilled labourers
\n """,
"""16 Given that FC = ₦500, VC = ₦1,500, and Q = 50 units. Find the average cost of the product.
  ₦30
  ₦40
  ₦10
  ₦20
  ₦20
\n """,
"""17 Rent and administrative expenses are examples of
average fixed costs
average variable costs
fixed costs
variable costs
\n """,
"""18 A perfect competitor will continue to expand output up to the point where
TC>TR
MR=AR
MC<MR
MC>MR
\n """,
"""19 One of the characteristics of a monopolist is that, he can influence
quantity produced by other producers
prices charged by other producers
both price and quantity
price or quantity
\n """,
"""20 A monopolist can boost up his revenue by
adjusting both price and output upward
reducing total output to match price
increasing price
reducing price
\n """,
"""21 Which of the following can be used to measure the Gross National product in an open economy?
C+I+G+(X+M)
C+I+G+X
C+I+G
C+I+G+(X-M)
\n """,
"""22 If MPC = 2/3 and investment is ₦100 million, the level of national income is
₦100 million
₦10 million
₦303 million
₦300 million
\n """,
"""23 The precautionary demand for money is determined by
 the rate of interest
 the level of savings
 the level of income
 general price level
\n """,
"""24 An inflation that co-exists with high rate of unemployment is
 hyperinflation
 stagflation
 demand-pull inflation
 cost-push inflation
\n """,
"""25 One of the challenges facing the banking industry in Nigeria is
ensuring technological security
providing employment
providing loans for investment
creating more money
\n """,
"""26 Short-term loans for investment are usually obtained through the
stock market
development banks
money market
capital market
\n """,
"""27 Given a base year and the price index of 175% the following year, which of the following year will arise?
The cost of living decreases of that year
The cost of living remains unchanged
The value of money rises by 75%
The value of money falls by 75%
\n """,
"""28 Wage freeze is a policy measure aimed at
encouraging investors
curbing inflation
regulating standard of living
curbing deflation
\n """,
"""29 A major obstacle to the development of Nigeria economy is
low capital formation
rural-urban migration
over dependence on oil
poor developmental policies
\n """,
"""30 A major feature of an underdeveloped economy is
excess capacity utilization
low rate of population growth
low level of standard of living
low level of unemployment
\n """,
"""31 An important role of agriculture in Nigeria's economic development is the
processing of raw materials for industries
regulation of price system
provision of infrastructure
provision of employment
\n """,
"""32 An advantage of large-scale farming over peasant farming is in the area of
providing research and massive employment of labour
redistributing national income to various regions of the country
encouraging the use of traditional implements
encouraging urban-rural migration
\n """,
"""33 A major disadvantage of localization of industry is
the risk of structural unemployment
over-utilization of installed industrial capacity
the risk of seasonal unemployment
under-utilization of installed industrial capacity
\n """,
"""34 One major factor that determines the location of an industry is
tax exemption grant
its proximity to the market
the capital base
the social responsibility of the firm
\n """,
"""35 The major contribution of OPEC to the Nigerian economy is the
provision of social infrastructures
granting of subsidies on petroleum products
stabilization of oil prices
building of refineries
\n """,
"""36 The loading of crude oil at the terminal is an activity in the
downstream sector of the oil industry
upstream and downstream sector of the oil industry
upstream sector of the oil industry
midstream and upstream sectors of the oil industry
\n """,
"""37 The short-run average variable cost of a firm will rise owing to
  the expansion of factory space
  the building of new warehouse
  an increase in the cost of labour
  an increase in the salaries of directors
\n """,
"""38 Firms embark on vertical integration in other to
take over markets formally controlled by other firms
prevent other firms from entering the market
reduce advertisement and management cost
enjoy economies of largescale production
\n """,
"""39 The voting power in co-operative societies is vested on
management
members without loan
shareholders
members with the highest contribution
\n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "A"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "C"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "C"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "B"),
        Question(question_prompts[37], "C"),
        Question(question_prompts[38], "D"),
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
        Economics_2016()
def Economics_2015():
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
         """0  If the standard deviation of a given data is 53, what is the variance?
  2,082
  2,809
  2,808
 2,209
\n """,
"""1   Which of the following set of statistical tools is used for further economic analysis?
  the median and standard deviation
  the mean and mode
 the mean and standard deviation
  the mode and median
\n """,
"""2 An advantage of the range as a measure of dispersion is that it
  can be used to calculate openended distribution
  make use of all values of observations in a distribution
 takes all values into consideration
  is useful for further statistical calculation
\n """,
"""3  Find the median of the following set of data 35, 10, 14, 38, 15, 18, 22, 30 and 28
  10
  38
  35
 22
\n """,
"""4  An increase in demand without a corresponding change in supply will lead to
  a decrease in equilibrium price and increase in equilibrium quantity
  an increase in equilibrium price and quantity
  a decrease in equilibrium price and quantity
  an increase in equilibrium price and a decrease in equilibrium quantity
\n """,
"""5  An increase in the price of a commodity will result in
  a decrease in the quantity demanded
  an increase in demand
  an increase in quantity demanded
 a decrease in demand
\n """,
"""6 If the price of a bicycle changes from N120 to N80 and quantity bought changes from 300 to 500 units, the elasticity of demand for bicycle is
  66.7
  0.5
  1.5
 2.0
\n """,
"""7  One of the assumptions of the cardinalist approach is
  diminishing marginal rate of substitution
  the consistency and transitivity of choice
  that total utility depends on the quantity of the commodities consumed
  unstable marginal utility of money
\n """,
"""8  Utility is the satisfaction derived from the
  distribution of goods and services
  use of goods and services
  demand of goods and services
  production of goods and services
\n """,
"""9   One of the major factors that brings about changes in supply is
  market discrimination
  availability of storage facilities
  the cost of storage
  incentives granted to workers
\n """,
"""10  If P = 14 (Qs + 10). What is the quantity supplied at N14?
  14
   60
  46
  32
\n """,
"""11 If the supply of a product is elastic, a small reduction in price will
  reduce the cost of production
  reduce the quantity supplied
  increase the quantity supplied
  lead to no change in the quantity supplied
\n """,
"""12 The supply of beverages by firms in a monopolistic market is an example of
 derived demand
  competitive supply
 composite supply
  joint demand
\n """,
"""13  If the price of a commodity is fixed below equilibrium, this will lead to
  excess demand
  a decrease in price
  an increase in price
 excess supply
\n """,
"""14  One of the criticisms of the price mechanism is that
  producers are sovereign
  it provides low degree of freedom
  it widens the inequitable gap
  consumers are sovereign
\n """,
"""15  In Nigeria, government can reduce the cost of accommodation by fixing rent
  at the prevailing rate
  at the equilibrium price
  above the equilibrium price
  below the equilibrium price
\n """,
"""16  If a refinery achieves a reduction in cost by purchasing and transporting crude oil in large quantities, it enjoys
 economies of scale
  specialization
 division of labour
  diseconomies of scale
\n """,
"""17 An isoquant lying above to the right of another represents
  a higher output level
  constant returns to scale
  over-capacity utilization
  a lower output level
\n """,
"""18  A measure of national income used as comparison of standard of living among nations is
  net national product
  gross domestic product
  gross national product
  per capita income
\n """,
"""19  The speculative demand for money is inversely related to the
  interest rate
  level of income
  exchange rate
  inflation rate
\n """,
"""20  If Mr. K obtains a N50.000 loan from a bank for the purpose of providing household needs, the demand for money is said to be
 transactionary
  speculative
  precautionary and speculative
 transactional and speculative
\n """,
"""21  Which of the following is used by the Central Bank of Nigeria to control inflation?
 Tariff on imports
 Tax rate
 Exchange rate
 Discount rate
\n """,
"""22 If CBN reduces money supply, the interest rate will
 fluctuate
  rise
 fall
 remain unchanged
\n """,
"""23  An example of an expansionary fiscal policy action is
  decrease in the corporate profit tax rates
  decrease in welfare payments
  purchase of government securities
 decrease in the bank rate
\n """,
"""24   A tax on land will ultimately fall
  partly on agents and users
  entirely on users
  entirely on owners
  partly on users and owners
\n """,
"""25   One of the goals of development plans in Nigeria is to
  increase the profitability of multinational businesses
 improve the country's GDP
  achieve higher standard of living for the citizens
  deregulate the economy
 \n """,
"""26 Life insurance companies contribute to economic development by holding a part of their assets in
 long-term financial instruments
 money market instruments
 cash and near money
 short-term financial instruments
\n """,
"""27  In order to add value to Nigeria agricultural produce, there is need to
   cultivate high breed crops
  process them into finished goods
 adopt modern storage methods
  advertise them in European markets
\n """,
"""28  The main reason for low agricultural produce in west Africa is need to
 the presence of large-scale agroallied industries
  high dependency ratio
 over dependence on agriculture for subsistence
  the use of crude implements in farming process
\n """,
"""29  The most important determinant for the location of a brick industry is the availability of
  market
 power supply
  water
 raw materials
\n """,
"""30  In Nigeria, efficiency in public corporations can be achieved through
 public offer
 indigenization
 privatization
  nationalization
\n """,
"""31 Government participation in the oil industry was necessitated by the
 annual increase in production
 formation of OPEC
 high demand for crude oil
  huge investment outlay
\n """,
"""32  The deregulation of the petroleum sector in Nigeria will bring about
  efficiency in pricing and distribution of the products
  an end to the importation of fuel
  an end to foreign firms' dominance
  fixing appropriate production quotas
\n """,
"""33 A distinguishing characteristic of consumer co-operative society is that the
  the maximum number of shareholders is 20
  members are the owners
 members are the workers
 the minimum number of shareholders is 5
\n """,
"""34 A major disadvantage of partnership business is
  difficulty in the transfer of shares
  distrust among members
 limited liability
 large capital outlay
\n """,
 """35 The quality of labour force in Nigeria can be improved by
  establishing more tertiary institutions
  creating sufficient job opportunities
  encouraging the study of science and technology
  establishing more skills acquisition centres
\n """,
"""36 The effect of emigration on a country's population is
 decrease in the population
 decrease in job opportunities
 increase in population
 increase in dependency ratio
\n """,
"""37  A measure for preventing the external value of the naira from falling is for the government to 22
 increase its spending with foreign Reserve
  sell its own currency
  reduce interest rate
  buy its currency with foreign reserve
\n """,
"""38  A fiscal policy instrument that can influence the demand pattern in an economy is
  government spending
  interest rate
  income tax
  tariff
\n """,
"""39  One of the main achievements of the Economic Commission for Africa is
 eliminating trade restrictions among States
  encouraging transport and communication development
  guaranteeing a steady flow of foreign investment into Africa
 providing the machinery for collaboration on monetary issues
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "A"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "A"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "C"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "A"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "D"),
        Question(question_prompts[21], "B"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "D"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "B"),
        Question(question_prompts[38], "C"),
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
        Economics_2015()
def Economics_2014():
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
        """0  The primary motive for an individual engaging in production is to
        make profit
        satisfy basic human wants
        redistribute wealth
        put inputs into use
        \n """,
        """1 One of the characteristics of free trade zone is
        common tariff against nonmember countries
        different trade policies of nonmember countries
        free factor mobility within the zone
        harmonized trade among member countries
        \n """,
        """2 If Nigeria imports vehicles from Japan the transaction will appear as a
        debit on Japan's balance of payments
        credit on Japan's balance of payments
        credit on Nigeria's balance of trade
        credit on Nigeria's balance of payment
        \n """,
        """3 One of the objectives of ADB is to
        provide subsidies on imported goods to member countries
        mobilize short-term loans for member countries
        promote economic and social development of member countries
        provide technical assistance to only poor member countries
        \n """,
        """4  The choice of the method of production in an economy is determined by the
        level of technical know-how
        rate of population growth
        availability of natural resources
        level of income
        \n """,
        """5 The amount of labour hired depends on the
        number of skilled labour available
        skill of labour
        marginal productivity of labour
        price of the inputs
        \n """,
        """6 An effective way of controlling inflation in a mixed economy is to
         increase productivity
         reduce income tax
         ration available output
         increase imports
        \n """,
        """7 One of the limitations PPC assumption is that there is
         no indication of technological development
         no recognition of preferred goods for countries
         technical inefficiency
         abundant resources
        \n """,
        """8 A major disadvantage of the arithmetic means is that it is
         not useful for large data
         not suitable for further statistical analysis
         cumbersome to determine the actual value
         affected by extreme data
        \n """,
        """9 Demand patterns are determined by the market on the basis of
         scale of preference
         consumer sovereignty
         consumer rationality
         price of the commodity
        \n """,
        """10 A consumer surplus measures the
         benefits derived from consuming a cheap commodity
         excess of total expenditure over total utility
          difference between marginal utility and marginal cost
         excess of marginal utility over price
        \n """,
        """11 If the demand for one commodity excludes another, it is said to be
         complementary demand
         competitive demand
         composite demand
         derived demand
        \n """,
        """12 The median of an odd-numbered set of scores is the
          Middle value in the set
          Highest value in the set
          Arithmetic means of the set
          Most frequent occurring score
        \n """,
        """13 If demand increases without a change in supply, equilibrium price and quantity will
         remain unchanged
          shift inward
          fall
          rise
        \n """,
        """14 In the process of production, total output is at maximum when
          MP=0
          MP>0
          AP=0
          AP>0
        \n """,
        """15  When a consumer is at equilibrium, the MRSxy is equal to the
          sum of the prices
          product of the two prices
         ratio of the two prices
         difference of the two prices
        \n """,
        """16  Minimum price legislation by government will
         reduce supply
         increase supply
          reduce demand and create surplus
         increase demand and create scarcity
        \n """,
        """17 Ranking is the method use in measuring
          marginal utility
         ordinal utility
         cardinal utility
         total utility
        \n """,
        """18  If a firm is faced with an elastic supply curve, its revenue will
          be supplied at a higher price
          double at a higher price
         increase by more than the percentage increase in price
         equal percentage change in price
        \n """,
        """19 The optimal range of output for a perfectly competitive firm is
         AC is lowest
         AVC is lowest
         MC is rising
          MC is falling
        \n """,
        """20 A firm will experience diseconomies of scale when
         there are difficulties in coordinating production
          there is shortage in labour supply
         the size of market is small
         there is an increase in the price of raw materials
        \n """,
        """21 The law of variable proportions is applicable only
         in the long-run period
          to large-scale enterprises
         to small-scale enterprises
         in the short-run period
        \n """,
        """22 If real income increases while nominal income remains the same, it can be inferred that
        Unemployment rate has decreased
        General prices have fallen
        Employment rate has risen
        General prices have risen
       \n """,
        """23  One of the characteristics of oligopoly is the availability of
         few sellers
         few buyers
         many sellers
         a single seller
        \n """,
        """24 The profit of a monopolist can be eliminated where price equals
         AFC
         MC
         AC
         AVC
        \n """,
        """25 Bank consolidation policy in Nigeria is a measure to increase
         the capital base of banks
         employment opportunities in banks
         the number of shareholders
         the number of branches
        \n """,
        """26 An increase in the circulation of money without a corresponding increase in output will lead to
         a rise in income levels
         stagflation
         inflation
         deflation
        \n """,
        """27 In national income accounts, an item counted as part of government spending is
         salaries and wages
          pension
          scholarship
         social welfare
        \n """,
        """28 If aggregate demand is lower than total output in an economy national income will
          be constant
         be at equilibrium
         increase
         fall
        \n """,
        """29  During the era of barter, money was generally in the form of
         notes
         precious metals
         coins
         commodities
        \n """,
        """30 A country achieves economic development when there is
        an increase in military expenditure
        an increase in capacity utilization
        a sustained increase in per capital income
        an even distribution of goods and services
        \n """,
        """31 An indicator of growth in an economy over a period of time is the
        GDP gap
        GDP at factor cost
        GDP at market price
        GDP deflator
        \n """,
        """32 A country embarks on deficit financing in order to
        increase revenue
        reduce aggregate demand
        curb inflation
        stimulate investment
        \n """,
        """33 The import-substitution strategy of industrialization is to encourage
        domestic production
        large-scale production
        importation
        exportation
        \n """,
        """34 Upstream oil activities involve the
        management of pollution
        marketing of refined products
        exploration of crude oil
        refining of crude oil
        \n """,
        """35 Agricultural production in Nigeria is constrained by
        ineffective use of stabilization measures
        inadequate demand
        poor implementation of policies
        balance of payments deficits
        \n """,
        """36 The main function of NNPC is to
        oversee the development of the oil sector
        develop the oil producing area
        fix the price of products
        ensure regular supply of products
        \n """,
        """37 A major disadvantage of a socialist economy is that
        corruption is rampant
        consumer's sovereignty is lost
        income inequality is entrenched
        there is high level of unemployment
        \n """,
        """38 The privatization of public enterprises will lead to efficient management of resources in the economy. This statement can best be described as
        normative reasoning
        inductive reasoning
        deductive reasoning
        positive reasoning
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "C"),
        Question(question_prompts[1], "D"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "C"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "D"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "D"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "B"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "B"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "B"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "D"),
        Question(question_prompts[27], "D"),
        Question(question_prompts[28], "D"),
        Question(question_prompts[29], "D"),
        Question(question_prompts[30], "C"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "C"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "A"),
        Question(question_prompts[37], "A"),
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
        Economics_2014()
def Economics_2013():
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
        """0 The sign of the slope of a graph in economic analysis is important because it
shows whether a good is normal or inferior
shows the relationship between variables
reveals the magnitude of the change between variables
helps to determine the unit of measurement of variables
\n """,
"""1 If the quantity of rice bought decreases from 250 tonnes to 200 tonnes owing to a 2% rise in price, it shows that there is a change in
consumers' income
demand
consumers' tastes
quantity damanded
\n """,
"""2 A rise in income will, ceteris paribus, bring about
a movement along the demand curve
a leftward shift of the demand curve
a rightward shift of the demand curve
no effect on the demand curve
\n """,
"""3 If the price of an item increases by 8% while the quantity demanded falls from 1500 units to 1492 units, the demand is said to be
perfectly elastic
inelastic
elastic
perfectly inelastic
\n """,
"""4 Comparison of interpersonal utility is impossible because
  utility is measured in utils
  marginal utility is not observable
  utility is subjectively determined
  individual income differ
\n """,
"""5 When the slope of the total utility curve is declining, the marginal utility of a consumer will be increasing if he
stops consuming more of the commodity
reduces the quantity consumed
increases the quantity consumed
consumes more of another commodity
\n """,
"""6 The supply of cocoa is influenced by
seasonal conditions
the efficacy of fertilizer used
the demand for beverages
the availability of close substitutes
\n """,
"""7 If quantity supplied is constant irrespective of price changes, the supply elasticity is
unitary
infinity
fairly elastic
perfectly inelastic
\n """,
"""8 The cost elasticity of supply is a useful instrument for measuring
profit
productivity
national income
price index
\n """,
"""9 The invisible hand promotes the interests of
consumers
society
government
producers
\n """,
"""10 Fixing price above equilibrium will cause
 demand and supply to remain constant
 an increase in quantity supplied
 an increase in supply
 a decrease in quantity supplied
\n """,
"""11 An important function of the price system is to
ensure that producers' profits remain high
guarantee full employment of resources
allocate resources to most productive uses
protect the economic interests of government
\n """,
"""12  If all factors are variable in the long run,firms will experience
 decreasing returns to scale
 increasing returns to scale
  diminishing returns
economies of scale
\n """,
"""13 The equilibrium point of a firm is attained at the point where the isoquant is
 greater than the isocost
 less than the isocost
 tangent to the isocost
  greater than the output
\n """,
"""14 The long-run average cost curve touches to the short-run average cost curves at the
  minimum points of all short run average cost curves
  declining points of all short-run average cost curves
 minimum point of only one of the short-run cost curves
 rising points of all short-run average cost curves
\n """,
"""15  If a firm doubles all inputs in the long run and the total output is less than doubled, this results in
  diminishing returns
  constant returns to scale
  increasing returns to scale
  decreasing returns to scale
\n """,
"""16 Patents and copyrights enable monopolists to
  determine the quality of their products
  determine the scale of their products
  restrict information flow to new firms
  restrict entry of new firms
\n """,
"""17 A discriminatory monopoly is characterized by
a common elasticity in different markets
different elasticities in different markets
a finite elasticity in all markets
zero elasticity in all markets
\n """,
"""18 Net National Product is derived by deducting
net exports from GNP
subsidies from GDP
taxes from GDP
depreciation from GNP
\n """,
"""19 The money that commands a higher market value than its face value is called
paper money
standard money
commodity money
fiat money
\n """,
"""20 If a basket of commodities cost N120 in the base year and N240 in the current year, calculate the price index
  100
  200
  240
  300
\n """,
"""21 The minimum amount which banks are required to deposit with the central bank is determined by the
 liquidity ratio
 cash reserve ratio
 minimum lending rate
 aggregate credit ceiling
\n """,
"""22 The major function of money market is to
 provide funds for long-term financing
 provide funds short-term financing
 stabilize the value of the local currency
  stabilize domestic prices
\n """,
"""23 An ad valorem tax is imposed on
  special commodities
  exports
  imports
 the value of a commodity
\n """,
"""24   A huge national debt is an indication that the gold reserves of a nation has
  appreciated
  decreased
  depreciated
  stagnated
\n """,
"""25 Rapid economic development in Nigeria is realizable by
 continuous dependence on oil
 concentrating more on agriculture
  developing the tourism industry
  diversifying the economy
\n """,
"""26 The primary reason for desiring economic growth is to
 control inflation
 reduce poverty
 redistribute income
 raise standard of living
\n """,
"""27 An emerging agricultural export crop in Nigeria is
  cassava
 cotton
 cocoa
 soya beans
\n """,
"""28 A strategy for improving agriculture in Nigeria will involve
  controlling the prices of agricultural products
  ensuring self-sufficiency in food production
  reducing agricultural exports
  establishing commondity boards
\n """,
"""29 A sugar industry is best located near the source of
 labour
 raw materials
 power
 capital
\n """,
"""30 An important contribution of small-scale industries to the Nigerian economy is in the area of
  technological development
 foregin exchange earnings
  raw materials processing
  labour employment
\n """,
"""31 A change in the pump price of petrol in Nigeria has a direct effect on the
  prices of consumer goods
  prices of essential goods
  cost of raw materials
  cost of transportation
\n """,
"""32 Long-term funds for investment projects are sourced from the
  money market
 commodity market
  foreign exchange market
 capital market
\n """,
"""33 A policy aimed at enhancing globalization of the Nigerian economy is
  indigenization
  dereglation
 commercialization
  privatization
\n """,
"""34  The Malthusian theory was concerned about the relationship between
 population growth rates of the rich and the poor nations
 population density and national income
  population growth rate and natural resources
 age distribution of population
\n """,
"""35 In a village of 50 persons, 10 immigrated, 25 died and 5 emigrated in year. Determine the total population
  10
  20
 30
 50
\n """,
"""36 A deficit balance of payments is measured by subtracting the debits from the credits in the
 current account
 current and capital accounts
 current and escrow accounts
 capital and escrow accounts
\n """,
"""37 One of the functions of ECOWAS is to
 provide funds for infrastructural development
 determine prices of exports
 redistribute income among citizens
  provide employment for citizens of member nations
\n """,
"""38 The reward on machinery and equipment in the process of production is known as
 profit
 interest
 rent
 wages
\n """,
"""39 An economy in which both the public and private sectors contribute to economic growth is as
 feudal economy
  capitalist economy
 socialist economy
 mixed economy
\n """,

    ]

    questions = [
        Question(question_prompts[0], "D"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "B"),
        Question(question_prompts[3], "B"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "C"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "D"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "B"),
        Question(question_prompts[14], "D"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "D"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "D"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "C"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "B"),
        Question(question_prompts[32], "D"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "B"),
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
        Economics_2013()
def Economics_2012():
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
        """0  Economics is the study of human behaviour as it relates to the
 efficient allocation of resources
 production of goods
 operation of companies
 generation of income
\n """,
"""1 The downturn in the prices of shares on stock markets is a highlight of
 efficient allocation of resources
the invisible hand
the regulatory nature of the market
consumer rationality
\n """,
"""2 The standard deviation of a set of data is
 always measured from the mode
the most representative of averages
always measured from the median
a measure of dispersion
\n """,
"""3 The mean is the best measure of central tendency because it
 is not affected by extreme values in a data
 is a midpoint value in an array of data
is a balancing point in an observation
can be calculated from incomplete data
\n """,
"""4 The most popular sizes of dresses and shoes are determined by the
range
mean
 mode
median
\n """,
"""5 If the demand for a good is more elasticthan its supply, the tax burden is borne
 equally by consumers and producers
 more by producers
more by consumers
more by retailers and producers
\n """,
"""6 If the price of a commodity with elastic demand increases, the revenue accruing to the producer will
double
 increase
 be constant
decrease
\n """,
"""7 An excess demand for beans will result from
an increase in the price of beans
 a decrease in the price of beans
an increase in the supply of beans
a decrease in the supply of beans
\n """,
"""8 Consumer surplus tends to be higher when demand is
inelastic
perfectly elastic
elastic
unitarily elastic
\n """,
"""9 One of the assumptions of ordinal utility theory is that
choice is not consistent
utility can be ranked
total utility is a function of price
satisfaction is measurable
\n """,
"""10 The law of diminishing marginal utility explains why
the slope of a normal demand curve is negative
an abnormal demand curve slopes upwards
the slope of a normal demand curve is positive
the consumption of inferior goods increases with income
\n """,
"""11 If a consumer plans to spend 120k on four oranges but spent 80k, his consumer surplus is
#1.50
#0.40
#1.00
#2.00
\n """,
"""12 A set of factors that can shift the supply curve are changes in
 weather, price and technology
technology, weather and population
technology, price and taste
population, price and taste
\n """,
"""13 If the coefficient of price elasticity of supply is greater than one, the supply is said to be
perfectly elastic
fairly inelastic
infinitely inelastic
fairly elastic
\n """,
"""14 If commodity X is a by-product of commodity Y, this implies that both commodities are
 in competitive supply
in composite supply
jointly supplied
in excess supply
\n """,
"""15 In perfect competition, price is determined by the
government
sellers
buyers
market
\n """,
"""16 In order to reduce hardship faced by consumers due to high prices government can introduce
maximum prices
commodity boards
 minimum prices
price control boards
\n """,
"""17 Average product is less than marginal product when
there is constant returns to scale
there is increasing returns to scale
there is decreasing returns to scale
diminishing returns set in the margine 
\n """,
"""18 A firm enjoying economies of scale is said to be
reducing average cost as production increases
benefiting from the activities of other firms
maximizing profits as production increases
having an upward-sloping average cost curve
\n """,
"""19 The rising portion of the long-run average cost curve of a firm is an indication that it is experiencing
increasing efficiency
economies of scale
 diseconomies of scale
increasing marginal returns
\n """,
"""20 An industry's supply curve is more likely to be elastic when firms are
 enjoying free entry and exit
 operating at full capacity
operating below capacity
maximizing profits
\n """,
"""21 One of the characteristics of monopolistic competition is that
there is mobility of factors of production
no single seller dominates the market
the firms are price-takers
consumers have perfect knowledge of price
\n """,
"""22  The demand curve for factors of production
is perfect elastic
slopes upwards
slopes of downwards
is perfectly inelastic
\n """,
"""23.An agreement among firms on price and segmentation is termed
cartel
collusion
haggling
specialization
\n """,
"""24 In national income accounting, tax is determined by the
level of income
level of consumption
level of investment
rate of savings `
\n """,
"""25 A decrease in aggregate spending in an economy will ultimately lead to
boom
inflation
deflation
recession
\n """,
"""26 If MPC is 0.7 while government expenditure increased by ? 150m, the equilibrium national income is
#214 million
#45 million
#105 million
#500 million
\n """,
"""27 The function of money which makes division of labour possible is its
unit of account
store of value
medium of exchange
standard of deferred payment
\n """,
"""28 By buying treasury bills, the Central Bank of Nigeria intends to
increase money supply in the economy
reduce the cash reserve ratio for banks
reduce money supply in the economy
increase the capital base of commercial banks
\n """,
"""29 The velocity of money is represented as
Money supply Real GDP
Real GDP Money supply
Nominal GDP Money supply
Real GDP Nominal GDP
\n """,
"""30  One of the functions of commercial banks is
maintaining stable price in the economy
regulating monetary policies
 granting loans to customers
 issuing bank notes and coins
\n """,
"""31 A strategy for curbing unemployment is to
 implement government stabilization policy
 increase taxes and decrease government expenditure
increase government expenditure and decrease taxes
ensure even distribution of job opportunities
\n """,
"""32 In Nigeria, the distribution of job opportunities
balanced budgeting
deficit budgeting
surplus budgeting
zero budgeting
\n """,
"""33 National development plans in Nigeria fail mainly because of
overdependence on foreign aids
inadequate funding of projects
poor implementation strategies
shortage of skilled manpower
\n """,
"""34 The ultimate aim of agricultural policies in Nigeria is to achieve
food sufficiency
industrialization
full employment
industrial capacity utilization
\n """,
"""35 Government can boost agricultural output in Nigeria primarily by
embarking on buffer stock programmes
placing embargo on food importation
granting subsidies on farm inputs
placing farmers on monthly income
\n """,
"""36 Localization of industries refers to the
spread of firms producing different products
 siting of industries near the market
 concentration of firms of an industry
siting of firms producing different products
\n """,
"""37 In developing countries, governments influence the location of industries in order to
spread development
redistribute wealth
encourage entrepreneurs
encourage industries to earn high profits
\n """,
"""38 A disadvantage of Nigeria's dependence on imported petroleum products is the
instability in the demand for the products
dominance of multinational firms
instability in the supply of the product
poor maintenance of the refineries
\n """,
"""39 The maximum number of shareholders for a limited liability company's is
twenty
five
seven
infinite
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
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "D"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "C"),
        Question(question_prompts[12], "A"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "D"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "D"),
        Question(question_prompts[18], "A"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "C"),
        Question(question_prompts[22], "B"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "B"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "B"),
        Question(question_prompts[28], "B"),
        Question(question_prompts[29], "A"),
        Question(question_prompts[30], "B"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "C"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "B"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "A"),
        Question(question_prompts[38], "B"),
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
        Economics_2012()