import sys

if __name__ == "__main__":
    result = 0
    for i in range(16):
        line = input()
        a = [int(x) for x in line.split()]
        MIN = min(a)
        MAX = max(a)
        result += MAX-MIN
    print(result)

