'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''

import re

email = input("Unesite mail: ")
regex = "(^[a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$" 
result = re.match(regex, email)

edu = input("Unesite eduId: ")
regex1 = "^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
result1 = re.match(regex1, edu)

if result:
  print("Email tocan")
  if result1:
    print("EduId tocan")
  else:
    print("EduId nije tocan")  
else:
  print("Email nije tocan")
  if result1:
    print("EduId tocan")
  else:
    print("EduId nije tocan") 