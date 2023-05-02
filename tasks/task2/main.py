STEP = 500


def read_input():
    n = int(input().strip())
    return n, [int(input().strip()) for _ in range(n)]


def main_algo(n, ratings):
    bonuses = [STEP]
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            bonuses.append(bonuses[i-1] + STEP)
        elif ratings[i] == ratings[i-1]:
            bonuses.append(STEP)
        else:
            bonuses.append(STEP)
            if bonuses[i-1] == STEP:
                j = i - 1
                while j >= 0 and ratings[j] > ratings[j+1]:
                    bonuses[j] += STEP
                    j -= 1

    return sum(bonuses)


if __name__ == "__main__":
    print(main_algo(*read_input()))
