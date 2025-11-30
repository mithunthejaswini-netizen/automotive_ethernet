from signals.signal import Signal

class Pdu:

    """
    Represents a Protocol Data Unit (PDU).

    A PDU contains multiple signals packed into a byte payload according
    to bit positions and endianness. Signals are stored in a dictionary
    by name and can be added, removed, or queried.

    The PDU manages its own payload buffer and updates it whenever
    signals are added.
    
    """

    def __init__(
                self,
                /,
                endian='big',
                pdu_id=0x3285,
                pdu_length=9
        ):

        """
        Initialize a "Pdu" instance.

        :param str endian:
            Endianness of the PDU ("big" or "little").

        :param int pdu_id:
            Unique identifier for the PDU.

        :param int pdu_length:
            Length of the PDU payload in bytes.

        :returns: "None"
        :rtype: None
        """

        self._pdu_id = pdu_id
        self._pdu_length = pdu_length
        self._endian = endian
        self.signals = {}
        self._payload = [0] * pdu_length
        self._iterator = None

    @property
    def endian(self):
    
        """
        Endianness of the PDU.

        :returns: 'big' or 'little'.
        :rtype: str
        """ 
        return self._endian

    @property
    def pdu_length(self):
        """
        Total length of the PDU payload in bytes.

        :returns: Length in bytes.
        :rtype: int
        """
            
        return self._pdu_length

    @property
    def pdu_id(self):

        """
        Identifier of the PDU.

        :returns: The PDU ID.
        :rtype: int
        """
        return self._pdu_id

    @property
    def payload(self):

        """
        Byte representation of the PDU's current payload.

        :returns: The payload as immutable bytes.
        :rtype: bytes
        """
        return self._payload

    @payload.setter
    def payload(
            self,
            value
        ):

        """
        Prevent modification of the PDU payload.

        The payload can only be changed through signal updates.

        :raises AttributeError:
            Always raised because direct payload assignment is forbidden.
        """

        raise AttributeError('Payload cannot be changed')

    #@check_valid_signal_range
    def add_signal(
            self,
            signal
        ):

        """
        Add a signal to the PDU and update the payload.

        If the signal already exists (based on name), it is ignored.
        Otherwise, the signal is inserted and encoded into the payload
        according to its bit position and endianness.

        :param Signal signal:
            The signal object to be added.

        :returns:
            The current 'Pdu' instance (for chaining).
        :rtype: Pdu
        """

        if not isinstance(signal, Signal):
            raise TypeError(f'signal should be of {type(Signal)}')
        
        if signal in self.signals.values():
            print(f'{signal.name} already exists')
        else:
            self.signals[signal.name] = signal
            signal.update_signal_data(
                                self.endian,
                                self._payload
            )

        return self

    def remove_signal(
            self,
            signal
        ):

        """
        Remove a signal from the PDU and reset its data.
        

        :param signal:
            Either the signal name (str) or a Signal instance.

        :returns: None
        :rtype: None
        """

        if isinstance(signal, str):
            self.signals[signal].reset_signal_data(self)
            
        elif isinstance(signal, Signal):
            signal.reset_signal_data(self)
            signal = signal.name 

        del self.signals[signal]

    def __eq__(
            self,
            other
        ):

        """
        Compare two PDUs for equality.

        Two PDUs are equal if both their PDU IDs and their signal sets match.

        :param Pdu other:
            Another PDU instance.

        :returns: 'True' if equal, otherwise 'False'.
        :rtype: bool
        """
        
        return self.pdu_id==other.pdu_id and\
                self.signals == other.signals

    def __contains__(
            self,
            signal
        ):
    
        # If a string is passed, check by name
        if isinstance(signal, str):
            return signal in self.signals
    
        # If a Signal object is passed, check by equality
        elif isinstance(signal, Signal):
            return signal.name in self.signals and self.signals[signal.name] == signal
    
        # Anything else → not contained
        return False

    def __getitem__(
            self,
            signal
        ):

        """
        Retrieve a signal by name.

        :param str signal:
            Name of the signal to retrieve.

        :returns:
            The corresponding 'Signal' instance.

        :raises TypeError:
            If the key is not a 'str'.
        """

        if isinstance(signal, str):
            return self.signals[signal]
        elif isinstance(signal, slice):
            raise TypeError('__getitem__ only works for str')
        else:
            raise TypeError('__getitem__ only works for str or slice')

    def get_signal(
            self,
            signal_name
        ):
        
        """
        Retrieve a signal by name.

        :param str signal_name:
            Name of the signal.

        :returns:
            The 'Signal' instance, or 'None' if not present.
        :rtype: Signal | None
        """
        return self.signals[signal_name]

    def __hash__(self):

        """
        Compute a hash value for the PDU.

        :returns:
            Hash derived from the signal dictionary.
            
        :rtype: int
        """
        
        ## making the perfect has with sorted so that there shouldn't be any iota of mis-match of PDUs
        
        signals_tuple = tuple(sorted(
            (sig.name, sig.start_bit, sig.total_length_bits, tuple(sig._signal_data))
            for sig in self.signals.values()
        ))

        return hash((self.pdu_id, signals_tuple))

    def __str__(self):

        """
        Return a formatted string representation of the PDU.

        Includes PDU ID, length, endianness, and the list of signals.

        :returns:
            Human-readable description of the PDU.
            
        :rtype: str
        """

        signals_in_pdu = list(self.signals.keys())
        signal_tree = ''

        for signal in signals_in_pdu:
            signal_tree = signal_tree + f'{signal}\n\t\t'

        return f'self.pdu_id: {self.pdu_id}\nself.pdu_length: {self.pdu_length}\nself.endian: {self.endian}\nsignals: \n\t\t{signal_tree}'

    def __iter__(self):

        """
        Iterate over all signals in the PDU.

        :returns:
            
            Iterator over `Signal` objects.
            
        :rtype: iterator
        """         

        return iter(self.signals.values())

    def __len__(self):

        """
        Number of signals stored in the PDU.

        :returns: Count of signals.
        :rtype: int
        """

        return len(self.signals)

    def __next__(self):

        """
        Return the next signal in iteration.

        :returns:
            Next "Signal" object.
        :rtype: Signal

        :raises StopIteration:
            When iteration is exhausted.
        """
        return next(self._iterator)