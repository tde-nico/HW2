
def retrieve_match_result( 
        player, opponent, points_player, points_opponent, player_sequence, opponent_sequence
    ) -> dict:

    current_match = dict({ player: 0, opponent: 0 })

    if points_player > points_opponent:
        current_match[player] = 1
    elif points_opponent > points_player:
        current_match[opponent] = 1
    else:
        if sum(player_sequence) < sum(opponent_sequence):
            current_match[player] = 1
        else:
            current_match[opponent] = 1
 
    return current_match

def execute_match(k, player_sequence, opponent_sequence, player, opponent) -> dict:
    points_player, points_opponent = 0,0
    for a,b in zip(player_sequence, opponent_sequence):
        if a > b:
            if a - b <= k:
                points_player += 1 
                continue
            else:
                points_opponent += 1
                continue
        elif  a < b:
            if b - a <= k:
                points_opponent += 1
                continue
            else:
                points_player += 1
                continue
        continue

    return retrieve_match_result(
        player, opponent, points_player, points_opponent, player_sequence, opponent_sequence
    )

def format_string_to_list_unicode(matches) -> list:
    return list((
        [ord(character) for character in list(seq.replace(' ','').replace('\t',''))]
        for seq in matches
    ))

def update_ranking(key, value, data) -> int:
    return data.get(key, 0) + value
    
def tournament(matches, k, len_matches) -> dict:

    player, opponent = 0,1
    results = dict()

    player_sequences = format_string_to_list_unicode(matches)
    match_finished = False

    matches_1 = len_matches - 1
    matches_2 = len_matches - 2

    while not match_finished:
        match_finished = player == matches_2 and opponent == matches_1
        current_match_result = execute_match( 
            k, 
            player_sequences[player], player_sequences[opponent],
            player, opponent)

        results[player] = update_ranking(player, current_match_result[player],results )
        results[opponent] = update_ranking(opponent, current_match_result[opponent],results )

        opponent += 1

        if (opponent-1) == matches_1:
            player +=1
            opponent = player + 1
    return results

def ex(matches, k):
    len_matches = len(matches)
    results = tournament(matches, k, len_matches)
    return sorted(results, key=results.get, reverse=True)






