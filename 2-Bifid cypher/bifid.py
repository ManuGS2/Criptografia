tableau = [ ['E','N','C','R','Y'],
			['P','T','A','B','D'],
			['F','G','H','I','K'],
			['L','M','O','Q','S'],
			['U','V','W','X','Z']]

def find_coordinates(msg):
	"""
		msg(str): cadena de caracteres a encontrar sus coordenadas
		ret (list(int)): Lista de enteros representando las coordenadas
	"""
	coord = []
	for char in msg:
		for i in range(len(tableau)):
			if char in tableau[i]:
				coord.append(i)
				coord.append(tableau[i].index(char))
				break
	return coord

def decrypt(msg_encrypted):
	"""
		msg_encrypted(str): Mensaje encriptado sin espacios
		ret (str): Mensaje desencriptado sin espacios
	"""
	coord = find_coordinates(msg_encrypted)

	msg_decrypted = ''
	for i in range(len(coord)//2):
		msg_decrypted += tableau[coord[i]][coord[i+len(coord)//2]]

	return msg_decrypted

def encrypt(msg):
	"""
		msg(str): Mensaje en claro con espacios
		ret (str): Mensaje encriptado sin espacios
	"""
	coord = find_coordinates(msg)
	msg_encrypted = ''
	for i in range(0,len(coord),4):
		msg_encrypted += tableau[coord[i]][coord[(i+2)%len(coord)]]

	for i in range(1+2*((len(coord)//2)%2),len(coord),4):
		msg_encrypted += tableau[coord[i]][coord[(i+2)%len(coord)]]

	return msg_encrypted

op = input()
if op == "DECRYPT":
	encrypted_msg = input()
	print(decrypt(encrypted_msg))

elif op == "ENCRYPT":
	msg = input()
	print(encrypt(msg))

#print(encrypt("MEET ME ON FRIDAY"))
#print(encrypt("TRAVELNORTHATONCE"))
#print(decrypt('PDRRNGBENOPNIAGGF'))
#print(encrypt('BRING ALL YOUR MONEY'))
#print(decrypt('PFGQRUQERQTFYFMGY'))