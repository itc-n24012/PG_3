#星座名のリスト
seiza_list=['山羊座','水瓶座','魚座','牡羊座','牡牛座','双子座','蟹座','獅子座',
       '乙女座','天秤座','蠍座','射手座']

#キーワードのリスト
keyword_list=[
    'I keep...(私は守る)',
    'I solve...(私は解明する)',
    'I believe...(私は信じる)',
    'I exist...(私は存在する)',
    'I have...(私は所有する)',
    'I choose...(私は選択する)',
    'I sense...(私は感じる)',
    'I will...(私は〜する)',
    'I analyze...(私は分析する)',
    'I balance...(私はバランスをとる)',
    'I want...(私は要求する)',
    'I experience...(私は体験する)'
]
#誕生日の入力
month=int(input("生まれた月を入力してください >> "))
day=int(input("生まれた日を入力してください >> "))

#星座判定
if month== 1:
    index = 1 if day >= 20 else 0
elif month == 2:
    index = 1 if day >= 19 else 1
elif month == 3:
    index = 3 if day >= 21 else 2
elif month == 4:
    index = 4 if day >= 20 else 3
elif month == 5:
    index = 5 if day >= 21 else 4
elif month == 6:
    index = 6 if day >= 22 else 5
elif month == 7:
    index = 7 if day >= 23 else 6
elif month == 8:
    index = 8 if day >= 23 else 7
elif month == 9:
    index = 9 if day >= 23 else 8
elif month == 10:
    index = 10 if day >= 24 else 9
elif month == 11:
    index = 11 if day >= 23 else 10
elif month == 12:
    index = 0 if day >= 22 else 11

#結果
print(f"あなたの星座は{seiza_list[index]}です。")
print(f'キーワードは"{keyword_list[index]}"です。')