import random
import sys

score = 5
max_guesses = 10
perfect_count = 0

print("--- 数当てゲーム その２：スコア制 ---")
print(f"初期スコア: {score}点。ルール: 1〜10の数を当ててね。0でゲーム終了。")

while True:

    if max_guesses <= 0:
        print("\n*** ループ回数が0になりました。ゲーム終了です。 ***")
        break

    secret_number = random.randint(1, 10)
    guesses_taken = 0

    print(f"\n[現在のスコア: {score}点] [残りゲーム回数: {max_guesses}回]")
    print('1から10までの数を当ててください (0を入力すると終了)。')

    for i in range(1, 11):

        while True:
            try:
                guess = int(input(f'試行 {i}/{10}: 数を入力してください (0で終了): '))
            except ValueError:
                print('無効な入力です。整数を入力してください。')
                continue

            if guess == 0:
                print("\n0が入力されました。ゲームを終了します。")
                print(f"最終スコア: {score}点")
                sys.exit()

            if 1 <= guess <= 10:
                break
            else:
                print('エラー: 1から10の範囲の数を入力してください。')

        guesses_taken = i

        if guess < secret_number:
            print('あなたの推定値は小さいです。')
            score -= 1
        elif guess > secret_number:
            print('あなたの推定値は大きいです。')
            score -= 1
        else:
            print(f' **当たり!** {guesses_taken}回で当てました!')
            score += 10
            perfect_count += 1
            max_guesses -= 1
            break

        if score <= 0:
            print("\n*** スコアが0点以下になりました。ゲーム終了です。 ***")
            break

    if score <= 0:
        break

    if perfect_count >= 10:
        print("\n\n *** パーフェクト達成！ *** ")
        score += 100
        print(f"ボーナス100点加算！最終スコア: {score}点")
        break


print(f"\n--- ゲーム終了 ---")
print(f"最終スコア: {score}点")