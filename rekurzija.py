'''
Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.
'''

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse("Mario"))