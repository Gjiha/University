from Crypto.PublicKey import RSA
from hashlib import sha256

keyPair = RSA.generate(bits = 1024)

msg = b'Benvenuti a Priciples of Cryptocurrency Design - AA 25/26!'
msg_hash = int.from_bytes(sha256(msg).digest(), byteorder = "big")
msg_sig = pow(msg_hash, keyPair.d, keyPair.n )

print("Firma: ", hex(msg_sig))