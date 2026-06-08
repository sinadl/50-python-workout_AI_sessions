import os
def response_ips(filename):
    codes = {}

    with open(filename) as f:
        for line in f:
            parts = line.split()

            ip = parts[0]
            code = parts[-2]

            if code not in codes:
                codes[code] = []

            codes[code].append(ip)

    return codes

path = os.path.join(os.path.dirname(__file__), "logfile.txt")
print(response_ips(path))
