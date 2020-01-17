import sys
import requests
import bs4
import vobject

search = ""
for x in sys.argv[1:]:
    search = search + x + "+"
search = search[:-1]
print("Query: " + search)

response = requests.get("https://adm.edu.p.lodz.pl/user/users.php?search="+search)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
profiles = soup.findAll("div", {"class": "user-info"})
profilesArray = []

print("Znaleziono nastepujace profile: ")
i = 0
for x in profiles:
    for y in x.contents:
        if isinstance(y, bs4.element.NavigableString):
            continue
        profilesArray.append(y)
        print(str(i) + ": " + y['title'])
        i=i+1
choice = 0
while choice != -1:
    choice = int(input("Podaj profil, ktory chcesz pobrac lub wpisz -1 aby zakonczyc: "))
    if choice >= len(profilesArray):
        print("Error")
    else:
        vcard = vobject.vCard()
        names = profilesArray[choice]['title'].split()
        vcard.add('n')
        if len(names) < 1:
            print("Error")
        elif len(names) == 1:
            vcard.n.value = vobject.vcard.Name(given = names[0])
        elif len(names) == 2:
            vcard.n.value = vobject.vcard.Name(family = names[-1], given = names[0])
        else:
            vcard.n.value = vobject.vcard.Name(family = names[-1], given = names[0], additional = names[1:-1])
        vcard.add('fn')
        vcard.fn.value = profilesArray[choice]['title']
        vcard.add('url')
        vcard.url.value = "https://adm.edu.p.lodz.pl" + profilesArray[choice]['href']
        with open(names[-1] + names[0] + '.vcf', 'w', encoding="utf-8") as my_file:
            my_file.writelines(vcard.serialize())
            print("Zapisano do pliku")
