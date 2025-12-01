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

def test_pdu_eq_and_hash():
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])

    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    p2 = Pdu(Endianness.BIG, 0x3285, 20)
    
    p1.add_signal(signal_media_title)
    p1.add_signal(signal_media_type)
    
    p2.add_signal(signal_media_title)
    p2.add_signal(signal_media_type)

    # Hash test
    h1 = hash(p1)
    h2 = hash(p1)  # same object hash
    assert h1 == h2
    assert p1==p2

def test_pdu_contains():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    p2 = Pdu(Endianness.BIG, 0x378, 20)
    
    p1.add_signal(signal_media_title)
    
    p2.add_signal(signal_media_title)
    p2.add_signal(signal_media_type)

    assert "mediaTitle" in p1
    assert "mediaType" not in p1
    
    assert "mediaTitle" in p2
    assert "mediaType" in p2
    
def test_pdu_contains_and_removed():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    p2 = Pdu(Endianness.BIG, 0x378, 20)
    
    p1.add_signal(signal_media_title)
    
    p2.add_signal(signal_media_title)
    p2.add_signal(signal_media_type)

    assert "mediaTitle" in p1
    assert "mediaType" not in p1
    
    assert "mediaTitle" in p2
    assert "mediaType" in p2
    
    p2.remove_signal(signal_media_type)
    
    assert "mediaType" not in p2

def test_pdu_iter_and_len():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    
    p1.add_signal(signal_media_title).add_signal(signal_media_type)

    assert len(p1) == 2
    signals_list = list(p1)
    assert signal_media_title in signals_list and signal_media_type in signals_list

def test_pdu_payload_read_only():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    
    p1.add_signal(signal_media_title).add_signal(signal_media_type)

    payload_bytes = p1.payload

    assert isinstance(payload_bytes, list)

    with pytest.raises(AttributeError):
        p1.payload = [0] * 10

def test_pdu_str_contains_signal_names():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    
    p1.add_signal(signal_media_title).add_signal(signal_media_type)

    s = str(p1)
    
    assert "mediaTitle" in s
    assert "mediaType" in s

def test_add_duplicate_signal_prints(monkeypatch):
    p1 = Pdu(Endianness.BIG, 0x3285, 20)
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    p1.add_signal(signal_media_type)
    printed = []
    
    # Capture print output
    def fake_print(msg):
        printed.append(msg)

    monkeypatch.setattr("builtins.print", fake_print)
    p1.add_signal(signal_media_type)
    assert any("already exists" in msg for msg in printed)