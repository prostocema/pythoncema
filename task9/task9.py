#TASK 9.1

# access_mode_template = [
#     'switchport mode access', 'switchport access vlan',
#     'switchport nonegotiate', 'spanning-tree portfast',
#     'spanning-tree bpduguard enable'
# ]

# access_config = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17
# }

# def generate_access_config(intf_vlan_mapping, access_template):
#     #mcdiman = list(intf_vlan_mapping.keys())
#     config = ''
#     for i in intf_vlan_mapping:
#         config += 'interface ' + i + '\n'
#         for j in access_template:
#             config1 = j
#             if j != 'switchport access vlan':
#                 config1 += '\n'
#             if j == 'switchport access vlan':
#                 time = intf_vlan_mapping.get(i)
#                 config1 = config1 + ' ' + str(time) + '\n' 
#             config += config1
#     config = config.split('\n')
#     return config

# kek = generate_access_config(access_config, access_mode_template)
# print(kek)

#TASK 9.1a

# access_mode_template = [
#     'switchport mode access', 'switchport access vlan',
#     'switchport nonegotiate', 'spanning-tree portfast',
#     'spanning-tree bpduguard enable'
# ]

# access_config = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17
# }

# port_security_template = [
#     'switchport port-security maximum 2',
#     'switchport port-security violation restrict',
#     'switchport port-security'
# ]

# def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):

#     config = ''
#     for i in intf_vlan_mapping:
#         config += 'interface ' + i + '\n'
#         for j in access_template:
#             config1 = j
#             if j != 'switchport access vlan':
#                 config1 += '\n'
#                 config += config1
#             if j == 'switchport access vlan':
#                 time = intf_vlan_mapping.get(i)
#                 config1 = config1 + ' ' + str(time) + '\n'
#                 config += config1
#         if psecurity != None:
#             for u in psecurity:
#                 config1 = u + ' ' + '\n'
#                 config += config1
#                 # break
#         # config += config1
#     config = config.split('\n')
#     config = config[:-1]
#     return config

# kek = generate_access_config(access_config, access_mode_template, port_security_template)
# print(kek)

#TASK 9.2

# trunk_mode_template = [
#     'switchport mode trunk', 'switchport trunk native vlan 999',
#     'switchport trunk allowed vlan'
# ]

# trunk_config = {
#     'FastEthernet0/1': [10, 20, 30],
#     'FastEthernet0/2': [11, 30],
#     'FastEthernet0/4': [17]
# }

# def generate_trunk_config(trunk_mode_template, trunk_config):

#     config = ''
#     for i in trunk_config:
#         config += 'interface ' + i + '\n'
#         for j in trunk_mode_template:
#             config1 = j
#             if j != 'switchport trunk allowed vlan':
#                 config1 += '\n'
#                 config += config1
#                 continue
#             if j == 'switchport trunk allowed vlan':
#                 time = trunk_config.get(i)
#                 config1 = (config1 + ' ' + str(time).strip('[]') + '\n')
#                 config += config1
#         # config += config1
#     config = config.split('\n')
#     config = config[:-1]
#     return config

# kek = generate_trunk_config(trunk_mode_template, trunk_config)
# print(kek)

#TASK 9.2a

# trunk_mode_template = [
#     'switchport mode trunk', 'switchport trunk native vlan 999',
#     'switchport trunk allowed vlan'
# ]

# trunk_config = {
#     'FastEthernet0/1': [10, 20, 30],
#     'FastEthernet0/2': [11, 30],
#     'FastEthernet0/4': [17]
# }

# def generate_trunk_config(trunk_mode_template, trunk_config):

#     config = {}
#     for i in trunk_config:
#         buff = i
#         mode = ''
#         for j in trunk_mode_template:
#             if j != 'switchport trunk allowed vlan':
#                 mode += j + ', ' 
#             if j == 'switchport trunk allowed vlan':
#                 time = trunk_config.get(i)
#                 mode = (mode + j + ' ' + str(time).strip('[]') + ', ')
#                 # buff += mode
#                 config.update({buff:mode})
#     #     # config += config1
#     # config = config.split('\n')
#     # config = config[:-1]
#     return config

# kek = generate_trunk_config(trunk_mode_template, trunk_config)
# print(kek)

#TASK 9.3

# file = '/home/prostocema/Desktop/python/task9/config_sw11.txt'

# def get_int_vlan_map(config_filename):

#     buff = ''
#     dictaccess = {}
#     dicttrunk = {}
    
#     with open(config_filename, 'r') as f:
#         for line in f:
#             buff += line
#         for i in buff:
#             buff = buff[buff.find('interface'):]
#             time = buff[buff.find('interface'):buff.find('!') + 1]
#             time = time.split(' ')
#             for j in time:
#                 if j == 'access':
#                     value = time[8].strip()
#                     key = time[0] + time[1].strip()
#                     dictaccess.update({key:value})
#                     break
#                 elif j == 'trunk':
#                     value = time[10].strip()
#                     key = time[0] + time[1].strip()
#                     dicttrunk.update({key:value})
#                     break
#             key = ''
#             value = ''
#             buff = buff[buff.find('!') + 1:]
#         tuple1 = (dictaccess, dicttrunk)
#     return tuple1

# bigcema = get_int_vlan_map(file)
# print(bigcema)

#TASK 9.3a

# file = '/home/prostocema/Desktop/python/task9/config_sw11.txt'

# def get_int_vlan_map(config_filename):

#     buff = ''
#     dictaccess = {}
#     dicttrunk = {}

#     with open(config_filename, 'r') as f:
#         for line in f:
#             buff += line
#         for i in buff:
#             buff = buff[buff.find('interface'):]
#             time = buff[buff.find('interface'):buff.find('!') + 1]
#             time = time.split(' ')
#             for j in time:
#                 if j == 'access':
#                     value = time[8].strip()
#                     key = time[0] + time[1].strip()
#                     dictaccess.update({key:value})
#                     break
#                 elif j == 'trunk':
#                     value = time[10].strip()
#                     key = time[0] + time[1].strip()
#                     dicttrunk.update({key:value})
#                     break
#                 elif time[0] != '' and len(time) < 7:
#                     value = 1
#                     key = time[0] + time[1].strip()
#                     dictaccess.update({key:value})
#                     break
#             key = ''
#             value = ''
#             buff = buff[buff.find('!') + 1:]
#         tuple1 = (dictaccess, dicttrunk)
#     return tuple1

# bigcema = get_int_vlan_map(file)
# print(bigcema)

#TASK 9.4

file = '/home/prostocema/Desktop/python/task9/config_sw11.txt'

def convert_config_to_dict(config_filename):

    ignore = ['duplex', 'alias', 'Current configuration']
    buff = ''
    value = ''
    confdict = {}
    spisok = []
    with open(config_filename, 'r') as f:

        for line in f:
            if not (line.startswith('!')) and not any(string in line for string in ignore):
                buff += line
        buff = buff[15:]
        for buffer in buff:
            if buff.startswith(' ') == False:
                key = buff[:buff.find('\n')]
                confdict.update({key:spisok})
                tkey = key                
                buff = buff[buff.find('\n') + 1:]
                value = ''
            if buff.startswith(' ') == True:
                if tkey == key:
                    tvalue = buff[:buff.find('\n')]
                    value += tvalue + ','
                    confdict.update({key:value})
                    buff = buff[buff.find('\n') + 1:]
    return(confdict)

bigcema = convert_config_to_dict(file)
print(bigcema)