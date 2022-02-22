import os

__scores = {}
__file_path = "MiniProject01/score.txt"
__file_path_tmp = "MiniProject01/score.tmp"

def LoadScoresFromFiles():
    if os.path.exists(__file_path) is False:
        return {}

    f = open(__file_path)
    for line in f.readlines():
        items = line.split(',')
        if len(items) < 2: continue

        name = items[0].strip()
        score = items[1].strip()

        if score.isdigit() is False: continue
        __scores[name] = int(score)

    f.close()

def SaveScoresToFiles():
    f = open(__file_path_tmp, "w")
    for user in __scores:
        f.write(f'{user}, {__scores[user]}\n')
    f.close()
    os.remove(__file_path)
    os.rename(__file_path_tmp, __file_path)

def UpdateUserScore(name, score):
    if name in __scores and __scores[name] > score: return
    __scores[name] = score
    SaveScoresToFiles()

def ShowLeaderboard():
    _items = list(__scores.items())
    _items.sort(key = lambda item: item[1], reverse = True)

    print('======== LEADERBOARD ========')
    for i in range(0, len(_items)):
        print(f"{i} - {_items[i][0]}: {_items[i][1]}")