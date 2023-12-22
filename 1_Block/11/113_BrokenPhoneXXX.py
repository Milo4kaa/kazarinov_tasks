test_string = 'И мне, и жене, и Тотоше.\nМой милый, хороший,\nПришли мне калоши,'


def start(input_string: str) -> str:
    lines = input_string.split("\n")
    return lines[1] + "\n" + lines[2] + "\n" + lines[0]


print(start(test_string))
