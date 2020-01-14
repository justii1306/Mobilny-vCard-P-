import sys
import requests
from bs4 import BeautifulSoup
import vobject

search = ""
for x in sys.argv[1:]:
    search = search + x + "+"
search = search[:-1]
print("Query: ")
print(search)

response = requests.get("https://adm.edu.p.lodz.pl/user/users.php?search="+search)
soup = BeautifulSoup(response.text, 'html.parser')
