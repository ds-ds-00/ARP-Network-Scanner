#!/usr/bin/python 
import scapy.all as scapy
import argparse,requests,ipaddress
from tabulate import tabulate

def save_to_file(clients, filename):
    with open(filename, "w") as f:
        for client in clients:
            f.write(f"{client['ip']}\t{client['mac']}\t{client['vendor']}\n")

def validate_ip(ip):
    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError:
        return False

def get_arguments():
    parser=argparse.ArgumentParser(description="network scanner")
    parser.add_argument("-i","--ip",dest="ip",help="target ip address",metavar="",required=True) 
    parser.add_argument("-v","--verbose",action="store_true",help="verbosity") 
    parser.add_argument("-o", "--output", help="Save output to file")
    args=parser.parse_args()
    return args

def scan(ip,verbose):
   broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   arp_request_broadcast=broadcast/scapy.ARP(pdst=ip)
   ans_list,unans_list= scapy.srp(arp_request_broadcast,timeout=1,verbose=verbose) 
   client_list = []
   for  element in ans_list:
      vendor=get_vendor(element[1].hwsrc)
      client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc,"vendor":vendor}
      client_list.append(client_dict)
   return client_list
   
def display(clients):
    table = []
    for client in clients:
        table.append([
            client["ip"],
            client["mac"],
            client["vendor"]
        ])

    print(tabulate(table, headers=["IP", "MAC", "Vendor"], tablefmt="grid"))

def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url, timeout=2)

        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except:
        return "Unknown"


if __name__== "__main__":
   args=get_arguments()
   if not validate_ip(args.ip):
        print("Invalid IP or range!")
        exit(1)

   clients = scan(args.ip, args.verbose)
   display(clients)

   if args.output:
      save_to_file(clients, args.output)
      print(f"\nResults saved to {args.output}")

