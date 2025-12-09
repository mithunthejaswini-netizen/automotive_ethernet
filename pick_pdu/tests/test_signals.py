import pytest

from signals.signal import Signal
from pdus.pdu import Pdu
from utils.pdu_utils import Endianness

def test_initialization():
    sig = Signal("Speed", 8, 16, [0x12, 0x34])

    assert sig.name == "Speed"
    assert sig.start_bit == 8
    assert sig.total_length_bits == 16
    assert sig.signal_data == [0x12, 0x34]

def test_signal_data_read_only():
    sig = Signal("Speed", 0, 8, [0x55])

    with pytest.raises(AttributeError):
        sig.signal_data = b"\x99"

def test_reset_signal_data():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    
    pdu1.add_signal(signal_media_title)
    pdu1.add_signal(signal_media_type)
    pdu1.add_signal(signal_media_file_system)
    
    sig = Signal("RPM", 0, 16, [0x12, 0x34])
    
    sig.reset_signal_data(pdu1)
    
    assert sig.signal_data == [0x00, 0x00]

def test_update_signal_data_big_endian():
    
    payload = [0] * 10
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    signal_media_title.update_signal_data(Endianness.BIG, payload)
    signal_media_type.update_signal_data(Endianness.BIG, payload)
    
    assert payload==[0xff, 0xff, 0xf8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
    
def test_update_signal_data_small_endian():
    
    payload = [0] * 10
    signal_bridge_disc = Signal('BridgeDisc', 0, 5, [0x1F]) # Endianness.BIG
    signal_joliet = Signal('Joliet', 5, 11, [0x7, 0xFF])
    signal_photo_cd = Signal('PhotoCD', 16, 8, [0xFF])
    signal_cd_extra = Signal('CDExtra', 24, 14, [0x3F, 0xFF])
    signal_udf = Signal('UDF', 38, 8, [0xFF])
    
    signal_bridge_disc.update_signal_data(Endianness.SMALL, payload)
    signal_joliet.update_signal_data(Endianness.SMALL, payload)
    signal_photo_cd.update_signal_data(Endianness.SMALL, payload)
    signal_cd_extra.update_signal_data(Endianness.SMALL, payload)
    signal_udf.update_signal_data(Endianness.SMALL, payload)
    
    assert payload==[0xff, 0xff, 0xff, 0xff, 0xff, 0x3f, 0x0, 0x0, 0x0, 0x0]

def test_signal_equality():
    s1 = Signal("Speed", 8, 16, [0x32, 0x85])
    s2 = Signal("Speed", 8, 16, [0x32, 0x85])

    assert s1 == s2
    #assert hash(s1) == hash(s2)
    
def test_signal_value_equality():
    s1 = Signal("Speed", 8, 16, [0x32, 0x85])
    s2 = Signal("Speed", 8, 16, [0x32, 0x85])
    
    assert s1 == s2
    assert s1.signal_data == s2.signal_data

def test_signal_inequality():
    s1 = Signal("Speed", 8, 16, [0x56, 0x53])
    s2 = Signal("Speed", 8, 16, [0x56, 0x51])

    assert s1 != s2

def test_str_output():
    sig = Signal("Speed", 8, 16, [0x01, 0x02])
    text = str(sig)

    assert "Speed" in text
    assert "start_bit=8" in text
    assert "total_length_bits=16" in text