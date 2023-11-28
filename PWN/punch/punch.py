import PyPunch

def decode_card(image_path):
    decoder = PyPunch.PunchCardDecoder()
    return decoder.decode_from_file(image_path)

image_path = "0.jpg"
decoded_text = decode_card(image_path)
print(decoded_text)
