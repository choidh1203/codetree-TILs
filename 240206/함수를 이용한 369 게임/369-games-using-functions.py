def contains_369(n):
    k = str(n)
    if '3' in k or '6' in k or '9' in k:
        return True
    else:
        return False

def main(start, end):
    cnt = 0
    for i in range(start, end+1):
        if i % 3 == 0 or contains_369(i):
            cnt += 1
    print(cnt)

a, b = map(int, input().split())

main(a, b)