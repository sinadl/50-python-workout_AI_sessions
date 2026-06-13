shells = {}

with open("/etc/passwd", "r") as passwd_file:
    for line in passwd_file:
        fields = line.strip().split(":")

        username = fields[0]
        shell = fields[-1]

        if shell not in shells:
            shells[shell] = []

        shells[shell].append(username)

for shell, users in shells.items():
    print(shell)
    print("  Users:", ", ".join(users))