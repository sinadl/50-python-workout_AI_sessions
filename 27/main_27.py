import random



def create_password(characters):
    def password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return "".join(output)

    return password


alpha_password = create_password('abcdef')
symbol_password = create_password('!@#$%')
print(alpha_password(5))
print(symbol_password(10))