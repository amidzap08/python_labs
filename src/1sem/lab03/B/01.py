import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lab03.lib.text as text

stdin = sys.stdin.readline()
allwords = text.tokenize(stdin)
uniquewords = text.count_freq(allwords)
top = text.top_n(uniquewords, n=5)
print(f"Bcero слов: {len(allwords)}")
print(f"Уникальных слов: {len(uniquewords)} ")
print("Ton-5: ")
for i in top:
    print(i[0] + ":" + str(i[1]))
