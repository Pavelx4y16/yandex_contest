def read_input():
    n, x, k = map(int, input().split())
    return n, x, k, sorted([int(input().strip()) for _ in range(n)])


def main():
    n, x, k, dates = read_input()



if __name__ == "__main__":
    main()