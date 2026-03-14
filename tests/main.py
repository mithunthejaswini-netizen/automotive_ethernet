from signals.signal import *
from pdus.pdu_cyclic_timer import *
from pdus.pdu import *
from sockets.pdu_socket import *
from sockets.udp_pdu import *
from utils.ip_utils import *
from utils.ip_port_builder import *
from utils.udp_sender import *
from jsons.json_file_operations import *
from pdus.pdu_builder import *

def parse_json_file():
    
    script_dir = Path(__file__).parent
    json_path = script_dir / 'jsons' / 'pdus.json'
    json_data = parse_json_file_and_read_data(json_path)

    for pkt, pkt_values in json_data.items():
                
        source_endpoint = pkt_values.pop('source_socket')
        destination_endpoint = pkt_values.pop('destination_socket')
        
        protocol_data_units = build_protocol_data_units_for_udp_payload(pkt_values)    
        port = PortBuilder().src_and_dst(source_endpoint, destination_endpoint, SocketAttr.port)
        
        udp = UdpPdu(port)
        
        for pdu in protocol_data_units:
            udp.add_protocol_data_unit(pdu)
    
        ip_address = PortBuilder().src_and_dst(source_endpoint, destination_endpoint, SocketAttr.address)
        
        start_udp_packets_transmission(udp, ip_address, port)

def start_udp_packets_transmission(udp, ip_address, port):
    
    u_socket = get_udp_socket(ip_address, port)
    send_udp_packet(udp, u_socket, 1, float('inf'))

if __name__=='__main__':
    parse_json_file()
    while True:
        pass