from utils.pdu_utils import *


def test_big_endian_for_max_signal_values_1():

	payload = [0x00] * 10

	#signal    length 14 start bit 13  ( MAX = 0x3FFF,    MIN = 0x00)
	#signal    length 7  start bit 20  ( MAX = 0x7F ,     MIN = 0x00 )
	#signal    length 18  start bit 38 ( MAX = 0x3FFFF,   MIN = 0x00 )
	#signal    length 3  start bit 41  ( MAX = 0x7,       MIN = 0x00 )
	#signal    length 2  start bit 43  ( MAX = 0x03,      MIN = 0x00 )

	endian_byte_order(payload, 13, 14,[0x3F, 0xFF], Endianness.BIG )
	endian_byte_order(payload, 20, 7, [0x7F] , Endianness.BIG) 
	endian_byte_order(payload, 38, 18, [0x03, 0xFF, 0xFF], Endianness.BIG) 
	endian_byte_order(payload, 41, 3, [0x7], Endianness.BIG) 
	endian_byte_order(payload, 43, 2, [0x03], Endianness.BIG) 

	assert payload == [0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_max_signal_values_2():
    
	#signal    length 6  start bit 5   ( MAX = 0x3F, MIN = 0x00 )
	#signal    length 11  start bit 16 ( MAX = 0x7FF , MIN = 0x00 )
	#signal    length 5  start bit 21  ( MAX = 0x1F , MIN = 0x00 )
	#signal    length 19  start bit 40 ( MAX = 0x7FFFF, MIN = 0x00 )
	#signal    length 13  start bit 53 ( MAX =  0x1FFF, MIN = 0x00 )
	#signal    length 6  start bit 59  ( MAX =  0x3F, MIN = 0x00 )
    
	payload = [0] * 10

	endian_byte_order(payload, 5, 6,[0x3F], Endianness.BIG ) # start bit 0 length 11 data = 
	endian_byte_order(payload, 16, 11, [0x7, 0xFF] , Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 21, 5, [0x1F], Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 40, 19, [0x7, 0xFF, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 53, 13, [0x1F, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 59, 6, [0x3F], Endianness.BIG) # start bit 0 length 11 data = 

	assert payload == [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x0, 0x0]

def test_big_endian_for_max_signal_values_3():

	#	signal    length 7  start bit 6   ( MAX =  0x7F, MIN = 0x00 )
	#	signal    length 5  start bit 11  ( MAX =  0x1F, MIN = 0x00 )
	#	signal    length 9  start bit 20  ( MAX =  0x1FF, MIN = 0x00 )
	#	signal    length 3  start bit 23  ( MAX =  0x7, MIN = 0x00 )
	#	signal    length 11  start bit 34 ( MAX  = 0x7FF, MIN = 0x00 )
    
	payload = [0] * 10

	endian_byte_order(payload, 6, 7,[0x7F], Endianness.BIG ) # start bit 0 length 11 data = 
	endian_byte_order(payload, 11, 5, [0x1F] , Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 20, 9, [0x1, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 23, 3, [0x7], Endianness.BIG) # start bit 0 length 11 data = 
	endian_byte_order(payload, 34, 11, [0x7, 0xFF], Endianness.BIG) # start bit 0 length 11 data = 

	assert payload == [0xff, 0xff, 0xff, 0xff, 0xE0, 0x0, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_variable_signal_values_4():
    
    #signal    length 14 start bit 13  ( MAX = 0x3FFF,    MIN = 0x00)
	#signal    length 7  start bit 20  ( MAX = 0x7F ,     MIN = 0x00 )
	#signal    length 18  start bit 38 ( MAX = 0x3FFFF,   MIN = 0x00 )
	#signal    length 3  start bit 41  ( MAX = 0x7,       MIN = 0x00 )
	#signal    length 2  start bit 43  ( MAX = 0x03,      MIN = 0x00 )
    
	payload = [0] * 10

	endian_byte_order(payload, 13, 14,[0x2F, 0x97], Endianness.BIG ) # value 12183 
	endian_byte_order(payload, 20, 7, [0x6B] , Endianness.BIG) # value 107
	endian_byte_order(payload, 38, 18, [0x03, 0x18, 0xBF], Endianness.BIG) #  value 202943
	endian_byte_order(payload, 41, 3, [0x3], Endianness.BIG) #  value 3
	endian_byte_order(payload, 43, 2, [0x01], Endianness.BIG) #  value 1
	
	assert payload == [0xbe, 0x5f, 0x5e, 0x31, 0x7e, 0xd0, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_variable_signal_values_5():
    
    #signal    length 6  start bit 5   ( MAX = 0x3F, MIN = 0x00 )
	#signal    length 11  start bit 16 ( MAX = 0x7FF , MIN = 0x00 )
	#signal    length 5  start bit 21  ( MAX = 0x1F , MIN = 0x00 )
	#signal    length 19  start bit 40 ( MAX = 0x7FFFF, MIN = 0x00 )
	#signal    length 13  start bit 53 ( MAX =  0x1FFF, MIN = 0x00 )
	#signal    length 6  start bit 59  ( MAX =  0x3F, MIN = 0x00 )
    
	payload = [0] * 10

	endian_byte_order(payload, 5, 6,[0x37], Endianness.BIG ) # value  55
	endian_byte_order(payload, 16, 11, [0x4, 0x3D] , Endianness.BIG) # value 1085 
	endian_byte_order(payload, 21, 5, [0x1D], Endianness.BIG) #  value 29
	endian_byte_order(payload, 40, 19, [0x6, 0x9A, 0xD3], Endianness.BIG) #  value 432851 
	endian_byte_order(payload, 53, 13, [0xC, 0xD5], Endianness.BIG) #  value 3285
	endian_byte_order(payload, 59, 6, [0x38], Endianness.BIG) #  value 56

def test_big_endian_for_variable_signal_values_6():

	#	signal    length 7  start bit 6   ( MAX =  0x7F, MIN = 0x00 )
	#	signal    length 5  start bit 11  ( MAX =  0x1F, MIN = 0x00 )
	#	signal    length 9  start bit 20  ( MAX =  0x1FF, MIN = 0x00 )
	#	signal    length 3  start bit 23  ( MAX =  0x7, MIN = 0x00 )
	#	signal    length 11  start bit 34 ( MAX  = 0x7FF, MIN = 0x00 )
    
	payload = [0] * 10

	endian_byte_order(payload, 6, 7,[0x4D], Endianness.BIG ) # value 77
	endian_byte_order(payload, 11, 5, [0x10] , Endianness.BIG) # value 16
	endian_byte_order(payload, 20, 9, [0x1, 0xBC], Endianness.BIG) # value 444
	endian_byte_order(payload, 23, 3, [0x2], Endianness.BIG) # value 2
	endian_byte_order(payload, 34, 11, [0x4, 0x08], Endianness.BIG) # value 1032



def test_small_endian_for_max_signal_values_7():

	# big_endian_byte_order(a, 0, 11,[0x00, 0x20], Endianness.SMALL) # start bit 0 length 11 data = 
	# big_endian_byte_order(a, 11, 4, [0x09], Endianness.SMALL) # start bit 0 length 11 data = 
	# big_endian_byte_order(a, 15, 13, [0x0F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	# big_endian_byte_order(a, 28, 15, [0x7D, 0x55], Endianness.SMALL) # start bit 0 length 11 data = 
	# big_endian_byte_order(a, 43, 5, [0x00, 0x1D], Endianness.SMALL) # start bit 0 length 11 data =
    
	payload = [0] * 10

	endian_byte_order(payload, 0, 4,[0xF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 4, 7, [0x7F], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 11, 11, [0x7, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 22, 2, [0x3], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 24, 5, [0x1F], Endianness.SMALL) # start bit 0 length 11 data = 

	assert payload == [0xff, 0xff, 0xff, 0x1f, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]	

def test_small_endian_for_max_signal_values_8():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 5,[0x1F], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 5, 11, [0x7, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 16, 8, [0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 24, 14, [0x3F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 38, 8, [0xFF], Endianness.SMALL) # start bit 0 length 11 data = 

	assert payload == [0xff, 0xff, 0xff, 0xff, 0xff, 0x3f, 0x0, 0x0, 0x0, 0x0]	

def test_small_endian_for_max_signal_values_9():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 3,[0x7], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 3, 10, [0x3, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 13, 10, [0x3, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 23, 13, [0x1F, 0xFF], Endianness.SMALL) # start bit 0 length 11 data = 
	
	assert payload == [0xff, '0xff, 0xff, 0xff, 0xf, 0x0, 0x0', 0x0, 0x0, 0x0]


def test_small_endian_for_max_signal_values_9():

	payload = [0x00] * 10
	
	endian_byte_order(payload, 0, 4,[0xB], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 4, 7, [0x69], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 11, 11, [0x4, 0x08], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 22, 2, [0x2], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 24, 5, [0x1A], Endianness.SMALL) # start bit 0 length 11 data = 

	assert payload == [0x9b, 0x46, 0xa0, 0x1a, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]


def test_small_endian_for_max_signal_values_10():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 5,[0x17], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 5, 11, [0x3, 0xF2], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 16, 8, [0xCD], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 24, 14, [0x3B, 0xB5], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 38, 8, [0x20], Endianness.SMALL) # start bit 0 length 11 data = 

	assert payload == [0x57, 0x7e, 0xcd, 0xb5, 0x3b, 0x8, 0x0, 0x0, 0x0, 0x0]



def test_small_endian_for_max_signal_values_11():

	payload = [0x00] * 10


	endian_byte_order(payload, 0, 3,[0x3], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 3, 10, [0x3, 0x87], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 13, 10, [0x3, 0xE9], Endianness.SMALL) # start bit 0 length 11 data = 
	endian_byte_order(payload, 23, 13, [0x7, 0x1B], Endianness.SMALL) # start bit 0 length 11 data = 

	assert payload == [0x3b, 0x3c, 0xfd, 0x8d, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_single_byte_signal_values_12():

	payload = [0x00] * 10

	endian_byte_order(payload, 2, 3,[3], Endianness.BIG) 
	endian_byte_order(payload, 11, 4, [10], Endianness.BIG) 
	endian_byte_order(payload, 20, 5, [25], Endianness.BIG)
	endian_byte_order(payload, 29, 6, [29], Endianness.BIG)
	endian_byte_order(payload, 38, 7, [60], Endianness.BIG)
	endian_byte_order(payload, 40, 1, [1], Endianness.BIG)
	
	assert payload == [0x60, 0xa0, 0xc8, 0x74, 0x78, 0x80, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_single_byte_signal_values_13():

	payload = [0x00] * 10

	endian_byte_order(payload, 2, 3, [5], Endianness.BIG) 
	endian_byte_order(payload, 11, 4, [12], Endianness.BIG) 
	endian_byte_order(payload, 16, 1, [1], Endianness.BIG)
	endian_byte_order(payload, 29, 6, [60], Endianness.BIG)
	endian_byte_order(payload, 36, 5, [29], Endianness.BIG)
	
	assert payload == [0xA0, 0xC0, 0x80, 0xF0, 0xE8, 0x00, 0x0, 0x0, 0x0, 0x0]

def test_big_endian_for_single_byte_signal_values_14():

	payload = [0x00] * 10

	endian_byte_order(payload, 1, 2, [2], Endianness.BIG) 
	endian_byte_order(payload, 14, 7, [120], Endianness.BIG) 
	endian_byte_order(payload, 19, 4, [11], Endianness.BIG)
	endian_byte_order(payload, 26, 3, [1], Endianness.BIG)
	
	assert payload == [0x80, 0xF0, 0xB0, 0x20, 0x00, 0x00, 0x0, 0x0, 0x0, 0x0]

def test_little_endian_for_single_byte_signal_values_15():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 3, [3], Endianness.SMALL) 
	endian_byte_order(payload, 8, 4, [14], Endianness.SMALL) 
	endian_byte_order(payload, 16, 7, [20], Endianness.SMALL)
	endian_byte_order(payload, 24, 5, [15], Endianness.SMALL)
	endian_byte_order(payload, 32, 6, [60], Endianness.SMALL)
	
	assert payload == [0x3, 0xE, 0x14, 0xF, 0x3C, 0x0, 0x0, 0x0, 0x0, 0x0]

def test_little_endian_for_single_byte_signal_values_16():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 3, [7], Endianness.SMALL) # 7
	endian_byte_order(payload, 8, 5, [31], Endianness.SMALL) # 31
	endian_byte_order(payload, 16, 2, [3], Endianness.SMALL) # 3
	endian_byte_order(payload, 24, 6, [63], Endianness.SMALL) # 63

	assert payload == [0x7, 0x1F, 0x3, 0x3F, 0x00, 0x0, 0x0, 0x0, 0x0, 0x0]

def test_little_endian_for_single_byte_signal_values_17():

	payload = [0x00] * 10

	endian_byte_order(payload, 0, 3, [6], Endianness.SMALL) # 7
	endian_byte_order(payload, 8, 5, [29], Endianness.SMALL) # 31
	endian_byte_order(payload, 16, 4, [14], Endianness.SMALL) # 15
	endian_byte_order(payload, 24, 5, [30], Endianness.SMALL) # 31
	endian_byte_order(payload, 32, 6, [61], Endianness.SMALL) # 63

	assert payload == [0x6, 0x1D, 0xE, 0x1E, 0x3D, 0x0, 0x0, 0x0, 0x0, 0x0]
	
