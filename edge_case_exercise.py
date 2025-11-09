def move(my_list, direction):
    idx = my_list.index(1)

    if direction == 'left':
        new_idx = idx - 1
    elif direction == 'right':
        new_idx = idx + 1
    else:
        return my_list

    if 0 <= new_idx < len(my_list):
        my_list[idx], my_list[new_idx] = 0, 1

    return my_list
