mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
macc = []
for i in range(4):
    macc.append(mac[i].replace(':', '.'))
print(macc)
