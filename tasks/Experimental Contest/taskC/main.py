def remove_dups():
    n = int(input().strip())

    if n > 1:

        previous = input().strip()
        for _ in range(1, n):
            x = input().strip()
            if x != previous:
                print(previous)
                previous = x

        if x == previous:
            print(x)
    elif n == 1:
        print(input().strip())


if __name__ == "__main__":
    remove_dups()

