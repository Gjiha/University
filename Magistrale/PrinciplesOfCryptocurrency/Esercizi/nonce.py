from hashlib import sha256

# nonce = "16114492071"
# text = 'Francesco ' + nonce

# print(sha256(text.encode('utf-8')).hexdigest())

# find = False
# i = 1
# while(not find):
#     for tempNonce in range(2**(i-1),2**i):
#         text = 'Francesco ' + str(tempNonce)
#         print(tempNonce)
#         hash = sha256(text.encode('utf-8')).hexdigest() 
#         if hash[0:9] == "000000000":
#             find = True
#             print(hash)
#     i += 1
        

from hashlib import sha256
from multiprocessing import Process, Value, cpu_count

def worker(start, step, found, result):
    nonce = start
    while not found.value:
        text = 'Ionut ' + str(nonce)
        h = sha256(text.encode('utf-8')).hexdigest()

        if h.startswith("0000000"):  # abbassa difficoltà per test
            found.value = True
            result.value = nonce
            print(f"\nTrovato! Nonce: {nonce}")
            print(f"Hash: {h}")
            break

        # stampa ogni tanto per debug
        if nonce % 1000000 == 0:
            print(f"Processo {start}: {nonce}")

        nonce += step


if __name__ == "__main__":
    num_processes = cpu_count()

    found = Value('b', False)   # boolean condiviso
    result = Value('i', 0)      # nonce trovato

    processes = []

    for i in range(num_processes):
        p = Process(target=worker, args=(i, num_processes, found, result))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    if found.value:
        print(f"\nNonce finale: {result.value}")