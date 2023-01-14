from Question import Question
def FinancialAcc_2016():
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
        """0 Use the information below to answer questions 1 and 2. Ada and Udo are lawyers who went into partnership \nas Ado and Co. Ada brought cash of ₦12 000, furnishings worth ₦18,000 and a motor vehicle worth ₦70,000. Udo on the other hand brought in cash N10 000, his building valued at ₦105 000 and a personal computer worth ₦35 000. 1. What is the capital of Ado & Co.?
        A. ₦100 000
        B. ₦22 000
        C. ₦250 000
        D. ₦150 000.
        \n """,
        """1 Use the information below to answer questions 1 and 2. Ada and Udo are lawyers who went into partnership\n as Ado and Co. Ada brought cash of ₦12 000, furnishings worth ₦18,000 and a motor vehicle worth ₦70,000. Udo on the other hand brought in cash N10 000, his building valued at ₦105 000 and a personal computer worth ₦35 000. 2. What is the profit-sharing ratio if it is based on capital contributed by Ada and Udo?
        A.3:2
        B.2:3
        C. 1:2 
        D. 2:1.
        \n """,
        """2 One major advantage of a ledger is that it __.
        A. is a book of original entry
        B. is only accessible to shareholders during liquidation
        C. can be used by any type of business
        D. removes the need for preparing a balance sheet after each transaction
        \n """,
        """3 A trial balance is usually prepared by an accountant from account balances in the ledger for the purpose of __.
        A. classifying accounts in the ledger
        B. identifying the balance sheet items
        C. providing a basis for establishing the accountant's competence
        D. testing arithmetical accuracies of the ledger account balances. 
        \n """,
        """4 The total of the creditors at the beginning of the year was ₦4 600 and at the end of the year ₦5 250.\n During the year, ₦26 500 was paid to suppliers and ₦130 was received in discounts from these suppliers. The purchases for the year would be __?
        A. ₦27 038
        B. ₦26 630
        C. ₦27 280
        D. ₦27 150
        \n """,
        """5 Given: ₦ Capital at the beginning  20 000 Drawings     3 000 Capital at end    30 000 New capital introduced \n 8,000 What is the profit for the period?
        A. ₦8 000
        B. ₦4 000
        C. ₦5 000
        D. ₦6 000.
        \n """,
        """6 Given:  ₦ Bank account    59,410 Capital account   50,000 Purchases account  20,000 Rent    \n 2,500 Stationery    90 Typewriter    6,500 Sales     38,500 In preparing a trial balance from the list of balances given above, what is the total; in debit and credit columns?
        A. ₦88,500
        B. ₦85,800
        C. ₦147,910
        D. ₦138,500
        \n """,
        """7  The purchase of two generators by Hassan Electronics Enterprises should be recorded as
        A. a part of capital in the capital account
        B. an acquisition of stock
        C. an expense in its general office expense account
        D. an acquisition of fixed assets 
        \n """,
        """8 Appropriation Account Kudu      Wale ₦    ₦  Interest on capital  750   550 Salaries   800    600 Share \nof profits   3,300      3,300 Determine the net profits of the partnership.
        A. ₦6,600
        B. ₦4,850
        C. ₦9,300
        D. ₦4,450
        \n """,
        """9 Dele and Seun who are in partnership have decided to convert their business into a limited liability\n company where both become directors. To convert the __.
        A. they will simply continue since there are no new members.
        B. the partnership is formally ended and new company books opened 
        C. computation of goodwill must be done as it is legally required
        D. the shares and all other items will be shared equally and not in their former ratios.
        \n """,
        """10 The most convenient cash book used by a petty trader operating in an area where there is no banking\n facility is __.
        A. four column
        B. single column
        C. two column
        D. three column.
        \n """,
        """11 A general journal contains __.
        A. date, narration, folio, debit and credit
        B. folio, credit. date, debit and sales
        C. date, narration, folio. debit and purchases
        D. folio, credit. narration. date and discount.
        \n """,
        """12 Use the information below to answer questions 13 and 14. Given ₦  Fixed assets    85,600\n Sales     197,000 Stock     34,300 Salaries and wages   37,000 Purchases    127,700 Share capital    120,000 Creditors     16,050 Motor expenses \n  10,500 Debtors     25,000. 13 What is the cash balance?
        A. ₦12,095
        B. ₦12,905
        C. ₦12,590
        D. ₦12,950
        \n """,
        """13 Use the information below to answer questions 13 and 14. Given ₦  Fixed assets    85,600 \n Sales     197,000 Stock     34,300 Salaries and wages   37,000 Purchases    127,700 Share capital    120,000 Creditors  \n   16,050 Motor expenses   10,500 Debtors     25,000. 14. Determine the total of the trial balance
        A. ₦335,050
        B. ₦323,050
        C. ₦333,000
        D. ₦230,550
        \n """,
        """14 The value of capital invested by the owners is __. 
        A. ₦101,000
        B. ₦103,000
        C. ₦100,000
        D. ₦110.000
        \n """,
        """15 The liabilities of Udo Co. Ltd is
        A. ₦177,000
        B. ₦180,000
        C. ₦110,000
        D. ₦181,000
        \n """,
        """16 Use the information below to answer questions 17 and 18. ₦ Capital        2000 Bank        1200 \nPurchases       2500 Sales        6700 Stock        1300 Creditors        1000 Fixed assets       3700 Drawings      ? Drawings are always estimated at 60% of capital 17. The trial balance total is __. 
        A. ₦8700
        B. ₦9700
        C. ₦7800
        D. ₦7900
        \n """,
        """17 Use the information below to answer questions 17 and 18. ₦ Capital        2000 Bank        1200\n Purchases       2500 Sales        6700 Stock        1300 Creditors        1000 Fixed assets       3700 Drawings      ? Drawings are always estimated at 60% of capital . 18 Compute the amount withdrawn
        A. ₦1 000
        B. ₦2 000
        C. ₦1 500
        D. ₦1 250
        \n """,
        """18 Zakari started a business in January 2000. He bought a shop costing ₦54,000 and stock worth ₦7,600.\n Profit for the year amounted to ₦22,100. His closing capital was 73,800. Zakari's personal drawings amounted to
        A. ₦9,900
        B. ₦2,300
        C. ₦19,500
        D. ₦17,100
        \n """,
        """19 The balance on the provision for depreciation account is __.
        A. deducted from fixed assets on the balance sheet
        B. added to fixed assets on the balance sheet
        C. added to the current liabilities of the account
        D. deducted from the profit and loss account
        \n """,
        """20 What are the appropriate recording procedures for entries in the trial balance?
        A. Ledgers. source documents and trial balance
        B. Ledgers, trial balance and source documents
        C. Source documents, ledgers and trial balance
        D. Cash account, ledgers and trial balance.
        \n """,
        """21 Mr Bassev purchased a motor vehicle for use in his business and debited the purchases account with\n the same value. This is an error of __.
        A. principle
        B. omission
        C. original entry
        D. commission
        \n """,
        """22 Accrual accounting differs from cash accounting because it recognizes __.
        A. cash and creditors.
        B. cash and debtors
        C. debtors and creditors
        D. prepayment and cash
        \n """,
        """23 A private company is different from a public company because __.
        A. it cannot invite members of the public to subscribe for its shares
        B. it does not restrict the right to transfer its shares
        C. it can only offer its shares to members of the public for subscription 
        D. its shares are owned by one person.
        \n """,
        """24 The receipts and payments of account of a not-for-profit-making organization plays a similar role in \nprofit-making organization as __.
        A. a cash account
        B. an expenses account
        C. a balance sheet
        D. an income account
        \n """,
        """25 Osei, and Yabo were in partnership sharing profits and losses in the ratio of 3:2. On admitting Takwa,\n the profit and loss sharing ratio was changed to 1:1:1, supposed Takwa paid -₦30 000 for goodwill, this amount would be
        A. debited to goodwill account
        B. credited to Takwa's current account
        C. credited to the old partners' capital account
        D. shared to all the partners’ capital account. 
        \n """,
        """26 Commission-on-turnover is charged on
        A. savings accounts
        B. current accounts only
        C. all bank accounts
        D. fixed deposit accounts only
        \n """,
        """27 The medium that enables the ATM to read the account details and process transactions directly with the\n account held in the bank is the __.
        A. smart card
        B. computerized account
        C. magnetic strip
        D. communication network
        \n """,
        """28 Use the information below to answer questions 29 and 30. Adodo Enterprises and Loss Account (Extract)\n ₦   ₦  Opening stock   5,000 Sales      100,000 Purchases   ? Less closing stock 5,600 Cost of goods sold ?  Gross profit ? 100,000  100,000 . 29 If the gross profit margin is  10%, what is the value of the cost of goods sold?
        A. ₦90,000
        B. ₦10,000
        C. ₦110,000
        D. ₦105,600
        \n """,
        """29 Use the information below to answer questions 29 and 30. Adodo Enterprises and Loss Account (Extract)\n ₦   ₦  Opening stock   5,000 Sales      100,000 Purchases   ? Less closing stock 5,600 Cost of goods sold ?  Gross profit ? 100,000  100,000 . 30 If the opening stock is 5% of sales, calculate the purchases.
        A. ₦95.600
        B. ₦90,600
        C. ₦95,000
        D. ₦85,000
        \n """,
        """30 A major cause of discrepancy between bank statement and the cash book that overstates the bank statement\n balance is the __.
        A. direct payment
        B. commission paid
        C. direct withdrawal
        D. interest received
        \n """,
        """31 The bank charges levied on a current account holder is the charges on __.
        A. transactions
        B. cash received
        C. turnover
        D. transfer
        \n """,
        """32 Given  ₦ Light expenses   400 Purchases    3,000 Sales     1,200 Creditors     2,250 Debtors     50 \nCalculate the total of the trial balance.
        A. ₦3,450
        B. ₦4,300
        C. ₦3,500
        D. ₦4,250
        \n """,
        """33 The major feature of a journal is that it has __. 
        A. six columns. date, particulars, folio, amount, debit and credit
        B. four columns, date, particulars, folio and amount
        C. three columns, date, particular and folio
        D. six columns, date, particulars, folio, debit and credit.
        \n """,
        """34 Use the information below to answer questions 35 and 36. ₦     ₦ Stock       20,000  Net sales   370,000 \nAdd purchases  250,000  Cost of goods available for sale 270,000 Less stock 31/12        40,000 Cost of goods sold        230,000 Rent expenses    35,000  . 35 Find the gross profit.
        A. ₦370,000
        B. ₦140.000
        C. ₦230,000
        D. ₦150,000
        \n """,
        """35 Use the information below to answer questions 35 and 36. ₦     ₦ Stock       20,000  Net sales   370,000\n Add purchases  250,000  Cost of goods available for sale 270,000 Less stock 31/12        40,000 Cost of goods sold        230,000 Rent expenses    35,000  . 36 Calculate the net profit. 
        A. ₦105,000
        B.₦35,000
        C. ₦40,000
        D. ₦115,000
        \n """,
        """36 Which of the following items is a capital expenditure?
        A. Maintenance of office machine.
        B. Purchase of office machinery
        C. Purchase of office stationery.
        D. Carriage inwards.
        \n """,
        """37 The corresponding entry of personal accounts found in the debit side of the cash book is to __.
        A. credit the ledger.
        B. credit real accounts.
        C. debit real accounts.
        D. debit the ledger.
        \n """,
        """38 The major focus of the trading account is to show __.
        A. net profit.
        B. total purchases.
        C. gross margin.
        D. total sales.
        \n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "A"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "C"),
        Question(question_prompts[9], "B"),
        Question(question_prompts[10], "B"),
        Question(question_prompts[11], "A"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "C"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "B"),
        Question(question_prompts[16], "B"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "B"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "C"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "C"),
        Question(question_prompts[23], "A"),
        Question(question_prompts[24], "C"),
        Question(question_prompts[25], "A"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "B"),
        Question(question_prompts[30], "A"),
        Question(question_prompts[31], "C"),
        Question(question_prompts[32], "A"),
        Question(question_prompts[33], "D"),
        Question(question_prompts[34], "B"),
        Question(question_prompts[35], "B"),
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
        FinancialAcc_2016()
def FinancialAcc_2017():
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
        """1. The major distinguishing element between the final account of a partnership and a sole trader is the
A. drawing
B. creditors account
C. appropriation account
D. capital account
\n """,
"""2. Goodwill appears in the books of a business only if it has been
A. raised in connection with the admission of a new partner
B. purchased at a certain price if it has been raised
C. raised to account for the true value of a business on the death of a partner
D. raised in other to prevent the balance sheet showing that the business is insolent
\n """,
"""3. A payment of cash of ₦20 to john was entered on the receipts side of the cash book in error and credited to john’s account. 
Which   of the following journal entries can be used to correct the error
A. John ₦40 Dr, cash ₦40 Cr
B. cash ₦40 Dr, john ₦40 Cr
C. cash ₦20 Dr, john ₦20 Cr
D. john ₦20 Dr, cash ₦20 Cr
\n """,
"""4. The following represents extracts from the trading account of a retail outlet for a retail outlet for a given month: 
₦ Opening stock    2400 Closing stock    6400 Other expenses   2000 Sales     11000 Profit     900 
What is the purchase figure for the month?
A. ₦13 000
B. ₦11 000
C. ₦12 000
D. ₦12 000
\n """,
"""5. Subscription relating to the accounting to the accounting year 1993 
in the income and expenditure account is __.
A. ₦14,300
B. ₦13,400
C. ₦15,050
D. ₦14, 550
\n """,
"""6. Accumulated fund on 1st January 1993 is __.
A. ₦8,570
B. ₦7, 520
C. ₦8, 470
D. ₦7,850
\n """,
"""7. Sobande incorporation acquired a machine that involved the following expenditures and related factors.  
₦ gross invoice price   15,000 sales tax     900 purchases discount taken    300 freight     750  
assembly of machines   500 installation of machines   800 assorted spare parts for future use        1200 
turning and adjusting machines     700 gross invoice price     15,000 
What is the initial accounting cost of the machine?
A. ₦17, 500
B. ₦18, 350
C. ₦19, 550
D. ₦18, 950
\n """,
"""8. A pottery company had sales of ₦176,000 during the current period and a gross profit rate of 40% the company cost of
 merchandise for sale during the period was ₦128,000. 
