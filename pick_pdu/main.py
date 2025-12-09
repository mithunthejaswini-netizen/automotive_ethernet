from signals.signal import *
from pdus.pdu_cyclic_timer import *
from pdus.pdu import *
from sockets.pdu_socket import *
from sockets.udp_pdu import *
from utils.ip_utils import *
from jsons.json_file_operations import *
from pdus.pdu_builder import *

def parse_json_file():
    
    script_dir = Path(__file__).parent
    json_path = script_dir / 'jsons' / 'pdus.json'
    json_data = parse_json_file_and_read_data(json_path)
    
    p = list(json_data.values())[3]

    p.pop('source_socket')
    p.pop('destination_socket')
        
    pdus = build_protocol_data_units_for_udp_payload(p)
    
    print(len(pdus))

def start_udp_packets_transmission():
    pass

if __name__=='__main__':
    parse_json_file()