import random

secret_number = random.randint(1, 20)
print('1から20までの数を当ててください。')

for guesses_taken in range(1, 7):

    try:
        guess_str = input('数を入力してください: ')
        if guess_str:
            guess = int(guess_str)
        else:
            print('何も入力されていません。もう一度入力してください。')
            continue
    except ValueError:
        print('無効な入力です。整数を入力してください。')
        continue

    if guess < secret_number:
        print('あなたの推定値は小さいです。')
    elif guess > secret_number:
        print('あなたの推定値は大きいです。')
    else:
        break

if guess == secret_number:
    print(f'当たり! {guesses_taken}回で当てました!')
else:
    print(f'残念。正解は{secret_number}でした。')