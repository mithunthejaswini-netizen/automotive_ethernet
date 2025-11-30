from utils.pdu_utils import *

"""
['0xff', '0xff', '0xff', '0xff', '0xff', '0xf0', '0x0', '0x0', '0x0', '0x0']
['0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xf0', '0x0', '0x0']
['0xff', '0xff', '0xff', '0xff', '0xe0', '0x0', '0x0', '0x0', '0x0', '0x0']
['0xbe', '0x5f', '0x5e', '0x31', '0x7e', '0xd0', '0x0', '0x0', '0x0', '0x0']
['0xde', '0x1e', '0xf7', '0x4d', '0x69', '0xb3', '0x57', '0x80', '0x0', '0x0']
['0x9b', '0xd', '0xe2', '0x81', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']
"""

a = [0] * 10

#big_endian_2 
#signal    length 14 start bit 13  ( MAX = 0x3FFF,    MIN = 0x00)
#signal    length 7  start bit 20  ( MAX = 0x7F ,     MIN = 0x00 )
#signal    length 18  start bit 38 ( MAX = 0x3FFFF,   MIN = 0x00 )
#signal    length 3  start bit 41  ( MAX = 0x7,       MIN = 0x00 )
#signal    length 2  start bit 43  ( MAX = 0x03,      MIN = 0x00 )


big_endian_byte_order(a, 13, 14,[0x3F, 0xFF], Endianness.BIG )

big_endian_byte_order(a, 20, 7, [0x7F] , Endianness.BIG) 
big_endian_byte_order(a, 38, 18, [0x03, 0xFF, 0xFF], Endianness.BIG) 
big_endian_byte_order(a, 41, 3, [0x7], Endianness.BIG) 
big_endian_byte_order(a, 43, 2, [0x03], Endianness.BIG) 

print('*' * 100)
print([hex(value) for value in a])

    #big_endian_3
	#signal    length 6  start bit 5   ( MAX = 0x3F, MIN = 0x00 )
	#signal    length 11  start bit 16 ( MAX = 0x7FF , MIN = 0x00 )
	#signal    length 5  start bit 21  ( MAX = 0x1F , MIN = 0x00 )
	#signal    length 19  start bit 40 ( MAX = 0x7FFFF, MIN = 0x00 )
	#signal    length 13  start bit 53 ( MAX =  0x1FFF, MIN = 0x00 )
	#signal    length 6  start bit 59  ( MAX =  0x3F, MIN = 0x00 )

