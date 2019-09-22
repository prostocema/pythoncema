ip = input('Введите IPv4-адрес в десятичном формате с маской(Пример: 10.1.1.0/24):')
mask = ip[ip.find('/')::].strip('/')
#print(mask)
end = int(mask)
ip = ip.strip(mask).strip('/')
#print(ip)
ip = ip.split('.')
a, b, c, d = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
ip = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''
bits = '1' * end
nols = (32 - end) * '0'
itog = bits + nols
# print(itog)
oct0, oct1, oct2, oct3 = int(itog[0:8]), int(itog[8:16]), int(itog[16:24]), int(itog[24:32])
oct00 = int(str(oct0), 2)
oct11 = int(str(oct1), 2)
oct22 = int(str(oct2), 2)
oct33 = int(str(oct3), 2)

massk = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{4:<8} {5:<8} {6:<8} {7:<08}
'''
print(ip.format(a, b, c, d))
print('Mask:')
print(massk.format(oct00, oct11, oct22, oct33, oct0, oct1, oct2, oct3))
print(mask)