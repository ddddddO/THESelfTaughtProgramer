#1
musicians = ["The back horn", "イエローモンキー", "スピッツ"]
print(musicians)
print(musicians[0])

#2
geos = [("35.301279", "139.481001"), ("35.33511", "139.349476")]
for geo in geos:
    print(geo)

#3
characteristic = {"height": 166, "weight": 46, "name": "daiki"}
print(characteristic)
print(characteristic["name"])

#4
key = input("enter characteristic key:")
if key in characteristic:
    print(characteristic[key])
else:
    print("invalid key")

#5
setlist = {
    "The back horn": ["惑星メランコリー", "ひょうひょうと", "雨"], 
    "イエローモンキー": ["jam", "球根"], 
    "スピッツ": ["チェリー", "夜を翔ける"]
    }

#print(setlist)
print(setlist["スピッツ"])

#6 https://note.nkmk.me/python-set/
s = {1, 1, 2, 3, 5}
print(s)

l = ["aa", "aa", "aa", "bb"]
ss = set(l)
print(ss)