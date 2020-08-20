from random import shuffle
people = ['Ian', 'Kevin', 'Carl', 'Veronica', 'Daniel', 'Christian', 'Sean', 'Frank', 'Phillip', 'Fiona','kek']
number_of_teams = 3
number_people = len(people)
peapol_in_teams = round(len(people)/number_of_teams)
shuffle(people)
teams = [people[i:i+peapol_in_teams] for i in range(0, number_people, peapol_in_teams)]
del people
list2 = teams
i=0
while len(list2) > number_of_teams:
    teams[i].append(teams[-1][-1])
    i =+ 1
    del teams[-1][-1]
    list2 = [x for x in teams if x != []]
del i
del number_of_teams
del teams
del peapol_in_teams
print(list2)
