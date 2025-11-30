from signals.signal import *
from pdus.pdu_cyclic_timer import *
from pdus.pdu import *
from sockets.pdu_socket import *
from sockets.udp_pdu import *
from utils.ip_utils import *

def parse_json_file():
    pass

if __name__=='__main__':

    """
        s1 = Signal('Sadananda', 0, 16, [0x32, 0x85])
        s2 = Signal('Maharaj', 16, 16, [0x32, 0x85])
        s3 = Signal('Datta', 32, 16, [0x32, 0x85])
        s4 = Signal('Datta', 32, 16, [0x32, 0x85])
        s5 = Signal('Dattas', 32, 16, [0x32, 0x85])

        pdu1 = Pdu('big', 0x3285, 0x20)

        print(s5)

        pdu1.add_signal(s1)
        pdu1.add_signal(s2)
        pdu1.add_signal(s3)
        pdu1.add_signal(s4)

        pdu2 = Pdu('big', 0x1235, 0x21)

        pdu2.add_signal(s5)    

        p = Port()
        p.src_port = 32
        p.dst_port = 85

        ip_address = IpAddress()

        ip_address.src_ip = '127.0.0.1'
        ip_address.dst_ip = '127.0.0.2'

        print(p.src_port)

        u_socket = get_udp_socket(ip_address, p)
        print(type(u_socket))

        Udp = UdpPdu(p)

        Udp.add_protocol_data_unit(pdu1)
        Udp.add_protocol_data_unit(pdu2)


        from utils.udp_sender import *
        import time

        send_udp_packet(Udp, u_socket,  0, 0)
        time.sleep(1)
        print('------- second time ----------')
        send_udp_packet(Udp, u_socket, 1, float('inf'))

        time.sleep(20)

        stop_udp_packet(Udp)
    """

    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type = Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_tract = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track = Signal('lastTrack', 43, 2, [0x03])
    
    a = [0] * 10
    signal_media_title.update_signal_data(Endianness.BIG, a)
    print('Examining one signal',[hex(value) for value in a])  
    signal_media_type.update_signal_data(Endianness.BIG, a)
    print('Examining two signal',[hex(value) for value in a])  
# #    signal_media_file_system.update_signal_data(Endianness.BIG, a)
# #    signal_first_tract.update_signal_data(Endianness.BIG, a)
    signal_last_track.update_signal_data(Endianness.BIG, a)
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    pdu1.add_signal(signal_media_title)
    pdu1.payload
    pdu1.add_signal(signal_media_type)
    pdu1.payload
