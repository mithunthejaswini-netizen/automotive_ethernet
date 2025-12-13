from threading import Timer
import time

def send_udp(
        udp_packet,
        udp_socket
    ):

    """
    Send a single UDP packet using the specified socket.

    :param UdpPdu udp_packet: The encoded UDP PDU object containing payload data.
    :param socket.socket udp_socket: The UDP socket through which the packet is sent.
    :returns: None
    :rtype: None
    
    """

    print(type(udp_socket))

    udp_packet.udp_payload()
    udp_socket.send(time.strftime("%Y-%m-%d %H:%M:%S").encode())

class CyclicTimer(Timer):

    """
    A repeating (cyclic) timer based on ``threading.Timer``.

    Unlike the standard ``Timer`` which runs only once, ``CyclicTimer`` repeatedly
    executes the target function at fixed time intervals until the timer is cancelled.

    The timer calls the provided function with the given arguments on every cycle.
    Cancellation stops further executions immediately.
    """

    def run(self):
        while not self.finished.wait(self.interval):                     
            self.function(*self.args, **self.kwargs)