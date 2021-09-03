import pandas as pd
import numpy as np

values, variables = 0, 0


def mean_data(arr):
    mean = list()

    global values, variables
    values, variables = arr.shape

    for i in range(variables):
        sum = 0.0
        for j in range(values):
            sum += arr[j][i]
        mean.append(sum / values)
    return np.array(mean)


def standard_deviation(arr, mean):
    s_deviation = np.zeros(mean.shape)
    for i in range(variables):
        sum = 0.0
        for j in range(values):
            sum += pow((arr[j, i] - mean[i]), 2)
        s_deviation[i] = pow((sum / values), 0.5)
    return s_deviation


def scaling(arr, s_deviation, mean):
    for i in range(variables):
        for j in range(values):
            arr[j, i] = (arr[j, i] - mean[i]) / s_deviation[i]


def covariance_matrix(arr, mean):
    cov_mat = np.identity(variables)  # uses determined mean to compute covariance matrix

    for i in range(variables):
        for k in range(variables):
            sum = 0.0
            for j in range(values):
                sum += (arr[j][i] - mean[i]) * (
                        arr[j][k] - mean[k])  # j is row here not i or k (was previously doing opposite)
            cov_mat[i][k] = sum / (values - 1)  # formula has -1 (not for population)
    return cov_mat


def correlation_matrix(cov_mat):
    cor_mat = np.zeros((variables, variables))  # zeros takes shape, not a square matrix dimension
    for i in range(variables):
        for j in range(variables):
            cor_mat[j][i] = cov_mat[j][i] / (pow(cov_mat[i][i], 0.5) * pow(cov_mat[j][j],
                                                                           0.5))  # use abs or else will get complex
            # no.(no need)
    return cor_mat


def orthogonalize(a):
    Q = np.zeros(a.shape)
    for i in range(a.shape[0]):
        Q[:, i] = a[:, i]
        for j in range(i):
            Q[:, i] -= ((scalar_multiplication(Q[:, i], Q[:, j])) / pow(magnitude(Q[:, j]), 2)) * Q[:, j]  # slicing
            # producing 1d array
    return Q


def scalar_multiplication(a, b):
    c = [float(a[i] * b[i]) for i in range(a.shape[0])]  # each number is of type numpy.float64 not float
    sum = 0.0
    for i in c:
        sum += i
    return sum


def magnitude(m):  # takes single column input (as vector)
    sum = 0.0
    for i in m:
        sum += i * i  # use zero index or else causes cartesian product
    return pow(sum, 0.5)


def unit_vectors(v):  # returns vectors of unit(column only) length from matrix,(magnitude function call included)
    for i in range(v.shape[0]):  # orthonormalization
        v[:, i] /= magnitude(v[:, i])
    return v


def matrix_multiplication(A, B):
    M = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(B.shape[1]):
            for j in range(A.shape[1]):
                M[i][k] += A[i][j] * B[j][k]
    return M


def hessenberg(A):
    i = 0
    size = A.shape[0]
    while i < size - 2:
        x = A[i + 1:, i]
        w = magnitude(x) * np.identity(x.shape[0])[:, 0]
        v = (np.subtract(w, x).reshape(x.shape[0], 1))
        temp = np.identity(x.shape[0]) - 2 * matrix_multiplication(v, np.transpose(v)) / pow(magnitude(v), 2)
        H = np.identity(size)
        H[i + 1:, i + 1:] = temp
        A = matrix_multiplication(A, H)
        A = matrix_multiplication(H, A)
        i += 1
    return A


def diagonal_subtraction(A, L_val):
    A = A.copy()
    for i in range(A.shape[0]):
        A[i, i] = A[i, i] - L_val
    return A


def echelon_form(B):
    for i in range(B.shape[0]):  # no return statement
        j = i
        while j < B.shape[0]:
            if abs(B[i][j]) < 0.001:
                B[i][j] = 0.0
                j += 1
            else:
                div = B[i][j]
                for k in range(B.shape[0]):
                    B[i][k] /= div
                for k in range(i + 1, B.shape[0]):
                    mul = B[k][j] / B[i][j]
                    for l in range(B.shape[0]):
                        B[k][l] -= B[i][l] * mul
                break


def find_vector(A):  # row echelon form input
    x = np.zeros(A.shape[0])
    for i in range(1, A.shape[0] + 1):
        if A[-i, -i] == 0:
            x[-i] = 1

        for j in range(1, i):
            x[-i] -= x[-j] * A[-i, -j]
    return x


def variance_ratio(A):
    ratio = np.zeros(A.shape[0])
    sum = 0.0
    for i in range(A.shape[0]):
        sum += A[i, i]
    for i in range(A.shape[0]):
        ratio[i] = (A[i, i] / sum) * 100
    return ratio


def QR_method(cov_mat):
    A = cov_mat.copy()
    A = hessenberg(A)
    k = 500  # what should be the value of k?
    for i in range(k):
        Q = orthogonalize(A)
        Q = unit_vectors(Q)  # orthonormal matrix required hence have to find the unit vectors
        A = matrix_multiplication(A, Q)
        A = matrix_multiplication(np.transpose(Q), A)
    return A
    # pd.DataFrame(A)


def eigen_vectors(cov_mat, A):
    eigvector_mat = np.zeros(A.shape)
    for i in range(A.shape[0]):
        B = diagonal_subtraction(cov_mat, A[i, i])
        echelon_form(B)
        eigvector_mat[:, i] = find_vector(B)
    return unit_vectors(eigvector_mat)


# def transform():


# def execution(arr):
#     mean = mean_data(arr)
#     s_deviation = standard_deviation(arr, mean)
#     scaling(arr, s_deviation, mean)
#     print(arr)
#     mean = mean_data(arr)
#     print(mean)  # New mean for standardised data
#     cov_mat = covariance_matrix(arr, mean)
#     print(cov_mat)
#     A = QR_method(cov_mat)
#     print(A)
#     eigvector = eigen_vectors(cov_mat, A)
#     print('\n\n\n')
#     print(pd.DataFrame(eigvector))


# arr = np.random.RandomState(42).rand(10,3)
# print(arr)
# main(arr)
# The code for