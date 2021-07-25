values = [
['*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*'],
['*','*','*','x','x','x','*','*'],
['*','*','*','x','x','x','*','*'],
['*','*','*','*','x','*','*','*'],
['*','*','*','x','*','*','*','*'],
['*','*','*','*','*','*','*','*']
]

def check_pattern(data):
    data_length = len(data)
    for i in range(1,data_length-1):
        for index,j in enumerate(data[i]):
            if j == 'x':
                conditions = [                       
                        data[i][index-1] == 'x',
                        data[i][index+1] == 'x',
                        data[i+1][index] == 'x',
                        data[i-1][index] == 'x'
                        ]
                if all(conditions):
                    return True
                
    
    return False
        
        
print(check_pattern(values))
