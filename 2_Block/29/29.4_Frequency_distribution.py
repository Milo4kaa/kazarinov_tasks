test_string = '''
2
Ехал Грека через реку. Видит Грека в реке рак.
Сунул Грека руку в реку, рак за руку Греку цап.
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

def main():
    n = int(input())
    text = [input().split() for _ in range(n)]

    word_freq = {}
    for line in text:
        for word in line:
            word = word.strip(',.!?;:')
            word = word.capitalize()
            word_freq[word] = word_freq.get(word, 0) + 1

    sorted_words = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))

    for word, freq in sorted_words:
        print(word)

if __name__ == "__main__":
    main()