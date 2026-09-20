# QET Core Selection - Problem Statement 2: Driven Qubit Simulator (Rabi Oscillations)

## Task

A qubit is described by the state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, 
evolving under the Schrödinger Equation 
$$H|\psi\rangle = i\hbar \frac{d|\psi\rangle}{dt} $$

You are given a qubit with a natural (bare) frequency $\omega_0$, sitting under an external
oscillating drive of amplitude $\Omega_0$ and frequency $\omega_d$:

$$H(t) = \frac{\omega_0}{2}\sigma_z + \frac{\Omega_0 \cos(\omega_d t)}{2}\sigma_x$$

where

$$\sigma_z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}, \qquad \sigma_x = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$$

The $\sigma_z$ term is the qubit spinning at its own natural frequency;
the $\sigma_x$ term is an external control field that can flip the qubit between $|0\rangle$ and $|1\rangle$.
Your job is to simulate a bit flip using this system and characterize how the qubit responds to being driven.

Implement a **driven qubit simulator** using **QuTiP** 
(plus NumPy and Matplotlib; no Qiskit or other quantum circuit libraries). 
Fill in the template in [`driven_qubit_simulator.py`](./qubit_drive_simulator.py). Your simulator must support:

- Building the time-dependent Hamiltonian $H(t)$ above for arbitrary $\omega_0, \Omega_0, \omega_d$.
- Solving the Schrödinger equation for the resulting statevector and returning the populations $P_0(t) = |\langle 0|\psi(t)\rangle|^2$ and $P_1(t) = |\langle 1|\psi(t)\rangle|^2$.

### Task 1 — Free Evolution

Set $\Omega_0 = 0$ and start the qubit in $|0\rangle$. Plot $P_0(t)$ and $P_1(t)$, and explain in one or two sentences what is physically happening (and why it makes sense given $H(t)$ with no drive).

### Task 2 — Resonant Drive and the Bit-Flip Duration

Set the drive on resonance, $\omega_d = \omega_0$. Plot $P_1(t)$ — these are the Rabi oscillations.
From your simulated data (not by hand-deriving it), numerically extract the **bit-flip (π-pulse) duration**: 
the first time $P_1(t)$ reaches its maximum ($\approx 1$). 
Compare this against the theoretical value $t_{\text{flip}} = 2\pi/\Omega_0$.
Also explain, in one or two sentences, what the drive amplitude $\Omega_0$ physically controls. Try changing $\Omega_0$ and observing what happens to your plots before answering.

### Running your code

Running

```bash
uv run qubit_drive_simulator.py
```

should execute both tasks end-to-end and save `task1_no_drive.png` and `task2_resonant_drive.png`, along with printing the bit-flip duration (measured vs. theoretical) and your written explanations.

## Rules

- Only **NumPy**, **Matplotlib**, and **QuTiP** are allowed (no Qiskit, PennyLane, etc., and frankly, they're not needed for this as well).
- Your simulator must work for **arbitrary** $\omega_0$, $\Omega_0$, and $\omega_d$ — don't hardcode logic that only works for the specific values used in Task 1/Task 2.
- The statevector must remain normalized after every step of the evolution.

## Setting Up

### Repository

1. Clone this repository:

   ```bash
   git clone <repo-url>
   ```

2. Create a **private** repository of your own named `QET_{RollNo}_PROBLEM_{1/2}` depending on which problem statement you picked. For example, `QET_EP24BTECH11026_PROBLEM_2`.
   - [Creating a new repository (GitHub Docs)](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
   - [Setting repository visibility to private (GitHub Docs)](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

3. Share access to your private repository with one of the heads:
   - [Inviting collaborators to a personal repository (GitHub Docs)](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)

### Commit Guidelines

- Commit early and often; your commit history is part of the evaluation.
- Write clear, descriptive commit messages (what changed and why).
- [How to write a good commit message](https://cbea.ms/git-commit/)
- [GitHub Git cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/)

### Environment

We require you to use **uv** for environment and dependency management. This repository already contains a `uv.lock`, so setup is:

1. Install uv: [uv installation](https://docs.astral.sh/uv/getting-started/installation/)
2. Create the environment and install dependencies:

   ```bash
   uv sync
   ```

3. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

- [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html)

## Learning Resources

### Quantum Computing Basics

- IBM Quantum lectures:
  - [Lecture 1](https://www.youtube.com/watch?v=3-c4xJa7Flk&list=PLOFEBzvs-VvqKKMXX4vbi4EB1uaErFMSO&index=3)
  - [Lecture 2](https://www.youtube.com/watch?v=DfZZS8Spe7U&list=PLOFEBzvs-VvqKKMXX4vbi4EB1uaErFMSO&index=4)

### Quantum Mechanics, Rabi Oscillations and Driven Two-Level Systems

- [Qubit (Wikipedia)](https://en.wikipedia.org/wiki/Qubit)
- [Rabi cycle (Wikipedia)](https://en.wikipedia.org/wiki/Rabi_cycle)

These should be sufficient, but if you're looking for advanced references:

Advanced References: 
- [Daniel Steck, *Quantum and Atom Optics* — see the "Two-Level Atom" chapter for Rabi flopping, the RWA, and π/π-2 pulses](https://atomoptics.uoregon.edu/~dsteck/teaching/quantum-optics/quantum-optics-notes.pdf)
- Nielsen & Chuang, Ch. 7.5–7.7 (Control of a two-level system) is also a useful reference if you have access to the text.

### QuTiP

- [QuTiP documentation](https://qutip.readthedocs.io/)
- [Time-dependent Hamiltonians in QuTiP (List Format:`[H0, [H1, coeff(t)]]`, `sesolve`)](https://qutip.readthedocs.io/en/latest/guide/dynamics/dynamics-time.html)
- [QuTiP tutorials](https://qutip.org/qutip-tutorials/)

## Submission

Push your completed solution to your private `QET_{RollNo}_PROBLEM_{1/2}` repository and make sure the head you were assigned has collaborator access before the deadline.