a = [0] * 10
big_endian_byte_order(a, 5, 6,[0x3F], Endianness.BIG ) # start bit 0 length 11 data = 
big_endian_byte_order(a, 16, 11, [0x7, 0xFF] , Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 21, 5, [0x1F], Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 40, 19, [0x7, 0xFF, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 53, 13, [0x1F, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 59, 6, [0x3F], Endianness.BIG) # start bit 0 length 11 data = 

print([hex(value) for value in a])

#   big_endian_4
#	signal    length 7  start bit 6   ( MAX =  0x7F, MIN = 0x00 )
#	signal    length 5  start bit 11  ( MAX =  0x1F, MIN = 0x00 )
#	signal    length 9  start bit 20  ( MAX =  0x1FF, MIN = 0x00 )
#	signal    length 3  start bit 23  ( MAX =  0x7, MIN = 0x00 )
#	signal    length 11  start bit 34 ( MAX  = 0x7FF, MIN = 0x00 )

a = [0] * 10
big_endian_byte_order(a, 6, 7,[0x7F], Endianness.BIG ) # start bit 0 length 11 data = 
big_endian_byte_order(a, 11, 5, [0x1F] , Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 20, 9, [0x1, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 23, 3, [0x7], Endianness.BIG) # start bit 0 length 11 data = 
big_endian_byte_order(a, 34, 11, [0x7, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 

print([hex(value) for value in a])


# --------------------------------------------------------------------------------------------

#big_endian_2 
#signal    length 14 start bit 13  ( MAX = 0x3FFF,    MIN = 0x00)
#signal    length 7  start bit 20  ( MAX = 0x7F ,     MIN = 0x00 )
#signal    length 18  start bit 38 ( MAX = 0x3FFFF,   MIN = 0x00 )
#signal    length 3  start bit 41  ( MAX = 0x7,       MIN = 0x00 )
#signal    length 2  start bit 43  ( MAX = 0x03,      MIN = 0x00 )

a = [0] * 10

big_endian_byte_order(a, 13, 14,[0x2F, 0x97], Endianness.BIG ) # value 12183 
big_endian_byte_order(a, 20, 7, [0x6B] , Endianness.BIG) # value 107
big_endian_byte_order(a, 38, 18, [0x03, 0x18, 0xBF], Endianness.BIG) #  value 202943
big_endian_byte_order(a, 41, 3, [0x3], Endianness.BIG) #  value 3
big_endian_byte_order(a, 43, 2, [0x01], Endianness.BIG) #  value 1

print([hex(value) for value in a])

    #big_endian_3
	#signal    length 6  start bit 5   ( MAX = 0x3F, MIN = 0x00 )
	#signal    length 11  start bit 16 ( MAX = 0x7FF , MIN = 0x00 )
	#signal    length 5  start bit 21  ( MAX = 0x1F , MIN = 0x00 )
	#signal    length 19  start bit 40 ( MAX = 0x7FFFF, MIN = 0x00 )
	#signal    length 13  start bit 53 ( MAX =  0x1FFF, MIN = 0x00 )
	#signal    length 6  start bit 59  ( MAX =  0x3F, MIN = 0x00 )

a = [0] * 10
big_endian_byte_order(a, 5, 6,[0x37], Endianness.BIG ) # value  55
big_endian_byte_order(a, 16, 11, [0x4, 0x3D] , Endianness.BIG) # value 1085 
big_endian_byte_order(a, 21, 5, [0x1D], Endianness.BIG) #  value 29
big_endian_byte_order(a, 40, 19, [0x6, 0x9A, 0xD3], Endianness.BIG) #  value 432851 
big_endian_byte_order(a, 53, 13, [0xC, 0xD5], Endianness.BIG) #  value 3285
big_endian_byte_order(a, 59, 6, [0x38], Endianness.BIG) #  value 56

print([hex(value) for value in a])

#   big_endian_4
#	signal    length 7  start bit 6   ( MAX =  0x7F, MIN = 0x00 )
#	signal    length 5  start bit 11  ( MAX =  0x1F, MIN = 0x00 )
#	signal    length 9  start bit 20  ( MAX =  0x1FF, MIN = 0x00 )
#	signal    length 3  start bit 23  ( MAX =  0x7, MIN = 0x00 )
#	signal    length 11  start bit 34 ( MAX  = 0x7FF, MIN = 0x00 )

a = [0] * 10
big_endian_byte_order(a, 6, 7,[0x4D], Endianness.BIG ) # value 77
big_endian_byte_order(a, 11, 5, [0x10] , Endianness.BIG) # value 16
big_endian_byte_order(a, 20, 9, [0x1, 0xBC], Endianness.BIG) # value 444
big_endian_byte_order(a, 23, 3, [0x2], Endianness.BIG) # value 2
big_endian_byte_order(a, 34, 11, [0x4, 0x08], Endianness.BIG) # value 1032

print([hex(value) for value in a])


#little endian 2

# big_endian_byte_order(a, 0, 11,[0x00, 0x20], Endianness.SMALL) # start bit 0 length 11 data = 
# big_endian_byte_order(a, 11, 4, [0x09], Endianness.SMALL) # start bit 0 length 11 data = 
# big_endian_byte_order(a, 15, 13, [0x0F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
# big_endian_byte_order(a, 28, 15, [0x7D, 0x55], Endianness.SMALL) # start bit 0 length 11 data = 
# big_endian_byte_order(a, 43, 5, [0x00, 0x1D], Endianness.SMALL) # start bit 0 length 11 data =

a = [0x00] * 10
big_endian_byte_order(a, 0, 4,[0xF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 4, 7, [0x7F], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 11, 11, [0x7, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 22, 2, [0x3], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 24, 5, [0x1F], Endianness.SMALL) # start bit 0 length 11 data = 
print([hex(item) for item in a])

#little endian 3

a = [0x00] * 10
big_endian_byte_order(a, 0, 5,[0x1F], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 5, 11, [0x7, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 16, 8, [0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 24, 14, [0x3F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 38, 8, [0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
print([hex(item) for item in a])

# little endian 4

a = [0x00] * 10
big_endian_byte_order(a, 0, 3,[0x7], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 3, 10, [0x3, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 13, 10, [0x3, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 23, 13, [0x1F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 

print([hex(item) for item in a])


# ---------------------------------------------------------------------------------------------------

a = [0x00] * 10
big_endian_byte_order(a, 0, 4,[0xB], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 4, 7, [0x69], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 11, 11, [0x4, 0x08], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 22, 2, [0x2], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 24, 5, [0x1A], Endianness.SMALL) # start bit 0 length 11 data = 
print([hex(item) for item in a])

#little endian 3

a = [0x00] * 10
big_endian_byte_order(a, 0, 5,[0x17], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 5, 11, [0x3, 0xF2], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 16, 8, [0xCD], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 24, 14, [0x3B, 0xB5], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 38, 8, [0x20], Endianness.SMALL) # start bit 0 length 11 data = 
print([hex(item) for item in a])

# little endian 4

a = [0x00] * 10
big_endian_byte_order(a, 0, 3,[0x3], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 3, 10, [0x3, 0x87], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 13, 10, [0x3, 0xE9], Endianness.SMALL) # start bit 0 length 11 data = 
big_endian_byte_order(a, 23, 13, [0x7, 0x1B], Endianness.SMALL) # start bit 0 length 11 data = 

print([hex(item) for item in a])

['0xff', '0xff', '0xff', '0x1f', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']
['0xff', '0xff', '0xff', '0xff', '0xff', '0x3f', '0x0', '0x0', '0x0', '0x0']
['0xff', '0xff', '0xff', '0xff', '0xf', '0x0', '0x0', '0x0', '0x0', '0x0']
['0x9b', '0x46', '0xa0', '0x1a', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']
['0x57', '0x7e', '0xcd', '0xb5', '0x3b', '0x8', '0x0', '0x0', '0x0', '0x0']
['0x3b', '0x3c', '0xfd', '0x8d', '0x3', '0x0', '0x0', '0x0', '0x0', '0x0']