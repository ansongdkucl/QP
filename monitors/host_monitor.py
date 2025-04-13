import scapy.all as scapy


def discover_hosts(subnet_address):
    
    print(f'\n---------Discovering hosts on {subnet_address} ----------')
    ans, unans  = scapy.arping(subnet_address)
    ans.summary()
    print(ans)

def main():

    #subnet_address = '192.168.1.0/24'
    subnet_address = "172.17.57.240/32"
    discover_hosts(subnet_address)
    

if __name__== "__main__":
    try:
    
        main()

    except KeyboardInterrupt:
        print("\n\nExiting monitor")
