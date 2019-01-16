#1
sakka = "カミュ"
for s in sakka:
    print(s)

#2
s1 = input("in string 1:")
s2 = input("in string 2:")
print("私は昨日{}を書いて、{}に送った！".format(s1, s2))

#3
sentence0 = "aldous hu was born..."
print(sentence0.capitalize())

#4
sentence1 = "どこで？　だれが？　いつ？"
sentence1_list = sentence1.split("　")
print(sentence1_list)

#5
list1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
sentence2 = " ".join(list1)
i = sentence2.index(".")
s3 = sentence2[:i-1] + sentence2[i:]
print(s3)

#6
sentence3 = "A screaming comes across the sky."
rep_sentence3 = sentence3.replace("s", "$")
print(rep_sentence3)

#7
print("Hemingway".index("m"))

#8
sentence4 = '風はろうそくの火を消すが、"炎を燃え上がらせる"'
print(sentence4)

#9
sentence5 = "three" + " " + "three" + " " + "three"
print(sentence5)

sentence6 = ("three " * 3).strip()
print(sentence6)

#10
sentence7 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
sentence7_slice = sentence7[:sentence7.index("、")]
print(sentence7_slice)