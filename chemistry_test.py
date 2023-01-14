from ChemistryApp import*
print(""" enter the available year from these years 
2020, 2019, 2018, 2017, 2016, 2015, 2014 , 
2013 """)
year = input("enter your year")
year = year.upper()
if year =="2020":
    Chemistry_2020()
if year =="2019":
    Chemistry_2019()
if year =="2018":
    Chemistry_2018()
if year =="2017":
    Chemistry_2017()
if year =="2016":
    Chemistry_2016()
if year =="2015":
    Chemistry_2015()
if year =="2014":
    Chemistry_2014()
if year =="2013":
    Chemistry_2013()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")