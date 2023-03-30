def kindersect(T, k):
    best = -1
    dp = [[None for _ in range(k+1)] for _ in range(len(T))]
    for i in range(len(T)-k):
        best = max(best, f(T, k, i, T[i][0], T[i][1], dp))
    for el in dp:
        print(el)

    return best


def f(T, k, i, left, right, dp):
    if k == 0:
        return right-left
    if i >= len(T):
        return -1

    flag, coordinatesy, coordinatesx = intersects(left, right, T[i])
    f1 = -1
    if flag:
        f1 = f(T, k-1, i+1, coordinatesx, coordinatesy, dp)
        # dp[i][k]=i
    f2 = f(T, k, i+1, left, right, dp)
    mini = max(f1, f2)
    return mini


def intersects(left, right, val):
    if val[1] <= left or val[0] >= right:
        return False, None, None
    else:
        return True, min(right, val[1]), max(left, val[0])


A = [(0, 4), (1, 10), (6, 7), (2, 8), [1, 5]]
print(kindersect(A, 3))
