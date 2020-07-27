import rsa
(pubkey, privkey) = '1'
message = b'1234567890'
print(pubkey)
# шифруем
crypto = rsa.encrypt(message, pubkey)
print(crypto)
#расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)



# Будет выведено: b'1a5abae9b195a4d1dbd2c79d9787841c2c68c39e507c3f26e89b2969eea8dac6'

def encode(key):
    imp=key
    imp_code=1
