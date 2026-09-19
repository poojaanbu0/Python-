import json 

data ={
    'Student-id' : "S101" ,
    'Student_name': 'Ajay',
    'has_membership' : True
    }

with open('data.json', 'w') as f:
    json.dumps(data,f,indent = 4)

print(data)