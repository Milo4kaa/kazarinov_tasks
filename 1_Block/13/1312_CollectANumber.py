test = [
    (164, 107),
    (345, 97),
    (678, 1513),
]

for num, true_res in test:
    hundreds = num // 100
    tens = (num - hundreds * 100) // 10
    units = num % 10

    sum_sen = hundreds + tens
    sum_jun = units + tens
    if sum_sen < sum_jun:
        sum_sen, sum_jun = sum_jun, sum_sen

    shift_mult = 100 if sum_jun >= 10 else 10
    print(sum_sen * shift_mult + sum_jun)
