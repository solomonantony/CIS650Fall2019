data = [{'Customer':'Jostens Inc', 'Q1':200, 'Q2':230, 'Q3':300},
        {'Customer':'ADOLFO   RODRIGUEZ', 'Q1':120, 'Q2':320, 'Q3':200},
        {'Customer':'Wired Rhino, Inc.', 'Q1':400, 'Q2':150, 'Q3':90},
        {'Customer':'Spotify USA Inc', 'Q1':500, 'Q2':210, 'Q3':30}]

# print custonmer with highest Q1
highestQ1 = 0
for dataLine in data:
    if dataLine['Q1'] > highestQ1:
        highestQ1 = dataLine['Q1'] 
        highestQ1Customer = dataLine['Customer']
print(f'Highest Q1 customer is {highestQ1Customer}')

# print custonmer with highest Q2
highestQ2 = 0
for dataLine in data:
    if dataLine['Q2'] > highestQ2:
        highestQ2 = dataLine['Q2'] 
        highestQ2Customer = dataLine['Customer']
print(f'Highest Q2 customer is {highestQ2Customer}')

# print custonmer with highest Q3
highestQ3 = 0
for dataLine in data:
    if dataLine['Q3'] > highestQ3:
        highestQ3 = dataLine['Q3'] 
        highestQ3Customer = dataLine['Customer']
print(f'Highest Q3 customer is {highestQ3Customer}')


            