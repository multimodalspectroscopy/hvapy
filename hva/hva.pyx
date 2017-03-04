cimport cython

import numpy as np
cimport numpy as np

ctypedef np.int8_t INT8TYPE_t
ctypedef np.float64_t FLOAT64TYPE_t


def _hva(
    np.ndarray[FLOAT64TYPE_t, ndim=1] x,
    int N, np.ndarray[INT8TYPE_t, ndim=2] A):

    cdef:
        int i, j, k
        float minimum

    for i in range(N-2):
        for j in range(i+2, N):
            k = i + 1
            minimum = min(x[i], x[j])

            while x[k] < minimum and k < j:
                k += 1

            if k == j:
                A[i, j] = A[j, i] = 1

    # Add trivial connections of subsequent observations in time series
    for i in range(N-1):
        A[i, i+1] = A[i+1, i] = 1
