data = [{'Customer':'Jostens Inc', 'Q1':200, 'Q2':230, 'Q3':300},
        {'Customer':'ADOLFO   RODRIGUEZ', 'Q1':120, 'Q2':320, 'Q3':200},
        {'Customer':'Wired Rhino, Inc.', 'Q1':400, 'Q2':150, 'Q3':90},
        {'Customer':'Spotify USA Inc', 'Q1':500, 'Q2':210, 'Q3':30}]

def returnHighest(returnField, valueField, dataList):
    highestValue = 0
    for dataLine in dataList:
        if dataLine[valueField] > highestValue:
            highestValue = dataLine[valueField]
            returnValue = dataLine[returnField]
    return returnValue
    
for q in ['Q1', 'Q2', 'Q3']:
    print(f'Highest {q} customer is {returnHighest("Customer", q, data)}')
    
