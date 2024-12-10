import sqlite3

# データベースに接続
conn = sqlite3.connect('p1_words.db')
c = conn.cursor()

# word_id に対応する単語と意味を取得
i = 35

# 単語を取得
c.execute("SELECT word FROM words WHERE word_id=:word_id", {'word_id': i})
word = c.fetchone()
if word:  # 結果がある場合
    print(word[0])  # タプルの最初の要素を取得
else:
    print("Word not found.")

# 意味を取得
c.execute("SELECT meaning FROM words WHERE word_id=:word_id", {'word_id': i})
meaning = c.fetchone()
if meaning:  # 結果がある場合
    print(meaning[0])  # タプルの最初の要素を取得
else:
    print("Meaning not found.")

# 接続を閉じる
conn.close()
