
def get_ip():
    from netifaces import interfaces, ifaddresses, AF_INET

    all_ip_addresses = []
    for ifacename in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifacename).setdefault( AF_INET,
            [{'addr':'No IP Address'}] )]
        for address in addresses:
            all_ip_addresses.append(address)

    local_net_ip_addresses = [x for x in all_ip_addresses if x.startswith("192")]
    return local_net_ip_addresses[0]

if __name__ == '__main__':
    print get_ip()
