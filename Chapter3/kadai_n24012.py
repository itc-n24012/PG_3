#あいさつする関数
#n24012 仲本優衣
def aisatsu(namae, jikantai):
    if jikantai == 1:
        print(f"{name}さん、おはようございます")
    elif jikantai == 2:
        print(f"{name}さん、こんにちは")
    elif jikantai == 3:
        print(f"{name}さん、こんばんは")
    else:
        print(f"{name}さん、おやすみなさい")
    #関数aisatsuはここまで

#プログラム実行はここから
name=input("名前を入力してください >>")
print("朝:1 昼:2 晩:3 寝る前:4")
jikan = int(input("時間帯を入力してください >>"))
aisatsu(name,jikan)