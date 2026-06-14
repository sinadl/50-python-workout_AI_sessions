import os
import arrow

directory = input("Enter directory: ")

for filename in os.listdir(directory):
    print(filename)
    
    modified_time = os.stat(directory).st_mtime
    print(arrow.get(modified_time).humanize())


