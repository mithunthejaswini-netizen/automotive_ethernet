import functools
import time
from collections import UserDict
from enum import Enum

class Endianness(Enum):
    BIG = 'big'
    SMALL = 'small'

class PduDict(UserDict):

    def __init__(
        self,
        *args,
        **kwargs
    ):

        self.no_pdu_sent = 0
        self.pdu_timestamp = 0.0

        super().__init__(
                        *args,
                        **kwargs
        )

    def received_pdu(self):
        pass

    def pdu_sent(self):
        self.no_pdu_sent+=1
        self.pdu_timestamp = time.time()


def check_valid_signal_range(add_signal_to_pdu):

    signal_indexes_range = []

    @functools.wraps(add_signal_to_pdu)
    def is_signal_range_valid(
            pdu_instance,
            signal
        ):

        signal_end_bit = signal.start_bit + signal.total_length_bits

        if signal_indexes_range is not None:

            for start, end in signal_indexes_range:
                if signal.start_bit in range(start, end) or \
                        signal_end_bit in range(start, end):
                    raise ValueError('Signal Range should not overlap with already existing signals')

        signal_indexes_range.append((signal.start_bit, signal_end_bit))

        return add_signal_to_pdu(pdu_instance, signal)

    return is_signal_range_valid

class BitUtils:

    BYTE_LENGTH = 8
    NIBBLE_LENGTH = 4
    MASK = 0xFF

    @staticmethod
    def set_bit_and_return_byte(
    
            byte_value,
            bit_position
    
        ):

        byte_value = byte_value | (1 << bit_position)
        return byte_value

    @staticmethod
    def clear_bit_and_return_byte(
            byte_value,
            bit_position
        ):

        byte_value = byte_value & (BitUtils.MASK & ~(1 << bit_position))
        return byte_value

    @staticmethod
    def is_bit_set(
    
            byte_value,
            bit_position
    
        ):

        return int(True) if (byte_value & (1 << bit_position)) \
                        else int(False)

    @staticmethod
    def byte_length(byte_value):

        _MAX_BYTE = BitUtils.BYTE_LENGTH \
                    if (byte_value > 0xF)  \
                    else BitUtils.NIBBLE_LENGTH

        return _MAX_BYTE

def big_endian_byte_order(
    
        network_payload,
        signal_start_bit,
        signal_total_bits,
        signal_data
    ):

    if len(signal_data) > 1:
        signal_data = list(reversed(signal_data))

    pdu_bit = signal_start_bit % 8
    pdu_byte = signal_start_bit // 8
    signal_bit = 0
    signal_byte = 0

    is_single_byte, _MAX_BYTE = (False, signal_total_bits)  \
                                if signal_total_bits <=8 \
                                else (True, 0)

    while signal_total_bits:

        if is_single_byte:
            _MAX_BYTE = BitUtils.byte_length(signal_data[signal_byte])

        if signal_bit == _MAX_BYTE:
            signal_bit = 0
            signal_byte+= 1

        if pdu_bit == 8:
            pdu_bit = 0
            pdu_byte+= 1

        is_set = BitUtils.is_bit_set(signal_data[signal_byte], signal_bit)

        if is_set:
            network_payload[pdu_byte] = BitUtils.set_bit_and_return_byte(network_payload[pdu_byte], pdu_bit)
            
        else:
            network_payload[pdu_byte] = BitUtils.clear_bit_and_return_byte(network_payload[pdu_byte], pdu_bit)

        signal_bit+=1
        pdu_bit+=1

        signal_total_bits -= 1

a = [0x00] * 2

big_endian_byte_order()