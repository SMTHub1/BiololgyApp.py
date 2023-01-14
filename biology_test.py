from BiologyApp import*
print("""
the years available are 2020,2019,2018,2017,2016
----2015,2014,2013 and 2012
enter any of this year and let go there ! 
you can do it """)
year = input("enter your year")
year = year.upper()
if year =="2020":
    Biology_2020()
if year =="2019":
    Biology_2019()
if year =="2018":
    Biology_2018()
if year =="2017":
    Biology_2017()
if year =="2016":
    Biology_2016()
if year =="2015":
    Biology_2015()
if year =="2014":
    Biology_2014()
if year =="2013":
    Biology_2013()
if year =="2012":
    Biology_2012()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")