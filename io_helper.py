import json


def get_input():
    with open('moves.txt', 'r') as fp:
        for line in fp:
            line = line.strip()
            if line == 'GAME-START':
                continue
            if line == 'GAME-END':
                return
            yield line.split(':')
    return


def make_output(knights, weapons):
    final_state = {}

    for k in knights.values():
        if k.live:
            final_state[k.name] = [[k.x, k.y], k.status, k.weapon_name(), k.attack_score(), k.defense_score()]
        else:
            final_state[k.name] = [None, k.status, None, 0, 0]

    for w in weapons.values():
        final_state[w.name] = [[w.x, w.y], w.taken]

    with open('final_state.json', 'w+') as fp:
        fp.write(json.dumps(final_state))
    return
