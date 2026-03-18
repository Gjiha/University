from Crypto.PublicKey import RSA
from hashlib import sha256

keyPair = RSA.generate(bits = 1024)

msg = b'Benvenuti a Principles of Cryptocurrency Design - AA 25 / 26 !'
msg_hash = int.from_bytes(sha256(msg).digest(), byteorder = 'big')
msg_sign  = pow(msg_hash, keyPair.d, keyPair.n)

print("firma: ", hex(msg_sign))