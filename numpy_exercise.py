import numpy as np

if __name__ == "__main__":
    a = np.zeros(10)
    a[4] = 1
    print(a)
    print(np.arange(10, 100, 1))
    print(np.arange(9).reshape(3, 3))
    print(np.nonzero([1, 2, 0, 0, 4, 0]))
    print(np.eye(4))
    a = np.random.random((10, 10))
    print(a)
    min, max = np.min(a), np.max(a)
    print(min, max)
    print(np.tile(np.array([[0, 1], [1, 0]]), (4, 4)))
    Z = np.random.random((5, 5))
    min, max = np.min(Z), np.max(Z)
    # min max normalization
    Z = (Z - min) / (max - min)
    A = np.arange(15).reshape(5, 3)
    B = np.arange(6).reshape(3, 2)
    print("---------------------------")
    print(A, B, np.dot(A, B), A.dot(B))
    a = np.arange(10)
    print(np.tile(a, (10, 1)))
    print("---------------------------")
    Z = np.zeros((10, 10))
    print(Z)
    Z += np.arange(10)
    print(Z)
    print(np.linspace(0, 1, 1002)[1:-1])
    a = np.random.random((100))
    np.sort(a)
    print("---------------------------")
    A = np.random.randint(0, 2, (2, 2))
    B = np.random.randint(0, 2, (2, 2))
    print(np.allclose(A, B))
    Z = np.random.random(1000)
    print(Z.mean())
    print(np.mean(Z))

    Z = np.random.random((100, 2))
    X, Y = Z[:, 0], Z[:, 1]
    print(np.sqrt(X**2 + Y**2))
    print(np.arctan2(Y, X))

    Z = np.zeros((10, 10), [("x", float), ("y", float)])
    print(Z)

    Z["x"], Z["y"] = np.meshgrid(np.linspace(0, 1, 10), np.linspace(0, 1, 10))
    print(Z["x"], Z["y"], Z)
    print("---------------------------")

    for dtype in [np.int8, np.int32, np.int64]:
        print(np.iinfo(dtype).min)
        print(np.iinfo(dtype).max)

    for dtype in [np.float32, np.float64]:
        print(np.finfo(dtype).min)
        print(np.finfo(dtype).max)
        print(np.finfo(dtype).eps)

    Z = np.zeros(
        10,
        [
            ("position", [("x", float, (1,)), ("y", float, (1,))]),
            ("color", [("r", float, (1,)), ("g", float, (1,)), ("b", float, (1,))]),
        ],
    )
    print(Z)

    Z = np.random.random((10, 2))
    X, Y = np.atleast_2d(Z[:, 0]), np.atleast_2d(Z[:, 1])
    D = np.sqrt((X - X.T) ** 2 + (Y - Y.T) ** 2)

    sigma, mu = 1.0, 0.0
    G = np.exp(-((D - mu) ** 2 / (2.0 * sigma**2)))
    print(G)

    Z = np.array([1, 2, 3, 4, 5])
    Z0 = np.zeros(len(Z) * 4 - 1)
    Z0[::4] = Z
