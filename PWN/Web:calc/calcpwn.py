from pwn import *
import re
import math
import requests
from bs4 import BeautifulSoup
session = requests.Session()
url = "http://ctf.hackucf.org:4000/calc/calc.php"
content = session.get(url).content

soup = BeautifulSoup(content, "html.parser")
msg = soup.get_text()

expr = re.findall(r'(\d+|[-+*/])', msg)
expr = ' '.join(expr)
expr = expr[1:]
val = eval(expr)
# Floor the result
result = math.floor(val)

data = {"answer": result}
submit_response = session.post(url, data=data)

# Check the response
if submit_response.status_code == 200:
    print("Successfully submitted the answer.")
    response_soup = BeautifulSoup(submit_response.content, "html.parser")
    print(response_soup.get_text(strip=True))
else:
    print("Failed to submit the answer.")