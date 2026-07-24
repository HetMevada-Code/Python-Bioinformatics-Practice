"""
Write a Python program to ask the user to enter their 3 favorite restriction enzyme recognition sequences 
(or primer sequences) and store them in a list.
"""

RE_sites = []
RE_sites_1 = input("Enter 1st site: ")
RE_sites_2 = input("Enter 2nd site: ")
RE_sites_3 = input("Enter 3rd site: ")

RE_sites.append(RE_sites_1)
RE_sites.append(RE_sites_2)
RE_sites.append(RE_sites_3)

print(RE_sites)
