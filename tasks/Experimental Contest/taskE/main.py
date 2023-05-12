def read():
    n = int(input())

    cities = [list(map(int, input().split())) for _ in range(n)]

    k = int(input())
    fro, to = map(int, input().split())

    return n, cities, k, fro, to


def init_dict(n, cities, k):
    routes = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distance = abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1])
            if distance <= k:
                routes[i].append(j)
                routes[j].append(i)

    return routes


def queue(routes, fro, to):
    q = [(fro, 0)]
    while q:
        current = q.pop(0)
        city = current[0]
        step = current[1] + 1

        for _city in routes[city]:
            if _city == to:
                return step
            q.append((_city, step))

        routes[city] = []

    return -1


def main():
    n, cities, k, fro, to = read()
    routes = init_dict(n, cities, k)

    print(queue(routes, fro - 1, to - 1))


if __name__ == "__main__":
    main()
