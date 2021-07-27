# my original implementation:
def print_formatted(number):
    binary = f"{number:b}"
    digits = len(binary)
    solution = ""

    for i in range(1, number + 1):
        solution = "%s%s %s%s %s%s %s%s" % (
            spacing(digits, str(i)), i, spacing(digits, f"{i:o}"), f"{i:o}", spacing(digits, f"{i:x}".upper()),
            f"{i:x}".upper(),
            spacing(digits, f"{i:b}"), f"{i:b}")
        print(solution)


def spacing(digits, number_str):
    spaces = ""
    number = len(number_str)
    for i in range(digits - number):
        spaces += " "

    return spaces


# alternative implementation:
def print_formatted_2(n):
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = 99  # int(input()) #sample input: 2
    print_formatted(n)
