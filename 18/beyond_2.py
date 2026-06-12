import os,re
def sum_int(filename):
    output = 0
    with open(filename) as f:
        for line in f:
            line_result = 0
            words = line.split()
            if len(words) > 1:
                match1 = re.search(r'\d+', words[0])
                match2 = re.search(r'\d+', words[1])
                if match1 and match2:
                    line_result = int(match2.group()) * int(match1.group())

                    output += line_result
    
    return(output)
            
            



path = os.path.join(os.path.dirname(__file__), "two_col.txt")
print(sum_int(path))