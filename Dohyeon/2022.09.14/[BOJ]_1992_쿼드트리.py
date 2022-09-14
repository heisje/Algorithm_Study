N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(input()))


def count_paper(n, start_i, start_j):


    if n == 1:
        if matrix[start_i][start_j] == "0":
            print("0", end="")
            return
        else:
            print("1", end="")
            return

    else:
        first = matrix[start_i][start_j]
        for i in range(start_i, start_i + n):
            for j in range(start_j, start_j + n):
                if first != matrix[i][j]:
                    print("(", end="")
                    count_paper(n // 2, start_i, start_j)
                    count_paper(n // 2, start_i, start_j + (n // 2))

                    count_paper(n // 2, start_i + (n // 2), start_j)
                    count_paper(n // 2, start_i + (n // 2), start_j + (n // 2))
                    print(")", end="")
                    return

        else:

            if first == "0":
                print("0", end="")
                return
            else:
                print("1", end="")
                return

count_paper(N, 0, 0)
