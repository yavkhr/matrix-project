import random





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


size = int(input("Enter the size of the matrix: "))
print()
print("1 - Hand matrix")
print("2 - Random matrix")
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
else:
    print("Invalid choice")



#Какок размер, рандом или нет(две функции), функция показать матрицу , красивое меню