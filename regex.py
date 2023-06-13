'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

string = str(input("Unesite neki string: "))
string = string.lower()

regex = r"^m.*[0-5]+.*\s.*j$"

result = re.findall(regex, string)

if result:
  print("Podudaranje")
else:
  print("Nema podudaranja")  