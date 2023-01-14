from GeneraltestApp import*
print("""
you have biology , english , chemistry and physics
for biology enter year 1980 for English enter year 1981 for Chemistry enter year 1982 for Physics enter year 1983
for biology enter year 1984 for biology enter year 1985 for physics enter year 1986 for biology enter year 1987 for biology enter year 1988
for English enter year 1990 for Physics enter year 1991 for Physics enter year 1992 for Physics enter year 1993 
for Physics enter year 1994 for Physics enter year 1995
if you decide not to do again enter no""")
year = input("enter your year")
year = year.upper()
if year == "1980":
    biology_1980()
if year == "1981":
    English_1981()
if year == "1982":
    Chemistry_1982()
if year == "1983":
    Physics_1983()
if year == "1984":
    biology_1984()
if year == "1985":
    biology_1985()
if year == "1986":
    Physics_1986()
if year == "1987":
    biology_1987()
if year == "1988":
    biology_1988()
if year == "1989":
    Chemistry_1989()
if year == "1990":
    English_1990()
if year == "1991":
    Physics_1991()
if year == "1992":
    Physics_1992()
if year == "1993":
    Physics_1993()
if year == "1994":
    Physics_1994()
if year == "1995":
    Physics_1995()
if year == "NO":
    print("bye for now and see you when you are ready to take the tests.")




