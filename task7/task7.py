# #task7.1
# f = open('ospf.txt', 'r')

# str = f.read()

# ospf_route = str.split()
# for i in range(8):
#     ospf_route.remove('via')

# f.close()

# # print(ospf_route)

# a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

# ospf_route1 = '''
# Protocol:            {}
# Prefix:              {}         
# AD/Metric:           {}
# Next-Hop:            {}
# Last update:         {}
# Outbound Interface:  {}
# '''

# for i in range(7):
#     print(ospf_route1.format(ospf_route[a], ospf_route[b], 
#     ospf_route[c].strip('[]'), ospf_route[d].strip(','),
#     ospf_route[e].strip(','),  ospf_route[f]))
#     a += 6
#     b += 6
#     c += 6
#     d += 6
#     e += 6
#     f += 6



# list_ip = []
# with open("ospf.txt") as f:
#     for i in f:
#         list_ip.append(i)

# ip_template = """
# Protocol:            {0}
# Prefix:              {1}         
# AD/Metric:           {2}
# Next-Hop:            {3}
# Last update:         {4}
# Outbound Interface:  {5}
# """
# temp = []
# for i in list_ip:
#     temp = i.strip(",").split()
#     print(ip_template.format(temp[0], temp[1], temp[2].strip("[]"), temp[4], temp[5], temp[6]))




#TASK7.2
# from sys import argv

# with open(argv[1], 'r') as f:
#     for line in f:
#         line = line.rstrip()
#         if line.startswith('!'):
#             continue
#         else:
#             print(line)

#TASK7.2a

# ignore = ['duplex', 'alias', 'Current configuration']
# with open('config_sw1.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip()
#         if not (line.startswith('!')) and not any(string in line for string in ignore):
#             print(line)

#TASK 7.2b

# ignore = ['duplex', 'alias', 'Current configuration']
# with open('config_sw1.txt', 'r') as f, open('config_sw1_cleared.txt', 'w') as fw:
#     for line in f:
#         #line = line.rstrip()
#         if not any(string in line for string in ignore):t
#             fw.write(line)

#TASK 7.2c

# from sys import argv

# ignore = ['duplex', 'alias', 'Current configuration']
# with open(argv[1], 'r') as f, open(argv[2], 'w') as fw:
#     for line in f:
#         #line = line.rstrip()
#         if not any(string in line for string in ignore):
#             fw.write(line)

#TASK 7.3

# with open('CAM_table.txt', 'r') as f:
#     line = f.read()
#     line = line[line.find('100')::]
#     print(line.replace('DYNAMIC', ''))

#TASK 7.3a

# with open('CAM_table.txt', 'r') as f:
#     line = f.read()
#     line = line[line.find('100')::]
#     line = line.replace('DYNAMIC', '')
#     line = line.split('\n')
#     del line[-1]
#     n = len(line)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             a = int(line[j][0:5].strip())
#             b = int(line[j+1][0:5].strip())
#             # print(a,b)
#             if a > b:
#                 line[j], line[j+1] = line[j+1], line[j]
#     for i in line:
#         print(i.strip())

# TASK 7.3b

# with open('CAM_table.txt', 'r') as f:
#     line = f.read()
#     line = line[line.find('100')::]
#     line = line.replace('DYNAMIC', '')
#     line = line.split('\n')
#     del line[-1]
#     n = len(line)
#     sear = input('Введите искомый VLAN: ')
#     sear = int(sear)
#     for i in range(n):
#         if sear == int(line[i][0:5]):
#             print(line[i])


