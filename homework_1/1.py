
def module(exit_code, inter, checker):
    inter_cases = {
        1: checker,
        6: 0,
        7: 1
    }

    if inter in inter_cases.keys():
        return inter_cases[inter]
    elif inter == 0:
        return 3 if exit_code != 0 else checker
    elif inter == 4:
        return 3 if exit_code != 0 else 4
    else:
        return inter


with open("input.txt", "r") as file:
    r, i, c = map(int, file.readlines())
    print(module(r, i, c))
