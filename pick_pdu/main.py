from signal import Signal
from pdu import Pdu
from udp import *
from pdu_socket import *

def parse_json_file():
    pass

if __name__=='__main__':

    s1 = Signal('Sadananda', 0, 16, [0x32, 0x85])
    s2 = Signal('Maharaj', 16, 16, [0x32, 0x85])
    s3 = Signal('Datta', 32, 16, [0x32, 0x85])
    s4 = Signal('Datta', 32, 16, [0x32, 0x85])
    s5 = Signal('Dattas', 32, 16, [0x32, 0x85])

    pdu1 = Pdu('big', 0x3285, 0x20)

    print(s5)

    pdu1.add_signal(s1)
    pdu1.add_signal(s2)
    pdu1.add_signal(s3)
    pdu1.add_signal(s4)

    pdu2 = Pdu('big', 0x1235, 0x21)

    pdu2.add_signal(s5)    

    p = Port()
    p.src_port = 32
    p.dst_port = 85

    ip_address = IpAddress()

    ip_address.src_ip = '127.0.0.1'
    ip_address.dst_ip = '127.0.0.2'

    print(p.src_port)

    u_socket = get_udp_socket(ip_address, p)
    print(type(u_socket))

    Udp = UdpPdu(p)

    Udp.add_protocol_data_unit(pdu1)
    Udp.add_protocol_data_unit(pdu2)


    from udp_sender import *
    import time

    send_udp_packet(Udp, u_socket,  0, 0)
    time.sleep(1)
    print('------- second time ----------')
    send_udp_packet(Udp, u_socket, 1, float('inf'))

    time.sleep(20)

    stop_udp_packet(Udp)
