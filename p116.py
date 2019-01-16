#1
eiga = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for e in eiga:
    print(e)

#2
for i in range(25, 51):
    print(i)

#3
for i, v in enumerate(eiga):
    print("index:{} title:{}".format(i, v))

#4
seikai = [22, 44, 88]
while True:
    mozi = input("数字を当ててね('q'で終了):")
    if mozi == "q":
        print("終了")
        break
    else:
        try:
            num = int(mozi)
            if num in seikai:
                print("正解")
                break
            else:
                print("不正解")
        except ValueError:
            print("数字か'q'を入力してね")

#5
a_list = [8, 19, 148, 4]
b_list = [9, 1, 33, 83]
result = []
for a in a_list:
    for b in b_list:
        x = a * b
        result.append(x)
        print("{} * {} = {}".format(a, b, x))

print(result)