import os
def find_diff(filename):
    ip_list = set()
    with open(filename) as f:
        for line in f:
            parts = line.split()

            ip = parts[0]
            
            ip_list.add(ip)
    
    return(ip_list)
            
            



path = os.path.join(os.path.dirname(__file__), "logfiles.log")
print(find_diff(path))