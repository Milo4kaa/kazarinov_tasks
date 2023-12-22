test_string = 10
def fibonacci_sequence(n):
    sequence = [1, 1]
    while sequence[-1] <= n:
        next_number = sequence[-1] + sequence[-2]
        if next_number <= n:
            sequence.append(next_number)
        else:
            break
    return sequence

print("Ввдите натуральное число: ")
n = test_string
print (n)
sequence = fibonacci_sequence(n)
print(sequence)