The company’s ending inventory is
A. ₦76 800
B. ₦51300
C. ₦32,000
D.₦22400
\n """,
"""Use the information below to answer questions 9 and 10. Zoom Plc balance sheet [extract] as at 
31st December, 1997  ₦    ₦  Paidup  capital 200,000   Fixed  assets  300,000 Share Premium 15,000 
Profit and loss account 60,000   Investments 180,000 Longterm      Stock 28,000 Loan Debtors 90,000 Creditors 200,000  
Provision (3,000)  87,000 Other Current 100,  000 Cash 60,000  Liabilities   Bank 100,000 ,         ,      
9. The quick ratio is __
A. 0.95:1
B. 0.82:1 
C. 1:53:1
D. 0.91:1
\n """,
"""Use the information below to answer questions 9 and 10. Zoom Plc balance sheet [extract] as at 31st December, 1997  ₦    ₦  
Paidup  capital 200,000   Fixed  assets  300,000 Share Premium 15,000 Profit and loss account 60,000   
Investments 180,000 Longterm      Stock 28,000 Loan Debtors 90,000 Creditors 200,000  
Provision (3,000)  87,000 Other Current 100,  000 Cash 60,000  Liabilities   Bank 100,000 ,         ,      
10. Determine the owners’ equity
A. ₦275,000
B. ₦755,000
C. ₦200,000
D. ₦215,000
\n """,
"""Use the information below to answer questions 11 and 12. ₦ Cost of raw materials consumed  300, 600 
Returns of raw materials     6,700 Closing stocks of raw materials   100,250 Manufacturing wages    27,000 
Lighting, power, insurance and rent relating to the factory are apportioned 1/3, 2/5, 1/6 and 1/7 
with totals ₦30,000; ₦75,000; ₦36,000 and ₦56,000 respectively.  
11. What is the cost of the opening raw materials?
A. ₦400,250
B. ₦398,250
C. ₦404,950
D. ₦418,350
\n """,
"""Use the information below to answer questions 11 and 12. ₦ Cost of raw materials consumed  300, 600 
Returns of raw materials     6,700 Closing stocks of raw materials   100,250 Manufacturing wages    27,000 
Lighting, power, insurance and rent relating to the factory are apportioned 1/3, 2/5, 1/6 and 1/7 
with totals ₦30,000; ₦75,000; ₦36,000 and ₦56,000 respectively.  
12. The production cost offinished goods is __.
A. ₦408,600
B. ₦381,000
C. ₦327,600
D. ₦54,600
\n """,
"""Use the information below to answer questions 13 and 14. ₦ Subscriptions received during the year    30,000 
Subscriptions owed last year   4,000 Subscriptions received for  next year    6,000  
13. The ₦6,000 subscription received is
A. capital
B. fixed asset
C. current asset
D. current liability
\n """,
"""Use the information below to answer questions 13 and 14. ₦ Subscriptions received during the year    30,000 
Subscriptions owed last year   4,000 Subscriptions received for  next year    6,000  . 
14. What is the subscription to be charged to income and expenditure account?
A. ₦20,000
B. ₦30,000
C. ₦34,000
D. ₦36,000
\n """,
"""Use the information below to answer questions 15 and 16.Erero’s Trading Account for the month ended 31/05/2001.
 ₦ ₦ ₦  Opening Stock  45000  Sales       161000  110000  
Less returns        4000  6000 104000       157000 149000 Less closing stock  ??? Cost of sales  ??? 
Gross profit  ???  157,000   157,000 The gross profit ratio for the company is 25%.  
15. If the total expenses is ₦20 845, what will be the net profit for the company during the month?
A. ₦18405
B. ₦21655
C. ₦19149
D. ₦16168
\n """,
"""Use the information below to answer questions 15 and 16.Erero’s Trading Account for the month ended 31/05/2001. 
₦ ₦ ₦  Opening Stock  45000  Sales       161000  110000  
Less returns        4000  6000 104000       157000 149000 Less closing stock  ??? Cost of sales  ??? 
Gross profit  ???  157,000   157,000 The gross profit ratio for the company is 25%.  
16. The closing stock for this company is __.
A. ₦72 000
B. ₦42 500
C. ₦31 250
D. ₦45 000
\n """,
"""Use the information below to answer questions 17 and 18.  ₦ 
Capital     24,000 Land and building   18,470 Mortgage on premises 11,090 
Drawings     3,000 Profit and Loss   3,600 Furniture and fittings  5,120 Motor Vehicles    3,462 
Closing Stock    3,000 Debtors     11,474 Creditors    7354 Cash     1,518  46,044. 
17. What is the capital employed?
A. ₦44 600
B. ₦43 052
C. ₦38 600
D. ₦43 044
\n """,
"""Use the information below to answer questions 17 and 18.  ₦ Capital     24,000 
Land and building   18,470 Mortgage on premises 11,090 Drawings     3,000 Profit and Loss   3,600 
Furniture and fittings  5,120 Motor Vehicles    3,462 Closing Stock    3,000 
Debtors     11,474 Creditors    7354 Cash     1,518  46,044 .
18. Calculate the value of fixed assets.
A. ₦15 992
B. ₦18 470
C. ₦27 052
D. ₦27 000
\n """,
"""Use the information below to answer questions 19 and 20. Dept        Dept      Total S  T ₦   ₦   ₦  
Gross profit b/d 6,000      4,000         10,000  ==== ==== ==  ==    ====  == Less:  
Salaries and Wages 1,800  1,200         3,000 Electricity     ?  ?         2,000 
Depreciation 600  ?          1,000 Net Profit   ?  1,600         4,000 ,         ,           ,        
It is the tradition of the organization to apportion expenses in the proportion 60%: 40% for S and T respectively. 
19. What is the net profit made by department S?
A. ₦2,000
B. ₦3,000 
C. ₦3,600
D. ₦2,400
\n """,
"""Use the information below to answer questions 19 and 20. Dept        
Dept      Total S  T ₦   ₦   ₦  Gross profit b/d 6,000      4,000         10,000  ==== ==== ==  ==    ====  == Less:  
Salaries and Wages 1,800  1,200         3,000 Electricity     ?  ?         2,000 Depreciation 600  ?          1,000 Net 
Profit   ?  1,600         4,000 ,         ,           ,        
It is the tradition of the organization to apportion expenses in the proportion 60%: 40% for S and T respectively. 
20. The depreciation to be charged to department T is __.
A. ₦400
B. ₦300
C. ₦500
D. ₦600
\n """,
"""21. Given:  Jan.        Dec. 2003       2003 ₦    ₦  Provision for bad debts  1 000 Debtors       20 000 
Bad debt to be written off       2 000 The provision for bad debt stands at 10% of debtors. 
How much is to be charged to profit and loss account as provision for bad debt?
A. ₦800
B. ₦2 000 
C. ₦1 000
D. ₦1 800
\n """,
"""22. Goods withdrawn from for private use are credited to __.
A. Purchases
B. Drawing
C. Sales
D. Capital
\n """,
"""23. Stationery which will be used for a long period of time is usually recorded as an expense instead of an asset. 
This concept is called __.
A. Entity
B. Realisation
C. Accrual
D. Materiality
\n """,
"""24. Adaobi mistakenly entered ₦7,000 as credit in Abba’saccount instead of Baba’s account this is __.
A. An error of principles
B. An error of commission 
C. A compensating error
D. An error of omission
\n """,
"""25. The gross profit disclosed in the branch stock adjustment account represents __.
A. Branch profit
B. Estimated profit
C. Unrealized profit
D. Head office profit
\n """,
"""26. Partner’s share of profit is credited to __.
A. The profit and loss appropriation account
B. The profit and loss account
C. A partner’s current account
D. A partner’s capital account
\n """,
"""Use the information below to answer questions 27 and 28. 
Use the information below to answer questions 27 and 28. Stock of material 1/1      10 000 
Purchase of raw materials     160 000 Manufacturing wages      420 000 Royalties        3 000 
Stock of raw materials 31/12    14 000 ₦  
27. What is the cost of raw materials consumed?
A. ₦156 000
B. ₦173 000
C. ₦170 000
D. ₦160 000
\n """,
"""Use the information below to answer questions 27 and 28. 
Use the information below to answer questions 27 and 28. Stock of material 1/1      10 000 
Purchase of raw materials     160 000 Manufacturing wages      420 000 
Royalties        3 000 Stock of raw materials 31/12    14 000 ₦  
28. Calculate the prime cost.
A. ₦597 000
B. ₦567 000
C. ₦57 9000
D. ₦576 000
\n """,
"""Use the information below to answer questions 29 and 30. Jan. 1  
Received 1,000  ₦10 each units at Jan. 2  Received 2,000  ₦12 each  units at 
Jan. 3  Issued 1,500 units  Jan. 4  Received 1,000  ₦11 each units at  Jan. 5  Issued 1000 units  
29. Using FIFO method, what is the value of the closing stock? 
A. ₦17 000
B. ₦29 000
C. ₦34 000
D. ₦12 000
\n """,
"""Use the information below to answer questions 29 and 30. Jan. 1  
Received 1,000  ₦10 each units at Jan. 2  Received 2,000  ₦12 each  units at Jan. 3  Issued 1,500 units  
Jan. 4  Received 1,000  ₦11 each units at  Jan. 5  Issued 1000 units  
30. What is the value of closing stock using simple average?
A. ₦11 500
B. ₦17 000
C. ₦28 500
D. ₦17 500
\n """,
"""31. The gross loss on manufacturing is always transferred to the __.
A. credit side of the balance sheet
B. credit side of the profit and loss account
C. debit side of the balance sheet
D. debit side of the profit and loss account
\n """,
"""32. The depreciation on a motor vehicle that is being used 
for manufacturing and administration is charged to the __.
A. Debit side of the manufacturing and profit and loss account
B. Credit side of profit and loss account only
C. Debit side of manufacturing and balance sheet
D. Debit side of the profit and loss account only
\n """,
"""33. In bank reconciliation process, discrepancies caused by timing arises as a result of __.
A. bank statement only
B. cash book and bank statement
C. cash book, bank statements and incidental records
D. cash book only
\n """,
"""34. The process of reconciling cheque between banks termed cheque __.
A. truncation
B. clearing
C. holding
D. confirmation
\n """,
"""35.  Cash Book (Extract) ₦    ₦  Balance b/f     2,200 
Sundry Expenses  16,800  Receipt from Customers     1600 
Drawings    4,700  Suppliers    7,300 
Debtors opening and closing balances amount to ₦6 500 and ₦7,600 respectively. 
What is the sales value?
A. ₦17 500
B. ₦29 400
C. ₦31 600
D. ₦15 300
\n """,
"""36. Given:  ₦ Fixtures     30,000 Debtors     7,000 Stock     8,000 
Creditors    3,000 Goodwill    10,000 Determine the capital
A. ₦10,000
B. ₦42,000 
C. ₦52,000
D. ₦15,300
\n """,
"""Use the information below to answer questions 37 and 38. 
 ₦ Sales     232,000 Opening stock    28,000 Purchases    128,000 
Carriage inwards  4,000 Carriage outwards  6,000 Closing stock    10,000
 Discount received  18,000 Expenses     20,000 
37. Calculate the gross profit.
A. ₦100 000
B. ₦86 000
C. ₦76 000
D. ₦82 000
\n """,
"""Use the information below to answer questions 37 and 38.  
₦ Sales     232,000 Opening stock    28,000 Purchases    128,000 
Carriage inwards  4,000 Carriage outwards  6,000 
Closing stock    10,000 Discount received  18,000 Expenses     20,000 38. 
Calculate the expenses debited to the profit and loss account.
A. ₦17 000
B. ₦23 000 
C. ₦30 000
D. ₦26 000
\n """,
"""Use the information below to answer questions 39 and 40. 
Income and Expenditure (Extract)    ₦           ₦  Bal. b/d     390  
Expenses  on cleaning  300  Sales of tickets    4,000 New tool   50 Donations     3,000 
Repairs   400 Subscriptions   6,500 Electricity  350  
39. What is the total income for the period?
A. ₦13 500
B. ₦13 890
C. ₦9 500
D. ₦10 500
\n """,
"""Use the information below to answer questions 39 and 40. 
Income and Expenditure (Extract)    ₦           ₦  Bal. b/d     390  
Expenses  on cleaning  300  Sales of tickets    4,000 New tool   50 Donations     3,000 
Repairs   400 Subscriptions   6,500 Electricity  350  
40. What is the balance carried down?
A. ₦12 330
B. ₦13 430
C. ₦11 680
D. ₦11 930 
\n """,

    ]

    questions = [
        Question(question_prompts[0], "B"),
        Question(question_prompts[1], "A"),
        Question(question_prompts[2], "D"),
        Question(question_prompts[3], "C"),
        Question(question_prompts[4], "A"),
        Question(question_prompts[5], "B"),
        Question(question_prompts[6], "B"),
        Question(question_prompts[7], "D"),
        Question(question_prompts[8], "A"),
        Question(question_prompts[9], "C"),
        Question(question_prompts[10], "C"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "D"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "A"),
        Question(question_prompts[15], "C"),
        Question(question_prompts[16], "D"),
        Question(question_prompts[17], "C"),
        Question(question_prompts[18], "D"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "D"),
        Question(question_prompts[23], "B"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "C"),
        Question(question_prompts[26], "A"),
        Question(question_prompts[27], "C"),
        Question(question_prompts[28], "A"),
        Question(question_prompts[29], "C"),
        Question(question_prompts[30], "D"),
        Question(question_prompts[31], "D"),
        Question(question_prompts[32], "B"),
        Question(question_prompts[33], "B"),
        Question(question_prompts[34], "A"),
        Question(question_prompts[35], "C"),
        Question(question_prompts[36], "D"),
        Question(question_prompts[37], "D"),
        Question(question_prompts[38], "B"),
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
        FinancialAcc_2017()
def financial_accounting_2018():
    question_prompts=["""9. Calls in advance are treated in the balance sheet as __.
