from AccountingApp import*
print("""Accounting Concepts and Conventions enter year 2020,Cash Book, Bank Transactions and Reconciliation Statements
enter year 2021,Company Accounts=2019,Departmental and Branch Accounts=2018

""")
year = input("enter your year")
year = year.upper()
if year == "2020":
    Accounting_2020()
if year =="2021":
    Accounting_2021()
if year =="2019":
    Accounting_2019()
if year =="2018":
    Accounting_2018()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")