#  pdu1.add_signal(signal_media_file_system)
#  pdu1.add_signal(signal_first_tract)
    pdu1.add_signal(signal_last_track)
    
    print([hex(value) for value in a])  
    pdu1.payload
    
    pdu1.remove_signal(signal_media_title)
    pdu1.payload
    
    pdu1.remove_signal(signal_last_track)
    pdu1.payload

    # signal_play = Signal('Play', 5, 6, [0x3F]) # Endianness.BIG
    # signal_stop = Signal('Stop', 16, 11, [0x7, 0xFF])
    # signal_pause = Signal('Pause', 21, 5, [0x1F])
    # signal_load = Signal('Load', 40, 19, [0x7, 0xFF, 0xFF])
    # signal_unload = Signal('Unload', 53, 13, [0x1F, 0xFF])
    # signal_search_forward = Signal('SearchForward', 59, 6, [0x3F])

    # a = [0] * 10
    # signal_play.update_signal_data(Endianness.BIG, a)
    # signal_stop.update_signal_data(Endianness.BIG, a)
    # signal_pause.update_signal_data(Endianness.BIG, a)
    # signal_load.update_signal_data(Endianness.BIG, a)
    # signal_unload.update_signal_data(Endianness.BIG, a)
    # signal_search_forward.update_signal_data(Endianness.BIG, a)
    
    # pdu2 = Pdu(Endianness.BIG, 0x8932, 0x35)
    # pdu2.add_signal(signal_play)
    # pdu2.add_signal(signal_stop)
    # pdu2.add_signal(signal_pause)
    # pdu2.add_signal(signal_load)
    # pdu2.add_signal(signal_unload)
    # pdu2.add_signal(signal_search_forward)
    
    # print([hex(value) for value in a])
    
    
    # signal_no_magazine = Signal('NoMagazine', 6, 7, [0x7F]) # Endianness.BIG
    # signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x1F])
    # signal_disk_check = Signal('DiskCheck', 20, 9, [1, 0xFF])
    # signal_disk_change = Signal('DiskChange', 23, 3, [0x7])
    # signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x7, 0xFF])

    # a = [0] * 10
    # signal_no_magazine.update_signal_data(Endianness.BIG, a)
    # signal_magazine_loaded.update_signal_data(Endianness.BIG, a)
    # signal_disk_check.update_signal_data(Endianness.BIG, a)
    # signal_disk_change.update_signal_data(Endianness.BIG, a)
    # signal_magazine_status.update_signal_data(Endianness.BIG, a)
    
    # pdu3 = Pdu(Endianness.BIG, 0x5651, 0x15)
    # pdu3.add_signal(signal_no_magazine)
    # pdu3.add_signal(signal_magazine_loaded)
    # pdu3.add_signal(signal_disk_check)
    # pdu3.add_signal(signal_disk_change)
    # pdu3.add_signal(signal_magazine_status)
    
    # print([hex(value) for value in a])
    
    # # varying values 
    # signal_media_title = Signal('mediaTitle', 13, 14, [0x2F, 0x97]) # Endianness.BIG
    # signal_media_type = Signal('mediaType', 20, 7, [0x6B])
    # signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0x18, 0xBF])
    # signal_first_tract = Signal('firstTrack', 41, 3, [0x3])
    # signal_last_track = Signal('lastTrack', 43, 2, [0x01])

    # a = [0] * 10
    # signal_media_title.update_signal_data(Endianness.BIG, a)
    # signal_media_type.update_signal_data(Endianness.BIG, a)
    # signal_media_file_system.update_signal_data(Endianness.BIG, a)
    # signal_first_tract.update_signal_data(Endianness.BIG, a)
    # signal_last_track.update_signal_data(Endianness.BIG, a)
    
    # pdu4 = Pdu(Endianness.BIG, 0x5100, 0x21)
    # pdu4.add_signal(signal_media_title)
    # pdu4.add_signal(signal_media_type)
    # pdu4.add_signal(signal_media_file_system)
    # pdu4.add_signal(signal_first_tract)
    # pdu4.add_signal(signal_last_track)
    
    # print([hex(value) for value in a])    

    # signal_play = Signal('Play', 5, 6, [0x37]) # Endianness.BIG
    # signal_stop = Signal('Stop', 16, 11, [0x4, 0x3D])
    # signal_pause = Signal('Pause', 21, 5, [0x1D])
    # signal_load = Signal('Load', 40, 19, [0x6, 0x9A, 0xD3])
    # signal_unload = Signal('Unload', 53, 13, [0xC, 0xD5])
    # signal_search_forward = Signal('SearchForward', 59, 6, [0x38])

    # a = [0] * 10
    # signal_play.update_signal_data(Endianness.BIG, a)
    # signal_stop.update_signal_data(Endianness.BIG, a)
    # signal_pause.update_signal_data(Endianness.BIG, a)
    # signal_load.update_signal_data(Endianness.BIG, a)
    # signal_unload.update_signal_data(Endianness.BIG, a)
    # signal_search_forward.update_signal_data(Endianness.BIG, a)
    
    # pdu5 = Pdu(Endianness.BIG, 0x5153, 0x15)
    # pdu5.add_signal(signal_play)
    # pdu5.add_signal(signal_stop)
    # pdu5.add_signal(signal_pause)
    # pdu5.add_signal(signal_load)
    # pdu5.add_signal(signal_unload)
    # pdu5.add_signal(signal_search_forward)
    
    # print([hex(value) for value in a])
    
    
    # signal_no_magazine = Signal('NoMagazine', 6, 7, [0x4D]) # Endianness.BIG
    # signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x10])
    # signal_disk_check = Signal('DiskCheck', 20, 9, [1, 0xBC])
    # signal_disk_change = Signal('DiskChange', 23, 3, [0x2])
    # signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x4, 0x8])

    # a = [0] * 10
    # signal_no_magazine.update_signal_data(Endianness.BIG, a)
    # signal_magazine_loaded.update_signal_data(Endianness.BIG, a)
    # signal_disk_check.update_signal_data(Endianness.BIG, a)
    # signal_disk_change.update_signal_data(Endianness.BIG, a)
    # signal_magazine_status.update_signal_data(Endianness.BIG, a)
    
    # pdu6 = Pdu(Endianness.BIG, 0x1111, 0x17)
    # pdu6.add_signal(signal_no_magazine)
    # pdu6.add_signal(signal_magazine_loaded)
    # pdu6.add_signal(signal_disk_check)
    # pdu6.add_signal(signal_disk_change)
    # pdu6.add_signal(signal_magazine_status)
    
    # print([hex(value) for value in a])
    
    # print("#" * 95)
        
    # signal_no_disk = Signal('No_Disk', 0, 4, [0xF]) # Endianness.BIG
    # signal_audio = Signal('Audio', 4, 7, [0x7F])
    # signal_video = Signal('Video', 11, 11, [0x7, 0xFF])
    # signal_rom = Signal('ROM', 22, 2, [0x3])
    # signal_mixed = Signal('Mixed', 24, 5, [0x1F])

    # a = [0] * 10
    # signal_no_disk.update_signal_data(Endianness.SMALL, a)
    # signal_audio.update_signal_data(Endianness.SMALL, a)
    # signal_video.update_signal_data(Endianness.SMALL, a)
    # signal_rom.update_signal_data(Endianness.SMALL, a)
    # signal_mixed.update_signal_data(Endianness.SMALL, a)
    
    # pdu7 = Pdu(Endianness.SMALL, 0x1212, 0x19)
    # pdu7.add_signal(signal_no_disk)
    # pdu7.add_signal(signal_audio)
    # pdu7.add_signal(signal_video)
    # pdu7.add_signal(signal_rom)
    # pdu7.add_signal(signal_mixed)
    
    # print([hex(value) for value in a])
    
    # signal_bridge_disc = Signal('BridgeDisc', 0, 5, [0x1F]) # Endianness.BIG
    # signal_joliet = Signal('Joliet', 5, 11, [0x7, 0xFF])
    # signal_photo_cd = Signal('PhotoCD', 16, 8, [0xFF])
    # signal_cd_extra = Signal('CDExtra', 24, 14, [0x3F, 0xFF])
    # signal_udf = Signal('UDF', 38, 8, [0xFF])

    # a = [0] * 10
    # signal_bridge_disc.update_signal_data(Endianness.SMALL, a)
    # signal_joliet.update_signal_data(Endianness.SMALL, a)
    # signal_photo_cd.update_signal_data(Endianness.SMALL, a)
    # signal_cd_extra.update_signal_data(Endianness.SMALL, a)
    # signal_udf.update_signal_data(Endianness.SMALL, a)
    
    # print('sadananda',[hex(value) for value in a])
    
    # pdu7 = Pdu(Endianness.SMALL, 0x1234, 0x15)
    # pdu7.add_signal(signal_bridge_disc)
    # pdu7.add_signal(signal_joliet)
    # pdu7.add_signal(signal_photo_cd)
    # pdu7.add_signal(signal_cd_extra)
    # pdu7.add_signal(signal_udf)
    
    
    
    # signal_e_motor_speed = Signal('EMotorSpeed', 0, 3, [0x7]) 
    # signal_e_motor_temperature = Signal('EMotorTemperature', 3, 10, [0x3, 0xFF])
    # signal_e_motor_current = Signal('EMotorCurrent', 13, 10, [0x03, 0xFF])
    # signal_e_motor_power = Signal('EMotorPower', 23, 13, [0x1F, 0xFF])

    # a = [0] * 10
    # signal_e_motor_speed.update_signal_data(Endianness.SMALL, a)
    # signal_e_motor_temperature.update_signal_data(Endianness.SMALL, a)
    # signal_e_motor_current.update_signal_data(Endianness.SMALL, a)
    # signal_e_motor_power.update_signal_data(Endianness.SMALL, a)
    
    # pdu8 = Pdu(Endianness.SMALL, 0x1234, 0x15)
    # pdu8.add_signal(signal_e_motor_speed)
    # pdu8.add_signal(signal_e_motor_temperature)
    # pdu8.add_signal(signal_e_motor_current)
    # pdu8.add_signal(signal_e_motor_power)
    
    # print([hex(value) for value in a])
    
    # signal_rpm_cm = Signal('RpmCM', 0, 4, [0xB]) 
    # signal_temperature_cm = Signal('TemperatureCM', 4, 7, [0x69])
    # signal_current_cm = Signal('CurrentCM', 11, 11, [0x04, 0x8])
    # signal_power_cm = Signal('PowerCM', 22, 2, [0x2])
    # signal_rpm_unit = Signal('RpmUnit', 24, 5, [0x1A])

    # a = [0] * 10
    # signal_rpm_cm.update_signal_data(Endianness.SMALL, a)
    # signal_temperature_cm.update_signal_data(Endianness.SMALL, a)
    # signal_current_cm.update_signal_data(Endianness.SMALL, a)
    # signal_power_cm.update_signal_data(Endianness.SMALL, a)
    # signal_rpm_unit.update_signal_data(Endianness.SMALL, a)
    
    # print([hex(value) for value in a])
    
    

    # signal_Lane_detection = Signal('LaneDetection_Sig', 0, 5, [0x17]) 
    # signal_traffic_sign_detection = Signal('TrafficSignDetection_Sig', 5, 11, [3, 0xF2])
    # signal_start_stop_response = Signal('StartStopResponseSig', 16, 8, [0xCD])
    # signal_frame_rate_notifier = Signal('FrameRate_NotifierSig', 24, 14, [0x3B, 0xB5])
    # signal_frame_rate_getter_resp = Signal('FrameRate_GetterRespSig', 38, 8, [0x20])

    # a = [0] * 10
    # signal_Lane_detection.update_signal_data(Endianness.SMALL, a)
    # signal_traffic_sign_detection.update_signal_data(Endianness.SMALL, a)
    # signal_start_stop_response.update_signal_data(Endianness.SMALL, a)
    # signal_frame_rate_notifier.update_signal_data(Endianness.SMALL, a)
    # signal_frame_rate_getter_resp.update_signal_data(Endianness.SMALL, a)
    
    # print([hex(value) for value in a])
    
    
    # signal_Lane_detection = Signal('FrameRate_Notifier', 0, 3, [0x3]) 
    # signal_traffic_sign_detection = Signal('FrameRate_GetterRqst', 3, 10, [3, 0x87])
    # signal_start_stop_response = Signal('FrameRate_GetterResp', 13, 10, [0x3, 0xE9])
    # signal_frame_rate_notifier = Signal('FrameRate_SetterRqst', 23, 13, [0x7, 0x1B])

    # a = [0] * 10
    # signal_Lane_detection.update_signal_data(Endianness.SMALL, a)
    # signal_traffic_sign_detection.update_signal_data(Endianness.SMALL, a)
    # signal_start_stop_response.update_signal_data(Endianness.SMALL, a)
    # signal_frame_rate_notifier.update_signal_data(Endianness.SMALL, a)
    
    # print([hex(value) for value in a])
    
    
    