def move(my_list, direction):
    result = my_list.copy()
    try:
        idx = result.index(1)
    except ValueError:
        return result

    if direction == 'left':
        new_idx = idx - 1
    elif direction == 'right':
        new_idx = idx + 1
    else:
        return result

    if 0 <= new_idx < len(result):
        result[idx] = 0
        result[new_idx] = 1
        return result
    else:
        return result
