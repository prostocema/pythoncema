ip = input('Введите IP-адрес в формате 10.0.1.1: ')
ipc = ip.count('.')
ip = ip.split('.')

if ipc == 3 and 0 <= int(ip[0]) <= 255 and 0 <= int(ip[1]) <= 255 and 0 <= int(ip[2]) <= 255  and 0 <= int(ip[3]) <= 255 :

    if 1 <= int(ip[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip[0]) <= 239:
        print('multicast')
    elif int(ip[0] and ip[1] and ip[2] and ip[3]) == 255:
        print('local broadcast')
    elif int(ip[0] and ip[1] and ip[2] and ip[3]) == 0:
        print('unassigned')
    else:
        print('unused')
else:
    print('Введен неправильный айпи!!')