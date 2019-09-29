import subprocess

iplist = ['127.0.0.1', '8.8.8.8', '192.168.0.0']

def ping_ip_addresses(ip_list):

    available = ['True']
    fail = ['False']
    flist = []
    for ip in ip_list:
        test = subprocess.run(['ping', '-c', '4', '-n', ip])
        if test.returncode == 0:
            available += ip.split()
        else:
            fail += ip.split()
    flist.append(available)
    flist.append(fail)
    fdict = tuple(flist)

    return fdict
    
bicema = ping_ip_addresses(iplist)
print(bicema)
