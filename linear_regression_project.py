# coding: utf-8
# 本项目要求矩阵统一使用二维列表表示，如下：
A = [[1,2,3],
     [2,3,3],
     [1,2,5]]

B = [[1,2,3,5],
     [2,3,3,5],
     [1,2,5,1]]

#TODO 创建一个 4*4 单位矩阵
def identity_matrix(n):
    I = [0] * n
    for i in range(0, n):
        I[i] = [0]*n
        I[i][i] = 1
    return I
print identity_matrix(4)

# 使用len直接获取矩阵的行和列数

def shape(M):
    i = len(M)
    j = len(M[0])
    return i,j
