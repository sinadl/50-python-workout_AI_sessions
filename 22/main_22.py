import csv,os

path = os.path.join(os.path.dirname(__file__), "passwd.txt")


def passwd_to_csv(input_file,output_file):
    with open(input_file) as f, open(output_file, 'w') as out_f:
        infile = csv.reader(f,delimiter=':')
        output = csv.writer(out_f,delimiter='\t')
        
        for item in infile:
            if len(item) > 1:
                output.writerow((item[0],item[2]))
                
passwd_to_csv(path,'22/output.txt')