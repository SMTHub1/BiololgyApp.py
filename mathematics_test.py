from MathematicsApp import *
def play():
    for i in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
       year=input("""enter your between 2010, 2015, 
       2020, 2012, 2016, 2008,2011 ,2018,2009, 2014, 2013: """)
       if year=='2010':
          math_jamb_2010()
       elif  year == '2011':
           math_jamb_2011()
       elif year =="2013":
           math_jamb_2013()
       elif year == "2014":
           math_jamb_2014()
       elif year =="2015":
           math_jamb_2015()
       elif year =="2018":
            math_jamb_2018()
       elif year =="2020":
           math_jamb_2020()
       elif year =="2012":
           math_jamb_2012()
       elif year =="2016":
           math_jamb_2016()
       elif year =="2008":
           math_jamb_2008()
       elif year =="2009":
           math_jamb_2009()
       else:
           print('\ninvalid year\n')
       response=input('\nenter anything to continue or enter # to stop')
       if response=='#':
           break
play()