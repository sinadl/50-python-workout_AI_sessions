import os
from pathlib import Path

def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path,filename)

        try:
            for line in open(full_filename):
                yield line
        except OSError:
            
            pass
    
    
for one_line in all_lines(Path(__file__).parent):
    print(one_line)

