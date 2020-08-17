import logging
from datetime import datetime
import subprocess
import sys
 
#This will suppress all messages that have a lower level of seriousness than error messages, while running or loading Scapy
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)
 
 
try:
    from scapy.all import *
 
except ImportError:
    print("Scapy package for Python is not installed on your system.")
    sys.exit()