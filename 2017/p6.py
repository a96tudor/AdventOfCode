def transform_blocks(idx, blocks):
    x = blocks[idx]
    blocks[idx] = 0
    idx = idx + 1 if idx + 1 < len(blocks) else 0
    while (x > 0):
        blocks[idx] += 1
        x -= 1
        idx = idx + 1 if idx + 1 < len(blocks) else 0

    return blocks

if __name__ == "__main__":
    blocks = [
        int(x) for x in input().split()
    ]
    history = list()
    history.append(list(blocks))
    steps = 0

    while True:
        m = max(blocks)
        idx = [i for i, j in enumerate(blocks) if j == m][0]

        blocks = transform_blocks(idx, blocks)

        steps += 1

        if blocks in history:
            print(steps)
            break

        history.append(list(blocks))
