import draw_network_graph

filelist = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

def create_network_map(list_files):

    connectdict = {}
    for el in list_files:
        with open('/home/prostocema/Desktop/python/task11/' + el, 'r') as f:
            buff = ''
            for line in f:
                buff += line

        alllist = ''
        name = buff[:buff.find('>')].strip()
        buff = buff[buff.find('Device'):]
        headlist = buff[:buff.find('\n')].split()
        buff = buff[buff.find('\n') +1:]

        headlist[0] = headlist[0] + ' ' + headlist[1]
        headlist.pop(1)
        headlist[1] = headlist[1] + ' ' + headlist[2]
        headlist.pop(2)
        headlist[-2] = headlist[-2] + ' ' + headlist[-1]
        headlist.pop(-1)

        for el in headlist:
            alllist = buff[:buff.find('\n')].split()
            buff = buff[buff.find('\n') + 1:]
            if alllist != []:
                alllist[1] = alllist[1] + alllist[2]
                alllist.pop(2)
                alllist[3] = alllist[3] + alllist[4] + alllist[5]
                alllist.pop(4)
                alllist.pop(4)
                alllist[-2] = alllist[-2] + alllist[-1]
                alllist.pop(-1)

                connectdict.update({name + ', ' + str(alllist[1]):str(alllist[0]) + ', ' + str(alllist[-1])})
                alllist = []

    return connectdict

bigcema = create_network_map(filelist)
print(bigcema)

draw_network_graph.draw_topology(bigcema, 'topology')
