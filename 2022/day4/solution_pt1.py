with open('input', 'r') as f:
    intervals = map(lambda x : tuple(x.rstrip().split(',')), f.readlines())
    cnt = 0
    for i1,i2 in intervals:
        i1_min,i1_max = map(int, i1.split('-'))
        i2_min,i2_max = map(int, i2.split('-'))
        if (i1_min <= i2_min and i1_max >= i2_max) or (i2_min <= i1_min and i2_max >= i1_max):
            cnt += 1
    print(cnt)