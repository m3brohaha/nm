a1 = int(input("請輸入第一次段考成績: "))
a2 = int(input("請輸入第二次段考成績: "))
a3 = int(input("請輸入第三次段考成績: "))
a4 = a1 + a2 + a3
a5 = a4 / 3
score1 = a5 * 0.6

b1 = int(input("請輸入第一次平時成績: "))
b2 = int(input("請輸入第二次平時成績: "))
b3 = int(input("請輸入第三次平時成績: "))
b4 = b1 + b2 + b3
b5 = b4 / 3
score2 = b5 * 0.4

score3 = score1 + score2  # 總成績

print(f"總成績: {score3:.2f}")  # 格式化輸出小數點

if score3 >= 80:
    print("你還偷捲上了")
    print("讚喔! 不用補考")
elif score3 >= 60:
    print("讚喔! 不用補考")
elif 40 <= score3 < 60:
    print("去補考吧")
else:
    print("你超菜 連補考都不行 等重修吧")