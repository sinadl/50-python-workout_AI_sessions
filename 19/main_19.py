import os
def passwd_to_dict(filename):
    output={}
    with open(filename) as f:
        for line in f:
            # skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
            one_line = line.strip()
            parts = one_line.split(':')
            if len(parts) < 3:
                continue
            username = parts[0]
            u_id = parts[2]
            output[username] = u_id
    
    return(output)
            
    
    



print(passwd_to_dict('/etc/passwd'))