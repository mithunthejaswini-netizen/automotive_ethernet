
from pdus.pdu import Pdu
from signals.signal_builder import SignalBuilder

def build_protocol_data_units_for_udp_payload(protocol_data_units):
    
    udp_payload_protocol_data_units = []
    
    for _pdu, _pdu_attributes in protocol_data_units.items():
        
        p = PduBuilder(_pdu_attributes)
        p.add_endian().add_length().add_signals().add_pdu_id().add_signals().build()
        udp_payload_protocol_data_units.append(p)
    
    return udp_payload_protocol_data_units

class PduBuilder:
    
    def __init__(self, fields):
        
        self.pdu_fields = fields
        self.pdu = Pdu()
        
    def add_endian(self):
        self.pdu.endian = self.pdu_fields['endianness']
        return self
    
    def add_pdu_id(self):
        self.pdu.pdu_id = self.pdu_fields['pdu_id']       
        return self
    
    def add_length(self):
        self.pdu.pdu_length = self.pdu_fields['length']
        return self
    
    def add_signals(self):
        
        signals = self.pdu_fields['signals']
        
        print(signals)
        
        for signal_name, signal_fields in signals.items():
            
            b_signal = SignalBuilder(signal_fields)
            
            signal = (b_signal.add_signal_name(signal_name)
                .add_signal_start_bit()
                .add_signal_total_bits()
                .add_signal_values()
                .build())
            
            self.pdu.add_signal(signal)
        
        return self
    
    def build(self):
        return self.pdu
        