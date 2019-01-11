
import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(N, K):
    number = []
    for i in range(1, N + 1):
        number.append(i)
    if K == 0:
        return " ".join(str(e) for e in number)
    else:
        if N % (2 * K) == 0:
            for j in range(0, int(N / (2 * K))):
                for i in range(1, K + 1):
                    temp = number[j * 2 * K + i - 1]
                    number[j * 2 * K + i - 1] = number[j * 2 * K + i + K - 1]
                    number[j * 2 * K + i + K - 1] = temp
            return " ".join(str(e) for e in number)
        else:
            return "-1"


if __name__ == "__main__":
    sss = ""
    # fptr = open("test_file.txt", "w")

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)
        sss+=" ".join(map(str, result))
        sss+="\n"
        # fptr.write(" ".join(map(str, result)))
        # fptr.write("\n")

    # fptr.close()
    print(sss)
