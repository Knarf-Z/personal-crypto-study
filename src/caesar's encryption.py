text = input('Please enter a message: ').upper()
for c in text:
    c2 = chr((ord(c) - ord('A') + 3) % 26 + ord('A'))
    print(c2, end='')