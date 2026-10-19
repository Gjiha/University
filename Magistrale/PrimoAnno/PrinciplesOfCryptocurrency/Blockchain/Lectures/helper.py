from hashlib import sha256
from datetime import datetime
from io import BytesIO
from configparser import ConfigParser


def hash256(byte_string):
    return sha256(sha256(byte_string).digest()).digest()

def now():
    return int(datetime.now().timestamp()).to_bytes(4, 'big')

def varint2int(reader):
    first = int.from_bytes(reader.read(1))
    if first <= 252:
        return first
    elif first == 253:
        return int.from_bytes(reader.read(2)[::-1])
    elif first == 254:
        return int.from_bytes(reader.read(4)[::-1])
    elif first == 255:
        return int.from_bytes(reader.read(8)[::-1])
    
def int2varint(n):
    if n < 0 or n >= 2**64:
        return None
    if n <= 252:
        return n.to_bytes(1, byteorder='little')
    if n < 2**16:
        return int(253).to_bytes(1, byteorder='little') + n.to_bytes(2, byteorder='little')
    if n < 2**32:
        return int(254).to_bytes(1, byteorder='little') + n.to_bytes(4, byteorder='little')
    if n < 2**64:
        return int(255).to_bytes(1, byteorder='little') + n.to_bytes(8, byteorder='little')
    
def opcodes(fname: str):
    config = ConfigParser()
    config.read(fname)
    return {int(config['OPCODES'][code], 16):code for code in config['OPCODES']}

    
if __name__ == '__main__':
    # h = 'fd0302'
    # reader = BytesIO(bytes.fromhex(h))
    # print(varint2int(reader))

    # print(int2varint(515))

    print(opcodes("opcodes.cfg"))