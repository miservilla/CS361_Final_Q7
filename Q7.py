from math import floor


def what_am_i_doing(A, left, right):
    if left == right:
        return A[right-1]
    else:
        m = floor((left + right) / 2)
        x = what_am_i_doing(A, left, m)
        y = what_am_i_doing(A, m + 1, right)
        return min(x, y)


A = [2, 5, 7, 3, 4, 1, 6, 8]
print(what_am_i_doing(A, 1, 8))
