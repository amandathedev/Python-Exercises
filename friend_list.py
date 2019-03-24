people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]

# Hannah
people[0] = people[0] + "h"
#Jeffrey
people[4] = people[4][3:]
people[4] = "Je" + people[4]
#Aparna
people[-1] = people[-1].capitalize()

print(people)