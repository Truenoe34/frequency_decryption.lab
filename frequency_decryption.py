import sys
import collections

# Зчитуємо весь вхідний текст
encrypted_text = sys.stdin.read()
if encrypted_text.endswith('\n'):
    encrypted_text = encrypted_text[:-1]

def decrypt(text, s):
    res = []
    for char in text:
        if 'a' <= char <= 'z':
            res.append(chr((ord(char) - ord('a') - s) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            res.append(chr((ord(char) - ord('A') - s) % 26 + ord('A')))
        else:
            res.append(char)
    return "".join(res)

# Шукаємо зсув, за якого найчастішою літерою в розшифрованому тексті стане 'E'
best_shift = 0
max_e_count = -1

for s in range(26):
    candidate = decrypt(encrypted_text, s)
    # Рахуємо, скільки разів літера 'e' (або 'E') з'являється у розшифрованому варіанті
    e_count = candidate.lower().count('e')
    if e_count > max_e_count:
        max_e_count = e_count
        best_shift = s

print(decrypt(encrypted_text, best_shift))
