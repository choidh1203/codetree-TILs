def gang(a, b):
    max_value = max(a, b)
    min_value = min(a, b)

    max_value += 25
    min_value *= 2

    print(a, b)

a, b = map(int, input().split())
gang(a, b)