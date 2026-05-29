def url_encode_string(text):
    encoded_result = ""
    
    for char in text:
        if not char.isalnum():
            ascii_hex = hex(ord(char))[2:].upper()    
            encoded_result += f"%{ascii_hex}"
        else:
            encoded_result += char
            
    return encoded_result


sample_input = "Hello World! @2026"
encoded_output = url_encode_string(sample_input)

print(f"Original: {sample_input}")
print(f"Encoded:  {encoded_output}")
