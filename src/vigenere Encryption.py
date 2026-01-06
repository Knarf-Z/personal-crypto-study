key = input('please write down the key:').lower()
plain = input('please write down the plain:').lower()

cipher = ''
if len(key) < len(plain):
    times = len(plain) // len(key) + 1
    key = key * times

key = key[:len(plain)]
i = 0
for j in range(len(plain)):
    shift = ord(key[i]) - ord('a')
    cipher += chr((ord(plain[j]) - ord('a') + shift) % 26 + ord('a'))
    i += 1

print(cipher)
