r, t = map(int, input().split())


def calculate_distance(x, y):
    return abs(x) + abs(y)


def read_service_cars():
    n = int(input().strip())

    current_min = 2000_000_001
    service_cars = []
    for i in range(n):
        x, y = map(int, input().split())

        current_point_distance = calculate_distance(x, y)
        if current_point_distance <= r + t:
            service_cars.append(current_point_distance)

            if current_point_distance < current_min:
                current_min = current_point_distance

    return service_cars, current_min


def find_confidence(service_cars, min_distance):
    result = 0
    for car in service_cars:
        if car < min_distance:
            result += 1

    return result


def main():
    first_service_cars, first_min = read_service_cars()
    second_service_cars, second_min = read_service_cars()

    if first_min == second_min:
        print(0)
        print(0)
    elif first_min < second_min:
        print(1)
        print(find_confidence(first_service_cars, second_min))
    else:
        print(2)
        print(find_confidence(second_service_cars, first_min))


if __name__ == "__main__":
    main()
