if __name__ == "__main__":
    inpt = input()
    result = 0
    no_list = [
        int(x) for x in inpt
    ]
    for i in range(len(no_list) - 1):
        if no_list[i] == no_list[i+1]:
            result += no_list[i]

    if no_list[0] == no_list[len(no_list) - 1]:
        result += no_list[0]
    print(result)