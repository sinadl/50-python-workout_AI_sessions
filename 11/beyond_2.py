def shell_users(filename='/etc/passwd'):
    shells = {}

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            parts = line.split(':')

            username = parts[0]
            shell = parts[-1]

            if shell not in shells:
                shells[shell] = []

            shells[shell].append(username)

    for shell in shells:
        shells[shell].sort()

    sorted_shells = sorted(shells.items(), key=lambda item: len(item[1]), reverse=True)

    for shell, users in sorted_shells:
        print(f"{shell}: {len(users)} users")
        print("  " + ", ".join(users))
