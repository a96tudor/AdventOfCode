import math

if __name__ == "__main__":
    inpt = int(input())
    lng = math.floor(math.sqrt(inpt))
    prev_corner = lng ** 2
    if lng ** 2 != inpt:
        lng = lng + 1
    corner = lng ** 2
    if prev_corner == corner:
        print(lng - 1)
    else:
        d1 = int(lng / 2)
        if inpt > corner - lng + 1:
            print("case 1")
            mid = corner - math.floor(lng/2) + 1
        elif inpt > corner - 2*lng + 2:
            print("case 2")
            if lng % 2 != 0:
                mid = corner - 2*lng + 2 + math.floor(lng/2)
            else:
                mid = corner - 2*lng + 1 + math.floor(lng/2)

        d2 = abs(mid - inpt)

        print(corner - 2*lng + 2)
        print(d1+d2)


