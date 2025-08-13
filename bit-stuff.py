def bit_stuffing(data):
    s = ""
    count = 0
    for bit in data:
        s += bit
        if bit == '1':
            count += 1
            if count == 5:
                # Insert a 0 after five consecutive 1's
                s += '0'
                count = 0
        else:
            count = 0
    return s


def bit_unstuffing(stuffed_data):
    us = ""
    count = 0
    i = 0
    while i < len(stuffed_data):
        bit = stuffed_data[i]
        us += bit
        if bit == '1':
            count += 1
            if count == 5:
                # Skip the next 0 bit
                i += 1
                count = 0
        else:
            count = 0
        i += 1
    return us


# Example usage:
data = "011111101111110"
print("Original Data: ", data)
stuffed_data = bit_stuffing(data)
print("Bit Stuffed: ", stuffed_data)
unstuffed_data = bit_unstuffing(stuffed_data)
print("Bit Unstuffed: ", unstuffed_data)

print()

def bit_s(data):
    s = ""
    c=0
    for el in data:
        s += el
        if el=='1':
            c+=1
        else:
            c=0
        if c==5:
            c=0
            s+="0"
        # print(s)
    return s


def bit_us(data):
    s = ""
    c =0 
    for el in data:
        if c==-1:
            c=0
            continue

        s += el

        if el == "1": c+=1
        else: c=0
        if c==5:
            c=-1   
        # print("s: ", s, "; c: ", c)    
    return s


data = "011111101111110"
print(data[:-1])
print("Original Data: ", data)
stuffed_data = bit_s(data)
print("Bit Stuffed: ", stuffed_data)
unstuffed_data = bit_us(stuffed_data)
print("Bit Unstuffed: ", unstuffed_data)
print("Original Data: ", data)