A. current asset
B. fixed asset
C. current liability
D. fixed liability
""","""10. Shares issued to a vendor in payment of business purchased would require a debit to __.
A. cash account and credit to share capital account
B. share capital account and credit to vendors 
C. share capital account and credit to cash account
D. vendor's account and credit to share capital account
""","""Use the information below to answer questions 11 and 12 Rakiya and Joy are in partnership and agreed that 5% interest per annum is to be charged on drawings. The drawing made by both partners in one year were: Rakiya, ₦200 on March 31st and ₦300 on September 30th. Joy, ₦100 on April 1 st and ₦240 on July 1st. 11. The interest Joy’s drawing is__.
A. ₦511.25 debit
B. ₦500.00 credit
C. ₦349.75 credit
D. ₦340.00 credit
""","""Use the information below to answer questions 11 and 12 Rakiya and Joy are in partnership and agreed that 5% interest per annum is to be charged on drawings. The drawing made by both partners in one year were: Rakiya, ₦200 on March 31st and ₦300 on September 30th. Joy, ₦100 on April 1 st and ₦240 on July 1st.  12. Assuming that Rakiya was not credited with any income during the period. What is her closing current account balance?
A. ₦340.00 credit
B. ₦500.00 credit
C. ₦340.75 debit
D. ₦511.25 debit
""","""13. To account for expenses paid by head office on behalf of the branch, the branch should__.
A. debit profit and loss account and credit head office account
B. debit head office account and credit cash
C. credit cash and debit profit and loss account
D. credit profit and loss account and debit head office account.
""","""14. The officer responsible for ascertaining whether all public expenditure and appropriation are in line with approved guidelines is the __.
A. Accountant general
B. Finance Minster 
C. Auditor General
D. Permanent Secretary
""","""Use the information below to answer questions 15 and 16.Adex Ltd. issues stock to its retail branches at cost price. The following particulars relate to Ede branch. Stock at branch 1st January at cost     400 Goods sent to branch at cost         8000 Returns to head office    340 Cash sales             9160 Stock at branch 31st December at cost    720  15. What is the gross profit carried to the profit and loss account?
A. ₦1870
B. ₦1530
C. ₦1640
D. ₦1820
""","""Use the information below to answer questions 15 and 16.Adex Ltd. issues stock to its retail branches at cost price. The following particulars relate to Ede branch. Stock at branch 1st January at cost     400 Goods sent to branch at cost         8000 Returns to head office    340 Cash sales             9160 Stock at branch 31st December at cost    720  16. Calculate the cost of goods credited to the head office trading account.
A. ₦7200
B. ₦7460
C. ₦7500
D. ₦7660
""","""17. Advertising expenses incurred on a product in a business organization should be charged to__.
A. sales department
B. production department
C. Purchases department 
D. administration department
""","""18. Four broad classifications of overheads are __.
A. production, selling, distribution and material
B. selling, distribution, production and wages production
C. selling, distribution and administration 
D. distribution, selling, administration and materials
""","""19. Transfers from the head office to branches are best carried out at __.
A. cost price
B. cost plus mark-up
C. selling price
D. market price
""","""20. On dissolution, the final distribution of cash to partners is based on __.
A. partnership agreement
B. capital, balances
C. goodwill
D. Articles of Association
""","""21. In reconciling the branch and head office accounts, remittance in transit in the branch books is treated as a __.
A. debit entry
B. contra entry
C. credit entry 
D. reversal entry
""","""22. Profit or loss in a partnership is usually arrived at after deducting from gross profit all expenses including __.
A. partners' salaries
B. interest on capital
C. interest on loans
D. partners’ drawings.
""","""23. Departmentalization of accounts is useful because it shows the __.
A. overall performance of a division
B. cost per unit of a profit
C. price per unit of a product
D. overall performance of a firm
""","""24. When goodwill is not retained in the business. the entries in the new partners' books will be to debit __.
A. good account and credit partners’ capital account 
B. cash account and credit partners’ capital account
C. goodwill account and credit cash account
D. partners' capital account and credit goodwill account.
""","""Use the information below to answer questions 25 and 26.₦ Balance as per cash book   13,560 Unpresented cheques      5 120 Uncredited lodgments      2 300 Dividend received not entered in the cash book      2 000 Bank charges     280 Standing order payments      600 Balance as per bank statement        ? 25. Calculate the balance in the bank statement.
A. ₦10740
B. ₦ 11 860
C. ₦16 380
D. ₦17500
""","""Use the information below to answer questions 25 and 26.₦ Balance as per cash book   13,560 Unpresented cheques      5 120 Uncredited lodgments      2 300 Dividend received not entered in the cash book      2 000 Bank charges     280 Standing order payments      600 Balance as per bank statement        ? 26. What is the adjusted cash book balance?
A. ₦15 560
B. ₦14 680
C. ₦16 440
D. ₦17 000.
""","""Use the information below to answer questions 27 and 28 Departmental Trading Account(Extract) Total () 1-otal A- Stock 3000 2000 1000 Sales 10000 G 000 4000 Purchases 4000 2500 1500 Closing stock 2000 1500 500 Goods worth ₦300 was transferred from department Q to P. Similarly. P's total expenses for the period was ₦200.27. What was department Q's gross profit?
A. ₦2 500
B. ₦2 200
C. ₦2 300 
D. ₦1700
""","""Use the information below to answer questions 27 and 28 Departmental Trading Account(Extract) Total () 1-otal A- Stock 3000 2000 1000 Sales 10000 G 000 4000 Purchases 4000 2500 1500 Closing stock 2000 1500 500 Goods worth ₦300 was transferred from department Q to P. Similarly. P's total expenses for the period was ₦200. 28. Department P’'s net profit was
A. ₦2 500
B. ₦2 800
C. ₦3 000
D. ₦5 200
""","""29. Which of the following is a common cause of a discrepancy between head office and branch trial balance?
A. Stock and prepayment
B. Creditors and cash in transit
C. Stock and cash in transit
D. Debtors and cash in transit.
""","""30. Sule and Ahmed are in partnership sharing profits and losses equally. If Khadija is admitted as a new partner to take 1⁄5 ℎ as her share. What is the new profit or loss sharing?
A. Sule 1⁄3, Ahmed 1⁄3 and Khadija 11⁄3 
B. Sule2⁄5, Ahmed 2⁄5 and Khadija 1⁄5
C. Sule 1/5, Ahmed 1/5 and Khadija 3⁄5
D. Sule 2⁄5, Ahmed 1⁄5 and Khadija 2⁄5
""","""31. The prime cost is the total of the
A. production cost + selling expenses
B. administrative expenses + selling + distribution expenses
C. direct materials + work overhead expenses
D. direct material + direct labour + direct
""","""32. In the not-for-profit-making organization, the excess of income over expenditure is__.
A. deducted from the capital
B. added to the capital
C. added to the accumulated fund
D. deducted from the accumulated fund
""","""Use the information to answer questions 33 and 34.Trading account for the year ended 31st December 2009 ₦      ₦  Opening stock     32,000   Sales   48,000 Purchases        40000     Less  returns     2,000 Carriage Inwards       1 000      41 000  Less returns       2 000 39,000 Cost of goods available for sale  ?? Less closing stock  9000 Cost of goods sold  ??  33. Find the average stock for the period.
A. ₦20 500
B. ₦23 000
C. ₦28 000
D. ₦27 000
""","""Use the information to answer questions 33 and 34.Trading account for the year ended 31st December 2009 ₦      ₦  Opening stock     32,000   Sales   48,000 Purchases        40000     Less  returns     2,000 Carriage Inwards       1 000      41 000  Less returns       2 000 39,000 Cost of goods available for sale  ?? Less closing stock  9000 Cost of goods sold  ??   34. Calculate the cost of goods sold.
A. ₦61 000
B. ₦62 000
C. ₦58 000
D. ₦57 000
""","""35. In the head office ledger, the value of goods sent to the branch are__.
A. debited to the branch current account
B. debited to the head office current account
C. credited to the head office current account
D. credited to the branch current account 
""","""36. Which of the following methods of invoicing goods to branches facilitate easy checks on the activities of branches?
A. selling price
B. fixed percentage on cost
C. cost price 
D. invoice price
""","""37. The amount paid by the new partner on admission as a compensation for the reputation built up by old pant is a __.
A. bonus.
B. goodwill
C. premium
D. commission.
""","""38. A partnership's internal regulations are set out by __.
A. a constitution
B. a law
C. a deed.
D. D. an article
""","""39. In the absence of a partnership deed, the act stipulates that __.
A. an amount should be fixed as salary for partners
B. profits and losses should not be shared equally 
C. interest on partners loan should be 25%.
D. interest should not be allowed on partners drawing 
""","""40. The profit of a branch is usually credited to the __.
A. branch office goods account
B. head office sales
C. adjustment account.
D. head office current account."""]
    question = [
        Question(question_prompts[0], 'c'),
        Question(question_prompts[1], 'd'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'a'),
        Question(question_prompts[5], 'c'),
        Question(question_prompts[6], 'd'),
        Question(question_prompts[7], 'd'),
        Question(question_prompts[8], 'a'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'b'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'b'),
        Question(question_prompts[13], 'c'),
        Question(question_prompts[14], 'a'),
        Question(question_prompts[15], 'd'),
        Question(question_prompts[16], 'd'),
        Question(question_prompts[17], 'b'),
        Question(question_prompts[18], 'c'),
        Question(question_prompts[19], 'a'),
        Question(question_prompts[20], 'd'),
        Question(question_prompts[21], 'b'),
        Question(question_prompts[22], 'd'),
        Question(question_prompts[23], 'c'),
        Question(question_prompts[24], 'b'),
        Question(question_prompts[25], 'a'),
        Question(question_prompts[26], 'b'),
        Question(question_prompts[27], 'b'),
        Question(question_prompts[28], 'b'),
        Question(question_prompts[29], 'c'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'a'),
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
def FinancialAcc_2020():
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
        """1.Ada and Udo are lawyers who went into partnership as Ado and Co. Ada brought cash of ₦12 000, furnishings worth 
