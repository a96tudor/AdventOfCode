if __name__ == "__main__":
    jumps = list()
    for i in range(1059):
        jumps.append(int(input()))

    current = 0
    cnt_jumps = 0

    while (current < len(jumps) and current >= 0):
        jumps[current] += 1
        current = current + jumps[current] - 1
        cnt_jumps += 1
    print(cnt_jumps)