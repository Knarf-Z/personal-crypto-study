ciphertext = input('Enter the ciphertext: ').lower()

for k in range(26):  # 0..25
    print(f'k={k}: ', end='')
    for ch in ciphertext:
        # if 'a' <= ch <= 'z':
        ch2 = chr((ord(ch) - ord('a') - k) % 26 + ord('a'))
        # else:
        #     ch2 = ch
        print(ch2, end='')
    print()
