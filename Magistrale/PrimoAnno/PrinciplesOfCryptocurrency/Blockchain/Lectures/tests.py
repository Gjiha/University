import secrets # usata per generare bytes crittograficamente sicuri
import helper
from io import BytesIO
from transaction import TxOut

# Testing TxOut
value = secrets.token_bytes(4) + 4*b'\x00'
n = 515 # lunghezza script
script_len = helper.int2varint(n)
script_pk = secrets.token_bytes(n)

bs = value + script_len + script_pk
reader = BytesIO(bs)

tx_out = TxOut.parse(reader)

print(tx_out)