₦18,000 and a motor vehicle worth ₦70,000. Udo on the other hand brought in cash N10 000, his building valued at ₦105 000 
and a personal computer worth ₦35 000. What is the capital of Ado & Co.? 
A. ₦100 000 
B. ₦22 000 
C. ₦250 000 
D. ₦150 000. 
\n """,
"""2.Ada and Udo are lawyers who went into partnership as Ado and Co. Ada brought cash of ₦12 000, furnishings worth 
₦18,000 and a motor vehicle worth ₦70,000. Udo on the other hand brought in cash N10 000, his building valued at 
₦105 000 and a personal computer worth ₦35 000. What is the profit-sharing ratio 
if it is based on capital contributed by Ada and Udo?  
A.3:2 
B.2:3 
C. 1:2  
D. 2:1. 
\n """,
"""3. One major advantage of a ledger is that it __.  
A. is a book of original entry 
B. is only accessible to shareholders during liquidation 
C. can be used by any type of business 
D. removes the need for preparing a balance sheet after each transaction 
\n """,
"""4. A trial balance is usually prepared by an accountant from account balances in the ledger for the purpose of __.  
A. classifying accounts in the ledger 
B. identifying the balance sheet items 
C. providing a basis for establishing the accountant's competence 
D. testing arithmetical accuracies of the ledger account balances. 
\n """,
"""5. The total of the creditors at the beginning of the year was ₦4 600 and at the end of the year 
₦5 250. During the year, ₦26 500 was paid to suppliers and ₦130 
was received in discounts from these suppliers. The purchases for the year would be __?  
A. ₦27 038 
B. ₦26 630 
C. ₦27 280 
D. ₦27 150 
\n """,
"""6. Given:₦ Capital at the beginning  20 000 Drawings 3 000 Capital at end 30 000 
New capital introduced 8,000 What is the profit for the period?  
A. ₦8 000 
B. ₦4 000 
C. ₦5 000 
D. ₦6 000. 
\n """,
"""7 The purchase of two generators by Hassan Electronics Enterprises should be recorded as  
A. a part of capital in the capital account 
B. an acquisition of stock 
C. an expense in its general office expense account 
D. an acquisition of fixed assets 
\n """,
"""8. Dele and Seun who are in partnership have decided to convert their business into a limited liability company 
where both become directors. To convert the __. 
A. they will simply continue since there are no new members. 
B. the partnership is formally ended and new company books opened 
C. computation of goodwill must be done as it is legally required 
D. the shares and all other items will be shared equally and not in their former ratios. 
\n """,
"""9 The most convenient cash book used by a petty trader operating in an area where there is no banking facility is __.  
A. four column 
B. single column 
C. two column 
D. three column. 
\n """,
"""10 A general journal contains __.  
A. date, narration, folio, debit and credit 
B. folio, credit. date, debit and sales 
C. date, narration, folio. debit and purchases 
D. folio, credit. narration. date and discount. 
\n """,
"""11 The value of capital invested by the owners is __. 
A. ₦101,000 
B. ₦103,000 
C. ₦100,000 
D. ₦110.000 
\n """,
"""12 The liabilities of Udo Co. Ltd is  
A. ₦177,000 
B. ₦180,000 
C. ₦110,000 
D. ₦181,000 
\n """,
"""13 Zakari started a business in January 2000. He bought a shop costing ₦54,000 and stock worth ₦7,600. 
Profit for the year amounted to ₦22,100. His closing 
capital was 73,800.Zakari's personal drawings amounted to  
A. ₦9,900 
B. ₦2,300 
C. ₦19,500 
D. ₦17,100 
\n """,
"""14 The balance on the provision for depreciation account is __.  
A. deducted from fixed assets on the balance sheet 
B. added to fixed assets on the balance sheet 
C. added to the current liabilities of the account 
D. deducted from the profit and loss account 
\n """,
"""15 What are the appropriate recording procedures for entries in the trial balance?  
A. Ledgers. source documents and trial balance 
B. Ledgers, trial balance and source documents 
C. Source documents, ledgers and trial balance 
D. Cash account, ledgers and trial balance. 
\n """,
"""16 Mr Bassev purchased a motor vehicle for use in his business and debited 
the purchases account with the same value. This is an error of __.  
A. principle 
B. omission 
C. original entry 
D. commission 
\n """,
"""17 Accrual accounting differs from cash accounting because it recognizes __.  
A. cash and creditors. 
B. cash and debtors 
C. debtors and creditors 
D. prepayment and cash 
\n """,
"""18 A private company is different from a public company because __.  
A. it cannot invite members of the public to subscribe for its shares 
B. it does not restrict the right to transfer its shares 
C. it can only offer its shares to members of the public for subscription 
D. its shares are owned by one person. 
\n """,
"""19 The receipts and payments of account of a not-for-profit-making organization plays 
a similar role in profit-making organization as __.  
A. a cash account 
B. an expenses account 
C. a balance sheet 
D. an income account 
\n """,
"""20 Osei, and Yabo were in partnership sharing profits and losses in the ratio of 3:2. 
On admitting Takwa, the profit and loss sharing ratio was changed to 1:1:1, 
supposed Takwa paid -₦30 000 for goodwill, this amount would be  
A. debited to goodwill account 
B. credited to Takwa's current account 
C. credited to the old partners' capital account 
D. shared to all the partners’ capital account. 
\n """,
"""21 Commission-on-turnover is charged on  
A. savings accounts 
B. current accounts only 
C. all bank accounts 
D. fixed deposit accounts only 
\n """,
"""22 The medium that enables the ATM to read the account details and 
process transactions directly with the account held in the bank is the __.  
A. smart card 
B. computerized account 
C. magnetic strip 
D. communication network 
\n """,
"""23 A major cause of discrepancy between bank statement and the cash book 
that overstates the bank statement balance is the __.  
A. direct payment 
B. commission paid 
C. direct withdrawal 
D. interest received 
\n """,
"""24 The bank charges levied on a current account holder is the charges on __.  
A. transactions 
B. cash received 
C. turnover 
D. transfer 
\n """,
"""25 Given Light expenses 400 Purchases 3,000 Sales 1,200 Creditors 2,250 Debtors  50 
Calculate the total of the trial balance.  
A. ₦3,450 
B. ₦4,300 
C. ₦3,500 
D. ₦4,250 
\n """,
"""26 The major feature of a journal is that it has __.  
A. six columns. date, particulars, folio, amount, debit and credit 
B. four columns, date, particulars, folio and amount 
C. three columns, date, particular and folio 
D. six columns, date, particulars, folio, debit and credit. 
\n """,
"""27 Which of the following items is a capital expenditure?  
A. Maintenance of office machine. 
B. Purchase of office machinery 
C. Purchase of office stationery. 
D. Carriage inwards. 
\n """,
"""28 The corresponding entry of personal accounts found in the debit side of the cash book is to __. 
A. credit the ledger. 
B. credit real accounts. 
C. debit real accounts. 
D. debit the ledger. 
\n """,
"""29 The major focus of the trading 
account is to show __.
A. net profit. 
B. total purchases. 
C. gross margin. 
D. total sales. 
\n """,

    ]

    questions = [
        Question(question_prompts[0], "A"),
        Question(question_prompts[1], "B"),
        Question(question_prompts[2], "C"),
        Question(question_prompts[3], "D"),
        Question(question_prompts[4], "B"),
        Question(question_prompts[5], "C"),
        Question(question_prompts[6], "D"),
        Question(question_prompts[7], "B"),
        Question(question_prompts[8], "B"),
        Question(question_prompts[9], "A"),
        Question(question_prompts[10], "A"),
        Question(question_prompts[11], "B"),
        Question(question_prompts[12], "B"),
        Question(question_prompts[13], "A"),
        Question(question_prompts[14], "C"),
        Question(question_prompts[15], "A"),
        Question(question_prompts[16], "C"),
        Question(question_prompts[17], "A"),
        Question(question_prompts[18], "C"),
        Question(question_prompts[19], "A"),
        Question(question_prompts[20], "B"),
        Question(question_prompts[21], "A"),
        Question(question_prompts[22], "A"),
        Question(question_prompts[23], "C"),
        Question(question_prompts[24], "A"),
        Question(question_prompts[25], "D"),
        Question(question_prompts[26], "B"),
        Question(question_prompts[27], "A"),
        Question(question_prompts[28], "C"),

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
        FinancialAcc_2020()
def FinancialAcc_2015():
    question_prompts=[
        """1. The Term “accounting period” is used to refer to the __.  
A. period within which debtors are expected to settle accounts 
B. time span, usually one year, covered by financial statement 
C. time span during which taxes are paid to the Inland Revenue Board 
D. budget period, usually one year, relied on by the accountant. 
\n """,
"""2. Assigning revenues to the accounting period in which goods were sold 
or services rendered and expenses incurred is known as ___. 
A. matching concept 
B. consistency convention 
C. adjusting for revenue 
D. passing of entries 
\n """,
"""3. An effective accounting system should provide information __.    
A. for customer feedback and requirement 
B. on new products and methods 
C. for promoters, directors, labour unions and distributors 
D. on internal and external reporting for managers and third party 
\n """,
"""4. Which of the following accounting records are source documents?  
A. Sales invoice and cash book 
B. Sales invoice and debit note 
C. journals and ledger 
D. cash book and debit note 
\n """,
"""5. The instruments that are generated when firms enter into business transactions with others are called __.  
A. invoices 
B. source documents 
C. purchases documents 
D. journals 
\n """,
"""6. The document that is used to acknowledge the acceptance of the return ofgoods by the seller from the buyer is known as __.  
A. invoice 
B. debit note 
C. credit note 
D. voucher 
\n """,
"""7. The act establishing the Institute of Chartered Accountants of Nigeria (ICAN) came into force on  
A. 1st September, 1963 
B. 1st October, 1960 
C. 1st September, 1960 
D. 1st October, 1963 
\n """,
"""8. An advantage of the use of the voucher system is that it __.  
A. reduces the number of cheques that will ne written during any given period 
B. provides a highly flexible system for handling unusual transactions 
C. ensures that every expenditure is reviewed and verified before payment is made 
D. provides a comprehensive record of business done with particular suppliers 
\n """,
"""9.Sales 20,000 Cost of sales 10,000 Operating expenses 2,500 
Expenses prepaid included in operating expense 500   Calculate the net profit  
A. ₦7,500 
B. ₦12,500 
C. ₦10,000 
D. ₦8,000 
\n """,
"""10. What is the gross profit margin?  
A. 50% 
B. 50% 
C. 30% 
D. 100% 
\n """,
"""11 The main objective of accounting report is to provide information about __.  
A. a company's shareholders 
B. the efficacy of assets 
C. a company's economic resources 
D. an entity’s management 
\n """,
"""12 If liabilities amounted to ₦12,045, other assets ₦360,800 and
 equity ₦26,896, the cash at hand would be __. 
A. ₦2,241 
B. ₦2,214 
C. ₦2,114 
D. ₦2,141 
\n """,
"""13 In preparing the final accounts, the Bad debt account is closed by a transfer to the __.  
A. balance sheet 
B. profit and loss account 
C. trading, account 
D. provision for bad debts account 
\n """,
"""14. Which of the following is used to update the cashbook bank reconciliation?  
A. Interest received and unpresented cheques 
B. Commission and debit note 
C. Interest received and direct credit 
D. Unpresented cheques and direct credit 
\n """,
"""15. The two legally recognized professional accounting bodies in Nigeria are the __.  
A. Nigerian Accounting Association and the Executive Cost and Management Accountants of Nigeria 
B. Institute of Certified Public Accountants of Nigeria and the Institute of Cost and Management Accountants of Nigeria 
C. Association of Accountants of Nigeria and the Institute of Management Accountants of Nigeria 
D. Institute of Chartered Accountants of Nigeria and the Association of National  Accountants of Nigeria 
\n """,
"""16. A source document is used for verifying, the __.  
A. amount due from debtors 
B. selling, price of goods 
C. actual cost of an asset 
D. amount due to creditors 
\n """,
"""17. The rule of accounting  equation requires that account  payable should be placed under __.  
A. capital 
B. assets 
C. liabilities 
D. equities 
\n """,
"""18. The double entry principle of accounting was developed by __. 
A. William Pickles 
B. Akintola Williams 
C. Luca Pacioli 
D. Frank Wood. 
\n """,
"""19. The concept that has much influence over asset valuation and income determination is__. 
A. entity 
B. realization 
C. matching 
D. conservatism 
\n """,
"""20. In the trading profit and loss account of a manufacturing organization, purchases is __.  
A. always the same amount as the total factory overhead cost 
B. equivalent to the total cost of goods manufactured 
C. always the same as the price cost  
D. given separately 
\n """,
"""21. Goods worth ₦50 000 were sent at different times from head office to the branch during the year. By the end of the period, only ₦40 000 worth of goods had arrived at the branch. Which of the following is correct about the treatment of this transaction?  
A. Branch should debit goods received from head office with ₦50,000. 
B. Head office should debit goods sent to branch account with ₦10,000. 
C. Head office should debit goods sent to branch account with ₦50,000. 
D. Branch should debit goods received from head office with ₦10,000. 
\n """,
"""22. Bariga, a stock broker bought stationery for ₦12 000 by cash. To record this transaction, debit  
A. cash and credit stationery 
B. stationery and credit cash 
C. stationery and credit purchases 
D. purchases and credit stationery 
\n """,
"""23. Cash discount is often recorded on __.  
A. the debit side of the cash book 
B. the credit side of the cash book 
C. both credit and debit side of the cashbook 
D. the folio column of the cash book 
\n """,
"""24. The standing order is a payment instruction given by a __.  
A. customer to a fellow customer 
B. bank to an employee 
C. hank to the customers 
D. customer to the bank 
\n """,
"""25. The major function of accounting bodies in Nigeria is to __.  
A. promote the ethics of the profession 
B. show the dynamic nature of the profession 
C. provide good remuneration to the members 
D. provide proper financial management of businesses 
\n """,
"""26. Ledger account is mainly classified into __.  
A. fixed and current accounts 
B. nominal. real and personal accounts 
C. bank and cash accounts 
D. management. financial and public sector accounting 
\n """,
"""27. The historical development of accounting reveals that it__.  
A. is an ideal subject for financial development 
B. is a product of its own environment. 
C. deals with debit and credit of items 
D. is a product of financial development 
\n """,
"""28. In a trial balance. income and liabilities are __.  
A. credited 
B. credited and debited respectively 
C. debited 
D. debited and credited respectively 
\n """,
"""29. Ibrahim, a micro business operator, sold 10 bags of sugar to Jide at total cost of ₦12 000.
 The record in Jide’s book would be to debit __.  
A. purchases ₦12 000 and credit sugar account ₦12 000 
B. purchases ₦12,000 and credit Ibrahim ₦12,000 
C. Ibrahim ₦12,000 and sugar account ₦12,000 
D. Jide ₦12,000 and credit purchases ₦12,000 
\n """,
"""30. Accounting information seeks to provide__.  
A. analysis of accounts to trade debtors 
B. permanent records for all transactions. 
C. audited reports on the accounts of a company. 
D. data about the employees of a company.  
\n """,
"""31. When the debit side total of an account exceeds the credit side 
total while balancing an account, it means that the account has __.  
A. debit balance 
B. credit balance 
C. been understated 
D. been overdrawn 
\n """,
"""32. One of the differences between bookkeeping and accounting is that the former __. 
A. records data while the latter interprets it. 
B. is regarded as the language of the business while the latter ascertains its strength 
C. interprets data while the latter records it 
D. summarizes information while the latter communicates it. 
\n """,
"""33. The concept which states that  revenue should recognized at the  
point when the sale is deemed to  have been made is __. 
A. matching 
B. consistency 
C. going concern 
D. realization 
\n """,]
    question = [
        Question(question_prompts[0], 'b'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'd'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'b'),
        Question(question_prompts[5], 'c'),
        Question(question_prompts[6], 'a'),
        Question(question_prompts[7], 'c'),
        Question(question_prompts[8], 'd'),
        Question(question_prompts[9], 'a'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'd'),
        Question(question_prompts[12], 'b'),
        Question(question_prompts[13], 'c'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'c'),
        Question(question_prompts[17], 'c'),
        Question(question_prompts[18], 'c'),
        Question(question_prompts[19], 'd'),
        Question(question_prompts[20], 'c'),
        Question(question_prompts[21], 'b'),
        Question(question_prompts[22], 'c'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'a'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'c'),
        Question(question_prompts[27], 'a'),
        Question(question_prompts[28], 'b'),
        Question(question_prompts[29], 'b'),
        Question(question_prompts[30], 'a'),
        Question(question_prompts[31], 'c'),
        Question(question_prompts[32], 'd'),
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
def FinancialAcc_2014():
    question_prompts=[
        """1. One of the differences betweenbookkeeping and accounting is that the former __.  
