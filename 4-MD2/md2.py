# S array that define the 0..255 permutation 
S = [
	41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
	19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
	76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
	138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
	245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
	148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
	39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
	181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
	150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
	112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
	96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
	85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
	234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
	129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
	8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
	203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
	166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
	31, 26, 219, 153, 141, 51, 159, 17, 131, 20]

def padding(msg):
	""" Padding of the message, append n bytes with n value to the message"""
	
	# Number of bytes to append
	if len(msg) == 0:
		n = 16
	else:
		n = 16 - len(msg)%16 if len(msg)%16 != 0 else 0

	# Append n bytes with valu n
	for i in range(n):
		msg.append(n)

	return msg

def checksum(padded_msg):
	""" Append checksum (C_i) to padded message """

	checksum = [0 for i in range(16)]
	L = 0
	for i in range(len(padded_msg)//16):
		for j in range(16):
			c = padded_msg[16*i+j]
			checksum[j] = checksum[j] ^ S[c^L]
			L = checksum[j]

	padded_msg += checksum

	return padded_msg

def digest(check_msg):
	"""Calculate the hash of the message"""

	X = [0 for i in range(48)]

	for i in range(len(check_msg)//16):
		for j in range(16):
			X[j+16] = check_msg[16*i+j]
			X[j+32] = X[j+16] ^ X[j]
		t=0
		for j in range(18):
			for k in range(48):
				t = X[k] ^ S[t]
				X[k] = t
			t = (t+j) % 256

	get_hex = lambda x, n: format(x, 'x').zfill(n)
	msg_dig = ''
	for i in range(16):
		msg_dig += get_hex(X[i],2)

	return msg_dig 

message = [ord(c) for c in input()]

print(message, len(message))
padded_message = padding(message)
print(padded_message, len(padded_message))
check_message = checksum(padded_message)
print(check_message, len(check_message))
message_digest = digest(check_message)
print(message_digest, len(message_digest))