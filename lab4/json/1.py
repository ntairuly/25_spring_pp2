import json

json_file = 'jsonExample.json'

with open(json_file, "r") as openedFile:
    global jsonDict
    jsonDict = json.load(openedFile)

print("Interface Status")
print("=" * 80)
print("DN", " " * 45, "Description", " " * 10, "Speed", " " * 2, " MTU")
print("-" * 48, "-" * 21, "", "-" * 6, "", "-" * 6)
for imdata in jsonDict['imdata']:
    for phys in imdata:
        if len(imdata[phys]['attributes']['dn']) < 42:
            print(imdata[phys]['attributes']['dn'], end = " " * 31)
            print(imdata[phys]['attributes']['speed'], end = " " * 3)
            print(imdata[phys]['attributes']['mtu'])
        else :
            print(imdata[phys]['attributes']['dn'], end = " " * 30)
            print(imdata[phys]['attributes']['speed'], end = " " * 3)
            print(imdata[phys]['attributes']['mtu'])