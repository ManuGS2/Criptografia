def KSA(key):
	S = list(range(256))
	j = 0
	for i in range(256):
		j = (j + S[i] + ord(key[i%len(key)])) % 256
		S[i], S[j] = S[j], S[i]

	return S

def PRGA(S, message):
	i, j = 0, 0
	output = []
	while message:
		i = (i + 1) % 256
		j = (j + S[i] )% 256
		S[i], S[j] = S[j], S[i]
		k = S[(S[i] + S[j]) % 256]
		output.append(k ^ ord(message[0]))
		message = message[1:]

	return output

def showCipher(text):
	output = ''
	for b in text:
		hexa = hex(b).split('x')[-1].upper()
		if len(hexa) == 1:
			hexa = '0' + hexa
		output += hexa
	return output


key = input() 
message = input()

S = KSA(key)
cipher = PRGA(S, message)

print(showCipher(cipher))
