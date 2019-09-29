from tabulate import tabulate

ipreach = ['10.0.0.0', '10.0.0.1']
ipunreach = ['10.0.0.3', '10.0.0.4', '10.0.0.5']

def print_ip_table(reach, unreach):

    head = ['reachable', 'unreachable']
    flist = []
    if len(reach) > len(unreach):
        biggest = reach
    else:
        biggest = unreach
        
    for i in range(len(biggest)):
        time = []
        max = len(reach)
        if i >= len(reach):
            time.append('')
        else:
            time.append(reach[i])
        if i >= len(unreach):
            time.append('')
        else:
            time.append(unreach[i])
        flist.append(time)

    final = (tabulate(flist, headers = head))
    
    return final

bicema = print_ip_table(ipreach, ipunreach)
print(bicema)

    