"""Box occupancies for a finite real spectrum."""
import numpy as np


def BoxCountingE(E, N):
    """Return N occupancies and their left edges over [min(E), max(E)].

    Bins are left-closed and right-open, except the last bin includes max(E).
    Input order does not matter. For a constant spectrum NumPy expands the
    zero-width range by 0.5 on each side before making the bins.
    """
    if np.iscomplexobj(E):
        raise ValueError("E must be real-valued")
    values = np.asarray(E, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("E must be a non-empty one-dimensional spectrum")
    if not np.all(np.isfinite(values)):
        raise ValueError("E must contain only finite values")
    if isinstance(N, (bool, np.bool_)) or not isinstance(N, (int, np.integer)) or N <= 0:
        raise ValueError("N must be a positive integer")

    counts, edges = np.histogram(values, bins=N)
    return counts.tolist(), edges[:-1].tolist()


def GetNb(data, q=0.001):
    """Sum count**q over occupied boxes; q=0 counts the occupied boxes.

    The historical default q is retained. Empty boxes do not contribute,
    including for q <= 0.
    """
    counts = np.asarray(data, dtype=float)
    if counts.ndim != 1 or not np.all(np.isfinite(counts)) or np.any(counts < 0):
        raise ValueError("data must be a one-dimensional array of finite non-negative counts")
    if not np.isfinite(q):
        raise ValueError("q must be finite")
    return float(np.sum(counts[counts > 0] ** q))


def HistPlot(data, E_all):
    # Plotting is optional when importing the numerical functions.
    from matplotlib import pyplot as plt
    plt.plot(E_all, data)
    plt.show()


# Benchmark
if __name__ == "__main__":
    E = np.linspace(1, 100, 2000)
    N = 10
    data, E_all = BoxCountingE(E, N)
    print(data, E_all)
    HistPlot(data, E_all)

