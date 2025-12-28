text = input('please write a message: ')
text = text.lower()
for c in text:
    if 'a' <= c <= 'z':
        c2 = chr((ord(c) - ord('a') - 3) % 26 + ord('a')).lower()
    else:
        c2 = c
    print(c2, end='')

