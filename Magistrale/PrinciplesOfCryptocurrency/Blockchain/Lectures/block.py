from io import BytesIO 
import helper

class Block:

    def __init__(self, version, prev_hash, merkle_root, timestamp, bits, nonce):
        self.version = version #Versione del blocco
        self.prev_hash = prev_hash #Hash del blocco precedente
        self.merkle_root = merkle_root #Contenuto del blocco
        self.timestamp = timestamp #Instante di tempo in cui viene effettuato l'hash del blocco
        self.bits = bits #Target del blocco
        self.nonce = nonce #4 Byte aggiunti per trovare l'hash del blocco  

    @classmethod
    def parse(cls, byte_string): #Funzione che legge l'header di un blocco e lo spezza nelle sue componentistiche
        reader = BytesIO(byte_string)
        version = reader.read(4)
        prev_hash = reader.read(32)
        merkle_root = reader.read(32)
        timestamp = reader.read(4)
        bits = reader.read(4)
        nonce = reader.read(4)
        return cls(version[::-1], prev_hash[::-1], merkle_root[::-1], timestamp[::-1], bits[::-1], nonce[::-1])
    
    def serialize(self): #Ricompone l'header
        return self.version[::-1] + self.prev_hash[::-1] + self.merkle_root[::-1] + self.timestamp[::-1] + self.bits[::-1] + self.nonce[::-1]

    def hash(self):
        return helper.hash256(self.serialize())[::-1]
    
    def target(self): #Calcola il target partendo dai bits 
        return int.from_bytes(self.bits[1:], "big") * 256**(self.bits[0] - 3)
    
    def is_valid_target(self): #Controlla se l'hash sia inferiore al target
        return int.from_bytes(self.hash(), "big") <= self.target()

    def update_nonce(self, i):
        self.nonce = i.to_bytes(4, 'big')

    def __str__(self):
        out = dict()
        out['version'] = self.version.hex()
        out['prev_hash'] = self.prev_hash.hex()
        out['merkle_root'] = self.merkle_root.hex()
        out['timestamp'] = self.timestamp.hex()
        out['bits'] = self.bits.hex()
        out['nonce'] = int(self.nonce.hex(),16)
        return out.__str__()


if __name__ == '__main__':
    header = "00e0a323fd73cb833ac1b091f339b14cb320f98fa7756d31fe520100000000000000000093918fc1931493becee43e9ec9f4d12fbcb4e8815653163ea58ecffe8c4e6a361f9edc6984060217395b599f"
    blk = Block.parse(bytes.fromhex(header))
    print(blk)

    print(blk.hash())

    print(hex(blk.target()))

    print(blk.is_valid_target())


