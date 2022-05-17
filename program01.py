
def game(matches, player, k, ranking):
    current_opponent = 0
    while current_opponent < len(matches):
        opponent = matches[current_opponent]
        set_winner = set_round(player, opponent, k)
        ranking[(player, opponent)[set_winner]] += 1
        current_opponent += 1
    return ranking


def match(player, opponent, k):
    points_1, points_2 = 0, 0
    for pl, op in zip(player, opponent):
        if pl == op: continue
        o1, o2 = ord(pl), ord(op)
        if k+1>o1-o2>0 or o2-o1>k:
            points_1 += 1
            continue
        points_2 += 1
    return points_1, points_2


def set_round(player, opponent, k):
    points_1, points_2 = match(player, opponent, k)
    if points_1 > points_2: return 0
    elif points_1 < points_2: return 1
    return tie_solver(player, opponent)


def tie_solver(player, opponent):
    counter_1, counter_2 = counter(player, opponent)
    if counter_1 < counter_2: return 0
    elif counter_1 > counter_2: return 1
    elif player < opponent: return 0
    return 1


def counter(player, opponent):
    counter_1, counter_2 = 0, 0
    for pl, op in zip(player, opponent):
        counter_1 += ord(pl)
        counter_2 += ord(op)
    return counter_1, counter_2


def ex(matches, k):
    matches = list(map(lambda x: x.translate({32: None, 9: None}), matches)) # 32 = ' '  9 = '\t'   ### ord(' '): None, ord('\n'): None ###
    ranking = dict(map(lambda x: (x,0), matches))
    indexes = {}
    while matches:
        player = matches.pop(0)
        indexes[player] = len(indexes)
        ranking = game(matches, player, k, ranking)
    return list(map(lambda x: indexes.get(x[0]), sorted(ranking.items(),key=lambda x: -x[1])))



if __name__ == "__main__":
    assert ex([ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."], 50) == [1, 2, 0]




    
