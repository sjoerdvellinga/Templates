# Import Package
from cryptography.fernet import Fernet

# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
f = Fernet(key)
# print key for debugging purpose only. 
# Not in real code
print(key)

# String to encrypt
plaintext = b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='

# Encrypt
ciphertext = f.encrypt(plaintext)
# print encrypted plaintext
print(ciphertext)

# Decrypt
decryptedtext = f.decrypt(ciphertext)
# print plaintext (after decryption)
print(decryptedtext)