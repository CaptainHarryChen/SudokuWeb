import math


def check_row(data):
    tag = True
    vis = [0 for i in range(10)]
    for i in range(9):
        for k in range(10):
            vis[k] = -1
        for j in range(9):
            if (data[i * 9 + j] != 0):
                if (vis[data[i * 9 + j]] != -1):
                    tag = False
                vis[data[i * 9 + j]] = i * 9 + j
    return tag


def check_col(data):
    tag = True
    vis = [0 for i in range(10)]
    for j in range(9):
        for k in range(10):
            vis[k] = -1
        for i in range(9):
            if (data[i * 9 + j] != 0):
                if (vis[data[i * 9 + j]] != -1):
                    tag = False
                vis[data[i * 9 + j]] = i * 9 + j
    return tag


def check_diag(data):
    tag = True
    vis = [0 for i in range(10)]
    for k in range(10):
        vis[k] = -1
    for i in range(9):
        if (data[i * 9 + i] != 0):
            if (vis[data[i * 9 + i]] != -1):
                tag = False
            vis[data[i * 9 + i]] = i * 9 + i
    for k in range(10):
        vis[k] = -1
    for i in range(9):
        j = 8 - i
        if (data[i * 9 + j] != 0):
            if (vis[data[i * 9 + j]] != -1):
                tag = False
            vis[data[i * 9 + j]] = i * 9 + j
    return tag


def check_blk(data):
    tag = True
    vis = [0 for i in range(10)]
    for i in range(9):
        for k in range(10):
            vis[k] = -1
        for j in range(9):
            x = math.floor(i / 3) * 3 + math.floor(j / 3)
            y = (i % 3) * 3 + (j % 3)
            s = x * 9 + y
            if (data[s] != 0):
                if (vis[data[s]] != -1):
                    tag = False
                vis[data[s]] = s
    return tag


def check(data):
    tag = True
    if not check_row(data):
        tag = False
    if not check_col(data):
        tag = False
    # if not check_diag(data):
    #    tag = False
    if not check_blk(data):
        tag = False
    for i in data:
        if i == 0:
            tag = False
    return tag


def difficulty(data):
    cnt = 0
    for d in data:
        if d != '0':
            cnt += 1
    if cnt <= 10 or cnt >= 70:
        return 1 # easy
    if cnt <= 20 or cnt >= 60:
        return 2 # medium
    return 3 # hard
