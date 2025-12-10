import random
import sys
from collections import defaultdict


def get_move_display(move):
    if move == 'r':
        return 'グー (ROCK)'
    elif move == 'p':
        return 'パー (PAPER)'
    elif move == 's':
        return 'チョキ (SCISSORS)'
    return ''


def run_janken_game():
    player_score = 0
    computer_score = 0

    print('--- じゃんけん 10回勝負 ---')
    print('r: グー, p: パー, s: チョキ, q: ゲーム終了')

    for round_num in range(1, 11):
        print(f'\n--- 第 {round_num} 回戦 ---')

        rand_num = random.randint(1, 3)
        if rand_num == 1:
            computer_move = 'r'
        elif rand_num == 2:
            computer_move = 'p'
        else:
            computer_move = 's'

        while True:
            player_move = input('あなたの手を入力してください: ').lower()

            if player_move == 'q':
                player_score -= 1
                print('\nゲーム終了を選択しました。あなたのスコアから1点マイナスします。')
                break

            if player_move in ('r', 'p', 's'):
                break

            print('エラー: r, p, s, または q を入力してください。')

        if player_move == 'q':
            break

        print(f'あなた: {get_move_display(player_move)}')
        print(f'コンピュータ: {get_move_display(computer_move)}')

        if player_move == computer_move:
            result = 'あいこ'
            print('判定: あいこです！')

        elif (player_move == 'r' and computer_move == 's') or \
                (player_move == 'p' and computer_move == 'r') or \
                (player_move == 's' and computer_move == 'p'):
            result = '勝ち'
            player_score += 1
            print('判定: あなたの勝ちです！ (+1 ポイント)')

        else:
            result = '負け'
            computer_score += 1
            print('判定: あなたの負けです。')

    print('\n--- 最終結果 ---')
    print(f'あなたの最終ポイント: {player_score}点')
    print(f'コンピュータの最終ポイント: {computer_score}点')

    if player_score > computer_score:
        print('🏆 総合優勝はあなたです！おめでとうございます！')
    elif computer_score > player_score:
        print('残念、総合優勝はコンピュータでした。')
    else:
        print(' 最終ポイントは同点です。')


def run_ichi_hachi_game():
    ichi_hachi_score = defaultdict(int)

    print('--- 18（イチハチ）ゲーム ---')
    print('ルール: 連続でじゃんけんに勝つと、勝った回数分の点数が得られます。')
    print('負けるかあいこになると、それまで貯めた連続勝ちの記録はリセットされます。')
    print('r: グー, p: パー, s: チョキ, q: ゲーム終了')

    player_name = 'あなた'
    computer_name = 'コンピュータ'

    player_streak = 0
    computer_streak = 0

    while True:
        print(
            f'\n--- スコア: {player_name}: {ichi_hachi_score[player_name]}点, {computer_name}: {ichi_hachi_score[computer_name]}点 ---')

        while True:
            player_move = input(f'{player_name}の手を入力してください (qで終了): ').lower()
            if player_move == 'q':
                print('\nゲームを終了します。')
                print(
                    f'最終スコア: {player_name}: {ichi_hachi_score[player_name]}点, {computer_name}: {ichi_hachi_score[computer_name]}点')
                sys.exit()
            if player_move in ('r', 'p', 's'):
                break
            print('エラー: r, p, s, または q を入力してください。')

        rand_num = random.randint