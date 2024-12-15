phrase = "Chittagong"
plist = list(phrase)

print(phrase)
print(plist)

for i in range(2):
    plist.pop ()

plist.remove('t')
plist.remove('t')
plist.insert(3, 'c')
new_phrase = ''.join(plist)

print(new_phrase)
print(plist)
