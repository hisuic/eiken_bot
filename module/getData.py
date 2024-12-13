import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect(str(os.getenv('DB_FILE')))
c = conn.cursor()

def GetWord(i):
    c.execute("SELECT word FROM words WHERE word_id=:word_id", {'word_id': num})
    word = c.fetchone()
    if word:  # 結果がある場合
        # print(word[0])  # タプルの最初の要素を取得
        return word[0]
    else:
        return "ERROR: Word not found."


def GetMeaning(i):
    # 意味を取得
    c.execute("SELECT meaning FROM words WHERE word_id=:word_id", {'word_id': num})
    meaning = c.fetchone()
    if meaning:  # 結果がある場合
        # print(meaning[0])  # タプルの最初の要素を取得
        return meaning[0]
    else:
        return "ERROR: Meaning not found."


def GetData(mode, num): # Mode 0: val1<-Word, val2<-Meaning Mode 1: Reverse
    val1 = GetWord(num)
    val2 = GetMeaning(num)
    if mode == 0:
        return val1, val2 # Word, Meaning
    elif mode == 1:
        return val2, val1 # Meaning, Word

if __name__ == '__main__':
    print("hello")

conn.close() # 接続を閉じる
