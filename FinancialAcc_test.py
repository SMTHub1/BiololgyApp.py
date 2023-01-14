from FinancialAccApp import*
print("""the years available 2016,2017,2018,
        2020,2015, 2014, 2012, 2010, 2011, 2019
        2013""")
year = input("enter your year")
year = year.upper()
if year == "2016":
    FinancialAcc_2016()
if year =="2017":
    FinancialAcc_2017()
if year =="2018":
    financial_accounting_2018()
if year =="2020":
    FinancialAcc_2020()
if year =="2015":
    FinancialAcc_2015()
if year =="2014":
    FinancialAcc_2014()
if year =="2012":
    FinancialAcc_2012()
if year =="2010":
    FinancialAcc_2010()
if year =="2011":
    FinancialAcc_2011()
if year =="2019":
    accounting_2019()
if year =="2013":
    financial_accounting_2013()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")