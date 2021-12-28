lower_ascii_start = 97


def print_rangoli(size):
    if size==1:
        print('a')
    else:
        dash_size = (size - 1) * 2
        rangoli = ''
        rangoli += make_pattern("range(size)", dash_size, size)
        rangoli += make_pattern("range(size-2, -1, -1)", dash_size, size)

        print(rangoli)


def make_pattern(for_range, dash_size, size):
    pattern = ''

    for i in eval(for_range):
        dash_qtd = dash_size - (i * 2)
        pattern += make_dash(dash_qtd) + make_chardash(i + 1, size) + make_dash(dash_qtd - 1) + '\n'

    return pattern


def make_dash(size):
    return '-' * size


def make_chardash(size, max_size):
    if size == 1:
        return chr(lower_ascii_start + max_size - 1) + '-'
    else:
        s = ''
        for i in range(size):
            s += chr(lower_ascii_start + max_size - 1 - i) + '-'
        for i in range(size - 1, 0, -1):  # range(1, size):
            if size == max_size and i == 1:
                s += chr(lower_ascii_start + max_size - i)
            else:
                s += chr(lower_ascii_start + max_size - i) + '-'
        return s


if __name__ == '__main__':
    n = 1  # int(input())
    print_rangoli(n)
