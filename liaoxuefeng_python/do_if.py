height = 1.75
weight = 80.5

bmi = (weight/height/100)*(weight/height)
print(bmi)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
elif bmi >= 32:
    print("严重肥胖")