A. records data while the latter interprets 
B. is regarded as the language of the business while the latter ascertains its strength 
C. interprets data while the latter records it  
D. summarises information while the latter communicates it 
\n """,
"""2. The concept which states that revenue should be recognized at the point when the sale is deemed to have been made is  
A. matching 
B. consistency 
C. realization 
D. going concern 
\n """,
"""3. A cheque of ₦5,000 paid to Sulieman had been correctly entered in the cash book but had not been entered in
 Sulieman's account. To correct this error, debit Sulieman's account and credit  
A. cash account 
B. bank account 
C. suspense account 
D. purchases account 
\n """,
"""4. Aduke Motors bought three Toyota Hilux vans on cash at the cost of₦6,000,000, on debiting the vehicle account, 
the corresponding credit for the purchase will appear in the __.  
A. sales day book 
B. purchases day book 
C. sales subsidiary book 
D. cash book 
\n """,
"""5. Which of the following affects the accuracy and authenticity of the trial balance?  
A. Error of omission 
B. Error of commission 
C. Error of transposition 
D. Error of original entry 
\n """,
"""6. A ledger is classified into  
A. private, sales and purchases 
B. personal, general and private 
C. general, private and sales 
D. sales, purchases and general 
\n """,
"""7. The book of account in which information from the source documents are recorded consists of __.  
A. debit and credit notes 
B. ledger and subsidiary books 
C. prepayments and accruals 
D. profit and loss and balance sheet 
\n """,
"""8. The accounting entries torecord a cheque issued by a business is to  
A. debit cash book and credit drawer 
B. credit cash book and debit drawer 
C. debit cash book and credit suspense account 
D. credit cash book and debit suspense account 
\n """,
"""9. The major advantage of an imprest system is that it __.  
A. ensures a proper accountability for every expenditure 
B. trains the young accountants in preparation for greater responsibilities 
C. relieves the chief cashier of the numerous petty cash payments 
D. serves as an analysis column for every expense 
\n """,
"""10. Petty cash book records transactions on  
A. the debit side only 
B. the credit side only 
C. both credit and debit sides 
D. reversed entry 
\n """,
"""11. A major way by which the headquarters guard against fraud in branches on 
cash remittance is through the introduction of  
A. imprest system only 
B. direct purchase by branch 
C. separate accountant for the branch 
D. credit sales by only the headquarters 
\n """,
"""12. I. Cash sales II. Cash purchases III. Cash discount allowed IV. Cash payment
 V. Cash receipts Which of the following are recorded on the debit side of the cashbook?  
A. I and II 
B. I and III 
C. I and V 
D. I and IV 
\n """,
"""13. An item credited in the bank statement but yet to be recorded in the firm's cash book is  
A. bank loan 
B. contract payment 
C. standing order 
D. direct deposit 
\n """,
"""14. The major focus of the trading account is to show  
A. net profit 
B. gross margin 
C. total purchases 
D. total sales 
\n """,
"""15. If goods were bought from Tanko at a cost price of ₦9,000 with a cash discount of 5%, 
how much will be paid assuming prompt payment was made?  
A. ₦4,500 
B. ₦8,550 
C. ₦9,000 
D. ₦9,450 
\n """,
"""16. If machine X cost ₦600,000 with anticipated life span of five years and estimated scrap 
value of ₦50,000, using straight line method; depreciation charged for two years will be  
A. ₦700,000 
B. ₦240,000 
C. ₦220,000 
D. ₦202,000 
\n """,
"""17. The excess of sales over cost of goods sold is 
A. gross sales 
B. gross profit 
C. net profit 
D. net sales 
\n """,
"""18. The control account is used in facilitating  
A. the location of errors in the various accounts 
B. up to date bank transactions 
C. the payment of debts and liabilities of the firm 
D. assets distribution with respect to income 
\n """,
"""19. A book of account that possesses the features of both daybook and ledger is  
A. sales day book 
B. cash book 
C. purchases day book 
D. returns day book 
\n """,
"""20. The value of the sales ledger control account is derived from the summation of  
A. the total debtors' account 
B. the total creditors' account 
C. all day books 
D. both the debtors’ and creditors' accounts 
\n """,
"""21. Subscription in arrears is treated in the balance sheet of a club as  
A. current asset 
B. current liability 
C. fixed asset 
D. intangible asset 
\n """,
"""22. In a departmental account, where no basis of apportionment exist, apportionment is  
A. on profit basis 
B. according to employee decision 
C. according to material available 
D. on equal basis 
\n """,
"""23. In a departmental account, the expenses to be apportioned on the basis of turnover is  
A. carriage inwards 
B. returns outwards 
C. discount received 
D. carriage outwards 
\n """,
"""24. If goods are sent to branch at 25% on cost, what will be the cost of 
goods sent to the branch at a selling price of ₦100,000?  
A. ₦130,000 
B. ₦125,000 
C. ₦80,000 
D. ₦75,000 
\n """,
"""25.Hussaina Enterprises sent goods worth ₦800,000 at cost plus mark-up of 20%to its branch  
What is the cost price of the goods sent to the branch?  
A. ₦600,000 
B. ₦620,000 
C. ₦640,000 
D. ₦700,000 
\n """,
"""26.Hussaina Enterprises sent goods worth ₦800,000 at cost plus mark-up of 20% to its branch 
Determine the profit on the goods sent to the branch at profit margin of 25% mark-up. 
A. ₦150,000 
B. ₦160,000 
C. ₦170,000 
D. ₦180,000 
\n """,
"""27. In the absence of a partnership deed, the act stipulates that __.  
A. an amount should be fixed as salary for partners 
B. interest on partners loan should be 25% 
C. interest should not be allowed on partners drawings 
D. profits and losses should not be shared equally 
\n """,
"""28. The profit of a branch is usually credited to the __ .  
A. adjustment account 
B. head office sales 
C. head office goods account 
D. head office current account 
\n """,
"""29. Where partnership is converted into a limited liability company, 
current account balances of partners are transferred to a  
A. realization account 
B. savings account 
C. share capital account 
D. capital account 
\n """,
"""30. The expenses incurred in purchasing a vehicle is a 
A. revenue expenditure 
B. capital expenditure 
C. recurrent expenditure 
D. concurrent expenditure 
\n """,
"""31. Payment for shares in excess of amount offered gives rise to  
A. subscription in advance 
B. revenue reserves 
C. capital reserves 
D. calls-in-advance 
\n """,
"""32. The details of the share capital which a company is authorized to issue is contained in the  
A. Articles of Association 
B. Companies and Allied Matters Act 
C. Memorandum of Association 
D. Share capital certificate 
\n """,
"""33. ₦800,000 worth of ordinary shares of 50k were issued at ₦1 each, payable in full on application. 
The entry in the cash book would be to  
A. credit ₦1,600,000 
B. debit ₦1,600,000 
C. credit ₦1,600,000 
D. debit ₦800,000 
\n """,
"""34. The account of government into which all monies are received and from which all expenditures are disbursed is the __  
A. Federation account 
B. Petroleum Technology Development Fund 
C. Central Bank Account 
D. Development fund 
\n """,
"""35. In government accounting, the method used which records on the basis of financial entity with self-balancing books 
instead of entity of proprietorship is 
A. virement 
B. fund accounting 
C. consolidated fund 
D. financial regulation 
\n """, ]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'c'),
        Question(question_prompts[2], 'b'),
        Question(question_prompts[3], 'd'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'b'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'b'),
        Question(question_prompts[8], 'c'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'd'),
        Question(question_prompts[11], 'c'),
        Question(question_prompts[12], 'd'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'b'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'b'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'a'),
        Question(question_prompts[20], 'b'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'd'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'b'),
        Question(question_prompts[25], 'd'),
        Question(question_prompts[26], 'd'),
        Question(question_prompts[27], 'c'),
        Question(question_prompts[28], 'a'),
        Question(question_prompts[29], 'b'),
        Question(question_prompts[30], 'c'),
        Question(question_prompts[31], 'c'),
        Question(question_prompts[32], 'd'),
        Question(question_prompts[33], 'a'),
        Question(question_prompts[34], 'd'),
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
def FinancialAcc_2012():
    question_prompts=[
        """1. One of the differences betweenbookkeeping and accounting is that the former __.  
A. records data while the latter interprets 
B. is regarded as the language of the business while the latter ascertains its strength 
C. interprets data while the latter records it  
D. summarises information while the latter communicates it 
\n """,
"""2. The concept which states that revenue should be recognized at the point when the sale is deemed to have been made is  
A. matching 
B. consistency 
C. realization 
D. going concern 
\n """,
"""3. A cheque of ₦5,000 paid to Sulieman had been correctly entered in the cash book but had not been entered in
 Sulieman's account. To correct this error, debit Sulieman's account and credit  
A. cash account 
B. bank account 
C. suspense account 
D. purchases account 
\n """,
"""4. Aduke Motors bought three Toyota Hilux vans on cash at the cost of₦6,000,000, on debiting the vehicle account, 
the corresponding credit for the purchase will appear in the __.  
A. sales day book 
B. purchases day book 
C. sales subsidiary book 
D. cash book 
\n """,
"""5. Which of the following affects the accuracy and authenticity of the trial balance?  
A. Error of omission 
B. Error of commission 
C. Error of transposition 
D. Error of original entry 
\n """,
"""6. A ledger is classified into  
A. private, sales and purchases 
B. personal, general and private 
C. general, private and sales 
D. sales, purchases and general 
\n """,
"""7. The book of account in which information from the source documents are recorded consists of __.  
A. debit and credit notes 
B. ledger and subsidiary books 
C. prepayments and accruals 
D. profit and loss and balance sheet 
\n """,
"""8. The accounting entries torecord a cheque issued by a business is to  
A. debit cash book and credit drawer 
B. credit cash book and debit drawer 
C. debit cash book and credit suspense account 
D. credit cash book and debit suspense account 
\n """,
"""9. The major advantage of an imprest system is that it __.  
A. ensures a proper accountability for every expenditure 
B. trains the young accountants in preparation for greater responsibilities 
C. relieves the chief cashier of the numerous petty cash payments 
D. serves as an analysis column for every expense 
\n """,
"""10. Petty cash book records transactions on  
A. the debit side only 
B. the credit side only 
C. both credit and debit sides 
D. reversed entry 
\n """,
"""11. A major way by which the headquarters guard against fraud in branches on 
cash remittance is through the introduction of  
A. imprest system only 
B. direct purchase by branch 
C. separate accountant for the branch 
D. credit sales by only the headquarters 
\n """,
"""12. I. Cash sales II. Cash purchases III. Cash discount allowed IV. Cash payment
 V. Cash receipts Which of the following are recorded on the debit side of the cashbook?  
