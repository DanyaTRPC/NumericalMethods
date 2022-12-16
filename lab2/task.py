import math

matrica = [
    [7, 2, 3],
    [4, 8, 2],
    [-1, 4, 15]
]


right = [
    12,
    14,
    18
]

vl_znach = []

epsilon = 10 ** -3

start = [
    0,
    0,
    0
]

diagonalic = True

def pohibka(current, prev):
    err_size = 0

    for i in range(0,len(current)):
        err_size += math.fabs(
            current[i] - prev[i]
        )

    return err_size < epsilon

def yakobi():
    count = 0

    result = start[:]

    while True:
        row = result[:]

        for i in range(0,len(matrica)):
            s1 = 0
            s2 = 0
            s3 = 0

            for j in range(0,len(matrica)):
                if j < i:
                    s1 = s1 + (matrica[i][j] * row[j]) / matrica[i][i]
                
                if j > i:
                    s2 = s2 + (matrica[i][j] * row[j]) / matrica[i][i]

            s3 = right[i] / matrica[i][i]

            result[i] = - s1 - s2 + s3

        if pohibka(result, row):
            break

        count += 1

    return (count, result)

def relax(omega):
    count = 0

    result = start[:]

    while True:
        row = result[:]

        for i in range(0,len(matrica)):
            s1 = 0
            s2 = 0
            s3 = 0

            for j in range(0,len(matrica)):
                if j < i:
                    s1 = s1 + (matrica[i][j] * result[j]) / matrica[i][i]
                
                if j > i:
                    s2 = s2 + (matrica[i][j] * row[j]) / matrica[i][i]

            s1 = s1 * omega
            s2 = s2 * omega

            s3 = omega * (right[i] / matrica[i][i])

            result[i] = ((1-omega) * row[i]) - s1 - s2 + s3

        if pohibka(result, row):
            break

        count += 1

    return (count, result)

def prosta_iter(tau):
    count = 0

    result = start[:]

    while True:
        row = result[:]

        for i in range(0,len(matrica)):
            s = 0

            for j in range(0,len(matrica)):
               s += matrica[i][j] * row[j]

            s = tau * (s - right[i])

            result[i] = row[i] - s

        if pohibka(result, row):
            break

        count += 1

    return (count, result)

if diagonalic:     
    print("метод Якобі = ", yakobi())
    print("метод Зейделя = ", relax(1))
    print("Метод релаксації (0.5) = ", relax(0.5))
    print("Метод релаксації (0.75) = ", relax(0.5))
    print("Метод релаксації (1) / Zeidel = ", relax(1))
    print("Метод релаксації (1.5) = ", relax(1.5))

if len(vl_znach) > 0:
    maxVlZnach = max(vl_znach)
    minVlZnach = min(vl_znach)

    tau = 2 / (maxVlZnach + minVlZnach)

    print("Проста ітерація = ", prosta_iter(tau))