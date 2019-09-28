with open('/home/prostocema/Desktop/python/task11/sh_cdp_n_sw1.txt', 'r') as f:
    buff = ''
    for line in f:
        buff += line

def parse_cdp_neighbors(command_output):

    connectdict = {}
    alllist = ''
    name = command_output[:command_output.find('>')].strip()
    command_output = command_output[command_output.find('Device'):]
    headlist = command_output[:command_output.find('\n')].split()
    command_output = command_output[command_output.find('\n') +1:]

    headlist[0] = headlist[0] + ' ' + headlist[1]
    headlist.pop(1)
    headlist[1] = headlist[1] + ' ' + headlist[2]
    headlist.pop(2)
    headlist[-2] = headlist[-2] + ' ' + headlist[-1]
    headlist.pop(-1)

    for el in headlist:
        alllist = command_output[:command_output.find('\n')].split()
        command_output = command_output[command_output.find('\n') + 1:]
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

bigcema = parse_cdp_neighbors(buff)
print(bigcema)