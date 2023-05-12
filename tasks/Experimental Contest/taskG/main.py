def check():
    a = input().strip()
    b = input().strip()

    if len(a) != len(b):
        return 0

    counts = [0] * 26
    base = ord('a')
    for i in range(len(a)):
        counts[ord(a[i]) - base] += 1
        counts[ord(b[i]) - base] -= 1

    return int(all([item == 0 for item in counts]))


if __name__ == "__main__":
    print(check())
