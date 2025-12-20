from numpy.lib.mixins import NDArrayOperatorsMixin
import numpy as np
import numbers

class PropertyValueMixin:
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class StrPrintMixin:
    def __str__(self):
        return str(self.value)


class WriteFileMixin:
    def write_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

class Arithmetic(NDArrayOperatorsMixin,StrPrintMixin,WriteFileMixin,PropertyValueMixin):
    _HANDLED_TYPES = (np.ndarray, numbers.Number)
    def __init__(self, value):
        self.value = np.asarray(value)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(
                x, self._HANDLED_TYPES + (Arithmetic,)
            ):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, Arithmetic) else x
                    for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Arithmetic) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)


def main():
    np.random.seed(0)

    matrix1 = Arithmetic(np.random.randint(0, 10, (10, 10)))
    matrix2 = Arithmetic(np.random.randint(0, 10, (10, 10)))

    result_add =  matrix1 + matrix2
    result_mul =  matrix1 * matrix2
    result_matmul =  matrix1 @ matrix2

    result_add.write_file('matrix+.txt')
    result_mul.write_file('matrix*.txt')
    result_matmul.write_file('matrix@.txt')

if __name__ == "__main__":
    main()

