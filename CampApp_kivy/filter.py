num_game = 1122
n_max = 0
while True:
    if num_game - n_max > 100:
        print(f'{n_max + 1} - {n_max + 100}')
    else:
        print(f'{n_max + 1} - {n_max + num_game % 100}')
    n_max += 100
    if n_max >= num_game:
        break

