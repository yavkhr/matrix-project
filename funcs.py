
import numpy as np


def change_contrast(mat, polzunok):
    if polzunok < 0:
        polzunok = 0
    res  = np.round((mat - 127.5) * polzunok + 127.5)
    res = np.where(res > 255, 255, res)
    res = np.where(res < 0, 0, res)
    return res.astype(np.uint8)


def change_brights_numpy(number, mat):
    result = mat.astype(np.int16) + number
    result = np.where(result > 255, 255, result)
    result = np.where(result < 0, 0, result)
    return result.astype(np.uint8)


def normalization(mat):
    mat_min = np.min(mat)
    mat_max = np.max(mat)
    if mat_min == mat_max:
        mat_norm = ((mat - mat_min) / (mat_max - mat_min) ) * 255
    return mat_norm

def invert_color(mat):
    new_mat = 255 - mat
    return new_mat

def blur_mat(mat):
    new_mat = mat.copy()
    for i in range(1, mat.shape[0] - 1):
        for j in range(1, mat.shape[1] - 1):
            area = mat[i-1:i+2, j-1:j+2]
            new_mat[i][j] = np.mean(area)
    return new_mat