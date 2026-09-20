# NumPy Reference for the Statevector Simulator

A short list of NumPy functions you will likely need, with syntax examples. This is not exhaustive, and you are free to use any other NumPy functionality.

## Array Creation

```python
import numpy as np

np.zeros(2**n, dtype=complex)        # zero vector (use for the initial |0...0> state)
np.eye(2, dtype=complex)             # 2x2 identity matrix
np.array([[0, 1], [1, 0]], dtype=complex)   # explicit matrix, e.g. the X gate
```

## Combining Matrices (Tensor Products)

```python
np.kron(A, B)                        # Kronecker (tensor) product of two matrices
# Example: X on qubit 0 of a 2-qubit system (qubit 1 untouched):
U = np.kron(X, np.eye(2))
```

## Reshaping the Statevector

```python
psi.reshape(2**s, 2**(n - s))        # statevector -> coefficient matrix a (for SVD)
a.reshape(-1)                        # flatten a matrix back into a vector
```

## Applying Gates

```python
psi = U @ psi                        # matrix-vector multiplication (also: np.dot(U, psi))
np.einsum('ij,j->i', U, psi)         # same thing via Einstein summation
```

## SVD and Entropy

```python
U, lambdas, Vdagger = np.linalg.svd(a)          # singular value decomposition
prob = lambdas**2                                # eigenvalues of the reduced density matrix
prob = prob[prob > 0]                            # drop zeros (0 * log 0 = 0)
S = -np.sum(prob * np.log2(prob))                # von-Neumann entropy in bits
```

## Useful Utilities

```python
np.abs(psi) ** 2                     # measurement probabilities
np.argmax(probabilities)             # index of the most likely basis state
np.conj(U)                           # complex conjugate
U.conj().T                           # conjugate transpose (dagger)
np.isclose(a, b)                     # floating-point safe comparison
np.allclose(A, B)                    # ... for arrays
```
