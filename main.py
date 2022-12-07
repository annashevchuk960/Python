try:
    begin = int(input('begin->'))
    end = int(input('end->'))

    for item in range(begin, end + 1):
        if item % 7 == 0:
            print(item, end="\t")
