from collections import defaultdict

States_Cities = defaultdict(list)
l = []

Cities_By_State = [('TN', 'Chennai'), ('KN', 'Bangalore'), ('TN', 'Madurai'), ('KN', 'Mysore'), ('AP', 'Tirupathi')
    , ('TN', 'Coimbatore'), ('AP', 'Nellore'), ('TN', 'Hosur'), ('KN', 'Coorg'), ('AP', 'Vijayawada'),
                   ('AP', 'Amalapuram')]
for state, city in Cities_By_State:
    States_Cities[state].append(city)

for state, city in States_Cities.iteritems():
    l.append((state, ','.join(city)))

print l
