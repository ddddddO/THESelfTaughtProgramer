import csv
import os

dir = os.getcwd()
input_path = dir + "/input/challenge1.txt"

#1
with open(input_path, "r", encoding="utf-8") as f:
    print(f.read())

#2
ans1 = input("your favorite food:")
ans2 = input("your favorite color:")
output_path = dir + "/output/challenge2.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ans1 + "\n")
    f.write(ans2 + "\n")

#3
data = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

output_csv_path = dir + "/output/challenge3.csv"
with open(output_csv_path, "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for r in data:
        w.writerow(r)

#4
data_jp = [
    ["トップガン", "危険ビジネス", "マイノリティー・リポート"],
    ["タイタニック", "リバント", "インセプション"],
    ["トレーニング・デイ", "クビ・男", "フライト"]
]

output_csv_jp_path = dir + "/output/challenge4.csv"
with open(output_csv_jp_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for r in data_jp:
        w.writerow(r)
