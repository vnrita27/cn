def byte_stuffing(data):
    s = ""
    for ch in data:
        if ch == '~':   # Frame delimiter
            s += '}' + '~'
        elif ch == '}':  # Escape character
            s += '}' + '}'
        else:
            s += ch
    return s


def byte_unstuffing(stuffed_data):
    us = ""
    i = 0
    while i < len(stuffed_data):
        if stuffed_data[i] == '}':
            # Next character is either ~ or }
            i += 1
            us += stuffed_data[i]
        else:
            us += stuffed_data[i]
        i += 1
    return us


# Example usage:
data = "Hello~World}Test~"
print("Original Data: ", data)
stuffed_data = byte_stuffing(data)
print("Byte Stuffed: ", stuffed_data)
unstuffed_data = byte_unstuffing(stuffed_data)
print("Byte Unstuffed: ", unstuffed_data)
