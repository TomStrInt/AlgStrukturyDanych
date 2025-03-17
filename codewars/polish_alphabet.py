#! /usr/bin/python3

def zamien(stary_tekst):
    znaki = {
        'ą': 'a','ć': 'c','ę': 'e','ł': 'l',
        'ń': 'n','ó': 'o','ś': 's','ź': 'z',
        'ż': 'z'
    }

    tekst = ''.join(znaki.get(char, char) for char in stary_tekst)
    return tekst

polski_tekst = "Jędrzej Błądziński"
nowy_tekst = zamien(polski_tekst)
print(nowy_tekst)  
