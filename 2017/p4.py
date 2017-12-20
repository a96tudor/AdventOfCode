import sys

if __name__ == "__main__":
    count_valid = 0
    for i in range(512):
        line = input()
        words = line.split()
        valid = True
        for i in range(len(words)):
            if words[i] in words[i+1:]:
                valid = False
                break

        if valid:
            count_valid += 1

    print(count_valid)
