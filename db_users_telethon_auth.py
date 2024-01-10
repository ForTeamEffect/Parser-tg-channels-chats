from telethon.sync import TelegramClient
import socks
from python_socks import ProxyType

accounts = [{
    "api_id": 26916777, "api_hash": "c4abeac38a9fad71aaafaff79c112cc4", "phone_number": "+66994011738",
    'my_proxy': {
        'proxy_type': ProxyType.SOCKS5, 'addr': "213.226.101.73", 'port': 5501, 'username': "TG",
        "password": "proxysoxybot"
    }},
    {
        "api_id": 22979979, "api_hash": "34c33fa9f295b9d68e3c493c9e474671", "phone_number": "+66993579241",
        'my_proxy': {
            'proxy_type': ProxyType.SOCKS5, 'addr': "45.84.177.184", 'port': 5501, 'username': "TG",
            "password": "proxysoxybot"
        }},
    {
        "api_id": 25349595, "api_hash": "85d317b1027d6a0153a224d862f05bcb", "phone_number": "+66950854080",
        'my_proxy': {
            'proxy_type': ProxyType.SOCKS5, 'addr': "45.134.183.101", 'port': 5501, 'username': "TG",
            "password": "proxysoxybot"
        }},
    {
        "api_id": 27989247, "api_hash": "9540fdf91af3d7b2a34b523f72837711", "phone_number": "+66946120531",
        'my_proxy': {
            'proxy_type': ProxyType.SOCKS5, 'addr': "45.145.119.54", 'port': 5501, 'username': "TG",
            "password": "proxysoxybot"
        }},
    {
        "api_id": 22664147, "api_hash": "1f9e192aa8c7a069ce384f494550e005", "phone_number": "+66805472167",
        'my_proxy': {
            'proxy_type': ProxyType.SOCKS5, 'addr': "185.181.247.121", 'port': 5501, 'username': "TG",
            "password": "proxysoxybot"
        }},
    {"api_id": 29332341, "api_hash": "d0577a3be51c5b6f75897d5ac8ca2adc", "phone_number": "+66629215486", }]


for acc in accounts:
    my_proxy = acc.get('my_proxy', None)

    # Разбиваем proxy_server на тип, адрес и порт
    # proxy_type = 'socks5'
    # proxy_type = proxy_type.lower()  # Приводим к нижнему регистру
    # proxy_address, port = proxy_server.split(':')
    # proxy = (socks.SOCKS5, proxy_address, int(port), (proxy_username, proxy_password) if proxy_username else None)

    client = TelegramClient(f'{acc["phone_number"]}_telethon', acc["api_id"], acc["api_hash"], proxy=my_proxy)
    client.start(int(acc["phone_number"]), password='Wf52')
    client.connect()
