from signals.signal import *
from pdus.pdu_cyclic_timer import *
from pdus.pdu import *
from sockets.pdu_socket import *
from sockets.udp_pdu import *
from utils.ip_utils import *

def parse_json_file():
    pass

if __name__=='__main__':
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x3F, 0xFF]) # Endianness.BIG
    signal_media_type =  Signal('mediaType', 20, 7, [0x7F])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0xFF, 0xFF])
    signal_first_tract = Signal('firstTrack', 41, 3, [0x7])
    signal_last_track =  Signal('lastTrack', 43, 2, [0x03])

    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    
    pdu1.add_signal(signal_media_title)
    pdu1.add_signal(signal_media_type)
    pdu1.add_signal(signal_media_file_system)
    pdu1.add_signal(signal_first_tract)
    pdu1.add_signal(signal_last_track)
    
    
    #### build one UDP frame and send
    
    pdu1.remove_signal(signal_media_type)
    
    ### build one UDP frame and send
    
    #---------------------------------------------
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    pdu2 = Pdu(Endianness.BIG, 0x5600, 0x20)
    pdu3 = Pdu(Endianness.BIG, 0x378, 0x20)
    pdu4 = Pdu(Endianness.BIG, 0x9842, 0x20)
    pdu5 = Pdu(Endianness.BIG, 0x1234, 0x20)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu3.add_signal(signal_media_file_system)
    pdu4.add_signal(signal_first_tract)
    pdu5.add_signal(signal_last_track)
    
    # build udp frame and send
    #---------------------------------------------
    
    pdu1 = Pdu(Endianness.BIG, 0x3285, 0x20)
    pdu2 = Pdu(Endianness.BIG, 0x5600, 0x20)
    pdu3 = Pdu(Endianness.BIG, 0x378, 0x20)
    
    pdu1.add_signal(signal_media_title)
    
    pdu2.add_signal(signal_media_type)
    pdu2.add_signal(signal_media_file_system)
    
    pdu3.add_signal(signal_first_tract)
    pdu3.add_signal(signal_last_track)
    
    ##-------------------------------------------
    
    # SIGNAL SET 2
    
    signal_play = Signal('Play', 5, 6, [0x3F]) # Endianness.BIG
    signal_stop = Signal('Stop', 16, 11, [0x7, 0xFF])
    signal_pause = Signal('Pause', 21, 5, [0x1F])
    signal_load = Signal('Load', 40, 19, [0x7, 0xFF, 0xFF])
    signal_unload = Signal('Unload', 53, 13, [0x1F, 0xFF])
    signal_search_forward = Signal('SearchForward', 59, 6, [0x3F])
    
    pdu1 = Pdu(0x123456, 15)
    pdu2 = Pdu(0x112233, 15)
    pdu3 = Pdu(0x223344, 15)
    pdu4 = Pdu(0x560051, 15)
    pdu5 = Pdu(0x314151, 15)
    pdu6 = Pdu(0x356576, 15)
    
    pdu1.add_signal(signal_play)
    pdu2.add_signal(signal_stop)
    pdu3.add_signal(signal_pause)
    pdu4.add_signal(signal_load)
    pdu5.add_signal(signal_unload)
    pdu6.add_signal(signal_search_forward)
    
    ##3 build udp frame and send
    
    pdu1 = Pdu(0x908070, 15)
    pdu2 = Pdu(0x102030, 15)
    pdu3 = Pdu(0x405060, 15)
    
    pdu1.add_signal(signal_play)
    pdu1.add_signal(signal_stop)
    pdu2.add_signal(signal_pause)
    pdu2.add_signal(signal_load)
    pdu3.add_signal(signal_unload)
    pdu3.add_signal(signal_search_forward)

    ################ send udp frame ################
    signal_no_magazine = Signal('NoMagazine', 6, 7, [0x7F]) # Endianness.BIG
    signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x1F])
    signal_disk_check = Signal('DiskCheck', 20, 9, [1, 0xFF])
    signal_disk_change = Signal('DiskChange', 23, 3, [0x7])
    signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x7, 0xFF])    
    
    pdu1 = Pdu(0x213141, 5)
    pdu2 = Pdu(0x211345, 8)
    pdu3 = Pdu(0x887716, 9)
    pdu4 = Pdu(0x881766, 9)
    pdu5 = Pdu(0x817766, 9)
    
    pdu1.add_signal(signal_no_magazine)
    pdu2.add_signal(signal_magazine_loaded)
    pdu3.add_signal(signal_disk_check)
    pdu4.add_signal(signal_disk_change)
    pdu5.add_signal(signal_magazine_status)
    
    ### send upd frame
    
    pdu1 = Pdu(0x222222, 5)
    pdu2 = Pdu(0x333333, 8)
    pdu3 = Pdu(0x444444, 9)
    
    pdu1.add_signal(signal_no_magazine)
    pdu2.add_signal(signal_magazine_loaded)
    pdu2.add_signal(signal_disk_check)
    pdu3.add_signal(signal_disk_change)
    pdu3.add_signal(signal_magazine_status)
    
    ################ send udp frame
    
    signal_media_title = Signal('mediaTitle', 13, 14, [0x2F, 0x97])
    signal_media_type = Signal('mediaType', 20, 7, [0x6B])
    signal_media_file_system = Signal('mediaFileSystem', 38, 18, [0x03, 0x18, 0xBF])
    signal_first_tract = Signal('firstTrack', 41, 3, [0x3])
    signal_last_track = Signal('lastTrack', 43, 2, [0x01])
    
    pdu1 = Pdu(0x987654, 0x10)
    pdu2 = Pdu(0x191614, 0x10)
    pdu3 = Pdu(0x282624, 0x10)
    pdu4 = Pdu(0x383634, 0x10)
    pdu5 = Pdu(0x484644, 0x10)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_type)
    pdu3.add_signal(signal_media_file_system)
    pdu4.add_signal(signal_first_tract)
    pdu5.add_signal(signal_last_track)
    
    ### build udp frame
    
    pdu1 = Pdu(0x987654, 0x10)
    pdu2 = Pdu(0x191614, 0x10)
    pdu3 = Pdu(0x282624, 0x10)
    pdu4 = Pdu(0x383634, 0x10)
    pdu5 = Pdu(0x484644, 0x10)
    
    pdu1.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_title)
    pdu2.add_signal(signal_media_title)
    pdu3.add_signal(signal_media_title)
    pdu3.add_signal(signal_media_title)
    
    ## BIG
    signal_play = Signal('Play', 5, 6, [0x37]) # Endianness.BIG
    signal_stop = Signal('Stop', 16, 11, [0x4, 0x3D])
    signal_pause = Signal('Pause', 21, 5, [0x1D])
    signal_load = Signal('Load', 40, 19, [0x6, 0x9A, 0xD3])
    signal_unload = Signal('Unload', 53, 13, [0xC, 0xD5])
    signal_search_forward = Signal('SearchForward', 59, 6, [0x38])
    
    pdu1 = Pdu(0x123456, 0x8)
    pdu2 = Pdu(0x223355, 0x8)
    pdu3 = Pdu(0x333444, 0x8)
    pdu4 = Pdu(0x444555, 0x8)
    pdu5 = Pdu(0x555666, 0x8)
    pdu6 = Pdu(0x151616, 0x8)
    
    pdu1.add_signal(signal_play)
    pdu2.add_signal(signal_stop)
    pdu3.add_signal(signal_pause)
    pdu4.add_signal(signal_load)
    pdu5.add_signal(signal_unload)
    pdu6.add_signal(signal_search_forward)
    
    ################### build udp frame and send ########################
    
    ## BIG
    signal_no_magazine = Signal('NoMagazine', 6, 7, [0x4D]) # Endianness.BIG
    signal_magazine_loaded = Signal('Magazine_Loaded', 11, 5, [0x10])
    signal_disk_check = Signal('DiskCheck', 20, 9, [1, 0xBC])
    signal_disk_change = Signal('DiskChange', 23, 3, [0x2])
    signal_magazine_status = Signal('Magazine_Status', 34, 11, [0x4, 0x8])
    
    pdu1 = Pdu(0x112233, 0x6)
    pdu2 = Pdu(0x445566, 0x6)
    pdu3 = Pdu(0x778899, 0x6)
    pdu4 = Pdu(0x102030, 0x6)
    pdu5 = Pdu(0x405060, 0x6)
    
    pdu1.add_signal(signal_no_magazine)
    pdu2.add_signal(signal_magazine_loaded)
    pdu3.add_signal(signal_disk_check)
    pdu4.add_signal(signal_disk_change)
    pdu5.add_signal(signal_magazine_status)
    
    pdu1 = Pdu(0x112233, 0x6)
    pdu2 = Pdu(0x445566, 0x6)
    
    pdu1.add_signal(signal_no_magazine)
    pdu1.add_signal(signal_magazine_loaded)
    pdu2.add_signal(signal_disk_check)
    pdu2.add_signal(signal_disk_change)
    pdu2.add_signal(signal_magazine_status)
    
    
    ## SMALL
    signal_no_disk = Signal('No_Disk', 0, 4, [0xF]) # Endianness.BIG
    signal_audio = Signal('Audio', 4, 7, [0x7F])
    signal_video = Signal('Video', 11, 11, [0x7, 0xFF])
    signal_rom = Signal('ROM', 22, 2, [0x3])
    signal_mixed = Signal('Mixed', 24, 5, [0x1F])
    
    pdu1 = Pdu(0x112233, 0x5)
    pdu2 = Pdu(0x445566, 0x5)
    pdu3 = Pdu(0x778899, 0x5)
    pdu4 = Pdu(0x998877, 0x5)
    pdu5 = Pdu(0x554433, 0x5)

    pdu1.add_signal(signal_no_disk)
    pdu2.add_signal(signal_audio)
    pdu3.add_signal(signal_video)
    pdu4.add_signal(signal_rom)
    pdu5.add_signal(signal_mixed)
    
    #### build and send udp
    
    pdu1 = Pdu(0x102030, 0x5)
    pdu2 = Pdu(0x405060, 0x5)
    pdu3 = Pdu(0x718191, 0x5)

    pdu1.add_signal(signal_no_disk)
    pdu2.add_signal(signal_audio)
    pdu3.add_signal(signal_video)
    pdu3.add_signal(signal_rom)
    pdu3.add_signal(signal_mixed)
    
    #### build and send udp
    
    ## SMALL
    signal_bridge_disc = Signal('BridgeDisc', 0, 5, [0x1F]) # Endianness.BIG
    signal_joliet = Signal('Joliet', 5, 11, [0x7, 0xFF])
    signal_photo_cd = Signal('PhotoCD', 16, 8, [0xFF])
    signal_cd_extra = Signal('CDExtra', 24, 14, [0x3F, 0xFF])
    signal_udf = Signal('UDF', 38, 8, [0xFF])
    
    pdu1 = Pdu(0xAABBCC, 0x5)
    pdu2 = Pdu(0xBBCCDD, 0x5)
    pdu3 = Pdu(0xDDEEFF, 0x5)
    pdu4 = Pdu(0xFFEEDD, 0x5)
    pdu5 = Pdu(0xEEDDAA, 0x5)
    
    pdu1.add_signal(signal_bridge_disc)
    pdu2.add_signal(signal_joliet)
    pdu3.add_signal(signal_photo_cd)
    pdu4.add_signal(signal_cd_extra)
    pdu5.add_signal(signal_udf)
    
    pdu1 = Pdu(0xABCDEF, 0x10)
    pdu2 = Pdu(0xFEDCBA, 0x10)
    
    pdu1.add_signal(signal_bridge_disc)
    pdu1.add_signal(signal_joliet)
    pdu2.add_signal(signal_photo_cd)
    pdu2.add_signal(signal_cd_extra)
    pdu2.add_signal(signal_udf)
    
    #### build udp and send
    
    ## SMALL
    signal_e_motor_speed = Signal('EMotorSpeed', 0, 3, [0x7]) 
    signal_e_motor_temperature = Signal('EMotorTemperature', 3, 10, [0x3, 0xFF])
    signal_e_motor_current = Signal('EMotorCurrent', 13, 10, [0x03, 0xFF])
    signal_e_motor_power = Signal('EMotorPower', 23, 13, [0x1F, 0xFF])
    
    pdu1 = Pdu(0xCABBAD, 0x5)
    pdu2 = Pdu(0xBABADA, 0x5)
    pdu3 = Pdu(0xBFBFAA, 0x5)
    pdu4 = Pdu(0xDEEDAD, 0x5)
    
    pdu1.add_signal(signal_e_motor_speed)
    pdu2.add_signal(signal_e_motor_temperature)
    pdu3.add_signal(signal_e_motor_current)
    pdu4.add_signal(signal_e_motor_power)
    
    
    pdu1 = Pdu(0xCADCAD, 0x5)
    pdu2 = Pdu(0xBABABA, 0x5)
    
    pdu1.add_signal(signal_e_motor_speed)
    pdu1.add_signal(signal_e_motor_temperature)
    pdu2.add_signal(signal_e_motor_current)
    pdu2.add_signal(signal_e_motor_power)
    
    ## build udp frame
    
    ### SMALL ENDIAN
    signal_rpm_cm = Signal('RpmCM', 0, 4, [0xB]) 
    signal_temperature_cm = Signal('TemperatureCM', 4, 7, [0x69])
    signal_current_cm = Signal('CurrentCM', 11, 11, [0x04, 0x8])
    signal_power_cm = Signal('PowerCM', 22, 2, [0x2])
    signal_rpm_unit = Signal('RpmUnit', 24, 5, [0x1A])
    
    pdu1 = Pdu(0xABBACE, 0x5)
    pdu2 = Pdu(0xDEADCE, 0x5)
    pdu3 = Pdu(0xDADACE, 0x5)
    pdu4 = Pdu(0xDEEDCE, 0x5)
    pdu5 = Pdu(0xAEEDCE, 0x5)
    
    pdu1.add_signal(signal_rpm_cm)
    pdu2.add_signal(signal_temperature_cm)
    pdu3.add_signal(signal_current_cm)
    pdu4.add_signal(signal_power_cm)
    pdu5.add_signal(signal_rpm_unit)
    
    pdu1 = Pdu(0xAFDECA, 0x5)
    pdu2 = Pdu(0xAFEDAC, 0x5)
    
    pdu1.add_signal(signal_rpm_cm)
    pdu1.add_signal(signal_temperature_cm)
    pdu2.add_signal(signal_current_cm)
    pdu2.add_signal(signal_power_cm)
    pdu2.add_signal(signal_rpm_unit)
    
    ### SMALL ENDIAN
    signal_Lane_detection = Signal('LaneDetection_Sig', 0, 5, [0x17]) 
    signal_traffic_sign_detection = Signal('TrafficSignDetection_Sig', 5, 11, [3, 0xF2])
    signal_start_stop_response = Signal('StartStopResponseSig', 16, 8, [0xCD])
    signal_frame_rate_notifier = Signal('FrameRate_NotifierSig', 24, 14, [0x3B, 0xB5])
    signal_frame_rate_getter_resp = Signal('FrameRate_GetterRespSig', 38, 8, [0x20])
    
    pdu1 = Pdu(0xBBCCDD, 0x5)
    pdu2 = Pdu(0xBADACA, 0x5)
    pdu3 = Pdu(0xABDBCB, 0x5)
    pdu4 = Pdu(0xBCACDC, 0x5)
    pdu5 = Pdu(0xBCACDA, 0x5)
    
    pdu1.add_signal(signal_Lane_detection)
    pdu2.add_signal(signal_traffic_sign_detection)
    pdu3.add_signal(signal_start_stop_response)
    pdu4.add_signal(signal_frame_rate_notifier)
    pdu5.add_signal(signal_frame_rate_getter_resp)
    
    
    pdu1 = Pdu(0xDCDCDC, 0x5)
    pdu2 = Pdu(0xBCBCBC, 0x5)
    
    pdu1.add_signal(signal_Lane_detection)
    pdu1.add_signal(signal_traffic_sign_detection)
    pdu2.add_signal(signal_start_stop_response)
    pdu2.add_signal(signal_frame_rate_notifier)
    pdu2.add_signal(signal_frame_rate_getter_resp)
    
    ### SMALL ENDIAN
    
    signal_frame_rate_notifier = Signal('FrameRate_Notifier', 0, 3, [0x3]) 
    signal_frame_rate_getter_request = Signal('FrameRate_GetterRqst', 3, 10, [3, 0x87])
    signal_frame_rate_getter_response = Signal('FrameRate_GetterResp', 13, 10, [0x3, 0xE9])
    signal_frame_rate_setter_request = Signal('FrameRate_SetterRqst', 23, 13, [0x7, 0x1B])
    
    pdu1 = Pdu(0xABACAC, 0x5)
    pdu2 = Pdu(0xABBACA, 0x5)
    pdu3 = Pdu(0xABADDC, 0x5)
    pdu4 = Pdu(0xABDACA, 0x5)
    
    pdu1.add_signal(signal_frame_rate_notifier)
    pdu2.add_signal(signal_frame_rate_getter_request)
    pdu3.add_signal(signal_frame_rate_getter_response)
    pdu4.add_signal(signal_frame_rate_setter_request)
    
    pdu1 = Pdu(0xCAACAA, 0x5)
    pdu2 = Pdu(0xAAEEFF, 0x5)
    
    pdu1.add_signal(signal_frame_rate_notifier)
    pdu1.add_signal(signal_frame_rate_getter_request)
    pdu2.add_signal(signal_frame_rate_getter_response)
    pdu2.add_signal(signal_frame_rate_setter_request)