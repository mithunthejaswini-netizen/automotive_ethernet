from utils.pdu_utils import Endianness, big_endian_byte_order

class Signal:

    """
    Represents a signal within a PDU or frame.

    A Signal contains metadata such as its name, starting bit position,
    and total bit-length. It also stores the raw signal data, which may
    be encoded or decoded elsewhere in the system.

    """

    __slots__ = ('name', 'start_bit', 'total_length_bits', '_signal_data')

    def __init__(
    
            self,
            name,
            start_bit,
            total_length_bits,
            signal_data
        ):
        
        """
        Initialize a "Signal" object.

        :param str name:
            Name of the signal.

        :param int start_bit:
            Bit position where the signal begins inside the PDU or frame.

        :param int total_length_bits:
            Total size of the signal in bits.

        :param bytes signal_data:
            Raw encoded data representing the signal value.

        :returns: "None"
        :rtype: None

        """

        self.name = name
        self.start_bit = start_bit
        self.total_length_bits = total_length_bits
        self._signal_data = signal_data

    def update_signal_data(
            self,
            endian,
            pdu_payload
        ):
        
        """
        Update the signal's encoded data inside the given PDU payload.

        This method writes "self._signal_data" into "pdu_payload" at the
        correct bit position and using the specified endianness.

        :param str endian:
            Endianness to use (e.g. ``Endianness.BIG.value``).

        :param bytearray pdu_payload:
            The PDU payload into which this signal will be encoded.

        :returns: "None"
        :rtype: None
    
        """
            
        big_endian_byte_order(
                        
            pdu_payload,
            self.start_bit,
            self.total_length_bits,
            self._signal_data,
            endian
        )

    @property
    def signal_data(self):
        """
        Read-only access to the raw signal data.

        :returns:
            The internal encoded signal bytes.
        :rtype: bytes
        """

        return self._signal_data

    @signal_data.setter
    def signal_data(
        
            self,
            signal_data
    
        ):
        
        """
        Prevent external modification of ``signal_data``.

        Assigning to this property is not allowed to maintain signal
        integrity.

        :raises AttributeError:
            Always raised because signal data cannot be changed directly.
        """
        
        raise AttributeError('Signal data cannot be updated')

    def reset_signal_data(self):

        """
        Reset all bytes of the signal data to ``0x00``.

        Useful for clearing a PDU before re-encoding new signal values.

        :returns: ``None``
        :rtype: None
        """

        for index, _byte in enumerate(self._signal_data):
            self._signal_data[index] = 0x00

    def __eq__(self, other):

        """
        Compare two signals for equality.

        Two "Signal" objects are considered equal if their names and
        raw signal data match.

        :param Signal other:
            Another signal to compare with.

        :returns:
            "True" if equal, otherwise "False`"
        
        :rtype: bool
        """

        if not isinstance(other, type(self)):
            return NotImplemented

        result =  self.name == other.name and \
                    self.start_bit == other.start_bit and \
                    self.total_length_bits == other.total_length_bits and \
                    self._signal_data == other._signal_data
        
        return result

        # use the below version if you want to strictly compare
        
        '''
        return  self.name == other.name and \
                self.total_length_bits == other.total_length_bits and \
                self.start_bit == other.start_bit and \
                self.signal_data == other.signal_data
        '''

    def __hash__(self):

        """
        Compute the hash of this signal.

        The hash is derived from the signal's name, start bit,
        total bit-length, and its raw signal data.

        :returns:
            Hash value for this signal.
            
        :rtype: int
        """

        return hash((self.name, self.start_bit, self.total_length_bits, tuple(self._signal_data)))

    def __str__(self):

        """
        Return a human-readable formatted representation of the signal.

        Includes the name, start bit, length, and raw signal data.

        :returns:
            Formatted multi-line string describing the signal.
            
        :rtype: str
        """

        return f'{self.name}\n\t +-- {self.start_bit=}\n\t +-- {self.total_length_bits=}\n\t +-- {self.signal_data=}\n'
    
