import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect(str(os.getenv('DB_FILE')))
c = conn.cursor()

def GetWord(i):
    c.execute("SELECT word FROM words WHERE word_id=:word_id", {'word_id': i})
    word = c.fetchone()
    if word:  # 結果がある場合
        # print(word[0])  # タプルの最初の要素を取得
        strWord = word[0]
        return strWord
    else:
        return "ERROR: Word not found."


def GetMeaning(i):
    # 意味を取得
    c.execute("SELECT meaning FROM words WHERE word_id=:word_id", {'word_id': i})
    meaning = c.fetchone()
    if meaning:  # 結果がある場合
        # print(meaning[0])  # タプルの最初の要素を取得
        strMeaning = meaning[0]
        return strMeaning
    else:
        return "ERROR: Meaning not found."


def GetData(mode, num):
    # Mode 0: Word, Meaning
    # Mode 1: Meaning, Word
    val1 = GetWord(num)
    val2 = GetMeaning(num)
    if mode == 0:
        return val1, val2 # Word, Meaning
    elif mode == 1:
        return val2, val1 # Meaning, Word

if __name__ == '__main__':
    # Mode 0
    test1_word, test1_meaning = GetData(0, 20)
    # Mode 1 
    test2_meaning, test2_word = GetData(1, 20)

    print("test1_word: " + test1_word)
    print("test1_meaning: " + test1_meaning)
    print("test2_meaning: " + test2_meaning)
    print("test2_word: " + test2_word)

    print("Test Done")

# conn.close() # 接続を閉じる
