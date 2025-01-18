import base64

# Encoding
input_string = input("ENTER THE STRING: ")
encoded_string = base64.b64encode(input_string.encode("utf-8")).decode("utf-8")
print(f"Encoded: {encoded_string}")

# Decoding
decoded_string = base64.b64decode(encoded_string).decode("utf-8")
print(f"Decoded: {decoded_string}")
