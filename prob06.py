length = input()
text = input()

ciphertext = list("FGHIJKLMNOPQRSTUVWXYZABCDE ")
plaintext = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

cipher = {ciphertext[i]: plaintext[i] for i in range(len(ciphertext))}

decoded = ""
for letter in text:
    decoded += cipher[letter]

print(decoded)