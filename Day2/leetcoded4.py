#Nth no. in seq that has prime factors as 2,3,5 only.Take 1 as first elm.
def nthUglyNumber(self, n: int) -> int:
    if n == 1:
        return 1
    t2 = 0
    t3 = 0
    t5 = 0
    ugly = [0] * n
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = min(ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5)
        if ugly[i] == ugly[t2] * 2: t2 += 1
        if ugly[i] == ugly[t3] * 3: t3 += 1
        if ugly[i] == ugly[t5] * 5: t5 += 1

    return ugly[n - 1]





