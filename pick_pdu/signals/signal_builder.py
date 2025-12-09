from signals.signal import Signal

class SignalBuilder:
    
    def __init__(self, fields):
        self.signal_fields = fields
        self.name = ''
        self.start_bit = 0
        self.total_length_bits = 0
        self.signal_data = []
    
    def add_signal_name(self, name):
        self.name = name
        return self
    
    def add_signal_start_bit(self):
        self.name = self.signal_fields['start_bit']
        return self
        
    def add_signal_total_bits(self):
        self.name = self.signal_fields['signal_total_bits']
        return self
    
    def add_signal_values(self):
        self.signal_data = self.signal_fields['signal_values']
        return self
    
    def build(self):
        return Signal(self.name, self.start_bit, self.total_length_bits, self.signal_data)
        