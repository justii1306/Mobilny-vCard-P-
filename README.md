# Mobilny-vCard-P-

**Syntax:** *vcard.py [query]*

**Na przykład:** *vcard.py Paweł Kapusta*

Program pobiera plik html ze strony: https://adm.edu.p.lodz.pl/user/users.php?search= + [query] oraz wyciąga z niego odpowiednie elementy, w których zawarty jest profil.

Po wyświetleniu profili (indeks + imiona i nazwiska),  użytkownik pytany jest o indeks profilu, który chce zapisać do pliku.
Zapytanie to jest w pętli while, gdyby użytkownik chciał zapisać więcej niż jeden profil. Aby przerwać pętle należy podać ***-1***

Po wybraniu profilu program tworzy obiekt vcard, dodaje do niego pola ***n***, ***fn*** oraz ***url*** oraz wypełnia je danymi.

Następnie obiekt vcard jest serializowany i zapisany do pliku [Nazwisko][Imie].vcf

Program może zwrócić:
* ***0*** - jeśli wszystko poszło pomyślnie
* ***1*** - jeśli nie podano żadnego dodatkowego argumentu
* ***2*** - jeśli nie znaleziono żadnego profilu
