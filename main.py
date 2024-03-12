import hashlib
import random

def hashing (string):
    hash_obj = hashlib.sha256(string.encode())
    return hash_obj.hexdigest()

#1 hash de las transacciones
def hashTransactions (transacciones):
    hash_transactions =[]
    for transaccion in transacciones:
        hash_transaction = hashing(transaccion)

        hash_transactions += [hash_transaction]

    return (hash_transactions)

#2 Construir el árbol de merkle
def merkle (hash_transactions):

    if len(hash_transactions) == 1:
        return hash_transactions[0]

    new_hash_transactions = []
    tamano = len(hash_transactions)

    restar = 0
    if (tamano%2 == 1): restar = 1

    for i in range (0, tamano - restar, 2):
        new_hash = hashing(hash_transactions[i]+hash_transactions[i+1])
        new_hash_transactions += [new_hash]
        
    if restar: new_hash_transactions += [hash_transactions[-1]]
    
    return merkle (new_hash_transactions)

#3. realizar el "proof - of - work" del bloque
def minar(bloque, datos, anterior, dificultad):
    ceros = '0'*dificultad

    while True:
        nonce = str(random.randint(0,999999))

        transaccion = bloque + nonce + datos + anterior

        hash_obj = hashlib.sha256(transaccion.encode())
        hash_hex = hash_obj.hexdigest()

        if (ceros == hash_hex[:dificultad]):
            return nonce, hash_hex

# Bloque #1
transacciones = ['t1', 't2', 't3', 't4', 't5']
hash_transactions = hashTransactions(transacciones)
hash_tree = merkle (hash_transactions)

hash_block = minar('1', hash_tree, '0000000000000000000000000000000000000000000000000000000000000000', 4)
print(hash_block)

print (hash_tree)
