with open('input', 'r') as f:
    intervals = map(lambda x : tuple(x.rstrip().split(',')), f.readlines())
    cnt = 0
    for i1,i2 in intervals:
        i1_min,i1_max = map(int, i1.split('-'))
        i2_min,i2_max = map(int, i2.split('-'))
        if not ((i1_min < i2_min and i1_max < i2_min) or (i1_min > i2_max and i1_min > i2_max)):
            cnt += 1
    print(cnt)