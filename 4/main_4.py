def hex_output():
    normal_number = 0
    hex_number = input('enter your hex number to convert:')
    for power,digit in  enumerate(reversed(hex_number)):
        normal_number += int(digit,16) * (16 ** power)
    print(normal_number)

hex_output()