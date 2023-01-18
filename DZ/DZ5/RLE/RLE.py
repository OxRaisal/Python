def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1   
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
    
encodet_val = rle_encode('AAAAABBBBBBBCCDFFF')
print(encodet_val)

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    
    return decode

decodet_val = rle_decode('3A1b7C2d4F')
print(decodet_val)