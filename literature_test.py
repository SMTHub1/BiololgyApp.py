from LiteratureApp import*
print("the years available 2016,2018,2019 ")
year = input("enter your year")
year = year.upper()
if year == "2016":
    Literature_2016()
if year =="2018":
    Literature_2018()
if year =="2019":
    Literature_2019()
if year =="2011":
    literature_jamb_2011()
if year =="2015":
    literature_jamb_2015()
if year =="2014":
    literature_in_english_2014()
if year =="2017":
    literature_in_english_2017()
if year =="2020":
    literature_in_english_2020()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")
