from utils.pdu_utils import *
class UdpPdu:

    """
    Represents a UDP Protocol Data Unit (UDP PDU) containing one or more
    protocol data units (PDUs), the associated UDP port, socket, payload,
    and an optional cyclic timer for periodic transmission.

    The class manages:
    - storage of PDUs in an internal PduDict
    - binding and managing a UDP socket
    - attaching and controlling a timer thread for periodic sending
    - assembling payloads from contained PDUs
    """

    def __init__(
            
            self,
            port
        ):

        """
        Initialize a UdpPdu instance.

        :param Port port: Port object containing source and destination ports.
        :returns: None
        :rtype: None
        """

        self.protocol_data_units = PduDict()
        self._port = port
        self._udp_socket = None
        self.MTU = 1200
        self._payload = []
        self._timer_thread = None    
        self.timer_count = 0  

    @property
    def port(self):
        """
        Return the configured port for this UDP PDU.

        :returns: Port object.
        :rtype: Port
        """
        
        return self._port
    
    @port.setter
    def port(        
        
            self,
            port        
    
        ):
        
        """
        Set the port for this UDP PDU only once.

        Once set, attempting to modify the port raises an AttributeError.

        :param Port port: Port object to assign.
        :raises AttributeError: If the port is already set.
        """

        if self._port:
            raise AttributeError('Port cannot be set')
        else:
            self._port = port

    @property
    def udp_socket(self):

        """
        Return the currently attached UDP socket.

        :returns: The socket object or None.
        :rtype: socket.socket or None
        """

        return self._udp_socket
    
    @udp_socket.setter
    def udp_socket(self, _socket):
    
        """
        Attach a UDP socket to this UDP PDU.

        :param socket.socket _socket: The socket to attach.
        :returns: None
        :rtype: None
        """

        self._udp_socket = _socket

    def attach_socket(self, _socket):

        """
        Attach a UDP socket to the PDU.

        This is an alternative to using the ``udp_socket`` setter.

        :param socket.socket _socket: The socket to attach.
        :returns: None
        :rtype: None
        """

        self._udp_socket = _socket

    @property
    def payload(self):
        
        self._payload.clear()
        
        for pdu in self.protocol_data_units.values():
            
            self._payload += list(pdu.pdu_id.to_bytes(4, byteorder=pdu.endian))
            self._payload += list(pdu.pdu_length.to_bytes(4, byteorder=pdu.endian))
            self._payload += pdu.payload
            
        return self._payload
    
    @payload.setter
    def payload(self, value):
        raise AttributeError('Payload should not be set {use add_protocol_data_unit method to set}')

    @property
    def timer_thread(self):
        
        """
        Return the timer thread attached to this UDP PDU, if any.

        :returns: Timer thread object or None.
        :rtype: threading.Timer or None
        """

        return self._timer_thread
    
    @timer_thread.setter
    def timer_thread(
    
            self,
            timer_thread
    
        ):
        
        """
        Attach a timer thread for cyclic UDP transmission.

        The timer can only be assigned once.

        :param threading.Timer timer_thread: The timer thread to attach.
        :raises ValueError: If a timer is already attached.
        :returns: None
        :rtype: None
        """

        if not self._timer_thread:            
            self._timer_thread = timer_thread
        else:
            raise ValueError('Timer is already attached.')


    def start_timer_thread(self):
        """
        Start the attached timer thread if it exists.

        :returns: None
        :rtype: None
        """
        if self._timer_thread:            
            self._timer_thread.start()

    def stop_timer_thread(self):
        
        """
        Stop the attached timer thread if it exists.

        :returns: None
        :rtype: None
        """

        if self._timer_thread:
            self._timer_thread.cancel()

    def add_protocol_data_unit(
    
            self,
            protocol_data_unit
        ):
        
        """
        Add a protocol data unit (PDU) into this UDP PDU.

        PDUs are stored in ``protocol_data_units`` using ``pdu_id`` as key.

        :param Pdu protocol_data_unit: The PDU to add.
        :returns: Self, allowing method chaining.
        :rtype: UdpPdu
        """

        if protocol_data_unit.pdu_id in self.protocol_data_units:
            print('protocol data unit already exists', 'decimal=', protocol_data_unit.pdu_id, 'hex=', hex(protocol_data_unit.pdu_id))
        else:
            self.MTU -= protocol_data_unit.pdu_length
            
            if self.MTU >= 0:
                self.protocol_data_units[protocol_data_unit.pdu_id] = protocol_data_unit
            else:
                raise PayloadOverflowError('Payload Exceeds Max MTU(1200)')
                
        return self

    def __getitem__(self, pdu):

        """
        Retrieve a PDU by PDU ID string.

        :param str pdu: PDU identifier.
        :returns: The matching PDU.
        :rtype: Pdu
        :raises TypeError: If key is not of type ``str``.
        """

        if isinstance(pdu, str):
            return self.protocol_data_units[pdu]
        elif isinstance(pdu, slice):
            raise TypeError('__getitem__ only works for str')
        else:
            raise TypeError('__getitem__ only works for str')

    def get_pdu(self, pdu_id):
        
        """
        Retrieve a PDU by integer PDU ID.

        :param int pdu_id: The numeric identifier of the PDU.
        :returns: The matching PDU.
        :rtype: Pdu
        :raises TypeError: If ``pdu_id`` is not an integer.
        """

        if isinstance(pdu_id, int):
            return self.protocol_data_units[pdu_id]
        else:
            raise TypeError('get_pdu only works for int')

    def delete_protocol_data_unit(self, pdu):

        """
        Delete a PDU from this UDP PDU.

        :param Pdu pdu: The PDU object whose entry will be removed.
        :returns: None
        :rtype: None
        """
        
        del self.protocol_data_units[pdu.pdu_id]

    def udp_payload(self):

        """
        Handle the payload assembly and timer decrement logic.

        This method:
        - updates the internal timer counter
        - cancels the timer thread when the count reaches zero
        - prints diagnostic information

        :returns: None
        :rtype: None
        """
        
        '''for pdu in self.protocol_data_units:
            self.payload+= pdu.payload'''

        if not self.timer_count:
            self.timer_count-=1

            if not self.timer_count and self._timer_thread:   
                print('Transmission of UDP Frame Stopped')
                self.timer_thread.cancel()

    def __str__(self):

        """
        Return a string representation of all protocol data units stored in this UDP PDU.

        :returns: Concatenated string of all PDUs.
        :rtype: str
        """

        total_pdu = ''

        for pdu in self.protocol_data_units.values():
            total_pdu += str(pdu)

        return total_pdu