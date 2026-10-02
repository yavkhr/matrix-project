import random

pixel = [
    [0, 50, 100],
    [150, 200, 255],
    [30, 120, 220]]

def change_brights(number, mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] += number
            if mat[i][j] > 255:
                mat[i][j] = 255

    return mat

# polzunok = 1 - bez izmenenii
# polzunok = 1.5 - uvelichit'
# polzunok = 0.5 - umenshit
# polzunok = 0 - odinakovo serie
# new = (pixel - 127.5) * factor + 127.5

def normalization(mat):
    flat_mat = [x for row in mat for x in row]
    min_val = min(flat_mat)
    max_val = max(flat_mat)
    if min_val == max_val:
        return mat

    res = []
    for row in mat:
        norm_row = [round((x-min_val) / (max_val-min_val), 2) for x in row]
        res.append(norm_row)
    return res

def blur(mat):
    res = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            total = 0
            count = 0
            for ni in range(-1, 2, 1):
                for nj in range(-1, 2 ,1):
                    if 0 <= i + ni  < len(mat) and 0 <= j + nj < len(mat[i]):
                        total += mat[i + ni][j + nj]
                        count += 1
            row.append(round(total/count))
        res.append(row)
    return res



def change_contrast(mat, polzunok=1):
    if polzunok < 0:
        polzunok = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = round((mat[i][j] - 127.5) * polzunok + 127.5)
            if mat[i][j] > 255:
                mat[i][j] = 255
            if mat[i][j] < 0:
                mat[i][j] = 0
    return mat

def create_ordered_matrix(n):
    res = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num += 1
        res.append(row)
    return res

def matrix(mat):
    res = []
    while len(mat):
        res += mat.pop(0)
        if  len(mat) == 0:
            return res
        mat = transporation(mat)[::-1]
    return res


def transporation(mat):
    res = []
    for i in range(len(mat[0])):
        rows = []
        for j in range(len(mat)):
            rows.append(mat[j][i])
        res.append(rows)
    return res



def show_matrix(mat):
    for row in mat:
        print(row)

def hand_matrix(size):
    res = []
    for i in range(size):
        row = []
        for j in range(size):
            num = int(input("Which num you want? "))
            row.append(num)
        res.append(row)
    return res

def rand_matrix(size):
    return [[random.randint(0,9) for j in range(size)] for i in range(size)]

print(blur(pixel))
size = int(input("Enter the size of the matrix: "))
print()
print("1 - Hand matrix")
print("2 - Random matrix")
print("3 - Range matrix")
choice = str(input("Enter your choice: "))
if choice == "1":
    start_matrix = hand_matrix(size)
    show_matrix(start_matrix)
    print()
    snail = matrix(start_matrix)
    print(snail)
elif choice == "2":
    start_matrix = rand_matrix(size)
    show_matrix(start_matrix)
    print()
    snail = matrix(start_matrix)
    print(snail)
elif choice == "3":
    n = int(input("Enter the range of the matrix: "))
    start_matrix = create_ordered_matrix(n)
    show_matrix(start_matrix)
    print()
    snail = matrix(start_matrix)
    print(snail)
else:
    print("Invalid choice")



#Какок размер, рандом или нет(две функции), функция показать матрицу , красивое менюй