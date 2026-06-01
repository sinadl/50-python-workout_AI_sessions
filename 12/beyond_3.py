import collections

def count_shells(filename='/etc/passwd'):
    shell_counts = {}

    try:
        with open(filename, 'r') as f:
            for line in f:
                if not line.strip() or line.startswith('#'):
                    continue
                
                parts = line.strip().split(':')
                shell = parts[-1]

                if shell in shell_counts:
                    shell_counts[shell] += 1
                else:
                    shell_counts[shell] = 1

 
        sorted_shells = sorted(shell_counts.items(), key=lambda x: x[1], reverse=True)

        for shell, count in sorted_shells:
            print(f"{shell}: {count}")

    except FileNotFoundError:
        print(f"Error: {filename} not found. This script requires a Unix-like system.")

if __name__ == "__main__":
    count_shells()
