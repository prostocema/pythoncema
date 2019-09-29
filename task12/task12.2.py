import ipaddress

iplist = ['10.0.0.1', '192.168.0.1-3', '127.0.0.1-127.0.0.5']

def convert_ranges_to_ip_list(ip_list):

    flist = []
    for ip in ip_list:
        if str(ip).find('-') != -1:
            if len(ip[ip.find('-') + 1:]) > 3:
                ipp = int(ipaddress.ip_address(ip[ip.find('-') + 1:])) 
                ipm = int(ipaddress.ip_address(ip[:ip.find('-')]))
                ipmm = ipaddress.ip_address(ip[:ip.find('-')])
                ipr = ipp - ipm + 1
                for i in range(ipr):
                    flist.append(str(ipmm + i))
            else:
                iptolist = ip.split('.')
                iptolist.pop(-1)
                iptolist.append(ip[ip.find('-') + 1:])
                ipt = '.'.join(iptolist)
                ipp = int(ipaddress.ip_address(ipt))

                # iptolist.split
                ipm = int(ipaddress.ip_address(ip[:ip.find('-')]))
                ipmm = ipaddress.ip_address(ip[:ip.find('-')])
                ipr = ipp - ipm + 1
                for i in range(ipr):
                    flist.append(str(ipmm + i))
                
        else:
            flist.append(ip)
    return flist

bicema = convert_ranges_to_ip_list(iplist)
print(bicema)