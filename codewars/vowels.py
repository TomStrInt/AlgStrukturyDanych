#! /usr/bin/python3

znaki = input("prosze podac ciag znakow:     ")
def zamien(ciag_znakow):
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    changed = ''.join('!' if ch in vowels else ch for ch in ciag_znakow)
    return changed

print(zamien("Hi!"))          
print(zamien("ABCDE"))     
print(zamien("abrakadabra"))   
print(zamien(znaki))
