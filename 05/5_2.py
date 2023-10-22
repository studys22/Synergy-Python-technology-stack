s = input("Input a string: ")
o = 0
i = 0
e = 0
a = 0
u = 0
d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

vowel = 0
consonant = 0

for c in s:
    if c in "aeiou":
        vowel += 1
        d[c] += 1
    else:
        consonant += 1

result = "Vowel: " + str(vowel) + "\nConsonant: " + str(consonant) + "\n"

for key, value in d.items():
    result += key + ": "
    result += "False" if value == 0 else str(value)
    result += "\n"

print(result)
