import numpy as np
import argparse
from hva import _hva

def network(ts):
    n = len(ts)
    A = np.zeros((n, n), int)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if j == i + 1:
                A[i, j] = 1
            elif j > i + 1:
                if np.amax(ts[i + 1:j]) < np.amin([ts[i], ts[j]]):
                    A[i, j] = 1
            if ts[j] >= ts[i]:
                break
    return A + np.transpose(A)

def network_optim(ts):
    """
    Function to calculate horizontal visiblity graph matrix from a
    1D-timeseries.
    Inputs:
    :param ts: 1xN Float64/double numpy array of the time series.

    Outputs:
    :return: NxN matrix of nodes and edges
    :rtype: NxN int8 numpy array
    """
    x = ts
    N = len(ts)
    A = np.zeros((N, N), dtype="int8")

    _hva(x, N, A)
    return A

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process time series data using HVA.')
    parser.add_argument('ts_len', metavar='N', type=int,
                        help='Number of time series points')
    parser.add_argument('--test', action='store_true',
                        help="Check both methods return same matrix")
    args = parser.parse_args()
    ts = np.random.randn(args.ts_len)

    if args.test:
        print(np.all(network(ts) == network_optim(ts)))
