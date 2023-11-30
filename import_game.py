import json

# импорт базы игр
with open('list_of_game.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


def app_filter(alf, pattern=None):
    game_name = []
    if alf == 'A-z':
        if pattern != None:
            for i in data:
                if pattern in i['tag']:
                    game_name.append(i['name'])
        else:
            for i in data:
                game_name.append(i['name'])
    game_name = sorted(game_name)
    # if alf == 'z-A':
    #     for i in data:
    #         if pattern:
    #             for pat in pattern:
    #                 if pat in i['tag']:
    #                     add = True
    #                 else:
    #                     add = False
    #                 if not add:
    #                     break
    #             if add:
    #                 game_name.append(i['name'])
    #         else:
    #             game_name.append(i['name'])
    #     game_name = sorted(game_name, reverse=True)
    return game_name
