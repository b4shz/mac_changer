import subprocess
import optparse
import os
from sys import exit
from time import sleep

if os.getuid() != 0:
	print("[!] This script must be run as root.")
	exit(1)

parser = optparse.OptionParser()
parser.add_option("-i", dest="interface", help="interface to change the mac address.")
parser.add_option("-m", dest="mac", help="your new mac address")
(options, arguments) = parser.parse_args()
interface = options.interface
mac = options.mac

print("[+] Changing your mac to", mac, "in", interface)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
sleep(1.5)
print("[!] Now your mac address is", mac)
