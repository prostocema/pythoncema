ip = input('Введите IPv4-адрес в десятичном формате с маской(Пример: 10.1.1.0/24):')
#mask = input('Введите маску в десятичном виде(Пример: /24)' + '\n' + '/')
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
str = '1' * end
kol = int(str)
kol0 = kol[0:7]
kol1 = kol[8:15]
kol2 = kol[16:23]
kol3 = kol[24:]
print(kol0, kol1, kol2, kol3)

massk = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''
print(ip.format(a, b, c, d))
print('Mask:')
print(mask)