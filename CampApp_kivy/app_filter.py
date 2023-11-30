def app_filter(alf, *pattern):
    filtered_game = []
    if alf == 'A-z':
        for i in data:
            if pattern:
                for pat in pattern:
                    if pat in i['tag']:
                        add = True
                    else:
                        add = False
                    if not add:
                        break
                if add:
                    filtered_game.append(i['name'])
            else:
                filtered_game.append(i['name'])
        filtered_game = sorted(filtered_game)
    if alf == 'z-A':
        for i in data:
            if pattern:
                for pat in pattern:
                    if pat in i['tag']:
                        add = True
                    else:
                        add = False
                    if not add:
                        break
                if add:
                    filtered_game.append(i['name'])
            else:
                filtered_game.append(i['name'])
        filtered_game = sorted(filtered_game, reverse=True)
        num_game = len(filtered_game)
        print(len(filtered_game))
        return [filtered_game, num_game]