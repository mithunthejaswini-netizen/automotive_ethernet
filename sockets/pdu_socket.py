import socket

def get_udp_socket(

        endpoint_ip,
        endpoint_port

    ):
    
    """
    Create and return a UDP socket configured for the given endpoint.

    :param str endpoint_ip: Target IP address to which the socket will send UDP packets.
    :param int endpoint_port: Target UDP port number.
    :returns: A configured UDP socket object.
    :rtype: socket.socket
    """

    # Create UDP socket
    udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)    ## please use socket.AF_INET for ipv4

    # Bind to the source IP and port
    udp_socket.bind((endpoint_ip.src_ip, endpoint_port.src_port))

    # Connect to destination
    udp_socket.connect((endpoint_ip.dst_ip, endpoint_port.dst_port))

    return udp_socket