A. I and II 
B. I and III 
C. I and V 
D. I and IV 
\n """,
"""13. An item credited in the bank statement but yet to be recorded in the firm's cash book is  
A. bank loan 
B. contract payment 
C. standing order 
D. direct deposit 
\n """,
"""14. The major focus of the trading account is to show  
A. net profit 
B. gross margin 
C. total purchases 
D. total sales 
\n """,
"""15. If goods were bought from Tanko at a cost price of ₦9,000 with a cash discount of 5%, 
how much will be paid assuming prompt payment was made?  
A. ₦4,500 
B. ₦8,550 
C. ₦9,000 
D. ₦9,450 
\n """,
"""16. If machine X cost ₦600,000 with anticipated life span of five years and estimated scrap 
value of ₦50,000, using straight line method; depreciation charged for two years will be  
A. ₦700,000 
B. ₦240,000 
C. ₦220,000 
D. ₦202,000 
\n """,
"""17. The excess of sales over cost of goods sold is 
A. gross sales 
B. gross profit 
C. net profit 
D. net sales 
\n """,
"""18. The control account is used in facilitating  
A. the location of errors in the various accounts 
B. up to date bank transactions 
C. the payment of debts and liabilities of the firm 
D. assets distribution with respect to income 
\n """,
"""19. A book of account that possesses the features of both daybook and ledger is  
A. sales day book 
B. cash book 
C. purchases day book 
D. returns day book 
\n """,
"""20. The value of the sales ledger control account is derived from the summation of  
A. the total debtors' account 
B. the total creditors' account 
C. all day books 
D. both the debtors’ and creditors' accounts 
\n """,
"""21. Subscription in arrears is treated in the balance sheet of a club as  
A. current asset 
B. current liability 
C. fixed asset 
D. intangible asset 
\n """,
"""22. In a departmental account, where no basis of apportionment exist, apportionment is  
A. on profit basis 
B. according to employee decision 
C. according to material available 
D. on equal basis 
\n """,
"""23. In a departmental account, the expenses to be apportioned on the basis of turnover is  
A. carriage inwards 
B. returns outwards 
C. discount received 
D. carriage outwards 
\n """,
"""24. If goods are sent to branch at 25% on cost, what will be the cost of 
goods sent to the branch at a selling price of ₦100,000?  
A. ₦130,000 
B. ₦125,000 
C. ₦80,000 
D. ₦75,000 
\n """,
"""25.Hussaina Enterprises sent goods worth ₦800,000 at cost plus mark-up of 20%to its branch  
What is the cost price of the goods sent to the branch?  
A. ₦600,000 
B. ₦620,000 
C. ₦640,000 
D. ₦700,000 
\n """,
"""26.Hussaina Enterprises sent goods worth ₦800,000 at cost plus mark-up of 20% to its branch 
Determine the profit on the goods sent to the branch at profit margin of 25% mark-up. 
A. ₦150,000 
B. ₦160,000 
C. ₦170,000 
D. ₦180,000 
\n """,
"""27. In the absence of a partnership deed, the act stipulates that __.  
A. an amount should be fixed as salary for partners 
B. interest on partners loan should be 25% 
C. interest should not be allowed on partners drawings 
D. profits and losses should not be shared equally 
\n """,
"""28. The profit of a branch is usually credited to the __ .  
A. adjustment account 
B. head office sales 
C. head office goods account 
D. head office current account 
\n """,
"""29. Where partnership is converted into a limited liability company, 
current account balances of partners are transferred to a  
A. realization account 
B. savings account 
C. share capital account 
D. capital account 
\n """,
"""30. The expenses incurred in purchasing a vehicle is a 
A. revenue expenditure 
B. capital expenditure 
C. recurrent expenditure 
D. concurrent expenditure 
\n """,
"""31. Payment for shares in excess of amount offered gives rise to  
A. subscription in advance 
B. revenue reserves 
C. capital reserves 
D. calls-in-advance 
\n """,
"""32. The details of the share capital which a company is authorized to issue is contained in the  
A. Articles of Association 
B. Companies and Allied Matters Act 
C. Memorandum of Association 
D. Share capital certificate 
\n """,
"""33. ₦800,000 worth of ordinary shares of 50k were issued at ₦1 each, payable in full on application. 
The entry in the cash book would be to  
A. credit ₦1,600,000 
B. debit ₦1,600,000 
C. credit ₦1,600,000 
D. debit ₦800,000 
\n """,
"""34. The account of government into which all monies are received and from which all expenditures are disbursed is the __  
A. Federation account 
B. Petroleum Technology Development Fund 
C. Central Bank Account 
D. Development fund 
\n """,
"""35. In government accounting, the method used which records on the basis of financial entity with self-balancing books 
instead of entity of proprietorship is 
A. virement 
B. fund accounting 
C. consolidated fund 
D. financial regulation 
\n """, ]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'c'),
        Question(question_prompts[2], 'b'),
        Question(question_prompts[3], 'd'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'b'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'b'),
        Question(question_prompts[8], 'c'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'd'),
        Question(question_prompts[11], 'c'),
        Question(question_prompts[12], 'd'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'b'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'b'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'a'),
        Question(question_prompts[20], 'b'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'd'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'b'),
        Question(question_prompts[25], 'd'),
        Question(question_prompts[26], 'd'),
        Question(question_prompts[27], 'c'),
        Question(question_prompts[28], 'a'),
        Question(question_prompts[29], 'b'),
        Question(question_prompts[30], 'c'),
        Question(question_prompts[31], 'c'),
        Question(question_prompts[32], 'd'),
        Question(question_prompts[33], 'a'),
        Question(question_prompts[34], 'd'),
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
def FinancialAcc_2010():
    question_prompts=[
        """1. The historical development of accounting reveals that it ___.  
        A. deals with debit and credit terms 
        B. is a product of financial development 
        C. is a product of its own environment 
        D. is an ideal subject for financial development 
        \n """,
        """2. In a trial balance, income and liabilities are__  
        A. debited and credited respectively  
        B. Credited 
        C. Credited and debited respectively 
        D. Debited 
        \n """,
        """3. The principle of double entry ensures__.  
        A. mathematical accuracy in trial balance 
        B. Balance at the bank 
        C. increases in the assets and liabilities 
        D. balance of cash account. 
        \n """,
        """4. The major feature of a journal is that it has__.  
        A. six columns, date, particulars, folio, amount, debit and credit 
        B. five columns, date, particulars, folio, debit and credit 
        C. three columns, date, particulars, folio and amount 
        D. four columns, date, particulars, folio and amount 
        \n """,
        """5. The medium of correcting errors whose difference are shown in the trial balance is by the use of __.  
        A. debtors’ account 
        B. creditors’ account 
        C. suspense account 
        D. ledger account 
        \n """,
        """6. In bank reconciliation process, discrepancies caused by timing arises as a result of __.  
        A. cash book and bank statement 
        B. bank statement only 
        C. cash book, bank statement and other incidental records 
        D. cash book only 
        \n """,
        """7. The process of reconciling cheques between banks is termed cheque__.  
        A. clearing 
        B. truncation 
        C. holding 
        D. confirmation 
        \n """,
        """8. In a bank reconciliation statement, interest charged for overdrawn balances should beadded to the ___.  
        A. balance as per bank statement 
        B. bank balance as per adjusted cashbook 
        C. aggregate balance as per cashbook 
        D. bank balance as per cashbook 
        \n """,
        """9.I. Stock of goods II. Furniture III. Creditors IV. Cash at bank V. Loan from the bank. Determine the
         current liabilities  
        A. III and V 
        B. Il and III 
        C. IV and V 
        D. l and II 
        \n """,
        """10 .I. Stock of goods II. Furniture III. Creditors IV. Cash at bank V. Loan from the bank. Find the current assets.  
        A. Ill and V 
        B. II and I 
        C. IV and V 
        D. I and IV 
        \n """,
        """11. The type of expense charged against administration of a firm is the __.  
        A. repairs on building 
        B. interest paid on loan 
        C. discount allowed 
        D. tax expense. 
        \n """,
        """12. In a period of declining price, which of the following methods would result in higher profit? 
        A. FIFO. 
        B. Simple average. 
        C. LIFO. 
        D. Weighted average. 
        \n """,
        """13. The item on the credit side of the trading account is the __.  
        A. returns outwards 
        B. carriage on sales 
        C. sales 
        D. purchases. 
        \n """,
        """14. A typical example of a real account is ___. 
        A. prepayment 
        B. expenses 
        C. plant 
        D. income. 
        \n """,
        """15. The control account can be used in ___.  
        A. recording all business transactions of the enterprise 
        B. keeping records of all direct deposits in the bank account 
        C. monitoring the books of original entry 
        D. monitoring the efficiency of bookkeeping by accountants. 
        \n """,
        """16. The costs that are directly traceable to the goods being produced is  
        A. partly manufactured goods 
        B. overhead cost 
        C. total factory expenses 
        D. prime cost. 
        \n """,
        """17. The production cost that does not form part of the product but is incidental to production and facilitates the production activities is the  
        A. prime cost 
        B. indirect cost 
        C. total cost 
        D. direct cost. 
        \n """,
        """18. Work-in-progress is the ___.  
        A. value of partly finished goods 
        B. value of finished goods on hand 
        C. sales less cost of goods sold 
        D. value of goods produced. 
        \n """,
        """19. The major feature of not-forprofit-making organization is that they are formed __?  
        A. to use accumulated fund to describe the net amount owed to members 
        B. mainly to improve the welfare of her members 
        C. to engage in trading activities to sponsor its activities 
        D. in order to compute the receipts and payments account. 
        \n """,
        """20. The subscription paid in advance is treated in the balance sheet of a club as __? 
        A. a surplus 
        B. a liability 
        C. a deficit 
        D. an asset. 
        \n """,
        """21. The capital of not-for-profit making organization is referred to  as __.  
        A. entity fund 
        B. capital owned 
        C. accumulated fund 
        D. capital employed. 
        \n """,
        """22. The major objective of departmental accounts is to ascertain the __.  
        A. contribution of each department to profit 
        B. materials sold in each department 
        C. insurance premium payable on employees 
        D. number of employees in each department. 
        \n """,
        """23. The transactions relating to liquidation in partnership account is drawn by using __.  
        A. current account 
        B. cash account 
        C. capital account 
        D. realization account. 
        \n """,
        """24. The cost method of charging goods to branch is used where__.  
        A. branch stock adjustment account is in use 
        B. the retention of branch trading account is in addition to the cost of goods sold 
        C. goods are sent without invoice or any documents 
        D. goods are of a perishable nature on which a pre-determined price is inapplicable. 
        \n """,
        """25. The correct entries to record goods transferred to branch from head office is to debit__.  
        A. branch stock account and credit goods sent to branch account 
        B. branch supplies account and credit branch stock account 
        C. branch stock account and credit purchases account 
        D. D. goods sent to branch account and credit branch stock account. 
        \n """,
        """26. The two accounts that are normally opened in the head office when goods are transferred to a branch are ______.  
        A. branch supplies and branch receipts 
        B. branch stock account and goods sent to branch accounts 
        C. goods sent to branch account and branch receipt account 
        D. goods sent to branch account and branch supplies. 
        \n """,
        """27. Goods invoiced to a branch can be sent using __.  
        A. cost price, selling price and fixed percentage on selling price 
        B. cost price, selling price and fixed percentage on cost price 
        C. cost price and fixed percentage on cost price 
        D. cost price and fixed percentage on selling price. 
        \n """,
        """28. The major point of agreement carried by the partnership deed is__.  
        A. 5% interest per annum on any loan 
        B. an oral agreement among the partners 
        C. method of inheritance by the partners' children 
        D. the profit and loss sharing ratio of the partners. 
        \n """,
        """29. Which of the following can be used on admission of a new partnership?  
        A. Revaluation account. 
        B. Profit and loss account. 
        C. Capital account. 
        D. Trading account. 
        \n """,
        """30. Goodwill is determined using __.  
        A. capital contribution of old partners. 
        B. number of partners admitted. 
        C. the business and customer relations 
        D. number of active partners. 
        \n """,
        """31. The founders of a company are __.  
        A. promoters 
        B. shareholders 
        C. canvassers 
        D. stakeholders. 
        \n """,
        """32. The fund in which all government receipts are paid is __.  
        A. consolidated revenue fund 
        B. development fund 
        C. trust fund 
        D. contingency fund. 
        \n """,
        """33. Which of the following accounts for the highest revenue to Nigeria?  
        A. Import duties. 
        B. Personal income tax. 
        C. Petroleum resources. 
        D. Company tax. 
        \n """,
        """34. If Aboki Holdings Limited issued 120,000 ordinary share of ₦2.00 each at market value of 5.50k each, the share premium would  
        A. ₦500,000 
        B. ₦450,000 
        C. ₦550,000 
        D. ₦420,000 
        \n """,
        """35. Which of the following is a signatory to federal government account?  
        A. Auditor-General. 
        B. Governor of Central Bank. 
        C. Accountant-General. 
        D. President. 
        \n """,
        """36. The chief accounting officer of a local government is the __.  
        A. Chairman 
        B. Treasurer 
        C. Director of personnel 
        D. Auditor. 
        \n """,
        """37. Which of the following signs general warrant for the release of money from the consolidated revenue fund?  
        A. Minister of Finance. 
        B. Chairman, Economic Advisory Committee 
        C. Permanent secretary. 
        D. Minister of Economic Plan
        \n """, ]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'b'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'a'),
        Question(question_prompts[6], 'a'),
        Question(question_prompts[7], 'a'),
        Question(question_prompts[8], 'a'),
        Question(question_prompts[9], 'd'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'a'),
        Question(question_prompts[12], 'c'),
        Question(question_prompts[13], 'c'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'd'),
        Question(question_prompts[16], 'b'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'b'),
        Question(question_prompts[20], 'c'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'c'),
        Question(question_prompts[23], 'a'),
        Question(question_prompts[24], 'a'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'b'),
        Question(question_prompts[27], 'd'),
        Question(question_prompts[28], 'a'),
        Question(question_prompts[29], 'b'),
        Question(question_prompts[30], 'a'),
        Question(question_prompts[31], 'a'),
        Question(question_prompts[32], 'c'),
        Question(question_prompts[33], 'd'),
        Question(question_prompts[34], 'c'),
        Question(question_prompts[35], 'a'),
        Question(question_prompts[36], 'a'),
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
def FinancialAcc_2011():
    question_prompts=[
        """1. The major function of accounting bodies in Nigeria is to ____.  
