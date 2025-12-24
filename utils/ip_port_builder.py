from enum import Enum
from utils.ip_utils import IpAddress, Port

class SocketAttr(Enum):
    port = "port"
    address = 'address'

class PortBuilder:
    
    @classmethod
    def src_and_dst(cls, src_endpoint, dst_endpoint, attr):
        
        if attr==None or attr=='':
            raise AttributeError('Invalid Socket Attribute Provided')
        
        if SocketAttr.port == attr:
            
            port = Port()    
            port.src_port , port.dst_port = (src_endpoint[attr.value], dst_endpoint[attr.value])
            
            return port
            
        elif SocketAttr.address == attr:
            
            ip_address = IpAddress()
            ip_address.src_ip = src_endpoint[attr.value]
            ip_address.dst_ip = dst_endpoint[attr.value]
            
            return ip_address
            