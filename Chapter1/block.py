name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    password = input()
    print('Maryさん、こんにちは。')
    if password == 'swordfish':
        print('認証しました。')
    else:
        print('パスワードが間違っています。')
else:
    print('名前が間違っているようです。')