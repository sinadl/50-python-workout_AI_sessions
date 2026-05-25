def char_to_int(char):
    code = ord(char.lower())
    if 48 <= code <= 57:    # 0-9
        return code - 48
    elif 97 <= code <= 102: # a-f
        return code - 87
    else:
        return None 


def hex_output():
    normal_number = 0
    hex_number = input('enter your hex number to convert:')
    for power,digit in  enumerate(reversed(hex_number)):
        normal_number += char_to_int(digit) * (16 ** power)
    print(normal_number)

hex_output()