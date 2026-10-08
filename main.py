import numpy as np
from PIL import Image
import funcs as f

image = Image.open("pahan.jpg").convert("L")

matrix = np.array(image)

def reset_image(mat):
    mat = np.array(image)
    return mat


while True:
    print("""
    ==============================
           IMAGE EDITOR
    ==============================

    1. Открыть изображение
    2. Изменить яркость
    3. Изменить контрастность
    4. Инвертировать цвета
    5. Нормализовать изображение
    6. Размыть изображение
    7. Сбросить изменения
    8. Сохранить изображение


    0. Выход
    ==============================
    """)
    chs = int(input("Choose your choice: "))

    if chs == 1:
        Image.fromarray(matrix.astype(np.uint8)).show()
    elif chs == 2:
        number = int(input("Choose how much you want to change: "))
        matrix = f.change_brights_numpy(number, matrix)
    elif chs == 3:
        polzunok = int(input("Choose polzunok: "))
        matrix = f.change_contrast(matrix, polzunok)
    elif chs == 4:
        matrix = f.invert_color(matrix)
    elif chs == 5:
        matrix = f.normalization(matrix)
    elif chs == 6:
        matrix = f.blur_mat(matrix)
    elif chs == 7:
        matrix = reset_image(matrix)
    elif chs == 8:
        Image.fromarray(matrix.astype(np.uint8)).save("pahan_edited.jpg")
    elif chs == 0:
        print("Quited")
        break

