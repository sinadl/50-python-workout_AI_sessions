import os
def find_diff(filename):
    ip_list = set()
    code_list = set()
    with open(filename) as f:
        for line in f:
            parts = line.split()

            ip = parts[0]
            code = parts[8]
            
            ip_list.add(ip)
            code_list.add(code)
    
    return(code_list)
            
            



path = os.path.join(os.path.dirname(__file__), "logfiles.log")
print(find_diff(path))