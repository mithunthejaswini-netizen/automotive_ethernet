import pytest
from signals.signal import Signal
from pdus.pdu import Pdu
from utils.pdu_utils import Endianness

# -------------------------------
# PDU Tests
# -------------------------------

'''
def test_pdu_equality_and_hash():
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    pdu2 = Pdu(Endianness.BIG, 0x3285, 0x10)
    
    pdu1.add_signal(signal_media_title)
    pdu1.add_signal(signal_media_type)
    
    pdu2.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    
    assert pdu1==pdu2
    
    pdu2.add_signal(signal_media_file_system)
        
    assert pdu1!=pdu2

def test_pdu_signal_reset_signal_data():
    
    s = Signal('mediaTitle', 13, 14, [0x3F, 0xFF])
    
    pdu = Pdu(Endianness.BIG, 0x3285)
    pdu.add_signal(s)
    
    assert pdu.payload == [255, 252, 0, 0, 0, 0, 0, 0, 0]
    
    s.reset_signal_data(pdu)
    assert s.signal_data == [0, 0]
    
    print(pdu.payload)
    
    assert pdu.payload == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    

def test_pdu_signal_signal_data_property_immutable():
    
    s = Signal('mediaTitle', 13, 14, [0x3F, 0xFF])
    
    with pytest.raises(AttributeError):
        s.signal_data = [0x01]


def test_pdu_add_signal_to_pdu():
    
    pdu = Pdu(Endianness.BIG, 0x5651)
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])

    # Adding signal
    pdu.add_signal(signal_media_title)
    pdu.add_signal(signal_media_type)
    pdu.add_signal(signal_media_file_system)
    
    assert "mediaTitle" in pdu.signals
    
    assert pdu.signals["mediaFileSystem"] == signal_media_file_system

'''

def test_pdu_remove_signal_from_pdu():
    
    pdu = Pdu(Endianness.BIG, 0x378)
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    
    pdu.add_signal(signal_media_title)
    pdu.add_signal(signal_media_type)
    pdu.add_signal(signal_media_file_system)
    
    # Remove by object
    pdu.remove_signal(signal_media_type)
    
    assert "mediaType" not in pdu.signals

    # Add and remove by name
    pdu.remove_signal("mediaFileSystem")
    
    assert "mediaFileSystem" not in pdu.signals
    
    assert 'mediaTitle' in pdu.signals

'''
def test_pdu_eq_and_hash():
    s1 = Signal("Speed")
    s2 = Signal("RPM")

    p1 = Pdu()
    p2 = Pdu()
    p1.add_signal(s1)
    p1.add_signal(s2)
    p2.add_signal(Signal("Speed"))
    p2.add_signal(Signal("RPM"))

    # Signals are the same
    assert p1 != p2  # different _signal_data instances will fail equality unless same bytes
    # Hash test
    h1 = hash(p1)
    h2 = hash(p1)  # same object hash
    assert h1 == h2

def test_pdu_contains():
    sig1 = Signal("Speed")
    sig2 = Signal("RPM")
    pdu = Pdu()
    pdu.add_signal(sig1)

    assert "Speed" in pdu
    assert sig1 in pdu
    assert "RPM" not in pdu
    assert sig2 not in pdu

def test_pdu_iter_and_len():
    sig1 = Signal("Speed")
    sig2 = Signal("RPM")
    pdu = Pdu()
    pdu.add_signal(sig1).add_signal(sig2)

    assert len(pdu) == 2
    signals_list = list(pdu)
    assert sig1 in signals_list and sig2 in signals_list

def test_pdu_payload_read_only():
    pdu = Pdu()
    sig = Signal("Speed")
    pdu.add_signal(sig)

    payload_bytes = pdu.payload
    assert isinstance(payload_bytes, bytes)

    with pytest.raises(AttributeError):
        pdu.payload = [0] * 10

def test_pdu_str_contains_signal_names():
    sig1 = Signal("Speed")
    pdu = Pdu()
    pdu.add_signal(sig1)

    s = str(pdu)
    assert "Speed" in s
    assert "pdu_id" in s

def test_add_duplicate_signal_prints(monkeypatch):
    pdu = Pdu()
    sig = Signal("Speed")
    pdu.add_signal(sig)

    printed = []

    # Capture print output
    def fake_print(msg):
        printed.append(msg)

    monkeypatch.setattr("builtins.print", fake_print)
    pdu.add_signal(sig)
    assert any("already exists" in msg for msg in printed)
    
'''