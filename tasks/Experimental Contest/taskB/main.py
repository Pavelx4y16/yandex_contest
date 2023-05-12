
def max_sequence():
    n = int(input().strip())

    current_max = 0
    current = 0
    for _ in range(n):
        x = input().strip()
        if x == '1':
            current += 1
            current_max = max(current_max, current)
        else:
            current = 0

    return current_max


if __name__ == "__main__":
    print(max_sequence())

