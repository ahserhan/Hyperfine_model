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


## Physical Model

The Hamiltonian includes the following interactions:

1. **Spin-Orbit Coupling (SOC)**: Coupling between electron spin and orbital angular momentum
2. **Iso-Orbital Coupling (IOC)**: Coupling between nuclear spin and orbital degree of freedom
3. **Strain/Jahn-Teller**: Static and dynamic Jahn-Teller effects
4. **Magnetic Field**: Applied to electron, nucleus, and orbital degrees of freedom

