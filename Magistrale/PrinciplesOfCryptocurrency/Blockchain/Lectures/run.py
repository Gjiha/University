from block import Block
import helper

GENESIS = "0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c"

blk = Block.parse(bytes.fromhex(GENESIS))

print(blk)
print(blk.hash().hex())
print()

height = 0
while True:
    blk.prev_hash = blk.hash()
    blk.bits = bytes.fromhex('1e02ffff')
    blk.timestamp = helper.now()
    height += 1
    tx = "PCD 25/26 block " + str(height) 
    blk.merkle_root = helper.hash256(tx.encode('utf-8'))
    i = 0
    blk.update_nonce(i)
    flag = blk.is_valid_target()
    while not flag:
        i += 1
        if i == 2**32:
            i = 0
            blk.timestamp = helper.now()
        blk.update_nonce(i)
        flag = blk.is_valid_target()

    print(blk)
    print(blk.hash().hex())
    print()
