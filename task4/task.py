#4.1

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('Fast', 'Gigabit')
print(NAT)

#4.2

mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', '.')
print(mac)

#4.3

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config = (config.split()[-1]).split(',')
print(config)

#4.4

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans = sorted(set(vlans))
print(vlans)

#4.5

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1 = set((command1.split()[-1]).split(','))
command2 = set((command2.split()[-1]).split(','))
command3 = list(command1 & command2)
print(sorted(command3))

#4.6

ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()

#print(ospf_route)

ospf_route1 = '''
Protocol:            {}
Prefix:              {}         
AD/Metric:           {}
Next-Hop:            {}
Last update:         {}
Outbound Interface:  {}
'''

print(ospf_route1.format(ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[4],
ospf_route[5],  ospf_route[6]))

#4.7

macc = 'AAAA:BBBB:CCCC'
macc = bin(int('AAAABBBBCCCC', 16))[2:]
print(macc)

#4.8

ip = '192.168.3.1'
ip = '''
IP address:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip.format(192, 168, 3, 1))