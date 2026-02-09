"""
Parameters for SnV117 center in diamond (for use with DJT Hamiltonian).
Reduction parameters are for the 117SnV- defect center from paper 10.1103/PhysRevX.8.021063.
hyperfine parameters are for the 117SnV- defect center from paper 10.1103/fq19-lfmv.
Hyperfine parameters use the DJT form with A1, A2, A_parallel, A_perpendicular.
"""

# Spin values
S = 1/2  # Electron spin
Sn = 1/2  # Nuclear spin (117Sn)

# Orbital magnetic field susceptibility
q = 0.328 * 0.471 # [] ground state orbital magnetic field susceptibility
q_exc = 0.782 * 0.125  # [] excited state orbital magnetic field susceptibility

# Spin-orbit coupling
L = 830.0  # [GHz] spin-orbit coupling ground state
L_exc = 3000.0  # [GHz] spin-orbit coupling excited state

# Hyperfine Properties
# Ratio of electron to proton mass
rmep = 5.44617021e-4
# Ratio of nuclear/electron gyromagnetic ratio (assuming g~2 for electrons)
rg = 2.00208 * rmep / 2

# Ground state hyperfine parameters (117Sn, S_n = 1/2)
# DJT form: A1, A2, A_parallel, A_perpendicular
# A1_gnd = 0 / 1000.0      # [GHz] test
# A2_gnd = 0 / 1000.0      # [GHz] test
A1_gnd = 1.1 / 1000.0      # [GHz] off-diagonal hyperfine coupling A1 (1.1 MHz)
A2_gnd = 1.9 / 1000.0      # [GHz] off-diagonal hyperfine coupling A2 (1.9 MHz)
Apar_gnd = 488.0 / 1000.0  # [GHz] parallel hyperfine coupling A∥ (488.0 MHz)
Aperp_gnd = 1029.7 / 1000.0  # [GHz] perpendicular hyperfine coupling A⊥ (1029.7 MHz)

# Excited state hyperfine parameters (117Sn, S_n = 1/2)
# DJT form: A1, A2, A_parallel, A_perpendicular
# A1_exc = 0 / 1000.0      # [GHz] test
# A2_exc = 0 / 1000.0      # [GHz] test
A1_exc = 0.1 / 1000.0      # [GHz] off-diagonal hyperfine coupling A1 (0.1 MHz)
A2_exc = -0.43 / 1000.0    # [GHz] off-diagonal hyperfine coupling A2 (-0.43 MHz)
Apar_exc = 15.0 / 1000.0   # [GHz] parallel hyperfine coupling A∥ (15.0 MHz)
Aperp_exc = 32.3 / 1000.0  # [GHz] perpendicular hyperfine coupling A⊥ (32.3 MHz)
