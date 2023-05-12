n = int(input())


def generate_brackets(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            generate_brackets(count, s + '(', left+1, right)
        if right < left:
            generate_brackets(count, s + ')', left, right+1)


if __name__ == "__main__":
    generate_brackets(n)
