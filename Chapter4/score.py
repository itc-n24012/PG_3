#学生の名前リスト
students=['相沢いわし','伊藤うずら','上野えのき']

#点数を格納するリスト作成
scores=[0,0,0]

#点数を入力するforループ
for i in range(len(students)):
    scores[i]=int(input(f"{students[i]}さんの点数を入力してください。 >> "))

#結果を表示する
for i in range(len(students)):
    print(f"{students[i]}さん: {scores[i]}点")