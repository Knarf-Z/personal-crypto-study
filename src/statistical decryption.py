from collections import Counter
import re

cipher = ('JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRL'
          'OLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHL'
          'HLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGB'
          'ABHZQOCGFHX')
text = re.sub(r'[^A-Z]', '', cipher.upper())

# 单字频率
freq = Counter(text)
print("Top letters:", freq.most_common(10))

# IC
n = len(text)
ic = sum(v*(v-1) for v in freq.values()) / (n*(n-1))
print("len =", n, "IC =", ic)

from collections import Counter

bigrams = Counter(text[i:i+2] for i in range(len(text)-1))
trigrams = Counter(text[i:i+3] for i in range(len(text)-2))

print("Top bigrams:", bigrams.most_common(15))
print("Top trigrams:", trigrams.most_common(15))

