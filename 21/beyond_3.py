import os 

path = os.path.join(os.path.dirname(__file__), "access.log")
output = {}
with open(path,'r') as f:
    for line in f:
        response = line.split()
        code = response[-2]
        
        output[code] = output.get(code,0) + 1
        
for code,count in sorted(output.items()):
    print(f'{code}:{count}')