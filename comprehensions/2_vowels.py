vowels = {'a', 'o', 'u', 'e', 'i'}

text = input()

result = [ch for ch in text if ch.lower() not in vowels]
print(''.join(result))
