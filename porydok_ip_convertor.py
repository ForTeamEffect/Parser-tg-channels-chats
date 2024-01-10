from python_socks import ProxyType
uniq = [1, 2, 3, 4, 5]
fifa = ['a', 'b', 'c', 'd', 'e']
uniq_and_fifa = zip(uniq, fifa)
print(uniq_and_fifa)
print(dict(uniq_and_fifa))
for t, a in list(uniq_and_fifa):
    print(t, a)

d = {}
with open('human_proxys_ids.txt','w') as h:
    with open('ids_proxy.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = ['ProxyType.SOCKS5']+line.rstrip('\n').split(':')
            print(line)
            # line = line.insert(-5, 'ProxyType.SOCKS5')

            print(line)
            info = ['proxy_type', 'addr', 'port', 'username', "password"]
            dic = dict(zip(info, line))
            dic['proxy_type'] = dic['proxy_type'].rstrip()
            dic['port'] = int(dic['port'])
            h.write(str(dic)+'\n')
