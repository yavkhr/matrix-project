import random

start_matrix = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9],
]



def matrix(mat):
    res = []
    while len(mat):
        res += mat.pop(0)


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
elif choice == "2":
    start_matrix = rand_matrix(size)
else:
    print("Invalid choice")

show_matrix(start_matrix)
#Какок размер, рандом или нет(две функции), функция показать матрицу , красивое меню