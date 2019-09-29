from draw_network_graph import draw_topology
from task11 import parse_cdp_neighbors

filelist = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

def create_network_map(list_files):

    connectdict = {}
    for el in list_files:
        with open('/home/prostocema/Desktop/python/task11/' + el, 'r') as f:
            buff = ''
            for line in f:
                buff += line
            test = parse_cdp_neighbors(buff)
            connectdict.update(test)
    return connectdict

bigcema = create_network_map(filelist)
print(bigcema)

draw_topology(bigcema, output_filename= 'topology')
