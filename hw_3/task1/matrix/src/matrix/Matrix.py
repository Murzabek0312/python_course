# cursor: disable
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix =  matrix

    def __add__(self, right):
        self.__check_matrix_size(right)
        return Matrix(self.matrix + right.matrix)

    def __mul__(self, right):
        self.__check_matrix_size(right)
        return Matrix(self.matrix * right.matrix)

    def __matmul__(self, right):
        if self.matrix.shape[1] != right.matrix.shape[0]:
            raise ValueError(
                f"Некорректные размеры матриц для матричного умножения: "
                f"{self.matrix.shape} @ {right.matrix.shape}. "
                f"Число столбцов первой ({self.matrix.shape[1]}) должно равняться "
                f"числу строк второй ({right.matrix.shape[0]})"
            )
        return Matrix(self.matrix @ right.matrix)

    def __check_matrix_size(self, right):
        if self.matrix.shape != right.matrix.shape:
            raise ValueError(
                f"Некорректные размеры матриц: {self.matrix.shape} и {right.matrix.shape}")

def main():
    np.random.seed(0)

    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    result_add =  matrix1 + matrix2
    result_mul =  matrix1 * matrix2
    result_matmul =  matrix1 @ matrix2

    np.savetxt('matrix+.txt', result_add.matrix, fmt='%d')
    np.savetxt('matrix*.txt', result_mul.matrix, fmt='%d')
    np.savetxt('matrix@.txt', result_matmul.matrix, fmt='%d')

if __name__ == "__main__":
    main()
