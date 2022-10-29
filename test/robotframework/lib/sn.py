from time import sleep
from scapy.all import *

import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
OUPUT_PATH = os.path.join(FILE_PATH, "../output") 

class sn:

    def Start(self, numero="0"):
        try:
            self.snif = AsyncSniffer(iface="lo", count=0, store=True) # filter="" ip and tcp and port 8000
            self.snif.start()
            sleep(1)
            packet = IP(dst="127.0.0.1", src="127.0.0.1")/TCP()/Raw(str.encode("TEST NUMERO " + numero))
            send(packet)
        except Exception as e:
            return e
       
        return 0

    def Stop(self):
        try:
            data = self.snif.stop()
            wrpcap(os.path.join(OUPUT_PATH, "cap.pcap"), data)
        except Exception as e:
            return e

        return 0

# if __name__ == "__main__":
#     t = sn()
#     t.start()
#     sleep(5)s
#     t.stop()