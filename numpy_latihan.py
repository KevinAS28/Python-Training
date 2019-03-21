import numpy
a = numpy.array([1, 2, 3], ndmin=2, dtype=complex)
print(a)
b = numpy.array([1, 2, 3], dtype=complex, order='C')
print(b)