A. provide proper financial management of businesses 
B. provide good remuneration to the members 
C. promote the ethics of the profession 
D. show the dynamic nature of the profession. 
\n """,
"""2. Ledger account is mainly classified into ___.   
A. nominal, real and personal accounts 
B. fixed and current accounts 
C. management, financial and public sector accounting 
D. bank and cash accounts. 
\n """,
"""3. If salary account is debited instead of stationery account. the error committed is that of __.  
A. commission 
B. omission 
C. principle 
D. compensation. 
\n """,
"""4. If stationery bought for ₦200 has been entered as ₦2000. To correct this error  
A. debit stationery with ₦2,200 
B. credit stationery with ₦1800 
C. debit stationery with ₦1800 
D. credit stationery with ₦2200. 
\n """,
"""5. The account which refers to the tangible assets of a company that is of permanent nature is the __. 
A. personal account 
B. real account 
C. nominal account 
D. cash account. 
\n """,
"""6. The major feature of an invoice is that, it ___.  
A. passes information through the sales day book 
B. has cash and bank column 
C. specifies the particulars of goods bought 
D. indicates only the cash sales. 
\n """,
"""7. The source documents include___.  
A. cash book 
B. petty cash book 
C. general ledger 
D. credit notes. 
\n """,
"""8. A major cause of discrepancy between bank statement and the cash book that overstates the bank statement balance is the ___.  
A. commission paid 
B. interest received 
C. direct payment 
D. direct withdrawal. 
\n """,
"""9. The bank charges levied on a current account holder is the charges on ___.  
A. transaction 
B. turnover 
C. transfer 
D. cash received. 
\n """,
"""10 The cause of discrepancies between the bank statement and the cash book that overstates the cash book is the__.  
A. dividend received 
B. uncredited expenses 
C. uncredited cheques 
D. interest on lodgement. 
\n """,
"""11. Determine the provision for bad debts to profit and loss account.  
A. ₦ 500 
B. ₦ 820 
C. ₦1 300 
D. ₦ 300 
\n """,
"""12. Calculate the provision to be taken to the balance sheet.  
A. ₦ 780 
B. ₦ 44, 800 
C. ₦ 1200 
D. ₦ 200 
\n """,
"""13. Benefits enjoyed for which payments have not been made are __.  
A. accruals 
B. prepayments 
C. acquisitions 
D. provisions. 
\n """,
"""14. If an organization maintains a periodic stock system, the stock quantities are __.  
A. updated at the end of the accounting year 
B. not considered in the updating process 
C. updated continuously 
D. updated at the beginning of the accounting year. 
\n """,
"""15. If a company values its stocks in the period of rising prices using LIFO method, there is a tendency for it to  
A. have a higher cost of goods sold 
B. have a higher gross profit 
C. pay higher income tax 
D. have a higher value for closing stock. 
\n """,
"""16. The gross loss on manufacturing is always transferred to the ___. 
A. credit side of balance sheet 
B. debit side of profit and loss account 
C. credit side of profit and loss account 
D. debit side of balance sheet. 
\n """,
"""17 The depreciation on a motor vehicle that is being used for manufacturing and administration is charged to the  
A. debit side of manufacturing and profit and loss account 
B. debit side of profit and loss account only. 
C. credit side of profit and loss account only 
D. debit side of manufacturing and balance sheet. 
\n """,
"""18.The prime cost is the total of the ___  
A. production cost + selling expenses. 
B. direct material + direct labour + direct expenses 
C. direct materials + work overhead expenses. 
D. administrative expenses + selling + distribution expenses. 
\n """,
"""19.In the not-for-profit-making organization, the excess of income over expenditure is __.  
A. deducted from the capital 
B. added to the accumulated fund 
C. added to the capital 
D. deducted from the accumulated fund. 
\n """,
"""20. The equivalent of a club's receipts and payment account is the___.  
A. trading account 
B. revenue account 
C. cash account 
D. suspense account. 
\n """,
"""21. The summary of receipt and payments account represents __. 
A. cash at hand 
B. journal proper 
C. general journal 
D. ledger accounts 
\n """,
"""22. Abingo Limited has three departments K, L and M.  (i) Rent for the year ₦3000 (ii) Selling 
and distribution expenses ₦1800 Department  Turnover  Floor space in square meters  
₦ ₦ K 40 000 120 L 60 000 80 M 89 000 100 How much rent is apportioned to department K?  
A. 4 1 200 
B. ₦1 800 
C. ₦2 000 
D. ₦750 
\n """,
"""23. Abingo Limited has three departments K, L and M.  (i) Rent for the year ₦3000 (ii) Selling and distribution expenses 
₦1800 Department  Turnover  Floor space in square meters  ₦ ₦ K 40 000 120 L 60 000 80 M 89 000 100 How much selling 
and  distribution expenses is  apportioned to department M?  
A. ₦ 800 
B. ₦ 600 
C. ₦ 400 
D. ₦ 1 800 
\n """,
"""24. The Akachala Limited has four departments W, X, Y and Z. The profits or loss of the departments were 
₦20 000 loss, X ₦25 000 profit, V ₦30 000 loss and Z 1 800 profit. How much is the net profit or loss of the company?  
A. ₦7 000 loss 
B. ₦5 000 loss 
C. ₦ 5 000 profit
D. ₦7 000 profit 
\n """,
"""25. If goods were returned to branch by the customers. The correct posting for this transaction is to debit  
A. branch debtor's account and credit head office account 
B. head office account and credit branch stock account 
C. branch stock account and credit branch debtors' account 
D. branch cash account and credit branch stock account. 
\n """,
"""26. The branch expenses paid by the head office is recorded in the books by debiting branch __.  
A. bad debt account and crediting branch debtors' account 
B. expenses account and crediting bank account 
C. profit and loss account and crediting branch stock account 
D. discount allowed account and crediting branch debtors' account. 
\n """,
"""27 Goods returned to branch by branch customers is recorded in the head office books by debiting ___.  
A. bank account and crediting branch stock account 
B. goods sent to branch account and crediting branch debtors' account 
C. branch stock account and crediting branch debtors' account 
D. branch debtors' account and crediting cash account. 
\n """,
"""28. Which of the following is mostly used in treating partners' current earnings?  
A. Savings account 
B. Current account 
C. Capital account 
D. Share capital account 
\n """,
"""29. The salary of a partner is usually debited to the __.  
A. sundry debtors' account 
B. appropriation account 
C. profit and loss account 
D. sundry current account. 
\n """,
"""30. The rules which govern the internal management of a firm and its financial affairs ina partnership business is a  
A. memorandum 
B. bye-law 
C. deed 
D. financial regulation. 
\n """,
"""31. The interest on partners' loan is __. 
A. debited in current account 
B. credited in profit and loss account 
C. debited in profit and loss account 
D. credited in current account. 
\n """,
"""32.  The capital contributed by the partners is treated in the  
A. current account 
B. capital account 
C. trading account 
D. balance sheet 
\n """,
"""33. Given: 6 000 000 10% preference shares of ₦ 0.50 each 6 000 000 ordinary shares of
 ₦1 each Capital reserves ₦2 700 000 Long-term liabilities ₦4 000 000  Find the value of authorized share capital.  
A 13 000 000 
B. 12 000 000 
C. 9 000 000 
D.15 700 000 
\n """,
"""34. The Directors' salaries paid are items of ___.  
A. current liabilities 
B. profit and loss account 
C. trading account 
D. current assets. 
\n """,
"""35. Sundry debtors in the balance sheet of Onoja Bakery and Sons totalled ₦800 000. A provision of 2% was 
made for discount and 5% provision for bad and doubtful debts.  Find the amount for sundry debtors after provision.  
A. ₦760 000
B. ₦744 800 
C. ₦744 000
D. ₦784 000 
\n """,
"""36. An ordinary share of ₦80 was issued at ₦96. The share was issued at  
A. premium 
B. par 
C. discount 
D. loss. 
\n """,
"""37. The financial plan of the government for a year is contained in the __.  
A. budget 
B. cash analysis book 
C. vote book 
D. gazette. 
\n """,
"""38. An increase in government expenditure within a year is taken care of by means of ___  
A. financial regulations 
B. virement 
C. warrant 
D. supplementary estimate. 
\n """,
"""39. As evidence of payments to a government ministry, the revenue collectors will issue  
A. treasury receipt 
B. receipts voucher card 
C. treasury card 
D. stores receipt voucher. 
\n """, ]
    question = [
        Question(question_prompts[0], 'c'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'b'),
        Question(question_prompts[5], 'c'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'c'),
        Question(question_prompts[8], 'b'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'd'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'a'),
        Question(question_prompts[13], 'a'),
        Question(question_prompts[14], 'b'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'b'),
        Question(question_prompts[17], 'b'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'c'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'a'),
        Question(question_prompts[23], 'a'),
        Question(question_prompts[24], 'c'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'b'),
        Question(question_prompts[27], 'b'),
        Question(question_prompts[28], 'b'),
        Question(question_prompts[29], 'c'),
        Question(question_prompts[30], 'c'),
        Question(question_prompts[31], 'b'),
        Question(question_prompts[32], 'c'),
        Question(question_prompts[33], 'b'),
        Question(question_prompts[34], 'c'),
        Question(question_prompts[35], 'a'),
        Question(question_prompts[36], 'a'),
        Question(question_prompts[37], 'd'),
        Question(question_prompts[38], 'a'),
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
def accounting_2019():
    question_prompts=["""1. The major distinguishing element between the final account of a partnership and a sole trader is the  
A. drawing 
B. creditors account 
C. appropriation account 
D. capital account 
""","""2. Goodwill appears in the books of a business only if it has been  
A. raised in connection with the admission of a new partner 
B. purchased at a certain price if it has been raised 
C. raised to account for the true value of a business on the death of a partner 
D. raised in other to prevent the balance sheet showing that the business is insolent  
""","""3. A payment of cash of ₦20 to john was entered on the receipts side of the cash book in error and credited to john’s account. Which  of the following journal entries can be used to correct the error  
A. John ₦40 Dr, cash ₦40 Cr 
B. cash ₦40 Dr, john ₦40 Cr 
C. cash ₦20 Dr, john ₦20 Cr 
D. john ₦20 Dr, cash ₦20 Cr   
""","""4. The following represents extracts from the trading account of a retail outlet for a retail outlet for a given month:Opening stock 2400 Closing stock 6400 
Other expenses 2000 Sales 11000 Profit 900  What is the purchase figure for 
the month?  
A. ₦13 000 
B. ₦11 000 
C. ₦12 000 
D. ₦12 000   
""","""5. Subscription relating to the accounting to the accounting year 1993 in the income and expenditure account is __.  
A. ₦14,300 
B. ₦13,400 
C. ₦15,050 
D. ₦14, 550  
""","""6. Accumulated fund on 1st January 1993 is __.  
A. ₦8,570 
B. ₦7, 520 
C. ₦8, 470
D. ₦7,850 
""","""7. A pottery company had sales of ₦176,000 during the current period and a gross profit rate of 40% the company cost of merchandise for sale during the period was ₦128,000. The company’s ending inventory is  
A. ₦76 800 
B. ₦51300 
C. ₦32,000 
D. ₦22400    
""","""8.Cost of raw materials consumed 300,600 Returns of raw materials 6,700 Closing stocks of raw materials 100,250 Manufacturing wages 27,000 Lighting, power, insurance and rent relating to the factory are apportioned 1/3, 2/5, 1/6 and 1/7 with totals ₦30,000; ₦75,000; ₦36,000 and ₦56,000 respectively.  What is the cost of the opening raw materials?  
A. ₦400,250 
B. ₦398,250 
C. ₦404,950 
D. ₦418,350 
""","""9.Cost of raw materials consumed 300,600 Returns of raw materials 6,700 Closing stocks of raw materials 100,250 Manufacturing wages 27,000 Lighting, power, insurance and rent relating to the factory are apportioned 1/3, 2/5, 1/6 and 1/7 with totals ₦30,000; ₦75,000; ₦36,000 and ₦56,000 respectively.  The production cost of finished goods is __.  
A. ₦408,600 
B. ₦381,000 
C. ₦327,600 
D. ₦54,600   
""","""10.Subscriptions received during the year 30,000 Subscriptions owed last year  4,000 Subscriptions received for  next year 6,000  The ₦6,000 subscription 
received is  
A. capital 
B. fixed asset 
C. current asset 
D. current liability   
""","""11. What is the subscription to be charged to income and expenditure account?  
A. ₦20,000 
B. ₦30,000 
C. ₦34,000 
D. ₦36,000   
""","""12.Capital 24,000 Land and building 18,470 Mortgage on premises 11,090 Drawings 3,000 Profit and Loss 3,600 Furniture and fittings 5,120 Motor Vehicles 3,462 Closing Stock 3,000 Debtors 11,474 Creditors 7354 Cash 1,518 46,044 What is the capital employed?  
A. ₦44 600 
B. ₦43 052 
C. ₦38 600 
D. ₦43 044  
""","""13.Capital 24,000 Land and building 18,470 Mortgage on premises 11,090 Drawings 3,000 Profit and Loss 3,600 Furniture and fittings 5,120 Motor Vehicles 3,462 Closing Stock 3,000 Debtors 11,474 Creditors 7354 Cash 1,518 46,044.Calculate the value of fixed assets.  
A. ₦15 992 
B. ₦18 470 
C. ₦27 052 
D. ₦27 000  
""","""14. Goods withdrawn from for private use are credited to __.  
A. Purchases 
B. Drawing 
C. Sales 
D. Capital   
""","""15. Stationery which will be used for a long period of time is usually recorded as an expense instead of an asset. This concept is called __.  
A. Entity 
B. Realisation 
C. Accrual 
D. Materiality  
""","""16. Adaobi mistakenly entered ₦7,000 as credit in Abba’s account instead of Baba’s account this is __.  
A. An error of principles 
B. An error of commission 
C. A compensating error 
D. An error of omission  
""","""17. The gross profit disclosed in the branch stock adjustment account represents __. 
A. Branch profit 
B. Estimated profit 
C. Unrealized profit 
D. Head office profit 
""","""18. Partner’s share of profit is credited to __.  
A. The profit and loss appropriation account 
B. The profit and loss account 
C. A partner’s current account 
D. A partner’s capital account    
""","""19.Stock of material 1/1 10 000 Purchase of raw materials 160 000 Manufacturing wages 420 000 Royalties 3 000 Stock of raw materials 31/12 14 000  What is the cost of raw materials consumed?  
A. ₦156 000 
B. ₦173 000 
C. ₦170 000 
D. ₦160 000  
""","""20. Calculate the prime cost.  
A. ₦597 000 
B. ₦567 000 
C. ₦57 9000 
D. ₦576 000   
""","""21.Jan. 1  Received 1,000  ₦10 each units at Jan.2  Received 2,000  ₦12 each units at Jan. 3  Issued 1,500 units Jan. 4  Received 1,000  ₦11 each units at Jan. 5  Issued 1000 units   Using FIFO method, what is the value of the closing stock? 
A. ₦17 000 
B. ₦29 000 
C. ₦34 000 
D. ₦12 000   
""","""22.Jan. 1  Received 1,000  ₦10 each units at Jan.2  Received 2,000  ₦12 each units at Jan. 3  Issued 1,500 units Jan. 4  Received 1,000  ₦11 each units at Jan. 5  Issued 1000 units   What is the value of closing stock using simple average? 
A. ₦11 500 
B. ₦17 000 
C. ₦28 500 
D. ₦17 500 
""","""23. The gross loss on manufacturing is always transferred to the __.  
A. credit side of the balance sheet 
B. credit side of the profit and loss account 
C. debit side of the balance sheet 
D. debit side of the profit and loss account   
""","""24. The depreciation on a motor vehicle that is being used for manufacturing and administration is charged to the __.  
A. Debit side of the manufacturing and profit and loss account 
B. Credit side of profit and loss account only 
C. Debit side of manufacturing and balance sheet 
D. Debit side of the profit and loss account only   
""","""25. In bank reconciliation process, discrepancies caused by timing arises as a result of __.  
A. bank statement only 
B. cash book and bank statement 
C. cash book, bank statements and incidental records 
D. cash book only   
""","""26. The process of reconciling cheque between banks termed cheque __.  
A. truncation 
B. clearing 
C. holding 
D. confirmation 
""","""27. Cash Book(Extract)Balance b/f 2,200 Sundry Expenses 16,800 Receipt from Customers 1600 Drawings 4,700 Suppliers 7,300  Debtors opening and closing balances amount to ₦6 500 and ₦7,600 respectively. What is the sales value?  
A. ₦17 500 
B. ₦29 400 
C. ₦31 600 
D. ₦15 300  
""","""28. Given:Fixtures 30,000 Debtors 7,000 Stock 8,000 Creditors 3,000 Goodwill    10,000  Determine the capital  
A. ₦10,000 
B. ₦42,000 
C. ₦52,000    
""","""29.Sales 232,000 Opening stock 28,000 Purchases 128,000 Carriage inwards 4,000 Carriage outwards 6,000 Closing stock 10,000 Discount received  18,000 Expenses  20,000 Calculate the gross profit.  
A. ₦100 000 
B. ₦86 000 
C. ₦76 000 
D. ₦82 000  
""","""30.Sales 232,000 Opening stock 28,000 Purchases 128,000 Carriage inwards 4,000 Carriage outwards 6,000 Closing stock 10,000 Discount received  18,000 Expenses  20,000   Calculate the expenses debited to the profit and loss account.  
A. ₦17 000 
B. ₦23 000 
C. ₦30 000 
D. ₦26 000   
""","""31.(Extract)Bal.b/d 390  Expenses on cleaning 300 Sales of tickets 4,000 New tool   50 Donations 3,000 Repairs 400 Subscriptions 6,500 Electricity 350   What is the total income for the period?  
A. ₦13 500 
B. ₦13 890 
C. ₦9 500 
D. ₦10 500   
""","""32. What is the balance carried down?  
A. ₦12 330 
B. ₦13 430 
C. ₦11 680 
D. ₦11 930  """]
    question = [
        Question(question_prompts[0], 'b'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'd'),
        Question(question_prompts[3], 'c'),
        Question(question_prompts[4], 'a'),
        Question(question_prompts[5], 'b'),
        Question(question_prompts[6], 'd'),
        Question(question_prompts[7], 'c'),
        Question(question_prompts[8], 'b'),
        Question(question_prompts[9], 'd'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'd'),
        Question(question_prompts[12], 'c'),
        Question(question_prompts[13], 'a'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'a'),
        Question(question_prompts[17], 'c'),
        Question(question_prompts[18], 'a'),
        Question(question_prompts[19], 'c'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'c'),
        Question(question_prompts[22], 'd'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'b'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'a'),
        Question(question_prompts[27], 'c'),
        Question(question_prompts[28], 'd'),
        Question(question_prompts[29], 'd'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'a'),
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
             print('\nsorry,you failed the question😣😣😦😦😭😢😟\nthe answer is',question.answer,"\n")
     des.update({nam:(str(score)+'/'+str(len(questions)))})
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%','/100%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
     while True:
       r=input("do you wish to replay(yes or no):")
       if r.lower()=="yes":
           accounting_2019()
       elif r.lower()=="no":
           break
    run_test(question)
def financial_accounting_2013():
    question_prompts=["""1. Accounting information seeks to provide ___. 
