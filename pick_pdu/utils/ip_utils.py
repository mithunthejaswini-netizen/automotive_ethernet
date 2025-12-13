import ipaddress

class ValidIp:

    def __init__(self, ip):
        self.ip = ip
        
    def __set__(self, instance, value):
        # Validate IP
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise ValueError("Invalid IP address provided")

        # Store value on the instance using the backing attribute
        setattr(instance, self.ip, value)

    def __get__(self, instance, owner):
        # Access via class (IpAddress.src_ip) should return descriptor itself
        if instance is None:
            return self

        # Return value if set, else None
        return getattr(instance, self.ip, None)

class IpAddress:

    """

    Represents a pair of IP addresses consisting of a source IP and a
    destination IP.

    The class uses "ValidIp" descriptors to validate and store the
    internal attributes "_src_ip" and "_dst_ip". It supports readable
    string representation, equality comparison, and hashing.
    
    """

    src_ip = ValidIp('_src_ip')
    dst_ip = ValidIp('_dst_ip')

    def __str__(self):
                
        """
        Return a formatted string representation of the IP address pair.

        The format includes labels and shows both source and destination IPs
        for readability.

        :returns: Human-readable IP address string.
        :rtype: str
        """
                
        return f' src ip = {self.src_ip}   ::  dst ip = {self.dst_ip} \n'

    def __repr__(self):

        """
        Return a concise representation of the IP address pair.

        The format is ``"<src_ip>::<dst_ip>"``.

        :returns: Canonical string representation.
        :rtype: str
        
        """

        return str(self.src_ip) + "::" + str(self.dst_ip)

    def __eq__(self, other):

        """
        Compare two "IpAddress" objects for equality.

        Two instances are considered equal if both their source and
        destination IPs match.

        :param IpAddress other: The other instance to compare with.
        :returns: True if both addresses match, otherwise False.
        :rtype: bool
        
        """

        return self.src_ip == other.src_ip and self.dst_ip == other.dst_ip

    def __hash__(self):
        
        """
        Compute the hash value for the IP address pair.

        The hash is based on both the source and destination IPs, allowing
        the object to be used in hashed collections such as sets and dicts.

        :returns: Hash value of the instance.
        :rtype: int
        
        """
                
        return hash((self.src_ip, self.dst_ip))

class ValidPort:

    """
    
    Descriptor used to validate and store a port number on an owning class.

    "ValidPort" ensures that the assigned port value is non-zero and
    positive. It stores the validated value in the attribute name provided
    during initialization (e.g., "_src_port" or "_dst_port").
    
    """

    def __init__(self, port):
        
        """
        Initialize the descriptor with the name of the internal attribute
        where the port value will be stored.

        :param str port: Name of the private attribute that holds the port.
        :returns: None
        :rtype: None
        
        """
                
        self.port = port

    def __set__(self, instance, value):
        
        """
        Validate and set the port value on the instance.

        The port is considered valid if it is not ``None`` and is a
        positive integer. If the value is invalid, a ``ValueError`` is raised.

        :param object instance: The object on which the port is being set.
        :param int value: The port number to validate and assign.
        :raises ValueError: If the port number is invalid.
        :returns: None
        :rtype: None
        
        """

        def isvalid_port(value):        
            return (value is not None) and not (value <=0) and not (value>65535)
        
        if isvalid_port(value):            
            setattr(instance, self.port, value)
        else:
            raise ValueError('Port number is not valid { 0 < port > 65535 }')

    def __get__(self, instance, owner):
        
        """
        Retrieve the stored port value from the instance.

        If accessed on the class, the descriptor itself is returned.
        If accessed on an instance, the stored port value is returned.

        :param object instance: The object from which the port is retrieved.
        :param type owner: The class owning this descriptor.
        :returns: The stored port value or the descriptor itself.
        :rtype: int or ValidPort
        
        """

        if not instance:
            return self
        
        return getattr(instance, self.port, None)

class Port:

    """
    Represents a pair of network ports consisting of a source port and a
    destination port.

    The class uses "ValidPort" descriptors to validate and store the
    internal attributes "_src_port" and "_dst_port".

    """

    src_port = ValidPort('_src_port') 
    dst_port = ValidPort('_dst_port')

    def __str__(self):

        """
        Return the string representation of the port pair.

        The format is "<src_port>::<dst_port>" which shows the source and
        destination ports in a readable form.

        :returns: String representation of the port pair.
        :rtype: str
        
        """

        return str(self._src_port) + "::" + str(self._dst_port)


