import os,re
def sum_int(filename):
    output = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            match = re.search(r'\d+', words[0])
            if match:
                output += int(match.group())
            
    
    return(output)
            
            



path = os.path.join(os.path.dirname(__file__), "textfile.txt")
print(sum_int(path))