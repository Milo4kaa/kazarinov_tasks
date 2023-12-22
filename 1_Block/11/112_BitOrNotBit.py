test_string = '''
1 бит - минимальная единица количества информации.
1 байт = 8 бит.
1 Килобит = 1024 бита.
1 Килобайт = 1024 байта.
1 Килобайт = ХХХХ бит.
'''


def start(input_string: str) -> str:
    kilobyte_in_bytes = 1024
    kilobyte_in_bits = kilobyte_in_bytes * 8
    return input_string.replace("ХХХХ", str(kilobyte_in_bits))


print(start(test_string))