A. permanent records for all transactions 
B. analysis of accounts to trade debtors 
C. audited reports on the accounts of a company 
D. data about the employees of a company 
A. permanent records for all transactions  
""","""2. When the debit side total of an account, it means that the account has  
A. been overdrawn  
B. been understated 
C. debit balance 
D. credit balance 
C. debit balance  
""","""3.July 1 - Started business with ₦10,500 July 31- Paid Agromachinex ₦6,000 owing them.The double entry for July 1 would be 
A. debit capital and credit cash 
B. credit cash and debit bank 
C. debit cash and credit capital 
D. debit purchases and credit cash 
C. debit cash and credit capital  
""","""4.July 1 - Started business with ₦10,500 July 31- Paid Agromachinex₦6,000 owing them  The double entry for July 31 would be  
A. debit Agromachinex and credit cash 
B. debit equipment and credit Agromachinex 
C. credit capital and debit cash 
D. credit cash and debit purchases 
A. debit Agromachinex and credit cash  
""","""5. The total credit sales for a period can be extracted from the __.  
A. cash book 
B. sales day book 
C. petty cash book 
D. returns inwards 
B. sales day book  
""","""6. The major source document which enables an employer to calculate the employee wages is the __.  
A. nominal roll of employees 
B. record of number of hours worked 
C. effort of the employee 
D. record of number of dependants per employee 
B. record of number of hours worked  
""","""7. Which of the following items is a capital expenditure?  
A. Maintenance of office machine 
B. Purchase of office stationery 
C. Carriage inwards 
D. Purchase of office machinery 
D. Purchase of office machinery  
""","""8. The corresponding entry of personal accounts found in the debit side of the cash is to __.  
A. credit real accounts 
B. debit real accounts 
C. credit the ledger 
D. debit the ledger 
C. credit the ledger  
""","""9. Alaka who owed Saka ₦15,000, settled his debt after deducting cash discount of 10 %. To record the discount in the book of Saka, debit  
A. discount received account and credit Alaka's account 
B. Alaka's account and credit discount received account 
C. Saka's account and credit discount received account 
D. discount allowed account and credit Alaka's account  
D. discount allowed account and credit Alaka's account  
""","""10.A machine bought for ₦35,000 was estimated to have a life span of 5 years with a scrap value of ₦9,000.  The yearly depreciation using the straight line method would be  
A. ₦8,800 
B. ₦6,500 
C. ₦5,200 
D. ₦4,400 
C. ₦5,200  
""","""11.A machine bought for ₦35,000 was estimated to have a life span of 5 years with a scrap value of ₦9,000.  If the scrap value is presently ₦15,000 what will be the yearly depreciation using straight line method?  
A. ₦4,000 
B. ₦7,000 
C. ₦11,000 
D. ₦24,000 
A. ₦4,000  
""","""12. The purchase of mattresses from Freehold enterprises by cheque amounted to ₦305,150. The correct entries for this transaction in the book of the buyer is to debit  
A. sales account and credit bank account 
B. purchases and credit bank account 
C. cash and credit freehold 
D. bank and credit freehold 
B. purchases and credit bank account  
""","""13. What type of stock valuation would a vegetable seller adopt in valuing it's product?  
A. LIFO 
B. FIFO 
C. Simple average 
D. Weighted average 
B. FIFO  
""","""14. The total cash and cheques received from customers in a control account is derived from the 
A. purchases day book 
B. cash book 
C. income and expenditure account 
D. sales journal 
B. cash book  
""","""15. Given: Opening capital   ₦50,000 Closing capital   ₦64,000 Drawings    ₦16,000 Determine the net profit  
A. ₦2,000 
B. ₦14,000 
C. ₦20,000 
D. ₦30,000 
D. ₦30,000  
""","""16. The estimated profit or loss for a period is calculated by  
A. closing capital less opening capital add drawings 
B. opening capital less closing capital add drawings 
C. opening capital less drawings add closing capital 
D. opening capital add closing add drawings 
A. closing capital less opening capital add drawings  
""","""17. When goods produced are transferred at cost plus mark-up sale, the difference between the cost and the transferred price is a  
A. discount 
B. sales commission 
C. manufacturing profit 
D. factory reserves 
C. manufacturing profit  
""","""18. The addition of prime cost, indirect cost and opening work-inprogress less the closing work-inprogress will result in cost of__. 
A. goods available for sale 
B. goods sold 
C. goods manufactured 
D. materials put into production 
C. goods manufactured  
""","""19. Calculate the cost of raw materials used  
A. ₦495,000 
B. ₦415,000 
C. ₦335,000 
D. ₦305,000 
C. ₦335,000  
""","""20. Determine the prime cost. 
A. ₦525,000 
B. ₦515,000 
C. ₦465,000 
D. ₦365,000 
D. ₦365,000  
""","""21. In manufacturing account, the work-in-progress at the end of the year is __.  
A. deducted from the cost of goods completed during this year 
B. added to the cost of goods completed 
C. stated in the profit and loss account 
D. stated in the prime cost section 
A. deducted from the cost of goods completed during this year  
""","""22. Which of the following is accounted for in receipts and payment account?  
A. Subscriptions received in advance 
B. Subscriptions due not yet received 
C. Accrued expenses on annual dances 
D. Depreciation of the club house 
A. Subscriptions received in advance  
""","""23. Which of the following expenses relates to the profit and loss account of a manufacturing firm  
A. Direct materials 
B. Direct labour 
C. Administrative overhead 
D. Work-in-progress 
C. Administrative overhead  
""","""24. I. Direct materials II. Direct labour III. Direct expenses IV. Factory expenses  Prime cost consists of? 
A. I, II and III 
B. I, II and IV 
C. I, III and IV 
D. II, III and IV 
A. I, II and III  
""","""25. The amount paid by a new partner on admission as a compensation for the reputation built up by old partners is a  
A. bonus 
B. commission 
C. premium 
D. goodwill 
D. goodwill  
""","""26. A partnership's internal regulations are set out by 
A. a deed 
B. a law 
C. a constitution 
D. an article 
A. a deed  
""","""27. In a partnership account, interest on drawings is  
A. debited to appropriation account 
B. credited to appropriation account 
C. treated as an expense in profit and loss account 
D. recorded in the balance sheet as current assets 
B. credited to appropriation account  
""","""28. When a share valued at 50k is issued at ₦1.59, it is said to be issued at  
A. par 
B. premium 
C. discount 
D. interest 
B. premium  
""","""29. The purchase consideration that is lower than the net asset implies that, the buyer has gained the advantage of  
A. net income 
B. revenue reserve 
C. capital reserve 
D. net loss 
C. capital reserve  
""","""30. When shares are issued at a discount, entries are to debit __.  
A. application allotment account and credit discount account 
B. discount account and credit 
C. cash account and credit discount account 
D. discount account and credit bank account 
A. application allotment account and credit discount account  
""","""31. When there is no basis of apportionment in an organization, the expenses should be apportioned based on  
A. sales 
B. purchases 
C. equality 
D. floor space 
C. equality  
""","""32. The objective of departmental account is to  
A. ascertain the cost of running the organization 
B. ascertain the amount of profit or loss for each department 
C. ascertain the amount of profits for losses for the enterprises 
D. offset the loss of each treatment 
B. ascertain the amount of profit or loss for each department  
""","""33. Which of the following is the capital reserve of a company?  
A. Share premium 
B. Retained profit 
C. Accumulated depreciation 
D. Loss on forfeited shares 
A. Share premium  
""","""34. Given:Applications were invited by the directors of Abiodun PLC for 500,000 ordinary shares of ₦1:00 each at ₦1:10 per share payable as follows;   On application 46k On allotment 20k 1st Call 15k 2nd Call 19k How much is to be paid for application?  
A. ₦230,000
B. ₦280,000 
C. ₦500,000 
D. ₦550,000 
A. ₦230,000 
""","""35. The issued share capital is the number of shares that are ___ 
A. authorized by share holders 
B. shared among the directors 
C. fully subscribed 
D. in the share certificate 
A. authorized by share holders  
""","""36. The distributable profit available to shareholders at the end of each year is the __.  
A. total profit and debtors balance 
B. general reserve and retained profit 
C. retained profit and fictitious assets 
D. total profit less creditors balance 
D. total profit less creditors balance  
""","""37. The debenture issued at par above the nominal value is said to be issued at a  
A. cost price 
B. mark-up 
C. premium 
D. margin 
C. premium  
""","""38. Accountant-general of the federation is responsible for  
A. the general supervision of all auditing personnel in all the ministries 
B. the compilation of annual financial statement 
C. the interpretation of rules and regulations affecting the private sectors 
D. ensuring the efficient operation of the ministries 
B. the compilation of annual financial statement  
""","""39. Given:Assets and Liabilities of a Local Government Bank balance 6,484,000 Cash 900 General revenue balances 9,774,500 Accrued salaries 1,220,000 Investment in shares 1,480,000 Vehicles 7,620,000  Calculate the liabilities of the local government  
A. ₦10,994,500 
B. ₦17,394,500 
C. ₦18,774,500 
D. ₦18,874,500 
A. ₦10,994,500  
""","""40. An instrument which allows public officers to increase expenditure within a year is __ .  
A. statutory allocation 
B. supplementary budget 
C. virement 
D. warrant 
B. supplementary budget"""  ]
    question = [
        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'c'),
        Question(question_prompts[2], 'c'),
        Question(question_prompts[3], 'a'),
        Question(question_prompts[4], 'b'),
        Question(question_prompts[5], 'b'),
        Question(question_prompts[6], 'd'),
        Question(question_prompts[7], 'c'),
        Question(question_prompts[8], 'd'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'b'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'a'),
        Question(question_prompts[16], 'c'),
        Question(question_prompts[17], 'c'),
        Question(question_prompts[18], 'c'),
        Question(question_prompts[19], 'd'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'c'),
        Question(question_prompts[23], 'a'),
        Question(question_prompts[24], 'd'),
        Question(question_prompts[25], 'a'),
        Question(question_prompts[26], 'b'),
        Question(question_prompts[27], 'b'),
        Question(question_prompts[28], 'c'),
        Question(question_prompts[29], 'a'),
        Question(question_prompts[30], 'c'),
        Question(question_prompts[31], 'b'),
        Question(question_prompts[32], 'a'),
        Question(question_prompts[33], 'a'),
        Question(question_prompts[34], 'a'),
        Question(question_prompts[35], 'd'),
        Question(question_prompts[36], 'c'),
        Question(question_prompts[37], 'b'),
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
     while True:
       r=input("do you wish to replay(yes or no):")
       if r.lower()=="yes":
           accounting_2019()
       elif r.lower()=="no":
           break
    run_test(question)