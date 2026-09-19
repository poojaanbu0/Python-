import json
import os 
print(os.getcwd())
filename = "users.json"

file = open(filename,"w")
file.write('[{"name":"pooja","num":400},{"name":"pooj","num":203},{"name":"poa","num":4}]')
file.close()

file = open(filename,"r")
data = json.loads(file.read())

for i in range(len(data)):
   data[i]['num'] +=50
print(data)

with open(filename,'w') as f:
   json.dump(data, f, indent = 4)
print(type(filename))

# with open(filename) as f:
#    print(f.read())

#with open()


