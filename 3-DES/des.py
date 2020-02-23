def keys_gen(key):
    # bits permutation of the key [0 1 2 3 4 5 6 7 8 9] > [2 4 1 6 3 9 0 8 7 5]
    key[0],key[1],key[2],key[3],key[4],key[5],key[6],key[7],key[8],key[9] = key[2],key[4],key[1],key[6],key[3],key[9],key[0],key[8],key[7],key[5]

    # Circular shifting to the left on each half for first subkey
    key.insert(4, key.pop(0))
    key.insert(9, key.pop(5))

    # Index for first subkey [5 2 6 3 7 4 9 8] 
    subkey1 = list()
    subkey1.append(key[5])
    subkey1.append(key[2])
    subkey1.append(key[6])
    subkey1.append(key[3])
    subkey1.append(key[7])
    subkey1.append(key[4])
    subkey1.append(key[9])
    subkey1.append(key[8])
    
    # Circular shifting to the left on each half for second subkey
    key.insert(4, key.pop(0))
    key.insert(4, key.pop(0))
    key.insert(9, key.pop(5))
    key.insert(9, key.pop(5))

    # Index for second subkey [5 2 6 3 7 4 9 8] 
    subkey2 = list()
    subkey2.append(key[5])
    subkey2.append(key[2])
    subkey2.append(key[6])
    subkey2.append(key[3])
    subkey2.append(key[7])
    subkey2.append(key[4])
    subkey2.append(key[9])
    subkey2.append(key[8])

    return subkey1, subkey2

def mixing(key,text):
    # S-boxes
    S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

    # Text's expansion [0 1 2 3] > [3 0 1 2 1 2 3 0]
    expan = text.copy()
    expan.extend(text)
    expan.insert(0,expan.pop(3))
    expan.append(expan.pop(4))

    # text-expanded XOR key
    xor = [x ^ y for x,y in zip(expan,key)]
    
    # S-boxes replacement and permutation
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    aux = list()
    aux += [int(x) for x in get_bin(S0[2*xor[0]+xor[3]][2*xor[1]+xor[2]],2)]
    aux += [int(x) for x in get_bin(S1[2*xor[4]+xor[7]][2*xor[5]+xor[6]],2)]
    aux[0],aux[1],aux[2],aux[3] = aux[1],aux[3],aux[2],aux[0]

    return aux

def simDES(plain,key1,key2):
    # bits permutation of plaintext [0 1 2 3 4 5 6 7] > [1 5 2 0 3 7 4 6]
    plain[0],plain[1],plain[2],plain[3],plain[4],plain[5],plain[6],plain[7] = plain[1],plain[5],plain[2],plain[0],plain[3],plain[7],plain[4],plain[6]

    # First round mixing function
    aux = mixing(key1,plain[4:])
    xor = [x ^ y for x,y in zip(aux,plain[:4])]
    plain = xor + plain[4:]

    # Switching both halves of the previous result
    plain = plain[4:] + plain[:4]

    # Second round mixing function
    aux = mixing(key2,plain[4:])
    xor = [x ^ y for x,y in zip(aux,plain[:4])]
    plain = xor + plain[4:]

    # Final inverse permutation [0 1 2 3 4 5 6 7] > [3 0 2 4 6 1 7 5]
    plain[0],plain[1],plain[2],plain[3],plain[4],plain[5],plain[6],plain[7] = plain[3],plain[0],plain[2],plain[4],plain[6],plain[1],plain[7],plain[5]

    return plain

opt, key, text = input(), input(), input()
key = [int(x) for x in list(key)]
text = [int(x) for x in list(text)]

# Keys generation
key1, key2 = keys_gen(key)

if opt == 'E':
    chiper = "".join([str(x) for x in simDES(text,key1,key2)])
    print(chiper)

elif opt == 'D':
    plain = "".join([str(x) for x in simDES(text,key2,key1)])
    print(plain)
