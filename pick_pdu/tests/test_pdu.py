import pytest
from signals.signal import Signal
from pdus.pdu import Pdu
from utils.pdu_utils import Endianness

# -------------------------------
# PDU Tests
# -------------------------------

def test_pkt_1():
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track = Signal('lastTrack', 43, 2, [0x03])
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    
    pdu1.add_signal(signal_media_title)
    pdu1.add_signal(signal_media_type)
    pdu1.add_signal(signal_media_file_system)
    pdu1.add_signal(signal_first_track)
    pdu1.add_signal(signal_last_track)
    
    assert pdu1.payload == [255, 255, 255, 255, 255, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_pkt_2():
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track = Signal('lastTrack', 43, 2, [0x03])
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 10)
    
    pdu1.add_signal(signal_media_title)
    pdu1.add_signal(signal_media_file_system)
    pdu1.add_signal(signal_first_track)
    pdu1.add_signal(signal_last_track)
    
    assert pdu1.payload == [255, 252, 7, 255, 255, 240, 0, 0, 0, 0]
    
def test_pkt_3():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track = Signal('lastTrack', 43, 2, [0x03])
    
    pdu1 = Pdu(Endianness.BIG, 12933, 20)
    pdu2 = Pdu(Endianness.BIG, 22016, 20)
    pdu3 = Pdu(Endianness.BIG, 888, 20)
    pdu4 = Pdu(Endianness.BIG, 38978, 20)
    pdu5 = Pdu(Endianness.BIG, 4660, 20)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu3.add_signal(signal_media_file_system)
    pdu4.add_signal(signal_first_track)
    pdu5.add_signal(signal_last_track)
    
    assert pdu1.payload == [255, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [0, 3, 248, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 7, 255, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu4.payload == [0, 0, 0, 0, 1, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu5.payload == [0, 0, 0, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_pkt_4():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track = Signal('lastTrack', 43, 2, [0x03])
    
    pdu1 = Pdu(Endianness.BIG, 12933, 20)
    pdu2 = Pdu(Endianness.BIG, 22016, 20)
    pdu3 = Pdu(Endianness.BIG, 888, 20)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu2.add_signal(signal_media_file_system)
    pdu3.add_signal(signal_first_track)
    pdu3.add_signal(signal_last_track)
    
    assert pdu1.payload == [255, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [0, 3, 255, 255, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 0, 0, 1, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_pkt_5():
    
    signal_play = Signal('play', 5, 6, [0x3F]) # Endianness.BIG
    signal_stop = Signal('stop', 16, 11, [0x7, 0xFF])
    signal_pause = Signal('pause', 21, 5, [0x1F])
    signal_load = Signal('load', 40, 19, [7, 0xFF, 0xFF])
    signal_unload = Signal('Unload', 53, 13, [0x1F, 0xFF])
    signal_search_forward = Signal('searchForward', 59, 6, [0x3F])
    
    pdu1 = Pdu(Endianness.BIG, 12933, 20)
    pdu2 = Pdu(Endianness.BIG, 12934, 20)
    pdu3 = Pdu(Endianness.BIG, 12935, 20)
    pdu4 = Pdu(Endianness.BIG, 12936, 20)
    pdu5 = Pdu(Endianness.BIG, 12937, 20)
    pdu6 = Pdu(Endianness.BIG, 12938, 20)
    
    pdu1.add_signal(signal_play)
    pdu2.add_signal(signal_stop)
    pdu3.add_signal(signal_pause)
    pdu4.add_signal(signal_load)
    pdu5.add_signal(signal_unload)
    pdu6.add_signal(signal_search_forward)
    
    assert pdu1.payload == [252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [3, 255, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu4.payload == [0, 0, 3, 255, 255, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu5.payload == [0, 0, 0, 0, 0, 127, 252, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu6.payload == [0, 0, 0, 0, 0, 0, 3, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_pkt_6():
    
    signal_play = Signal('play', 5, 6, [0x3F]) # Endianness.BIG
    signal_stop = Signal('stop', 16, 11, [0x7, 0xFF])
    signal_pause = Signal('pause', 21, 5, [0x1F])
    signal_load = Signal('load', 40, 19, [7, 0xFF, 0xFF])
    signal_unload = Signal('Unload', 53, 13, [0x1F, 0xFF])
    signal_search_forward = Signal('searchForward', 59, 6, [0x3F])
    
    pdu1 = Pdu(Endianness.BIG, 9470064, 20)
    pdu2 = Pdu(Endianness.BIG, 1056816, 20)
    pdu3 = Pdu(Endianness.BIG, 4214880, 20)
    
    pdu1.add_signal(signal_play)
    pdu1.add_signal(signal_stop)
    pdu2.add_signal(signal_pause)
    pdu2.add_signal(signal_load)
    pdu3.add_signal(signal_unload)
    pdu3.add_signal(signal_search_forward)
    
    assert pdu1.payload == [255, 255, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [0, 0, 127, 255, 255, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 0, 0, 0, 127, 255, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_pkt_7():
    
    signal_no_magazine = Signal('NoMagazine', 6, 7, [0x7F]) # Endianness.BIG
    signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x1F])
    signal_disk_check = Signal('DiskCheck', 20, 9, [0x01, 0xFF])
    signal_disk_change = Signal('DiskChange', 23, 3, [7])
    signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x7, 0xFF])
    
    pdu1 = Pdu(Endianness.BIG, 2175297, 5)
    pdu2 = Pdu(Endianness.BIG, 2167621, 8)
    pdu3 = Pdu(Endianness.BIG, 8943382, 9)
    pdu4 = Pdu(Endianness.BIG, 8918886, 9)
    pdu5 = Pdu(Endianness.BIG, 8484710, 9)
    
    pdu1.add_signal(signal_no_magazine)
    pdu2.add_signal(signal_magazine_loaded)
    pdu3.add_signal(signal_disk_check)
    pdu4.add_signal(signal_disk_change)
    pdu5.add_signal(signal_magazine_status)
    
    assert pdu1.payload == [254, 0, 0, 0, 0]
    assert pdu2.payload == [1, 240, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 15, 248, 0, 0, 0, 0, 0, 0]
    assert pdu4.payload == [0, 0, 7, 0, 0, 0, 0, 0, 0]
    assert pdu5.payload == [0, 0, 0, 255, 224, 0, 0, 0, 0]

def test_pkt_8():
    
    signal_no_magazine = Signal('NoMagazine', 6, 7, [0x7F]) # Endianness.BIG
    signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x1F])
    signal_disk_check = Signal('DiskCheck', 20, 9, [0x01, 0xFF])
    signal_disk_change = Signal('DiskChange', 23, 3, [7])
    signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x7, 0xFF])
    
    pdu1 = Pdu(Endianness.BIG, 2236962, 5)
    pdu2 = Pdu(Endianness.BIG, 3355443, 8)
    pdu3 = Pdu(Endianness.BIG, 4473924, 9)
    
    pdu1.add_signal(signal_no_magazine)
    pdu2.add_signal(signal_magazine_loaded)
    pdu2.add_signal(signal_disk_check)
    pdu3.add_signal(signal_disk_change)
    pdu3.add_signal(signal_magazine_status)
        
    assert pdu1.payload == [254, 0, 0, 0, 0]
    assert pdu2.payload == [1, 255, 248, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 7, 255, 224, 0, 0, 0, 0]
    
def test_pkt_9():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x2F, 0x97]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x6B])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0x18, 0xBF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x3])
    signal_last_track = Signal('lastTrack', 43, 2, [0x01])
    
    pdu1 = Pdu(Endianness.BIG, 9991764, 10)
    pdu2 = Pdu(Endianness.BIG, 1644052, 10)
    pdu3 = Pdu(Endianness.BIG, 2631204, 10)
    pdu4 = Pdu(Endianness.BIG, 3683892, 10)
    pdu5 = Pdu(Endianness.BIG, 4736580, 10)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu3.add_signal(signal_media_file_system)
    pdu4.add_signal(signal_first_track)
    pdu5.add_signal(signal_last_track)
    
    assert pdu1.payload == [190, 92, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [0, 3, 88, 0, 0, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 6, 49, 126, 0, 0, 0, 0, 0]
    assert pdu4.payload == [0, 0, 0, 0, 0, 192, 0, 0, 0, 0]
    assert pdu5.payload == [0, 0, 0, 0, 0, 16, 0, 0, 0, 0]
    
def test_pkt_10():
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x2F, 0x97]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x6B])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0x18, 0xBF])
    signal_first_track = Signal('firstTrack', 41, 3, [0x3])
    signal_last_track = Signal('lastTrack', 43, 2, [0x01])
    
    pdu1 = Pdu(Endianness.BIG, 9991764, 10)
    pdu2 = Pdu(Endianness.BIG, 1644052, 10)
    pdu3 = Pdu(Endianness.BIG, 2631204, 10)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu2.add_signal(signal_media_file_system)
    pdu3.add_signal(signal_first_track)
    pdu3.add_signal(signal_last_track)
    
    assert pdu1.payload == [190, 92, 0, 0, 0, 0, 0, 0, 0, 0]
    assert pdu2.payload == [0, 3, 94, 49, 126, 0, 0, 0, 0, 0]
    assert pdu3.payload == [0, 0, 0, 0, 0, 208, 0, 0, 0, 0]
    
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