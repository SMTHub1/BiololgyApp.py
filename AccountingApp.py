from Question import Question
def Accounting_2020():
    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False
    question_prompts=["""Q1 "Financial statements do not disclose all information users need to know about a firm." This is the
concept of
A consistency
B money measurement
C dual aspect
D materiality
\n""",
"""Q2 A merchant paid ₦180,000 on rent for 18 months but charged ₦120,000 to profit and loss account for
the year. The concept applied is
A business entity
B going concern
C accrual
D materiality
\n""",
"""Q3 The practice of identifying the one constant approach where a number of approaches exist for solving
an accounting problem is the convention of
A conservatism
B consistency
C prudence
D materiality
\n""",
"""Q4 The assumption that a business has perpetual existence is recognised by
A entity concept
B periodicity concept
C going-concern concept
D realisation concept
\n""",
"""Q5 The accounting principle which states that for every debit entry, there is a corresponding credit entry
is recognised by
A realisation concept
B entity concept
C going concern concept
D dual aspect concept
\n""",
"""Q6 Which of the following is not an accounting convention?
A Materiality
B Consistency
C Business entity
D Periodicity
\n""",
"""Q7 Which of the following bases of accounting does not make allowance for depreciation?
A Cash basis
B Accrual basis
C Matching basis
D Commitment basis
\n""",
"""Q8 The basis of accounting which eliminates debtors and creditors is
A cash basis
B accrual basis
C fund basis
D commitment basis
\n""",
"""Q9 Whatever is fed into the computer is exactly what would be processed and produced as output. This is
the concept of
A sorting out
B last in, first out
C first in, first out
D garbage in, garbage out
\n""",
"""Q10 "A business unit is assumed to operate into foreseeable future and earn reasonable net income." This
statement is emphasizes by the concept of
A business entity
B going concern
C realization
D accrual
\n""",
"""Q11 Which of the following is not an accounting concept?
A Periodicity
B Accuracy
C Consistency
D Objectivity
\n""",
"""Q12 Transactions are governed by legal principles, but are nevertheless accounted for an presented in
accordance with the substance and financial reality. This is in compliance with the principle of
A substance over form
B prudence
C objectivity
D materiality
\n""",
"""Q13 The accounting concept which allows the use of a partical method for treating a transaction for a
reasonable number of years is
A consistency
B cost
C accrual
D conservatism
\n""",
"""Q14 The accounting concept that supports the application of double entry book-keeping is the
A going concern concept
B dual aspect concept
C historical cost concept
D consistency concept
\n""",
"""Q15 Which of the following is a limitation of the money measurement concept?
A Efficient management is not diclosed
B There is no basis for comparison
C Inter-period comparison is impossible
D It does not allow choice of methods
\n""",
"""Q16 Which of the following is not an accounting concept?
A Entity
B Going-concern
C Consistency
D Historical cost
\n""",
"""Q17 A trader is paid ₦15,000 on rent for 15 months but charged ₦12,000 to the Profit and Loss Account for
the year. This is the concept of
A accrual
B materiality
C prudence
D going-concern
\n""",
"""Q18 "Accountants do not count chickens before they are hatched". This is the concept of
A accrual
B materiality
C realisation
D going-concern
\n""",
"""Q19 "The Accountant thinks the investment in the books are worthless." This is
A consistency concept
B objectivity concept
C conservatism concept
D money measurement concept
\n""",
"""Q20 Profits are recognised when goods are sold. What concept is this?
A Realization
B Matching
C Periodicity
D Going concern
\n""",]
    question = [
        Question(question_prompts[0], 'b'),
        Question(question_prompts[1], 'c'),
        Question(question_prompts[2], 'b'),
        Question(question_prompts[3], 'c'),
        Question(question_prompts[4], 'd'),
        Question(question_prompts[5], 'd'),
        Question(question_prompts[6], 'd'),
        Question(question_prompts[7], 'a'),
        Question(question_prompts[8], 'd'),
        Question(question_prompts[9], 'b'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'a'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'a'),
        Question(question_prompts[15], 'a'),
        Question(question_prompts[16], 'a'),
        Question(question_prompts[17], 'c'),
        Question(question_prompts[18], 'c'),
        Question(question_prompts[19], 'a'),
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
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")

    run_test(question)
    while play_again():
        Accounting_2020()
    print("""Accounting Concepts and Conventions enter year 2020,Cash Book, Bank Transactions and Reconciliation Statements
    enter year 2021

    """)
    year = input("enter your year")
    year = year.upper()
    if year == "2020":
        Accounting_2020()
    if year == "2021":
        Accounting_2021()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")
def Accounting_2021():

    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False
    question_prompts=["""Q1 Cash discount is often recorded on
A the debit side of the cash book
B the credit side of the cash book
C the folio column of the cash book
D both credit and debit side of the cash book
\n""",
"""Q2 The standing order is a payment instruction given by a
A customer to the bank
B bank to the customers
C bank to an employee
D customer to a fellow customer
\n""",
"""Q3 Which of the following should not be added or subtracted from the bank statement balance to
determine the adjusted cash balance?
A Error by the bank
B Undercasting of the cash book
C Overcasting of the cash book
D Bank service charges
\n""",
"""Q4 Receipts and payments account is a summary of the
A budget
B trading account
C cash book
D profit and loss account
\n""",
"""Q5 Bariga, a stock broker stationery for &#8358;12 000 by cash. To record this transaction, debit
A cash and credit stationery
B purchases and credit stationery
C stationery and credit cash
D stationery and credit purchases
\n""",
"""Q6 An entry made in the bank in the column of the cash book to record movement of cash between the
office and bank is the
A real entry
B special entry
C direct entry
D contra entry
\n""",
"""Q7 Commission-on-turnover is charged on
A current accounts only
B savings accounts only
C fixed deposit accounts only
D all bank accounts
\n""",
"""Q8 The medium that enables the ATM to read the account details and process transactions directly with
the account held in the bank is the
A smart card
B communication network
C magnetic strip
D computerized account
\n""",
"""Q9 Determine the closing balance of the cash book
A #8358;655 credit
B #8358;655 debit
C #8358;130 credit
D #8358;130 debit
\n""",
"""Q10 Journal proper is used in recording
A transactions that are not regular
B returns from customers
C credit sales
D the receipts and payment of money
\n""",
"""Q11 The process whereby a cheque received by one person is given to another for payment is known as
A cheque crossing
B payment in cheque
C cheque transfer
D cheque endorsement
\n""",
"""Q12 Fatima withdraws goods from the business for personal use. The accounting treatment is to debit
A stock account and credit profit and loss account
B drawings account and credit stock account
C profit and loss account and credit drawings account
D stock and credit drawings account
\n""",
"""Q13 The use of a three-colum cash book is determine by
A cash discounts
B trade discounts
C cash transactions
D bank transactions
\n""",
"""Q14 Adaobi mistakenly entered #8358;7,000 as credit sales in Abba's account instead of Baba's account.
This is
A an error of principles
B a compensating error
C an error of commission
D an error of omission
\n""",
"""Q15 Goods withdrawn from business for private use are credited to
A sales
B capital
C purchases
D drawings
\n""",
"""Q16 Mr. Bassey purchased a motor vehicle for use in his business and debited the purchases account with
the same value. This is an error of
A principle
B omission
C original entry
D commission
\n""",
"""Q17 In a three-column cash book, the discount allowed is shown on the
A credit side
B memorandum column
C debit side
D folio column
\n""",
"""Q18 The recipient whose name appears on a cheque is called
A payee
B drawee
C drawer
D payer
\n""",
"""Q19 The imprest account is subsidiary to the
A petty cash
B cash book
C bank account
D ledger account
\n""",
"""Q20 The three-column cash book differs from the two-column cash book in
A bank column
B folio column
C discount column
D cash column
\n""",
"""Q21 Which of the following is used to update the cash book in bank reconciliation?
A Interest received and unpresented cheques
B Commission and debit note
C Unpresented cheques and direct credit
D Interest received and direct credit
\n""",
"""Q22 The transaction would be recorded in the cash book as debit
A cash and credit bank
B bank and credit cash
C cash and credit cash
D bank and credit bank
\n""",
"""Q23 Receipts and payments account is the summary of
A income and expenditure
B cash book
C balance sheet
D profit and loss
\n""",
"""Q24 The normal accounting entry to record the dishonour of a cheque by a businessman is to
A debit cash book and credit suspense account
B debit cash book and credit drawer
C credit cash book and debit suspense account
D credit cash book and debit drawer
\n""",
"""Q25 When a bill is negotiated to a bank, it is said to be
A accepted
B discounted
C surrendered
D cashed
\n""",
"""Q26 To write off bad debt, debit
A debtor's account and credit provision for bad debt
B bad debt account and credit debtor's account
C debtor's account and credit bad debt
\n""",
"""Q27 In order to make the cash book balance equal to the bank statement, it is usual to add
A uncredited cheques
B direct payments by bank
C bank charhges
D unpresented cheques
\n""",
"""Q28 A source document that aids the ascertainment of amount paid out of a current account is the
A teller
B cheque stub
C cheque
D teller stub
\n""",
"""Q29 The most convenient cash book used by a petty trader operating in an area where there is no banking
faculty is
A four column
B three column
C single column
D two column
\n""",
"""Q30 An expenses account is closed by a debit to
A an asset account and credit to the expenses account
B the expense account and a credit to an asset account
C profit and loss account and credit to the expense account
D the expense account and a credit to profit and loss account
\n""",
"""Q31 A source document for the sales day book is
A requisition form
B an invoice
C a customer advice
D a credit advice
\n""",
"""Q32 In a cash book, the opening balance was #8358;7,600, closing balance #8358;9,200 and 
the total cash received during the period was #8358;18,000. What was the amount of cash paid out during the
period?
A #8358;8,900
B #8358;9,900
C #8358;14,600
D #8358;16,400
\n""",]
    question = [

        Question(question_prompts[0], 'd'),
        Question(question_prompts[1], 'a'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'c'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'd'),
        Question(question_prompts[6], 'a'),
        Question(question_prompts[7], 'a'),
        Question(question_prompts[8], 'a'),
        Question(question_prompts[9], 'a'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'b'),
        Question(question_prompts[12], 'a'),
        Question(question_prompts[13], 'c'),
        Question(question_prompts[14], 'd'),
        Question(question_prompts[15], 'a'),
        Question(question_prompts[16], 'c'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'b'),
        Question(question_prompts[19], 'c'),
        Question(question_prompts[20], 'b'),
        Question(question_prompts[21], 'b'),
        Question(question_prompts[22], 'b'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'b'),
        Question(question_prompts[25], 'b'),
        Question(question_prompts[26], 'd'),
        Question(question_prompts[27], 'b'),
        Question(question_prompts[28], 'c'),
        Question(question_prompts[29], 'c'),
        Question(question_prompts[30], 'b'),
        Question(question_prompts[31], 'd'),
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
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
    while play_again():
        Accounting_2021()
    print("""Accounting Concepts and Conventions enter year 2020,Cash Book, Bank Transactions and Reconciliation Statements
       enter year 2021

       """)
    year = input("enter your year")
    year = year.upper()
    if year == "2020":
        Accounting_2020()
    if year == "2021":
        Accounting_2021()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")
def Accounting_2019():

    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False
    question_prompts=["""Q1 A document which acknowledges that a company owes a person a stated sum of money with an
agreement to pay a fixed rate of interest periodically is
A share certificate
B allotment certificate
C preference certificate
D debenture certificate
\n""",
"""Q2 The document making a public offer for the sale of a company's share is
A Memorandum of Association
B Articles of Association
C Prospectus
D Certificate of Registration
\n""",
"""Q3 Prepayment is treated in the balance sheet of firm as a
A fixed asset
B long-term liability
C current asset
D current liability
\n""",
"""Q4 A debenture holder is
A creditor
B promoter
C debtor
D shareholder
\n""",
"""Q5 A stock as a form of capital of a company comprises
A tons of merchandise
B units of goods
C units of shares
D bundles of war
\n""",
"""Q6 Which of the following terms is not used to describe the total amount stated in the memorandum of
association approved by the registrar of companies?
A Authorised capital
B Registered capital
C Issued capital
D Nominal capital
\n""",
"""Q7 The class of share to which payment of dividend depends on profit is
A forfeited shares
B ordinary shares
C bonus shares
D preference shares
\n""",
"""Q8 Payment for shares in instalments is done by means of
A calls
B circulars
C subscription
D invitation
\n""",
"""Q9 Which of the following formulae is used to calculate stock turnover rate?
A sales / Average stock
B Cost of Sales / Average stock
C Cost of sales / Closing stock
D Cost of sales / Opening stock
\n""",
"""Q10 The maximum amount which a company is allowed to raise through the sale of shares is
A authorised capital
B paid-up capital
C issued capital
D working capital
\n""",
"""Q11 Holders of ordinary shares do not have the right to
A participate in additional issue of shares
B vote at annual general meetings
C elect the board of directors
D receive dividends at a predetermined rate
\n""",
"""Q12 An example of capital gain is
A premium
B bonus
C shares
D debentures
\n""",
"""Q13 Which of the following attracts a fixed rate of dividend?
A Ordinary shares
B founders' shares
C Preference shares
D Deferred shares
\n""",
"""Q14 The amount set aside out of profits earned by a company which are not meant for liability or
contigency are
A dividends
B provisions
C retained profits
D reserves
\n""",
"""Q15 In company accounts, profit after tax is shared in the
A appropriation account
B revaluation account
C current account
D realization account
\n""",
"""Q16 Which of the following ratios measure the ability of a firm to meet short-term obligations?
A Net profit margin
B Quick assets ratio
C Turnover ratio
D Creditors ratio
\n""",
"""Q17 When shares are sold at less than the nominal value, it means they are issued at
A a premium
B a loss
C a discount
D par
\n""",
"""Q18 A class of preference shares in which dividends rights are carried forward is
A cumulative
B participating
C redeemable
D floating-rate
\n""",
"""Q19 The class of shareholders who paid last in the event of winding-up are
A Ordinary
B Preference
C Founder
D Treasury
\n""",
"""Q20 The price paid by an acquiring company is
A conversion fee
B premium
C sales consideration
D purchase consideration
\n""",
"""Q21 A unit of a company's capital which can be bought is
A share
B interest
C asset
D property
\n""",
"""Q22 The document which advertises the sale of shares of a company is a/an
A prospectus
B debenture
C statement
D invoice
\n""",
"""Q23 Which of the following brings a company into legal existence?
A Certificate of Incorporation
B Memorandum of Association
C Articles of Association
\n""",
"""Q24 The account that shows both the cash and bank transactions of an enterprise is
A Appropriation Account
B Trading Account
C Profit and Loss Account
D Cash Book
\n""",
"""Q25 The document authorising an officer to incur expenditure is known as
A virement
B budget
C warrant
D vote
\n""",
"""Q26 When shares are oversubscribed, the promoter may decide to scale down. When this is done, the
shares are issued proportionately
A on pro-rata
B at discount
C at par
D at premium
\n""",
"""Q27 The price paid for the purchase of a business is
A credited to the Cash Account and debited to the Vendor's Account
B debited to Cash Account and credited to Vendor's Account
C debited to Business Purchase Account and credited to Asset Account
D credited to Cash Account and debited to Asset Account
\n""",
"""Q28 The income accruing to debenture holders is called
A dividend
B not profit
C shares
D interest
\n""",
"""Q29 Which of the following is not an example of fictitious asset?
A Raw materials stock
B Debit balance of Profit and Loss Account
C Premilinary expenses of a limited company
D Expenditure on incorporation carried forward
\n""",
"""Q30 Which of the following explains the short term solvency of a company?
A Acid test ratioIN NOW
B Debtor to equity ratio
C Net profit ratio margin
D Gross profit margin ratio
\n""",
"""Q31 Which of the following are correct about a limited liability company?
I. Members have power to bind the companyII. Perpetual successionIII. Certificate of Incorporation
IV. Wound-up on death of a shareholder
A II and III only
B I and IV only
C II and IV only
D I and III only
\n""",
"""Q32 Issue of prospectus is an invitation to members of the public to
A subscribe for shares
B register a company
C redeem shares
D liquidate a company
\n""",
"""Q33 Acid test ratio is
A 1:8:1
B 1:7:1
C 1:4:1
D 1:2:1
\n""",
"""Q34 Which of the following is not an intangible asset?
A Licences
B Patent
C Trade marks
D Fixtures
\n""",
"""Q35 Shares sold at the nominal value are issued at
A discount
B premium
C a loss
D par
\n""",
"""Q36 Expenses incurred when incorporating a company are
A preliminary expenses
B selling expenses
C administrative expenses
D financial expenses
\n""",
"""Q37 Company tax paid is debited to
A Profit and Loss Appropriation Account
B Manufacturing Account
C Profit and Loss Account
D Trading Account
\n""",
"""Q38 Dividend proposed by a company is shown in the Balance sheet as
A current asset
B current liability
C long-term liability
D fixed asset
\n""",
"""Q39 The main classes of shares are
A Preference Shares and Right Issue
B Fixed shares and Current Shares
C Ordinary Shares and Preferencce Shares
D Redeemable Shares and Irredeemable Shares
\n""",]
    question = [

        Question(question_prompts[0], 'd'),
        Question(question_prompts[1], 'c'),
        Question(question_prompts[2], 'c'),
        Question(question_prompts[3], 'a'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'c'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'a'),
        Question(question_prompts[8], 'b'),
        Question(question_prompts[9], 'a'),
        Question(question_prompts[10], 'a'),
        Question(question_prompts[11], 'a'),
        Question(question_prompts[12], 'c'),
        Question(question_prompts[13], 'd'),
        Question(question_prompts[14], 'a'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'c'),
        Question(question_prompts[17], 'a'),
        Question(question_prompts[18], 'a'),
        Question(question_prompts[19], 'd'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'a'),
        Question(question_prompts[22], 'a'),
        Question(question_prompts[23], 'd'),
        Question(question_prompts[24], 'c'),
        Question(question_prompts[25], 'a'),
        Question(question_prompts[26], 'a'),
        Question(question_prompts[27], 'd'),
        Question(question_prompts[28], 'a'),
        Question(question_prompts[29], 'a'),
        Question(question_prompts[30], 'a'),
        Question(question_prompts[31], 'a'),
        Question(question_prompts[32], 'b'),
        Question(question_prompts[33], 'd'),
        Question(question_prompts[34], 'd'),
        Question(question_prompts[35], 'a'),
        Question(question_prompts[36], 'a'),
        Question(question_prompts[37], 'b'),
        Question(question_prompts[38], 'c'),
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
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
    while play_again():
        Accounting_2019()
    print("""Accounting Concepts and Conventions enter year 2020,Cash Book, Bank Transactions and Reconciliation Statements
       enter year 2021

       """)
    year = input("enter your year")
    year = year.upper()
    if year == "2020":
        Accounting_2020()
    if year == "2021":
        Accounting_2021()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")
def Accounting_2018():

    def play_again():
        response = input("do you want to take the quiz again? (type yes or no)")
        response = response.upper()
        if response == "YES":
            return True
        else:
            return False
    question_prompts=["""Q1 Rent is apportioned to each department on the basis of
A area or space occupied
B equality
C turnover
D purchases
\n""",
"""Q2 Mark-up on goods sent to branch are recorded in the books by crediting
A Stock Adjustment Account; debiting Branch Stock Account
B Goods sent to Branch Account; debiting Branch Stock Account
C Bank Stock Account; debiting Stock Adjustment
D Branch Stock Account; credit Cash Account
\n""",
"""Q3 Where the head office maintains all books of accounts, goods sent to branch is credited to
A Goods sent to Branch Account
B Branch Stock Account
C Branch Stock Adjustment Account
D Head Office Current Account
\n""",
"""Q4 Which of the following is not a purpose for preparing departmental accounts? To
A compare the results of different departments
B employ staff into different departments
C reward departmental managers
D obtain information for formulating policies
\n""",
"""Q5 Where goods are invoiced by a firm to its branch at cost-plus, the branch stock adjustment account is
used to determine
A cost price
B branch profit
C selling price
\n""",
"""Q6 Which of the following is apportioned in proportion to the purchases of each department?
A Discounts received
B Selling commission
C Bad debts
D Carriage outwards
\n""",
"""Q7 Use the following information to answer 10 ₦
Rent prepaid1/01/2003 600.00
Rent paid 31/12/20033,000.00
Rent prepaid31/12/2003 400.00
Rent for 2003 amounted
A ₦4,000
B ₦3,200
C ₦3,000
D ₦2,800
\n""",
"""Q8 
Unpresented cheques 85,305
Balance as per bank statement 206,865
Balance as per
cash book 144,495
Uncredited cheques amount to
A ₦229,800
B ₦121,560
C ₦85,305
D ₦22,935
\n""",
"""Q9 A business operates on a mark-up of 25%. 
If cost of goods sold is ₦800,000. What is the profit?
A ₦360,000
B ₦200,000
C ₦160,000
D ₦40,000
\n""",
"""Q10 Rent paid as at 1st January, 2002 was ₦10,000. 
Annual rent payable is ₦80,000 and rent accrued as at
31st December, 2002 was ₦15,000. How much was paid for rent in 2002.
A ₦80,000
B ₦75,000
C ₦55,000
D ₦35,000
\n""",
"""Q11 The procedure for utilising the savings from one sub-head of expenditure to pay for another under the
same head is
A apportionment
B virement
C appropriation
D allocation
\n""",
"""Q12 The transfer of goods between departments is recorded by debiting
A the receiving department and crediting the giving department
B the giving department and crediting the receiving department
C Stock Account and and crediting Trading Account
D Trading Account and crediting Purchases Account
\n""",
"""Q13 Which of the following is the basis for apportioning rent among departments?
A Sales
B Floor area
C Number of employee
D Direct labour cost
\n""",
"""Q14 The head office usually issues goods to branches at
A prime cost
B production cost
C net realisable value
D cost price
\n""",
"""Q15 The entries necessary for recording profit loading on goods sent to branch are
A debit Branch Stock Account, credit Branch stock Adjustment
B credit Branch Stock Adjustment Account, debit goods sent to Branch Account
C debit goods sent to Branch Account, credit Branch Stock Account
D debit Branch Stock Adjustment Account, credit Branch Stock Account
\n""",
"""Q16 Profit expressed as a fraction of the selling price is known
A mark-up
B marginOIN NOW
C gross profit
D net profit
\n""",
"""Q17 How much did Olu sell goods bought at ₦1,000 if he sells at a margin of 20% on selling?
A ₦1,250
B ₦1,200
C ₦1,000
D ₦250
\n""",
"""Q18 Profit expressed as a proportion of cost price is
A gross profit
B mark-up
C margin
D profit percentage
\n""",
"""Q19 Yinka bought goods worth ₦800 and sold at a margin of 20% on selling price. How much did she sell
the goods?
A ₦1,000
B ₦960
C ₦933
D ₦820
\n""",
"""Q20 The double entry required for the mark-up is debit Branch
A Sales Account, Credit Branch Adjustment Account
B Adjustment Account, credit Branch Stock Account
C Stock Account, credit Branch Adjustment Account
D Adjustment Account, credit Branch Profit and Loss Account
\n""",
"""Q21 Which of the following serves the same purpose as a Trading Account?
A Branch Adjustment Account
B Goods sent to Branch Account
C Branch Stock Account
D Branch Debtors Account
\n""",
"""Q22 Profit expressed as proportion of cost price is known as
A gross profit
B profit mark-up
C profit margin
D profit percentage
\n""",
"""Q23 Mark-up on goods sent to branch offices are recorded in the books by crediting
A Stock Adjustment Account debitting Branch Stock Account
B Goods sent to Branch Account and debitting Branch Stock Account
C Branch Stock Account and debitting Stock Adjustment
D Cash account and crediting Branch Stock Account
\n""",
"""Q24 Cash stolen from branch takings, iss recorded in the Head Office books by debiting
A defalcations account and crediting Branch Stock Account
B mark-up Account and crediting defalcations account
C defalcations account and crediting Profit and Loss Account
D Cash Account and creditng Branch stock Account
\n""",
"""Q25 Use the following information to answer question 49Rent paid
31/12/89 ₦4,000 Rent owing
1/1/89 ₦500OIN NOW Rent owing
31/12/89 ₦300 The Rent for 1989 amount to
A ₦4,500
B ₦4,300
C ₦4,000
D ₦3,800
\n""",
"""Q26 A business marked up its cost by 50%. This would mean a gross profit of
A 33 1/3 % on the cost price
B 50 % on the selling price
C 66 2/3 % on the selling
D 66 2/3 % on the market price
\n""",]
    question = [

        Question(question_prompts[0], 'a'),
        Question(question_prompts[1], 'b'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'c'),
        Question(question_prompts[5], 'a'),
        Question(question_prompts[6], 'b'),
        Question(question_prompts[7], 'd'),
        Question(question_prompts[8], 'b'),
        Question(question_prompts[9], 'c'),
        Question(question_prompts[10], 'b'),
        Question(question_prompts[11], 'a'),
        Question(question_prompts[12], 'b'),
        Question(question_prompts[13], 'b'),
        Question(question_prompts[14], 'a'),
        Question(question_prompts[15], 'b'),
        Question(question_prompts[16], 'a'),
        Question(question_prompts[17], 'b'),
        Question(question_prompts[18], 'a'),
        Question(question_prompts[19], 'c'),
        Question(question_prompts[20], 'a'),
        Question(question_prompts[21], 'b'),
        Question(question_prompts[22], 'a'),
        Question(question_prompts[23], 'a'),
        Question(question_prompts[24], 'd'),
        Question(question_prompts[25], 'd'),
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
     print('your profile is',des,'\nyour percentage:',round((score/len(questions))*100,2),'%')
     if score >=40:
         print("\nyou passed the test🎉🎉👨‍🎓👨‍🎓👍\n")
     else:
         print("\nyou failed the test,go and read your book and try again😭☹👎\n")
    run_test(question)
    while play_again():
        Accounting_2018()
    print("""Accounting Concepts and Conventions enter year 2020,Cash Book, Bank Transactions and Reconciliation Statements
       enter year 2021

       """)
    year = input("enter your year")
    year = year.upper()
    if year == "2020":
        Accounting_2020()
    if year == "2021":
        Accounting_2021()
    if year == "NO":
        print("bye for now and see you when you are ready to take the tests.")