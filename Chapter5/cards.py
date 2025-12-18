import random

cards = list(range(1, 53))

print(cards)  # シャッフル前
random.shuffle(cards)
print(cards)  # シャッフル後

pick = int(input("何枚目のカードを引きますか(1-52) >>"))
card = cards[pick - 1]  # インデックスは0から

# スート判定
suits = ["スペード", "ハート", "ダイヤ", "クラブ"]
suit = suits[(card - 1) // 13]

# ナンバー判定
number = (card - 1) % 13 + 1
if number == 1:
    number = "A"
elif number == 11:
    number = "J"
elif number == 12:
    number = "Q"
elif number == 13:
    number = "K"

print(f"あなたが引いたカードは {suit} の {number} です")
