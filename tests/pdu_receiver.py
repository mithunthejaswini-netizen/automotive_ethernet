import socket
import threading

sockets = [

("fd12:3285:378::15",1999),
("fd12:3285:378::15",6661),
("fd12:3285:378::15",6666),
("fd12:3285:378::15",9199),
("fd12:3285:378::15",9919),
("fd12:3285:378::15",9991),
("fd12:3285:378::15",9999),

("fd12:3285:378::8532",3285),
("fd13:3285:378::3285",3285),

("fd13:3285:378::40",1444),
("fd13:3285:378::40",1777),
("fd13:3285:378::40",4144),
("fd13:3285:378::40",4414),
("fd13:3285:378::40",4444),
("fd13:3285:378::40",6166),
("fd13:3285:378::40",6616),

("fd14:3285:378::50",2222),
("fd14:3285:378::50",5555),

("ff12::baba",1111),
("ff13::baba",6666),
("ff14::1fa",2222),
("ff15::1fb",1111)

]


def receiver(ip, port):

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    print(f"Listening on [{ip}]:{port}")

    while True:
        data, addr = sock.recvfrom(4096)

        print("\nPacket Received")
        print("From:", addr)
        print("To:", ip, port)
        print("Length:", len(data))
        print("Payload:", data.hex())


threads = []

for ip, port in sockets:
    t = threading.Thread(target=receiver, args=(ip, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()