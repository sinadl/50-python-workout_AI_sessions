def reverse_file(input_file, output_file):

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:

        for line in infile:
            # remove newline, reverse content, then add newline back
            reversed_line = line.rstrip("\n")[::-1]

            outfile.write(reversed_line + "\n")
            
reverse_file("24/input.txt", "24/output.txt")