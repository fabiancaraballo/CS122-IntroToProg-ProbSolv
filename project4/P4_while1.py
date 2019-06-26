# p4_while1.py
# Create a list of countries,
# then print each country on a new line
# find and fix the bugs
hint = "Enter name of country or 'quit': "
country_list = [ ]
country = ""
nation = "None"
while country != "quit":
 country = input(hint)
 nation = nation.title()
 country_list.append(country)
print()
print("Countries")
for country in range(len(country_list)):
 print(country_list[country])
print()
print("Finished")