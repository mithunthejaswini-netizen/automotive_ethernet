import time
from colorama import init, Fore

class PacketInfo:
    
    src_ip = None
    dst_ip = None
    src_port = None
    dst_port = None
    _socket = None
    timestamp = ''
    
    @classmethod
    def init(cls, _sock):
        init(autoreset=True)
        cls._socket = _sock
        cls.get_source_ip()
        cls.get_destination_ip()
        cls.get_source_port()
        cls.get_destination_port()
        cls.get_timestamp()
        
        return cls
    
    @classmethod
    def get_source_ip(cls):
        cls.src_ip = cls._socket.getsockname()[0]
        
    @classmethod    
    def get_destination_ip(cls):
        cls.dst_ip = cls._socket.getpeername()[0]
    
    @classmethod
    def get_source_port(cls):
        cls.src_port = cls._socket.getsockname()[1]
        
    @classmethod
    def get_destination_port(cls):
        cls.dst_port = cls._socket.getpeername()[1]
        
    @classmethod
    def get_timestamp(cls):
        cls.timestamp =  time.strftime("%Y-%m-%d %H:%M:%S").encode()

    @classmethod
    def ppkt(cls, pkt):
        print(f"{Fore.RED}{cls.timestamp}  "
            f"{Fore.GREEN} sip {cls.src_ip}  "
            f"{Fore.BLUE} dip {cls.src_port}  "
            f"{Fore.GREEN} sp {cls.dst_ip}  "
            f" {Fore.BLUE} dp {cls.dst_port}  "
            f"{Fore.BLUE}{len(pkt.payload)}  "
            f"PDUs :- {Fore.BLUE}{pkt.get_protocol_data_units()}  ")