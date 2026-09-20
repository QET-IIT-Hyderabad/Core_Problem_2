import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

# ----------------------------------------------------------------------
# Operators
# ----------------------------------------------------------------------
ket_0 = ___ # TODO
ket_1 = ___ # TODO

sx = ___ # TODO
sz = ___ # TODO

P0_op = ket_0 * ket_0.dag()
P1_op = ket_1 * ket_1.dag()

# Qubit Frequency:
w0 = 5


# ----------------------------------------------------------------------
# Helper Function: Build the Time Dependent Hamiltonian:
#   H(t) = (w0/2) sigma_z + (Omega0*cos(wd*t)/2)
#   H(t) = H0 + H1 * f(t)
# ----------------------------------------------------------------------
def build_hamiltonian(w0, Omega0, wd):
    H0 = ___ # TODO

    def drive_coefficient(t): # f(t)
        return ___ # TODO

    H1 = ___ # TODO

    return [H0, [H1, drive_coefficient]]


def run_sim(w0, psi0, Omega0, wd, t_max, n_points):
    """Solve the Schrodinger equation and return t, P0(t), P1(t)."""
    H = build_hamiltonian(w0, Omega0, wd)
    tlist = np.linspace(0, t_max, n_points)
    result = qt.sesolve(___, ___, tlist, e_ops=[P0_op, P1_op]) # TODO
    P0_t, P1_t = result.expect
    return tlist, P0_t, P1_t


# ========================================================================
# TASK 1 — No drive (Omega0 = 0), start in |0>
# ========================================================================
initial_state = ___ # TODO
Omega0 = ___ # TODO

t1, P0_no_drive, P1_no_drive = run_sim(w0 = w0, psi0=initial_state, Omega0 = Omega0, wd=0.0,
                                       t_max=3, n_points=2000)

plt.figure()
plt.plot(t1, P0_no_drive, label="P0(t)")
plt.plot(t1, P1_no_drive, label="P1(t)", linestyle="--")
plt.xlabel("time")
plt.ylabel("population")
plt.title("Task 1: No drive")
plt.legend()
plt.savefig("task1_no_drive.png", dpi=150)

# TODO: Explain the Physical Meaning of this Plot:
print("Your Explanation")

# ========================================================================
# TASK 2 — Resonant drive (wd = w0), Rabi oscillations
# ========================================================================
wd = ___ # TODO: Fill in resonance condition

Omega0 = 5
t2, P0_resonance, P1_resonance = run_sim(w0=w0, psi0=initial_state, Omega0=Omega0, wd=wd,
                                         t_max=15, n_points=6000)

plt.figure()
plt.plot(t2, P1_resonance)
plt.xlabel("time")
plt.ylabel("P1(t)")
plt.title("Task 2: Oscillations on resonance")
plt.savefig("task2_resonant_drive.png", dpi=150)

# TASK 2 Part 2 - Bit Flip Duration

# First time P1_resonance reaches its maximum (~1.0)
peak_idx = np.argmax(P1_resonance)
t_pi = t2[peak_idx]

print("TASK 2:")
print(f"Bit Flip Pulse duration: t_flip      = {t_pi:.4f}")
print(f"Theoretical Answer: t_flip           = {2*np.pi/Omega0:.4f}")

# TODO: Explain what the Driving Pulse' Amplitude Signifies
# Clue - Try changing Omega0 and check what your plots produce
print("Your Explanation")