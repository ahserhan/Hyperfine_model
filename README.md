# Hyperfine Model for SnV117 Center in Diamond

This repository contains a Hamiltonian model for the SnV117 (117SnV⁻) defect center in diamond, implemented using QuTiP. The model includes spin-orbit coupling, hyperfine interactions, strain effects, and dynamic Jahn-Teller effects.

## Overview

The SnV117 center is a spin-1/2 electron system with a spin-1/2 nuclear spin (from ¹¹⁷Sn). This model provides a comprehensive description of the energy structure and optical transitions for both ground and excited states.

## Files

- **`hamiltonian_DJT.py`**: Main Hamiltonian implementation with functions for:
  - Creating the full Hamiltonian including SOC, IOC, strain, Jahn-Teller, magnetic field, and hyperfine coupling
  - Solving the Hamiltonian for energy eigenvalues and eigenstates
  - Calculating PLE (Photoluminescence Excitation) transitions and spectra
  - Computing cyclicity (spin preservation probability) for transitions

- **`parameters_DJT.py`**: Physical parameters for the SnV117 center:
  - Spin values (electron S=1/2, nuclear Sn=1/2)
  - Orbital magnetic field susceptibilities (ground and excited states)
  - Spin-orbit coupling strengths
  - Hyperfine coupling parameters in DJT form (A₁, A₂, A∥, A⊥) for both ground and excited states

- **`SnV117_energy_structure.ipynb`**: Jupyter notebook with examples demonstrating:
  - Energy level structure vs. magnetic field strength
  - Energy levels vs. magnetic field direction (θ sweep)
  - Energy levels vs. strain parameter α
  - Spin labeling using |F, Fz⟩ notation

## Dependencies

- Python 3.x
- NumPy
- QuTiP
- Matplotlib
- Jupyter (for the notebook)

Install dependencies with:
```bash
pip install numpy qutip matplotlib jupyter
```

## Usage

### Basic Example

```python
import numpy as np
import hamiltonian_DJT as ham
import parameters_DJT as params

# Magnetic field parameters
B = np.linspace(0, 0.56, 200)  # [GHz]
theta = 0  # polar angle [rad]
phi = 0    # azimuthal angle [rad]

# Solve ground state Hamiltonian
E_gnd, Eref_gnd, U, U_states, alignment = ham.solve_hamiltonian(
    B, theta, phi,
    alpha=50,  # strain parameter [GHz]
    beta=0     # strain parameter [GHz]
)
```

### PLE Spectrum Calculation

```python
# Calculate PLE transitions
f_meas = np.linspace(1080, 1090, 1000)  # frequency array [GHz]
eta = [1, 0, 1]  # polarization vector [px, py, pz]

PLE = ham.PLE_spectrum(
    f_meas, B, theta, phi, eta,
    intensity=1.0,
    lw=0.080  # linewidth [GHz]
)
```

## Physical Model

The Hamiltonian includes the following interactions:

1. **Spin-Orbit Coupling (SOC)**: Coupling between electron spin and orbital angular momentum
2. **Iso-Orbital Coupling (IOC)**: Coupling between nuclear spin and orbital degree of freedom
3. **Strain/Jahn-Teller**: Static and dynamic Jahn-Teller effects
4. **Magnetic Field**: Applied to electron, nucleus, and orbital degrees of freedom
5. **Hyperfine Coupling**: Electron-nuclear spin interaction in DJT form with parameters A₁, A₂, A∥, A⊥

The tensor product structure is: **orbital ⊗ electron ⊗ nuclear**

## Parameters

The parameters are based on experimental measurements from:
- Reduction parameters: [Phys. Rev. X 8, 021063 (2018)](https://doi.org/10.1103/PhysRevX.8.021063)
- Hyperfine parameters: [10.1103/fq19-lfmv](https://doi.org/10.1103/fq19-lfmv)

## References

1. Reduction parameters for ¹¹⁷SnV⁻ defect center: [Phys. Rev. X 8, 021063 (2018)](https://doi.org/10.1103/PhysRevX.8.021063)
2. Hyperfine parameters for ¹¹⁷SnV⁻ defect center: [10.1103/fq19-lfmv](https://doi.org/10.1103/fq19-lfmv)

## License

This code is provided for research purposes.
