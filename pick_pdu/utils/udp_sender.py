from pdu_timer import *
from collections.abc import Sequence




def send_udp_packet(
    udp_pkt,
    udp_socket,
    interval=0,
    loop=0
):
    
    """
    Add two numbers.

    :param UdpPdu udp_pkt: Instance of the type UdpPdu holding pdu as payload
    :param socket udp_socket: instance of socket class for creating udp socket
    :param int interval: cyclic interval at which the timer should execute
    :param int loop: This is to indicate whether it has to run forever or number of times.  float('inf') for infinity
    :returns: None
    :rtype: None
    
    """
        
    if not interval and loop==float('inf'):        
        raise ValueError('Transmitting udp frame at 0ms is not Ideal')

    send_udp(udp_pkt, udp_socket)

    if loop:
        import time                
        udp_pkt.timer_count = loop
        udp_pkt.timer_thread = CyclicTimer(interval, send_udp,[udp_pkt, udp_socket])  
        time.sleep(0.02)               
        udp_pkt.start_timer_thread()                

def stop_udp_packet(*udp_pkt):


    """
    Stop one or more UDP packet transmissions.

    :type udp_pkt: UdpPdu
    :param udp_pkt (UdpPdu): One or more UdpPdu instances representing packets that are
                    currently being sent periodically or for a fixed number of loops.
    :returns: None
    :rtype: None
    
    """
        
    for pkt in  udp_pkt:
        pkt.stop_timer_thread()    
    


